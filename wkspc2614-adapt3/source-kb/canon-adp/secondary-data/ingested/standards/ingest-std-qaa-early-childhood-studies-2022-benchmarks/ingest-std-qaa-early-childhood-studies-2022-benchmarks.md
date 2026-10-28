---
id: std:doc:qaa-early-childhood-studies-2022-benchmarks
title: "Subject Benchmark Statement Early Childhood Studies"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100457", label: "early childhood studies", basis: "stated" }
  - { scheme: "cah", code: "CAH15-04-02", label: "childhood and youth studies", basis: "inferred" }
edition: "March 2022 (fourth edition)"
published: 2022-03
status: current
supersedes: "the third edition (2019), as the back matter states; earlier editions 2014 and 2007"
heldText: { method: sha256-bytes, raw: c45f8fb44d2278bd09400a0ad048647528c8386df892551bc5b5de599a4e37c6, normalised: 9bda721f1210f23d31c4505816ef3bc0d84e6fa2ebaf4b280ce60993c6a00a1a }
heldTextStan: { method: sha256-stan, raw: c45f8fb44d2278bd09400a0ad048647528c8386df892551bc5b5de599a4e37c6, normalised: 0404c5a31ece1fc7beb03890064a27e3a846cc9cd4c8d1b3ff091839f38b4e58 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2022 revision (fourth edition for this subject)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0100 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:17"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Early Childhood Studies (QAA, March 2022)

> Run 0100, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2022-early-childhood-studies-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in Early Childhood Studies, the interdisciplinary study of children from conception to eight, should know and be able to do: its subject-specific and generic skill lists and a four-column table of standards (threshold, typical, excellent and postgraduate), each column headed by a degree class. Reach for it when designing, reviewing or describing an early childhood course, its outcomes or its placements. It is not a curriculum, not the degrees network's graduate practitioner competencies and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2022 as the fourth edition, the statement sets out the context and purposes of the subject, its distinctive features (design, accessibility, progression, flexibility, partnership, monitoring and review), its content, skills, teaching, learning and assessment, and benchmark standards for the bachelor's degree with honours at threshold (third class), typical (lower to upper second) and excellent (first) standards, with a fourth postgraduate column for master's study. It carries three cross-cutting themes (equality, diversity and inclusion; education for sustainable development; entrepreneurship and enterprise education, with employability) and a section on accessibility, cites the FHEQ and FQHEIS at levels 6/10 and 7/11, and sets the subject beside the Early Childhood Studies Degrees Network and its optional Level 6 graduate practitioner competencies. The held text also carries the network's 2026 competencies document as an appendix, excluded here (Part E).

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Early Childhood Studies"
edition: "March 2022 (fourth edition)"
dates:
  published: 2022-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement; in England not a sector-recognised standard under the OfS framework; a key reference point in Wales (Quality Assessment Framework for Wales) and Scotland (Quality Enhancement Framework); part of quality requirements in Northern Ireland (D1, front matter: Relationship to legislation and regulation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2022", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what an Early Childhood Studies graduate can be expected to know, do and understand at the end of their studies, and the nature and characteristics of awards in the subject, with standards for honours and postgraduate study (D1, front matter: About this Statement; 1.16; 4.1)"
appliesTo:
  awards: ["bachelor's with honours", "master's", "foundation degrees, top-ups and doctorates named as courses it can apply to (1.6, 2.15, 4.2)"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"T he ECS Subject Benchmark Statement can apply to the full range of degree courses offered within early childhood, which can include foundation degrees; BA (Hons) t op ups as a progression from f oundation degrees; BA (Hons) full or part-time degrees; master’s and doctorate provision.\" (D1, 1.6)"
statedSubjects:
  - { name: "Early Childhood Studies", locator: "(D1, title; 1.1; 1.2)", kind: "subject", codes: [{ scheme: "hecos", code: "100457", label: "early childhood studies" }, { scheme: "cah", code: "CAH15-04-02", label: "childhood and youth studies" }] }
  - { name: "childhood studies degrees", locator: "(D1, 4.2)", kind: "programme title", codes: [{ scheme: "hecos", code: "100456", label: "childhood studies" }] }
  - { name: "foundation degrees; BA (Hons) top-ups; BA (Hons) full or part-time; master's and doctorate provision", locator: "(D1, 1.6; 2.15; 4.2)", kind: "programme title", codes: [{ scheme: "hecos", code: "100457", label: "early childhood studies" }] }
  - { name: "Early Childhood Graduate Practitioner Competencies (Level 6)", locator: "(D1, 1.6; 1.18 to 1.20; 2.20; 2.25)", kind: "specialism", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "the first degrees in 1992 and the period the field covers" }
  - { number: "1.2", order: 4, componentType: area, parent: "section 1", heading: "Context", gloss: "an established discipline drawing on many fields" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "graduate careers and further study" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "graduates as advocates for children and families" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "contested knowledge, social justice and sustainability" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "the courses the statement can serve; the practitioner competencies" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes of an Early Childhood Studies degree", gloss: "the underlying aim: critical study of research and practice" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes of an Early Childhood Studies degree", gloss: "social justice, holistic development and play" }
  - { number: "1.9", order: 11, componentType: area, parent: "section 1", heading: "Purposes of an Early Childhood Studies degree", gloss: "sociocultural context and holism in course structures" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes of an Early Childhood Studies degree", gloss: "professionalism and multi-professional practice" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes of an Early Childhood Studies degree", gloss: "students as agents of change" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Purposes of an Early Childhood Studies degree", gloss: "many perspectives on childhood and rights" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Purposes of an Early Childhood Studies degree", gloss: "research, enquiry and reflexivity" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Early Childhood Studies degree", gloss: "shared characteristics of courses" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Early Childhood Studies degree", gloss: "a base for postgraduate study" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Early Childhood Studies degree", gloss: "the standards as the floor for bachelor's and master's graduates" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Early Childhood Studies degree", gloss: "four nations and mapping to national requirements" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Early Childhood Studies degree", gloss: "the practitioner competencies and network membership" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Early Childhood Studies degree", gloss: "competencies through assessed placements; not expected of every degree" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Early Childhood Studies degree", gloss: "practising in early years settings: the nation's rules" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Early Childhood Studies degree", gloss: "language requirements where English is not the first language" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Early Childhood Studies degree", gloss: "varied approaches; a range of perspectives" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI vision: questioning dominant thought" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI mission: teaching that challenges dominant knowledge" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "equitable courses; placements and the age range" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "conditions for work-based and placement learning" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ESD vision: ecological study of early childhood" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ESD mission: sustainability through holistic development" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ESD as an aspirational process" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ESD as curriculum design" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainability, citizenship and advocacy in degrees" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "enterprise vision: challenging inequality, building relationships" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "enterprise mission: innovation and social value" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "research and practice informing each other" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "enterprising behaviours and attributes" }
  - { number: "1.36", order: 38, componentType: stem, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "opportunities to build enterprise skills" }
  - { number: "2.1", order: 40, componentType: area, parent: "section 2", heading: "Design - defining principles", gloss: "conception to eight and holistic development" }
  - { number: "2.2", order: 41, componentType: area, parent: "section 2", heading: "Design - defining principles", gloss: "interdisciplinarity and pedagogical approaches" }
  - { number: "2.3", order: 42, componentType: paragraph, parent: "section 2", heading: "Design - defining principles", gloss: "many perspectives and critical evaluation" }
  - { number: "2.4", order: 43, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "inclusive, accessible course design" }
  - { number: "2.5", order: 44, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "entry routes and modes of delivery" }
  - { number: "2.6", order: 45, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "digital inclusion and employability" }
  - { number: "2.7", order: 46, componentType: practice, parent: "section 2", heading: "Accessibility", gloss: "varied delivery and placement settings" }
  - { number: "2.8", order: 47, componentType: practice, parent: "section 2", heading: "Accessibility", gloss: "accessible, varied, authentic assessment" }
  - { number: "2.9", order: 48, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "assessment pitched at the level of study" }
  - { number: "2.10", order: 49, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "accessible spaces for reflection and debate" }
  - { number: "2.11", order: 50, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression year by year to honours" }
  - { number: "2.12", order: 51, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint honours" }
  - { number: "2.13", order: 52, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's, exit awards and Scottish degrees" }
  - { number: "2.14", order: 53, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "design for reflection and balance across disciplines" }
  - { number: "2.15", order: 54, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "courses served and doctoral progression" }
  - { number: "2.16", order: 55, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "suites of qualifications and placement design" }
  - { number: "2.17", order: 56, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible modes of study" }
  - { number: "2.18", order: 57, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "theory with practice; statutory and regulatory requirements" }
  - { number: "2.19", order: 58, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership across disciplines and places" }
  - { number: "2.20", order: 59, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "competencies, openness to applicants and the nations" }
  - { number: "2.21", order: 60, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.22", order: 61, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "externality in review" }
  - { number: "2.23", order: 62, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examining" }
  - { number: "2.24", order: 63, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "what external examiners need" }
  - { number: "2.25", order: 64, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation and network membership" }
  - { number: "3.1", order: 66, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "subject-specific and generic skills defined" }
  - { number: "3.2", order: 67, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "the split between kinds of skill is not sharp" }
  - { number: "3.3", order: 68, componentType: stem, parent: "section 3", heading: "Subject-specific skills", gloss: "subject-specific skills of an honours graduate" }
  - { number: "3.4", order: 69, componentType: stem, parent: "section 3", heading: "Generic skills", gloss: "generic skills of an honours graduate" }
  - { number: "3.5", order: 70, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "what teaching and learning are designed to do" }
  - { number: "3.6", order: 71, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "growing self-directed learning" }
  - { number: "3.7", order: 72, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "independent and group study" }
  - { number: "3.8", order: 73, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "reflecting on childhood experience, with support" }
  - { number: "3.9", order: 74, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "engagement with practice in teaching and learning" }
  - { number: "3.10", order: 75, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "mentoring for assessed professional practice" }
  - { number: "3.11", order: 76, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "culturally responsive, inclusive teaching" }
  - { number: "3.12", order: 77, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment tied to objectives; reasonable adjustments" }
  - { number: "3.13", order: 78, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "the range of assessment methods" }
  - { number: "3.14", order: 79, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment of practice; inclusive criteria" }
  - { number: "3.15", order: 80, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessing professional practice" }
  - { number: "3.16", order: 81, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "range of assessment and depth of feedback" }
  - { number: "4.1", order: 83, componentType: stem, parent: "section 4", heading: "Benchmark standards", gloss: "four categories of standard" }
  - { number: "4.2", order: 84, componentType: paragraph, parent: "section 4", heading: "Benchmark standards", gloss: "how the standards are phrased; who may use them" }
  - { number: "4.3", order: 85, componentType: paragraph, parent: "section 4", heading: "Benchmark standards", gloss: "every graduate gains a measure of the skills" }
  - { number: "4.4", order: 86, componentType: paragraph, parent: "section 4", heading: "Benchmark standards", gloss: "skills need not be shown one by one; the standards table follows" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of an Early Childhood Studies degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of an Early Childhood Studies degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, teaching, learning and assessment", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points", kind: "other: front matter, read for S1, S2, SB5 and SB6" }
  - { number: "none", heading: "section heading lines (sections 1 to 4)", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter; professional organisations listed (Part E)" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for Early Childhood Studies", kind: "other: back matter; read for the edition history (S8)" }
  - { number: "Appendix", heading: "Appendix: ECSDN Graduate Practitioner Competencies, March 2026", kind: "other: another issuer's document appended to the held text (ECSDN, revised March 2026); the skeleton labels it advisory-group membership and a contents listing (Part E)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 216 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/early-childhood-studies-2022/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Characteristics of an Early Childhood Studies degree"] }
  span: { start: 16928, end: 17287 }
  source: "1.18 Successful achievement of Level 6 Early Childhood Graduate Practitioner Competencies (ECGPC) aims to strengthen a graduate early childhood workforce. The competencies are written and reviewed by the Early Childhood Studies Degrees Network (ECSDN) and, as such, membership of this organisation is an expectation for institutions offering this opportunity."
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "institutions offering the graduate practitioner competencies"
  addressee: provider
  verbs: ["written", "reviewed"]
  about: "network membership to offer the competencies"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Achieving the Level 6 graduate practitioner competencies is meant to strengthen a graduate early years workforce; the network that writes and reviews them expects any institution offering them to be a member."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.20
  locator: { number: "1.20", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Characteristics of an Early Childhood Studies degree"] }
  span: { start: 17928, end: 18312 }
  source: "1.20 Early Childhood Studies degrees often provide opportunities to critically explore theory and research in practice. The ECGPC provide opportunities to strengthen this area. If awarding institutions indicate that completing the degree allows students to practice in early years settings, they must ensure they comply with the requirements of the nation that the student studies in."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "institutions that say the degree permits early years practice"
  addressee: provider
  verbs: ["indicate", "ensure", "comply"]
  about: "compliance where a degree claims to permit early years practice"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Early childhood degrees often let students explore theory and research in practice; where an institution says its degree lets graduates practise in early years settings, it must comply with the requirements of the nation where the student studies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Equality, diversity and inclusion"] }
  span: { start: 18830, end: 19395 }
  source: "1.23 Early Childhood Studies undergraduates and postgraduates should continually interrogate the language, perceptions and entrenchment of dominant systems of thought, within concepts of knowledge and power. Recognition and commitment to agency, equal rights and inherent dignity of all humans form the foundation of social justice. Equality is positioned as an ethical consideration of each person’s multiple identities and experiences\n\n6\nand a fundamental human right in relation to supporting and advocating for anti-oppressive knowledge generation and practice."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "undergraduate and postgraduate students of the subject"
  addressee: learner
  verbs: ["interrogate"]
  about: "questioning dominant systems of thought"
  themes: [theme:edi]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduates and postgraduates should keep questioning the language, assumptions and entrenched dominant ways of thinking in ideas of knowledge and power; agency, equal rights and dignity ground social justice, and equality is both an ethical matter and a human right."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Equality, diversity and inclusion"] }
  span: { start: 19404, end: 19959 }
  source: "1.24 Undergraduate and postgraduate students in ECS courses experience teaching and learning practices that challenge dominant knowledge within pedagogical spaces which enable greater representation for marginalised voices. Students will be challenged to think critically about different realities and form their own pedagogical judgements, bearing in mind the concepts of equality, diversity and inclusion for the development of continued reflective practice. There will be evidence of institutional proactive systems of support and inclusive structures."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students on courses in the subject and their institutions"
  addressee: both
  verbs: ["challenged", "think", "form"]
  about: "teaching that challenges dominant knowledge; institutional support"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students at all levels meet teaching that challenges dominant knowledge and gives marginalised voices more room; they will be pushed to think critically and make their own pedagogical judgements with equality in mind, and institutions will show active systems of support."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.25
  locator: { number: "1.25", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Equality, diversity and inclusion"] }
  span: { start: 19960, end: 20881 }
  source: "1.25 Every ECS degree programme will be meaningful, equitable and connected to scholarship and practice in studies of young children and their families which are underpinned by the principles of social justice. Early Childhood Studies courses will respect each graduate’s own identity, values and unique knowledge that they bring to the pedagogical space. Early Childhood Studies degree courses should enable personal and theoretical critical reflection on a wide range of theories, early childhood practice (0-8 years) and across disciplines. For practice placements to enable the students to practice in early years settings, the placement and the assessments must comply with the guidance provided by each nation. However, this is not the sole purpose of placements and students should be gaining experience across the age range up to eight years and across the discipline areas of health, s ocial c are and education."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "courses in the subject, their placements and their students"
  addressee: both
  verbs: ["respect", "enable", "comply", "gaining"]
  about: "equitable courses, critical reflection and placements from birth to eight"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Every degree will be meaningful, fair and grounded in scholarship and practice under social justice, and will respect each student's identity and knowledge; courses should foster personal and theoretical critical reflection across theories, practice from birth to eight and disciplines; placements meant to qualify students for early years practice must comply with each nation's guidance, while students should still gain experience across the age range and across health, social care and education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.26
  locator: { number: "1.26", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Equality, diversity and inclusion"] }
  span: { start: 20882, end: 21215 }
  source: "1.26 If EC S courses of study offer work-based/placement opportunities they must be well-defined, mentored, monitored, accessible and supervised for graduates to develop an understanding of how theory and practice are linked to support inclusive practice across a breadth of disciplines when working with young children and families."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "courses that offer work-based or placement learning"
  addressee: provider
  verbs: ["offer", "develop"]
  about: "conditions for placements"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Where courses offer work-based or placement learning, it must be clearly defined, mentored, monitored, accessible and supervised, so that students learn how theory and practice connect in inclusive work with children and families across disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.31
  locator: { number: "1.31", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Education for sustainable development"] }
  span: { start: 22005, end: 23120 }
  source: "1.31 These definitions, accessed from QAA’s and Advance HE’s Education for Sustainable Development Guidance Principles, allow students on ECS degrees to consider and critically evaluate the interrelatedness of the values that underpin ecological sustainability. Students can support young children and communities to understand what this means at a local, national and global level. Our aim is to give every c hild the best start in life\n\n7\nthrough adopting an interdisciplinary approach to e arly c hildhood. This is defined as seeing the child in context as a responsible citizen of the world. Early Childhood Studies degrees enable graduates to make informed decisions and take responsibility for present and future generations. Degrees should provide opportunities for the exploration of sustainability, social justice, democratic action and advocacy at different levels, with a focus on the personal, professional, community, national and global contexts. Therefore, ECS graduates demonstrate an understanding of how ecology and the sustainability of societies are linked by a response based on social justice."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "degrees in the subject and their graduates"
  addressee: both
  verbs: ["consider", "evaluate", "provide", "demonstrate"]
  about: "exploring sustainability, social justice and advocacy"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Drawing on the joint QAA and Advance HE sustainability guidance, students weigh the values behind ecological sustainability and can help children and communities grasp them; degrees should offer chances to explore sustainability, social justice, democratic action and advocacy from the personal to the global, so graduates show how ecology and sustainable societies link through social justice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.33
  locator: { number: "1.33", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Entrepreneurship and enterprise education"] }
  span: { start: 23695, end: 24192 }
  source: "1.33 ECS students and graduates contribute to a professional workforce leading and inspiring innovative practice and transforming practice and professional relationships, settings and services. Responsive to change and challenge, students and graduates will be well placed to add significant social, cultural and economic value to society. They contribute to, and work together to, support the ongoing development and professional recognition of the sector through knowledge and practice exchange."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students and graduates of the subject"
  addressee: learner
  verbs: ["contribute", "add", "support"]
  about: "innovation and social value"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students and graduates help build a workforce that leads innovation and changes practice, relationships, settings and services; ready for change, they will be well placed to add social, cultural and economic value, and they work together to develop the sector and its standing through exchanging knowledge and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.35
  locator: { number: "1.35", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Entrepreneurship and enterprise education"] }
  span: { start: 24408, end: 24909 }
  source: "1.35 Early Childhood Studies students should be developing behaviours, attributes and competencies suited to e arly c hildhood professions at different levels, such as taking initiative, making things happen, reflecting, communicating, pivoting and adapting, taking responsibility, networking, developing personal effectiveness and managing risk taking. Attributes and values include open-mindedness, proactivity, curiosity, self-efficacy, flexibility, adaptability, self-determination and resilience."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["developing"]
  about: "enterprising behaviours and attributes"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be building behaviours, attributes and competencies suited to early years professions at different levels, such as initiative, reflection, communication, adapting, responsibility, networking, personal effectiveness and managed risk-taking, with values such as open-mindedness, curiosity, self-efficacy and resilience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.36.b1
  locator: { number: "1.36.b1", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25171, end: 25256 }
  source: "confidence in professional intuitive decision making and in identifying opportunities"
  stem: "1.36"
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "students and postgraduates of the subject"
  addressee: both
  verbs: ["identifying"]
  about: "intuitive professional decisions and spotting opportunities"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students are to be given chances to develop confidence in intuitive professional decisions and in spotting opportunities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.36.b2
  locator: { number: "1.36.b2", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25259, end: 25290 }
  source: "creative problem-solving skills"
  stem: "1.36"
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "students and postgraduates of the subject"
  addressee: both
  verbs: []
  about: "creative problem-solving"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students are to be given chances to develop creative problem-solving."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.36.b3
  locator: { number: "1.36.b3", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25293, end: 25326 }
  source: "innovative and strategic thinking"
  stem: "1.36"
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "students and postgraduates of the subject"
  addressee: both
  verbs: []
  about: "innovative and strategic thinking"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students are to be given chances to develop innovative, strategic thinking."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.36.b4
  locator: { number: "1.36.b4", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25329, end: 25402 }
  source: "negotiation and communication skills, including critical digital literacy"
  stem: "1.36"
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "students and postgraduates of the subject"
  addressee: both
  verbs: []
  about: "negotiation, communication and critical digital literacy"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students are to be given chances to develop negotiation and communication, critical digital literacy among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.36.b5
  locator: { number: "1.36.b5", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25405, end: 25415 }
  source: "leadership"
  stem: "1.36"
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "students and postgraduates of the subject"
  addressee: both
  verbs: []
  about: "leadership"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students are to be given chances to develop leadership."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.36.b6
  locator: { number: "1.36.b6", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25418, end: 25555 }
  source: "collaboration between children, colleagues, employers and students to develop knowledge and trustful relationships through mutual respect"
  stem: "1.36"
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "students and postgraduates of the subject"
  addressee: both
  verbs: ["develop"]
  about: "collaborative relationships built on respect"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students are to be given chances to develop collaboration among children, colleagues, employers and students that builds knowledge and trust through mutual respect."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.36.b7
  locator: { number: "1.36.b7", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25558, end: 25741 }
  source: "open-mindedness through acknowledgement of diversity, capability, competencies, skills and knowledge, and support inter-dependent responsiveness in collaborative learning interactions"
  stem: "1.36"
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "students and postgraduates of the subject"
  addressee: both
  verbs: ["support"]
  about: "open-mindedness and responsive shared learning"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students are to be given chances to develop open-mindedness that values varied capabilities and knowledge and supports responsive, interdependent learning together."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/1.36.b8
  locator: { number: "1.36.b8", headingPath: ["Context and purposes of an Early Childhood Studies degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25747, end: 25833 }
  source: "recognition and respect of the uniqueness of each individual and the value they bring."
  stem: "1.36"
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "students and postgraduates of the subject"
  addressee: both
  verbs: []
  about: "respect for each person's uniqueness"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students are to be given chances to develop recognition of, and respect for, each person's uniqueness and what they bring."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Design - defining principles"] }
  span: { start: 25927, end: 27388 }
  source: "2.1 Courses in ECS aim to give students an understanding of early childhood from conception to the age of eight, and of multiple childhoods. Early childhood is defined as the period from conception to eight years old (including peri natal health) where children’s development is influenced by the environment and the people that surround them. Early childhood is much more than preparation for primary school. It is concerned with holistic development across the domains of social, emotional, cognitive and physical to build a solid and broad foundation for lifelong learning and wellbeing (UNESCO ). Conception to eight years takes into account global definitions of early childhood - for example, UNESCO; The 1001 Critical Days (Leadsom et al 2013). This context is understood as encompassing both time and geographical space, and encompassing the contexts of family and community, and children's and family services. The focus is on the unique development of the child in context and the implications for practice. Practitioners need to develop knowledge of the intricacies of supporting the development and learning of all children and the local situations in which they live. Degrees should be knowledgeable about the requirements of social justice, children’s rights, children’s culture and equality, and diversity and inclusion, and ensure that this encompasses supporting the development, well- being, participation and learning for multiple childhoods."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "degrees in the subject"
  addressee: provider
  verbs: ["develop", "ensure"]
  about: "social justice, rights and equality across childhoods"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses cover early childhood from conception to eight across many childhoods, a period of all-round development that is more than readiness for school; practitioners need to know how to support every child in their local setting, and degrees should know what social justice, children's rights, culture, equality, diversity and inclusion require and make sure this reaches the development, well-being, participation and learning of all childhoods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Accessibility"] }
  span: { start: 29047, end: 29451 }
  source: "2.4 The course design will ensure that those choosing to study Early Childhood Studies are able to think in ways that are creative and innovative. Courses will consider ways to be inclusive and to ensure that the teaching and assessment are accessible to a diverse community. This may include decolonising the curriculum and providing support for disabled students and students with diverse requirements."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "course design in the subject"
  addressee: provider
  verbs: ["ensure", "consider"]
  about: "creative thinking and accessible teaching and assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Course design will make sure students can think creatively and innovatively, and courses will look for ways to be inclusive and to make teaching and assessment accessible to a diverse community, which may mean decolonising the curriculum and supporting disabled students and others with diverse needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Accessibility"] }
  span: { start: 30527, end: 31297 }
  source: "2.7 Degree content should include a range of modes of delivery, for example face-to- face, online, flipped learning, group work, individual study, mirroring practice environments in simulated classrooms, or in placements located in a broad range of locations and professional environments. This ensures students can develop both a multidisciplinary and transdisciplinary experience alongside an understanding of multiple childhoods and their families. Examples include:\n• s ocial care\n• health\n• social enterprises\n• local authority\n• family and community support\n• charities and not-for-profit organisations\n• policy environments\n• outdoor learning environments, for example forest schools, beach schools, river schools\n• early years settings, childminders and schools."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "delivery of degrees in the subject"
  addressee: provider
  verbs: ["include", "develop"]
  about: "varied modes of delivery and placement settings"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Content should be delivered in varied ways, such as face to face, online, flipped, group and individual study, simulated classrooms or placements in a broad mix of settings, so that students gain multi- and transdisciplinary experience and understand diverse childhoods and families; nine kinds of setting are given as examples, from social care and health to forest schools and childminders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Accessibility"] }
  span: { start: 31298, end: 32427 }
  source: "2.8 Assessments and dialogue also need to be accessible and should be varied to allow the student to develop the academic and practice skills to understand the needs of young children, families and communities. Where possible, these assessments should reflect real-life situations to support future employability. Assessments should also support and demonstrate awareness of the range of learning opportunities and styles of all students, building on the knowledge and skills they have, helping them develop new knowledge and skills, and being flexible enough to enable reasonable adjustments. They should include the use of assistive technology to support accessibility. Early Childhood Studies degrees should offer a range of assessment methods that would benefit student understanding of the breadth and praxis nature of the discipline. These are outlined in more detail in s ection 3 of this Statement. Assessments should also ensure that they remain contemporary in terms of developing digital skills which encourage graduates to develop and sustain a wide range of digital platforms for communication and teaching purposes."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment in the subject"
  addressee: provider
  verbs: ["reflect", "include", "offer"]
  about: "accessible, varied, authentic assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment and dialogue should be accessible and varied so students build the academic and practice skills to understand children, families and communities; where possible tasks should mirror real situations, allow for different learners, permit reasonable adjustments, use assistive technology, offer a range of methods and keep digital skills current."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Accessibility"] }
  span: { start: 32428, end: 32638 }
  source: "2.9 W hatever assessment strategy is selected, it should be commensurate with the level of the degree and build on any academic and vocational assessments students may have undertaken before joining the degree."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment strategies in the subject"
  addressee: provider
  verbs: ["selected", "build"]
  about: "assessment pitched at the level of study"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Whatever the assessment strategy, it should match the level of the degree and build on the academic and vocational assessment students met before they joined."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Accessibility"] }
  span: { start: 32639, end: 33249 }
  source: "2.10 Physical and digital provision should be accessible for all students. This should provide spaces for reflection and debate on the subject and, as such, the emotional environment for students should be accepting of difference, including different viewpoints. These environments should be open to critical, constructive and research-informed debates to enhance the understanding of the breadth of topics covered in ECS degree courses.\n\n11\nAttending to these matters will help to foster and construct a learning community that includes staff, students and other partners in the workplace (where appropriate)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "physical and digital provision for the subject"
  addressee: provider
  verbs: ["provide", "foster"]
  about: "accessible spaces for reflection and debate"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Physical and digital provision should be accessible to all students and give room for reflection and debate in a climate that accepts difference and stays open to critical, research-informed discussion; this helps build a learning community of staff, students and workplace partners."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Progression"] }
  span: { start: 33262, end: 34086 }
  source: "2.11 Early Childhood Studies degrees offer students rich and varied progression routes into employment and/or further study. Over the course of a degree with honours (FHEQ Level 6; FQHEIS L evel 10), an ECS student will progress from one year of study to the next, in line with the regulations and processes for each institution. However, it is expected that each year would see the attainment of certain levels of knowledge, expertise and experience which builds towards the final achievement of meeting all of the threshold-level subject- specific and generic skills listed in this Statement. Upon graduation from an undergraduate degree, it would be expected that a student who had achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study or an associated discipline."
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "honours students of the subject"
  addressee: learner
  verbs: ["progress", "meeting", "undertaking"]
  about: "progress towards all the threshold skills"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Degrees open many routes into work and study; across an honours degree (FHEQ level 6, FQHEIS level 10) each year is expected to build knowledge, expertise and experience towards meeting every threshold-level subject-specific and generic skill, and a graduate with a second-class degree or above would be expected to be ready for postgraduate study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Progression"] }
  span: { start: 34087, end: 34346 }
  source: "2.12 Joint honours undergraduates will achieve elements of the specific and generic skills for the subject but will add others according to the subjects covered in a joint programme; these should also complement progression to master’s and/or d octoral study."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint honours students"
  addressee: learner
  verbs: ["achieve", "add", "complement"]
  about: "joint honours"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Joint honours students will reach some of the subject's specific and generic skills and add others from their other subject; the combination should also support progression to master's or doctoral study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Progression"] }
  span: { start: 35003, end: 35595 }
  source: "2.14 Early Childhood Studies degrees should be designed to encourage critical reflection, engagement with the academic field, and to develop high-quality practice across all aspects of e arly c hildhood. It is expected that teaching and learning is balanced across a range of disciplines and does not heavily focus on one discipline (for example, early education) at the expense of others. This should take account of research-informed debates and current and developing legislation and guidance. There should be scope for students and graduates to progress into their chosen career pathways."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "design of degrees in the subject"
  addressee: provider
  verbs: ["designed", "encourage", "develop", "take"]
  about: "design for reflection; balance across disciplines"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Degrees should be built to foster critical reflection and engagement with the field and to develop high-quality practice; teaching is expected to be balanced across disciplines rather than centred on one, such as early education, should take account of research debates and changing law and guidance, and should leave students room to move into their chosen careers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.15
  locator: { number: "2.15", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Progression"] }
  span: { start: 35596, end: 36124 }
  source: "2.15 These Subject Benchmark Statements can apply to the full range of degree courses offered which can include BA (Hons), t op-ups as a progression from f oundation degrees, BA (Hons) full or part-time degrees, and master’s provision. This encourages students and graduates to further develop their knowledge, understanding and skills. There should be the potential to progress to doctoral study (professional d octorate or PhD) which can enhance the development of new and innovative knowledge and practice in early childhood."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["apply", "encourages", "develop", "enhance"]
  about: "range of courses served; doctoral progression"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The statement can serve the full range of courses in the field, from top-ups and full or part-time honours to master's; there should be scope to go on to doctoral study, by professional doctorate or PhD, which can advance new knowledge and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.16
  locator: { number: "2.16", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Progression"] }
  span: { start: 36125, end: 36840 }
  source: "2.16 W here a suite of qualifications is developed, they should make clear how their design shows a deepening understanding of theory, research, practice, policy and legislation. This understanding should reflect a deepening understanding of EDI and sustainability. For courses t hat offer a practice placement option, the design of these placements and assessment should consider the requirement for those working in the Early Childhood Education and Care sectors across all four UK nations. However, these placements should offer an opportunity to develop a multidisciplinary and transdisciplinary experience with an understanding of multiple childhoods and families, not only in early years settings and schools."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "suites of qualifications and placement design"
  addressee: provider
  verbs: ["make", "shows", "reflect", "consider", "offer"]
  about: "suites of qualifications; placement design"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Where a suite of qualifications is built, it should show how understanding of theory, research, practice, policy and law deepens, EDI and sustainability included; where placements are offered, their design and assessment should take account of what early childhood education and care needs in each UK nation, while giving multi- and transdisciplinary experience beyond early years settings and schools."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Partnership"] }
  span: { start: 37851, end: 38354 }
  source: "2.19 Working in partnership with multidisciplinary and transdisciplinary practice forms a crucial part of ECS degrees, foundation degrees, apprenticeships and master’s provision. This can be in the form of placement opportunities or exploring employability opportunities through courses that do not have placements. Early Childhood Studies degrees should strive to demonstrate the multidisciplinary nature of the discipline itself through links with local, regional, national and international partners."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "degrees in the subject"
  addressee: provider
  verbs: ["strive", "demonstrate"]
  about: "partnership across disciplines and places"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Partnership with multi- and transdisciplinary practice is central to degrees, foundation degrees, apprenticeships and master's courses, through placements or, where there are none, through employability work; degrees should aim to show the field's multidisciplinary nature through partners from local to international."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.20
  locator: { number: "2.20", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Partnership"] }
  span: { start: 38355, end: 39602 }
  source: "2.20 S uccessful achievement of Level 6 ECGPCs meets the Level 3 requirements in England (with assessed practice) and, in addition, makes a significant contribution to strengthening a graduate-led early childhood workforce across all four nations and internationally. Higher education providers must make it clear whether or not they offer ECGPS to potential students to ensure transparency when students apply for degrees. Level 6 ECGPC provides students with assessed placement opportunities to critically apply theory to practice in a range of early childhood settings and/or schools, social care and health settings. This will enable students to develop graduate skills to further support children, to link to employability and in the application of the interdisciplinary early childhood knowledge base to reflective practice (see Appendix 1: Early Childhood Graduate Practitioner Competencies). However, as discussed in paragraph 1.19, the competencies are not an expected outcome for all ECS degrees; a professional qualification for work in early childhood may not be appropriate for all learners or providers. There may also be different requirements for home nations students and students should discuss these options with their provider."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "institutions and applicants to the subject"
  addressee: both
  verbs: ["make", "ensure", "discuss"]
  about: "openness about whether the competencies are offered"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Achieving the Level 6 competencies meets England's Level 3 requirements, with assessed practice, and strengthens a graduate-led workforce; institutions must tell prospective students clearly whether they offer the competencies, which are not expected of every degree, and students should talk through requirements for their home nation with their institution."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.22
  locator: { number: "2.22", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Monitoring and review"] }
  span: { start: 40364, end: 40681 }
  source: "2.22 E xternality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an\n\n13\n\nexternal perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "institutions reviewing courses in the subject"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Externality is essential to UK quality assurance: institutions will use external reviewers in periodic review to bring an outside view of proposed changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.24
  locator: { number: "2.24", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Monitoring and review"] }
  span: { start: 41477, end: 42062 }
  source: "2.24 External examiners should have the required specialist knowledge and understanding to be able to ensure the quality of courses and, where applicable, practice placements and the attainment of Graduate Practitioner Competencies. Examiners need to be flexible to the range of course designs but be aware of the core principles in this Subject Benchmark Statement which should underpin all degrees. They should also be aware of the different types of courses offered (with the required level for these), and the potential for a variety of delivery models when they examine provision."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "external examiners for the subject"
  addressee: provider
  verbs: ["have", "ensure"]
  about: "external examiners' knowledge"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "External examiners should hold the specialist knowledge to assure course quality and, where relevant, placements and the graduate practitioner competencies; they should be open to varied course designs while knowing the core principles here, the kinds and levels of course and the delivery models."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/2.25
  locator: { number: "2.25", headingPath: ["Distinctive features of an Early Childhood Studies degree", "Monitoring and review"] }
  span: { start: 42063, end: 42519 }
  source: "2.25 Courses with professional and vocational outcomes may also require evaluation and accreditation from professional and regulatory bodies. These are usually done through a combination of assessed visits and reviews of academic work. The Early Childhood Studies Degrees Network provides further advice on the ECGPC. Higher education providers must be current members of this network to offer this as an embedded or extra certification option to students."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "institutions offering the graduate practitioner competencies"
  addressee: provider
  verbs: ["require", "provides", "offer"]
  about: "network membership to offer the competencies"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses with professional or vocational outcomes may also need evaluation and accreditation by professional and regulatory bodies, usually through visits and reviews of student work; the degrees network advises on the competencies, and an institution must be a current member of it to offer them, embedded or as an extra certificate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b1
  locator: { number: "3.3.b1", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 43761, end: 43974 }
  source: "r eflect upon a range of psychological, sociological, health, historical, educational and philosophical perspectives and consider how these underpin different understandings of babies, young children and childhood"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["consider"]
  about: "disciplinary perspectives on childhood"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to reflect on how psychology, sociology, health, history, education and philosophy each shape the way babies, young children and childhood are understood."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b2
  locator: { number: "3.3.b2", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 43977, end: 44146 }
  source: "apply multiple perspectives to early childhood issues, recognising that early childhood studies involves a range of research methods, theories, evidence and applications"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["apply", "recognising"]
  about: "many perspectives on early childhood issues"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to bring several perspectives to early childhood questions, aware that the field uses varied methods, theories, evidence and applications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b3
  locator: { number: "3.3.b3", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 44149, end: 44320 }
  source: "use skills of observation and analysis in relation to aspects of the lives of babies and young children with reasonable adjustments to support accessibility where required"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["use"]
  about: "observation with reasonable adjustments"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to observe and analyse aspects of babies' and young children's lives, with reasonable adjustments for accessibility where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b4
  locator: { number: "3.3.b4", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 44323, end: 44447 }
  source: "integrate ideas and findings across the multiple perspectives in ECS and recognise distinctive approaches to relevant issues"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["integrate", "recognise"]
  about: "integrating perspectives"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to combine ideas and findings from the field's many perspectives and see how each treats an issue in its own way."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b5
  locator: { number: "3.3.b5", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 44450, end: 44603 }
  source: "constructively critique theories, practice and research in the areas of child development, well-being, participation and learning for multiple childhoods"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["critique"]
  about: "critiquing theory, practice and research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to critique constructively the theory, practice and research on children's development, well-being, participation and learning across diverse childhoods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b6
  locator: { number: "3.3.b6", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 44606, end: 44711 }
  source: "demonstrate knowledge and awareness of the skills needed for different pedagogical approaches, including:"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "skills for pedagogical approaches"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show knowledge and awareness of the skills that different pedagogical approaches call for."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b7
  locator: { number: "3.3.b7", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 44714, end: 44902 }
  source: "the necessary depth and strength of relationships with individual babies and children, children in groups, and the facilitation of the building of relationships between babies and children"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: []
  about: "relationships with and between children"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to understand how deep and strong relationships need to be with individual babies and children and with groups, and how to help children build relationships with each other."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b8
  locator: { number: "3.3.b8", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 44905, end: 45032 }
  source: "the formation and promotion of mutually respectful relationships with families, colleagues, other professionals and communities"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: []
  about: "respectful relationships with adults"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to build and encourage relationships of mutual respect with families, colleagues, other professionals and communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b9
  locator: { number: "3.3.b9", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 45035, end: 45084 }
  source: "evaluate and develop their own pedagogical values"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["evaluate", "develop"]
  about: "own pedagogical values"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to evaluate and develop their own values about teaching and care."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b10
  locator: { number: "3.3.b10", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 45087, end: 45263 }
  source: "reflect on the importance of the natural environment and being outdoors to support the growth, development, knowledge and understanding of all young children and their families"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["reflect"]
  about: "the natural environment and the outdoors"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to reflect on why the natural world and time outdoors matter for how all young children and their families grow, develop, know and understand."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b11
  locator: { number: "3.3.b11", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 45266, end: 45556 }
  source: "critically explore, examine and evaluate the significance of the cultural, historical, and contemporary features of various policies, institutions and agencies, locally,\n\n15\nnationally and globally, regarding babies’ and young children’s development and the concept of childhood more widely"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["explore", "examine", "evaluate"]
  about: "policies, institutions and agencies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to explore, examine and judge critically the cultural, historical and current features of policies, institutions and agencies, local to global, and what they mean for children's development and for ideas of childhood."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b12
  locator: { number: "3.3.b12", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 45559, end: 45659 }
  source: "demonstrate a strong understanding of the pedagogy of play from a range of disciplinary perspectives"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the pedagogy of play"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show a strong grasp of the pedagogy of play as several disciplines see it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b13
  locator: { number: "3.3.b13", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 45662, end: 45860 }
  source: "plan for - and where appropriate implement - curriculum, assessment, evaluation and improvement of creative learning opportunities, taking account of young children's health and emotional well-being"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["plan", "implement"]
  about: "planning creative learning"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to plan, and where fitting carry out, curriculum, assessment, evaluation and improvement of creative learning, with regard to children's health and emotional well-being."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b14
  locator: { number: "3.3.b14", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 45863, end: 46023 }
  source: "lead, support and work collaboratively with others and demonstrate an understanding of working effectively in teams with parents, carers and other professionals"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["lead", "support", "work", "demonstrate"]
  about: "leading and teamwork"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to lead, support and collaborate with others and understand effective teamwork with parents, carers and other professionals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b15
  locator: { number: "3.3.b15", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 46026, end: 46232 }
  source: "demonstrate an understanding of how to plan for - and where appropriate implement - meeting and promoting children's health, well-being, protection and safety and the conditions that enable them to flourish"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "plan", "implement"]
  about: "health, protection and safety"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to understand how to plan for, and where fitting deliver, the protection, safety, health and well-being of children and the conditions in which they thrive."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b16
  locator: { number: "3.3.b16", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 46235, end: 46356 }
  source: "produce critical arguments for improvements to multiagency and multi-professional practices for babies and young children"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["produce"]
  about: "arguing for better joint practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to build critical arguments for improving multiagency and multi-professional practice for babies and young children."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b17
  locator: { number: "3.3.b17", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 46359, end: 46462 }
  source: "use skills of observation and analysis in relation to aspects of the lives of babies and young children"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["use"]
  about: "observation and analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to observe and analyse aspects of babies' and young children's lives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b18
  locator: { number: "3.3.b18", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 46465, end: 46561 }
  source: "reflect upon the ethics of studying babies and young children and their families and communities"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["reflect"]
  about: "the ethics of studying children"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to reflect on the ethics of studying babies, young children, their families and communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b19
  locator: { number: "3.3.b19", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 46564, end: 46671 }
  source: "generate and explore hypotheses and research questions relating to early childhood in an ecological context"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["generate", "explore"]
  about: "hypotheses and research questions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to form and test out hypotheses and research questions on early childhood, seen in its ecological context."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b20
  locator: { number: "3.3.b20", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 46674, end: 46881 }
  source: "c arry out empirical studies ethically, involving a variety of methods of data collection, including observations relating to early childhood in an ecological context analyse data relating to early childhood"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["involving", "analyse"]
  about: "ethical empirical study and analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to carry out ethical empirical studies with varied data collection, observation of early childhood in its ecological context among them, and analyse the data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b21
  locator: { number: "3.3.b21", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 46884, end: 46941 }
  source: "present and evaluate research findings in early childhood"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["present", "evaluate"]
  about: "presenting and evaluating findings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to present and judge research findings on early childhood."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b22
  locator: { number: "3.3.b22", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 46944, end: 47164 }
  source: "demonstrate a critical understanding of the interrelationships between political, economic, cultural and ideological contexts, locally, nationally and globally, in the lives of children and their families and communities"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "interrelated contexts in children's lives"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to understand critically how political, economic, cultural and ideological contexts, from local to global, act on one another in the lives of children, families and communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b23
  locator: { number: "3.3.b23", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 47167, end: 47248 }
  source: "recognise and challenge inequalities in society, and embrace an antibias approach"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["recognise", "challenge", "embrace"]
  about: "challenging inequality"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to recognise and challenge inequality in society and take an anti-bias approach."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.3.b24
  locator: { number: "3.3.b24", headingPath: ["Content, teaching, learning and assessment", "Subject-specific skills"] }
  span: { start: 47251, end: 47379 }
  source: "recognise agency, give voice to and, where appropriate, act as an advocate for babies, young children, families and communities."
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["recognise", "give", "act"]
  about: "agency, voice and advocacy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to recognise children's agency, help their voices be heard and, where fitting, advocate for babies, young children, families and communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b1
  locator: { number: "3.4.b1", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 47465, end: 47573 }
  source: "present information to others in appropriate f orms, including having a sense of audience, online or offline"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["present"]
  about: "presenting information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to present information in suitable forms, online or offline, with a sense of audience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b2
  locator: { number: "3.4.b2", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 47576, end: 47695 }
  source: "demonstrate empathy, active listening skills and develop strategies to protect against burn out from ‘emotional labour’"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "develop"]
  about: "empathy and guarding against burnout"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show empathy and active listening and develop ways to guard against burnout from emotional labour."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b3
  locator: { number: "3.4.b3", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 47698, end: 47788 }
  source: "offer and justify an informed point of view, drawing upon a range of theoretical positions"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["offer", "justify"]
  about: "arguing a view from theory"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to give and defend an informed view, drawing on a range of theoretical positions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b4
  locator: { number: "3.4.b4", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 47791, end: 47826 }
  source: "comprehend and use data effectively"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["comprehend", "use"]
  about: "using data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to understand data and use it well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b5
  locator: { number: "3.4.b5", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 47829, end: 47933 }
  source: "communicate with others and reflect upon one's own and others' skills, beliefs, understandings and views"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["communicate", "reflect"]
  about: "communicating and reflecting on views"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to communicate with others and reflect on their own and others' skills, beliefs, understanding and views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b6
  locator: { number: "3.4.b6", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 47936, end: 48018 }
  source: "generate, define and refine questions and make critical judgements and evaluations"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["generate", "define", "refine", "make"]
  about: "framing questions and judging"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to frame and sharpen questions and judge critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b7
  locator: { number: "3.4.b7", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 48025, end: 48123 }
  source: "reflect on different perspectives, and critically evaluate them to arrive at supported conclusions"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["reflect", "evaluate"]
  about: "reaching supported conclusions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to weigh different perspectives critically and reach well-supported conclusions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b8
  locator: { number: "3.4.b8", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 48126, end: 48262 }
  source: "access, retrieve, organise and use a range of sources of information, including primary sources, and critically evaluate their relevance"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["access", "retrieve", "organise", "use", "evaluate"]
  about: "finding and judging sources"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to find, retrieve, organise and use varied information sources, primary sources among them, and judge critically how relevant they are."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b9
  locator: { number: "3.4.b9", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 48265, end: 48362 }
  source: "engage with research and practice and the uncertainties of developing knowledge and understanding"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["engage"]
  about: "uncertainty in knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to engage with research and practice and with the uncertainty of knowledge still being built."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b10
  locator: { number: "3.4.b10", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 48365, end: 48541 }
  source: "use the communication skills necessary to converse, debate, negotiate, persuade and challenge the ideas of others, with reasonable adjustments for disabled students if required"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["use", "converse", "debate", "negotiate", "persuade", "challenge"]
  about: "communicating to debate and persuade"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to use communication skills to talk, debate, negotiate, persuade and challenge others' ideas, with reasonable adjustments for disabled students where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b11
  locator: { number: "3.4.b11", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 48544, end: 48622 }
  source: "have insight and confidence in leading and working collaboratively with others"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["have"]
  about: "leading and collaborating"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to lead and collaborate with others with insight and confidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b12
  locator: { number: "3.4.b12", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 48625, end: 48824 }
  source: "be sensitive to contextual and interpersonal factors, taking account of the complexity of factors that shape behaviour and social interaction and form the basis of problems and interpersonal conflict"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["shape", "form"]
  about: "context and interpersonal factors"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to be alert to contextual and interpersonal factors, seeing how complex influences shape behaviour and interaction and give rise to problems and conflict."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b13
  locator: { number: "3.4.b13", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 48827, end: 48933 }
  source: "be sensitive to the importance of enhancing cooperation to maximise the effectiveness of individual skills"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["enhancing", "maximise"]
  about: "cooperation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to see the value of cooperation in making individual skills more effective."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b14
  locator: { number: "3.4.b14", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 48936, end: 49097 }
  source: "write for different purposes, including but not limited to persuasion, explanation, description, evaluation and judgement, recount, recap, hypothesis and summary"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["write"]
  about: "writing for different purposes"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to write for varied purposes, such as persuading, explaining, describing, evaluating, recounting, summarising and hypothesising."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b15
  locator: { number: "3.4.b15", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 49100, end: 49142 }
  source: "engage in critical evaluation and analysis"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["engage"]
  about: "critical evaluation and analysis"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to evaluate and analyse critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b16
  locator: { number: "3.4.b16", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 49145, end: 49252 }
  source: "use digital technology and social media appropriately in a range of contexts and reflect on the experiences"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["use", "reflect"]
  about: "digital technology and social media"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to use digital technology and social media appropriately in different contexts and reflect on that use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.4.b17
  locator: { number: "3.4.b17", headingPath: ["Content, teaching, learning and assessment", "Generic skills"] }
  span: { start: 49255, end: 49354 }
  source: "become more independent, resilient, responsible and pragmatic and develop as an autonomous learner."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["become", "develop"]
  about: "autonomy and resilience"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to become a learner who works autonomously, growing in independence, resilience, responsibility and pragmatism."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.6
  locator: { number: "3.6", headingPath: ["Content, teaching, learning and assessment", "Teaching and learning"] }
  span: { start: 50479, end: 50851 }
  source: "3.6 Therefore, the teaching strategies and learning experiences reflect an increasing proportion of individualised and self-directed learning approaches. Students are encouraged to take personal responsibility for achieving the learning outcomes through their own efforts. They are expected to supplement the knowledge presented through additional enquiry and discussions."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["encouraged", "take", "supplement"]
  about: "self-directed learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Teaching moves towards more individual and self-directed learning; students are encouraged to take responsibility for meeting the outcomes and are expected to add to what is taught through their own enquiry and discussion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.8
  locator: { number: "3.8", headingPath: ["Content, teaching, learning and assessment", "Teaching and learning"] }
  span: { start: 50986, end: 51624 }
  source: "3.8 Approaches to teaching and learning value personal, theoretical, cultural and practice-based experiences and explore how they complement and enrich each other. There is a requirement to support students in reflecting on their own childhoods, on experience in early childhood settings and in exploring the relationship between these personal experiences and the theoretical perspectives that enable students to make sense of them developing their cultural competence. Personal reflection on childhood experiences can be a painful experience and emotional support for students is an essential part of teaching strategies in these cases."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "teaching in the subject"
  addressee: provider
  verbs: ["support"]
  about: "supported reflection on one's own childhood"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching values personal, theoretical, cultural and practice experience; there is a requirement to support students as they reflect on their own childhoods and on time in early years settings and link these to theory, building cultural competence, and emotional support is essential where such reflection is painful."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.12
  locator: { number: "3.12", headingPath: ["Content, teaching, learning and assessment", "Assessment"] }
  span: { start: 53658, end: 53983 }
  source: "3.12 The choice of assessment methods is clearly related to the learning objectives and enables students to demonstrate theoretical, subject-specific and generic skills and their understanding of the ways in which they complement and enrich each other. Reasonable adjustments should be made for disabled students if required."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment in the subject"
  addressee: provider
  verbs: ["made"]
  about: "reasonable adjustments in assessment"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment methods are tied to the learning objectives and let students show theoretical, subject-specific and generic skills and how they connect; reasonable adjustments should be made for disabled students where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.14
  locator: { number: "3.14", headingPath: ["Content, teaching, learning and assessment", "Assessment"] }
  span: { start: 54788, end: 55272 }
  source: "3.14 Students may also be assessed for their practice in an appropriate range of health, social care and early childhood settings. This is a requirement if students are completing the graduate practitioner competencies. To ensure that the full range of skills and inclusivity is being developed by a course, a diversity of innovative assessment methods is encouraged. Assessment criteria are explicit, inclusive and anticipate that critical thinking skills will develop progressively."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "students taking the graduate practitioner competencies"
  addressee: both
  verbs: ["assessed", "completing", "encouraged", "anticipate", "develop"]
  about: "assessment of practice for the competencies"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students may be assessed on their practice in health, social care and early years settings, and this is required for those completing the graduate practitioner competencies; varied, innovative assessment is encouraged, and criteria are explicit, inclusive and expect critical thinking to grow over time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/3.16
  locator: { number: "3.16", headingPath: ["Content, teaching, learning and assessment", "Assessment"] }
  span: { start: 55949, end: 56353 }
  source: "3.16 T he range and breadth of assessment is designed to enable students to demonstrate possession of a variety of subject-specific and general skills and qualities expected of a graduate, and an increasing degree of independence and autonomy in their studies. Assessment feedback and feed forward should be in sufficient depth to allow students to reflect on their achievement and inform their progress."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment feedback in the subject"
  addressee: provider
  verbs: ["designed", "demonstrate", "allow", "reflect", "inform"]
  about: "depth of feedback"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The range of assessment lets students show varied skills and growing independence; feedback and feed-forward should be deep enough for students to reflect on what they achieved and shape their next steps."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 57758, end: 58105 }
  source: "4.3 A ll ECS graduates should acquire a measure of the skills required by the discipline as set out in the standards below; although the range of skills demonstrated and the degree of competence exhibited will vary depending on whether students take single honours, joint honours or Early C hildhood Studies modules within a broader degree course."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: learner
  verbs: ["acquire", "demonstrated", "exhibited", "vary"]
  about: "every graduate gains a measure of the skills"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "All graduates of the subject should gain a measure of the skills the discipline needs, as the standards set out, though how many skills they show and how well will differ between single honours, joint honours and modules within a wider degree."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 58609, end: 58694 }
  source: "understand the conceptual underpinnings of e arly childhood studies as a subject area"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["understand"]
  about: "the conceptual foundations of the field"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will understand the core ideas on which early childhood studies is built as a field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b1.excellent
  locator: { number: "4.4.b1.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 58834, end: 58983 }
  source: "understand critically the conceptual underpinnings of e arly childhood studies as a subject area, its historical origins, development and limitations"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["understand"]
  about: "the conceptual foundations of the field"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b1.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will understand critically the field's founding ideas, its origins, growth and limits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b1.masters
  locator: { number: "4.4.b1.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 58984, end: 59195 }
  source: "detailed and accurate knowledge and understanding, showing critical engagement with the conceptual underpinnings of e arly childhood studies as a subject area, its historical origins, development and limitations"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: []
  about: "the conceptual foundations of the field"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will show detailed, accurate and critically engaged knowledge of the field's founding ideas, origins, growth and limits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b1.typical
  locator: { number: "4.4.b1.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 58695, end: 58833 }
  source: "understand the conceptual underpinnings of e arly childhood studies as a subject area, its historical origins, development and limitations"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["understand"]
  about: "the conceptual foundations of the field"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b1, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will understand those core ideas together with where the field came from, how it grew and where it falls short."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 59196, end: 59469 }
  source: "have a basic understanding of babies, young children and multiple childhoods, nationally and globally, from psychological, sociological, health, welfare, educational, cultural, decolonising, sustainable, philosophical, legal, historical, political and economic perspectives"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: []
  about: "babies, young children and diverse childhoods through many disciplines"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will have a basic grasp of babies, young children and the many forms childhood takes, at home and worldwide, through the disciplines that study them, from psychology and sociology to law, politics and economics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b2.excellent
  locator: { number: "4.4.b2.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 59779, end: 60108 }
  source: "demonstrate in-depth, systematic knowledge and consistently critical understanding of babies, young children and multiple childhoods, nationally and globally, from psychological, sociological, health, welfare, educational, cultural, decolonising, sustainable, philosophical, legal, historical, political and economic perspectives"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "babies, young children and diverse childhoods through many disciplines"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b2.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will know babies, young children and diverse childhoods in depth and systematically, and understand them with consistent criticality, through every lens the field uses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b2.masters
  locator: { number: "4.4.b2.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 60110, end: 60462 }
  source: "well-developed critical engagement with theoretical knowledge, and a consistently critical understanding of babies, young children and multiple childhoods, nationally and globally, from psychological, sociological, health, welfare, educational, c ultural, decolonising, sustainable, philosophical, legal, historical, political and economic perspectives"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: []
  about: "babies, young children and diverse childhoods through many disciplines"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will engage critically with theory and understand babies, young children and diverse childhoods with consistent criticality through every lens the field uses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b2.typical
  locator: { number: "4.4.b2.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 59471, end: 59778 }
  source: "demonstrate systematic knowledge and critical understanding of babies, young children and multiple\n\nchildhoods, nationally and globally, from psychological, sociological, health, welfare, educational, cultural, decolonising, sustainable, philosophical, legal, historical, political and economic perspectives"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "babies, young children and diverse childhoods through many disciplines"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b2, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will know babies, young children and diverse childhoods systematically and understand them critically, at home and worldwide, through every disciplinary lens the field uses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 60463, end: 60641 }
  source: "demonstrate knowledge and understanding of the areas of interest contributing to e arly childhood studies across the core subject-specific skills areas, and how they interrelate."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "interrelate"]
  about: "the field's areas of interest and how they connect"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will know and understand the areas of interest that feed early childhood studies across its core skills areas, and how they connect."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b3.excellent
  locator: { number: "4.4.b3.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 60840, end: 61061 }
  source: "demonstrate in-depth, systematic knowledge and consistently critical understanding of the areas of interest contributing to e arly childhood studies across the core subject-specific skills areas, and how they interrelate."
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "interrelate"]
  about: "the field's areas of interest and how they connect"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b3.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will know those areas in depth and systematically and understand them and their connections with consistent criticality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b3.masters
  locator: { number: "4.4.b3.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 61062, end: 61271 }
  source: "detailed and accurate knowledge and consistently critical engagement with the areas of interest contributing to e arly childhood studies across the core subject-specific skills areas, and how they interrelate."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["interrelate"]
  about: "the field's areas of interest and how they connect"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will show detailed, accurate knowledge of those areas and engage with them and their connections consistently and critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b3.typical
  locator: { number: "4.4.b3.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 60642, end: 60839 }
  source: "demonstrate systematic knowledge and critical understanding of the areas of interest contributing to early childhood studies across the core subject-specific skills areas, and how they interrelate."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["demonstrate", "interrelate"]
  about: "the field's areas of interest and how they connect"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b3, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will know those areas systematically and understand them and their connections critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 61333, end: 61451 }
  source: "understanding of local, national and global policy, and provision for babies, young children, families and communities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: []
  about: "policy and provision for children and families"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will understand local, national and global policy and the provision it makes for young children, babies, their families and communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b4.excellent
  locator: { number: "4.4.b4.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 61607, end: 61728 }
  source: "in-depth, systematic knowledge and significant critical understanding of local, national and global policy, and provision"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: []
  about: "policy and provision for children and families"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b4.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will know that policy and provision in depth and systematically, with marked critical understanding."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b4.masters
  locator: { number: "4.4.b4.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 61729, end: 61866 }
  source: "detailed and accurate systematic knowledge and consistently critical engagement with local, national and global policy, and provision for"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: []
  about: "policy and provision for children and families"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will show detailed, accurate and systematic knowledge of that policy and provision and engage with it consistently and critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b4.typical
  locator: { number: "4.4.b4.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 61452, end: 61606 }
  source: "a systematic knowledge and critical understanding of local, national and global policy, and provision for babies, young children, families and communities"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: []
  about: "policy and provision for children and families"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b4, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will know that policy and provision systematically and understand it critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 62115, end: 62308 }
  source: "understanding of multi- professional, inter-professional, multiagency, interagency and multicultural working as a means to\n\nenhance the lives of babies, young children, families and communities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["enhance"]
  about: "working across professions, agencies and cultures"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will understand how working across professions, agencies and cultures can make life better for babies, young children, their families and communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b5.excellent
  locator: { number: "4.4.b5.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 62572, end: 62843 }
  source: "a critical working knowledge of the importance of, but also the challenges and constraints of, multi-professional, inter- professional, multiagency, interagency and multicultural working as a means to enhance the\n\nlives of babies, young children, families and communities"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["enhance"]
  about: "working across professions, agencies and cultures"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b5.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will have a critical working knowledge of why such joint working matters and of its challenges and limits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b5.masters
  locator: { number: "4.4.b5.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 62844, end: 63123 }
  source: "a well-developed critical engagement with the importance of, but also the challenges and constraints of, multi-professional, inter-professional, multiagency, interagency and multicultural working as a means to enhance the lives of babies, young children, families and communities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["enhance"]
  about: "working across professions, agencies and cultures"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will engage critically and in depth with the value, challenges and limits of such joint working."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b5.typical
  locator: { number: "4.4.b5.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 62310, end: 62571 }
  source: "a working knowledge of the importance of, but also the challenges and constraints of, multi-professional, inter- professional, multiagency, interagency and multicultural working as a means to enhance the lives of babies, young children, families and communities"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["enhance"]
  about: "working across professions, agencies and cultures"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b5, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will have a working knowledge of why such joint working matters and of the challenges and limits it meets."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 63124, end: 63313 }
  source: "awareness of issues in relation to human rights, diversity, equity, social justice, sustainability and inclusion in relation to working with babies, young children, families and communities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: []
  about: "rights, diversity, equity, justice, sustainability and inclusion in practice"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will be aware of issues of equity, diversity, inclusion, human rights, social justice and sustainability when working with babies, young children, families and communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b6.excellent
  locator: { number: "4.4.b6.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 63511, end: 63710 }
  source: "excellent knowledge of issues in relation to human rights, diversity, equity, social justice, sustainability and inclusion in relation to working with babies, young children, families and communities"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: []
  about: "rights, diversity, equity, justice, sustainability and inclusion in practice"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b6.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will have excellent knowledge of those issues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b6.masters
  locator: { number: "4.4.b6.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 63711, end: 63950 }
  source: "Synthesizing of knowledge and understanding that leads to originality in relation to human rights, diversity, equity, social justice, sustainability and inclusion in relation to working with babies, young children, families and communities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["Synthesizing"]
  about: "rights, diversity, equity, justice, sustainability and inclusion in practice"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will synthesise knowledge and understanding of those issues in ways that lead to original thinking."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b6.typical
  locator: { number: "4.4.b6.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 63314, end: 63510 }
  source: "a good knowledge of issues in relation to human rights, diversity, equity, social justice, sustainability and inclusion in relation to working with babies, young children, families and communities"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: []
  about: "rights, diversity, equity, justice, sustainability and inclusion in practice"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b6, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will have a good knowledge of those issues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 63951, end: 64071 }
  source: "knowledge and understanding of pedagogical approaches for working with babies, young children, families and communities."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: []
  about: "pedagogical approaches and values"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will know and understand pedagogical approaches for work with babies, young children, families and communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b7.excellent
  locator: { number: "4.4.b7.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 64215, end: 64365 }
  source: "a critical working knowledge and understanding of pedagogical approaches/values for working with\n\nbabies and young children, families and communities."
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: []
  about: "pedagogical approaches and values"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b7.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will have a critical working knowledge and understanding of those approaches and values."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b7.masters
  locator: { number: "4.4.b7.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 64366, end: 64553 }
  source: "detailed and accurate knowledge and understanding showing critical engagement with the pedagogical approaches/values for working with\n\nbabies and young children, families and communities."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: []
  about: "pedagogical approaches and values"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will show detailed, accurate and critically engaged knowledge of those approaches and values."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b7.typical
  locator: { number: "4.4.b7.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 64073, end: 64214 }
  source: "a working knowledge and understanding of pedagogical approaches/values for working with\n\nbabies and young children, families and communities."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: []
  about: "pedagogical approaches and values"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b7, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will have a working knowledge and understanding of those approaches and the values behind them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 64627, end: 64811 }
  source: "demonstrate a critical understanding of the links between ethics, economics, politics, culture and ideology in the lives of babies, young children, their families and their communities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "ethics, economics, politics, culture and ideology in children's lives"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will understand critically how ethics, economics, politics, culture and ideology connect in the lives of young children, babies and their families and communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b8.excellent
  locator: { number: "4.4.b8.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 65012, end: 65206 }
  source: "have a highly developed critical understanding of the links between ethics, economics, politics, culture and ideology in the lives of babies, young children, their families and their communities"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: []
  about: "ethics, economics, politics, culture and ideology in children's lives"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b8.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will understand those connections critically, to a highly developed degree."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b8.masters
  locator: { number: "4.4.b8.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 65207, end: 65394 }
  source: "have an excellent critical engagement with the links between ethics, economics, politics, culture and ideology in the lives of babies, young children, their families and their communities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: []
  about: "ethics, economics, politics, culture and ideology in children's lives"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will engage with those connections critically, to an excellent degree."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b8.typical
  locator: { number: "4.4.b8.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 64812, end: 65011 }
  source: "demonstrate a well-developed critical understanding of the links between ethics, economics, politics, culture and ideology in the lives of babies, young children, their families and their communities"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "ethics, economics, politics, culture and ideology in children's lives"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b8, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will understand those connections critically, in a well-developed way."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 65541, end: 65644 }
  source: "knowledge of the methods required for systematic study and research relative to children and childhood."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: []
  about: "methods for systematic study and research"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will know the methods needed to study and research children and childhood systematically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b9.excellent
  locator: { number: "4.4.b9.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 65764, end: 65898 }
  source: "excellent and explicit working knowledge of the methods required for systematic study and research relative to children and childhood."
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: []
  about: "methods for systematic study and research"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b9.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will have an excellent and explicit working knowledge of those methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b9.masters
  locator: { number: "4.4.b9.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 65899, end: 66026 }
  source: "a critically reflexive evaluation of the methods required for systematic study and research relative to children and childhood."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: []
  about: "methods for systematic study and research"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will evaluate those methods critically and reflexively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b9.typical
  locator: { number: "4.4.b9.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 65645, end: 65763 }
  source: "a good working knowledge of the methods required for systematic study and research relative to children and childhood."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: []
  about: "methods for systematic study and research"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b9, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will have a good working knowledge of those methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b10
  locator: { number: "4.4.b10", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 66123, end: 66217 }
  source: "reason clearly, and demonstrate the relationship between theory, policy, practice and evidence"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "reason", "evidence"]
  about: "reasoning about theory, policy, practice and evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will reason clearly and show how theory, policy, practice and evidence relate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b10.excellent
  locator: { number: "4.4.b10.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 66397, end: 66604 }
  source: "have a high-level ability to reason clearly, understand the role of theory, policy, practice and evidence and make critical judgements about arguments relating to the subject area of e arly childhood studies"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["understand", "reason", "evidence"]
  about: "reasoning about theory, policy, practice and evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b10.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will reason clearly to a high level, understand the part played by theory, policy, practice and evidence, and judge arguments in the field critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b10.masters
  locator: { number: "4.4.b10.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 66605, end: 66824 }
  source: "have an excellent ability to reason clearly, critically engage with the role of theory, policy, practice and evidence and make critical judgements about arguments relating to the subject area of e arly childhood studies"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["reason", "engage", "evidence"]
  about: "reasoning about theory, policy, practice and evidence"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will reason clearly to an excellent level, engage critically with the part played by theory, policy, practice and evidence, and judge arguments in the field critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b10.typical
  locator: { number: "4.4.b10.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 66218, end: 66396 }
  source: "reason clearly, understand the role of theory, policy, practice and evidence and make critical judgements about arguments relating to the subject area of e arly childhood studies"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["understand", "reason", "evidence"]
  about: "reasoning about theory, policy, practice and evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b10, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will reason clearly, understand what theory, policy, practice and evidence each contribute, and judge arguments in the field critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b11
  locator: { number: "4.4.b11", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 66825, end: 66912 }
  source: "be able to adopt a range of theoretical perspectives in relation to multiple childhoods"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["adopt"]
  about: "taking up theoretical perspectives"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will take up a range of theoretical perspectives on diverse childhoods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b11.excellent
  locator: { number: "4.4.b11.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 67059, end: 67216 }
  source: "have a high-level ability to adopt multiple theoretical perspectives in relation to early childhood and systematically analyse the relationships between them"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["adopt", "analyse"]
  about: "taking up theoretical perspectives"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b11.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will take up many perspectives on early childhood to a high level and analyse systematically how they relate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b11.masters
  locator: { number: "4.4.b11.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 67217, end: 67370 }
  source: "have an excellent ability to adopt multiple theoretical perspectives in relation to early childhood and critically analyse the relationships between them"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["adopt", "analyse"]
  about: "taking up theoretical perspectives"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will take up many perspectives on early childhood to an excellent level and analyse critically how they relate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b11.typical
  locator: { number: "4.4.b11.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 66913, end: 67058 }
  source: "be able to adopt a range of theoretical perspectives in relation to multiple childhoods and systematically analyse the relationships between them"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["adopt", "analyse"]
  about: "taking up theoretical perspectives"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b11, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will take up a range of such perspectives and analyse systematically how they relate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b12
  locator: { number: "4.4.b12", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 67371, end: 67465 }
  source: "constructively critique theories, practice and research in the area of early childhood studies"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["critique"]
  about: "critiquing theory, practice and research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will critique theory, practice and research in the field constructively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b12.excellent
  locator: { number: "4.4.b12.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 67574, end: 67709 }
  source: "have a high-level ability to analyse and constructively critique theories, practice and research in the area of early childhood studies"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["analyse", "critique"]
  about: "critiquing theory, practice and research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b12.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will analyse and constructively critique theory, practice and research to a high level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b12.masters
  locator: { number: "4.4.b12.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 67710, end: 67856 }
  source: "have an excellent ability to critically analyse and constructively critique theories, practice and research in the area of early childhood studies"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["analyse", "critique"]
  about: "critiquing theory, practice and research"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will analyse critically and critique constructively theory, practice and research, to an excellent level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b12.typical
  locator: { number: "4.4.b12.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 67466, end: 67572 }
  source: "analyse and constructively critique theories, practice and research in the area of early childhood studies"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["analyse", "critique"]
  about: "critiquing theory, practice and research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b12, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will analyse theory, practice and research in the field and critique them constructively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b13
  locator: { number: "4.4.b13", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 67857, end: 68156 }
  source: "reflect upon a range of psychological, sociological, health, welfare, educational, cultural, philosophical, legal, historical, political and economic perspectives, and consider how these underpin different understandings of babies, young children and childhood, at a local, national and global level"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["reflect", "consider"]
  about: "reflecting on disciplinary perspectives"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will reflect on the many disciplinary perspectives on babies, young children and childhood and how each shapes understanding, from local to global."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b13.excellent
  locator: { number: "4.4.b13.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 68490, end: 68817 }
  source: "have a high-level ability to reflect upon a range of psychological, sociological, health, welfare, educational, cultural, philosophical, legal, historical, political and economic perspectives and consider how these underpin different understandings of babies, young children and childhood, at a local, national and global level"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["reflect", "consider"]
  about: "reflecting on disciplinary perspectives"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b13.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will reflect on those perspectives and how they shape understanding, to a high level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b13.masters
  locator: { number: "4.4.b13.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 68818, end: 69157 }
  source: "have an excellent ability to critically reflect upon a range of psychological, sociological, health, welfare, educational, cultural, philosophical, legal, historical, political and economic perspectives\n\nand consider how these underpin different understandings of babies, young children and childhood, at a local, national and global level"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["reflect", "consider"]
  about: "reflecting on disciplinary perspectives"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will reflect critically on those perspectives and how they shape understanding, to an excellent level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b13.typical
  locator: { number: "4.4.b13.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 68157, end: 68489 }
  source: "have a well-developed ability to reflect upon a range of psychological, sociological, health, welfare, educational, cultural, philosophical, legal, historical, political and economic perspectives, and consider how these underpin different understandings of babies, young children and childhood, at a local, national and global level"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["reflect", "consider"]
  about: "reflecting on disciplinary perspectives"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b13, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will reflect on those perspectives and how they shape understanding, in a well-developed way."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b14
  locator: { number: "4.4.b14", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 69304, end: 69449 }
  source: "explore critically the interrelationship between political, economic, cultural and ideological contexts in the lives of babies and young children"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["explore"]
  about: "contexts in young children's lives"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will explore critically how political, economic, cultural and ideological contexts bear on one another in the lives of babies and young children."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b14.excellent
  locator: { number: "4.4.b14.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 69631, end: 69813 }
  source: "have a highly developed ability to explore critically the interrelationships between political,\n\neconomic, cultural and ideological contexts in the lives of babies and young children"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["explore"]
  about: "contexts in young children's lives"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b14.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will explore those interrelations critically, with highly developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b14.masters
  locator: { number: "4.4.b14.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 69814, end: 69989 }
  source: "have an excellent ability to explore critically the interrelationships between political, economic, cultural and ideological contexts in the lives of babies and young children"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["explore"]
  about: "contexts in young children's lives"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will explore those interrelations critically, with excellent ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b14.typical
  locator: { number: "4.4.b14.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 69450, end: 69630 }
  source: "have a well-developed ability to explore critically the interrelationships between political,\n\neconomic, cultural and ideological contexts in the lives of babies and young children"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["explore"]
  about: "contexts in young children's lives"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b14, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will explore those interrelations critically, with well-developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b15
  locator: { number: "4.4.b15", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 69990, end: 70187 }
  source: "explore, examine and evaluate the significance of the cultural, historical and contemporary features of various policies, institutions and agencies in regard to babies, young children and childhood"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["explore", "examine", "evaluate"]
  about: "policies, institutions and agencies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will explore, examine and judge why the cultural, historical and present-day features of policies, institutions and agencies matter for babies, young children and childhood."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b15.excellent
  locator: { number: "4.4.b15.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 70394, end: 70620 }
  source: "have a high-level ability to explore, examine and evaluate the significance of the cultural, historical and contemporary features of various policies, institutions and agencies in regard to babies, young children and childhood"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["explore", "examine", "evaluate"]
  about: "policies, institutions and agencies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b15.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will explore, examine and judge those features to a high level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b15.masters
  locator: { number: "4.4.b15.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 70621, end: 70858 }
  source: "have an excellent ability to critically explore, examine and evaluate the significance of the cultural, historical and contemporary features of various policies, institutions and agencies in regard to babies, young children and childhood"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["explore", "examine", "evaluate"]
  about: "policies, institutions and agencies"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will explore, examine and judge those features critically, to an excellent level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b15.typical
  locator: { number: "4.4.b15.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 70188, end: 70393 }
  source: "critically explore, examine and evaluate the significance of the cultural, historical and contemporary features of various policies, institutions and agencies regarding babies, young children and childhood"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["explore", "examine", "evaluate"]
  about: "policies, institutions and agencies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b15, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will explore, examine and judge those features critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b16
  locator: { number: "4.4.b16", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 70859, end: 71027 }
  source: "evaluate competing positions in relation to the construction of babies, young children and childhood by different subjects, societal agents and time, place and\n\nculture"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["evaluate"]
  about: "competing constructions of childhood"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will weigh competing views of how babies, young children and childhood are constructed by subjects, social agents, time, place and culture."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b16.excellent
  locator: { number: "4.4.b16.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 71185, end: 71394 }
  source: "have a high-level ability to analyse and evaluate competing positions in relation to the construction of babies, young children and childhood by different subjects, societal agents and time, place and\n\nculture"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["analyse", "evaluate"]
  about: "competing constructions of childhood"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b16.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will analyse and weigh those competing views to a high level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b16.masters
  locator: { number: "4.4.b16.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 71395, end: 71614 }
  source: "have an excellent ability to critically analyse and evaluate competing positions in relation to the construction of babies, young children and childhood by different subjects, societal agents and time, place and culture"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["analyse", "evaluate"]
  about: "competing constructions of childhood"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will analyse critically and weigh those competing views, to an excellent level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b16.typical
  locator: { number: "4.4.b16.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 71028, end: 71184 }
  source: "analyse and evaluate competing positions with regards to the social construction of babies, young children and childhood relative to time, place and culture"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["analyse", "evaluate"]
  about: "competing constructions of childhood"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b16, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will analyse and weigh competing views of how childhood is socially constructed across time, place and culture."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b17
  locator: { number: "4.4.b17", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 71615, end: 71719 }
  source: "demonstrate knowledge and awareness of the skills needed for different relational pedagogical approaches"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "skills for relational pedagogy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will know and be aware of the skills that relational pedagogical approaches call for."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b17.excellent
  locator: { number: "4.4.b17.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 71835, end: 71945 }
  source: "have a high-level knowledge and awareness of the skills needed for different relational pedagogical approaches"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: []
  about: "skills for relational pedagogy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b17.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will have high-level knowledge and awareness of those skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b17.masters
  locator: { number: "4.4.b17.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 71946, end: 72056 }
  source: "have an excellent knowledge and awareness of the skills needed for different relational pedagogical approaches"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: []
  about: "skills for relational pedagogy"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will have excellent knowledge and awareness of those skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b17.typical
  locator: { number: "4.4.b17.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 71720, end: 71834 }
  source: "have a well-developed knowledge and awareness of the skills needed for different relational pedagogical approaches"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: []
  about: "skills for relational pedagogy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b17, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will have well-developed knowledge and awareness of those skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b18
  locator: { number: "4.4.b18", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 72057, end: 72160 }
  source: "use skills of observation and analysis in relation to aspects of the lives of babies and young children"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["use"]
  about: "observation and analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will observe and analyse parts of babies' and young children's lives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b18.excellent
  locator: { number: "4.4.b18.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 72275, end: 72396 }
  source: "have highly developed skills of observation and analysis in relation to aspects of the lives of babies and young children"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: []
  about: "observation and analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b18.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will observe and analyse those lives with highly developed skill."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b18.masters
  locator: { number: "4.4.b18.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 72397, end: 72511 }
  source: "have excellent skills of observation and analysis in relation to aspects of the lives of babies and young children"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: []
  about: "observation and analysis"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will observe and analyse those lives with excellent skill."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b18.typical
  locator: { number: "4.4.b18.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 72161, end: 72274 }
  source: "use developed skills of observation and analysis in relation to aspects of the lives of babies and young children"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["use"]
  about: "observation and analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b18, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will observe and analyse those lives with developed skill."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b19
  locator: { number: "4.4.b19", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 72512, end: 72574 }
  source: "identify meaningful patterns in play, behaviour and experience"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["identify"]
  about: "patterns in play, behaviour and experience"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will spot meaningful patterns in play, behaviour and experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b19.excellent
  locator: { number: "4.4.b19.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 72671, end: 72794 }
  source: "have a high-level ability to identify meaningful patterns in play, behaviour and experience and evaluate their significance"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["evaluate", "identify"]
  about: "patterns in play, behaviour and experience"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b19.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will spot such patterns and judge what they mean, to a high level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b19.masters
  locator: { number: "4.4.b19.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 72795, end: 72929 }
  source: "have an excellent ability to identify meaningful patterns in play, behaviour and experience and critically evaluate their significance"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["evaluate", "identify"]
  about: "patterns in play, behaviour and experience"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will spot such patterns and judge critically what they mean, to an excellent level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b19.typical
  locator: { number: "4.4.b19.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 72575, end: 72670 }
  source: "identify meaningful patterns in play, behaviour and experience, and evaluate their significance"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["evaluate", "identify"]
  about: "patterns in play, behaviour and experience"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b19, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will spot such patterns and judge what they mean."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b20
  locator: { number: "4.4.b20", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 73077, end: 73233 }
  source: "demonstrate the ability to be attuned to the perspectives of and, where appropriate, act as an advocate for babies, young children, families and communities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "act"]
  about: "attunement and advocacy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will attune to the views of babies, young children, families and communities and, where fitting, speak up for them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b20.excellent
  locator: { number: "4.4.b20.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 73397, end: 73561 }
  source: "have a highly developed ability to be attuned to the perspectives of and, where appropriate, act as an advocate for babies, young children, families and communities"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["act"]
  about: "attunement and advocacy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b20.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will attune to and, where fitting, advocate for babies, young children, families and communities, with highly developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b20.masters
  locator: { number: "4.4.b20.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 73562, end: 73720 }
  source: "have an excellent ability to be attuned to the perspectives of and, where appropriate, act as an advocate for babies, young children, families and communities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["act"]
  about: "attunement and advocacy"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will attune to and, where fitting, advocate for babies, young children, families and communities, with excellent ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b20.typical
  locator: { number: "4.4.b20.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 73234, end: 73396 }
  source: "have a well-developed ability to be attuned to the perspectives of and, where appropriate, act as an advocate for babies, young children, families and communities"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["act"]
  about: "attunement and advocacy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b20, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will attune to and, where fitting, advocate for babies, young children, families and communities, with well-developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b21
  locator: { number: "4.4.b21", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 73721, end: 73933 }
  source: "demonstrate the ability to plan for, and where appropriate implement, meet and promote children's holistic development, health, well- being, protection and safety, and the conditions which enable them to flourish"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "plan", "implement", "meet", "promote"]
  about: "planning for holistic development, health, protection and safety"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will plan for, and where fitting put in place, provision that protects children, keeps them safe and healthy, supports their all-round development and well-being, and creates the conditions for them to flourish."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b21.excellent
  locator: { number: "4.4.b21.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 74152, end: 74370 }
  source: "have a highly developed ability to plan for, and where appropriate implement, meet and promote children's holistic development, health, well-being, protection and safety, and the conditions that enable them to flourish"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["plan", "implement", "meet", "promote"]
  about: "planning for holistic development, health, protection and safety"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b21.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will plan and, where fitting, put in place provision for children's all-round development, health, well-being, protection and safety, with highly developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b21.masters
  locator: { number: "4.4.b21.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 74371, end: 74586 }
  source: "have an excellent ability to plan for, and where appropriate implement, meet and promote children's holistic development, health, w ell - being, protection and safety, and the conditions that enable them to flourish"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["plan", "implement", "meet", "promote"]
  about: "planning for holistic development, health, protection and safety"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will plan and, where fitting, put in place provision for children's all-round development, health, well-being, protection and safety, with excellent ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b21.typical
  locator: { number: "4.4.b21.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 73934, end: 74151 }
  source: "have a well-developed ability to plan for, and where appropriate implement, meet and promote children's holistic development, health, well-being, protection and safety, and the conditions which enable them to flourish"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["plan", "implement", "meet", "promote"]
  about: "planning for holistic development, health, protection and safety"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b21, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will plan and, where fitting, put in place provision for children's all-round development, health, well-being, protection and safety, with well-developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b22
  locator: { number: "4.4.b22", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 74587, end: 74725 }
  source: "demonstrate the ability to plan for, and where appropriate implement, effective collaborations with parents, carers and other stakeholders"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "plan", "implement"]
  about: "collaboration with parents, carers and other stakeholders"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b22.excellent
  locator: { number: "4.4.b22.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 74871, end: 75017 }
  source: "have a highly developed ability to plan for, and where appropriate implement, effective collaborations with parents, carers and other stakeholders"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["plan", "implement"]
  about: "collaboration with parents, carers and other stakeholders"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b22.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders, with highly developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b22.masters
  locator: { number: "4.4.b22.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 75018, end: 75158 }
  source: "have an excellent ability to plan for, and where appropriate implement, effective collaborations with parents, carers and other stakeholders"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["plan", "implement"]
  about: "collaboration with parents, carers and other stakeholders"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders, with excellent ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b22.typical
  locator: { number: "4.4.b22.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 74726, end: 74870 }
  source: "have a well-developed ability to plan for, and where appropriate implement, effective collaborations with parents, carers and other stakeholders"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["plan", "implement"]
  about: "collaboration with parents, carers and other stakeholders"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b22, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders, with well-developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b23
  locator: { number: "4.4.b23", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 75159, end: 75301 }
  source: "produce critical arguments for improvements to multiagency, multi-professional and inter- professional practices for babies and young children"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["produce"]
  about: "arguing for better joint professional practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will build critical arguments for improving multiagency, multi-professional and inter-professional practice for babies and young children."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b23.excellent
  locator: { number: "4.4.b23.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 75478, end: 75655 }
  source: "have a highly developed ability to produce critical arguments for improvements to multiagency, multi-professional and inter- professional practices for babies and young children"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["produce"]
  about: "arguing for better joint professional practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b23.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will build such arguments with highly developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b23.masters
  locator: { number: "4.4.b23.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 75656, end: 75826 }
  source: "have an excellent ability to produce critical arguments for improvements to multiagency, multi-professional and inter-professional practices for babies and young children"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["produce"]
  about: "arguing for better joint professional practice"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will build such arguments with excellent ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b23.typical
  locator: { number: "4.4.b23.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 75302, end: 75477 }
  source: "have a well-developed ability to produce critical arguments for improvements to multiagency, multi-professional and inter- professional practices for babies and young children"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["produce"]
  about: "arguing for better joint professional practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b23, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will build such arguments with well-developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b24
  locator: { number: "4.4.b24", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 75827, end: 75978 }
  source: "demonstrate the ability to recognise and challenge inequalities and social justice in society and to embrace anti-bias and anti- oppressive approaches."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "recognise", "challenge", "embrace"]
  about: "challenging inequality"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will recognise and challenge inequality and injustice in society and take up anti-bias, anti-oppressive approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b24.excellent
  locator: { number: "4.4.b24.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 76139, end: 76301 }
  source: "have a highly developed ability to recognise and challenge inequalities and social justice in society and to embrace an anti-bias\n\nand anti-oppressive approaches."
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["recognise", "challenge", "embrace"]
  about: "challenging inequality"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b24.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will recognise and challenge inequality and injustice and take up anti-bias, anti-oppressive approaches, with highly developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b24.masters
  locator: { number: "4.4.b24.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 76302, end: 76458 }
  source: "have an excellent ability to recognise and challenge inequalities and social justice in society and to embrace an anti-bias\n\nand anti-oppressive approaches."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["recognise", "challenge", "embrace"]
  about: "challenging inequality"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will recognise and challenge inequality and injustice and take up anti-bias, anti-oppressive approaches, with excellent ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b24.typical
  locator: { number: "4.4.b24.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 75979, end: 76138 }
  source: "have a well-developed ability to recognise and challenge inequalities and social justice in society and to embrace an anti-bias\n\nand anti-oppressive approaches"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["recognise", "challenge", "embrace"]
  about: "challenging inequality"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b24, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will recognise and challenge inequality and injustice and take up anti-bias, anti-oppressive approaches, with well-developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b25
  locator: { number: "4.4.b25", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 76459, end: 76591 }
  source: "demonstrate the ability to lead, mentor, facilitate and work collaboratively with others in order to support transformational change"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "lead", "mentor", "facilitate", "work", "support"]
  about: "leadership for transformational change"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will lead, mentor, facilitate and collaborate with others to bring about transformational change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b25.excellent
  locator: { number: "4.4.b25.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 76731, end: 76871 }
  source: "have a highly developed ability to lead, mentor, facilitate and work collaboratively with others in order to support transformational change"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["lead", "mentor", "facilitate", "work", "support"]
  about: "leadership for transformational change"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b25.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will lead, mentor, facilitate and collaborate with others to bring about transformational change, with highly developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b25.masters
  locator: { number: "4.4.b25.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 76872, end: 77034 }
  source: "have professional confidence and an excellent ability to lead, mentor, facilitate and work collaboratively with others in order to support transformational change"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["lead", "mentor", "facilitate", "work", "support"]
  about: "leadership for transformational change"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will show professional confidence and lead, mentor, facilitate and collaborate with others to an excellent level to bring about transformational change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b25.typical
  locator: { number: "4.4.b25.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 76592, end: 76730 }
  source: "have a well-developed ability to lead, mentor, facilitate and work collaboratively with others in order to support transformational change"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["lead", "mentor", "facilitate", "work", "support"]
  about: "leadership for transformational change"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b25, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will lead, mentor, facilitate and collaborate with others to bring about transformational change, with well-developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b26
  locator: { number: "4.4.b26", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 77181, end: 77345 }
  source: "pose and operationalise research questions in relation to early childhood and demonstrate competence in research skills through practical and theoretical activities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "pose", "operationalise"]
  about: "research questions and research competence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will pose research questions about early childhood, put them into operation, and show research competence through practical and theoretical work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b26.excellent
  locator: { number: "4.4.b26.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 77518, end: 77741 }
  source: "have a highly developed ability to pose, operationalise and critique research questions related to early childhood, and demonstrate a good\n\nlevel of competence in research skills through practical and theoretical activities"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "critique", "pose", "operationalise"]
  about: "research questions and research competence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b26.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will pose, operationalise and critique research questions with highly developed ability, showing a good level of research competence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b26.masters
  locator: { number: "4.4.b26.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 77742, end: 77970 }
  source: "have an excellent ability to pose, operationalise and critique research questions related to early childhood, and demonstrate a highly developed level of competence in research skills through practical and theoretical activities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["demonstrate", "critique", "pose", "operationalise"]
  about: "research questions and research competence"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will pose, operationalise and critique research questions with excellent ability, showing highly developed research competence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b26.typical
  locator: { number: "4.4.b26.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 77346, end: 77517 }
  source: "pose, operationalise and critique research questions related to early childhood, and demonstrate competence in research skills through practical and theoretical activities"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["demonstrate", "critique", "pose", "operationalise"]
  about: "research questions and research competence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b26, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will pose, operationalise and critique research questions on early childhood and show research competence in practice and in theory."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b27
  locator: { number: "4.4.b27", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 77971, end: 78091 }
  source: "initiate, design, conduct and report an empirically based early childhood research project under appropriate supervision"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["initiate", "design", "conduct", "report"]
  about: "the supervised research project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will start, design, carry out and report a supervised empirical research project on early childhood."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b27.excellent
  locator: { number: "4.4.b27.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 78297, end: 78564 }
  source: "initiate, design, conduct and report an early childhood research project under appropriate supervision with a high degree of competence, and demonstrate a highly developed ability to recognise its theoretical, practical and methodological implications and limitations"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "recognise", "initiate", "design", "conduct", "report"]
  about: "the supervised research project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b27.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will carry out the whole project, from start to report, with a high degree of competence, recognising with highly developed ability what it implies and where it falls short."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b27.masters
  locator: { number: "4.4.b27.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 78565, end: 78826 }
  source: "independently initiate, design, conduct and report an early childhood research project with appropriate supervision, evidencing\n\na high degree of competence and reflexive engagement with its theoretical, practical and methodological implications and limitations"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["initiate", "design", "conduct", "report"]
  about: "the supervised research project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will carry out the whole project independently with supervision, showing high competence and reflexive engagement with what it implies and where it falls short."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b27.typical
  locator: { number: "4.4.b27.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 78092, end: 78296 }
  source: "competently initiate, design, conduct and report an early childhood research project under appropriate supervision, and recognise its theoretical, practical and methodological implications and limitations"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["recognise", "initiate", "design", "conduct", "report"]
  about: "the supervised research project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b27, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will start, design, carry out and report such a project competently, recognising what it implies and where it falls short in theory, practice and method."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b28
  locator: { number: "4.4.b28", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 78827, end: 78914 }
  source: "reflect upon the ethics of studying babies and young children, families and communities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["reflect"]
  about: "the ethics of studying children"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will reflect on the ethics of studying babies, young children, families and communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b28.excellent
  locator: { number: "4.4.b28.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 79037, end: 79153 }
  source: "have a high-level ability to reflect upon the ethics of studying babies and young children, families and communities"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["reflect"]
  about: "the ethics of studying children"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b28.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will reflect on those ethics with high-level ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b28.masters
  locator: { number: "4.4.b28.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 79154, end: 79270 }
  source: "have an excellent ability to reflect upon the ethics of studying babies and young children, families and communities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["reflect"]
  about: "the ethics of studying children"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will reflect on those ethics with excellent ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b28.typical
  locator: { number: "4.4.b28.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 78915, end: 79036 }
  source: "have a well-developed ability to reflect upon the ethics of studying babies and young children, families\n\nand communities"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["reflect"]
  about: "the ethics of studying children"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b28, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will reflect on those ethics with well-developed ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b29
  locator: { number: "4.4.b29", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 79271, end: 79403 }
  source: "be aware of ethical principles and demonstrate this in relation to personal study, particularly with regard to the research project."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "ethical principles in the research project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will know the ethical principles involved and show this in personal study, above all the research project."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b29.excellent
  locator: { number: "4.4.b29.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 79568, end: 79724 }
  source: "be aware of the complexity of ethical principles and issues, and apply this in relation to personal study, particularly with regard to the research project."
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["apply"]
  about: "ethical principles in the research project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b29.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will be aware of that complexity and apply it in personal study, above all the research project."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b29.masters
  locator: { number: "4.4.b29.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 79725, end: 79916 }
  source: "well-considered reflexive engagement with the complexity of ethical principles and issues, and synthesise this in relation to personal study, particularly with regard to the research project."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["synthesise"]
  about: "ethical principles in the research project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will engage reflexively and with care with that complexity and synthesise it in personal study, above all the research project."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b29.typical
  locator: { number: "4.4.b29.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 79404, end: 79567 }
  source: "be aware of the complexity of ethical principles and issues, and demonstrate this in relation to personal study, particularly with regard to t he research project."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "ethical principles in the research project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b29, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will be aware of how complex ethical principles and issues are and show this in personal study, above all the research project."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b30
  locator: { number: "4.4.b30", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 79977, end: 80055 }
  source: "present a range of theoretical positions and offer and justify a point of view"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["present", "offer", "justify"]
  about: "arguing a point of view from theory"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will set out a range of theoretical positions and give and defend a point of view."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b30.excellent
  locator: { number: "4.4.b30.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 80154, end: 80267 }
  source: "present a wide range of theoretical positions and offer and justify a well-informed and insightful point of\n\nview"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["present", "offer", "justify"]
  about: "arguing a point of view from theory"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b30.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will set out a wide range of positions and give and defend a well-informed and insightful view."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b30.masters
  locator: { number: "4.4.b30.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 80268, end: 80423 }
  source: "detailed and accurate knowledge of a wide range of theoretical positions and be able to articulate and justify a well-informed and insightful point of view"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["justify", "articulate"]
  about: "arguing a point of view from theory"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will know a wide range of positions in accurate detail and articulate and defend a well-informed, insightful view."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b30.typical
  locator: { number: "4.4.b30.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 80056, end: 80153 }
  source: "present a wide range of theoretical positions and offer and justify a well-informed point of view"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["present", "offer", "justify"]
  about: "arguing a point of view from theory"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b30, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will set out a wide range of positions and give and defend a well-informed view."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b31
  locator: { number: "4.4.b31", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 80570, end: 80607 }
  source: "use a range of sources of information"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["use"]
  about: "using sources of information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will draw on a range of information sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b31.excellent
  locator: { number: "4.4.b31.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 80657, end: 80727 }
  source: "use a wide range of sources of information critically and with insight"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["use"]
  about: "using sources of information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b31.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will draw on a wide range of information sources critically and with insight."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b31.masters
  locator: { number: "4.4.b31.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 80728, end: 80806 }
  source: "engage with a wide range of sources of information critically and with insight"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["engage"]
  about: "using sources of information"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will engage critically and with insight with a wide range of information sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b31.typical
  locator: { number: "4.4.b31.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 80608, end: 80656 }
  source: "use a range of sources of information critically"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["use"]
  about: "using sources of information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b31, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will draw on a range of information sources critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b32
  locator: { number: "4.4.b32", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 80807, end: 80889 }
  source: "listen carefully to others and reflect upon one's own and others' skills and views"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["reflect", "listen"]
  about: "listening and reflecting on skills and views"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will listen carefully and reflect on their own and others' skills and views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b32.excellent
  locator: { number: "4.4.b32.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 80984, end: 81094 }
  source: "listen carefully to others and reflect critically and insightfully upon one's own and others' skills and views"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["reflect", "listen"]
  about: "listening and reflecting on skills and views"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b32.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will listen carefully and reflect critically and with insight on their own and others' skills and views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b32.masters
  locator: { number: "4.4.b32.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 81095, end: 81205 }
  source: "listen carefully to others and reflect critically and analytically upon one's own and others' skills and views"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["reflect", "listen"]
  about: "listening and reflecting on skills and views"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will listen carefully and reflect critically and analytically on their own and others' skills and views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b32.typical
  locator: { number: "4.4.b32.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 80890, end: 80983 }
  source: "listen carefully to others and critically reflect upon one's own and others' skills and views"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["reflect", "listen"]
  about: "listening and reflecting on skills and views"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b32, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will listen carefully and reflect critically on their own and others' skills and views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b33
  locator: { number: "4.4.b33", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 81206, end: 81294 }
  source: "recognise the need to assess one's own skills and to reflect on them for future learning"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["reflect", "recognise", "assess"]
  about: "managing own learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will see that their own skills need assessing and reflect on them to guide later learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b33.excellent
  locator: { number: "4.4.b33.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 81435, end: 81592 }
  source: "show sophistication in taking charge of one's own learning, reflect and be reflexive of personal strengths and weaknesses for the purposes of future learning"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["reflect", "show"]
  about: "managing own learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b33.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will take charge of their own learning with sophistication, reflecting reflexively on their own strengths and weaknesses for later learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b33.masters
  locator: { number: "4.4.b33.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 81593, end: 81746 }
  source: "evidence sophistication in leading one's own learning, evaluate and be reflexive of personal strengths and weaknesses for the purposes of future learning"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["evaluate", "evidence"]
  about: "managing own learning"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will lead their own learning with sophistication, evaluating their own strengths and weaknesses reflexively for later learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b33.typical
  locator: { number: "4.4.b33.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 81295, end: 81434 }
  source: "be able to take charge of one's own learning and reflect and evaluate personal strengths and weaknesses for the purposes of future learning"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["reflect", "evaluate", "take"]
  about: "managing own learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b33, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will take charge of their own learning and weigh up their own strengths and weaknesses to guide later learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b34
  locator: { number: "4.4.b34", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 81747, end: 81907 }
  source: "have the ability to use digital technologies/literacies appropriately as part of the learning\n\nprocess in a range of contexts to enhance provision for children."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard"
  addressee: learner
  verbs: ["use", "enhance"]
  about: "digital technologies and literacies"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours award, the graduate will use digital technologies and literacies appropriately in learning, across settings, to improve provision for children."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b34.excellent
  locator: { number: "4.4.b34.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 82072, end: 82227 }
  source: "show sophistication in the use of digital technologies/literacies as part of the learning process in a range of contexts to enhance provision for children."
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["use", "show", "enhance"]
  about: "digital technologies and literacies"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b34.typical, basis: stated }
  paraphrase: "At the excellent standard, the honours graduate will use digital technologies and literacies with sophistication in learning, across settings, to improve provision for children."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b34.masters
  locator: { number: "4.4.b34.masters", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 82228, end: 82411 }
  source: "critically and professionally engage with digital technologies/literacies with sophistication as part of the learning process in a range of contexts to enhance provision for children."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["engage", "enhance"]
  about: "digital technologies and literacies"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the postgraduate standard, the master's student will engage critically, professionally and with sophistication with digital technologies and literacies in learning, across settings, to improve provision for children."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/early-childhood-studies-2022/4.4.b34.typical
  locator: { number: "4.4.b34.typical", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 81908, end: 82071 }
  source: "be confident in the use of digital technologies/literacies appropriately as part of the learning\n\nprocess in a range of contexts to enhance provision for children."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["use", "enhance"]
  about: "digital technologies and literacies"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/early-childhood-studies-2022/4.4.b34, basis: stated }
  paraphrase: "At the typical standard, the honours graduate will use digital technologies and literacies appropriately and with confidence in learning, across settings, to improve provision for children."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/early-childhood-studies-2022/1.18
  forPractitioner: { text: "If your course offers the Level 6 practitioner competencies, the expectation is that your institution belongs to the degrees network that writes and reviews them.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition on the institution that offers the competencies", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a provider expectation, not a student outcome: an institution offering the Level 6 practitioner competencies is expected to belong to the degrees network (the issuer's word is expectation, recorded as describes). Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.18. Do not claim the competencies are required of every degree or that membership is a regulatory condition. Set it beside 1.19, 2.20 and 2.25, reading Level 6 as FHEQ level 6 (qaa/fheq-2024/4.15) only by inference."
  author-agent-dialogue: "Raise it with a programme team weighing whether to embed the practitioner competencies. Put it as a membership condition on the institution, not a task for students. Ask: is the institution a current member, and how would the competencies be assessed on placement? Avoid presenting it to students as a requirement of their degree."
- statement: qaa/early-childhood-studies-2022/1.20
  forPractitioner: { text: "If you advertise that the degree qualifies graduates to practise in early years settings, you must meet the requirements of the UK nation where each student studies.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the awarding institution", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a provider duty with the force must: an institution claiming that its degree permits early years practice has to meet the requirements of the student's nation. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.20. Do not state that every early childhood degree licenses practice, or that one nation's rules apply across the UK. Set it beside 1.17, 1.25 and 2.20."
  author-agent-dialogue: "Raise it when a programme team describes the degree as a route into early years practice. Frame it for staff as a compliance check, nation by nation. Ask: which nation's requirements does each cohort fall under, and where is the evidence that the course meets them? Do not put this duty to a student as something they must do."
- statement: qaa/early-childhood-studies-2022/1.23
  forPractitioner: { text: "Students at every level should be helped to keep questioning dominant ways of thinking about knowledge and power, with equality treated as an ethical and human-rights question that underpins anti-oppressive practice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should keep questioning the language and assumptions of dominant ways of thinking about knowledge and power, and treat equality as a matter of ethics and human rights.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation of students at undergraduate and postgraduate level, from the equality, diversity and inclusion theme. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.23. Do not present it as a graded outcome or as a legal duty. Set it beside 1.24, the inequality row of the section 4 table (4.4.b24) and qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student or team discusses whose knowledge a module puts first. With a student, invite them to notice the assumptions in their readings; with staff, ask where the curriculum makes room for that questioning. Ask: whose voices are missing from this topic, and why? Avoid lecturing the student or quoting the paragraph at length."
- statement: qaa/early-childhood-studies-2022/1.24
  forPractitioner: { text: "Teaching will challenge dominant knowledge and widen representation; students will be pushed to make their own pedagogical judgements with EDI in mind, and the institution will have proactive, inclusive support in place.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be stretched to question different realities critically and reach your own judgements about teaching and care, keeping equality and inclusion in view, with support from your institution.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level expectation that binds teaching and institutional support, from the equality, diversity and inclusion theme, on undergraduate and postgraduate courses. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.24. Do not describe it as measured attainment at a set level. Set it beside 1.23, 1.25 and 3.11."
  author-agent-dialogue: "Raise it when reviewing how a module handles diverse perspectives, or when a student feels unsupported. For a student, say plainly that you can expect to be both challenged and supported; for staff, ask what evidence shows proactive support. Ask: where in this course are marginalised voices represented? Avoid promising a particular support service by name."
- statement: qaa/early-childhood-studies-2022/1.25
  forPractitioner: { text: "Courses will be equitable and respect what each student brings, and should build critical reflection across theory, practice from birth to eight and disciplines. Placements that qualify students for early years practice must meet the guidance of the student's nation, and students should still gain experience across ages and across health, social care and education.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course will respect who you are and what you bring, and should help you reflect critically on theory and practice from birth to eight; you should gain placement experience across that age range and across health, social care and education.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this paragraph as mixed in force: will for equitable courses that respect students' identities, should for critical reflection and for experience across birth to eight, and must for placements that qualify students for early years practice, which have to follow each nation's guidance. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.25. Do not let the must spread to the whole paragraph or claim placements are required of every degree. Set it beside 1.20, 1.26 and 2.16."
  author-agent-dialogue: "Raise it when planning placements, or when a student asks why they work outside early years settings. With a student, explain plainly that experience across ages and sectors is part of the design; with staff, check placement assessments against the guidance of the student's nation. Ask: does the placement plan reach the whole birth-to-eight range and more than one sector? Avoid suggesting that every student must take a qualifying placement."
- statement: qaa/early-childhood-studies-2022/1.26
  forPractitioner: { text: "Any placement or work-based element you offer must be clearly scoped, mentored, monitored, accessible and supervised, so that it teaches the link between theory and inclusive practice.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course that offers placements", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a provider duty with the force must, applying only where a course offers placement or work-based learning. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.26. Do not claim that every course has to include placements. Set it beside 1.25, 2.16 and 3.10."
  author-agent-dialogue: "Raise it when a team designs or reviews placement arrangements. Frame it for staff as five tests each placement has to pass: defined, mentored, monitored, accessible, supervised. Ask: which of the five is weakest in the current placements, and what evidence shows it? Avoid presenting it to students as their duty."
- statement: qaa/early-childhood-studies-2022/1.31
  forPractitioner: { text: "The course should give students chances to explore sustainability, social justice, democratic action and advocacy at personal, professional, community, national and global scales, so that they can show how ecology and social justice connect.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should have chances to explore sustainability, social justice, democracy and advocacy, from your own life to the global scale, and to show how caring for the planet and fairness in society connect.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on degrees from the education for sustainable development theme, with a stated graduate result: seeing how ecology and sustainable societies link through social justice. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.31, with the joint guidance it draws on (std:doc:qaa-advancehe-esd-2021-guidance). Do not present it as a measured threshold or a regulatory rule. Set it beside 1.27 to 1.30 and the rights and sustainability row of the section 4 table (4.4.b6)."
  author-agent-dialogue: "Raise it when a team maps where sustainability sits in the course, or a student asks why it matters in early years work. With a student, ask plainly how fairness and care for the environment meet in children's lives; with staff, ask where students act on it, not only read about it. Ask: at which scale, from personal to global, does the course give least room? Avoid treating sustainability as an add-on topic."
- statement: qaa/early-childhood-studies-2022/1.33
  forPractitioner: { text: "Graduates will be well placed to add social, cultural and economic value; course design can build this through leadership, innovation and knowledge exchange with the sector.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be well placed to add social, cultural and economic value, helping to lead new practice and to raise the standing of early years work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level expected outcome for students and graduates from the enterprise theme, not a graded standard. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.33. Do not claim it sets an employment outcome a course must report. Set it beside 1.32, 1.34 to 1.36 and qaa/fheq-2024/4.15.b9.1, with spine:6."
  author-agent-dialogue: "Raise it when a student asks what difference their degree can make, or when a team plans enterprise and employability work. With a student, ask plainly where they see themselves adding value; with staff, ask which activities let students lead or innovate. Ask: what change in practice or in a setting could you help bring about? Avoid overpromising careers or pay."
- statement: qaa/early-childhood-studies-2022/1.35
  forPractitioner: { text: "Students should be building enterprising behaviours (initiative, reflection, communication, adaptability, responsibility, networking, managed risk) and attributes such as curiosity, self-efficacy and resilience; plan where each is practised.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be building the habits early years work needs, such as taking initiative, reflecting, communicating, adapting, taking responsibility, networking and judging risk, along with curiosity, open-mindedness and resilience.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation of students from the enterprise theme, set for professional work at different levels rather than one award level. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.35. Do not claim it lists assessed outcomes or a fixed set of competencies. Set it beside 1.36 and qaa/fheq-2024/4.15.b9.1 (initiative and personal responsibility)."
  author-agent-dialogue: "Raise it in personal tutoring or placement review, when a student reflects on how they work. Ask the student plainly which of these habits they already show and which they want to build. Ask: when did you last take the initiative or manage a risk in practice, and what did you learn? Avoid reading the list as a checklist to tick."
- statement: qaa/early-childhood-studies-2022/1.36.b1
  forPractitioner: { text: "Build in opportunities for students to develop confidence in intuitive professional decisions and in spotting opportunities.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course is meant to give you chances to develop confidence in intuitive professional decisions and in spotting opportunities.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a provider expectation from the enterprise theme (worded 'are to be provided', recorded as describes, not must): opportunities for students and postgraduates to develop intuitive professional decisions and spotting opportunities. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.36. Do not claim it is a graduate outcome with a set level or a regulatory duty. Set it beside 1.35, the generic skills in 3.4 and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Raise it when a student hesitates to make decisions in practice. With a student, say plainly that the course should give them room to build this; with staff, ask where these opportunities sit in the course. Ask: When did you trust your own judgement in practice, and how did it turn out? Avoid turning it into a test the student must pass."
- statement: qaa/early-childhood-studies-2022/1.36.b2
  forPractitioner: { text: "Build in opportunities for students to develop creative problem-solving.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course is meant to give you chances to develop creative problem-solving.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a provider expectation from the enterprise theme (worded 'are to be provided', recorded as describes, not must): opportunities for students and postgraduates to develop creative problem-solving. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.36. Do not claim it is a graduate outcome with a set level or a regulatory duty. Set it beside 1.35, the generic skills in 3.4 and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Raise it when a team plans problem-based tasks. With a student, say plainly that the course should give them room to build this; with staff, ask where these opportunities sit in the course. Ask: What problem did you solve in a way no one had suggested? Avoid turning it into a test the student must pass."
- statement: qaa/early-childhood-studies-2022/1.36.b3
  forPractitioner: { text: "Build in opportunities for students to develop innovative, strategic thinking.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course is meant to give you chances to develop innovative, strategic thinking.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a provider expectation from the enterprise theme (worded 'are to be provided', recorded as describes, not must): opportunities for students and postgraduates to develop innovative and strategic thinking. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.36. Do not claim it is a graduate outcome with a set level or a regulatory duty. Set it beside 1.35, the generic skills in 3.4 and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Raise it when a student plans change in a setting. With a student, say plainly that the course should give them room to build this; with staff, ask where these opportunities sit in the course. Ask: What would you change about this setting if you were planning five years ahead? Avoid turning it into a test the student must pass."
- statement: qaa/early-childhood-studies-2022/1.36.b4
  forPractitioner: { text: "Build in opportunities for students to develop negotiation and communication, critical digital literacy among them.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course is meant to give you chances to develop negotiation and communication, critical digital literacy among them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a provider expectation from the enterprise theme (worded 'are to be provided', recorded as describes, not must): opportunities for students and postgraduates to develop negotiation, communication and critical digital literacy. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.36. Do not claim it is a graduate outcome with a set level or a regulatory duty. Set it beside 1.35, the generic skills in 3.4 and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Raise it when a student weighs online sources or negotiates in practice. With a student, say plainly that the course should give them room to build this; with staff, ask where these opportunities sit in the course. Ask: How do you check whether online information can be trusted? Avoid turning it into a test the student must pass."
- statement: qaa/early-childhood-studies-2022/1.36.b5
  forPractitioner: { text: "Build in opportunities for students to develop leadership.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course is meant to give you chances to develop leadership.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a provider expectation from the enterprise theme (worded 'are to be provided', recorded as describes, not must): opportunities for students and postgraduates to develop leadership. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.36. Do not claim it is a graduate outcome with a set level or a regulatory duty. Set it beside 1.35, the generic skills in 3.4 and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Raise it when a student is offered a chance to lead. With a student, say plainly that the course should give them room to build this; with staff, ask where these opportunities sit in the course. Ask: Where have you had a chance to lead, and what did you learn? Avoid turning it into a test the student must pass."
- statement: qaa/early-childhood-studies-2022/1.36.b6
  forPractitioner: { text: "Build in opportunities for students to develop collaboration among children, colleagues, employers and students that builds knowledge and trust through mutual respect.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course is meant to give you chances to develop collaboration among children, colleagues, employers and students that builds knowledge and trust through mutual respect.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a provider expectation from the enterprise theme (worded 'are to be provided', recorded as describes, not must): opportunities for students and postgraduates to develop collaborative relationships built on respect. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.36. Do not claim it is a graduate outcome with a set level or a regulatory duty. Set it beside 1.35, the generic skills in 3.4 and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Raise it when a team plans work with employers or children. With a student, say plainly that the course should give them room to build this; with staff, ask where these opportunities sit in the course. Ask: Who outside your course have you learned alongside? Avoid turning it into a test the student must pass."
- statement: qaa/early-childhood-studies-2022/1.36.b7
  forPractitioner: { text: "Build in opportunities for students to develop open-mindedness that values varied capabilities and knowledge and supports responsive, interdependent learning together.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course is meant to give you chances to develop open-mindedness that values varied capabilities and knowledge and supports responsive, interdependent learning together.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a provider expectation from the enterprise theme (worded 'are to be provided', recorded as describes, not must): opportunities for students and postgraduates to develop open-mindedness and responsive shared learning. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.36. Do not claim it is a graduate outcome with a set level or a regulatory duty. Set it beside 1.35, the generic skills in 3.4 and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Raise it when a student meets views or abilities unlike their own. With a student, say plainly that the course should give them room to build this; with staff, ask where these opportunities sit in the course. Ask: When did someone's different experience change your mind? Avoid turning it into a test the student must pass."
- statement: qaa/early-childhood-studies-2022/1.36.b8
  forPractitioner: { text: "Build in opportunities for students to develop recognition of, and respect for, each person's uniqueness and what they bring.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course is meant to give you chances to develop recognition of, and respect for, each person's uniqueness and what they bring.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a provider expectation from the enterprise theme (worded 'are to be provided', recorded as describes, not must): opportunities for students and postgraduates to develop respect for each person's uniqueness. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 1.36. Do not claim it is a graduate outcome with a set level or a regulatory duty. Set it beside 1.35, the generic skills in 3.4 and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Raise it when a team reviews how inclusive its groups are. With a student, say plainly that the course should give them room to build this; with staff, ask where these opportunities sit in the course. Ask: How does this course show it values what each person brings? Avoid turning it into a test the student must pass."
- statement: qaa/early-childhood-studies-2022/2.1
  forPractitioner: { text: "Degrees should build in what social justice, children's rights, children's cultures and EDI require, applied to the development, well-being, participation and learning of every childhood from conception to eight.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on how degrees are designed", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level design expectation on degrees, which also sets the field's age range at conception to eight and its focus on holistic development. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.1. Do not narrow the field to school readiness or to the under-fives. Set it beside 1.1, 1.2, 2.2 and the rights and equity row of the section 4 table (4.4.b6)."
  author-agent-dialogue: "Raise it when a team checks whether the curriculum spans the whole age range and all childhoods. Frame it for staff as a coverage question. Ask: where does the course address children before birth, and from five to eight? Avoid giving this to a student as a duty."
- statement: qaa/early-childhood-studies-2022/2.4
  forPractitioner: { text: "Your course design will need to show how teaching and assessment are made accessible and inclusive, including support for disabled students and, where fitting, a decolonised curriculum.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level expectation on course design from the accessibility section. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.4. Do not claim it imposes a specific legal duty or a set method such as decolonising, which the text offers as a possibility. Set it beside 2.8, 2.10 and 3.12."
  author-agent-dialogue: "Raise it when a team reviews a module for access or when a student reports a barrier. For staff, ask how a disabled student, or one with other needs, would meet each assessment. Ask: what in this module would stop a student with different needs from taking part fully? Avoid telling the student it is their job to remove the barrier."
- statement: qaa/early-childhood-studies-2022/2.7
  forPractitioner: { text: "Plan a mix of delivery modes and of placement or simulated settings across sectors: social care, health, social enterprise, local authority, family support, charities, policy, outdoor learning, early years and schools.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on how the course is delivered", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on delivery, with the listed settings as examples, not a required set. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.7. Do not claim every listed setting has to be used. Set it beside 1.25, 2.16 and 2.19."
  author-agent-dialogue: "Raise it when a team plans its mix of teaching modes or placement settings. Ask staff which sectors students meet beyond early years settings. Ask: could a student graduate having seen only one kind of setting? Avoid reading the list of settings as a quota."
- statement: qaa/early-childhood-studies-2022/2.8
  forPractitioner: { text: "Use varied, accessible assessment, real-world tasks where you can, room for reasonable adjustments and assistive technology, and tasks that keep students' digital skills current (section 3 gives the methods).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on assessment design, joining the accessibility section to employability. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.8. Do not claim it fixes particular assessment types. Set it beside 2.9, 3.12, 3.13 and 3.14."
  author-agent-dialogue: "Raise it when a team reviews an assessment strategy or a student asks for an adjustment. For staff, ask how each task reflects real situations and allows adjustment. Ask: which assessment here would be hardest for a disabled student, and what adjustment is ready? Avoid quoting the paragraph to a student in place of help."
- statement: qaa/early-childhood-studies-2022/2.9
  forPractitioner: { text: "Match each assessment to the level of study and build on what students were assessed on before they arrived, academic or vocational.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that assessment is pitched at the level of study. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.9. Do not claim it sets the level itself; take that from the framework descriptors (qaa/fheq-2024/4.15 at level 6). Set it beside 2.8 and 3.16."
  author-agent-dialogue: "Raise it when a team checks that tasks grow in demand year by year or serve students from vocational routes. Ask staff how first-year tasks connect with students' earlier qualifications. Ask: is this task harder than last year's in a way the level descriptor would recognise? Avoid treating it as a student duty."
- statement: qaa/early-childhood-studies-2022/2.10
  forPractitioner: { text: "Make physical and online spaces accessible and keep a climate where different views are welcome and debate is critical and research-informed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the learning environment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the learning environment from the accessibility section. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.10. Do not claim it sets a standard for facilities. Set it beside 2.4 and 2.8."
  author-agent-dialogue: "Raise it when a team reviews the learning climate, or a student says their view was not welcome. For staff, ask how disagreement is handled in seminars and online. Ask: would a student with an unpopular view feel safe to voice it here? Avoid dismissing the student's experience."
- statement: qaa/early-childhood-studies-2022/2.11
  forPractitioner: { text: "Plan each year so that knowledge, expertise and experience build towards every threshold skill in the statement by graduation; a lower second or above is expected to equip graduates for postgraduate study.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Each year of your honours course builds towards the full set of minimum skills you need at graduation, and with a second-class degree or better you would be expected to be ready for postgraduate study.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a described expectation (the issuer writes 'it is expected'), not a must: each year builds towards all the threshold skills by the end of the honours degree, at FHEQ level 6 and FQHEIS level 10. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.11. Do not claim a second-class degree guarantees a postgraduate place. Set it beside the threshold column of the section 4 table and qaa/fheq-2024/4.15, with spine:6."
  author-agent-dialogue: "Raise it when a student asks how the years fit together or whether they could go on to a master's. With a student, say plainly that each year builds towards the minimum skills for graduation; with staff, ask where each threshold skill first appears. Ask: which of the minimum skills feel least secure for you now? Avoid presenting a second-class degree as a promise of further study."
- statement: qaa/early-childhood-studies-2022/2.12
  forPractitioner: { text: "Joint honours graduates will meet part of this subject's skill set alongside their other subject's; design the combination so that it supports progression to postgraduate study.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study the subject within joint honours, you will gain some of its subject-specific and general skills and add others from your second subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level outcome for joint honours students at FHEQ level 6: they meet part of the subject's skills, not all. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.12. Do not claim joint honours graduates have to meet every threshold item. Set it beside 4.3, 3.3 and 3.4."
  author-agent-dialogue: "Raise it when a joint honours student asks which skills they are expected to show. Say plainly that they will cover part of this subject's skills and add others; with a team, ask which items the joint route covers. Ask: which of this subject's skills does your other subject strengthen? Avoid holding joint honours students to the full single honours list."
- statement: qaa/early-childhood-studies-2022/2.14
  forPractitioner: { text: "Design for critical reflection and high-quality practice, keep teaching balanced across disciplines rather than led by one, follow research debates and changing law and guidance, and leave room for students' career paths.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on how degrees are designed", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level design expectation: balance across disciplines, critical reflection and high-quality practice. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.14. Do not claim a degree may centre on early education alone and still meet it. Set it beside 1.2, 2.2 and 2.16."
  author-agent-dialogue: "Raise it when a team reviews the balance of modules across health, social care, education and other fields. Ask staff to count credits by discipline. Ask: does one discipline dominate, and what is lost if it does? Avoid giving it to a student as their duty."
- statement: qaa/early-childhood-studies-2022/2.15
  forPractitioner: { text: "Show students a route onward to doctoral study (professional doctorate or PhD) from your honours and master's provision.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the range of courses offered", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that courses leave a path to doctoral study, and as the statement's account of the courses it serves. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.15. Do not claim it sets doctoral standards; doctoral level is FHEQ level 8 (qaa/fheq-2024/4.18), which the statement does not cover. Set it beside 1.6, 2.13 and 4.2."
  author-agent-dialogue: "Raise it when a master's team discusses progression or a student asks about a PhD. For staff, ask what research preparation opens the doctoral route. Ask: what would a graduate of this course need to apply for a doctorate? Avoid presenting doctoral entry as assured."
- statement: qaa/early-childhood-studies-2022/2.16
  forPractitioner: { text: "In a ladder of awards, show how understanding deepens from step to step, including EDI and sustainability; design any placement with each UK nation's requirements in mind but reach beyond early years settings and schools.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on course and placement design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on suites of linked qualifications and on placement design, carrying both the EDI and the sustainability themes. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.16. Do not claim it requires every course to offer placements. Set it beside 1.25, 1.26 and 2.7, and the steps qaa/fheq-2024/4.12, qaa/fheq-2024/4.15 and qaa/fheq-2024/4.17 for the levels of a suite."
  author-agent-dialogue: "Raise it when a team designs a ladder of awards, for example foundation degree, top-up and master's. Ask staff how each step deepens understanding of EDI and sustainability. Ask: what does a student understand at the top of the suite that they did not at the bottom? Avoid giving it to students as a duty."
- statement: qaa/early-childhood-studies-2022/2.19
  forPractitioner: { text: "Build partnerships, local to international and across disciplines, that show students the field's breadth, through placements or other employability work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on course partnerships", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that courses show the field's multidisciplinary nature through partnerships. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.19. Do not claim placements are compulsory; the text allows employability work instead. Set it beside 2.7, 2.18 and 2.20."
  author-agent-dialogue: "Raise it when a team reviews its partners, or a course without placements plans employability work. Ask staff which partners sit outside early years settings. Ask: which partner gives students a view from health or social care? Avoid treating partnership as only the supply of placements."
- statement: qaa/early-childhood-studies-2022/2.20
  forPractitioner: { text: "Tell applicants clearly whether your course offers the graduate practitioner competencies; you must do so for transparency, and students should be able to discuss home-nation differences with you.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Before you apply, you can expect to be told whether the course offers the graduate practitioner competencies; you should discuss any requirements for your home nation with your institution.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a provider duty with the force must (be open with applicants about whether the competencies are offered), with a should for students to discuss home-nation requirements. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.20. Do not claim the competencies come with every degree or that Level 6 is defined here; read it as FHEQ level 6 (qaa/fheq-2024/4.15) by inference, and England's Level 3 as an early years qualification level, not a higher education one. Set it beside 1.18, 1.19 and 2.25."
  author-agent-dialogue: "Raise it when an applicant or student asks whether the degree leads to recognised practitioner status. With a student, say plainly whether this course offers the competencies and suggest they check their home nation's rules; with staff, check the published course information. Ask: where does the course tell applicants whether the competencies are included? Avoid implying the competencies come with every degree."
- statement: qaa/early-childhood-studies-2022/2.22
  forPractitioner: { text: "Periodic review will draw on external reviewers who look at proposed changes and confirm that threshold standards are met and content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the institution's review process", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level expectation on institutions' review processes, not on students. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.22. Do not claim it sets the review procedure, which is each institution's own. Set it beside 2.23, 2.24 and the threshold column of the section 4 table."
  author-agent-dialogue: "Raise it when a team prepares for periodic review. Ask staff who the external reviewers are and what they will check. Ask: what evidence will show the reviewers that threshold standards are met? Avoid raising it with students as their concern."
- statement: qaa/early-childhood-studies-2022/2.24
  forPractitioner: { text: "Appoint external examiners with specialist knowledge of the subject and, where relevant, of placements and the practitioner competencies, who know the statement's core principles and the range of course types and delivery.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who appoint and brief external examiners", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the appointment and conduct of external examiners. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.24. Do not claim it sets a formal qualification for examiners. Set it beside 2.22, 2.23 and 2.25."
  author-agent-dialogue: "Raise it when a team nominates an external examiner, above all for a course with the practitioner competencies. Ask staff what placement and competency experience the nominee has. Ask: could this examiner judge evidence from practice as well as written work? Avoid involving students in it."
- statement: qaa/early-childhood-studies-2022/2.25
  forPractitioner: { text: "Before offering the practitioner competencies, embedded or as an extra certificate, confirm that your institution is a current member of the degrees network: it must be.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition on the institution", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a provider duty with the force must: current membership of the degrees network is a condition of offering the practitioner competencies, embedded or as an extra certificate. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 2.25. Do not claim membership is needed to run an early childhood degree at all. Set it beside 1.18 and 2.20, and treat the network's own requirements as a separate document, not yet ingested."
  author-agent-dialogue: "Raise it when a team proposes adding the competencies. Frame it for staff as a membership check before any design work. Ask: is the institution a current member, and who keeps the membership up to date? Avoid presenting this to students."
- statement: qaa/early-childhood-studies-2022/3.3.b1
  forPractitioner: { text: "Honours graduates in the subject will be able to reflect on how psychology, sociology, health, history, education and philosophy each shape the way babies, young children and childhood are understood.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reflect on how psychology, sociology, health, history, education and philosophy each shape the way babies, young children and childhood are understood.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: disciplinary perspectives on childhood. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b13 and qaa/fheq-2024/4.15.b1, with spine:6."
  author-agent-dialogue: "Raise it when a student struggles to see why the course draws on so many disciplines. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: Which discipline shapes your own view of childhood most, and what does another one add? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b2
  forPractitioner: { text: "Honours graduates in the subject will be able to bring several perspectives to early childhood questions, aware that the field uses varied methods, theories, evidence and applications.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to bring several perspectives to early childhood questions, aware that the field uses varied methods, theories, evidence and applications.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: many perspectives on early childhood issues. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b11 and qaa/fheq-2024/4.15.b3.1, with spine:6."
  author-agent-dialogue: "Raise it when a student analyses an issue from one angle only. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: How would someone from health or social care read this issue differently? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b3
  forPractitioner: { text: "Honours graduates in the subject will be able to observe and analyse aspects of babies' and young children's lives, with reasonable adjustments for accessibility where needed.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to observe and analyse aspects of babies' and young children's lives, with reasonable adjustments for accessibility where needed.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: observation with reasonable adjustments. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b18 and qaa/fheq-2024/4.15.b2, with spine:6."
  author-agent-dialogue: "Raise it when a student prepares to observe on placement or needs an adjustment to do so. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What adjustment, if any, would help you observe and record well? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b4
  forPractitioner: { text: "Honours graduates in the subject will be able to combine ideas and findings from the field's many perspectives and see how each treats an issue in its own way.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to combine ideas and findings from the field's many perspectives and see how each treats an issue in its own way.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: integrating perspectives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b11 and qaa/fheq-2024/4.15.b3.1, with spine:6."
  author-agent-dialogue: "Raise it when a student's essay lists views without bringing them together. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: Where do these perspectives agree, and where do they pull apart? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b5
  forPractitioner: { text: "Honours graduates in the subject will be able to critique constructively the theory, practice and research on children's development, well-being, participation and learning across diverse childhoods.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to critique constructively the theory, practice and research on children's development, well-being, participation and learning across diverse childhoods.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: critiquing theory, practice and research. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b12 and qaa/fheq-2024/4.15.b3.2, with spine:6."
  author-agent-dialogue: "Raise it when a student accepts a theory or study without question. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What would a critic of this study say, and how fair would that be? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b6
  forPractitioner: { text: "Honours graduates in the subject will be able to show knowledge and awareness of the skills that different pedagogical approaches call for.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to show knowledge and awareness of the skills that different pedagogical approaches call for.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: skills for pedagogical approaches. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b17 and qaa/fheq-2024/4.15.b1, with spine:6."
  author-agent-dialogue: "Raise it when a student plans an activity with children. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: Which approach are you using, and what skill does it ask of you? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b7
  forPractitioner: { text: "Honours graduates in the subject will be able to understand how deep and strong relationships need to be with individual babies and children and with groups, and how to help children build relationships with each other.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to understand how deep and strong relationships need to be with individual babies and children and with groups, and how to help children build relationships with each other.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: relationships with and between children. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b17 and qaa/fheq-2024/4.15.b6, with spine:6."
  author-agent-dialogue: "Raise it when a student reflects on relationships in a setting. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: How did you help two children build a relationship with each other? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b8
  forPractitioner: { text: "Honours graduates in the subject will be able to build and encourage relationships of mutual respect with families, colleagues, other professionals and communities.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to build and encourage relationships of mutual respect with families, colleagues, other professionals and communities.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: respectful relationships with adults. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b22 and qaa/fheq-2024/4.15.b9.1, with spine:6."
  author-agent-dialogue: "Raise it when a student works with parents or other professionals. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What did you do to earn a family's trust? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b9
  forPractitioner: { text: "Honours graduates in the subject will be able to evaluate and develop their own values about teaching and care.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to evaluate and develop your own values about teaching and care.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: own pedagogical values. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b7 and qaa/fheq-2024/4.15.b5, with spine:6."
  author-agent-dialogue: "Raise it when a student is asked what they believe about how young children learn. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: Which value guides your practice most, and where did it come from? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b10
  forPractitioner: { text: "Honours graduates in the subject will be able to reflect on why the natural world and time outdoors matter for how all young children and their families grow, develop, know and understand.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reflect on why the natural world and time outdoors matter for how all young children and their families grow, develop, know and understand.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: the natural environment and the outdoors. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b6 and qaa/fheq-2024/4.15.b1, with spine:6."
  author-agent-dialogue: "Raise it when a team plans outdoor learning or a student questions its value. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What did a child learn outdoors that they could not have learned inside? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b11
  forPractitioner: { text: "Honours graduates in the subject will be able to explore, examine and judge critically the cultural, historical and current features of policies, institutions and agencies, local to global, and what they mean for children's development and for ideas of childhood.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to explore, examine and judge critically the cultural, historical and current features of policies, institutions and agencies, local to global, and what they mean for children's development and for ideas of childhood.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: policies, institutions and agencies. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b15 and qaa/fheq-2024/4.15.b7, with spine:6."
  author-agent-dialogue: "Raise it when a student studies a policy or an agency. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: How has this policy changed over time, and whose idea of childhood does it carry? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b12
  forPractitioner: { text: "Honours graduates in the subject will be able to show a strong grasp of the pedagogy of play as several disciplines see it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to show a strong grasp of the pedagogy of play as several disciplines see it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: the pedagogy of play. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b19 and qaa/fheq-2024/4.15.b1, with spine:6."
  author-agent-dialogue: "Raise it when a student plans or reviews play-based learning. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What does play look like from a health or psychology view, not only an education one? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b13
  forPractitioner: { text: "Honours graduates in the subject will be able to plan, and where fitting carry out, curriculum, assessment, evaluation and improvement of creative learning, with regard to children's health and emotional well-being.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to plan, and where fitting carry out, curriculum, assessment, evaluation and improvement of creative learning, with regard to children's health and emotional well-being.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: planning creative learning. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b21 and qaa/fheq-2024/4.15.b6, with spine:6."
  author-agent-dialogue: "Raise it when a student plans a learning experience. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: How does your plan look after children's emotional well-being as well as their learning? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b14
  forPractitioner: { text: "Honours graduates in the subject will be able to lead, support and collaborate with others and understand effective teamwork with parents, carers and other professionals.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to lead, support and collaborate with others and understand effective teamwork with parents, carers and other professionals.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: leading and teamwork. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b25 and qaa/fheq-2024/4.15.b9.1, with spine:6."
  author-agent-dialogue: "Raise it when a student takes on a group or team role. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What did you do to help the team work well with a parent or another professional? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b15
  forPractitioner: { text: "Honours graduates in the subject will be able to understand how to plan for, and where fitting deliver, the protection, safety, health and well-being of children and the conditions in which they thrive.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to understand how to plan for, and where fitting deliver, the protection, safety, health and well-being of children and the conditions in which they thrive.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: health, protection and safety. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b21 and qaa/fheq-2024/4.15.b6, with spine:6."
  author-agent-dialogue: "Raise it when safeguarding or health promotion comes up in a module or on placement. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What conditions in this setting help children flourish, and what would you change? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b16
  forPractitioner: { text: "Honours graduates in the subject will be able to build critical arguments for improving multiagency and multi-professional practice for babies and young children.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to build critical arguments for improving multiagency and multi-professional practice for babies and young children.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: arguing for better joint practice. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b23 and qaa/fheq-2024/4.15.b8, with spine:6."
  author-agent-dialogue: "Raise it when a student studies a case where agencies did not work together. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What one change would most improve how these agencies work together, and what is your evidence? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b17
  forPractitioner: { text: "Honours graduates in the subject will be able to observe and analyse aspects of babies' and young children's lives.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to observe and analyse aspects of babies' and young children's lives.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: observation and analysis. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b18 and qaa/fheq-2024/4.15.b2, with spine:6."
  author-agent-dialogue: "Raise it when a student writes up an observation. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What did you notice, and how do you know it was not just your assumption? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b18
  forPractitioner: { text: "Honours graduates in the subject will be able to reflect on the ethics of studying babies, young children, their families and communities.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reflect on the ethics of studying babies, young children, their families and communities.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: the ethics of studying children. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b28 and qaa/fheq-2024/4.15.b4, with spine:6."
  author-agent-dialogue: "Raise it when a student plans research or observation with children. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: How will you know a young child is happy to take part? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b19
  forPractitioner: { text: "Honours graduates in the subject will be able to form and test out hypotheses and research questions on early childhood, seen in its ecological context.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to form and test out hypotheses and research questions on early childhood, seen in its ecological context.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: hypotheses and research questions. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b26 and qaa/fheq-2024/4.15.b7, with spine:6."
  author-agent-dialogue: "Raise it when a student begins a research project. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What exactly do you want to find out, and why does it matter for children? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b20
  forPractitioner: { text: "Honours graduates in the subject will be able to carry out ethical empirical studies with varied data collection, observation of early childhood in its ecological context among them, and analyse the data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to carry out ethical empirical studies with varied data collection, observation of early childhood in its ecological context among them, and analyse the data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: ethical empirical study and analysis. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b27 and qaa/fheq-2024/4.15.b6, with spine:6."
  author-agent-dialogue: "Raise it when a student designs data collection. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: Which methods suit your question, and how will you keep them ethical? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b21
  forPractitioner: { text: "Honours graduates in the subject will be able to present and judge research findings on early childhood.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to present and judge research findings on early childhood.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: presenting and evaluating findings. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b27 and qaa/fheq-2024/4.15.b8, with spine:6."
  author-agent-dialogue: "Raise it when a student prepares to share research results. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: How strong are your findings, and who needs to hear them? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b22
  forPractitioner: { text: "Honours graduates in the subject will be able to understand critically how political, economic, cultural and ideological contexts, from local to global, act on one another in the lives of children, families and communities.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to understand critically how political, economic, cultural and ideological contexts, from local to global, act on one another in the lives of children, families and communities.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: interrelated contexts in children's lives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b14 and qaa/fheq-2024/4.15.b1, with spine:6."
  author-agent-dialogue: "Raise it when a student analyses a child's or family's circumstances. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: How do money, politics and culture shape this family's choices? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b23
  forPractitioner: { text: "Honours graduates in the subject will be able to recognise and challenge inequality in society and take an anti-bias approach.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to recognise and challenge inequality in society and take an anti-bias approach.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: challenging inequality. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b24 and qaa/fheq-2024/4.15.b9.2, with spine:6."
  author-agent-dialogue: "Raise it when a student meets bias in materials or practice. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: Where have you seen bias in a setting, and how might you challenge it? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.3.b24
  forPractitioner: { text: "Honours graduates in the subject will be able to recognise children's agency, help their voices be heard and, where fitting, advocate for babies, young children, families and communities.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to recognise children's agency, help their voices be heard and, where fitting, advocate for babies, young children, families and communities.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: agency, voice and advocacy. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.3 (subject-specific skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b20 and qaa/fheq-2024/4.15.b9.1, with spine:6."
  author-agent-dialogue: "Raise it when a student considers how children take part in decisions. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: When did a child's view change what you did? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b1
  forPractitioner: { text: "Honours graduates in the subject will be able to present information in suitable forms, online or offline, with a sense of audience.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to present information in suitable forms, online or offline, with a sense of audience.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: presenting information. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b30 and qaa/fheq-2024/4.15.b8, with spine:6."
  author-agent-dialogue: "Raise it when a student prepares a presentation or poster. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: Who is your audience, and what do they need first? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b2
  forPractitioner: { text: "Honours graduates in the subject will be able to show empathy and active listening and develop ways to guard against burnout from emotional labour.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to show empathy and active listening and develop ways to guard against burnout from emotional labour.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: empathy and guarding against burnout. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b32 and qaa/fheq-2024/4.15.b9.1, with spine:6."
  author-agent-dialogue: "Raise it when a student finds placement emotionally demanding. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What helps you recover after an emotionally heavy day? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b3
  forPractitioner: { text: "Honours graduates in the subject will be able to give and defend an informed view, drawing on a range of theoretical positions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to give and defend an informed view, drawing on a range of theoretical positions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: arguing a view from theory. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b30 and qaa/fheq-2024/4.15.b3.1, with spine:6."
  author-agent-dialogue: "Raise it when a student writes an argued essay. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What is your view, and which theory supports it best? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b4
  forPractitioner: { text: "Honours graduates in the subject will be able to understand data and use it well.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to understand data and use it well.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: using data. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b9 and qaa/fheq-2024/4.15.b2, with spine:6."
  author-agent-dialogue: "Raise it when a student meets statistics in a report. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What does this figure tell you, and what does it leave out? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b5
  forPractitioner: { text: "Honours graduates in the subject will be able to communicate with others and reflect on their own and others' skills, beliefs, understanding and views.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to communicate with others and reflect on your own and others' skills, beliefs, understanding and views.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: communicating and reflecting on views. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b32 and qaa/fheq-2024/4.15.b8, with spine:6."
  author-agent-dialogue: "Raise it when a student reviews group work. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What did you learn about your own beliefs from someone who disagreed? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b6
  forPractitioner: { text: "Honours graduates in the subject will be able to frame and sharpen questions and judge critically.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to frame and sharpen questions and judge critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: framing questions and judging. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b26 and qaa/fheq-2024/4.15.b7, with spine:6."
  author-agent-dialogue: "Raise it when a student's question is too broad. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: How could you narrow this question so that it can be answered? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b7
  forPractitioner: { text: "Honours graduates in the subject will be able to weigh different perspectives critically and reach well-supported conclusions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to weigh different perspectives critically and reach well-supported conclusions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: reaching supported conclusions. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b30 and qaa/fheq-2024/4.15.b7, with spine:6."
  author-agent-dialogue: "Raise it when a student's conclusion goes beyond the evidence. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: Which perspective does your conclusion rest on, and what would change it? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b8
  forPractitioner: { text: "Honours graduates in the subject will be able to find, retrieve, organise and use varied information sources, primary sources among them, and judge critically how relevant they are.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to find, retrieve, organise and use varied information sources, primary sources among them, and judge critically how relevant they are.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: finding and judging sources. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b31 and qaa/fheq-2024/4.15.b5, with spine:6."
  author-agent-dialogue: "Raise it when a student starts a literature search. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: Why is this source the right one for your question? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b9
  forPractitioner: { text: "Honours graduates in the subject will be able to engage with research and practice and with the uncertainty of knowledge still being built.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to engage with research and practice and with the uncertainty of knowledge still being built.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: uncertainty in knowledge. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b12 and qaa/fheq-2024/4.15.b4, with spine:6."
  author-agent-dialogue: "Raise it when a student is unsettled that research disagrees. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What would you do in practice when the research does not agree? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b10
  forPractitioner: { text: "Honours graduates in the subject will be able to use communication skills to talk, debate, negotiate, persuade and challenge others' ideas, with reasonable adjustments for disabled students where needed.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to use communication skills to talk, debate, negotiate, persuade and challenge others' ideas, with reasonable adjustments for disabled students where needed.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: communicating to debate and persuade. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b30 and qaa/fheq-2024/4.15.b8, with spine:6."
  author-agent-dialogue: "Raise it when a student prepares for a debate or a hard conversation on placement. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: How would you challenge a colleague's idea respectfully? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b11
  forPractitioner: { text: "Honours graduates in the subject will be able to lead and collaborate with others with insight and confidence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to lead and collaborate with others with insight and confidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: leading and collaborating. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b25 and qaa/fheq-2024/4.15.b9.1, with spine:6."
  author-agent-dialogue: "Raise it when a student takes a lead in a group task. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What did you do as a leader that helped the group? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b12
  forPractitioner: { text: "Honours graduates in the subject will be able to be alert to contextual and interpersonal factors, seeing how complex influences shape behaviour and interaction and give rise to problems and conflict.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to be alert to contextual and interpersonal factors, seeing how complex influences shape behaviour and interaction and give rise to problems and conflict.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: context and interpersonal factors. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b14 and qaa/fheq-2024/4.15.b9.2, with spine:6."
  author-agent-dialogue: "Raise it when conflict arises in a group or a setting. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What lay behind this conflict, beyond the people involved? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b13
  forPractitioner: { text: "Honours graduates in the subject will be able to see the value of cooperation in making individual skills more effective.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to see the value of cooperation in making individual skills more effective.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: cooperation. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b22 and qaa/fheq-2024/4.15.b9.1, with spine:6."
  author-agent-dialogue: "Raise it when a student prefers to work alone. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What could the group do that you could not do alone? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b14
  forPractitioner: { text: "Honours graduates in the subject will be able to write for varied purposes, such as persuading, explaining, describing, evaluating, recounting, summarising and hypothesising.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to write for varied purposes, such as persuading, explaining, describing, evaluating, recounting, summarising and hypothesising.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: writing for different purposes. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b30 and qaa/fheq-2024/4.15.b8, with spine:6."
  author-agent-dialogue: "Raise it when a student plans a written task. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What is this piece of writing for, and does its form fit that purpose? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b15
  forPractitioner: { text: "Honours graduates in the subject will be able to evaluate and analyse critically.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to evaluate and analyse critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: critical evaluation and analysis. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b12 and qaa/fheq-2024/4.15.b7, with spine:6."
  author-agent-dialogue: "Raise it when a student's work describes more than it analyses. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What is your own judgement here, beyond the description? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b16
  forPractitioner: { text: "Honours graduates in the subject will be able to use digital technology and social media appropriately in different contexts and reflect on that use.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to use digital technology and social media appropriately in different contexts and reflect on that use.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: digital technology and social media. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b34 and qaa/fheq-2024/4.15.b9.3, with spine:6."
  author-agent-dialogue: "Raise it when a student uses social media in study or on placement. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: How would a family feel about the way you used that platform? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.4.b17
  forPractitioner: { text: "Honours graduates in the subject will be able to become a learner who works autonomously, growing in independence, resilience, responsibility and pragmatism.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to become a learner who works autonomously, growing in independence, resilience, responsibility and pragmatism.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: autonomy and resilience. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.4 (generic skills). Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside 4.4.b33 and qaa/fheq-2024/4.15.b5, with spine:6."
  author-agent-dialogue: "Raise it when a student asks how to study more independently. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. Ask: What did you decide about your learning this week without being told? Avoid reading the list aloud or treating each item as needing its own module."
- statement: qaa/early-childhood-studies-2022/3.6
  forPractitioner: { text: "Shift teaching towards self-directed learning over the course; students are expected to take responsibility for the outcomes and to extend what is taught through their own enquiry.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "As your course goes on you will do more self-directed learning, and you are expected to take responsibility for reaching the outcomes, adding to what you are taught through your own reading, enquiry and discussion.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a described expectation of students ('are expected to', recorded as describes) about growing independence across the honours degree. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.6. Do not present it as a graded outcome. Set it beside 3.4.b17 (autonomous learning), the own-learning row of the section 4 table (4.4.b33) and qaa/fheq-2024/4.15.b5."
  author-agent-dialogue: "Raise it when a student relies wholly on taught sessions or asks how much independent work is expected. Put it plainly: you are expected to go beyond what is taught. Ask: what did you read or explore this week that no one set you? Avoid making it sound like a rebuke."
- statement: qaa/early-childhood-studies-2022/3.8
  forPractitioner: { text: "You must support students in reflecting on their own childhoods and on practice experience and relating these to theory, and plan emotional support for when this reflection is painful.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on teaching staff; the student meets its effect", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a provider duty: the issuer's word is requirement, recorded as must. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.8. Do not claim students must disclose personal history. Set it beside 3.5, 3.9 and 3.11."
  author-agent-dialogue: "Raise it when a module asks students to reflect on their own childhoods. With staff, ask what emotional support is in place before the task is set. Ask: what will happen if a student finds this reflection distressing? Avoid pressing a student to share more than they choose."
- statement: qaa/early-childhood-studies-2022/3.12
  forPractitioner: { text: "Tie each assessment to its objectives, and make reasonable adjustments for disabled students where they need them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that assessment makes reasonable adjustments, alongside the link between methods and objectives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.12. Do not claim it replaces duties under equality law, which it does not name. Set it beside 2.4, 2.8 and 3.4.b10."
  author-agent-dialogue: "Raise it when a disabled student asks about an assessment or a team reviews its adjustments process. For staff, ask how adjustments are agreed before the deadline. Ask: does the adjusted task still let the student show the same outcome? Avoid making the student argue for what should already be in place."
- statement: qaa/early-childhood-studies-2022/3.14
  forPractitioner: { text: "If students are taking the practitioner competencies, their practice must be assessed in settings; for others, practice assessment is optional. Keep criteria explicit and inclusive and expect critical thinking to grow year on year.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you take the graduate practitioner competencies, your practice in settings must be assessed; you can expect clear, inclusive criteria that look for your critical thinking to grow.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a conditional must: assessment of practice in settings is required only for students taking the graduate practitioner competencies. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.14. Do not claim every student has to be assessed in practice. Set it beside 1.19, 2.20 and 3.15."
  author-agent-dialogue: "Raise it when a student chooses whether to take the competencies, or a team designs practice assessment. With a student, say plainly that taking the competencies means assessed practice; with staff, ask how practice evidence is gathered and judged. Ask: are you planning to take the competencies, and do you know how your practice will be assessed? Avoid suggesting practice assessment is compulsory for everyone."
- statement: qaa/early-childhood-studies-2022/3.16
  forPractitioner: { text: "Give feedback and feed-forward with enough depth for students to reflect on their results and plan what to do next.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who give feedback", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the depth of assessment feedback. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 3.16. Do not claim it sets turnaround times or a feedback format. Set it beside 2.9, 3.12 and the own-learning row of the section 4 table (4.4.b33)."
  author-agent-dialogue: "Raise it when a student says feedback did not help them improve, or a team reviews its feedback practice. For staff, ask whether feedback names next steps. Ask: what would you do differently next time, based on this feedback? Avoid defending the feedback before hearing the student out."
- statement: qaa/early-childhood-studies-2022/4.3
  forPractitioner: { text: "Every graduate should gain a measure of the subject's skills; expect the range and degree to differ between single honours, joint honours and modules taken within another degree.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should gain a measure of the skills the subject calls for; how many you show, and how strongly, will depend on whether you study it as single honours, joint honours or modules within another degree.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that every graduate gains a measure of the subject's skills, with range and degree varying by route. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, para 4.3. Do not claim joint or minor routes must meet every item in the table. Set it beside 2.12, 4.4 and the threshold column of the table."
  author-agent-dialogue: "Raise it when a joint honours student or a minor-route team asks how much of the table applies. Put it plainly: you will gain some of each skill, to a degree that depends on your route. Ask: which skills does your route leave thin? Avoid holding a minor-route student to single honours expectations."
- statement: qaa/early-childhood-studies-2022/4.4.b1
  forPractitioner: { text: "Every honours graduate will, at the minimum, understand the core ideas on which early childhood studies is built as a field; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will understand the core ideas on which early childhood studies is built as a field.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on the conceptual foundations of the field. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on the conceptual foundations of the field. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b1.typical, 4.4.b1.excellent, 4.4.b1.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student asks what holds the field together. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What idea sits at the centre of early childhood studies for you, and where did it come from? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b1.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will understand critically the field's founding ideas, its origins, growth and limits; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will understand critically the field's founding ideas, its origins, growth and limits.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on the conceptual foundations of the field. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on the conceptual foundations of the field. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b1, 4.4.b1.typical, 4.4.b1.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student asks what holds the field together. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What idea sits at the centre of early childhood studies for you, and where did it come from? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b1.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will show detailed, accurate and critically engaged knowledge of the field's founding ideas, origins, growth and limits; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will show detailed, accurate and critically engaged knowledge of the field's founding ideas, origins, growth and limits.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on the conceptual foundations of the field. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on the conceptual foundations of the field. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b1, 4.4.b1.typical, 4.4.b1.excellent) and qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it when a student asks what holds the field together. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What idea sits at the centre of early childhood studies for you, and where did it come from? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b1.typical
  forPractitioner: { text: "At the typical standard, honours graduates will understand those core ideas together with where the field came from, how it grew and where it falls short; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will understand those core ideas together with where the field came from, how it grew and where it falls short.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on the conceptual foundations of the field. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on the conceptual foundations of the field. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b1, 4.4.b1.excellent, 4.4.b1.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student asks what holds the field together. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What idea sits at the centre of early childhood studies for you, and where did it come from? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b2
  forPractitioner: { text: "Every honours graduate will, at the minimum, have a basic grasp of babies, young children and the many forms childhood takes, at home and worldwide, through the disciplines that study them, from psychology and sociology to law, politics and economics; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will have a basic grasp of babies, young children and the many forms childhood takes, at home and worldwide, through the disciplines that study them, from psychology and sociology to law, politics and economics.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on babies, young children and diverse childhoods through many disciplines. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on babies, young children and diverse childhoods through many disciplines. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b2.typical, 4.4.b2.excellent, 4.4.b2.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student writes about childhood from one discipline only. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: Which lens, such as decolonising or economic, have you used least, and what would it show? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b2.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will know babies, young children and diverse childhoods in depth and systematically, and understand them with consistent criticality, through every lens the field uses; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will know babies, young children and diverse childhoods in depth and systematically, and understand them with consistent criticality, through every lens the field uses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on babies, young children and diverse childhoods through many disciplines. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on babies, young children and diverse childhoods through many disciplines. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b2, 4.4.b2.typical, 4.4.b2.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student writes about childhood from one discipline only. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Which lens, such as decolonising or economic, have you used least, and what would it show? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b2.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will engage critically with theory and understand babies, young children and diverse childhoods with consistent criticality through every lens the field uses; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will engage critically with theory and understand babies, young children and diverse childhoods with consistent criticality through every lens the field uses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on babies, young children and diverse childhoods through many disciplines. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on babies, young children and diverse childhoods through many disciplines. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b2, 4.4.b2.typical, 4.4.b2.excellent) and qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it when a student writes about childhood from one discipline only. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: Which lens, such as decolonising or economic, have you used least, and what would it show? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b2.typical
  forPractitioner: { text: "At the typical standard, honours graduates will know babies, young children and diverse childhoods systematically and understand them critically, at home and worldwide, through every disciplinary lens the field uses; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will know babies, young children and diverse childhoods systematically and understand them critically, at home and worldwide, through every disciplinary lens the field uses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on babies, young children and diverse childhoods through many disciplines. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on babies, young children and diverse childhoods through many disciplines. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b2, 4.4.b2.excellent, 4.4.b2.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student writes about childhood from one discipline only. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Which lens, such as decolonising or economic, have you used least, and what would it show? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b3
  forPractitioner: { text: "Every honours graduate will, at the minimum, know and understand the areas of interest that feed early childhood studies across its core skills areas, and how they connect; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will know and understand the areas of interest that feed early childhood studies across its core skills areas, and how they connect.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on the field's areas of interest and how they connect. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on the field's areas of interest and how they connect. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b3.typical, 4.4.b3.excellent, 4.4.b3.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a team maps modules to the field's areas of interest. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: How does what you learned in one module change how you read another? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b3.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will know those areas in depth and systematically and understand them and their connections with consistent criticality; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will know those areas in depth and systematically and understand them and their connections with consistent criticality.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on the field's areas of interest and how they connect. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on the field's areas of interest and how they connect. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b3, 4.4.b3.typical, 4.4.b3.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/1st, with spine:6."
  author-agent-dialogue: "Raise it when a team maps modules to the field's areas of interest. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How does what you learned in one module change how you read another? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b3.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will show detailed, accurate knowledge of those areas and engage with them and their connections consistently and critically; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will show detailed, accurate knowledge of those areas and engage with them and their connections consistently and critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on the field's areas of interest and how they connect. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on the field's areas of interest and how they connect. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b3, 4.4.b3.typical, 4.4.b3.excellent) and qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it when a team maps modules to the field's areas of interest. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: How does what you learned in one module change how you read another? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b3.typical
  forPractitioner: { text: "At the typical standard, honours graduates will know those areas systematically and understand them and their connections critically; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will know those areas systematically and understand them and their connections critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on the field's areas of interest and how they connect. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on the field's areas of interest and how they connect. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b3, 4.4.b3.excellent, 4.4.b3.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a team maps modules to the field's areas of interest. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How does what you learned in one module change how you read another? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b4
  forPractitioner: { text: "Every honours graduate will, at the minimum, understand local, national and global policy and the provision it makes for young children, babies, their families and communities; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will understand local, national and global policy and the provision it makes for young children, babies, their families and communities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on policy and provision for children and families. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on policy and provision for children and families. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b4.typical, 4.4.b4.excellent, 4.4.b4.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student studies a policy that affects young children. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: How does this policy reach a child at home, and who decides how it is applied? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b4.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will know that policy and provision in depth and systematically, with marked critical understanding; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will know that policy and provision in depth and systematically, with marked critical understanding.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on policy and provision for children and families. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on policy and provision for children and families. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b4, 4.4.b4.typical, 4.4.b4.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student studies a policy that affects young children. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How does this policy reach a child at home, and who decides how it is applied? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b4.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will show detailed, accurate and systematic knowledge of that policy and provision and engage with it consistently and critically; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will show detailed, accurate and systematic knowledge of that policy and provision and engage with it consistently and critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on policy and provision for children and families. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on policy and provision for children and families. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b4, 4.4.b4.typical, 4.4.b4.excellent) and qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it when a student studies a policy that affects young children. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: How does this policy reach a child at home, and who decides how it is applied? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b4.typical
  forPractitioner: { text: "At the typical standard, honours graduates will know that policy and provision systematically and understand it critically; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will know that policy and provision systematically and understand it critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on policy and provision for children and families. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on policy and provision for children and families. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b4, 4.4.b4.excellent, 4.4.b4.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student studies a policy that affects young children. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How does this policy reach a child at home, and who decides how it is applied? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b5
  forPractitioner: { text: "Every honours graduate will, at the minimum, understand how working across professions, agencies and cultures can make life better for babies, young children, their families and communities; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will understand how working across professions, agencies and cultures can make life better for babies, young children, their families and communities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on working across professions, agencies and cultures. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on working across professions, agencies and cultures. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b5.typical, 4.4.b5.excellent, 4.4.b5.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student meets health, social care and education staff working on one case. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What made this joint work succeed or stall? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b5.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will have a critical working knowledge of why such joint working matters and of its challenges and limits; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will have a critical working knowledge of why such joint working matters and of its challenges and limits.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on working across professions, agencies and cultures. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on working across professions, agencies and cultures. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b5, 4.4.b5.typical, 4.4.b5.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student meets health, social care and education staff working on one case. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What made this joint work succeed or stall? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b5.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will engage critically and in depth with the value, challenges and limits of such joint working; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will engage critically and in depth with the value, challenges and limits of such joint working.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on working across professions, agencies and cultures. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on working across professions, agencies and cultures. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b5, 4.4.b5.typical, 4.4.b5.excellent) and qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it when a student meets health, social care and education staff working on one case. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What made this joint work succeed or stall? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b5.typical
  forPractitioner: { text: "At the typical standard, honours graduates will have a working knowledge of why such joint working matters and of the challenges and limits it meets; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will have a working knowledge of why such joint working matters and of the challenges and limits it meets.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on working across professions, agencies and cultures. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on working across professions, agencies and cultures. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b5, 4.4.b5.excellent, 4.4.b5.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student meets health, social care and education staff working on one case. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What made this joint work succeed or stall? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b6
  forPractitioner: { text: "Every honours graduate will, at the minimum, be aware of issues of equity, diversity, inclusion, human rights, social justice and sustainability when working with babies, young children, families and communities; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will be aware of issues of equity, diversity, inclusion, human rights, social justice and sustainability when working with babies, young children, families and communities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on rights, diversity, equity, justice, sustainability and inclusion in practice. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on rights, diversity, equity, justice, sustainability and inclusion in practice. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b6.typical, 4.4.b6.excellent, 4.4.b6.masters) and qaa/fheq-2024/4.15.b4, qaa/fheq-2024/annex-d/knowledge/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student or team considers fairness, rights or sustainability in a setting. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: Which of these issues did you notice in your last placement, and what did you do? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b6.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will have excellent knowledge of those issues; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will have excellent knowledge of those issues.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on rights, diversity, equity, justice, sustainability and inclusion in practice. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on rights, diversity, equity, justice, sustainability and inclusion in practice. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b6, 4.4.b6.typical, 4.4.b6.masters) and qaa/fheq-2024/4.15.b4, qaa/fheq-2024/annex-d/knowledge/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student or team considers fairness, rights or sustainability in a setting. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Which of these issues did you notice in your last placement, and what did you do? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b6.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will synthesise knowledge and understanding of those issues in ways that lead to original thinking; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will synthesise knowledge and understanding of those issues in ways that lead to original thinking.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on rights, diversity, equity, justice, sustainability and inclusion in practice. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on rights, diversity, equity, justice, sustainability and inclusion in practice. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b6, 4.4.b6.typical, 4.4.b6.excellent) and qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it when a student or team considers fairness, rights or sustainability in a setting. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: Which of these issues did you notice in your last placement, and what did you do? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b6.typical
  forPractitioner: { text: "At the typical standard, honours graduates will have a good knowledge of those issues; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will have a good knowledge of those issues.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on rights, diversity, equity, justice, sustainability and inclusion in practice. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on rights, diversity, equity, justice, sustainability and inclusion in practice. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b6, 4.4.b6.excellent, 4.4.b6.masters) and qaa/fheq-2024/4.15.b4, qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student or team considers fairness, rights or sustainability in a setting. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Which of these issues did you notice in your last placement, and what did you do? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b7
  forPractitioner: { text: "Every honours graduate will, at the minimum, know and understand pedagogical approaches for work with babies, young children, families and communities; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will know and understand pedagogical approaches for work with babies, young children, families and communities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on pedagogical approaches and values. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on pedagogical approaches and values. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b7.typical, 4.4.b7.excellent, 4.4.b7.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student compares ways of working with young children. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: Which approach fits your values best, and what are its limits? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b7.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will have a critical working knowledge and understanding of those approaches and values; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will have a critical working knowledge and understanding of those approaches and values.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on pedagogical approaches and values. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on pedagogical approaches and values. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b7, 4.4.b7.typical, 4.4.b7.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student compares ways of working with young children. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Which approach fits your values best, and what are its limits? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b7.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will show detailed, accurate and critically engaged knowledge of those approaches and values; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will show detailed, accurate and critically engaged knowledge of those approaches and values.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on pedagogical approaches and values. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on pedagogical approaches and values. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b7, 4.4.b7.typical, 4.4.b7.excellent) and qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it when a student compares ways of working with young children. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: Which approach fits your values best, and what are its limits? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b7.typical
  forPractitioner: { text: "At the typical standard, honours graduates will have a working knowledge and understanding of those approaches and the values behind them; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will have a working knowledge and understanding of those approaches and the values behind them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on pedagogical approaches and values. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on pedagogical approaches and values. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b7, 4.4.b7.excellent, 4.4.b7.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student compares ways of working with young children. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Which approach fits your values best, and what are its limits? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b8
  forPractitioner: { text: "Every honours graduate will, at the minimum, understand critically how ethics, economics, politics, culture and ideology connect in the lives of young children, babies and their families and communities; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will understand critically how ethics, economics, politics, culture and ideology connect in the lives of young children, babies and their families and communities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on ethics, economics, politics, culture and ideology in children's lives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on ethics, economics, politics, culture and ideology in children's lives. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b8.typical, 4.4.b8.excellent, 4.4.b8.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student explains a family's situation by one factor alone. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: How do money, politics and belief combine in this family's situation? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b8.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will understand those connections critically, to a highly developed degree; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will understand those connections critically, to a highly developed degree.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on ethics, economics, politics, culture and ideology in children's lives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on ethics, economics, politics, culture and ideology in children's lives. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b8, 4.4.b8.typical, 4.4.b8.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student explains a family's situation by one factor alone. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How do money, politics and belief combine in this family's situation? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b8.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will engage with those connections critically, to an excellent degree; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will engage with those connections critically, to an excellent degree.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on ethics, economics, politics, culture and ideology in children's lives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on ethics, economics, politics, culture and ideology in children's lives. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b8, 4.4.b8.typical, 4.4.b8.excellent) and qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it when a student explains a family's situation by one factor alone. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: How do money, politics and belief combine in this family's situation? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b8.typical
  forPractitioner: { text: "At the typical standard, honours graduates will understand those connections critically, in a well-developed way; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will understand those connections critically, in a well-developed way.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on ethics, economics, politics, culture and ideology in children's lives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on ethics, economics, politics, culture and ideology in children's lives. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b8, 4.4.b8.excellent, 4.4.b8.masters) and qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student explains a family's situation by one factor alone. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How do money, politics and belief combine in this family's situation? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b9
  forPractitioner: { text: "Every honours graduate will, at the minimum, know the methods needed to study and research children and childhood systematically; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will know the methods needed to study and research children and childhood systematically.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on methods for systematic study and research. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on methods for systematic study and research. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b9.typical, 4.4.b9.excellent, 4.4.b9.masters) and qaa/fheq-2024/4.15.b2, qaa/fheq-2024/annex-d/knowledge/r3/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student chooses a research method. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: Why is this method right for studying children, and what would it miss? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b9.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will have an excellent and explicit working knowledge of those methods; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will have an excellent and explicit working knowledge of those methods.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on methods for systematic study and research. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on methods for systematic study and research. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b9, 4.4.b9.typical, 4.4.b9.masters) and qaa/fheq-2024/4.15.b2, qaa/fheq-2024/annex-d/knowledge/r3/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student chooses a research method. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Why is this method right for studying children, and what would it miss? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b9.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will evaluate those methods critically and reflexively; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will evaluate those methods critically and reflexively.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on methods for systematic study and research. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on methods for systematic study and research. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b9, 4.4.b9.typical, 4.4.b9.excellent) and qaa/fheq-2024/4.17.b2 and spine:7."
  author-agent-dialogue: "Raise it when a student chooses a research method. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: Why is this method right for studying children, and what would it miss? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b9.typical
  forPractitioner: { text: "At the typical standard, honours graduates will have a good working knowledge of those methods; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will have a good working knowledge of those methods.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on methods for systematic study and research. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on methods for systematic study and research. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b9, 4.4.b9.excellent, 4.4.b9.masters) and qaa/fheq-2024/4.15.b2, qaa/fheq-2024/annex-d/knowledge/r3/2.2 and qaa/fheq-2024/annex-d/knowledge/r3/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student chooses a research method. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Why is this method right for studying children, and what would it miss? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b10
  forPractitioner: { text: "Every honours graduate will, at the minimum, reason clearly and show how theory, policy, practice and evidence relate; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will reason clearly and show how theory, policy, practice and evidence relate.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on reasoning about theory, policy, practice and evidence. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on reasoning about theory, policy, practice and evidence. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b10.typical, 4.4.b10.excellent, 4.4.b10.masters) and qaa/fheq-2024/4.15.b3.1, qaa/fheq-2024/annex-d/cognitive/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student argues from opinion rather than evidence. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What evidence and which policy support this point, and does practice bear it out? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b10.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will reason clearly to a high level, understand the part played by theory, policy, practice and evidence, and judge arguments in the field critically; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will reason clearly to a high level, understand the part played by theory, policy, practice and evidence, and judge arguments in the field critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on reasoning about theory, policy, practice and evidence. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on reasoning about theory, policy, practice and evidence. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b10, 4.4.b10.typical, 4.4.b10.masters) and qaa/fheq-2024/4.15.b3.1, qaa/fheq-2024/annex-d/cognitive/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student argues from opinion rather than evidence. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What evidence and which policy support this point, and does practice bear it out? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b10.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will reason clearly to an excellent level, engage critically with the part played by theory, policy, practice and evidence, and judge arguments in the field critically; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will reason clearly to an excellent level, engage critically with the part played by theory, policy, practice and evidence, and judge arguments in the field critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on reasoning about theory, policy, practice and evidence. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on reasoning about theory, policy, practice and evidence. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b10, 4.4.b10.typical, 4.4.b10.excellent) and qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise it when a student argues from opinion rather than evidence. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What evidence and which policy support this point, and does practice bear it out? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b10.typical
  forPractitioner: { text: "At the typical standard, honours graduates will reason clearly, understand what theory, policy, practice and evidence each contribute, and judge arguments in the field critically; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will reason clearly, understand what theory, policy, practice and evidence each contribute, and judge arguments in the field critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on reasoning about theory, policy, practice and evidence. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on reasoning about theory, policy, practice and evidence. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b10, 4.4.b10.excellent, 4.4.b10.masters) and qaa/fheq-2024/4.15.b3.1, qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student argues from opinion rather than evidence. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What evidence and which policy support this point, and does practice bear it out? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b11
  forPractitioner: { text: "Every honours graduate will, at the minimum, take up a range of theoretical perspectives on diverse childhoods; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will take up a range of theoretical perspectives on diverse childhoods.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on taking up theoretical perspectives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on taking up theoretical perspectives. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b11.typical, 4.4.b11.excellent, 4.4.b11.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student uses one theory for everything. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: How would a second theory explain the same behaviour? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b11.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will take up many perspectives on early childhood to a high level and analyse systematically how they relate; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will take up many perspectives on early childhood to a high level and analyse systematically how they relate.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on taking up theoretical perspectives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on taking up theoretical perspectives. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b11, 4.4.b11.typical, 4.4.b11.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student uses one theory for everything. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How would a second theory explain the same behaviour? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b11.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will take up many perspectives on early childhood to an excellent level and analyse critically how they relate; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will take up many perspectives on early childhood to an excellent level and analyse critically how they relate.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on taking up theoretical perspectives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on taking up theoretical perspectives. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b11, 4.4.b11.typical, 4.4.b11.excellent) and qaa/fheq-2024/4.17.b4.1 and spine:7."
  author-agent-dialogue: "Raise it when a student uses one theory for everything. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: How would a second theory explain the same behaviour? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b11.typical
  forPractitioner: { text: "At the typical standard, honours graduates will take up a range of such perspectives and analyse systematically how they relate; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will take up a range of such perspectives and analyse systematically how they relate.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on taking up theoretical perspectives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on taking up theoretical perspectives. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b11, 4.4.b11.excellent, 4.4.b11.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student uses one theory for everything. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How would a second theory explain the same behaviour? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b12
  forPractitioner: { text: "Every honours graduate will, at the minimum, critique theory, practice and research in the field constructively; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will critique theory, practice and research in the field constructively.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on critiquing theory, practice and research. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on critiquing theory, practice and research. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b12.typical, 4.4.b12.excellent, 4.4.b12.masters) and qaa/fheq-2024/4.15.b3.2, qaa/fheq-2024/annex-d/cognitive/r1/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student summarises research without judging it. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What is the strongest and the weakest point of this study? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b12.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will analyse and constructively critique theory, practice and research to a high level; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will analyse and constructively critique theory, practice and research to a high level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on critiquing theory, practice and research. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on critiquing theory, practice and research. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b12, 4.4.b12.typical, 4.4.b12.masters) and qaa/fheq-2024/4.15.b3.2, qaa/fheq-2024/annex-d/cognitive/r1/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student summarises research without judging it. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What is the strongest and the weakest point of this study? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b12.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will analyse critically and critique constructively theory, practice and research, to an excellent level; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will analyse critically and critique constructively theory, practice and research, to an excellent level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on critiquing theory, practice and research. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on critiquing theory, practice and research. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b12, 4.4.b12.typical, 4.4.b12.excellent) and qaa/fheq-2024/4.17.b4.1 and spine:7."
  author-agent-dialogue: "Raise it when a student summarises research without judging it. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What is the strongest and the weakest point of this study? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b12.typical
  forPractitioner: { text: "At the typical standard, honours graduates will analyse theory, practice and research in the field and critique them constructively; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will analyse theory, practice and research in the field and critique them constructively.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on critiquing theory, practice and research. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on critiquing theory, practice and research. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b12, 4.4.b12.excellent, 4.4.b12.masters) and qaa/fheq-2024/4.15.b3.2, qaa/fheq-2024/annex-d/cognitive/r1/2.2 and qaa/fheq-2024/annex-d/cognitive/r1/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student summarises research without judging it. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What is the strongest and the weakest point of this study? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b13
  forPractitioner: { text: "Every honours graduate will, at the minimum, reflect on the many disciplinary perspectives on babies, young children and childhood and how each shapes understanding, from local to global; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will reflect on the many disciplinary perspectives on babies, young children and childhood and how each shapes understanding, from local to global.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on reflecting on disciplinary perspectives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on reflecting on disciplinary perspectives. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b13.typical, 4.4.b13.excellent, 4.4.b13.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student wonders why the course mixes so many disciplines. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: How does a legal view of childhood differ from a psychological one? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b13.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will reflect on those perspectives and how they shape understanding, to a high level; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will reflect on those perspectives and how they shape understanding, to a high level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on reflecting on disciplinary perspectives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on reflecting on disciplinary perspectives. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b13, 4.4.b13.typical, 4.4.b13.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student wonders why the course mixes so many disciplines. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How does a legal view of childhood differ from a psychological one? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b13.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will reflect critically on those perspectives and how they shape understanding, to an excellent level; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will reflect critically on those perspectives and how they shape understanding, to an excellent level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on reflecting on disciplinary perspectives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on reflecting on disciplinary perspectives. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b13, 4.4.b13.typical, 4.4.b13.excellent) and qaa/fheq-2024/4.17.b4.1 and spine:7."
  author-agent-dialogue: "Raise it when a student wonders why the course mixes so many disciplines. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: How does a legal view of childhood differ from a psychological one? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b13.typical
  forPractitioner: { text: "At the typical standard, honours graduates will reflect on those perspectives and how they shape understanding, in a well-developed way; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will reflect on those perspectives and how they shape understanding, in a well-developed way.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on reflecting on disciplinary perspectives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on reflecting on disciplinary perspectives. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b13, 4.4.b13.excellent, 4.4.b13.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student wonders why the course mixes so many disciplines. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How does a legal view of childhood differ from a psychological one? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b14
  forPractitioner: { text: "Every honours graduate will, at the minimum, explore critically how political, economic, cultural and ideological contexts bear on one another in the lives of babies and young children; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will explore critically how political, economic, cultural and ideological contexts bear on one another in the lives of babies and young children.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on contexts in young children's lives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on contexts in young children's lives. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b14.typical, 4.4.b14.excellent, 4.4.b14.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student analyses the wider forces in a child's life. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: Which context, political, economic, cultural or ideological, matters most here, and why? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b14.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will explore those interrelations critically, with highly developed ability; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will explore those interrelations critically, with highly developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on contexts in young children's lives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on contexts in young children's lives. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b14, 4.4.b14.typical, 4.4.b14.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student analyses the wider forces in a child's life. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Which context, political, economic, cultural or ideological, matters most here, and why? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b14.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will explore those interrelations critically, with excellent ability; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will explore those interrelations critically, with excellent ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on contexts in young children's lives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on contexts in young children's lives. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b14, 4.4.b14.typical, 4.4.b14.excellent) and qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise it when a student analyses the wider forces in a child's life. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: Which context, political, economic, cultural or ideological, matters most here, and why? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b14.typical
  forPractitioner: { text: "At the typical standard, honours graduates will explore those interrelations critically, with well-developed ability; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will explore those interrelations critically, with well-developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on contexts in young children's lives. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on contexts in young children's lives. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b14, 4.4.b14.excellent, 4.4.b14.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student analyses the wider forces in a child's life. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Which context, political, economic, cultural or ideological, matters most here, and why? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b15
  forPractitioner: { text: "Every honours graduate will, at the minimum, explore, examine and judge why the cultural, historical and present-day features of policies, institutions and agencies matter for babies, young children and childhood; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will explore, examine and judge why the cultural, historical and present-day features of policies, institutions and agencies matter for babies, young children and childhood.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on policies, institutions and agencies. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on policies, institutions and agencies. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b15.typical, 4.4.b15.excellent, 4.4.b15.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r1/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student studies an agency or a policy. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What does the history of this agency tell you about how it treats children now? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b15.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will explore, examine and judge those features to a high level; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will explore, examine and judge those features to a high level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on policies, institutions and agencies. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on policies, institutions and agencies. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b15, 4.4.b15.typical, 4.4.b15.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r1/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student studies an agency or a policy. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What does the history of this agency tell you about how it treats children now? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b15.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will explore, examine and judge those features critically, to an excellent level; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will explore, examine and judge those features critically, to an excellent level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on policies, institutions and agencies. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on policies, institutions and agencies. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b15, 4.4.b15.typical, 4.4.b15.excellent) and qaa/fheq-2024/4.17.b4.1 and spine:7."
  author-agent-dialogue: "Raise it when a student studies an agency or a policy. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What does the history of this agency tell you about how it treats children now? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b15.typical
  forPractitioner: { text: "At the typical standard, honours graduates will explore, examine and judge those features critically; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will explore, examine and judge those features critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on policies, institutions and agencies. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on policies, institutions and agencies. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b15, 4.4.b15.excellent, 4.4.b15.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r1/2.2 and qaa/fheq-2024/annex-d/cognitive/r1/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student studies an agency or a policy. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What does the history of this agency tell you about how it treats children now? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b16
  forPractitioner: { text: "Every honours graduate will, at the minimum, weigh competing views of how babies, young children and childhood are constructed by subjects, social agents, time, place and culture; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will weigh competing views of how babies, young children and childhood are constructed by subjects, social agents, time, place and culture.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on competing constructions of childhood. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on competing constructions of childhood. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b16.typical, 4.4.b16.excellent, 4.4.b16.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student takes one idea of childhood for granted. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: How would childhood have been understood in another time or place? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b16.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will analyse and weigh those competing views to a high level; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will analyse and weigh those competing views to a high level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on competing constructions of childhood. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on competing constructions of childhood. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b16, 4.4.b16.typical, 4.4.b16.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student takes one idea of childhood for granted. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How would childhood have been understood in another time or place? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b16.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will analyse critically and weigh those competing views, to an excellent level; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will analyse critically and weigh those competing views, to an excellent level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on competing constructions of childhood. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on competing constructions of childhood. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b16, 4.4.b16.typical, 4.4.b16.excellent) and qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise it when a student takes one idea of childhood for granted. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: How would childhood have been understood in another time or place? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b16.typical
  forPractitioner: { text: "At the typical standard, honours graduates will analyse and weigh competing views of how childhood is socially constructed across time, place and culture; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will analyse and weigh competing views of how childhood is socially constructed across time, place and culture.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on competing constructions of childhood. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on competing constructions of childhood. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b16, 4.4.b16.excellent, 4.4.b16.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student takes one idea of childhood for granted. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How would childhood have been understood in another time or place? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b17
  forPractitioner: { text: "Every honours graduate will, at the minimum, know and be aware of the skills that relational pedagogical approaches call for; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will know and be aware of the skills that relational pedagogical approaches call for.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on skills for relational pedagogy. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on skills for relational pedagogy. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b17.typical, 4.4.b17.excellent, 4.4.b17.masters) and qaa/fheq-2024/4.15.b6, qaa/fheq-2024/annex-d/practical/r1/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student reflects on building relationships with children. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: Which relational skill do you rely on most, and which needs work? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b17.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will have high-level knowledge and awareness of those skills; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will have high-level knowledge and awareness of those skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on skills for relational pedagogy. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on skills for relational pedagogy. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b17, 4.4.b17.typical, 4.4.b17.masters) and qaa/fheq-2024/4.15.b6, qaa/fheq-2024/annex-d/practical/r1/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student reflects on building relationships with children. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Which relational skill do you rely on most, and which needs work? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b17.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will have excellent knowledge and awareness of those skills; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will have excellent knowledge and awareness of those skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on skills for relational pedagogy. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on skills for relational pedagogy. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b17, 4.4.b17.typical, 4.4.b17.excellent) and qaa/fheq-2024/4.17.b3 and spine:7."
  author-agent-dialogue: "Raise it when a student reflects on building relationships with children. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: Which relational skill do you rely on most, and which needs work? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b17.typical
  forPractitioner: { text: "At the typical standard, honours graduates will have well-developed knowledge and awareness of those skills; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will have well-developed knowledge and awareness of those skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on skills for relational pedagogy. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on skills for relational pedagogy. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b17, 4.4.b17.excellent, 4.4.b17.masters) and qaa/fheq-2024/4.15.b6, qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student reflects on building relationships with children. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Which relational skill do you rely on most, and which needs work? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b18
  forPractitioner: { text: "Every honours graduate will, at the minimum, observe and analyse parts of babies' and young children's lives; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will observe and analyse parts of babies' and young children's lives.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on observation and analysis. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on observation and analysis. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b18.typical, 4.4.b18.excellent, 4.4.b18.masters) and qaa/fheq-2024/4.15.b2, qaa/fheq-2024/annex-d/practical/r1/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student writes up an observation. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What did you see, and what are you reading into it? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b18.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will observe and analyse those lives with highly developed skill; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will observe and analyse those lives with highly developed skill.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on observation and analysis. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on observation and analysis. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b18, 4.4.b18.typical, 4.4.b18.masters) and qaa/fheq-2024/4.15.b2, qaa/fheq-2024/annex-d/practical/r1/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student writes up an observation. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What did you see, and what are you reading into it? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b18.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will observe and analyse those lives with excellent skill; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will observe and analyse those lives with excellent skill.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on observation and analysis. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on observation and analysis. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b18, 4.4.b18.typical, 4.4.b18.excellent) and qaa/fheq-2024/4.17.b2 and spine:7."
  author-agent-dialogue: "Raise it when a student writes up an observation. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What did you see, and what are you reading into it? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b18.typical
  forPractitioner: { text: "At the typical standard, honours graduates will observe and analyse those lives with developed skill; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will observe and analyse those lives with developed skill.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on observation and analysis. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on observation and analysis. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b18, 4.4.b18.excellent, 4.4.b18.masters) and qaa/fheq-2024/4.15.b2, qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student writes up an observation. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What did you see, and what are you reading into it? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b19
  forPractitioner: { text: "Every honours graduate will, at the minimum, spot meaningful patterns in play, behaviour and experience; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will spot meaningful patterns in play, behaviour and experience.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on patterns in play, behaviour and experience. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on patterns in play, behaviour and experience. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b19.typical, 4.4.b19.excellent, 4.4.b19.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/practical/r4/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student reviews notes on children's play. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What pattern runs through these observations, and what might it mean? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b19.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will spot such patterns and judge what they mean, to a high level; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will spot such patterns and judge what they mean, to a high level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on patterns in play, behaviour and experience. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on patterns in play, behaviour and experience. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b19, 4.4.b19.typical, 4.4.b19.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/practical/r4/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student reviews notes on children's play. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What pattern runs through these observations, and what might it mean? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b19.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will spot such patterns and judge critically what they mean, to an excellent level; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will spot such patterns and judge critically what they mean, to an excellent level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on patterns in play, behaviour and experience. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on patterns in play, behaviour and experience. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b19, 4.4.b19.typical, 4.4.b19.excellent) and qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise it when a student reviews notes on children's play. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What pattern runs through these observations, and what might it mean? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b19.typical
  forPractitioner: { text: "At the typical standard, honours graduates will spot such patterns and judge what they mean; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will spot such patterns and judge what they mean.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on patterns in play, behaviour and experience. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on patterns in play, behaviour and experience. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b19, 4.4.b19.excellent, 4.4.b19.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/practical/r4/2.2 and qaa/fheq-2024/annex-d/practical/r4/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student reviews notes on children's play. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What pattern runs through these observations, and what might it mean? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b20
  forPractitioner: { text: "Every honours graduate will, at the minimum, attune to the views of babies, young children, families and communities and, where fitting, speak up for them; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will attune to the views of babies, young children, families and communities and, where fitting, speak up for them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on attunement and advocacy. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on attunement and advocacy. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b20.typical, 4.4.b20.excellent, 4.4.b20.masters) and qaa/fheq-2024/4.15.b9.1, qaa/fheq-2024/annex-d/professional/r1/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student considers how to represent a child's view. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: When did you speak up for a child or family, and what did you base it on? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b20.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will attune to and, where fitting, advocate for babies, young children, families and communities, with highly developed ability; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will attune to and, where fitting, advocate for babies, young children, families and communities, with highly developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on attunement and advocacy. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on attunement and advocacy. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b20, 4.4.b20.typical, 4.4.b20.masters) and qaa/fheq-2024/4.15.b9.1, qaa/fheq-2024/annex-d/professional/r1/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student considers how to represent a child's view. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: When did you speak up for a child or family, and what did you base it on? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b20.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will attune to and, where fitting, advocate for babies, young children, families and communities, with excellent ability; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will attune to and, where fitting, advocate for babies, young children, families and communities, with excellent ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on attunement and advocacy. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on attunement and advocacy. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b20, 4.4.b20.typical, 4.4.b20.excellent) and qaa/fheq-2024/4.17.b8.1 and spine:7."
  author-agent-dialogue: "Raise it when a student considers how to represent a child's view. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: When did you speak up for a child or family, and what did you base it on? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b20.typical
  forPractitioner: { text: "At the typical standard, honours graduates will attune to and, where fitting, advocate for babies, young children, families and communities, with well-developed ability; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will attune to and, where fitting, advocate for babies, young children, families and communities, with well-developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on attunement and advocacy. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on attunement and advocacy. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b20, 4.4.b20.excellent, 4.4.b20.masters) and qaa/fheq-2024/4.15.b9.1, qaa/fheq-2024/annex-d/professional/r1/2.2 and qaa/fheq-2024/annex-d/professional/r1/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student considers how to represent a child's view. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: When did you speak up for a child or family, and what did you base it on? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b21
  forPractitioner: { text: "Every honours graduate will, at the minimum, plan for, and where fitting put in place, provision that protects children, keeps them safe and healthy, supports their all-round development and well-being, and creates the conditions for them to flourish; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will plan for, and where fitting put in place, provision that protects children, keeps them safe and healthy, supports their all-round development and well-being, and creates the conditions for them to flourish.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on planning for holistic development, health, protection and safety. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on planning for holistic development, health, protection and safety. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b21.typical, 4.4.b21.excellent, 4.4.b21.masters) and qaa/fheq-2024/4.15.b6, qaa/fheq-2024/annex-d/practical/r1/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student plans provision in a setting. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: How does your plan keep children safe while letting them flourish? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b21.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will plan and, where fitting, put in place provision for children's all-round development, health, well-being, protection and safety, with highly developed ability; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will plan and, where fitting, put in place provision for children's all-round development, health, well-being, protection and safety, with highly developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on planning for holistic development, health, protection and safety. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on planning for holistic development, health, protection and safety. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b21, 4.4.b21.typical, 4.4.b21.masters) and qaa/fheq-2024/4.15.b6, qaa/fheq-2024/annex-d/practical/r1/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student plans provision in a setting. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How does your plan keep children safe while letting them flourish? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b21.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will plan and, where fitting, put in place provision for children's all-round development, health, well-being, protection and safety, with excellent ability; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will plan and, where fitting, put in place provision for children's all-round development, health, well-being, protection and safety, with excellent ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on planning for holistic development, health, protection and safety. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on planning for holistic development, health, protection and safety. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b21, 4.4.b21.typical, 4.4.b21.excellent) and qaa/fheq-2024/4.17.b3 and spine:7."
  author-agent-dialogue: "Raise it when a student plans provision in a setting. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: How does your plan keep children safe while letting them flourish? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b21.typical
  forPractitioner: { text: "At the typical standard, honours graduates will plan and, where fitting, put in place provision for children's all-round development, health, well-being, protection and safety, with well-developed ability; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will plan and, where fitting, put in place provision for children's all-round development, health, well-being, protection and safety, with well-developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on planning for holistic development, health, protection and safety. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on planning for holistic development, health, protection and safety. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b21, 4.4.b21.excellent, 4.4.b21.masters) and qaa/fheq-2024/4.15.b6, qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student plans provision in a setting. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How does your plan keep children safe while letting them flourish? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b22
  forPractitioner: { text: "Every honours graduate will, at the minimum, plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on collaboration with parents, carers and other stakeholders. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on collaboration with parents, carers and other stakeholders. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b22.typical, 4.4.b22.excellent, 4.4.b22.masters) and qaa/fheq-2024/4.15.b9.2, qaa/fheq-2024/annex-d/transferable/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student plans work with families. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: How will you involve parents and carers from the start, not only at the end? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b22.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders, with highly developed ability; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders, with highly developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on collaboration with parents, carers and other stakeholders. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on collaboration with parents, carers and other stakeholders. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b22, 4.4.b22.typical, 4.4.b22.masters) and qaa/fheq-2024/4.15.b9.2, qaa/fheq-2024/annex-d/transferable/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student plans work with families. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How will you involve parents and carers from the start, not only at the end? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b22.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders, with excellent ability; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders, with excellent ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on collaboration with parents, carers and other stakeholders. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on collaboration with parents, carers and other stakeholders. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b22, 4.4.b22.typical, 4.4.b22.excellent) and qaa/fheq-2024/4.17.b8.2 and spine:7."
  author-agent-dialogue: "Raise it when a student plans work with families. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: How will you involve parents and carers from the start, not only at the end? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b22.typical
  forPractitioner: { text: "At the typical standard, honours graduates will plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders, with well-developed ability; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders, with well-developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on collaboration with parents, carers and other stakeholders. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on collaboration with parents, carers and other stakeholders. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b22, 4.4.b22.excellent, 4.4.b22.masters) and qaa/fheq-2024/4.15.b9.2, qaa/fheq-2024/annex-d/transferable/r2/2.2 and qaa/fheq-2024/annex-d/transferable/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student plans work with families. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How will you involve parents and carers from the start, not only at the end? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b23
  forPractitioner: { text: "Every honours graduate will, at the minimum, build critical arguments for improving multiagency, multi-professional and inter-professional practice for babies and young children; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will build critical arguments for improving multiagency, multi-professional and inter-professional practice for babies and young children.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on arguing for better joint professional practice. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on arguing for better joint professional practice. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b23.typical, 4.4.b23.excellent, 4.4.b23.masters) and qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/cognitive/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student reviews a case where professionals did not work well together. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What would you change in how these professionals work together, and why? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b23.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will build such arguments with highly developed ability; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will build such arguments with highly developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on arguing for better joint professional practice. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on arguing for better joint professional practice. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b23, 4.4.b23.typical, 4.4.b23.masters) and qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/cognitive/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student reviews a case where professionals did not work well together. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What would you change in how these professionals work together, and why? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b23.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will build such arguments with excellent ability; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will build such arguments with excellent ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on arguing for better joint professional practice. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on arguing for better joint professional practice. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b23, 4.4.b23.typical, 4.4.b23.excellent) and qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise it when a student reviews a case where professionals did not work well together. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What would you change in how these professionals work together, and why? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b23.typical
  forPractitioner: { text: "At the typical standard, honours graduates will build such arguments with well-developed ability; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will build such arguments with well-developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on arguing for better joint professional practice. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on arguing for better joint professional practice. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b23, 4.4.b23.excellent, 4.4.b23.masters) and qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student reviews a case where professionals did not work well together. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What would you change in how these professionals work together, and why? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b24
  forPractitioner: { text: "Every honours graduate will, at the minimum, recognise and challenge inequality and injustice in society and take up anti-bias, anti-oppressive approaches; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will recognise and challenge inequality and injustice in society and take up anti-bias, anti-oppressive approaches.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on challenging inequality. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on challenging inequality. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b24.typical, 4.4.b24.excellent, 4.4.b24.masters) and qaa/fheq-2024/4.15.b9.2, qaa/fheq-2024/annex-d/professional/r1/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student meets bias or exclusion in practice. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What inequality did you notice, and what could you do about it? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b24.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will recognise and challenge inequality and injustice and take up anti-bias, anti-oppressive approaches, with highly developed ability; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will recognise and challenge inequality and injustice and take up anti-bias, anti-oppressive approaches, with highly developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on challenging inequality. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on challenging inequality. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b24, 4.4.b24.typical, 4.4.b24.masters) and qaa/fheq-2024/4.15.b9.2, qaa/fheq-2024/annex-d/professional/r1/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student meets bias or exclusion in practice. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What inequality did you notice, and what could you do about it? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b24.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will recognise and challenge inequality and injustice and take up anti-bias, anti-oppressive approaches, with excellent ability; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will recognise and challenge inequality and injustice and take up anti-bias, anti-oppressive approaches, with excellent ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on challenging inequality. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on challenging inequality. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b24, 4.4.b24.typical, 4.4.b24.excellent) and qaa/fheq-2024/4.17.b8.2 and spine:7."
  author-agent-dialogue: "Raise it when a student meets bias or exclusion in practice. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What inequality did you notice, and what could you do about it? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b24.typical
  forPractitioner: { text: "At the typical standard, honours graduates will recognise and challenge inequality and injustice and take up anti-bias, anti-oppressive approaches, with well-developed ability; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will recognise and challenge inequality and injustice and take up anti-bias, anti-oppressive approaches, with well-developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on challenging inequality. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on challenging inequality. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b24, 4.4.b24.excellent, 4.4.b24.masters) and qaa/fheq-2024/4.15.b9.2, qaa/fheq-2024/annex-d/professional/r1/2.2 and qaa/fheq-2024/annex-d/professional/r1/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student meets bias or exclusion in practice. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What inequality did you notice, and what could you do about it? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b25
  forPractitioner: { text: "Every honours graduate will, at the minimum, lead, mentor, facilitate and collaborate with others to bring about transformational change; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will lead, mentor, facilitate and collaborate with others to bring about transformational change.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on leadership for transformational change. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on leadership for transformational change. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b25.typical, 4.4.b25.excellent, 4.4.b25.masters) and qaa/fheq-2024/4.15.b9.1, qaa/fheq-2024/annex-d/transferable/r4/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student leads or mentors others. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What change did you help others make, and how did you support them? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b25.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will lead, mentor, facilitate and collaborate with others to bring about transformational change, with highly developed ability; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will lead, mentor, facilitate and collaborate with others to bring about transformational change, with highly developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on leadership for transformational change. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on leadership for transformational change. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b25, 4.4.b25.typical, 4.4.b25.masters) and qaa/fheq-2024/4.15.b9.1, qaa/fheq-2024/annex-d/transferable/r4/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student leads or mentors others. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What change did you help others make, and how did you support them? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b25.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will show professional confidence and lead, mentor, facilitate and collaborate with others to an excellent level to bring about transformational change; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will show professional confidence and lead, mentor, facilitate and collaborate with others to an excellent level to bring about transformational change.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on leadership for transformational change. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on leadership for transformational change. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b25, 4.4.b25.typical, 4.4.b25.excellent) and qaa/fheq-2024/4.17.b8.1 and spine:7."
  author-agent-dialogue: "Raise it when a student leads or mentors others. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What change did you help others make, and how did you support them? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b25.typical
  forPractitioner: { text: "At the typical standard, honours graduates will lead, mentor, facilitate and collaborate with others to bring about transformational change, with well-developed ability; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will lead, mentor, facilitate and collaborate with others to bring about transformational change, with well-developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on leadership for transformational change. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on leadership for transformational change. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b25, 4.4.b25.excellent, 4.4.b25.masters) and qaa/fheq-2024/4.15.b9.1, qaa/fheq-2024/annex-d/transferable/r4/2.2 and qaa/fheq-2024/annex-d/transferable/r4/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student leads or mentors others. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What change did you help others make, and how did you support them? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b26
  forPractitioner: { text: "Every honours graduate will, at the minimum, pose research questions about early childhood, put them into operation, and show research competence through practical and theoretical work; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will pose research questions about early childhood, put them into operation, and show research competence through practical and theoretical work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on research questions and research competence. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on research questions and research competence. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b26.typical, 4.4.b26.excellent, 4.4.b26.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/practical/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student frames a research question. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: How would you turn this question into something you can measure or observe? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b26.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will pose, operationalise and critique research questions with highly developed ability, showing a good level of research competence; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will pose, operationalise and critique research questions with highly developed ability, showing a good level of research competence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on research questions and research competence. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on research questions and research competence. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b26, 4.4.b26.typical, 4.4.b26.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/practical/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student frames a research question. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How would you turn this question into something you can measure or observe? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b26.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will pose, operationalise and critique research questions with excellent ability, showing highly developed research competence; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will pose, operationalise and critique research questions with excellent ability, showing highly developed research competence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on research questions and research competence. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on research questions and research competence. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b26, 4.4.b26.typical, 4.4.b26.excellent) and qaa/fheq-2024/4.17.b4.2 and spine:7."
  author-agent-dialogue: "Raise it when a student frames a research question. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: How would you turn this question into something you can measure or observe? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b26.typical
  forPractitioner: { text: "At the typical standard, honours graduates will pose, operationalise and critique research questions on early childhood and show research competence in practice and in theory; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will pose, operationalise and critique research questions on early childhood and show research competence in practice and in theory.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on research questions and research competence. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on research questions and research competence. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b26, 4.4.b26.excellent, 4.4.b26.masters) and qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/practical/r2/2.2 and qaa/fheq-2024/annex-d/practical/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student frames a research question. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How would you turn this question into something you can measure or observe? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b27
  forPractitioner: { text: "Every honours graduate will, at the minimum, start, design, carry out and report a supervised empirical research project on early childhood; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will start, design, carry out and report a supervised empirical research project on early childhood.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on the supervised research project. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on the supervised research project. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b27.typical, 4.4.b27.excellent, 4.4.b27.masters) and qaa/fheq-2024/4.15.b6, qaa/fheq-2024/annex-d/practical/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student plans or writes up their project. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What are the limits of your project, and how do they affect what you can claim? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b27.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will carry out the whole project, from start to report, with a high degree of competence, recognising with highly developed ability what it implies and where it falls short; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will carry out the whole project, from start to report, with a high degree of competence, recognising with highly developed ability what it implies and where it falls short.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on the supervised research project. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on the supervised research project. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b27, 4.4.b27.typical, 4.4.b27.masters) and qaa/fheq-2024/4.15.b6, qaa/fheq-2024/annex-d/practical/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student plans or writes up their project. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What are the limits of your project, and how do they affect what you can claim? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b27.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will carry out the whole project independently with supervision, showing high competence and reflexive engagement with what it implies and where it falls short; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will carry out the whole project independently with supervision, showing high competence and reflexive engagement with what it implies and where it falls short.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on the supervised research project. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on the supervised research project. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b27, 4.4.b27.typical, 4.4.b27.excellent) and qaa/fheq-2024/4.17.b6 and spine:7."
  author-agent-dialogue: "Raise it when a student plans or writes up their project. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What are the limits of your project, and how do they affect what you can claim? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b27.typical
  forPractitioner: { text: "At the typical standard, honours graduates will start, design, carry out and report such a project competently, recognising what it implies and where it falls short in theory, practice and method; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will start, design, carry out and report such a project competently, recognising what it implies and where it falls short in theory, practice and method.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on the supervised research project. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on the supervised research project. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b27, 4.4.b27.excellent, 4.4.b27.masters) and qaa/fheq-2024/4.15.b6, qaa/fheq-2024/annex-d/practical/r2/2.2 and qaa/fheq-2024/annex-d/practical/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student plans or writes up their project. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What are the limits of your project, and how do they affect what you can claim? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b28
  forPractitioner: { text: "Every honours graduate will, at the minimum, reflect on the ethics of studying babies, young children, families and communities; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will reflect on the ethics of studying babies, young children, families and communities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on the ethics of studying children. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on the ethics of studying children. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b28.typical, 4.4.b28.excellent, 4.4.b28.masters) and qaa/fheq-2024/4.15.b4, qaa/fheq-2024/annex-d/transferable/r5/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student plans to study children or families. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: How will you protect the children and families you study? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b28.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will reflect on those ethics with high-level ability; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will reflect on those ethics with high-level ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on the ethics of studying children. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on the ethics of studying children. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b28, 4.4.b28.typical, 4.4.b28.masters) and qaa/fheq-2024/4.15.b4, qaa/fheq-2024/annex-d/transferable/r5/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student plans to study children or families. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How will you protect the children and families you study? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b28.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will reflect on those ethics with excellent ability; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will reflect on those ethics with excellent ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on the ethics of studying children. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on the ethics of studying children. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b28, 4.4.b28.typical, 4.4.b28.excellent) and qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise it when a student plans to study children or families. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: How will you protect the children and families you study? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b28.typical
  forPractitioner: { text: "At the typical standard, honours graduates will reflect on those ethics with well-developed ability; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will reflect on those ethics with well-developed ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on the ethics of studying children. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on the ethics of studying children. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b28, 4.4.b28.excellent, 4.4.b28.masters) and qaa/fheq-2024/4.15.b4, qaa/fheq-2024/annex-d/transferable/r5/2.2 and qaa/fheq-2024/annex-d/transferable/r5/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student plans to study children or families. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How will you protect the children and families you study? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b29
  forPractitioner: { text: "Every honours graduate will, at the minimum, know the ethical principles involved and show this in personal study, above all the research project; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will know the ethical principles involved and show this in personal study, above all the research project.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on ethical principles in the research project. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on ethical principles in the research project. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b29.typical, 4.4.b29.excellent, 4.4.b29.masters) and qaa/fheq-2024/4.15.b6, qaa/fheq-2024/annex-d/professional/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student prepares an ethics application. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: Which ethical issue in your project is hardest, and how will you handle it? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b29.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will be aware of that complexity and apply it in personal study, above all the research project; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will be aware of that complexity and apply it in personal study, above all the research project.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on ethical principles in the research project. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on ethical principles in the research project. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b29, 4.4.b29.typical, 4.4.b29.masters) and qaa/fheq-2024/4.15.b6, qaa/fheq-2024/annex-d/professional/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student prepares an ethics application. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Which ethical issue in your project is hardest, and how will you handle it? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b29.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will engage reflexively and with care with that complexity and synthesise it in personal study, above all the research project; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will engage reflexively and with care with that complexity and synthesise it in personal study, above all the research project.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on ethical principles in the research project. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on ethical principles in the research project. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b29, 4.4.b29.typical, 4.4.b29.excellent) and qaa/fheq-2024/4.17.b6 and spine:7."
  author-agent-dialogue: "Raise it when a student prepares an ethics application. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: Which ethical issue in your project is hardest, and how will you handle it? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b29.typical
  forPractitioner: { text: "At the typical standard, honours graduates will be aware of how complex ethical principles and issues are and show this in personal study, above all the research project; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will be aware of how complex ethical principles and issues are and show this in personal study, above all the research project.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on ethical principles in the research project. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on ethical principles in the research project. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b29, 4.4.b29.excellent, 4.4.b29.masters) and qaa/fheq-2024/4.15.b6, qaa/fheq-2024/annex-d/professional/r2/2.2 and qaa/fheq-2024/annex-d/professional/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student prepares an ethics application. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Which ethical issue in your project is hardest, and how will you handle it? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b30
  forPractitioner: { text: "Every honours graduate will, at the minimum, set out a range of theoretical positions and give and defend a point of view; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will set out a range of theoretical positions and give and defend a point of view.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on arguing a point of view from theory. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on arguing a point of view from theory. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b30.typical, 4.4.b30.excellent, 4.4.b30.masters) and qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/cognitive/r2/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student presents an argument. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What is your position, and which theory would challenge it? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b30.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will set out a wide range of positions and give and defend a well-informed and insightful view; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will set out a wide range of positions and give and defend a well-informed and insightful view.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on arguing a point of view from theory. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on arguing a point of view from theory. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b30, 4.4.b30.typical, 4.4.b30.masters) and qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/cognitive/r2/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student presents an argument. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What is your position, and which theory would challenge it? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b30.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will know a wide range of positions in accurate detail and articulate and defend a well-informed, insightful view; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will know a wide range of positions in accurate detail and articulate and defend a well-informed, insightful view.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on arguing a point of view from theory. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on arguing a point of view from theory. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b30, 4.4.b30.typical, 4.4.b30.excellent) and qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise it when a student presents an argument. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What is your position, and which theory would challenge it? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b30.typical
  forPractitioner: { text: "At the typical standard, honours graduates will set out a wide range of positions and give and defend a well-informed view; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will set out a wide range of positions and give and defend a well-informed view.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on arguing a point of view from theory. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on arguing a point of view from theory. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b30, 4.4.b30.excellent, 4.4.b30.masters) and qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student presents an argument. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What is your position, and which theory would challenge it? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b31
  forPractitioner: { text: "Every honours graduate will, at the minimum, draw on a range of information sources; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will draw on a range of information sources.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on using sources of information. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on using sources of information. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b31.typical, 4.4.b31.excellent, 4.4.b31.masters) and qaa/fheq-2024/4.15.b5, qaa/fheq-2024/annex-d/cognitive/r1/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student builds a reading list. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: Why do you trust this source, and what would make you doubt it? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b31.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will draw on a wide range of information sources critically and with insight; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will draw on a wide range of information sources critically and with insight.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on using sources of information. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on using sources of information. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b31, 4.4.b31.typical, 4.4.b31.masters) and qaa/fheq-2024/4.15.b5, qaa/fheq-2024/annex-d/cognitive/r1/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student builds a reading list. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Why do you trust this source, and what would make you doubt it? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b31.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will engage critically and with insight with a wide range of information sources; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will engage critically and with insight with a wide range of information sources.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on using sources of information. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on using sources of information. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b31, 4.4.b31.typical, 4.4.b31.excellent) and qaa/fheq-2024/4.17.b4.1 and spine:7."
  author-agent-dialogue: "Raise it when a student builds a reading list. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: Why do you trust this source, and what would make you doubt it? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b31.typical
  forPractitioner: { text: "At the typical standard, honours graduates will draw on a range of information sources critically; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will draw on a range of information sources critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on using sources of information. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on using sources of information. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b31, 4.4.b31.excellent, 4.4.b31.masters) and qaa/fheq-2024/4.15.b5, qaa/fheq-2024/annex-d/cognitive/r1/2.2 and qaa/fheq-2024/annex-d/cognitive/r1/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student builds a reading list. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: Why do you trust this source, and what would make you doubt it? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b32
  forPractitioner: { text: "Every honours graduate will, at the minimum, listen carefully and reflect on their own and others' skills and views; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will listen carefully and reflect on your own and others' skills and views.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on listening and reflecting on skills and views. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on listening and reflecting on skills and views. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b32.typical, 4.4.b32.excellent, 4.4.b32.masters) and qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/transferable/r5/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student reviews feedback from peers. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What did you learn from someone whose view differed from yours? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b32.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will listen carefully and reflect critically and with insight on their own and others' skills and views; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will listen carefully and reflect critically and with insight on your own and others' skills and views.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on listening and reflecting on skills and views. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on listening and reflecting on skills and views. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b32, 4.4.b32.typical, 4.4.b32.masters) and qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/transferable/r5/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student reviews feedback from peers. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What did you learn from someone whose view differed from yours? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b32.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will listen carefully and reflect critically and analytically on their own and others' skills and views; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will listen carefully and reflect critically and analytically on your own and others' skills and views.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on listening and reflecting on skills and views. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on listening and reflecting on skills and views. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b32, 4.4.b32.typical, 4.4.b32.excellent) and qaa/fheq-2024/4.17.b8.3 and spine:7."
  author-agent-dialogue: "Raise it when a student reviews feedback from peers. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What did you learn from someone whose view differed from yours? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b32.typical
  forPractitioner: { text: "At the typical standard, honours graduates will listen carefully and reflect critically on their own and others' skills and views; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will listen carefully and reflect critically on your own and others' skills and views.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on listening and reflecting on skills and views. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on listening and reflecting on skills and views. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b32, 4.4.b32.excellent, 4.4.b32.masters) and qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/transferable/r5/2.2 and qaa/fheq-2024/annex-d/transferable/r5/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student reviews feedback from peers. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What did you learn from someone whose view differed from yours? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b33
  forPractitioner: { text: "Every honours graduate will, at the minimum, see that their own skills need assessing and reflect on them to guide later learning; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will see that your own skills need assessing and reflect on them to guide later learning.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on managing own learning. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on managing own learning. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b33.typical, 4.4.b33.excellent, 4.4.b33.masters) and qaa/fheq-2024/4.15.b5, qaa/fheq-2024/annex-d/transferable/r3/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student plans how to improve. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: What is your strongest skill now, and which one will you work on next? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b33.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will take charge of their own learning with sophistication, reflecting reflexively on their own strengths and weaknesses for later learning; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will take charge of your own learning with sophistication, reflecting reflexively on your own strengths and weaknesses for later learning.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on managing own learning. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on managing own learning. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b33, 4.4.b33.typical, 4.4.b33.masters) and qaa/fheq-2024/4.15.b5, qaa/fheq-2024/annex-d/transferable/r3/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student plans how to improve. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What is your strongest skill now, and which one will you work on next? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b33.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will lead their own learning with sophistication, evaluating their own strengths and weaknesses reflexively for later learning; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will lead your own learning with sophistication, evaluating your own strengths and weaknesses reflexively for later learning.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on managing own learning. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on managing own learning. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b33, 4.4.b33.typical, 4.4.b33.excellent) and qaa/fheq-2024/4.17.b8.3 and spine:7."
  author-agent-dialogue: "Raise it when a student plans how to improve. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: What is your strongest skill now, and which one will you work on next? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b33.typical
  forPractitioner: { text: "At the typical standard, honours graduates will take charge of their own learning and weigh up their own strengths and weaknesses to guide later learning; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will take charge of your own learning and weigh up your own strengths and weaknesses to guide later learning.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on managing own learning. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on managing own learning. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b33, 4.4.b33.excellent, 4.4.b33.masters) and qaa/fheq-2024/4.15.b5, qaa/fheq-2024/annex-d/transferable/r3/2.2 and qaa/fheq-2024/annex-d/transferable/r3/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student plans how to improve. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: What is your strongest skill now, and which one will you work on next? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b34
  forPractitioner: { text: "Every honours graduate will, at the minimum, use digital technologies and literacies appropriately in learning, across settings, to improve provision for children; teaching and assessment need to give each student the chance to show this.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you will use digital technologies and literacies appropriately in learning, across settings, to improve provision for children.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold, the minimum an honours graduate has to show (third-class level), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on digital technologies and literacies. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the threshold column of the row on digital technologies and literacies. Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree. Set it beside the other cells of the row (4.4.b34.typical, 4.4.b34.excellent, 4.4.b34.masters) and qaa/fheq-2024/4.15.b9.3, qaa/fheq-2024/annex-d/transferable/r1/3rd, with spine:6."
  author-agent-dialogue: "Raise it when a student uses digital tools with children or in study. With a student, say it plainly in the second person as the floor every honours graduate reaches; with staff, frame it as what a module and its assessment have to let students show. Ask: How did a digital tool improve, or get in the way of, what you offered children? Avoid reading the table cell aloud or treating the floor as the goal."
- statement: qaa/early-childhood-studies-2022/4.4.b34.excellent
  forPractitioner: { text: "At the excellent standard, honours graduates will use digital technologies and literacies with sophistication in learning, across settings, to improve provision for children; marking criteria can use this to describe first-class work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent standard, for first-class work, you will use digital technologies and literacies with sophistication in learning, across settings, to improve provision for children.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard, expected of the highest achievers (first class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on digital technologies and literacies. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the excellent column of the row on digital technologies and literacies. Do not present it as the minimum or as expected of every student: it describes first-class work. Set it beside the other cells of the row (4.4.b34, 4.4.b34.typical, 4.4.b34.masters) and qaa/fheq-2024/4.15.b9.3, qaa/fheq-2024/annex-d/transferable/r1/1st, with spine:6."
  author-agent-dialogue: "Raise it when a student uses digital tools with children or in study. With a student, say it plainly in the second person as what first-class work looks like, never as the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How did a digital tool improve, or get in the way of, what you offered children? Avoid reading the table cell aloud or presenting this column as the pass standard."
- statement: qaa/early-childhood-studies-2022/4.4.b34.masters
  forPractitioner: { text: "At the postgraduate standard, master's students will engage critically, professionally and with sophistication with digital technologies and literacies in learning, across settings, to improve provision for children; use it when setting master's outcomes, not undergraduate ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's course, at the postgraduate standard, you will engage critically, professionally and with sophistication with digital technologies and literacies in learning, across settings, to improve provision for children.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the postgraduate standard, for master's study, for the master's degree at FHEQ level 7 (FQHEIS level 11), in the row on digital technologies and literacies. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the postgraduate column of the row on digital technologies and literacies. Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards. Set it beside the other cells of the row (4.4.b34, 4.4.b34.typical, 4.4.b34.excellent) and qaa/fheq-2024/4.17.b7 and spine:7."
  author-agent-dialogue: "Raise it when a student uses digital tools with children or in study. With a student, say it plainly in the second person, and only with master's students; with staff, frame it as what a module and its assessment have to let students show. Ask: How did a digital tool improve, or get in the way of, what you offered children? Avoid reading the table cell aloud or using it to judge undergraduate work."
- statement: qaa/early-childhood-studies-2022/4.4.b34.typical
  forPractitioner: { text: "At the typical standard, honours graduates will use digital technologies and literacies appropriately and with confidence in learning, across settings, to improve provision for children; marking criteria can use this to tell typical work from the threshold in the same row.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, which most students reach, you will use digital technologies and literacies appropriately and with confidence in learning, across settings, to improve provision for children.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard, what most honours graduates are expected to reach (lower to upper second class), for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10), in the row on digital technologies and literacies. Cite it as QAA (2022), Early Childhood Studies Subject Benchmark Statement, section 4, benchmark standards table, the typical column of the row on digital technologies and literacies. Do not present it as the minimum: the threshold cell in the same row is the floor. Set it beside the other cells of the row (4.4.b34, 4.4.b34.excellent, 4.4.b34.masters) and qaa/fheq-2024/4.15.b9.3, qaa/fheq-2024/annex-d/transferable/r1/2.2 and qaa/fheq-2024/annex-d/transferable/r1/2.1, with spine:6."
  author-agent-dialogue: "Raise it when a student uses digital tools with children or in study. With a student, say it plainly in the second person as what most students reach, not the minimum; with staff, frame it as what a module and its assessment have to let students show. Ask: How did a digital tool improve, or get in the way of, what you offered children? Avoid reading the table cell aloud or presenting this column as the pass standard."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.11" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.11" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.13" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.13" }
  - { id: "fheq:6", role: "infers", locator: "D1, 1.6; 1.18; 1.19; 2.20: \"Level 6\" of the practitioner competencies, framework not named (Part E)" }
  - { id: "spine:6", role: "infers", locator: "std:ref:uk-framework R2, for the honours columns" }
  - { id: "spine:7", role: "infers", locator: "std:ref:uk-framework R2, for the postgraduate column" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.11: \"FHEQ Level 6; FQHEIS L evel 10\" for a degree with honours)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.13: integrated master's at \"FHEQ Level 7; FQHEIS Level 11\")" }
  - { from: "rung:threshold", to: "band:3rd (qaa/fheq-2024/annex-d)", relation: "labelled-as", basis: "stated in the table head (\"3rd class degree\"); the link to Annex D is inferred (Part E)" }
  - { from: "rung:typical", to: "band:2.2 to band:2.1 (qaa/fheq-2024/annex-d)", relation: "labelled-as", basis: "stated in the table head (\"2nd class lower to 2nd class upper\"); the link to Annex D is inferred (Part E)" }
  - { from: "rung:excellent", to: "band:1st (qaa/fheq-2024/annex-d)", relation: "labelled-as", basis: "stated in the table head (\"1st class\"); the link to Annex D is inferred (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.4", "1.5", "1.23", "1.24", "1.25", "1.26", "2.1", "2.16", "3.11", "3.14", "4.4"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.26", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9", "2.10", "3.3", "3.4", "3.12"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.5", "1.8", "1.27", "1.28", "1.29", "1.30", "1.31", "2.16", "4.4"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.32", "1.33", "1.34", "1.35", "1.36", "2.6", "2.8", "2.19", "2.20"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-early-childhood-studies-2019-benchmarks (not yet ingested)", note: "the back matter names the third edition, 2019; earlier editions 2014 and 2007" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ levels 6 and 7 (2.11, 2.13); the table heads label the rungs by degree class, the classes Annex D describes (inferred)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS levels 10 and 11 (2.11, 2.13)" }
- { rel: "cites", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "1.31: the definitions in 1.29 and 1.30 come from QAA's and Advance HE's ESD guidance" }
- { rel: "refersTo", target: "ECSDN Early Childhood Graduate Practitioner Competencies (not yet ingested; Part E)", note: "1.6, 1.18 to 1.20, 2.20, 2.25, 3.14; the held text carries the March 2026 revision as an appendix" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance; QAA Glossary (not ingested)", note: "front matter" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2022-03"
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
- An interdisciplinary, multi-professional field, first offered as degrees in 1992, that studies children from conception to eight and educates those who work with them and their families (D1, 1.1, 1.2, 2.1).
- It draws on health, education, social work, psychology, sociology, philosophy, history, cultural, legal and political studies, economics and neuroscience (D1, 1.2).
- Holism is its organising idea: development, well-being, participation and learning seen together and in context, with play central (D1, 1.8, 1.9, 2.1, 2.2).
- It speaks of many childhoods, not one, and treats childhood as contested and changing, read locally, nationally and globally (D1, 1.5, 1.12, 2.3).
- It is committed to social justice, children's rights and advocacy, and asks graduates to act as agents of change (D1, 1.4, 1.8, 1.11, 1.32).
- Theory and practice are linked throughout; placements are common but optional, and the Level 6 practitioner competencies are an optional route (D1, 1.19, 2.18, 2.20).
- Research, enquiry and reflexivity run through it, including ethical study of young children (D1, 1.13, 3.3).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "framed as vision and mission: questioning dominant thought, anti-oppressive knowledge and practice, room for marginalised voices, respect for each student's identity, inclusive placements; the table carries rights, equity and anti-bias rows (D1, 1.23 to 1.26; 4.4)"
  statements: ["qaa/early-childhood-studies-2022/1.23", "qaa/early-childhood-studies-2022/1.24", "qaa/early-childhood-studies-2022/1.25", "qaa/early-childhood-studies-2022/1.26", "qaa/early-childhood-studies-2022/3.3.b23", "qaa/early-childhood-studies-2022/4.4.b6", "qaa/early-childhood-studies-2022/4.4.b24"]
- theme: theme:accessibility
  inThisSubject: "a section of its own under distinctive features: inclusive design, routes and modes of study, digital inclusion, accessible assessment with reasonable adjustments and assistive technology, accessible spaces; adjustments also in the skill lists (D1, 2.4 to 2.10; 3.3; 3.4; 3.12)"
  statements: ["qaa/early-childhood-studies-2022/2.4", "qaa/early-childhood-studies-2022/2.7", "qaa/early-childhood-studies-2022/2.8", "qaa/early-childhood-studies-2022/2.9", "qaa/early-childhood-studies-2022/2.10", "qaa/early-childhood-studies-2022/3.12", "qaa/early-childhood-studies-2022/3.3.b3", "qaa/early-childhood-studies-2022/3.4.b10"]
- theme: theme:esd
  inThisSubject: "headed Education for sustainable development: an ecological study of early childhood, sustainability through holistic development and equity, the two ESD definitions from the joint guidance, the child as a responsible citizen of the world (D1, 1.27 to 1.31); sustainability also a lens and a rights row in the table (4.4)"
  statements: ["qaa/early-childhood-studies-2022/1.31", "qaa/early-childhood-studies-2022/2.16", "qaa/early-childhood-studies-2022/3.3.b10", "qaa/early-childhood-studies-2022/4.4.b2", "qaa/early-childhood-studies-2022/4.4.b6"]
- theme: theme:enterprise
  inThisSubject: "headed Entrepreneurship and enterprise education (front matter: with employability): advocacy against inequality, innovation and social value, research and practice informing each other, enterprising behaviours and a list of opportunities to develop them (D1, 1.32 to 1.36); employability through digital inclusion, authentic assessment and partnership (2.6, 2.8, 2.19, 2.20)"
  statements: ["qaa/early-childhood-studies-2022/1.33", "qaa/early-childhood-studies-2022/1.35", "qaa/early-childhood-studies-2022/1.36.b1", "qaa/early-childhood-studies-2022/1.36.b2", "qaa/early-childhood-studies-2022/1.36.b3", "qaa/early-childhood-studies-2022/1.36.b4", "qaa/early-childhood-studies-2022/1.36.b5", "qaa/early-childhood-studies-2022/1.36.b6", "qaa/early-childhood-studies-2022/1.36.b7", "qaa/early-childhood-studies-2022/1.36.b8"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "1.2", gloss: "the contributing disciplines, from health and education to law, economics and neuroscience" }
  - { component: "1.9", gloss: "sociocultural context, family and community, play, environment, economic distribution, stress, risk, policy and law" }
  - { component: "2.1", gloss: "conception to eight, holistic development, children's rights, culture and EDI across many childhoods" }
  - { component: "2.2", gloss: "families, development, well-being, participation and learning; safeguarding law; pedagogical approaches" }
practices:
  - { component: "2.7", kind: "teaching", gloss: "face to face, online, flipped, group and individual study, simulation and placements across sectors" }
  - { component: "3.5", kind: "teaching", gloss: "courses designed for ethical awareness, digital literacy, self-assessment and access to support" }
  - { component: "3.6", kind: "learning", gloss: "more self-directed learning over time" }
  - { component: "3.7", kind: "learning", gloss: "independent and group study through reflection, analysis, enquiry, synthesis, evaluation" }
  - { component: "3.8", kind: "teaching", gloss: "supported reflection on one's own childhood and practice, with emotional support" }
  - { component: "3.9", kind: "learning", gloss: "engagement with practice: curriculum planning, health and safety, co-production" }
  - { component: "3.11", kind: "teaching", gloss: "culturally responsive, inclusive and active learning, from guided to independent" }
  - { component: "2.8", kind: "assessment", gloss: "accessible, varied, real-world assessment with adjustments and digital skills" }
  - { component: "3.12", kind: "assessment", gloss: "methods tied to objectives; reasonable adjustments" }
  - { component: "3.13", kind: "assessment", gloss: "eighteen example methods, from examinations to vivas and dissertations" }
  - { component: "3.14", kind: "assessment", gloss: "assessment of practice, required for the competencies; explicit, inclusive criteria" }
  - { component: "3.15", kind: "assessment", gloss: "assessing professional practice by reflection, discussion, portfolios and observation" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.1", award: "bachelor's with honours", items: 34 }
  - { rung: "typical", leadIn: "4.1", award: "bachelor's with honours", items: 34 }
  - { rung: "excellent", leadIn: "4.1", award: "bachelor's with honours", items: 34 }
  - { rung: "threshold", leadIn: "4.1", award: "master's", items: 34 }
rungBases: "4.1 defines four categories: threshold as the minimum to graduate with a single honours degree, typical, excellent, and postgraduate (advanced scholarship); 4.2: the same areas at each level, typical more securely shown than threshold, excellent a high level of proficiency. One table lists each outcome once per row under four column heads, the honours columns labelled 3rd, 2nd lower to 2nd upper, and 1st class."
outcomeLists:
  - { leadIn: "3.3", gloss: "subject-specific skills at graduation", items: 24, award: ["honours"] }
  - { leadIn: "3.4", gloss: "generic skills at graduation", items: 17, award: ["honours"] }
  - { leadIn: "1.36", gloss: "opportunities to develop enterprise skills (provider expectation)", items: 8, award: ["honours", "master's"] }
outcomes:
  - { outcome: "the conceptual foundations of the field", threshold: "qaa/early-childhood-studies-2022/4.4.b1", typical: "qaa/early-childhood-studies-2022/4.4.b1.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b1.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b1.masters", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "babies, young children and diverse childhoods through many disciplines", threshold: "qaa/early-childhood-studies-2022/4.4.b2", typical: "qaa/early-childhood-studies-2022/4.4.b2.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b2.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b2.masters", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "the field's areas of interest and how they connect", threshold: "qaa/early-childhood-studies-2022/4.4.b3", typical: "qaa/early-childhood-studies-2022/4.4.b3.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b3.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b3.masters", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "policy and provision for children and families", threshold: "qaa/early-childhood-studies-2022/4.4.b4", typical: "qaa/early-childhood-studies-2022/4.4.b4.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b4.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b4.masters", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "working across professions, agencies and cultures", threshold: "qaa/early-childhood-studies-2022/4.4.b5", typical: "qaa/early-childhood-studies-2022/4.4.b5.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b5.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b5.masters", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "rights, diversity, equity, justice, sustainability and inclusion in practice", threshold: "qaa/early-childhood-studies-2022/4.4.b6", typical: "qaa/early-childhood-studies-2022/4.4.b6.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b6.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b6.masters", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "pedagogical approaches and values", threshold: "qaa/early-childhood-studies-2022/4.4.b7", typical: "qaa/early-childhood-studies-2022/4.4.b7.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b7.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b7.masters", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "ethics, economics, politics, culture and ideology in children's lives", threshold: "qaa/early-childhood-studies-2022/4.4.b8", typical: "qaa/early-childhood-studies-2022/4.4.b8.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b8.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b8.masters", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "methods for systematic study and research", threshold: "qaa/early-childhood-studies-2022/4.4.b9", typical: "qaa/early-childhood-studies-2022/4.4.b9.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b9.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b9.masters", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "reasoning about theory, policy, practice and evidence", threshold: "qaa/early-childhood-studies-2022/4.4.b10", typical: "qaa/early-childhood-studies-2022/4.4.b10.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b10.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b10.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "taking up theoretical perspectives", threshold: "qaa/early-childhood-studies-2022/4.4.b11", typical: "qaa/early-childhood-studies-2022/4.4.b11.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b11.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b11.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "critiquing theory, practice and research", threshold: "qaa/early-childhood-studies-2022/4.4.b12", typical: "qaa/early-childhood-studies-2022/4.4.b12.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b12.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b12.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "reflecting on disciplinary perspectives", threshold: "qaa/early-childhood-studies-2022/4.4.b13", typical: "qaa/early-childhood-studies-2022/4.4.b13.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b13.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b13.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "contexts in young children's lives", threshold: "qaa/early-childhood-studies-2022/4.4.b14", typical: "qaa/early-childhood-studies-2022/4.4.b14.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b14.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b14.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "policies, institutions and agencies", threshold: "qaa/early-childhood-studies-2022/4.4.b15", typical: "qaa/early-childhood-studies-2022/4.4.b15.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b15.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b15.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "competing constructions of childhood", threshold: "qaa/early-childhood-studies-2022/4.4.b16", typical: "qaa/early-childhood-studies-2022/4.4.b16.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b16.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b16.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "skills for relational pedagogy", threshold: "qaa/early-childhood-studies-2022/4.4.b17", typical: "qaa/early-childhood-studies-2022/4.4.b17.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b17.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b17.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "observation and analysis", threshold: "qaa/early-childhood-studies-2022/4.4.b18", typical: "qaa/early-childhood-studies-2022/4.4.b18.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b18.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b18.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "patterns in play, behaviour and experience", threshold: "qaa/early-childhood-studies-2022/4.4.b19", typical: "qaa/early-childhood-studies-2022/4.4.b19.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b19.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b19.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "attunement and advocacy", threshold: "qaa/early-childhood-studies-2022/4.4.b20", typical: "qaa/early-childhood-studies-2022/4.4.b20.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b20.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b20.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "planning for holistic development, health, protection and safety", threshold: "qaa/early-childhood-studies-2022/4.4.b21", typical: "qaa/early-childhood-studies-2022/4.4.b21.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b21.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b21.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "collaboration with parents, carers and other stakeholders", threshold: "qaa/early-childhood-studies-2022/4.4.b22", typical: "qaa/early-childhood-studies-2022/4.4.b22.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b22.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b22.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "arguing for better joint professional practice", threshold: "qaa/early-childhood-studies-2022/4.4.b23", typical: "qaa/early-childhood-studies-2022/4.4.b23.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b23.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b23.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "challenging inequality", threshold: "qaa/early-childhood-studies-2022/4.4.b24", typical: "qaa/early-childhood-studies-2022/4.4.b24.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b24.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b24.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "leadership for transformational change", threshold: "qaa/early-childhood-studies-2022/4.4.b25", typical: "qaa/early-childhood-studies-2022/4.4.b25.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b25.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b25.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "research questions and research competence", threshold: "qaa/early-childhood-studies-2022/4.4.b26", typical: "qaa/early-childhood-studies-2022/4.4.b26.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b26.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b26.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "the supervised research project", threshold: "qaa/early-childhood-studies-2022/4.4.b27", typical: "qaa/early-childhood-studies-2022/4.4.b27.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b27.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b27.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "the ethics of studying children", threshold: "qaa/early-childhood-studies-2022/4.4.b28", typical: "qaa/early-childhood-studies-2022/4.4.b28.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b28.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b28.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "ethical principles in the research project", threshold: "qaa/early-childhood-studies-2022/4.4.b29", typical: "qaa/early-childhood-studies-2022/4.4.b29.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b29.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b29.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "arguing a point of view from theory", threshold: "qaa/early-childhood-studies-2022/4.4.b30", typical: "qaa/early-childhood-studies-2022/4.4.b30.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b30.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b30.masters", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "using sources of information", threshold: "qaa/early-childhood-studies-2022/4.4.b31", typical: "qaa/early-childhood-studies-2022/4.4.b31.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b31.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b31.masters", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "listening and reflecting on skills and views", threshold: "qaa/early-childhood-studies-2022/4.4.b32", typical: "qaa/early-childhood-studies-2022/4.4.b32.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b32.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b32.masters", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "managing own learning", threshold: "qaa/early-childhood-studies-2022/4.4.b33", typical: "qaa/early-childhood-studies-2022/4.4.b33.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b33.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b33.masters", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "digital technologies and literacies", threshold: "qaa/early-childhood-studies-2022/4.4.b34", typical: "qaa/early-childhood-studies-2022/4.4.b34.typical", excellent: "qaa/early-childhood-studies-2022/4.4.b34.excellent", masters: "qaa/early-childhood-studies-2022/4.4.b34.masters", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
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
- { body: "Early Childhood Studies Degrees Network (ECSDN)", says: "writes and reviews the Level 6 graduate practitioner competencies and advises on them; institutions offering the competencies are expected (1.18) and required (2.25) to be current members (D1, 1.18, 2.25; section 5)", requirements: "not yet ingested (Part E)" }
- { body: "professional, statutory and regulatory bodies (none named)", says: "may set requirements beside the statement and may evaluate and accredit courses with professional outcomes; some degrees let students meet statutory or regulatory requirements (D1, front matter; 2.18; 2.25; 3.10; 3.15)", requirements: "not-applicable-by-design: no body is named" }
- { body: "Office for Students", says: "its regulatory framework does not treat the statement as a sector-recognised standard in England (D1, front matter)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.4", "1.5", "1.23", "1.24", "1.25", "1.26", "2.1", "2.16", "3.11", "3.14", "4.4"], statements: ["qaa/early-childhood-studies-2022/1.23", "qaa/early-childhood-studies-2022/1.24", "qaa/early-childhood-studies-2022/1.25", "qaa/early-childhood-studies-2022/1.26", "qaa/early-childhood-studies-2022/3.3.b23", "qaa/early-childhood-studies-2022/4.4.b6", "qaa/early-childhood-studies-2022/4.4.b24"] }
  - { id: "theme:accessibility", named: "Accessibility", carriedIn: ["1.26", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9", "2.10", "3.3", "3.4", "3.12"], statements: ["qaa/early-childhood-studies-2022/2.4", "qaa/early-childhood-studies-2022/2.7", "qaa/early-childhood-studies-2022/2.8", "qaa/early-childhood-studies-2022/2.9", "qaa/early-childhood-studies-2022/2.10", "qaa/early-childhood-studies-2022/3.12", "qaa/early-childhood-studies-2022/3.3.b3", "qaa/early-childhood-studies-2022/3.4.b10"] }
  - { id: "theme:esd", named: "Education for sustainable development", carriedIn: ["1.5", "1.8", "1.27", "1.28", "1.29", "1.30", "1.31", "2.16", "4.4"], statements: ["qaa/early-childhood-studies-2022/1.31", "qaa/early-childhood-studies-2022/2.16", "qaa/early-childhood-studies-2022/3.3.b10", "qaa/early-childhood-studies-2022/4.4.b2", "qaa/early-childhood-studies-2022/4.4.b6"] }
  - { id: "theme:enterprise", named: "Entrepreneurship and enterprise education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.32", "1.33", "1.34", "1.35", "1.36", "2.6", "2.8", "2.19", "2.20"], statements: ["qaa/early-childhood-studies-2022/1.33", "qaa/early-childhood-studies-2022/1.35", "qaa/early-childhood-studies-2022/1.36.b1", "qaa/early-childhood-studies-2022/1.36.b2", "qaa/early-childhood-studies-2022/1.36.b3", "qaa/early-childhood-studies-2022/1.36.b4", "qaa/early-childhood-studies-2022/1.36.b5", "qaa/early-childhood-studies-2022/1.36.b6", "qaa/early-childhood-studies-2022/1.36.b7", "qaa/early-childhood-studies-2022/1.36.b8"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.11", "2.13"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.11", "2.13"] }
  - { framework: "other: \"Level 6\" of the practitioner competencies, framework not named; read as fheq:6 (inferred)", levels: ["fheq:6"], citedIn: ["1.6", "1.18", "1.19", "2.20"] }
  - { framework: "other: England's early years Level 3 (a staff qualification level, not a higher education framework)", levels: [], citedIn: ["2.20"] }
bodies:
  - { body: "Early Childhood Studies Degrees Network", citedIn: ["1.18", "2.25"] }
  - { body: "professional, statutory and regulatory bodies (generic)", citedIn: ["front matter", "2.18", "2.25", "3.10", "3.15"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
sharedDocuments:
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA’s and Advance HE’s Education for Sustainable Development Guidance Principles", citedIn: ["1.31"], role: "source of the two ESD definitions in 1.29 and 1.30" }
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D (not cited by name)", named: "the degree classes in the table heads: 3rd class; 2nd class lower to 2nd class upper; 1st class", citedIn: ["4.4"], role: "labels each honours rung by class; the link to the classification descriptions is inferred (Part E)" }
  - { document: "ECSDN Early Childhood Graduate Practitioner Competencies (not yet ingested: listed in Part E)", named: "Appendix 1: Early Childhood Graduate Practitioner Competencies", citedIn: ["1.19", "2.20"], role: "the optional Level 6 practice route" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code", citedIn: ["front matter"], role: "course design, learning and teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "early-childhood", definition: "the period from conception to eight, including perinatal health, in which development is shaped by environment and people; more than preparation for school (D1, 1.1, 2.1)", beneficiaryDefinition: "the years from before birth to age eight", scopeNote: "the field takes in global definitions, including the first 1001 days", category: "unknown", practices: ["education", "health", "social care"] }
- { slug: "multiple-childhoods", definition: "the many forms childhood takes across cultures, societies and places, studied in the plural rather than as one norm (D1, 1.5, 1.7, 2.1)", beneficiaryDefinition: "the different ways children grow up around the world", scopeNote: "used throughout the statement and its table", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the minimum standard needed to graduate with a single honours degree in the subject, labelled third class in the table (D1, 4.1; 1.16; 4.4)", beneficiaryDefinition: "the least you need to show to pass an honours degree", scopeNote: "honours only", category: "unknown", practices: ["education"] }
- { slug: "typical-standard", definition: "what a typical student is expected to attain, labelled lower to upper second class (D1, 4.1; 4.4)", beneficiaryDefinition: "what most students reach", scopeNote: "honours only", category: "unknown", practices: ["education"] }
- { slug: "excellent-standard", definition: "what the highest-attaining student is expected to achieve, labelled first class (D1, 4.1; 4.4)", beneficiaryDefinition: "the level of first-class work", scopeNote: "honours only", category: "unknown", practices: ["education"] }
- { slug: "postgraduate-standard", definition: "what students achieve who show advanced scholarship and understand how research advances knowledge (D1, 4.1)", beneficiaryDefinition: "what master's study asks of you", scopeNote: "a fourth column in the table, for master's study", category: "unknown", practices: ["education"] }
- { slug: "education-for-sustainable-development", definition: "both an aspirational, continuing process of tackling social, environmental and economic concerns and the building of curricula that support sustainable development (D1, 1.29, 1.30)", beneficiaryDefinition: "learning that helps make the world fairer and more sustainable", scopeNote: "definitions taken from the joint QAA and Advance HE guidance (1.31)", category: "unknown", practices: ["education"] }
- { slug: "subject-specific-and-generic-skills", definition: "skills tied to subject knowledge or integral to the degree, set against transferable skills less tied to the subject; the split is called artificial (D1, 3.1, 3.2)", beneficiaryDefinition: "skills for this subject and skills you can use anywhere", scopeNote: "3.3 and 3.4 list them", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "early-childhood", form: "early childhood", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "multiple-childhoods", form: "multiple childhoods", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "threshold standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "typical-standard", form: "typical standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "excellent-standard", form: "excellent standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "postgraduate-standard", form: "postgraduate standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "education-for-sustainable-development", form: "Education for Sustainable Development (ESD)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "subject-specific-and-generic-skills", form: "subject-specific skills; generic skills", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Early Childhood Studies"
  edition: "March 2022 (fourth edition)"
  year: 2022
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/early-childhood-studies-2022/early-childhood-studies-2022.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: c45f8fb44d2278bd09400a0ad048647528c8386df892551bc5b5de599a4e37c6
  heldFiles: ["wkspc2601-library/txt/qaa-2022-early-childhood-studies-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2022-early-childhood-studies-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2022-early-childhood-studies-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2022-early-childhood-studies-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0053", title: "ECSDN, Early Childhood Graduate Practitioner Competencies (revised March 2026)", why: "the optional Level 6 route the statement cites (1.19, 2.20); held only as an appendix inside this text; wanted as its own standards document", status: "wanted" }
- { w: "W-std-0054", title: "QAA Subject Benchmark Statement: Early Childhood Studies, third edition (2019)", why: "the edition this one supersedes, for the change comparison", status: "wanted" }
```

## Part E Gaps and questions
- Held text: stan's text carries, after QAA's back matter, the ECSDN's Graduate Practitioner Competencies revised March 2026 (contents line 'Appendix: ECSDN Graduate Practitioner Competencies, March 2026'), four years after the statement's publication; excluded here as another issuer's document. The skeleton labels it 'membership of the advisory group' and a 'contents listing'. For Abbott: was the QAA PDF itself updated with this appendix, and should the competencies be ingested as their own document (D3)?
- New rung shape: one table with four columns, threshold (3rd class), typical (2nd lower to 2nd upper), excellent (1st) and postgraduate. The fourth (postgraduate) column is recorded as rung `threshold` for another award, master's at fheq:7, with the id suffix `.masters` (std, 18:50, BM-BRIEF 0.2.3: a master's column is another award, not a rung); its force stays `will`, from 4.2.
- Rung ids follow the batch 1 convention: the threshold cell is 4.4.b<n> (the table sits after 4.4, unnumbered), the others 4.4.b<n>.typical, .excellent and .masters; 34 rows, 136 cell records. The cells are cut from the held text by bm_content.py (CELLS), not by the skeleton, which held the whole table inside 4.4.
- gradeOf: typical to threshold and excellent to typical in each row are `stated` (the issuer pairs the cells in one row); the postgraduate cells carry no gradeOf, being for another award; SB4 outcomes list them under `postgraduate`.
- The typical rung spans two degree classes (lower and upper second); the honours rungs are labelled by class in the table heads, but the statement does not cite Annex D: the link to qaa/fheq-2024/annex-d is inferred (S5, SB6).
- Force: the honours threshold cells are `threshold` (4.1 defines the rung as the minimum to graduate); typical, excellent and postgraduate cells take 4.2's "is expected to be able to demonstrate", recorded as will with forceFrom 4.2. The lead-in of 3.3 and 3.4 is also "is expected to be able to", recorded as will. For Abbott: is "expected to be able to" will?
- Obliging words outside the five: 1.18 "an expectation" (describes); 1.36 "are to be provided" (describes, 8 items); 2.11 "it is expected" (describes); 3.6 "are expected to" (describes); 3.8 "There is a requirement" and 3.14 "This is a requirement" (must, by the batch 1 convention); 2.1 "need to"; 1.17, 1.22, 2.6 "It is important" (not recorded as statements).
- Mixed modals in one paragraph, recorded at the strongest with each sentence's own modal kept in the paraphrase: 1.25 (will, should, must), 2.20 (must, should), 1.31 and 2.12 (will, should).
- Plain-present or descriptive paragraphs not recorded as statements: 3.5 (courses are generally designed to ..., 5 items), 3.7, 3.9, 3.11, 3.15 and 2.21, 2.23 (what review and external examiners typically do); 3.13 lists assessment methods with "may" and is a practice component, not a statement; 1.19 and 2.20's "This will enable" describe the competencies' effect.
- Skeleton corrections: 3.3.b6 has two sub-items (3.3.b7, 3.3.b8, marked "-" in the text), kept as their own records under the lead-in 3.3 (forceFrom), with no verbs; 3.3.b11 runs across a page break (its span holds the page number 15); 3.3.b20 holds two items run together ("... ecological context analyse data ..."); 3.3.b24 and 3.4.b17 trimmed of the next sub-heading; paragraph spans trimmed of the sub-headings and page numbers caught at their ends (1.23, 1.26, 1.31, 2.10, 2.16, 2.20, 2.25, 3.6, 3.16).
- Table cells cut short by the page layout: on page 21 the excellent and postgraduate cells of the policy row (4.4.b4.excellent, 4.4.b4.postgraduate) continue after the page head, so their spans end at "and provision" and "and provision for"; the remainder ("for babies, young children, families and communities") is outside the span.
- 3.3.b3 and 3.3.b17 are near repeats (observation and analysis, the first with reasonable adjustments); both recorded.
- Levels: "Level 6" of the practitioner competencies (1.6, 1.18, 1.19, 2.20) names no framework; read as fheq:6 (inferred). "Level 3 requirements in England" (2.20) is an early years staff qualification level, not a higher education framework level; not mapped.
- Codes: hecos 100457 'early childhood studies' matches the statement's subject name (stated); CAH15-04-02 'childhood and youth studies' is the HECoS code's CAH3 parent, inferred; 'childhood studies degrees' (4.2) given hecos 100456 in statedSubjects only.
- Awards: the statement can apply to foundation degrees, top-ups, honours, master's and doctorates (1.6, 2.15, 4.2) but states standards only for honours and postgraduate (master's) study; awardsCovered lists those two.
- Section 5 lists professional organisations (SEFDEY, BECERA, EECERA, Early Childhood Forum, UNICEF, UKCHRC) as resources; excluded matter, not recorded as bodies in SB5.
- Patterns that differ from Psychology: a single four-column table rather than separate rung lists; a postgraduate column; rungs labelled by degree class; three cross-cutting themes framed as 'Vision' and 'Mission' with accessibility as its own section under distinctive features; a sector network (ECSDN) and an optional Level 6 practice route in place of a PSRB; no Annex D citation.
- S9 commentary not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:17: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0100 (P1); built by tools/bm_build.py.
