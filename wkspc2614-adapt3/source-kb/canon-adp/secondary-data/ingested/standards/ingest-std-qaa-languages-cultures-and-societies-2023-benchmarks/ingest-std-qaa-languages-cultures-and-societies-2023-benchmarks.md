---
id: std:doc:qaa-languages-cultures-and-societies-2023-benchmarks
title: "Subject Benchmark Statement Languages, Cultures and Societies"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100329", label: "modern languages", basis: "stated" }
  - { scheme: "cah", code: "CAH19-04-09", label: "others in language and area studies", basis: "inferred" }
  - { scheme: "cah", code: "CAH19-04", label: "languages and area studies", basis: "inferred" }
  - { scheme: "cah", code: "CAH19", label: "language and area studies", basis: "inferred" }
  - { scheme: "hecos", code: "101130", label: "translation studies", basis: "stated" }
  - { scheme: "hecos", code: "101118", label: "Celtic studies", basis: "inferred" }
  - { scheme: "hecos", code: "100317", label: "British Sign Language studies", basis: "inferred" }
edition: "March 2023 (fifth edition)"
published: 2023-03
status: current
supersedes: "the fourth edition (2019), revised by QAA from the third (2015); earlier Languages and Related Studies editions 2007 and 2002"
heldText: { method: sha256-bytes, raw: 958b10f1f2733ce2f1f11ba8b9fa7a8b9e531265e63349305b02c7ae257e30cf, normalised: a9642b10d8c777b1c51e6f79f3acaadb60008bb6147db35bda68aff3ba5cc66e }
heldTextStan: { method: sha256-stan, raw: 958b10f1f2733ce2f1f11ba8b9fa7a8b9e531265e63349305b02c7ae257e30cf, normalised: bf34ba28e31f5b8ce6c30b11ff8b1650fa6f6f2c3093811cff773d960785e232 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, revision with cross-cutting themes (this statement: fifth edition, March 2023)"
awardsCovered: ["bachelor's with honours"]
levelsCovered: ["fheq:6", "fqheis:10"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0115 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:44"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Languages, Cultures and Societies (QAA, March 2023)

> Run 0115, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2023-languages-cultures-societies-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in Languages, Cultures and Societies (modern and other languages studied with their cultures and societies) can do at the end of an honours degree. It states one rung only, the threshold, in five groups: language proficiency (towards or at CEFR C1), explicit knowledge of language, intercultural awareness and pluricultural competence, subject knowledge and skills and general skills. Reach for it when designing, reviewing or describing a languages course or its outcomes. It is not a curriculum, it does not set master's standards and it is not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2023 as the fifth edition, the statement covers single, joint and combined honours degrees in languages, cultures and societies across the four UK nations and mentions master's provision without setting standards for it. It describes the subject and its graduates (1.10, 1.11), the four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability; enterprise and entrepreneurship), distinctive features (design, progression, flexibility, partnership, monitoring), content, teaching, immersive placements and assessment, and threshold standards only, at FHEQ level 6 and FQHEIS level 10, applying to courses where languages make up at least a third of study in every year. Performance above threshold is left to Annex D of the FHEQ. It names the CEFR as the proficiency scale and no professional body.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Languages, Cultures and Societies"
edition: "March 2023 (fifth edition)"
dates:
  published: 2023-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales (Quality Assessment Framework for Wales) and Scotland (Quality Enhancement Framework); part of the quality arrangements in Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2023", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate of an honours degree in languages, cultures and societies knows, understands and can do at threshold and the features, content, teaching and assessment of such degrees"
appliesTo:
  awards: ["bachelor's with honours"]
  levels: ["fheq:6", "fqheis:10"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This Subject Benchmark Statement refers to the provision of undergraduate and postgraduate degrees in Languages, Cultures and Societies (LCS) in the four nations of the UK.\" (D1, 1.1); the standards apply to courses in which languages are at least one-third of study and studied in every year (D1, 4.5)"
statedSubjects:
  - { name: "Languages, Cultures and Societies (LCS)", locator: "(D1, 1.1; 1.5)", kind: "subject", codes: [{ scheme: "hecos", code: "100329", label: "modern languages" }] }
  - { name: "Modern Languages", locator: "(D1, 4.6)", kind: "programme title", codes: [{ scheme: "hecos", code: "100329", label: "modern languages" }] }
  - { name: "translation and interpreting", locator: "(D1, 1.4; 2.2)", kind: "specialism", codes: [{ scheme: "hecos", code: "101130", label: "translation studies" }] }
  - { name: "Celtic languages", locator: "(D1, 1.8)", kind: "specialism", codes: [{ scheme: "hecos", code: "101118", label: "Celtic studies" }] }
  - { name: "sign languages", locator: "(D1, 1.14; 4.11)", kind: "specialism", codes: [{ scheme: "hecos", code: "100317", label: "British Sign Language studies" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "scope: degrees of every pattern across the UK, honours and master's" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "honours assumed; context holds for exit awards too" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "elective language study elsewhere gains some of the same skills" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "professional master's, chiefly translation and interpreting; interdisciplinary topics" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "how the subject is organised within institutions varies" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "overlap with English and Linguistics; TESOL left out" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Languages, Cultures and Societies degree", gloss: "core: communicative proficiency plus study of language, culture and society" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Languages, Cultures and Societies degree", gloss: "immersive learning and the year abroad as typical features" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Languages, Cultures and Societies degree", gloss: "value to the UK economy and society; graduate careers" }
  - { number: "1.10", order: 12, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of a Languages, Cultures and Societies degree", gloss: "profile of the typical graduate (outcome list)" }
  - { number: "1.11", order: 13, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of a Languages, Cultures and Societies degree", gloss: "capabilities shared with other SHAPE subjects (outcome list)" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "outward-looking, inclusive learning environments" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "varied teaching, assessment and delivery to widen access" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "minority, sign, heritage and constructed languages; language rights" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "injustice, colonialism and inclusive curriculum choices" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "against native-speakerism; proficiency measured by a framework" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "linguistic diversity beyond a single standard form" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "placements, diversity and student well-being abroad" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "uneven school provision; supporting varied prior learning" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "beginners and heritage speakers; languages open to everyone" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "barriers to placements abroad and alternative immersion" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainability through equality, peace and justice themes" }
  - { number: "1.23", order: 25, componentType: stem, parent: "section 1", heading: "Sustainability", gloss: "the four UN goals the subject engages most" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "nature, climate and finding common ground across cultures" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "the carbon cost of travel for placements" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "what enterprise education adds for careers" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise attributes graduates show" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "placements build entrepreneurial attributes" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "students as sensitive communicators and mediators at work" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "applied linguistics and sociolinguistics as workplace assets" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "cultural and digital literacy; working with machine translation" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise beyond employment; pointer to QAA guidance" }
  - { number: "2.1", order: 36, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "undergraduate study: proficiency plus engagement with cultures; teaching medium" }
  - { number: "2.2", order: 37, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "postgraduate depth, autonomy and professional skills" }
  - { number: "2.3", order: 38, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "analysis of historical and current material; joint degrees with SHAPE subjects" }
  - { number: "2.4", order: 39, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "combinations with STEM subjects" }
  - { number: "2.5", order: 40, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "intercultural and transnational by nature" }
  - { number: "2.6", order: 41, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "varied ways of bringing out intercultural dimensions" }
  - { number: "2.7", order: 42, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "diversity of voices against Anglophone dominance" }
  - { number: "2.8", order: 43, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression toward the threshold; second-class degrees and further study" }
  - { number: "2.9", order: 44, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined honours students" }
  - { number: "2.10", order: 45, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards, integrated master's and part-time routes" }
  - { number: "2.11", order: 46, componentType: stem, parent: "section 2", heading: "Progression", gloss: "what shapes progression; its consistent features" }
  - { number: "2.12", order: 47, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "study modes and levels of language modules" }
  - { number: "2.13", order: 48, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "language components in other subjects' degrees" }
  - { number: "2.14", order: 49, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "digital platforms and flipped teaching for flexibility" }
  - { number: "2.15", order: 50, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "work placements and internships" }
  - { number: "2.16", order: 51, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "civic and community partnerships" }
  - { number: "2.17", order: 52, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "exchange agreements; employer projects at master's level" }
  - { number: "2.18", order: 53, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.19", order: 54, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.20", order: 55, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners, one per language" }
  - { number: "3.1", order: 57, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "content varies; single and joint honours coverage" }
  - { number: "3.2", order: 58, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "content as a framework; designers stay open to change" }
  - { number: "3.3", order: 59, componentType: area, parent: "section 3", heading: "Subject-specific content", gloss: "subject content: proficiency, awareness, culture and society" }
  - { number: "3.4", order: 60, componentType: area, parent: "section 3", heading: "Subject-specific content", gloss: "the subject-specific skills courses develop" }
  - { number: "3.5", order: 61, componentType: area, parent: "section 3", heading: "Generic, transferable and employability content", gloss: "the distinctive education languages give" }
  - { number: "3.6", order: 62, componentType: area, parent: "section 3", heading: "Generic, transferable and employability content", gloss: "communicative, transactional and problem-solving skills" }
  - { number: "3.7", order: 63, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "methods listed in no order of priority" }
  - { number: "3.8", order: 64, componentType: practice, parent: "section 3", heading: "Characteristics of the study of Languages, Cultures and Societies", gloss: "what shapes teaching methods" }
  - { number: "3.9", order: 65, componentType: practice, parent: "section 3", heading: "Characteristics of the study of Languages, Cultures and Societies", gloss: "intensive language learning; beginners need more contact" }
  - { number: "3.10", order: 66, componentType: practice, parent: "section 3", heading: "Characteristics of the study of Languages, Cultures and Societies", gloss: "contact with proficient users and authentic material" }
  - { number: "3.11", order: 67, componentType: practice, parent: "section 3", heading: "Characteristics of the study of Languages, Cultures and Societies", gloss: "language as a gateway to culture and society" }
  - { number: "3.12", order: 68, componentType: practice, parent: "section 3", heading: "Characteristics of the study of Languages, Cultures and Societies", gloss: "learning technology and online resources" }
  - { number: "3.13", order: 69, componentType: practice, parent: "section 3", heading: "Characteristics of the study of Languages, Cultures and Societies", gloss: "learner autonomy and guided independent study" }
  - { number: "3.14", order: 70, componentType: practice, parent: "section 3", heading: "Teaching and learning methods", gloss: "methods for developing language skills" }
  - { number: "3.15", order: 71, componentType: practice, parent: "section 3", heading: "Teaching and learning methods", gloss: "methods for studying cultures and societies" }
  - { number: "3.16", order: 72, componentType: practice, parent: "section 3", heading: "International and national immersive placements", gloss: "residence in a target-language country" }
  - { number: "3.17", order: 73, componentType: practice, parent: "section 3", heading: "International and national immersive placements", gloss: "how placements vary and are supported" }
  - { number: "3.18", order: 74, componentType: practice, parent: "section 3", heading: "International and national immersive placements", gloss: "what immersive placements typically do" }
  - { number: "3.19", order: 75, componentType: practice, parent: "section 3", heading: "International and national immersive placements", gloss: "other routes when residence abroad is not possible" }
  - { number: "3.20", order: 76, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "inclusive principles of assessment design" }
  - { number: "3.21", order: 77, componentType: practice, parent: "section 3", heading: "Assessment of language proficiency", gloss: "feedback and a wide range of assessment types" }
  - { number: "3.22", order: 78, componentType: practice, parent: "section 3", heading: "Assessment of language proficiency", gloss: "the four skill areas assessed for proficiency" }
  - { number: "3.23", order: 79, componentType: practice, parent: "section 3", heading: "Assessment of language proficiency", gloss: "forms of proficiency assessment" }
  - { number: "3.24", order: 80, componentType: practice, parent: "section 3", heading: "Assessment of language proficiency", gloss: "further forms at master's level" }
  - { number: "3.25", order: 81, componentType: practice, parent: "section 3", heading: "Assessment of language proficiency", gloss: "assessing in the target language" }
  - { number: "3.26", order: 82, componentType: practice, parent: "section 3", heading: "Assessment of subject-related studies", gloss: "assessment of cultural, linguistic and social study" }
  - { number: "4.1", order: 84, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "standards are the minimum for the honours award" }
  - { number: "4.2", order: 85, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed threshold; Annex D for the classes" }
  - { number: "4.3", order: 86, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the CEFR for judging proficiency" }
  - { number: "4.4", order: 87, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "specifications cite the CEFR or other scales such as HSK" }
  - { number: "4.5", order: 88, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "where the standards apply: a third of study, every year" }
  - { number: "4.6", order: 89, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "award titles such degrees carry" }
  - { number: "4.7", order: 90, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "smaller language share: not every element expected" }
  - { number: "4.8", order: 91, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "no set curriculum; read with course documentation" }
  - { number: "4.9", order: 92, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "what shapes course objectives and outcomes" }
  - { number: "4.10", order: 93, componentType: stem, parent: "section 4", heading: "Standard of achievement at threshold level: Language proficiency", gloss: "threshold: language proficiency, towards or at C1" }
  - { number: "4.11", order: 94, componentType: paragraph, parent: "section 4", heading: "Standard of achievement at threshold level: Language proficiency", gloss: "when C1 is out of reach; B2 as the usual alternative" }
  - { number: "4.12", order: 95, componentType: stem, parent: "section 4", heading: "Explicit knowledge of language", gloss: "threshold: explicit knowledge of language" }
  - { number: "4.13", order: 96, componentType: stem, parent: "section 4", heading: "Intercultural awareness and pluricultural competence", gloss: "threshold: knowledge of cultures and societies" }
  - { number: "4.14", order: 97, componentType: stem, parent: "section 4", heading: "Intercultural awareness and pluricultural competence", gloss: "threshold: intercultural skills (continues 4.13)" }
  - { number: "4.15", order: 98, componentType: stem, parent: "section 4", heading: "Subject-specific knowledge and skills", gloss: "threshold: subject-specific knowledge and skills" }
  - { number: "4.16", order: 99, componentType: stem, parent: "section 4", heading: "General and transferable skills", gloss: "threshold: general and transferable skills" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Languages, Cultures and Societies degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Languages, Cultures and Societies degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1 and S2" }
  - { number: "section headings", heading: "section heading lines 1 to 4", kind: "other: headings, recorded in S3 as sections" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for SB6 and S7" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for Languages, Cultures and Societies", kind: "other: membership lists, read for SB5 and S8" }
  - { number: "none", heading: "closing page: edition, publication date and copyright", kind: "other: read for S1 and S8" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 60 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/languages-cultures-and-societies-2023/1.10.b1
  locator: { number: "1.10.b1", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 13105, end: 13319 }
  source: "have a high standard of proficiency in the language(s) studied, with strong productive, receptive, interactive and mediating skills, making them confident and sophisticated communicators in the language(s) studied."
  stem: "1.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["have"]
  about: "high proficiency in the studied languages"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates typically reach a high level in the language or languages studied, strong in producing, receiving, interacting and mediating, so they communicate in them with confidence and subtlety."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.10.b2
  locator: { number: "1.10.b2", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 13322, end: 13528 }
  source: "are aware of the broader context in which communication takes places, are sensitive to variations in language use and their significance, and are able to deal with uncertainty and ambiguity in communication"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["are", "deal"]
  about: "context, variation and ambiguity in communication"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates typically understand the wider setting of communication, notice how usage varies and why it matters and can handle uncertainty and ambiguity when communicating."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.10.b3
  locator: { number: "1.10.b3", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 13531, end: 13741 }
  source: "are aware of, and in some cases acquire, competence in relevant language technologies, such as computer-assisted translation, language-processing software, language-learning software and online language corpora"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["are", "acquire"]
  about: "awareness of language technologies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates typically know about relevant language technologies, such as translation tools, language software and corpora, and some become skilled with them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.10.b4
  locator: { number: "1.10.b4", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 13744, end: 13882 }
  source: "have an open mindset and are able to see the world through the eyes of others, enabling them to understand and value multiple perspectives"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["have", "see", "understand", "value"]
  about: "open mindset and multiple perspectives"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates typically have an open outlook and can view the world as others do, so they understand and value more than one perspective."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.10.b5
  locator: { number: "1.10.b5", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 13885, end: 14203 }
  source: "are able to appreciate, analyse and critically interpret a wide diversity of cultural forms, products and practices, including manifestations of community, local, regional and national cultures; forms of ‘high’ and ‘popular’ culture, material culture and digital culture; and the customs and practices of everyday life"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["appreciate", "analyse", "interpret"]
  about: "interpreting diverse cultural forms"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates typically appreciate, analyse and critically interpret a wide range of cultural forms, products and practices, from local and national cultures to high, popular, material and digital culture and everyday customs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.10.b6
  locator: { number: "1.10.b6", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 14206, end: 14394 }
  source: "are able to understand, mediate, analyse and compare ideas and events that cross national, cultural or linguistic boundaries, such as current and historical relationships between countries"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["understand", "mediate", "analyse", "compare"]
  about: "ideas and events across boundaries"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates typically grasp, mediate and compare ideas and happenings that cross national, cultural or linguistic borders, such as relations between countries past and present and analyse them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.10.b7
  locator: { number: "1.10.b7", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 14397, end: 14606 }
  source: "are able to address questions and problems comparatively across languages, cultures and societies, whether transnationally and/or with awareness of regional and/or minoritised languages, cultures and societies"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["address"]
  about: "comparative work across languages and cultures"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates typically tackle questions comparatively across languages, cultures and societies, transnationally or with attention to regional and minoritised ones."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.10.b8
  locator: { number: "1.10.b8", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 14609, end: 14804 }
  source: "are likely to possess the intercultural skills and language proficiency to facilitate their international mobility, especially where their degree has included a period of international placement."
  stem: "1.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["are", "possess", "facilitate"]
  about: "mobility through language and intercultural skill"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates typically have the intercultural skills and language ability to move and work internationally, especially when the degree included a placement abroad."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.11.b1
  locator: { number: "1.11.b1", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 15147, end: 15280 }
  source: "work independently while engaging with supervision and guidance, reflecting on their own progress and making use of feedback provided"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["work", "engaging", "reflecting"]
  about: "independent work using supervision and feedback"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates develop the capacity to work on their own while using supervision and guidance, reflecting on progress and acting on feedback."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.11.b2
  locator: { number: "1.11.b2", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 15283, end: 15334 }
  source: "work as part of a team as an effective collaborator"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["work"]
  about: "teamwork"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates develop as effective collaborators within a team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.11.b3
  locator: { number: "1.11.b3", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 15340, end: 15454 }
  source: "demonstrate initiative, self-discipline and self-direction, for example by managing their working time efficiently"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "managing"]
  about: "initiative and self-management"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates develop initiative, self-discipline and self-direction, for instance in managing their time well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.11.b4
  locator: { number: "1.11.b4", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 15457, end: 15567 }
  source: "demonstrate appropriate means of gathering, organising and deploying a range of evidence, data and information"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "gathering", "organising", "deploying"]
  about: "handling evidence and information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates develop sound ways of collecting, ordering and using a range of evidence, data and information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.11.b5
  locator: { number: "1.11.b5", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 15570, end: 15717 }
  source: "show analytical ability, questioning habits, and the capacity to consider and solve problems (including those to which there is no single solution)"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["show", "consider", "solve"]
  about: "analysis and problem-solving"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates develop analytical ability, a questioning habit and the capacity to work through problems, including those without one right answer."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.11.b6
  locator: { number: "1.11.b6", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 15720, end: 15783 }
  source: "demonstrate conceptual grasp and the ability to shape arguments"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "shape"]
  about: "conceptual grasp and argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates develop a grasp of concepts and the ability to build arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.11.b7
  locator: { number: "1.11.b7", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 15786, end: 15868 }
  source: "exhibit structure, coherence and clarity of verbal and/or non-verbal communication"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["exhibit"]
  about: "clear structured communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates develop structure, coherence and clarity in verbal and non-verbal communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.11.b8
  locator: { number: "1.11.b8", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 15871, end: 16013 }
  source: "show intellectual integrity, maturity and independence, including the ability to recognise strengths and weaknesses in the arguments of others"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["show", "recognise"]
  about: "intellectual integrity and independence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates develop intellectual integrity, maturity and independence, including spotting where others' arguments are strong or weak."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.11.b9
  locator: { number: "1.11.b9", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 16016, end: 16058 }
  source: "exhibit imaginative insight and creativity"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["exhibit"]
  about: "imagination and creativity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates develop imaginative insight and creativity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.11.b10
  locator: { number: "1.11.b10", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 16061, end: 16148 }
  source: "show awareness of academic integrity and the ethical responsibilities of the researcher"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["show"]
  about: "academic integrity and research ethics"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates develop awareness of academic integrity and of the ethical duties of anyone doing research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.11.b11
  locator: { number: "1.11.b11", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 16151, end: 16186 }
  source: "demonstrate digital literacy skills"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "digital literacy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates develop digital literacy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.11.b12
  locator: { number: "1.11.b12", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Purposes and characteristics of a Languages, Cultures and Societies degree"] }
  span: { start: 16189, end: 16293 }
  source: "appreciate and engage in contemporary debates relating to global sustainability and global perspectives."
  stem: "1.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["appreciate", "engage"]
  about: "global sustainability debates"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates develop an appreciation of, and take part in, current debates on global sustainability and global perspectives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.27
  locator: { number: "1.27", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Enterprise and entrepreneurship education"] }
  span: { start: 25181, end: 25868 }
  source: "1.27 All LCS students are challenged to understand and engage with languages, cultures and societies other than their own. As a result, LCS graduates are curious, open- minded, and able to recognise and mediate for their own bias. They display a range of enterprise attributes and competencies, including intellectual agility, flexibility, critical thinking, emotional literacy and digital skills. They are able to adapt to changing demands and are ready to continue their learning and professional development as they do so. They confront uncertainty, ambiguity, risk and failure which can help them build resilience and enable them to develop skills of initiative and problem-solving.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["challenged", "recognise", "mediate", "display", "adapt", "confront"]
  about: "enterprise attributes from engaging other cultures"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Because every student must engage with languages and cultures not their own, graduates will be curious and open, able to recognise and manage their own bias and will show enterprise attributes such as agility, flexibility, critical thinking, emotional literacy and digital skill; they will be able to adapt and keep learning, and facing uncertainty and failure builds resilience and initiative."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.29
  locator: { number: "1.29", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Enterprise and entrepreneurship education"] }
  span: { start: 26416, end: 26910 }
  source: "1.29 LCS students have a sophisticated understanding of language and communication in the real world (including the virtual world). They are alert to cultural and contextual factors which influence how language is used, such as the values ascribed to different registers and varieties of language. Their intercultural awareness and ability to mediate between cultures make them sensitive communicators, negotiators and influencers who are able to operate in a range of professional situations.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["have", "operate"]
  about: "sensitive communication and mediation at work"
  themes: [theme:enterprise]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students have a refined understanding of language and communication in real and virtual settings, notice the cultural and contextual factors shaping usage and through intercultural awareness and mediation will be able to work as sensitive communicators, negotiators and influencers in varied professional settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/1.31
  locator: { number: "1.31", headingPath: ["Context and purposes of a Languages, Cultures and Societies degree", "Enterprise and entrepreneurship education"] }
  span: { start: 27561, end: 28265 }
  source: "1.31 LCS graduates are culturally and digitally literate. They are able to navigate and analyse language, culture and society in the complexity of the contemporary world, which is technology-rich and hyper-connected across national, cultural and linguistic boundaries. They acquire enhanced collaborative skills, making connections and enabling encounters with people from different linguistic, cultural, social and disciplinary backgrounds to their own. They can provide effective leadership, for example by bringing their sensitivity to language use into their workplace. They are open to working productively with technology, for example by reviewing and enhancing the outputs of machine translation.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["are", "navigate", "analyse", "acquire", "provide", "reviewing", "enhancing"]
  about: "cultural and digital literacy, collaboration, machine translation"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates are culturally and digitally literate and will be able to find their way through and analyse language, culture and society in a connected, technology-heavy world; they gain collaborative skills across backgrounds, can lead by bringing sensitivity to language into work and work well with technology such as by revising machine translation output."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of a Languages, Cultures and Societies degree", "Progression"] }
  span: { start: 33332, end: 33744 }
  source: "2.9 Undergraduates studying LCS courses as part of a joint or combined degree with other subjects will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the topics covered in the other subject(s) of their degree. Additionally, they may explore the overlap between their subject areas, creating further opportunities for interdisciplinary study.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduates on joint or combined degrees"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "joint and combined honours students"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Undergraduates taking the subject within a joint or combined degree will reach the core of the specific and general skills set out, will gain others from their other subject or subjects and may explore where the subjects overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of a Languages, Cultures and Societies degree", "Monitoring and review"] }
  span: { start: 38072, end: 38384 }
  source: "2.19 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Providers will involve external reviewers in periodic review to get an outside view on changes and to make sure threshold standards are met and content suits the subject; externality is essential to UK quality assurance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/3.2
  locator: { number: "3.2", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 40137, end: 40652 }
  source: "3.2 The content described in this section is intended as a framework for use by curriculum designers, rather than as a list of topics or skills that must be covered. Given the rapidly changing nature of languages and language uses, the evidence base for additional language learning and teaching, technological developments in language learning and use, and the reasons for learning and using languages, it is essential that curriculum designers remain open to new ideas for the content and design of their courses."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "it is essential" read as must
  level: none
  appliesTo: "curriculum designers"
  addressee: provider
  verbs: ["remain"]
  about: "content as a framework; designers stay open to change"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The content section is a framework for designers, not a list that has to be covered; because languages, evidence, technology and motives for learning keep changing, designers are told it is essential to stay open to new content and design."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/3.13
  locator: { number: "3.13", headingPath: ["Content, structure and delivery", "Characteristics of the study of Languages, Cultures and Societies"] }
  span: { start: 46185, end: 46547 }
  source: "3.13 LCS courses explicitly require a measure of learner autonomy and responsibility for the development of linguistic proficiency through independent study. Guided independent study and research enable students to develop ideas beyond the classroom in a structured learning environment. They may be guided and developed alongside and beyond structured learning."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["require", "enable", "develop"]
  about: "learner autonomy in developing proficiency"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses require students to take some autonomy and responsibility for building their proficiency by studying on their own; guided self-study and research let ideas grow beyond the classroom in a structured setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56145, end: 56653 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be, and the reader should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees (QAA 2019). Annex D sets out common descriptions of the four main degree outcome classifications for undergraduate degrees with honours: 1st, 2.1, 2.2 and 3rd.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "readers judging achievement above threshold"
  addressee: provider
  verbs: ["perform", "refer"]
  about: "Annex D for achievement above threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will perform well above the threshold; providers set their own evidence for this, and readers should refer to Annex D, which sets out the four honours classes for degrees at FHEQ level 6 and its Scottish equivalent, FQHEIS level 10."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.8
  locator: { number: "4.8", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57823, end: 58386 }
  source: "4.8 The following standards do not prescribe a curriculum for degree courses in LCS. In determining learning outcomes of individual courses, greater or lesser importance may be given to the different areas of skills, knowledge and understanding described below. In some cases, the development of certain skills or aspects of knowledge and understanding may not figure in the course at all. These standards must therefore be read in conjunction with the information given in individual course documentation which makes clear the learning outcomes for that course.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "readers of the standards and course teams"
  addressee: provider
  verbs: ["prescribe", "read"]
  about: "standards read with course documentation"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The standards set no curriculum; courses may weight the skills and knowledge differently or leave some out, so the standards must be read together with each course's documentation of its outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.10.b1
  locator: { number: "4.10.b1", headingPath: ["Benchmark standards", "Standard of achievement at threshold level: Language proficiency"] }
  span: { start: 59056, end: 59138 }
  source: "understand a wide range of demanding, longer texts, and recognise implicit meaning"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["understand", "recognise"]
  about: "reading and listening to demanding long texts"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to follow a broad range of long, demanding texts and pick up what they imply as well as say, working towards or at CEFR C1."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.10.b2
  locator: { number: "4.10.b2", headingPath: ["Benchmark standards", "Standard of achievement at threshold level: Language proficiency"] }
  span: { start: 59141, end: 59233 }
  source: "express themselves fluently and spontaneously without much obvious searching for expressions"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["express"]
  about: "fluent spontaneous expression"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to speak and write fluently and spontaneously without obvious searching for words, towards or at CEFR C1."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.10.b3
  locator: { number: "4.10.b3", headingPath: ["Benchmark standards", "Standard of achievement at threshold level: Language proficiency"] }
  span: { start: 59236, end: 59320 }
  source: "use language flexibly and effectively for social, academic and professional purposes"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["use"]
  about: "flexible use across social, academic and work purposes"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to use the language flexibly and well for social, academic and professional ends."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.10.b4
  locator: { number: "4.10.b4", headingPath: ["Benchmark standards", "Standard of achievement at threshold level: Language proficiency"] }
  span: { start: 59323, end: 59472 }
  source: "produce clear, well structured, detailed text on complex subjects, showing controlled use of organisational patterns, connectors and cohesive devices"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["produce", "showing"]
  about: "clear, well-structured detailed writing"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to write clear, well-organised, detailed text on complex topics, with controlled use of structure, linking words and cohesion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.10.b5
  locator: { number: "4.10.b5", headingPath: ["Benchmark standards", "Standard of achievement at threshold level: Language proficiency"] }
  span: { start: 59475, end: 59615 }
  source: "translate complex texts on a wide range of general and specialised subjects from the target language(s), capturing nuances and implications."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["translate", "capturing"]
  about: "translating complex texts from the target language"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to translate complex texts on many general and specialist subjects out of the target language, conveying nuance and implication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.12.b1
  locator: { number: "4.12.b1", headingPath: ["Benchmark standards", "Explicit knowledge of language"] }
  span: { start: 60447, end: 60514 }
  source: "the structures, registers and varieties of the language(s) of study"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: []
  about: "structures, registers and varieties of the language"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will show some knowledge and an aware understanding of how each studied language is structured and of its registers and varieties."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.12.b2
  locator: { number: "4.12.b2", headingPath: ["Benchmark standards", "Explicit knowledge of language"] }
  span: { start: 60517, end: 60618 }
  source: "the sociolinguistic contexts in which different registers and varieties might be encountered and used"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["encountered", "used"]
  about: "sociolinguistic contexts of registers and varieties"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will show awareness, understanding and some knowledge of the social settings in which different registers and varieties are met and used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.12.b3
  locator: { number: "4.12.b3", headingPath: ["Benchmark standards", "Explicit knowledge of language"] }
  span: { start: 60621, end: 60692 }
  source: "the linguistic principles required to analyse the language(s) of study."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["required", "analyse"]
  about: "linguistic principles for analysing the language"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will show awareness, understanding and some knowledge of the linguistic principles needed to analyse the language or languages studied."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.13.b1
  locator: { number: "4.13.b1", headingPath: ["Benchmark standards", "Intercultural awareness and pluricultural competence"] }
  span: { start: 60843, end: 61032 }
  source: "one or more cultures and societies, typically enhanced by a period of residence in the country, or countries, of the language(s) of study, or by an alternative immersive learning experience"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["enhanced"]
  about: "knowledge of one or more cultures and societies"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will show knowledge and understanding of at least one culture and society, usually deepened by residence abroad or another immersive experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.13.b2
  locator: { number: "4.13.b2", headingPath: ["Benchmark standards", "Intercultural awareness and pluricultural competence"] }
  span: { start: 61035, end: 61137 }
  source: "different sociocultural and sociolinguistic perspectives and norms within other cultures and societies"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: []
  about: "sociocultural and sociolinguistic norms in other cultures"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will show awareness, understanding and knowledge of differing sociocultural and sociolinguistic perspectives and norms in other cultures and societies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.13.b3
  locator: { number: "4.13.b3", headingPath: ["Benchmark standards", "Intercultural awareness and pluricultural competence"] }
  span: { start: 61140, end: 61237 }
  source: "the similarities and dissimilarities of those cultures or societies in comparison with their own."
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: []
  about: "comparing other cultures with one's own"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will show awareness, understanding and knowledge of how those cultures and societies resemble and differ from their own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.14.b1
  locator: { number: "4.14.b1", headingPath: ["Benchmark standards", "Intercultural awareness and pluricultural competence"] }
  span: { start: 61272, end: 61418 }
  source: "deal sensitively with and show respect for cultural diversity and cultural difference through openness to a variety of perspectives and worldviews"
  stem: "4.14"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["deal", "show"]
  about: "respect for cultural diversity and difference"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to handle cultural diversity and difference with sensitivity and respect, open to varied perspectives and worldviews."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.14.b2
  locator: { number: "4.14.b2", headingPath: ["Benchmark standards", "Intercultural awareness and pluricultural competence"] }
  span: { start: 61421, end: 61605 }
  source: "describe and evaluate the viewpoints and practices of their own and other social groups, showing awareness of the implicit values on which judgments and prejudices are frequently based"
  stem: "4.14"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["describe", "evaluate", "showing"]
  about: "evaluating viewpoints and implicit values"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to describe and assess the views and practices of their own and other groups, aware of the hidden values behind judgements and prejudice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.14.b3
  locator: { number: "4.14.b3", headingPath: ["Benchmark standards", "Intercultural awareness and pluricultural competence"] }
  span: { start: 61608, end: 61734 }
  source: "identify differences in sociolinguistic and pragmatic conventions, reflect on them, and adjust their communication accordingly"
  stem: "4.14"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["identify", "reflect", "adjust"]
  about: "adapting to sociolinguistic and pragmatic conventions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to spot where sociolinguistic and pragmatic conventions differ, think about those differences and adapt their own communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.14.b4
  locator: { number: "4.14.b4", headingPath: ["Benchmark standards", "Intercultural awareness and pluricultural competence"] }
  span: { start: 61737, end: 61892 }
  source: "explain, interpret and discuss aspects of culture and cultural practices with reference to intercultural encounters, reading, film, social media, and so on"
  stem: "4.14"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["explain", "interpret", "discuss"]
  about: "discussing culture drawing on encounters and media"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to explain, interpret and discuss aspects of culture and its practices, drawing on intercultural encounters, reading, film, social media and the like."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.14.b5
  locator: { number: "4.14.b5", headingPath: ["Benchmark standards", "Intercultural awareness and pluricultural competence"] }
  span: { start: 61895, end: 61946 }
  source: "deal with ambiguity in cross-cultural communication"
  stem: "4.14"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["deal"]
  about: "handling ambiguity across cultures"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to cope with ambiguity in communication across cultures."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.14.b6
  locator: { number: "4.14.b6", headingPath: ["Benchmark standards", "Intercultural awareness and pluricultural competence"] }
  span: { start: 61949, end: 62096 }
  source: "act effectively as intercultural mediators, helping to maintain positive interaction by interpreting different perspectives and managing ambiguity."
  stem: "4.14"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["act", "helping", "interpreting", "managing"]
  about: "acting as an intercultural mediator"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to mediate effectively between cultures, keeping interaction positive by explaining differing views and handling ambiguity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.15.b1
  locator: { number: "4.15.b1", headingPath: ["Benchmark standards", "Subject-specific knowledge and skills"] }
  span: { start: 62175, end: 62428 }
  source: "demonstrate a knowledge and understanding of one or more aspects of the literatures, cultures, linguistic contexts, history, politics, geography, and social and economic structures of the societies of the country or countries of the language(s) of study"
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "knowledge of the target societies"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to show that they know and understand at least one area of the target societies, such as their literature, culture, linguistic setting, history, politics, geography or social and economic make-up."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.15.b2
  locator: { number: "4.15.b2", headingPath: ["Benchmark standards", "Subject-specific knowledge and skills"] }
  span: { start: 62431, end: 62563 }
  source: "deploy a range of critical methodologies to analyse and interpret diverse cultural materials, media forms and means of communication"
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["deploy", "analyse", "interpret"]
  about: "critical methods for cultural materials"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to use a range of critical methods to analyse and interpret varied cultural materials, media and forms of communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.15.b3
  locator: { number: "4.15.b3", headingPath: ["Benchmark standards", "Subject-specific knowledge and skills"] }
  span: { start: 62566, end: 62715 }
  source: "account for how language, image and other means of communication are exploited in particular social and cultural contexts and for particular purposes"
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["account", "exploited"]
  about: "how language and image work in context"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to explain how words, images and other modes of communication are put to use in particular social and cultural settings and for particular ends."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.15.b4
  locator: { number: "4.15.b4", headingPath: ["Benchmark standards", "Subject-specific knowledge and skills"] }
  span: { start: 62718, end: 62798 }
  source: "mediate between languages, demonstrating cultural and plurilinguistic competence"
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["mediate", "demonstrating"]
  about: "mediating between languages"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to mediate between languages, showing cultural and plurilingual competence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.15.b5
  locator: { number: "4.15.b5", headingPath: ["Benchmark standards", "Subject-specific knowledge and skills"] }
  span: { start: 62801, end: 62898 }
  source: "contribute to contemporary debates by drawing on historical, comparative and global perspectives."
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["contribute", "drawing"]
  about: "contributing to current debates"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to take part in current debates, bringing historical, comparative and global perspectives to them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.16.b1
  locator: { number: "4.16.b1", headingPath: ["Benchmark standards", "General and transferable skills"] }
  span: { start: 63063, end: 63165 }
  source: "gather, process and evaluate evidence and information from a variety of sources in different languages"
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["gather", "process", "evaluate"]
  about: "evidence from sources in several languages"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to collect, handle and assess evidence and information from varied sources in different languages."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.16.b2
  locator: { number: "4.16.b2", headingPath: ["Benchmark standards", "General and transferable skills"] }
  span: { start: 63168, end: 63307 }
  source: "make appropriate use of digital resources and information technology as a source of information, means of communication and aid to learning"
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["make"]
  about: "digital resources and information technology"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to use digital resources and information technology appropriately to find information, communicate and support learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.16.b3
  locator: { number: "4.16.b3", headingPath: ["Benchmark standards", "General and transferable skills"] }
  span: { start: 63310, end: 63373 }
  source: "identify and analyse problems and work towards their resolution"
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["identify", "analyse", "work"]
  about: "problem analysis and resolution"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to recognise and analyse problems and move towards resolving them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.16.b4
  locator: { number: "4.16.b4", headingPath: ["Benchmark standards", "General and transferable skills"] }
  span: { start: 63376, end: 63451 }
  source: "communicate information, ideas and arguments both verbally and non-verbally"
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating information and arguments"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to convey information, ideas and arguments in speech and writing and by non-verbal means."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.16.b5
  locator: { number: "4.16.b5", headingPath: ["Benchmark standards", "General and transferable skills"] }
  span: { start: 63454, end: 63595 }
  source: "conduct independent research, organise relevant information, and conceptualise ideas to formulate an appropriate written argument or response"
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["conduct", "organise", "conceptualise", "formulate"]
  about: "independent research and written argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to carry out independent research, organise relevant material and develop ideas into a fitting written argument or response."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.16.b6
  locator: { number: "4.16.b6", headingPath: ["Benchmark standards", "General and transferable skills"] }
  span: { start: 63598, end: 63728 }
  source: "present formal written material in a way which demonstrates consideration of the effective use of language, referencing and layout"
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["present", "demonstrates"]
  about: "presenting formal written work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to present formal written work with careful attention to effective language, referencing and layout."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.16.b7
  locator: { number: "4.16.b7", headingPath: ["Benchmark standards", "General and transferable skills"] }
  span: { start: 63731, end: 63813 }
  source: "demonstrate an ability to learn independently and to manage their time effectively"
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate", "learn", "manage"]
  about: "independent learning and time management"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to show that they learn independently and manage their time well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.16.b8
  locator: { number: "4.16.b8", headingPath: ["Benchmark standards", "General and transferable skills"] }
  span: { start: 63816, end: 64039 }
  source: "work as part of a team, cognitively framing collaborative tasks by deciding on aims, processes and steps, co-constructing ideas and solutions, and responding constructively to the strengths and weaknesses of other arguments"
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["work", "framing", "deciding", "responding"]
  about: "collaborative teamwork"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to work in a team, framing joint tasks by agreeing aims, processes and steps, building ideas and solutions together and answering the strong and weak points of other arguments constructively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/languages-cultures-and-societies-2023/4.16.b9
  locator: { number: "4.16.b9", headingPath: ["Benchmark standards", "General and transferable skills"] }
  span: { start: 64042, end: 64213 }
  source: "understand the principles of academic integrity and ethics and apply them to their own work, particularly in relation to the reuse of research and writing by other people."
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["understand", "apply"]
  about: "academic integrity and ethics in their own work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will be able to understand what academic integrity and ethics require and apply them to their own work, especially in reusing other people's research and writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/languages-cultures-and-societies-2023/1.10.b1
  forPractitioner: { text: "The usual graduate profile includes a high command of each studied language across all four modes (production, reception, interaction, mediation), enough to communicate with assurance and finesse.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are likely to finish this degree highly capable in your languages: confident speaking, writing, listening, reading and mediating between them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a descriptive profile of the usual graduate, carrying no modal: a typical graduate has a high command of the studied languages across all four modes. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.10, item 1. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside the threshold proficiency list (4.10.b1 to 4.10.b5), which asks less and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student asks how good their language will be by the end, or a team describes graduate attributes. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: Which of the four modes feels strongest for you now, and which needs the most work? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.10.b2
  forPractitioner: { text: "Graduates usually read communication in its context, are alert to variation in usage and its meaning and cope with uncertain or ambiguous exchanges.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are likely to become alert to how the setting shapes what people say, to notice shifts in usage and what they signal and to cope when meaning is unclear.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a descriptive profile of the usual graduate: awareness of context and variation and the ability to manage ambiguity. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.10, item 2. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.12.b2 and 4.14.b5 at threshold and qaa/fheq-2024/4.15.b4 on uncertainty and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student finds real conversations less tidy than the classroom, or staff discuss intercultural outcomes. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: When did a conversation last leave you unsure what was meant, and what did you do? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.10.b3
  forPractitioner: { text: "Graduates usually know the relevant language technologies (computer-assisted translation, processing and learning software, online corpora) and some gain competence in them.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are likely to learn about the tools that support language work, such as translation software and online corpora, and you may become skilled with some of them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a descriptive profile of the usual graduate, which itself says only some gain competence: awareness of language technologies, with competence for some. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.10, item 3. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.16.b2 at threshold and 1.31 on machine translation and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student asks whether translation tools matter for their career, or a team plans digital content. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: Which language tools have you tried, and do you trust their output? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.10.b4
  forPractitioner: { text: "The usual graduate is open-minded and able to take other people's viewpoints, valuing a plurality of perspectives.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are likely to grow more open-minded, able to see things as other people see them and to value views unlike your own.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a descriptive profile of the usual graduate: an open mindset and the capacity to take and value other perspectives. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.10, item 4. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.14.b1 at threshold and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student reflects on how study abroad or contact with another culture changed them. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: Can you name a view you understand better now than when you started? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.10.b5
  forPractitioner: { text: "Graduates usually analyse and interpret critically a broad span of culture: community to national, high to popular, material and digital and the habits of daily life.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are likely to be able to appreciate and critically interpret many kinds of culture, from literature and film to everyday habits, local traditions and digital media.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a descriptive profile of the usual graduate: critical interpretation of a wide range of cultural forms and practices. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.10, item 5. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.15.b2 at threshold and qaa/fheq-2024/4.15.b7 and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student asks what the culture side of the degree builds, or a team maps cultural modules. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: Which cultural form do you find easiest to analyse, and which least? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.10.b6
  forPractitioner: { text: "Graduates usually work with ideas and events that cross borders of nation, culture or language, understanding, mediating, analysing and comparing them, for instance relations between states.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are likely to be able to explain, compare and mediate ideas and events that cross borders of country, culture or language, such as how two nations relate.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a descriptive profile of the usual graduate: understanding and comparing ideas and events that cross borders. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.10, item 6. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.15.b5 and 4.14.b6 at threshold and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student links their languages to international affairs or careers in diplomacy. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: What cross-border issue could you explain from two sides? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.10.b7
  forPractitioner: { text: "Graduates usually approach problems comparatively across languages and cultures, at transnational scale or with attention to regional and minoritised communities.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are likely to learn to approach questions by comparing languages, cultures and societies, including regional and minority ones, not only national ones.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a descriptive profile of the usual graduate: comparative work across languages and cultures, including minoritised ones. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.10, item 7. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.13.b3 at threshold and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student plans a comparative project or a team designs comparative modules. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: Which two communities could you compare, and what would the comparison show? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.10.b8
  forPractitioner: { text: "Graduates are usually equipped for international mobility by their language and intercultural skills, most of all where an international placement was part of the degree.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are likely to leave with the language and intercultural skills to live and work in other countries, especially if you spend time abroad during your studies.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a descriptive profile of the usual graduate, hedged by the issuer as likely: readiness for international mobility. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.10, item 8. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 1.18 and 3.16 on placements and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student weighs a year abroad or asks about working overseas. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: Where could you see yourself working, and what would you need to manage there? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.11.b1
  forPractitioner: { text: "Graduates develop independent working that still draws on supervision, with reflection on progress and use of feedback.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You will build the habit of working on your own while still using guidance, thinking about your progress and acting on feedback.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as part of a descriptive list of general capabilities: independent work that uses guidance and feedback, one of the capabilities shared with other SHAPE subjects. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.11, item 1. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.16.b7 at threshold and qaa/fheq-2024/4.15.b5 and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student struggles with feedback or with working alone. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: What did you change after your last piece of feedback? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.11.b2
  forPractitioner: { text: "Graduates develop effective collaboration as team members.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You will learn to be a useful, effective member of a team.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as part of a descriptive list of general capabilities: effective teamwork, one of the capabilities shared with other SHAPE subjects. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.11, item 2. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.16.b8 at threshold and qaa/fheq-2024/annex-d/transferable/r2/3rd and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student faces group work or asks what employers look for. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: What role do you usually take in a group, and does it help the team? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.11.b3
  forPractitioner: { text: "Graduates develop initiative and self-direction, including efficient management of their own time.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You will grow in taking the initiative and organising yourself, including managing your time well.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as part of a descriptive list of general capabilities: initiative, self-discipline and time management, one of the capabilities shared with other SHAPE subjects. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.11, item 3. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.16.b7 at threshold and qaa/fheq-2024/4.15.b9.1 and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student is overwhelmed by deadlines or planning a placement. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: How do you plan your week when several deadlines meet? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.11.b4
  forPractitioner: { text: "Graduates develop appropriate methods for collecting, structuring and using varied evidence, data and information.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You will learn good ways to find, organise and use evidence, data and information of many kinds.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as part of a descriptive list of general capabilities: gathering and using evidence and information, one of the capabilities shared with other SHAPE subjects. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.11, item 4. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.16.b1 at threshold and qaa/fheq-2024/annex-d/cognitive/r1/3rd and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student starts a research task or essay. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: How do you keep track of your sources and decide which to use? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.11.b5
  forPractitioner: { text: "Graduates develop analysis, a questioning disposition and problem-solving, including for open problems with no single answer.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You will become more analytical and questioning, able to work through problems, even ones with no single right answer.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as part of a descriptive list of general capabilities: analysis, questioning and problem-solving, one of the capabilities shared with other SHAPE subjects. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.11, item 5. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.16.b3 at threshold and qaa/fheq-2024/4.15.b7 and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student meets an open question with no clear answer. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: How do you decide between two reasonable answers? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.11.b6
  forPractitioner: { text: "Graduates develop conceptual understanding and skill in constructing argument.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You will get better at grasping ideas and building a case of your own.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as part of a descriptive list of general capabilities: conceptual grasp and argument, one of the capabilities shared with other SHAPE subjects. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.11, item 6. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.16.b5 at threshold and qaa/fheq-2024/4.15.b3.1 and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student plans an essay or presentation. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: What is the one claim your essay is trying to prove? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.11.b7
  forPractitioner: { text: "Graduates develop well-structured, coherent and clear communication, verbal and non-verbal.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You will learn to communicate clearly and in an organised way, in words and in other ways.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as part of a descriptive list of general capabilities: clear, coherent communication, one of the capabilities shared with other SHAPE subjects. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.11, item 7. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.16.b4 at threshold and qaa/fheq-2024/4.15.b8 and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student prepares to present or receives feedback on clarity. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: Could a listener sum up your main point after one hearing? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.11.b8
  forPractitioner: { text: "Graduates develop intellectual integrity and independence of mind, including judging the strengths and flaws in others' reasoning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You will grow in intellectual honesty and independence, and get better at seeing where other people's arguments hold up or fall down.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as part of a descriptive list of general capabilities: intellectual integrity and judging others' arguments, one of the capabilities shared with other SHAPE subjects. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.11, item 8. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.16.b8 at threshold and qaa/fheq-2024/4.15.b7 and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student reviews a peer's work or a critic's argument. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: Where is the weakest step in the argument you are reading? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.11.b9
  forPractitioner: { text: "Graduates develop imaginative insight and creative ability.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You will develop your imagination and creativity.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as part of a descriptive list of general capabilities: imaginative insight and creativity, one of the capabilities shared with other SHAPE subjects. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.11, item 9. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside qaa/fheq-2024/annex-d/cognitive/r4/3rd and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student considers creative or reflective assessment options. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: What piece of work let you be most inventive? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.11.b10
  forPractitioner: { text: "Graduates develop awareness of academic integrity and the ethical obligations of researchers.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You will understand academic honesty and the ethical duties you take on when you do research.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as part of a descriptive list of general capabilities: awareness of academic integrity and research ethics, one of the capabilities shared with other SHAPE subjects. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.11, item 10. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.16.b9 at threshold and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student asks about referencing, translation tools or research with people. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: When might using a source or tool cross the line into someone else's work? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.11.b11
  forPractitioner: { text: "Graduates develop digital literacy skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You will become confident and capable with digital tools and information.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as part of a descriptive list of general capabilities: digital literacy, one of the capabilities shared with other SHAPE subjects. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.11, item 11. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside 4.16.b2 at threshold and qaa/fheq-2024/annex-d/transferable/r1/3rd and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student asks which digital skills the degree builds. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: Which digital tools do you use for your languages, and how well? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.11.b12
  forPractitioner: { text: "Graduates develop engagement with present-day debates on global sustainability and on global viewpoints.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You will take part in current debates about sustainability and the world seen from many places.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as part of a descriptive list of general capabilities: engagement with debates on global sustainability, one of the capabilities shared with other SHAPE subjects. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.11, item 12. Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. Set it beside the sustainability theme (1.22 to 1.25) and 4.15.b5 at threshold and the shared step spine:6."
  author-agent-dialogue: "Bring this up when a student connects their languages to climate or global justice questions. Put it to a student in plain words, as a picture of what people who finish the degree often show, and to staff as the issuer's profile of the subject's graduates. Ask: Which sustainability debate looks different in the language you study? Avoid reading the issuer's list aloud or treating it as a pass condition."
- statement: qaa/languages-cultures-and-societies-2023/1.27
  forPractitioner: { text: "Engaging with other languages and cultures is the means; the expected result is graduates who will be curious, aware of their own bias, agile and critical, emotionally and digitally literate, able to adapt and keep learning and resilient after facing risk and failure.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Working with languages and cultures unlike your own will make you more curious and open, help you notice your own bias and build flexibility, critical thinking, emotional awareness and digital skill; you will be able to adapt, keep learning and bounce back from setbacks.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected graduate outcome stated with 'are able to' inside the enterprise and entrepreneurship theme: curiosity, managing one's own bias, adaptability and resilience. Hold it at honours (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.27. Do not present it as one of the threshold outcomes in section 4 or as a regulatory requirement. Set it beside 1.11.b3 and 4.14.b2, the descriptor items qaa/fheq-2024/4.15.b9.1 and 4.15.b9.2 and the QAA enterprise guidance (std:doc:qaa-enterprise-2018-guidance)."
  author-agent-dialogue: "Raise this when a student asks how a languages degree helps with work or enterprise, or a team plans employability content. Put it to a student as qualities that living between languages tends to build, and to staff as an outcome to make visible in teaching and placements. Ask: When did working in another language make you change your plan, and what did you learn? Avoid presenting these traits as a checklist a student fails if they lack one."
- statement: qaa/languages-cultures-and-societies-2023/1.29
  forPractitioner: { text: "Students build a refined grasp of real-world communication, including online, and of how culture and context shape usage; the expected result is that they will be able to act as sensitive communicators, negotiators and influencers at work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how language works in real and online settings and how culture and context shape it, and you will be able to communicate, negotiate and influence with sensitivity in many kinds of job.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome for students, stated with 'are able to' within the enterprise theme: intercultural communication, negotiation and influence at work. Hold it at honours (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.29. Do not claim it is a threshold standard or that it promises a particular career. Set it beside 4.14.b3 and 4.14.b6 at threshold and the descriptor item qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Bring this up when a student asks how their language skills translate into professional roles. Put it to a student plainly as the professional value of reading context and mediating between people, and to staff as a link between language teaching and employability. Ask: In what situation have you had to adjust how you spoke to suit the person or setting? Avoid overstating it as a guarantee of negotiating or leadership roles."
- statement: qaa/languages-cultures-and-societies-2023/1.31
  forPractitioner: { text: "The expected result is graduates who will be able to analyse language and culture in a digitally connected world, collaborate across linguistic, cultural and disciplinary lines, lead through attention to language and work productively with technology, for instance post-editing machine translation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will become culturally and digitally literate, able to make sense of language and culture in a connected world, work well with people from many backgrounds and use technology wisely, for example by checking and improving machine translations.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected graduate outcome stated with 'are able to' within the enterprise theme: cultural and digital literacy, cross-boundary collaboration and productive use of language technology, including post-editing machine translation. Hold it at honours (FHEQ level 6, FQHEIS level 10) and cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 1.31. Do not present it as a threshold standard or claim the issuer sets rules on generative AI here. Set it beside 1.10.b3, 4.16.b2 and 4.16.b8 at threshold and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise this when a student asks whether translation technology makes their skills redundant, or staff plan digital and teamwork content. Put it to a student as the value of judging and improving what machines produce, and to staff as a reason to teach post-editing and collaboration explicitly. Ask: How would you check a machine translation before you relied on it? Avoid suggesting that technology use replaces developing proficiency of their own."
- statement: qaa/languages-cultures-and-societies-2023/2.9
  forPractitioner: { text: "For joint and combined honours, students will achieve the core of the subject-specific and generic skills and will add others from the partner subject; the overlap offers room for interdisciplinary work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study languages alongside another subject, you will gain the core language and general skills, add others from your second subject and may explore where the two meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation, stated with 'will', that joint and combined honours students reach the core of the subject's specific and generic skills, not every element. It holds at FHEQ level 6 and FQHEIS level 10; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 2.9. Do not claim joint honours students meet the whole threshold list in 4.10 to 4.16, nor that the issuer defines which elements are core. Set it beside 4.5 and 4.7 on the share of language study and 3.1 on content coverage."
  author-agent-dialogue: "Raise this when a joint honours student or programme team asks how much of the subject's standards apply to them. Explain to a student that they will build the core skills and add others from the second subject; to staff, that course documentation should make the core explicit. Ask: Which skills does your other subject add, and where do the two overlap? Avoid implying joint honours students fall short of single honours ones."
- statement: qaa/languages-cultures-and-societies-2023/2.19
  forPractitioner: { text: "In periodic review you will use external reviewers, both for an outside view on proposed changes and to confirm threshold standards are achieved and content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in course review; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider expectation, stated with 'will', that periodic review uses external reviewers to confirm threshold standards and subject content. It concerns review of honours provision, not a student outcome; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 2.19. Do not turn it into a learning outcome or claim it sets the review procedure. Set it beside 2.18 and 2.20 on monitoring and external examining, and the threshold lists 4.10 to 4.16 that reviewers check."
  author-agent-dialogue: "Raise this with a programme team preparing for periodic review or appointing external reviewers. Frame it for staff as what the review has to show an outsider: that threshold standards are met and content fits the subject. Ask: Which external reviewer would see your language provision with fresh eyes, and what evidence of threshold standards will you give them? Avoid putting this to a student as something they must do."
- statement: qaa/languages-cultures-and-societies-2023/3.2
  forPractitioner: { text: "Treat the content section as a framework rather than a syllabus, and keep your course content and design open to change as languages, the evidence base, technology and learners' reasons for study move on.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to curriculum designers, not a standard the student reaches", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as guidance to curriculum designers, worded as 'essential' (outside the five force words, so recorded as describes), that the content section is a framework and courses should stay open to change. It concerns honours course design; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 3.2. Do not claim the issuer lists required topics: it says the reverse, with 'must' negated. Set it beside 3.3 and 3.4 on content and 4.8 on reading the standards with course documentation."
  author-agent-dialogue: "Raise this when a programme team treats the content section as a checklist or debates adding new content such as language technology. Frame it for staff as freedom and a duty to keep content current. Ask: What has changed in how your languages are used or learned since the course was last designed? Avoid presenting it to students or as a list to tick off."
- statement: qaa/languages-cultures-and-societies-2023/3.13
  forPractitioner: { text: "Your course requires students to take a share of responsibility for their own language development through independent study, supported by guided independent study and research within a structured environment.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must take some responsibility for your own language progress through independent study; guided study and research help you develop ideas beyond the classroom.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement on students (the issuer says courses 'require' it, recorded as must): a measure of autonomy and responsibility for their own proficiency through independent study. It applies through the honours course and refines the descriptor item on managing one's own learning (qaa/fheq-2024/4.15.b5) at FHEQ level 6; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 3.13. Do not claim it sets hours or a proportion of independent study. Set it beside 1.11.b1 and 4.16.b7 at threshold and qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise this when a student relies wholly on class time or asks how to improve between lessons. Put it to a student as their own share of the work: progress in a language depends on what they do outside class. Ask: What do you do each week, outside class, to build your language, and is it enough? Avoid making it sound like the student is left without support."
- statement: qaa/languages-cultures-and-societies-2023/4.2
  forPractitioner: { text: "Expect most students to exceed the threshold; judge the higher classes by your own institutional method and refer to Annex D, which describes first, upper second, lower second and third class outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: an instruction to readers judging classification, chiefly staff", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an instruction, stated with 'should', to refer to Annex D (qaa/fheq-2024/annex-d) for achievement above the threshold, because the statement sets no typical or excellent rung. It holds for honours at FHEQ level 6 and FQHEIS level 10; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.2 (the issuer cites Annex D as QAA 2019, now within the FHEQ 2024). Do not invent typical or excellent standards for this subject. Set it beside 4.1 and the classification bands in the FHEQ document (SL6, qaa/fheq-2024/annex-d/summary/r1/3rd and the bands above it)."
  author-agent-dialogue: "Raise this when staff ask how to describe a 2.1 or first in this subject, or a student asks what a good degree looks like. Frame it for staff as the route to classification descriptions; for a student, explain that the subject sets a minimum and the classes above it are described generically. Ask: What would distinguish an upper second from a lower second in your module's tasks? Avoid presenting the threshold lists as the description of a good degree."
- statement: qaa/languages-cultures-and-societies-2023/4.8
  forPractitioner: { text: "The standards are not a curriculum: your course may weight the areas differently or omit some, so the standards must be read alongside your course documentation, which has to state its outcomes clearly.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: an instruction to readers of the standards, chiefly course teams", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement, stated with 'must', that the threshold standards are read with each course's own documentation, since courses may weight or omit areas. It governs use of the honours standards at FHEQ level 6; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.8. Do not claim every course must teach every element of 4.10 to 4.16. Set it beside 4.5, 4.7 and 4.9 on what shapes outcomes."
  author-agent-dialogue: "Raise this when a programme team maps its outcomes to the standards or an external examiner asks why an element is absent. Frame it for staff as the need for clear course documentation that explains the weighting. Ask: Where does your course documentation say which areas carry more or less weight, and why? Avoid giving this to a student as an obligation of theirs."
- statement: qaa/languages-cultures-and-societies-2023/4.10.b1
  forPractitioner: { text: "At threshold, graduates will be able to comprehend a wide variety of challenging, extended texts and grasp implicit meaning, working towards or at CEFR C1.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to understand long, challenging texts of many kinds and pick up meanings that are implied rather than stated.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: comprehension of long, demanding texts including implicit meaning, towards or at CEFR C1. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.10, item 1. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard; the issuer allows \"working towards\" C1, depending on starting point. Set it beside 4.11 for cases where C1 is out of reach and qaa/fheq-2024/4.15.b1, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student asks what level of reading or listening they need by the end. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: Can you read a long article in your language and say what it hints at as well as what it states? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.10.b2
  forPractitioner: { text: "At threshold, graduates will be able to express themselves fluently and spontaneously, rarely needing to search for words.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to express yourself fluently and on the spot, without often having to hunt for the right words.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: fluent, spontaneous expression, towards or at CEFR C1. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.10, item 2. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard; the issuer allows \"working towards\" C1, depending on starting point. Set it beside 4.10.b3, 4.16.b4 and qaa/fheq-2024/4.15.b8, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student worries about speaking without preparation. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: In an unplanned conversation, how often do you stop to search for a word? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.10.b3
  forPractitioner: { text: "At threshold, graduates will be able to deploy the language flexibly and effectively across social, academic and professional settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to use your language flexibly and well in social life, in study and at work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: flexible, effective use of the language across social, academic and professional purposes. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.10, item 3. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard; the issuer allows \"working towards\" C1, depending on starting point. Set it beside 4.10.b2 and qaa/fheq-2024/4.15.b8, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student asks whether classroom language is enough for work or study abroad. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: Which setting, social, academic or work, do you find hardest to manage in the language? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.10.b4
  forPractitioner: { text: "At threshold, graduates will be able to produce clear, detailed, well-organised text on complex topics, controlling organisation, connectors and cohesion.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to write clear, well-organised, detailed pieces on complex topics, linking your ideas smoothly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: clear, structured, detailed writing on complex subjects. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.10, item 4. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard; the issuer allows \"working towards\" C1, depending on starting point. Set it beside 4.16.b6 and qaa/fheq-2024/4.15.b8, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student gets feedback on organisation or cohesion in written work. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: How do you signal to a reader how one paragraph links to the next? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.10.b5
  forPractitioner: { text: "At threshold, graduates will be able to translate complex general and specialist texts from the target language, rendering nuance and implication.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to translate complex texts on general and specialist topics out of the language you study, keeping their nuances and implications.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: translation of complex texts from the target language, keeping nuance. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.10, item 5. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard; the issuer allows \"working towards\" C1, depending on starting point; the item names translation from, not into, the target language. Set it beside 4.15.b4 on mediation and qaa/fheq-2024/4.15.b2, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student prepares for translation assessment or asks about translation careers. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: When you translate, how do you check you have kept the tone and what is implied? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.12.b1
  forPractitioner: { text: "At threshold, graduates will show awareness and some knowledge of the structure, the registers and the varieties of each studied language.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will know about the structure of your language, its registers from formal to informal and its different varieties.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: awareness and some knowledge of the language's structures, registers and varieties. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.12, item 1. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 4.12.b2 and qaa/fheq-2024/4.15.b1, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student asks why grammar or register is taught explicitly. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: Can you explain why a sentence would sound wrong in a formal letter but fine in a chat? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.12.b2
  forPractitioner: { text: "At threshold, graduates will show awareness and some knowledge of the sociolinguistic settings where registers and varieties occur.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will understand the social settings where different registers and varieties of your language are heard and used.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: awareness and some knowledge of where registers and varieties occur socially. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.12, item 2. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 4.12.b1, 4.14.b3 and qaa/fheq-2024/4.15.b1, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student meets a dialect or register they were not taught. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: Where would you expect to hear this variety, and who uses it? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.12.b3
  forPractitioner: { text: "At threshold, graduates will show awareness and some knowledge of the linguistic principles used to analyse each studied language.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will know the basic principles of linguistics you need to analyse how your language works.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: awareness and some knowledge of the linguistic principles for analysing the language. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.12, item 3. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 4.12.b1 and qaa/fheq-2024/4.15.b2, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student asks why linguistics appears in a languages degree. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: Could you describe one pattern in your language using a linguistic term? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.13.b1
  forPractitioner: { text: "At threshold, graduates will show knowledge and understanding of one or more cultures and societies, typically deepened by residence or an alternative immersive experience.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will know and understand at least one culture and society linked to your language, usually deepened by time spent there or another immersive experience.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: knowledge of one or more cultures and societies, usually deepened by immersion. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.13, item 1. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard; residence abroad is typical, not required. Set it beside 1.21 and 3.19 on alternatives to residence abroad and qaa/fheq-2024/4.15.b1, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student cannot go abroad and asks whether that affects their degree. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: What have you learned about the culture through immersion, whether abroad or at home? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.13.b2
  forPractitioner: { text: "At threshold, graduates will show knowledge and understanding of the varied sociocultural and sociolinguistic norms and viewpoints within other societies.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will understand that other societies have their own social and language norms and that views differ within them too.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: knowledge of sociocultural and sociolinguistic norms and perspectives in other societies. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.13, item 2. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 4.14.b3 and qaa/fheq-2024/4.15.b1, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student is surprised by a social norm abroad. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: What norm surprised you, and how do people within that culture disagree about it? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.13.b3
  forPractitioner: { text: "At threshold, graduates will show understanding of the likenesses and differences between the cultures studied and their own.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to say how the cultures you study are like and unlike your own.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: knowledge of likeness and difference between studied cultures and one's own. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.13, item 3. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 1.10.b7 and 4.14.b2, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student reflects on a placement or compares cultures in an essay. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: What is one way the culture you study is closer to yours than you expected? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.14.b1
  forPractitioner: { text: "At threshold, graduates will be able to engage sensitively and respectfully with cultural diversity and difference, showing openness to other worldviews.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to treat cultural differences with sensitivity and respect, staying open to other ways of seeing the world.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: sensitive, respectful engagement with cultural diversity. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.14, item 1. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard; 4.14 continues the 4.13 threshold lead-in. Set it beside 1.10.b4 and qaa/fheq-2024/4.15.b9.1, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student finds a cultural difference uncomfortable. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: What helped you stay open when a view clashed with your own? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.14.b2
  forPractitioner: { text: "At threshold, graduates will be able to describe and judge the views and customs of their own social group and of others, aware of the implicit values beneath judgement and prejudice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to describe and assess how your own group and others think and behave, and notice the hidden values behind judgements and prejudice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: evaluating viewpoints and practices with awareness of implicit values. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.14, item 2. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 4.13.b3 and qaa/fheq-2024/4.15.b7, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student discusses stereotypes or their own assumptions. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: Which assumption of your own did study or contact with another culture make you notice? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.14.b3
  forPractitioner: { text: "At threshold, graduates will be able to identify and reflect on differing sociolinguistic and pragmatic conventions and adapt how they communicate.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to notice when the social rules of talking differ, think about them and change how you communicate to fit.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: noticing and adapting to sociolinguistic and pragmatic conventions. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.14, item 3. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 4.12.b2 and qaa/fheq-2024/4.15.b8, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student had a misunderstanding over politeness or directness. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: What did you change about how you spoke after that misunderstanding? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.14.b4
  forPractitioner: { text: "At threshold, graduates will be able to explain, interpret and discuss culture and cultural practice with reference to encounters, texts, film and social media.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to explain and discuss aspects of a culture using what you have met in person, read, watched or seen online.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: explaining and discussing culture with reference to encounters and media. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.14, item 4. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 4.15.b2 and qaa/fheq-2024/4.15.b8, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student plans a presentation or reflective piece on culture. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: Which encounter or text best shows the cultural point you want to make? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.14.b5
  forPractitioner: { text: "At threshold, graduates will be able to manage ambiguity in cross-cultural communication.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to cope when communication between cultures is unclear.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: handling ambiguity in cross-cultural communication. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.14, item 5. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 1.10.b2 and the descriptor item qaa/fheq-2024/4.15.b4, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student is unsettled by uncertain meaning in another culture. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: When meaning was unclear, how did you check or clarify it? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.14.b6
  forPractitioner: { text: "At threshold, graduates will be able to mediate effectively between cultures, sustaining positive exchange by interpreting perspectives and managing ambiguity.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to act as a go-between for people from different cultures, keeping things positive by explaining each side's view and handling uncertainty.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: effective intercultural mediation. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.14, item 6. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 4.15.b4, 1.29 and qaa/fheq-2024/4.15.b8, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student describes helping two people understand each other. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: What did you do to keep that exchange positive when the two sides misread each other? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.15.b1
  forPractitioner: { text: "At threshold, graduates will be able to demonstrate knowledge and understanding of at least one aspect of the target societies: literature, culture, language setting, history, politics, geography or social and economic structure.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to show what you know about at least one area of the places where your language is spoken: literature, culture, history, politics, geography, society or economy.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: knowledge of one or more aspects of the target-language societies. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.15, item 1. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard; one aspect suffices, not all of those listed. Set it beside 4.13.b1 and the descriptor item qaa/fheq-2024/4.15.b1, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student asks how much content knowledge the degree expects. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: Which aspect of the society you study could you explain in depth? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.15.b2
  forPractitioner: { text: "At threshold, graduates will be able to deploy several critical methods when analysing and interpreting a variety of cultural materials and media.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to use different critical approaches to analyse and interpret many kinds of cultural material and media.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: using critical methodologies on cultural materials and media. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.15, item 2. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 1.10.b5 and qaa/fheq-2024/4.15.b2, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student plans a cultural analysis or chooses a theoretical approach. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: Which critical approach would you choose for this text, and why that one? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.15.b3
  forPractitioner: { text: "At threshold, graduates will be able to account for the ways language, images and other modes are exploited in given social and cultural contexts and for given purposes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to explain how words, images and other forms of communication are used to particular effect in particular settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: accounting for how language and image are used in context and for purposes. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.15, item 3. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 4.15.b2 and qaa/fheq-2024/4.15.b7, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student analyses an advert, speech or film. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: What effect is this image or phrase trying to have, and on whom? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.15.b4
  forPractitioner: { text: "At threshold, graduates will be able to mediate between languages with cultural and plurilingual competence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to mediate between languages, showing you understand the cultures and can move between several languages.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: mediation between languages with cultural and plurilingual competence. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.15, item 4. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 4.10.b5, 4.14.b6 and qaa/fheq-2024/4.15.b8, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student prepares for interpreting or mediation tasks. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: When you mediate, what do you change besides the words? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.15.b5
  forPractitioner: { text: "At threshold, graduates will be able to contribute to present-day debates using historical, comparative and global perspectives.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to join current debates, bringing in history, comparison and a global view.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: contributing to current debates from historical, comparative and global perspectives. It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.15, item 5. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 1.11.b12 and the descriptor item qaa/fheq-2024/4.15.b3.1, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student wants to connect their study to news or public debate. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: What would a historical or comparative view add to this current debate? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.16.b1
  forPractitioner: { text: "At threshold, graduates will be able to gather, process and evaluate evidence from a range of sources across languages.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to find, work through and judge evidence and information from many sources, in more than one language.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: gathering and evaluating evidence from sources in several languages (a generic skill refining FHEQ level 6). It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.16, item 1. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 1.11.b4, qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/cognitive/r1/3rd, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student starts research using sources in the target language. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: How many of your sources are in the language you study, and how do you judge them? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.16.b2
  forPractitioner: { text: "At threshold, graduates will be able to make appropriate use of digital resources and IT for information, communication and learning.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to use digital resources and technology well to find information, communicate and help you learn.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: appropriate use of digital resources and IT (a generic skill refining FHEQ level 6). It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.16, item 2. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 1.11.b11, 1.31 and qaa/fheq-2024/annex-d/transferable/r1/3rd, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student asks which digital skills matter or how to use online tools responsibly. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: Which digital resource helps your learning most, and how do you check it is reliable? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.16.b3
  forPractitioner: { text: "At threshold, graduates will be able to identify and analyse problems and work towards solutions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to spot and analyse problems and work towards solving them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: identifying, analysing and working towards resolving problems (a generic skill refining FHEQ level 6). It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.16, item 3. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 1.11.b5, qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r3/3rd, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student is stuck on a task or a placement problem. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: What exactly is the problem, and what is one step towards solving it? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.16.b4
  forPractitioner: { text: "At threshold, graduates will be able to communicate information, ideas and arguments verbally and non-verbally.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to put across information, ideas and arguments in words and in other ways.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: communicating information, ideas and arguments (a generic skill refining FHEQ level 6). It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.16, item 4. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 1.11.b7 and the descriptor item qaa/fheq-2024/4.15.b8, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student prepares a presentation or poster. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: How will your audience know your main argument within the first minute? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.16.b5
  forPractitioner: { text: "At threshold, graduates will be able to conduct independent research, organise relevant material and conceptualise ideas into an appropriate written argument.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to research a topic on your own, organise what you find and shape your ideas into a sound written argument.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: independent research leading to a written argument (a generic skill refining FHEQ level 6). It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.16, item 5. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 1.11.b6, qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/4.15.b6, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student begins a dissertation or extended essay. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: How will you turn your notes into a single argument? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.16.b6
  forPractitioner: { text: "At threshold, graduates will be able to present formal writing that shows attention to effective language, referencing and layout.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to present formal written work that is well written, properly referenced and well laid out.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: presenting formal written work with care for language, referencing and layout (a generic skill refining FHEQ level 6). It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.16, item 6. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 4.10.b4 and qaa/fheq-2024/4.15.b8, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student receives feedback on presentation or referencing. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: What do you check before you submit a formal piece of writing? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.16.b7
  forPractitioner: { text: "At threshold, graduates will be able to demonstrate independent learning and effective time management.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to show that you can learn on your own and manage your time well.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: independent learning and time management (a generic skill refining FHEQ level 6). It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.16, item 7. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 3.13, 1.11.b3, qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/transferable/r3/3rd, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student falls behind or plans independent study. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: How do you plan your independent study time, and does the plan hold? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.16.b8
  forPractitioner: { text: "At threshold, graduates will be able to work as team members, framing shared tasks (aims, processes, steps), jointly building ideas and solutions and giving constructive responses to others' arguments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will be able to work in a team: agreeing what you are aiming for and how, building ideas together and responding fairly to the strong and weak points in others' arguments.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: collaborative teamwork that frames tasks and responds constructively (a generic skill refining FHEQ level 6). It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.16, item 8. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard. Set it beside 1.11.b2 and qaa/fheq-2024/annex-d/transferable/r2/3rd, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student is in a group project or a dispute within a group. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: How did your group agree its aims and steps, and how did you handle disagreement? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
- statement: qaa/languages-cultures-and-societies-2023/4.16.b9
  forPractitioner: { text: "At threshold, graduates will be able to understand and apply academic integrity and ethics in their own work, notably when reusing others' research and writing.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree, as a minimum, you will understand academic honesty and research ethics and apply them in your own work, especially whenever you use other people's research or writing.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: understanding and applying academic integrity and ethics (a generic skill refining FHEQ level 6). It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement, para 4.16, item 9. Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard; it does not rule on translation tools or generative AI. Set it beside 1.11.b10 and qaa/fheq-2024/4.15.b9.1, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum."
  author-agent-dialogue: "Raise this when a student asks about referencing, translation software or reusing their own work. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. Ask: If you used a translation tool or someone else's idea, how would you acknowledge it? Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.8; 4.2; 4.10" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.8; 4.2; 4.10 (as \"FHEQIS Level 10\")" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.10 (integrated master's)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.10 (integrated master's)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.8; 4.10: degree with honours at FHEQ Level 6, FQHEIS Level 10); matches the FHEQ Table 1 (std:doc:qaa-fheq-2024-framework)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.10: integrated master's); matches FHEQ 4.17 shared descriptor" }
  - { from: "fheq:6", to: "spine:6", relation: "equivalent", basis: "inferred from the reference framework R2 (std:ref:uk-framework)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "3.20"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.13", "1.19", "1.20", "1.21", "3.20"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.11", "1.22", "1.23", "1.24", "1.25"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "3.21"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-languages-cultures-and-societies-2019-benchmarks (not yet ingested)", note: "the closing page calls this the fifth edition; section 6 records the fourth (2019), third (2015) and, as Languages and Related Studies, 2007 and 2002" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree classification descriptions for FHEQ Level 6 and FQHEIS Level 10, cited as QAA 2019 (4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "levels 6 and 7 (2.8, 2.10, 4.10)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "levels 10 and 11 (2.8, 2.10, 4.2, 4.10)" }
- { rel: "refersTo", target: "std:doc:qaa-enterprise-2018-guidance", note: "QAA enterprise and entrepreneurship guidance (1.32; section 5)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "Education for Sustainable Development Guidance, in the reference list only (section 5)" }
- { rel: "refersTo", target: "CEFR, Council of Europe 2020 (not ingested; Part E)", note: "the proficiency scale for the threshold: C1, with B2 as the usual alternative (1.16, 4.3, 4.4, 4.10, 4.11)" }
- { rel: "overlaps", target: "std:doc:qaa-english-2023-benchmarks", note: "shares common ground with English (1.6); inferred" }
- { rel: "overlaps", target: "std:doc:qaa-linguistics-2023-benchmarks", note: "shares common ground with Linguistics, which covers TESOL (1.6); inferred" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance (not yet ingested)", note: "front matter" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2023-03"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "an advisory group of 22 named members drawn from universities, the Chartered Institute of Linguists and QAA, with GCHQ representatives (D1, section 6)"
replacedBy: "none"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- The subject joins communicative proficiency in one or more languages with study of their linguistics, cultures and societies from many disciplinary angles; the languages range from global to regional, indigenous and minoritised, past and present (D1, 1.7).
- Immersive learning, physical or digital, in the target language and culture is a defining feature, often a year abroad, valued for language, cultural understanding and intercultural competence (D1, 1.8, 3.16).
- It is intercultural and transnational by nature: ideas and events crossing borders, relations between countries, the effect of communities abroad on identities at home (D1, 2.5, 2.6).
- Most students learn a language they do not yet command fully, and the language of study may also be a teaching medium, a gateway to the study of culture and society (D1, 2.1, 3.11).
- It draws critical methods from the humanities and social sciences and combines readily with other SHAPE subjects and with STEM (D1, 1.11, 2.3, 2.4, 3.11).
- It sets itself against Anglophone hegemony and native-speakerism, measuring proficiency by a framework such as the CEFR (D1, 1.16, 2.7).
- Language learning is intensive, needs regular contact with proficient users and authentic material and asks for learner autonomy (D1, 3.9, 3.10, 3.13).
- Graduates go on to many sectors, from diplomacy and policy to translation, education, media and business (D1, 1.9).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "an outward-looking subject that values multilingualism, minority, sign and heritage languages, linguistic diversity beyond one standard form and rejects native-speakerism; it asks students to examine colonial and other injustices and prepares them for intolerance abroad (D1, 1.12 to 1.18)"
  statements: []
- theme: theme:accessibility
  inThisSubject: "uneven access to languages before university, so courses take beginners and heritage speakers; barriers to placements abroad (money, visas, caring, disability) met by reasonable accommodation or other immersion; alternatives to live oral assessment (D1, 1.13, 1.19 to 1.21, 3.20)"
  statements: []
- theme: theme:esd
  inThisSubject: "headed Sustainability: international perspectives on equality, peace and justice, four named UN goals (4, 5, 10, 16), climate and nature compared across cultures and the carbon cost of travel for placements (D1, 1.11, 1.22 to 1.25)"
  statements: ["qaa/languages-cultures-and-societies-2023/1.11.b12"]
- theme: theme:enterprise
  inThisSubject: "curiosity, adaptability and resilience from engaging other cultures; placements as enterprise learning; graduates as sensitive communicators, collaborators and users of language technology; employability through varied assessment (D1, 1.26 to 1.32, 3.21)"
  statements: ["qaa/languages-cultures-and-societies-2023/1.27", "qaa/languages-cultures-and-societies-2023/1.29", "qaa/languages-cultures-and-societies-2023/1.31"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.3", gloss: "proficiency, linguistic and intercultural awareness, language and society, cultures and societies of the language" }
  - { component: "3.4", gloss: "eight subject-specific skills from proficiency and mediation to comparative analysis and language technology" }
  - { component: "3.5", gloss: "receiving, producing, interacting and mediating in the language; sensitivity to difference" }
  - { component: "3.6", gloss: "creative, transactional and problem-solving communication skills" }
practices:
  - { component: "3.9", kind: "teaching", gloss: "intensive contact hours, more for beginners" }
  - { component: "3.10", kind: "learning", gloss: "contact with proficient users and authentic material" }
  - { component: "3.12", kind: "learning", gloss: "learning technology and online resources" }
  - { component: "3.13", kind: "learning", gloss: "learner autonomy and guided independent study" }
  - { component: "3.14", kind: "teaching", gloss: "methods for language skills: authentic material, explicit grammar, feedback, four skills, linguistic analysis, translation" }
  - { component: "3.15", kind: "teaching", gloss: "methods for culture and society: directed study, commentary, seminars, group work, dissertation" }
  - { component: "3.16", kind: "learning", gloss: "residence in a target-language country" }
  - { component: "3.18", kind: "learning", gloss: "what placements typically achieve" }
  - { component: "3.19", kind: "learning", gloss: "alternatives to residence abroad" }
  - { component: "3.20", kind: "assessment", gloss: "inclusive design; alternatives to live oral exams" }
  - { component: "3.22", kind: "assessment", gloss: "receptive, productive, interactive and mediation skills" }
  - { component: "3.23", kind: "assessment", gloss: "seventeen forms of proficiency assessment" }
  - { component: "3.24", kind: "assessment", gloss: "master's forms: dissertations, annotated translation, posters" }
  - { component: "3.25", kind: "assessment", gloss: "assessing in the target language" }
  - { component: "3.26", kind: "assessment", gloss: "nine forms for cultural, linguistic and social study" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.10; 4.12; 4.13 (continued by 4.14); 4.15; 4.16", award: "bachelor's with honours", items: 31 }
  - { rung: "typical", leadIn: "none", award: "bachelor's with honours", items: 0 }
  - { rung: "excellent", leadIn: "none", award: "bachelor's with honours", items: 0 }
rungBases: "4.1: the standards are the minimum a student will have shown at the honours award; 4.2: most students perform well above it, judged by each provider with Annex D. 4.5: the standards apply where languages are at least a third of study and studied in every year; 4.7: with a smaller share, not every element is expected. 4.11: where CEFR C1 is out of reach, B2 is the usual outcome."
outcomeLists:
  - { leadIn: "1.10", gloss: "profile of the typical graduate (no modal)", items: 8, award: ["bachelor's with honours"] }
  - { leadIn: "1.11", gloss: "capabilities shared with SHAPE subjects (no modal)", items: 12, award: ["bachelor's with honours"] }
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
- { body: "professional, statutory and regulatory bodies (PSRBs), none named", says: "the statement supports PSRBs with the academic standards expected and their requirements may be other reference points; no body is named in the body of the text (D1, front matter)", requirements: "not-applicable: no body named" }
- { body: "Office for Students", says: "in England these statements are not sector-recognised standards under its regulatory framework (D1, front matter)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "3.20"], statements: [] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["1.13", "1.19", "1.20", "1.21", "3.20"], statements: [] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.11", "1.22", "1.23", "1.24", "1.25"], statements: ["1.11.b12"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "3.21"], statements: ["1.27", "1.29", "1.31"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.8", "2.10", "4.2", "4.10"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.8", "2.10", "4.2", "4.10"] }
  - { framework: "other: CEFR (Council of Europe 2020), levels C1 Proficient User and B2 Independent User; no shared level id (Part E)", levels: [], citedIn: ["1.16", "4.3", "4.4", "4.10", "4.11"] }
  - { framework: "other: HSK proficiency test for Mandarin Chinese, named as an example (Part E)", levels: [], citedIn: ["4.4"] }
bodies:
  - { body: "PSRBs, unnamed", citedIn: ["front matter"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees (QAA 2019)", citedIn: ["4.2"], role: "describes the four honours classes, standing in for the typical and excellent rungs the statement does not set" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "the QAA enterprise and entrepreneurship guidance", citedIn: ["1.32", "section 5"], role: "further reading on the enterprise theme" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA and Advance HE (2021) Education for Sustainable Development Guidance", citedIn: ["section 5"], role: "reference list only" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code", citedIn: ["front matter"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "UN Sustainable Development Goals (external)", named: "the UN's sustainable development goals", citedIn: ["1.22", "1.23", "section 5"], role: "the frame of the sustainability theme; goals 4, 5, 10 and 16 named" }
  - { document: "CEFR (external; Part E)", named: "Common European Framework of Reference for Languages: Learning, Teaching, Assessment (Council of Europe 2020)", citedIn: ["1.16", "4.3", "4.10", "4.11", "section 5"], role: "the proficiency scale behind the threshold" }
  - { document: "British Academy reports (external)", named: "Born Global (2016); Towards a national languages strategy (2020); SHAPE", citedIn: ["1.9", "1.11", "section 5"], role: "evidence of the subject's value; the SHAPE grouping" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "immersive-learning", definition: "a physical placement or a digital space in which the student works mainly in the target language and culture (D1, 1.8)", beneficiaryDefinition: "time, in person or online, when you live and work mostly in the language you are learning", scopeNote: "includes the year abroad and in-country or virtual alternatives (1.21, 3.19)", category: "unknown", practices: ["education"] }
- { slug: "year-abroad", definition: "a full academic year of placement in a target-language setting (D1, 1.8)", beneficiaryDefinition: "a year spent studying or working in a country where your language is used", scopeNote: "one form of immersive placement", category: "unknown", practices: ["education"] }
- { slug: "native-speakerism", definition: "an exclusionary assumption that ties language ability to ethnicity or nationality instead of measured proficiency (D1, 1.16)", beneficiaryDefinition: "the mistaken idea that only people born into a language can be truly good at it", scopeNote: "rejected in favour of framework-based measures such as the CEFR", category: "unknown", practices: ["education"] }
- { slug: "shape-subjects", definition: "the social sciences, humanities and arts grouped as Social Sciences, Humanities and the Arts for People and the Economy (D1, 1.11)", beneficiaryDefinition: "the arts, humanities and social science subjects taken as one group", scopeNote: "the British Academy's grouping (section 5)", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the minimum a student will have shown when awarded the honours degree (D1, 4.1)", beneficiaryDefinition: "the minimum you must reach to be awarded the degree", scopeNote: "the only rung this statement sets; higher achievement is left to Annex D (4.2)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "immersive-learning", form: "immersive learning", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "year-abroad", form: "year abroad", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "informal" }
- { concept: "native-speakerism", form: "native-speakerism", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "shape-subjects", form: "SHAPE", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "minimum threshold standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Languages, Cultures and Societies"
  edition: "March 2023 (fifth edition)"
  year: 2023
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/languages-cultures-and-societies-2023/languages-cultures-and-societies-2023.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 958b10f1f2733ce2f1f11ba8b9fa7a8b9e531265e63349305b02c7ae257e30cf
  heldFiles: ["wkspc2601-library/txt/qaa-2023-languages-cultures-societies-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2023-languages-cultures-societies-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2023-languages-cultures-societies-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2023-languages-cultures-societies-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0073", citation: "Council of Europe (2020) Common European Framework of Reference for Languages: Learning, Teaching, Assessment, Companion Volume", settles: ["SB6", "S7", "S4 4.10 and 4.11 levels"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- SB4, rungs: threshold only. Five lead-ins (4.10, 4.12, 4.13, 4.15, 4.16) under one heading, "Standard of achievement at threshold level"; 4.14 ("They are also able to") continues 4.13 and is recorded as threshold with forceFrom 4.13. No typical or excellent lists: 4.2 sends readers to Annex D for the classes above. No gradeOf links.
- S4, force: threshold items take force threshold, since 4.1 defines the standards as the minimum for the honours award; lead-in wordings differ ("are able to", "demonstrate awareness, understanding and some knowledge of", "demonstrate competence in").
- S4, 4.10: the lead-in sets proficiency as "working towards or operating at level C1 of the CEFR", depending on starting point; 4.11 allows B2 as the usual outcome where C1 is not achievable (no placement, distant languages for European students, oral cultures, sign languages). 4.11 is not taken as a statement: its "typical outcome" is not the typical rung, and "expected to reach" is outside the five force words. For Abbott.
- S5: 4.10 writes "FHEQIS Level 10", the issuer's slip for FQHEIS; recorded as fqheis:10.
- S5, SB6: the CEFR (C1, B2) and HSK are proficiency scales with no shared level id; recorded by name only. Whether CEFR levels should become shared ids (for languages benchmarks and others) is for Abbott.
- S4, outcome lists in section 1: 1.10 ("Graduates of LCS degrees typically:") and 1.11 ("LCS graduates also develop ... the ability to:") have no modal in the lead-in; recorded as outcome lists, force describes. Their "typically" is a graduate profile, not the typical rung. For Abbott at P3: are these statements or descriptive components?
- S4, paragraphs with "are able to" in the enterprise section (1.27, 1.29, 1.31) taken as outcome statements, force will; 1.30 ("Where students have the opportunity ... they are able to apply") left as a component because its outcome depends on an optional study route; 1.3 (elective language students "will also ... develop some of the skills") left out as it concerns students of other subjects.
- S4, hedged "will": "will typically" and "will normally" read as descriptions, not standards: 3.1 (single honours graduates "will normally experience all of the content"), 3.3 ("will typically include"), 3.9, 3.18 (placements "will typically" do five things), 2.20 (external examiners "will be asked"); 1.25 ("will increasingly require reflection") is predictive. Not statements. 2.9 and 2.19 use plain "will" and are taken. For Abbott.
- S4, obliging words outside the five: 3.2 "it is essential that curriculum designers remain open" (taken, force describes; its "must" is negated: "rather than ... that must be covered"); 3.21 "an essential element" and 3.20 "Fundamental to the design of assessment" (descriptive, not taken); 2.8 "it is expected that each level would see ..." and "it would be expected that a student ... would be capable of ... postgraduate study" (not taken, as in Psychology 3.27). For Abbott.
- S4, 3.13: "courses explicitly require a measure of learner autonomy" recorded as must (required is must), addressed to the learner; domain generic-skill at fheq:6 though it applies through the course.
- S4, plain-present provider norms not taken (template open point 5): 2.11 (progression features), 3.4 (eight subject-specific skills that "courses develop"), 3.14, 3.15, 3.22, 3.23, 3.24, 3.26 (methods and forms of assessment), 4.5 and 4.9. 3.4 is the subject's skills list in all but form; for Abbott whether it should be an outcome list.
- S4, 1.20: the skeleton flagged "should" in "the belief that languages should be for all"; a stated value, not an obligation. Not taken.
- S4, domains: provider statements 2.19, 3.2, 4.2 and 4.8 carry domain none (no learner outcome); 2.9 carries subject-skill though it covers both specific and generic skills.
- S4, skeleton spans: 1.11.b12, 3.2, 3.13, 4.12.b3, 4.14.b6 and 4.15.b5 trimmed with find, because the skeleton ran each span into the next sub-heading.
- S3: the skeleton's cross-cutting hits sit one paragraph early in places (for example EDI at 1.11, where the heading ends 1.11's span); themes judged from the text.
- S2, subjects: the text names no HECoS or CAH codes. modern languages (100329) is entered as stated from "Modern Languages" (4.6) and translation studies (101130) from "translation and interpreting" (1.4); CAH19-04-09, CAH19-04 and CAH19 are inferred parents; Celtic studies (101118) and British Sign Language studies (100317) are inferred from the mention of Celtic languages (1.8) and sign languages (1.14, 4.11). All inferred codes held back until P3.
- S2, awards: the statement covers master's provision (1.1, 1.4, 2.2, 3.24) and names integrated master's at FHEQ 7 / FQHEIS 11 (2.10) but sets no master's standards; awardsCovered is honours only. In Scotland the honours degree is a Master of Arts (1.1), still at FQHEIS 10.
- SB5: no professional body is named in the body of the text; the Chartered Institute of Linguists and GCHQ appear only among advisory group members (section 6). The Office for Students' framework is not yet ingested.
- SB6: the ESD guidance and the UN goals and CEFR also appear in section 5, which is excluded matter; listed with "section 5" in citedIn.
- Generative AI: not named; 1.31 (reviewing machine translation output) and 3.23 (post-editing translations produced by language technology tools) touch language technology only, so no theme:generative-ai tag.
- S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are to check.
- S9: not researched in P1.
- Patterns differing from Psychology: threshold only, with no typical or excellent lists; the threshold split under five sub-headings with differing lead-in wordings and one continuation (4.14); proficiency stated against an external scale (CEFR C1, B2 fallback); the standards limited to courses with at least a third of language study (4.5); no PSRB; outcome lists in section 1 with no modal; master's provision described without standards.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:44: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0115 (P1); built by tools/bm_build.py.
