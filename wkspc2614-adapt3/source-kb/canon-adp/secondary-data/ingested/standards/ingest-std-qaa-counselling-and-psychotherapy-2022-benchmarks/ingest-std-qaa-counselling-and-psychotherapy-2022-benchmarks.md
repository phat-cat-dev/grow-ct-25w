---
id: std:doc:qaa-counselling-and-psychotherapy-2022-benchmarks
title: "Subject Benchmark Statement Counselling and Psychotherapy"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100495", label: "counselling", basis: "stated" }
  - { scheme: "hecos", code: "100254", label: "psychotherapy", basis: "stated" }
  - { scheme: "cah", code: "CAH02-06-07", label: "counselling, psychotherapy and occupational therapy", basis: "stated" }
edition: "March 2022 (second edition)"
published: 2022-03
status: current
supersedes: "the first Counselling and Psychotherapy statement (2013), named only through its advisory group list (section 6); the front matter lists the key changes"
heldText: { method: sha256-bytes, raw: 44e7c19f2b1ff0fe9f79a112c44746b22f9ac7b69983b88abfd73a49bfe7b4f0, normalised: 1ae804a483313c02bf3c0571e7fe1a043bbf196bacb0e06235c469bf8a33c46b }
heldTextStan: { method: sha256-stan, raw: 44e7c19f2b1ff0fe9f79a112c44746b22f9ac7b69983b88abfd73a49bfe7b4f0, normalised: a48c11c5e8cf826c6ced328cb9799a7f80a090fb878d1d80177d4d5ad74df75e }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2022 revision series with cross-cutting themes (published 30 March 2022)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0096 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:58"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Counselling and Psychotherapy (QAA, March 2022)

> Run 0096, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2022-counselling-psychotherapy-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in Counselling and Psychotherapy should know, be and do, for the honours degree and the master's degree. Reach for it when designing, approving, reviewing or describing a counselling or psychotherapy course, its placement, its outcomes or its assessment. Its honours standards are a threshold only, set out under Know, Be and Do across seven practice areas plus generic skills, with higher classes left to institutional marking schemes and Annex D; its master's standards add a further threshold. It favours no single modality, is not a regulatory requirement and does not replace a professional body's accreditation standards.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA on 30 March 2022 as the second edition, the statement covers bachelor's degrees with honours and master's degrees in Counselling and Psychotherapy, written to suit any core modality. It sets the subject's context and purposes (alleviating psychological distress through collaborative, reflective and reflexive practice in many settings), four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability, framed by the eight UNESCO competencies; and employability, enterprise and entrepreneurship), the distinctive features of personal development, progression, flexibility, partnership and review, a curriculum on five pillars (theory, professional skills practice, personal and professional development, research) with a mandatory assessed and supervised placement, and benchmark standards: an honours threshold in seven practice areas under Know, Be and Do plus nineteen generic skills, typical and excellent levels left to institutional marking schemes and Annex D, and a master's threshold. It notes there is no single PSRB and lists the PSA's accredited registers.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Counselling and Psychotherapy"
edition: "March 2022 (second edition)"
dates:
  published: 2022-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland and part of quality requirements in Northern Ireland (D1, Relationship to legislation and regulation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2022", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what can be expected of a graduate in Counselling and Psychotherapy, in what they know, do and understand, and the nature of awards in the subject (D1, front matter; 4.1; 4.4)"
appliesTo:
  awards: ["bachelor's degrees with honours, including joint honours (2.6, 2.7)", "master's degrees (2.8, 4.16, 4.17)"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining (2.15); PSRBs, prospective students and employers (front matter); earlier awards at Levels 4 and 5 may use it as a reference (3.1)"]
doesNot: "it favours no theoretical approach and addresses generic work rather than specific conditions; it is not a national curriculum, does not prescribe teaching, learning or assessment and carries no statutory or regulatory requirement; other related awards have their own standards (D1, front matter)"
beneficiary: the student
statedScope: "\"This Subject Benchmark Statement refers to bachelor's degrees with honours and master's degrees in Counselling and Psychotherapy.\" (D1, front matter)"
statedSubjects:
  - { name: "Counselling and Psychotherapy", locator: "(D1, title; front matter)", kind: "subject", codes: [{ scheme: "hecos", code: "100495", label: "counselling" }, { scheme: "hecos", code: "100254", label: "psychotherapy" }, { scheme: "cah", code: "CAH02-06-07", label: "counselling, psychotherapy and occupational therapy" }] }
  - { name: "gestalt, person-centred, cognitive behavioural therapy, psychodynamic, integrative", locator: "(D1, 1.8)", kind: "specialism", codes: [] }
  - { name: "Joint honours with Counselling and Psychotherapy", locator: "(D1, 2.7)", kind: "programme title", codes: [{ scheme: "hecos", code: "100495", label: "counselling" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "what counsellors and psychotherapists do" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "courses prepare reflective, reflexive practitioners" }
  - { number: "1.3", order: 5, componentType: stem, parent: "section 1", heading: "Context", gloss: "settings of client work" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "forms of service, read in context" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "modalities and modes of delivery" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "engagement with the therapeutic community; ethics; UNESCO" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes of Counselling and Psychotherapy", gloss: "purposes of training; reflective and reflexive self-awareness" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes of Counselling and Psychotherapy", gloss: "modalities, common training content, career routes, no single PSRB" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive training and diverse staff" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "experiential learning; inclusive content and assessment" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "open educators and accessible curricula" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Sustainability: Developing sustainable development knowledge", gloss: "sustainable development knowledge in the profession" }
  - { number: "1.13", order: 15, componentType: stem, parent: "section 1", heading: "Sustainability: Developing sustainable development competencies", gloss: "the eight UNESCO competencies" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Sustainability: Developing learning environments to promote sustainable development", gloss: "learning environments for sustainable development" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "growth in demand and posts" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "knowing and showing the value of skills" }
  - { number: "1.17", order: 19, componentType: stem, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "what an entrepreneurial mindset involves" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "purpose of EEEE" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "enterprise behaviours" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "enterprise attributes" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "competencies for employed or self-employed work" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "digital competency" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "employability in curriculum design" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "speakers from the profession" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "assignments that build business skills" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "initiatives with external partners" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "supervised placement as the base of professional skills" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "career pathways and confidence" }
  - { number: "2.1", order: 32, componentType: paragraph, parent: "section 2", heading: "Distinctive features of a Counselling and Psychotherapy degree", gloss: "integrated curriculum and supervised placement" }
  - { number: "2.2", order: 33, componentType: stem, parent: "section 2", heading: "Personal development", gloss: "what personal development enables" }
  - { number: "2.3", order: 34, componentType: stem, parent: "section 2", heading: "Accessibility", gloss: "equitable access, ten ways" }
  - { number: "2.4", order: 35, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "reasonable adjustments; fitness to practise" }
  - { number: "2.5", order: 36, componentType: stem, parent: "section 2", heading: "Progression", gloss: "progression: five considerations" }
  - { number: "2.6", order: 37, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "honours progression year to year" }
  - { number: "2.7", order: 38, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint honours" }
  - { number: "2.8", order: 39, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "master's degrees and exit awards" }
  - { number: "2.9", order: 40, componentType: stem, parent: "section 2", heading: "Flexibility", gloss: "flexible modes of delivery" }
  - { number: "2.10", order: 41, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "placement partnership agreements" }
  - { number: "2.11", order: 42, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "alignment with a professional body" }
  - { number: "2.12", order: 43, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership with students" }
  - { number: "2.13", order: 44, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and review by awarding bodies" }
  - { number: "2.14", order: 45, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "externality in review" }
  - { number: "2.15", order: 46, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examining" }
  - { number: "2.16", order: 47, componentType: stem, parent: "section 2", heading: "Monitoring and review", gloss: "what monitoring and review should cover" }
  - { number: "3.1", order: 49, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "where training is offered; related qualifications" }
  - { number: "3.2", order: 50, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "aim of training" }
  - { number: "3.3", order: 51, componentType: area, parent: "section 3", heading: "Content", gloss: "eleven areas of knowledge" }
  - { number: "3.4", order: 52, componentType: area, parent: "section 3", heading: "Content", gloss: "the five pillars" }
  - { number: "3.5", order: 53, componentType: area, parent: "section 3", heading: "Content: Theory", gloss: "common and modality-specific knowledge" }
  - { number: "3.6", order: 54, componentType: area, parent: "section 3", heading: "Content: Theory", gloss: "range of approaches; modality-neutral wording" }
  - { number: "3.7", order: 55, componentType: area, parent: "section 3", heading: "Content: Professional skills practice", gloss: "ten elements of skills practice" }
  - { number: "3.8", order: 56, componentType: stem, parent: "section 3", heading: "Content: Personal development", gloss: "what trainees must show in personal development" }
  - { number: "3.9", order: 57, componentType: area, parent: "section 3", heading: "Content: Professional development", gloss: "eleven elements of professional development" }
  - { number: "3.10", order: 58, componentType: area, parent: "section 3", heading: "Content: Research", gloss: "five elements of research" }
  - { number: "3.11", order: 59, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "integrated curriculum; placement required" }
  - { number: "3.12", order: 60, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "core methods of training" }
  - { number: "3.13", order: 61, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "experiential learning activities" }
  - { number: "3.14", order: 62, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "independent learners and practitioners" }
  - { number: "3.15", order: 63, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "in-person and remote training; digital core" }
  - { number: "3.16", order: 64, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "inclusive teaching by diverse trainers" }
  - { number: "3.17", order: 65, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "depth in a modality; integrative coherence" }
  - { number: "3.18", order: 66, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "teaching models; respect for other approaches" }
  - { number: "3.19", order: 67, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "research skills and a small study" }
  - { number: "3.20", order: 68, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "personal development provision" }
  - { number: "3.21", order: 69, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "placements and supervision" }
  - { number: "3.22", order: 70, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "staffing and ratios for experiential work" }
  - { number: "3.23", order: 71, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment of theory and competence" }
  - { number: "3.24", order: 72, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "typical assessment methods" }
  - { number: "3.25", order: 73, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "inclusive, authentic assessment criteria" }
  - { number: "3.26", order: 74, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "quality assurance of assessment" }
  - { number: "3.27", order: 75, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "readiness before client work" }
  - { number: "3.28", order: 76, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "placements in assessment and outcomes" }
  - { number: "4.1", order: 78, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "standards are the minimum threshold" }
  - { number: "4.2", order: 79, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most do better; Annex D" }
  - { number: "4.3", order: 80, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "a complex, changing landscape" }
  - { number: "4.4", order: 81, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "threshold at level 6 or 10; competent in all aspects" }
  - { number: "4.5", order: 82, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "standards framed as know, be and do" }
  - { number: "4.6", order: 83, componentType: stem, parent: "section 4", heading: "Threshold level (3rd class): Professional context", gloss: "threshold: professional context" }
  - { number: "4.7", order: 84, componentType: stem, parent: "section 4", heading: "Threshold level (3rd class): Understanding people and their experiences", gloss: "threshold: understanding people" }
  - { number: "4.8", order: 85, componentType: stem, parent: "section 4", heading: "Threshold level (3rd class): The therapist", gloss: "threshold: the therapist" }
  - { number: "4.9", order: 86, componentType: stem, parent: "section 4", heading: "Threshold level (3rd class): Ethical/legal", gloss: "threshold: ethical and legal" }
  - { number: "4.10", order: 87, componentType: stem, parent: "section 4", heading: "Threshold level (3rd class): Boundaries and contracting", gloss: "threshold: boundaries and contracting" }
  - { number: "4.11", order: 88, componentType: stem, parent: "section 4", heading: "Threshold level (3rd class): Assessment", gloss: "threshold: client assessment" }
  - { number: "4.12", order: 89, componentType: stem, parent: "section 4", heading: "Threshold level (3rd class): The therapeutic relationship", gloss: "threshold: the therapeutic relationship" }
  - { number: "4.13", order: 90, componentType: stem, parent: "section 4", heading: "Threshold level (3rd class): Generic skills", gloss: "threshold: nineteen generic skills" }
  - { number: "4.14", order: 91, componentType: paragraph, parent: "section 4", heading: "Typical level (2:2 or 2:1)", gloss: "typical level left to marking schemes" }
  - { number: "4.15", order: 92, componentType: paragraph, parent: "section 4", heading: "Excellent level (1st class)", gloss: "excellent level left to marking schemes" }
  - { number: "4.16", order: 93, componentType: stem, parent: "section 4", heading: "Benchmark standard for master's degrees", gloss: "master's: further critical and conceptual understanding" }
  - { number: "4.17", order: 94, componentType: stem, parent: "section 4", heading: "Benchmark standard for master's degrees", gloss: "master's: eleven further threshold statements" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Counselling and Psychotherapy degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Counselling and Psychotherapy degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and S8" }
  - { number: "none", heading: "section heading lines 1 to 4", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for SB5 and SB6 (the PSA accredited registers)" }
  - { number: "6", heading: "Membership of the Advisory Groups", kind: "other: back matter, read for S8 (the 2013 first edition)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 242 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/counselling-and-psychotherapy-2022/1.4
  locator: { number: "1.4", headingPath: ["Context and purposes of a Counselling and Psychotherapy degree", "Context"] }
  span: { start: 10378, end: 10632 }
  source: "1.4 Services may offer short or long-term therapeutic relationships in work with individuals, couples, families, groups or communities. Such settings and provision should be viewed within their historical, cultural/social, economic and political context."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses and their trainees"
  addressee: both
  verbs: ["viewed"]
  about: "therapy settings read in their wider context"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The settings where therapy happens and the services they run, from brief to long-term work with individuals, couples, families, groups or communities, should be understood against their history, culture, economics and politics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/1.5
  locator: { number: "1.5", headingPath: ["Context and purposes of a Counselling and Psychotherapy degree", "Context"] }
  span: { start: 10633, end: 11696 }
  source: "1.5 Client work is delivered through a wide range of different therapeutic modalities and practitioners acknowledge that there is no ‘one size fits all’. Practice may take place in person within a physical space or remotely within a virtual space (for example, online, text, videocall, telephone). Remote delivery can occur synchronously or asynchronously. Each of these modes of delivery carries a distinct set of working protocols, risks, challenges and benefits. These must be considered carefully to assess the most appropriate blend of methods, dependent on the client needs and suitability, the competence of the practitioner, and the nature of the therapeutic relationship. The professional title adopted by the practitioner depends largely on the training they have received, the core theoretical modality to which they adhere, their membership bodies’ protocols and the setting in which they practise. Mutual respect and appreciation for different ways of working are essential for collaborative practice across the field of mental health and well-being."
  stem: none
  statementType: expectation
  rung: none
  force: must
  level: none
  appliesTo: "Counselling and Psychotherapy courses and their trainees"
  addressee: both
  verbs: ["considered", "assess"]
  about: "choosing a mode of delivery with care"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Each way of delivering therapy, in a room or remotely, live or not, carries its own protocols, risks and benefits; these must be weighed with care to find the right mix for the client, the practitioner's competence and the relationship."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/1.7
  locator: { number: "1.7", headingPath: ["Context and purposes of a Counselling and Psychotherapy degree", "Purposes of Counselling and Psychotherapy"] }
  span: { start: 12867, end: 14808 }
  source: "1.7 Counselling and Psychotherapy educational courses train practitioners to form collaborative relationships with individuals, couples, families, groups or communities with the aim of exploring their concerns, thoughts and feelings, overcoming any obstacles, developing in awareness and acceptance and improving their mental health and well-being. Counsellors and psychotherapists are trained to draw on a body of knowledge and skills, including research evidence and their own personal and professional experiences, and use their skills and knowledge in the service of the client. The educational courses for Counselling and Psychotherapy encourage students to be both reflective and reflexive learners. Being reflective and having reflexivity are overlapping and complementary concepts. Reflective self-awareness involves the capacity to be aware of our own biases and preferences, whereas reflexive self-awareness involves considering what impact our own personal history and culture have on the way we interact with others. Counselling and Psychotherapy educational courses encourage students to be reflective in becoming aware of personal biases and preferences, including, for example, their social, political and psychological positions; and becoming reflexively self-aware in considering what impact this and their own personal history and culture has in the way they interact with others. Professional training will incorporate academic work alongside personal and skills development to support students in completing an assessed supervised placement in counselling and psychotherapy practice with clients. Such training should engender development of the UNESCO key competencies, enabling the Counselling/Psychotherapy graduate to be an independent reflective and reflexive lifelong learner committed to ongoing personal and professional development, thus enabling them to continue to enhance their practice, skills and knowledge."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Counselling and Psychotherapy courses and their trainees"
  addressee: both
  verbs: ["incorporate", "engender"]
  about: "training that joins study, growth and a supervised placement"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Training will join academic study with personal and skills development so that students can complete an assessed, supervised client placement, and it should build the UNESCO key competencies so that graduates keep learning, reflectively and reflexively, across their careers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/1.8
  locator: { number: "1.8", headingPath: ["Context and purposes of a Counselling and Psychotherapy degree", "Purposes of Counselling and Psychotherapy"] }
  span: { start: 14809, end: 16460 }
  source: "1.8 Counselling and Psychotherapy training courses will vary dependent on the therapeutic modality (such as gestalt, person-centred, cognitive behavioural therapy, psychodynamic, integrative) and mode of delivery (such as in person or remote or a combination of the two) intended as future practice for the student. However, all training will provide opportunities for engagement with the academic literature, understanding of research methods and applications, enhancement of skills relevant to working with clients, and personal and professional growth. The competent counsellor/psychotherapist graduating from this training will be able to engage in effective client work within a saf e and defined contractual relationship, while maintaining their own self-care. There are different career routes within mental health, and training in counselling/psychotherapy is not intended to direct down any career route beyond that which enables the graduating practitioner to work with clients as a counsellor or psychotherapist. There is no single professional statutory and regulatory body (PSRB) for counselling and psychotherapy, but different training providers may align to different standards which may result in formal accreditation and registration with a professional standards authority. Facilities to work collaboratively with allied professions such as medicine, health sciences, nursing, social work, education and psychology helps place counselling and psychotherapy in its wider professional, educational, social, economic and political context (providers may wish to refer to the Subject Benchmark Statements for these various professions)."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Counselling and Psychotherapy courses and their trainees"
  addressee: both
  verbs: ["provide", "engage"]
  about: "what all training offers and what the competent graduate can do"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Whatever its modality or mode, every course will give chances to engage with the literature, learn research methods, build client skills and grow personally and professionally; the competent graduate will be able to work effectively with clients in a safe, contracted relationship while caring for themselves."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of a Counselling and Psychotherapy degree", "Equality, diversity and inclusion"] }
  span: { start: 17274, end: 17721 }
  source: "1.10 Counselling and Psychotherapy courses value experiential processes alongside academic outcomes and incorporate learning experiences which allow vulnerability, openness and exploration. Course content strives to be mindful of minority experience and challenge theoretical biases located in majority cultural positioning in both theory and practice. Assessments need to be authentic, accessible and directly relevant to the work of a therapist."
  stem: none
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["value", "incorporate"]
  about: "experiential learning, inclusive content and authentic assessment"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses prize experiential learning beside academic results and make room for openness and vulnerability; content tries to keep minority experience in view and to question theory rooted in majority culture; assessment needs to be authentic, accessible and tied to the work of a therapist."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of a Counselling and Psychotherapy degree", "Sustainability: Developing sustainable development knowledge"] }
  span: { start: 18330, end: 19300 }
  source: "1.12 Counselling and psychotherapy training has as its core a view of the person within their family, social, cultural, economic and political context. Courses aim to develop sustainable development knowledge within the counselling and psychotherapy profession while placing the profession in its historical and cultural context, in terms of both origins of theory and its social and community provision. Courses invite critical review of professional infrastructures and prevailing discourses (regarding mental illness, research, recognised treatments) and their capacity to deliver public health and well-being in relation to current social, economic and political issues and limitations. This will involve a reflective and reflexive learning attitude to envision a trajectory of development for counselling and psychotherapy and its graduates that will sustain and grow holistic benefits for individuals, families, communities and the wider economic and social world."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Counselling and Psychotherapy courses and their trainees"
  addressee: both
  verbs: ["involve"]
  about: "a reflective view of the profession's sustainable future"
  themes: [theme:esd]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses seek to build knowledge of sustainable development in the profession, setting it in its history and culture and inviting critique of its structures and dominant discourses; this will call for a reflective and reflexive attitude that imagines how the profession and its graduates can keep bringing broad benefit to people and society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of a Counselling and Psychotherapy degree", "Sustainability: Developing sustainable development competencies"] }
  span: { start: 19349, end: 20004 }
  source: "1.13 All eight of the UNESCO sustainability competencies:\n• systems thinking\n• anticipatory\n• normative\n• strategic\n• collaboration\n• critical thinking\n• self -awareness\n• integrated problem-solving (UNESCO, 2017 ) are considered essential for sustainability of counselling and psychotherapy. The qualified graduate/therapist within their professional and working context requires practical operation of all the competencies in the delivery of their professional services. The learning environment for counselling and psychotherapy therefore requires these competencies to be manifested and exemplified within the learning facilities and course curricula."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "essential for" read as must
  level: none
  appliesTo: "Counselling and Psychotherapy courses and their trainees"
  addressee: both
  verbs: ["considered", "requires"]
  about: "the eight UNESCO sustainability competencies"
  themes: [theme:esd]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "All eight UNESCO competencies for sustainability (among them systems, anticipatory, normative and strategic thinking, collaboration, critical thought, self-awareness and joined-up problem-solving) are held to be essential; the qualified therapist needs to use them all in practice, so the learning setting and curriculum need to show them too."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/1.14
  locator: { number: "1.14", headingPath: ["Context and purposes of a Counselling and Psychotherapy degree", "Sustainability: Developing learning environments to promote sustainable development"] }
  span: { start: 20076, end: 20765 }
  source: "1.14 Counselling and psychotherapy training require facilities that provide both andragogic and experiential opportunities to learn, involving digital/virtual, personal/ individual, interpersonal/group and community/employer interface and practice engagement. To develop learning environments that promote sustainable development, Counselling and Psychotherapy courses aim to contextualise theoretical learning and professional provision at a practice level within the social, economic and political arena and promote the employability of their graduates. Engendering personal and social responsibility for the psychological well-being of others and themselves must be a developmental aim."
  stem: none
  statementType: expectation
  rung: none
  force: must
  level: none
  appliesTo: "Counselling and Psychotherapy courses and their trainees"
  addressee: both
  verbs: ["require", "contextualise", "promote"]
  about: "responsibility for one's own and others' well-being as a developmental aim"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Training needs facilities for adult-centred and experiential learning across digital, individual, group and community settings; courses aim to set theory and practice in their social, economic and political arena and to support employability, and fostering responsibility for one's own and others' psychological well-being must be a developmental aim."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/1.16
  locator: { number: "1.16", headingPath: ["Context and purposes of a Counselling and Psychotherapy degree", "Employability, enterprise and entrepreneurship education"] }
  span: { start: 21238, end: 21936 }
  source: "1.16 In these emerging professions, students should understand the commercial as well as practical value of their skillsets and be able to articulate and demonstrate them to potential employers and in plans for self-employment or private practice. They should also be encouraged to develop self-awareness of their own enterprising and entrepreneurial capabilities in counselling and psychotherapy, as well as the motivation and self-discipline to apply these flexibly in different ways and in changing contexts. This might include recognising themselves as being creative or resourceful; translating ideas into actions; prepared to challenge assumptions through critical investigation and research."
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["understand", "articulate", "demonstrate"]
  about: "knowing and showing the value of therapeutic skills"
  themes: [theme:enterprise]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should grasp both the commercial and the practical worth of their skills and be able to explain and show them to employers and in plans to work for themselves or set up a private practice; they should also be helped to see their own enterprising capacities and to use them flexibly as contexts change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of a Counselling and Psychotherapy degree", "Employability, enterprise and entrepreneurship education"] }
  span: { start: 24096, end: 24308 }
  source: "1.22 Developing digital competency and transferable skills should include using digital technology to communicate ideas creatively, innovatively and accessibly so as to enhance academic success and employability."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses and their trainees"
  addressee: both
  verbs: ["include", "communicate", "enhance"]
  about: "digital competency for communication and employability"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Building digital and transferable skills should include using technology to share ideas in creative, innovative and accessible ways that support study and employment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of a Counselling and Psychotherapy degree", "Employability, enterprise and entrepreneurship education"] }
  span: { start: 24309, end: 24728 }
  source: "1.23 The development of such professional knowledge, skills and competencies in counselling and psychotherapy should be a key aspect of curriculum design and might be achieved across the duration of a training programme. Learning outcomes, teaching and learning activities, and authentic assessment for employability, enterprise and entrepreneurship may be explicit within dedicated modules and embedded across modules."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["achieved", "embedded"]
  about: "employability and enterprise in curriculum design"
  themes: [theme:enterprise]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Building these professional capacities should be central to curriculum design and may run through the whole course; outcomes, activities and authentic assessment for employability and enterprise may sit in dedicated modules and across others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of a Counselling and Psychotherapy degree", "Employability, enterprise and entrepreneurship education"] }
  span: { start: 24729, end: 25141 }
  source: "1.24 The engagement of external speakers or representation from the profession and alumni to enrich teaching and offer f irst-hand experience is recommended. Exposure to a variety of therapists and agencies will develop awareness of the working context and could enhance the competencies of graduates to deal with market forces and promote themselves ethically as a counsellor or psychotherapist upon graduation."
  stem: none
  statementType: requirement
  rung: none
  force: describes
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["recommended", "develop"]
  about: "speakers from the profession and contact with agencies"
  themes: [theme:enterprise]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Bringing in speakers from the profession and alumni is advised; meeting a range of therapists and agencies builds awareness of the working world and can help graduates handle market forces and present themselves ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Distinctive features of a Counselling and Psychotherapy degree"] }
  span: { start: 27364, end: 28046 }
  source: "2.1 Counselling and Psychotherapy courses prepare candidates to be self-reflective and reflexive, ethical practitioners committed to career-long professional development and to the maintenance of professional standards. All courses of study covered by the scope of this Subject Benchmark Statement will offer an integrated curriculum of theory, professional skills practice, personal development, professional development and research. All professional Counselling and Psychotherapy courses will encompass a supervised placement enabling students to engage with clients. Detailed decisions about teaching, learning and assessment strategies are the preserve of individual providers."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["offer", "encompass"]
  about: "an integrated curriculum and a supervised placement in every course"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Every course in scope will offer a curriculum joining theory, skills practice, personal and professional development and research, and every professional course will include a supervised placement with clients; teaching and assessment strategies are for each institution to decide."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b1
  locator: { number: "2.2.b1", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 28260, end: 28296 }
  source: "take responsibility for own learning"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["take"]
  about: "owning one's learning"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Personal development should equip the learner to own their learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b2
  locator: { number: "2.2.b2", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 28299, end: 28337 }
  source: "work safely and ethically with clients"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["work"]
  about: "safe and ethical client work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should help the learner work with clients safely and ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b3
  locator: { number: "2.2.b3", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 28340, end: 28427 }
  source: "differentiate between self and client, and develop self-awareness in relation to others"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["differentiate", "develop"]
  about: "telling self from client"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should help the learner tell their own material apart from the client's and grow aware of themselves in relation to others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b4
  locator: { number: "2.2.b4", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 28430, end: 28460 }
  source: "acknowledge self as a resource"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["acknowledge"]
  about: "the self as a resource"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should help the learner see their own self as a resource in the work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b5
  locator: { number: "2.2.b5", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 28463, end: 28508 }
  source: "be self-aware of personal and social identity"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["be"]
  about: "awareness of personal and social identity"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should make the learner aware of their own personal and social identity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b6
  locator: { number: "2.2.b6", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 28511, end: 28587 }
  source: "identify and address implicit biases and prejudices within self and practice"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["identify", "address"]
  about: "hidden bias in self and practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should help the learner find and deal with hidden biases and prejudice in themselves and their practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b7
  locator: { number: "2.2.b7", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 28590, end: 28639 }
  source: "develop an accurate awareness of own competencies"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["develop"]
  about: "an accurate view of own competence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should give the learner an accurate sense of their own competence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b8
  locator: { number: "2.2.b8", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 28642, end: 28698 }
  source: "accept self, therefore enabling acceptance of the client"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["accept", "enabling"]
  about: "self-acceptance as a base for accepting clients"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should help the learner accept themselves and so accept the client."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b9
  locator: { number: "2.2.b9", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 28701, end: 28826 }
  source: "recognise the importance and foster the development of a self-care strategy to avoid burnout and promote emotional robustness"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["recognise", "foster", "avoid", "promote"]
  about: "a self-care strategy against burnout"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should help the learner see why self-care matters and build a strategy that guards against burnout and supports emotional strength."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b10
  locator: { number: "2.2.b10", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 28829, end: 28870 }
  source: "be self-organised, flexible and resilient"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["be"]
  about: "being organised, flexible and resilient"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should help the learner be organised, adaptable and resilient."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b11
  locator: { number: "2.2.b11", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 28873, end: 28954 }
  source: "commit to a lifelong process of self-awareness through reflection and reflexivity"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["commit"]
  about: "lifelong reflection and reflexivity"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should lead the learner to commit to building self-awareness through reflection and reflexivity for life."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b12
  locator: { number: "2.2.b12", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 28957, end: 29038 }
  source: "develop an awareness of self within a holistic, professional and societal context"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["develop"]
  about: "self-awareness in wider context"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should help the learner see themselves within a whole-person, professional and social context."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b13
  locator: { number: "2.2.b13", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 29041, end: 29096 }
  source: "be tolerant of uncertainty, ambiguity, risk and failure"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["be"]
  about: "tolerating uncertainty and failure"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should help the learner cope with uncertainty, ambiguity, risk and failure."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b14
  locator: { number: "2.2.b14", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 29099, end: 29194 }
  source: "be sensitive to personal values, such as ethical, social, diversity and environmental awareness"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["be"]
  about: "sensitivity to personal values"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should make the learner sensitive to values, including ethical, social, diversity and environmental ones."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.2.b15
  locator: { number: "2.2.b15", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Personal development"] }
  span: { start: 29197, end: 29373 }
  source: "develop self -awareness of their own enterprising and entrepreneurial capabilities, as well as the motivation and self-discipline to apply these flexibly in different contexts."
  stem: "2.2"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["develop", "apply"]
  about: "enterprising capabilities"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It should help the learner see their own enterprising capacities and apply them flexibly with motivation and discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.3.b1
  locator: { number: "2.3.b1", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Accessibility"] }
  span: { start: 29524, end: 29586 }
  source: "being accessible for all students both in person and digitally"
  stem: "2.3"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["being"]
  about: "access in person and online"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should be accessible to every student both in person and online."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.3.b2
  locator: { number: "2.3.b2", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Accessibility"] }
  span: { start: 29589, end: 29694 }
  source: "ensuring students have access to learning resources and technology that support their individual learning"
  stem: "2.3"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["ensuring", "support"]
  about: "resources and technology for each learner"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should make sure students can get the learning resources and technology their own learning needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.3.b3
  locator: { number: "2.3.b3", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Accessibility"] }
  span: { start: 29697, end: 29756 }
  source: "ensuring accessibility in respect of curriculum and content"
  stem: "2.3"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["ensuring"]
  about: "accessible curriculum and content"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should make the curriculum and its content accessible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.3.b4
  locator: { number: "2.3.b4", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Accessibility"] }
  span: { start: 29759, end: 29935 }
  source: "ensuring the environment is accessible to all students and fit for purpose, being an appropriate, saf e and private space for learning and practising counselling/ psychotherapy"
  stem: "2.3"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["ensuring"]
  about: "an accessible, safe and private space for practice"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should make sure the learning space is accessible, fit for purpose, safe and private enough for practising therapy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.3.b5
  locator: { number: "2.3.b5", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Accessibility"] }
  span: { start: 29938, end: 29978 }
  source: "delivering content in accessible formats"
  stem: "2.3"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["delivering"]
  about: "accessible formats"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should offer content in accessible formats."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.3.b6
  locator: { number: "2.3.b6", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Accessibility"] }
  span: { start: 29984, end: 30193 }
  source: "actively promoting equality, diversity and inclusion in relation to learning and teaching: curriculum design must be inclusive, delivery accessible and parity must be offered in terms of learning opportunities"
  stem: "2.3"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["promoting", "offered"]
  about: "inclusive design and parity of opportunity"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should actively promote equality, diversity and inclusion in teaching and learning; curriculum design must be inclusive, delivery accessible and learning opportunities equal."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.3.b7
  locator: { number: "2.3.b7", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Accessibility"] }
  span: { start: 30196, end: 30243 }
  source: "including a wide range of assessment strategies"
  stem: "2.3"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["including"]
  about: "a range of assessment strategies"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should use varied assessment strategies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.3.b8
  locator: { number: "2.3.b8", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Accessibility"] }
  span: { start: 30246, end: 30316 }
  source: "screening placements for health and safety standards and accessibility"
  stem: "2.3"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["screening"]
  about: "checking placements for safety and access"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should check placements for health and safety and for accessibility."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.3.b9
  locator: { number: "2.3.b9", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Accessibility"] }
  span: { start: 30319, end: 30387 }
  source: "remaining mindful of obstacles and barriers, such as digital poverty"
  stem: "2.3"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["remaining"]
  about: "barriers such as digital poverty"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should stay alert to barriers such as digital poverty."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.3.b10
  locator: { number: "2.3.b10", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Accessibility"] }
  span: { start: 30390, end: 30557 }
  source: "finding possible solutions for accessibility problems which may be experienced by marginalised groups, such as offering bursaries, lending laptops, and providing data."
  stem: "2.3"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["finding", "offering", "lending", "providing"]
  about: "practical help for marginalised groups"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should look for ways round access problems that marginalised groups may face, such as bursaries, loaned laptops and data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Accessibility"] }
  span: { start: 30558, end: 30850 }
  source: "2.4 Courses should consider making reasonable adjustments to ensure equitable access to learning. Counselling and Psychotherapy courses include ethical responsibilities for monitoring student fitness to practice in relation to client work and can identify actions needed to safeguard clients."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["consider", "making", "ensure"]
  about: "reasonable adjustments and fitness to practise"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should consider reasonable adjustments so that access to learning is fair; they also carry ethical duties to watch students' fitness to practise with clients and to act to protect clients."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.5.b1
  locator: { number: "2.5.b1", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Progression"] }
  span: { start: 30935, end: 31036 }
  source: "each stage of the course must be commensurate to both the appropriate academic and professional level"
  stem: "2.5"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["be"]
  about: "each stage set at the right academic and professional level"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Each stage of a course must match both the academic and the professional level it sits at."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.5.b2
  locator: { number: "2.5.b2", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Progression"] }
  span: { start: 31039, end: 31246 }
  source: "alternative non-practitioner exit awards should be offered to students who do not successf ully complete all course requirements (as ‘non-practitioner’, such exit awards would not confer practitioner status)"
  stem: "2.5"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["offered", "complete", "confer"]
  about: "non-practitioner exit awards"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Students who do not complete every requirement should be offered other exit awards that do not confer practitioner status."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.5.b3
  locator: { number: "2.5.b3", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Progression"] }
  span: { start: 31249, end: 31559 }
  source: "courses should make progression routes explicit to students, such as opportunities for higher level study and employment within the sector, and training providers should commit to ongoing working relationships with lower and higher level courses to ensure a streamlined and efficient progression where possible"
  stem: "2.5"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["make", "commit", "ensure"]
  about: "clear progression routes"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should make routes to further study and work clear to students, and work with courses at lower and higher levels to ease progression."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.5.b4
  locator: { number: "2.5.b4", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Progression"] }
  span: { start: 31562, end: 31699 }
  source: "if it is not possible to offer progression within the institution, then formalising articulation routes should be explored where possible"
  stem: "2.5"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["explored"]
  about: "articulation routes elsewhere"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Where an institution cannot offer progression itself, formal articulation routes should be explored."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.5.b5
  locator: { number: "2.5.b5", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Progression"] }
  span: { start: 31702, end: 31822 }
  source: "seamless progression routes should be in place to allow students to progress from one award or qualification to another."
  stem: "2.5"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["progress"]
  about: "seamless moves between awards"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Smooth routes should let students move from one award or qualification to the next."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Progression"] }
  span: { start: 31823, end: 32578 }
  source: "2.6 Over the course of a degree with honours (FHEQ Level 6; FQHEIS Level 10) a Counselling and Psychotherapy student will progress from one year of study to the next, in line with the regulations and processes for each institution. However, it is expected that each year would see the attainment of certain levels of knowledge, expertise and experience which builds towards the final achievement of meeting all the threshold-level subject-specific and generic skills listed in this Statement. Upon graduation from an undergraduate degree, it would be expected that a student who had achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in counselling and psychotherapy or an associated discipline."
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "students on honours courses in the subject"
  addressee: both
  verbs: ["progress", "expected"]
  about: "progress across the years towards the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours students move from year to year under their institution's rules, and each year is expected to build knowledge, expertise and experience towards meeting every threshold skill in the statement; a graduate with a second-class degree or better would be expected to be ready for postgraduate study in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Progression"] }
  span: { start: 32579, end: 32760 }
  source: "2.7 Joint honours undergraduates will achieve elements of the specific and generic skills for the subject but will add others according to the subjects covered in a joint programme."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint honours undergraduates"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "what joint honours students achieve"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students on joint honours will reach some of the subject's specific and generic skills and add others from their other subjects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.9.b1
  locator: { number: "2.9.b1", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Flexibility"] }
  span: { start: 33618, end: 33666 }
  source: "offered as full-time or part-time modes of study"
  stem: "2.9"
  statementType: requirement
  rung: none
  force: may
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["offered"]
  about: "full-time and part-time study"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses may be offered full-time or part-time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.9.b2
  locator: { number: "2.9.b2", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Flexibility"] }
  span: { start: 33669, end: 34332 }
  source: "offered with recognition of prior learning (RPL) entry points, where appropriate, allowing students to convert relevant university-level knowledge, skills and experience into credits to enable them to start the programme of study at the appropriate level. It should be noted that RPL could disadvantage those with no prior higher education experience or whose experience is dated when it comes to assessment. Support for these learners could include study skills packages and other mechanisms to aid their transition into higher-level learning. Clear information for learners on cost, timescales and what happens if module assessments are failed is also important"
  stem: "2.9"
  statementType: requirement
  rung: none
  force: may
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["offered", "allowing", "convert", "start"]
  about: "recognition of prior learning"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses may offer entry with recognition of prior learning, turning relevant experience into credit; the risk to those without recent higher education experience should be noted, with study support and clear information on costs, timescales and failed modules."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.9.b3
  locator: { number: "2.9.b3", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Flexibility"] }
  span: { start: 34335, end: 34562 }
  source: "delivered face to face or using blended or hybrid models which take adequate account of digital inclusion and sustainability; however, modes of delivery with no synchronous content are not eligible for professional recognition."
  stem: "2.9"
  statementType: requirement
  rung: none
  force: may
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["delivered", "take"]
  about: "face-to-face, blended or hybrid delivery"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses may be delivered in person or in blended or hybrid ways that attend to digital inclusion and sustainability; delivery with no live element is not eligible for professional recognition."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Partnership"] }
  span: { start: 34575, end: 34785 }
  source: "2.10 Courses work in partnership with placement providers and external stakeholders and there should be a collaborative written agreement between supervisors, course providers, placement providers and students."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["work"]
  about: "a written agreement with placement partners"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses work with placement partners and outside stakeholders, and there should be a joint written agreement between supervisors, the course, the placement and the student."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Partnership"] }
  span: { start: 34786, end: 34902 }
  source: "2.11 Courses should be written in alignment with an appropriate professional body requirement depending on modality."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["written"]
  about: "alignment with a professional body"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should be designed in line with the requirements of a suitable professional body for their modality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.16.b1
  locator: { number: "2.16.b1", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Monitoring and review"] }
  span: { start: 37427, end: 37586 }
  source: "feedback from current students, external stakeholders, such as employers and placement providers, and alumni influences curriculum design, content and delivery"
  stem: "2.16"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["influences"]
  about: "feedback from students, stakeholders and alumni"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Review should make sure that feedback from students, employers, placements and alumni shapes the curriculum."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.16.b2
  locator: { number: "2.16.b2", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Monitoring and review"] }
  span: { start: 37589, end: 37640 }
  source: "feedback from service users (Experts by Experience)"
  stem: "2.16"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: []
  about: "feedback from service users"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Review should draw on feedback from people who use services."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.16.b3
  locator: { number: "2.16.b3", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Monitoring and review"] }
  span: { start: 37643, end: 37736 }
  source: "the embedding of ESD (Education for Sustainable Development) throughout the entire curriculum"
  stem: "2.16"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: []
  about: "embedding sustainability education"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Review should check that education for sustainable development runs through the whole curriculum."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.16.b4
  locator: { number: "2.16.b4", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Monitoring and review"] }
  span: { start: 37739, end: 37768 }
  source: "internal moderation processes"
  stem: "2.16"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: []
  about: "internal moderation"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Review should include internal moderation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.16.b5
  locator: { number: "2.16.b5", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Monitoring and review"] }
  span: { start: 37771, end: 37802 }
  source: "external examiners or assessors"
  stem: "2.16"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: []
  about: "external examiners or assessors"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Review should include external examiners or assessors."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.16.b6
  locator: { number: "2.16.b6", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Monitoring and review"] }
  span: { start: 37805, end: 37835 }
  source: "institutional internal reviews"
  stem: "2.16"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: []
  about: "institutional internal review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Review should include the institution's own internal reviews."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.16.b7
  locator: { number: "2.16.b7", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Monitoring and review"] }
  span: { start: 37838, end: 37921 }
  source: "internal or external annual monitoring to align with professional body requirements"
  stem: "2.16"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["align"]
  about: "monitoring against professional body requirements"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Annual monitoring should keep the course in line with professional body requirements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.16.b8
  locator: { number: "2.16.b8", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Monitoring and review"] }
  span: { start: 37924, end: 37982 }
  source: "structured and minuted communication within teaching teams"
  stem: "2.16"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: []
  about: "minuted communication in the teaching team"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Review should rest on structured, minuted communication within the teaching team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/2.16.b9
  locator: { number: "2.16.b9", headingPath: ["Distinctive features of a Counselling and Psychotherapy degree", "Monitoring and review"] }
  span: { start: 37985, end: 38233 }
  source: "feedback from external quality assurance and enhancement exercises, including, for example, the Teaching Excellence Framework (TEF), National Student Survey (NSS), and the Postgraduate Taught and Research Student Experience Surveys (PTES and PRES)."
  stem: "2.16"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: []
  about: "national surveys and quality exercises"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Review should take account of external quality exercises and surveys such as the TEF, NSS, PTES and PRES."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 40304, end: 40531 }
  source: "3.4 Typically, courses will provide an integrated curriculum built on the five main pillars of counselling and psychotherapy:\n• theory\n• professional skills practice\n• personal development\n• professional development\n• research."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["provide"]
  about: "the five pillars of the curriculum"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses will typically offer an integrated curriculum resting on five pillars: theory, skills practice, personal growth, professional growth and research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.8.b1
  locator: { number: "3.8.b1", headingPath: ["Content, structure and delivery", "Content: Personal development"] }
  span: { start: 42628, end: 42786 }
  source: "appropriate emotional competency and emotional warmth, including the capacity to explore and resolve personal issues arising from engaging in therapeutic work"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: must
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["explore", "resolve", "engaging"]
  about: "emotional competence and warmth"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Trainees must be able to show fitting emotional competence and warmth, including working through personal issues that the work stirs up."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.8.b2
  locator: { number: "3.8.b2", headingPath: ["Content, structure and delivery", "Content: Personal development"] }
  span: { start: 42789, end: 42926 }
  source: "the ability to use personal and professional resources in a creative and flexible way, responding to the needs of a wide range of clients"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: must
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["use", "responding"]
  about: "using personal resources creatively"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Trainees must be able to use their personal and professional resources creatively and flexibly to meet a wide range of clients' needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.8.b3
  locator: { number: "3.8.b3", headingPath: ["Content, structure and delivery", "Content: Personal development"] }
  span: { start: 42929, end: 43095 }
  source: "the ability to identify personal triggers in the work with clients and address these by seeking appropriate self-care strategies, supervision, and/or personal therapy"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: must
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["identify", "address", "seeking"]
  about: "personal triggers and how to manage them"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Trainees must be able to spot their own triggers in client work and handle them through self-care, supervision or personal therapy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.8.b4
  locator: { number: "3.8.b4", headingPath: ["Content, structure and delivery", "Content: Personal development"] }
  span: { start: 43098, end: 43371 }
  source: "the awareness of the experience of being a client, which may be developed by the trainee in a variety of ways, for example through the process of live clinical supervision, group and experiential work throughout the course and may include the trainee’s own personal therapy"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: must
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["developed"]
  about: "knowing what it is to be a client"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Trainees must be able to show awareness of what being a client is like, gained through supervision, group and experiential work and possibly personal therapy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.8.b5
  locator: { number: "3.8.b5", headingPath: ["Content, structure and delivery", "Content: Personal development"] }
  span: { start: 43374, end: 43605 }
  source: "an awareness of how the trainee’s own experiences (past and present) can impact the therapeutic process and can be affected by factors such as age, family position, culture, disadvantage, gender, race, sexuality and social position"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: must
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["impact", "affected"]
  about: "how one's own history affects therapy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Trainees must be able to show awareness of how their past and present experience can affect therapy and be shaped by age, family, culture, disadvantage, gender, race, sexuality and social position."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.8.b6
  locator: { number: "3.8.b6", headingPath: ["Content, structure and delivery", "Content: Personal development"] }
  span: { start: 43608, end: 43982 }
  source: "an ability to make intrapersonal and interpersonal reflection an integral part of all clinical work to understand needs of self as differentiated from those of the client, and/or take responsibility for own learning, use of supervision and continued professional development recognising the need for, and engaging with, their own personal support and therapy, as appropriate"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: must
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["make", "understand", "take", "recognising", "engaging"]
  about: "reflection, supervision and personal support"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Trainees must be able to make reflection on themselves and the relationship central to clinical work, tell their needs from the client's, own their learning and use supervision, development and personal support or therapy as needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.8.b7
  locator: { number: "3.8.b7", headingPath: ["Content, structure and delivery", "Content: Personal development"] }
  span: { start: 43985, end: 44074 }
  source: "adopting personal responsibility and being willing to engage constructively with feedback"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: must
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["adopting", "engage"]
  about: "personal responsibility and use of feedback"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Trainees must be able to take personal responsibility and engage constructively with feedback."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.8.b8
  locator: { number: "3.8.b8", headingPath: ["Content, structure and delivery", "Content: Personal development"] }
  span: { start: 44081, end: 44124 }
  source: "recognising limitations, power and strength"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: must
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["recognising"]
  about: "knowing one's limits, power and strengths"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Trainees must be able to recognise their own limits, power and strengths."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.8.b9
  locator: { number: "3.8.b9", headingPath: ["Content, structure and delivery", "Content: Personal development"] }
  span: { start: 44127, end: 44252 }
  source: "developing and strengthening practical creativity, flexibility, self-motivation, autonomy and the ability to work proactively"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: must
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["developing", "strengthening", "work"]
  about: "creativity, autonomy and proactive working"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Trainees must be able to build practical creativity, flexibility, motivation, autonomy and a proactive way of working."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.8.b10
  locator: { number: "3.8.b10", headingPath: ["Content, structure and delivery", "Content: Personal development"] }
  span: { start: 44255, end: 44280 }
  source: "professional development."
  stem: "3.8"
  statementType: outcome
  rung: none
  force: must
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: []
  about: "professional development"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Trainees must be able to show professional development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.11
  locator: { number: "3.11", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 46360, end: 47160 }
  source: "3.11 Courses of study in Counselling and Psychotherapy prepare candidates to be self-reflective, evidence-based, ethical practitioners committed to career-long professional development. Such practitioners will recognise the significance of the individual existing within a social and cultural background, and the importance of co-created experiences in the therapy room. All courses of study covered by the scope of this Subject Benchmark Statement will offer an integrated curriculum of academic theory, research, professional\n\n15\nskills training, and personal and professional development. Courses must also incorporate an assessed and supervised counselling or psychotherapy placement. Detailed decisions about teaching, learning and assessment strategies are the preserve of individual providers."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["offer", "incorporate"]
  about: "an integrated curriculum with an assessed, supervised placement"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses prepare self-reflective, evidence-based and ethical practitioners; every course will offer an integrated curriculum of theory, research, skills training and personal and professional development, and must include an assessed and supervised placement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 47875, end: 48795 }
  source: "3.15 Courses should equip students with the skills for in-person counselling and psychotherapy practice and can include remote therapeutic practice (such as online, telephone, videocall). The delivery of training should reflect the modality in which the student may be expected to practise on placement and as a graduate. This mode of delivery may need to be flexible to meet the changing demands of the sector. Online training may be appropriate for developing skills in remote therapy, whereas in-person training may be required to refine in-person therapy skills. Blended teaching could provide a balance between these methods to develop holistic practitioners able to excel across multiple modalities. Irrespective of delivery mode, all courses should incorporate core training in the use of electronic systems for accessing data, literature, resources and the use of communication systems for enhancing interaction."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["equip", "reflect", "incorporate"]
  about: "in-person and remote skills and core digital training"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should equip students for in-person practice and can include remote practice; training should match the mode in which students will practise, and every course should include core training in electronic systems for data, literature, resources and communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.16
  locator: { number: "3.16", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 48796, end: 49514 }
  source: "3.16 Inclusive practice by a diverse range of trainers enables engagement from a diverse population of students and should be incorporated throughout all teaching and learning activities. These activities should be authentically designed to train the skills and knowledge needed to work effectively as a counsellor/psychotherapist, and the suitability of all activities should be proactively assessed to challenge any obstacles or barriers to those with different needs. Training providers should be open to exploring and addressing issues related to equality, diversity and inclusivity with the aim of raising awareness in all stakeholders, including academic and non-academic staff, students and placement providers."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["incorporated", "designed", "assessed", "exploring", "addressing"]
  about: "inclusive teaching by a diverse team"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Inclusive practice by diverse trainers should run through all teaching and learning; activities should be designed authentically for the work, checked in advance for barriers to students with different needs, and staff should be open to tackling equality, diversity and inclusion with all stakeholders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.17
  locator: { number: "3.17", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 49515, end: 50023 }
  source: "3.17 Courses typically provide in-depth experience of one or more recognised therapeutic modalities. This should involve understanding the explanations of human nature from the perspective of that modality and being aware of the cultural heritage of that approach, alongside holding an applied understanding of how to use the method in practice with clients. Where the course is integrative, the provider should be able to define the components which resource the approach and to demonstrate their coherence."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses and their trainees"
  addressee: both
  verbs: ["involve", "define", "demonstrate"]
  about: "depth in a modality, its view of people and its heritage"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses usually give depth in one or more recognised modalities; this should include understanding that modality's account of human nature and its cultural roots as well as how to use it with clients, and an integrative course should be able to name its parts and show they fit together."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.18
  locator: { number: "3.18", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 50028, end: 50767 }
  source: "3.18 There are many ways in which different established models of therapy can be taught. Creating a model that integrates diverse philosophies coherently is a complex process that needs to be accessible to students. In addition, it is essential that students develop an awareness of, and a respect for, other approaches to counselling/psychotherapy, as well as towards other recognised styles of mental health intervention. Different psychotherapeutic modalities make different demands on students and teachers/ practitioners. Providers will modify the style, emphasis and composition of the training experience in accordance with the specific needs of the modality and with reference to the requirements of the relevant professional body."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Counselling and Psychotherapy courses and their trainees"
  addressee: both
  verbs: ["modify", "develop"]
  about: "respect for other approaches and modality-specific training"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students need to develop awareness and respect for other therapeutic approaches and other mental health interventions, and course teams will adapt the style, emphasis and make-up of training to the modality and to the relevant professional body's requirements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.19
  locator: { number: "3.19", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 50768, end: 51982 }
  source: "3.19 Research is a cri tical skill for the practicing counsellor/psychotherapist. This may include opportunities for conducting formal empirical investigation and understanding published literature, alongside engaging in less formal explorations of ways of working with clients and personal research into the self for the purpose of development. The nature of research skills which are taught and assessed will vary with the type and level of the award. As a minimum, graduates require sufficient awareness to enable them to access continuing professional development opportunities and to evaluate research relevant to their area of activity. They should have an awareness of quantitative, qualitative, and mixed research methods relevant to the practice of counselling and psychotherapy. It is usual for students to undertake at least one small-scale study based on either primary or secondary enquiry. Such research will usually take the form of an empirical research project, systematic case study, or systematic review. These research studies could be completed independently or as part of a small research group, as the skills of independently led research and working in a research team are equally valuable."
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "trainees on Counselling and Psychotherapy courses"
  addressee: learner
  verbs: ["require", "access", "evaluate", "have", "undertake"]
  about: "research awareness and methods"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Research is a key skill for practitioners; at the least, graduates need enough awareness to use continuing development and to evaluate research in their field, and they should know quantitative, qualitative and mixed methods relevant to practice, usually through at least one small study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.20
  locator: { number: "3.20", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 51983, end: 52939 }
  source: "3.20 All courses will make provision for the personal development of students. Providers should make opportunities available to students to understand how the personal development and emotional competency of the counsellor/psychotherapist affects the therapeutic relationship and process. Trainees and staf f should be supported in assessing the social, cultural and family values that influence their own development, while being aware of their prejudices and biases. This may involve courses requiring trainees to have their own personal therapy but may also involve additional or alternative activities deemed to be appropriate to the course of study and therapeutic modality. All modalities should recognise the importance of personal development in training and engage in a variety of strategies for promoting such development (for example, through personal and professional development groups, reflective journals, and residential experiential work)."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["make", "supported"]
  about: "provision for personal development"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Every course will provide for students' personal development, and should create chances to understand how the therapist's growth and emotional competence affect the relationship, which may include personal therapy or other suitable activities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.21
  locator: { number: "3.21", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 52940, end: 54183 }
  source: "3.21 Training providers should support students in accessing placements appropriate to their interests and stage of development, and to liaise, as needed, with placement providers. Placements should offer opportunities for the student to practise in a manner congruent with the course philosophy. Students should be required to engage with regular supervision while working with clients on placement. Training providers should engage in the assessment and monitoring of placement providers and supervisors as suitable for trainees on placement, that supervision is of a suitable standard for that course, and decide how this will contribute to evaluating student progress. Supervision provides a significant setting for critical and reflective practice and courses should consider how they ensure that supervisors (like trainers and students) remain reflexive in relation to the lenses of privilege, power and oppression. Successful completion of a supervised counselling/psychotherapy placement is likely to be an integral part of the assessment portfolio, and this portfolio may specify a required number of hours of client work and supervision in relation to this client work (in line with professional body requirements, where applicable)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["support", "liaise", "engage"]
  about: "placements, supervision and their oversight"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Training staff should help students find placements that fit their interests and stage, check placements and supervisors, require regular supervision during client work, consider how supervisors stay reflexive about privilege, power and oppression, and decide how placement feeds into assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.22
  locator: { number: "3.22", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 54184, end: 55898 }
  source: "3.22 Courses should be delivered and managed by appropriately qualified and experienced training staff. Experiential work needs close containment and students undertaking therapeutic work (real or in role-play) need to be observed and given detailed\n\n17\nfeedback. Only small group sizes can make that possible. The very nature of the training, which involves self-disclosure and exposure to sensitive and distressing material, also lends itself to small class sizes in which there is room for everyone to have a voice. Enhanced self-awareness and self-discovery are common consequences of the reflective personal and professional development work completed on Counselling and Psychotherapy courses. This experiential process can raise issues of historical or current trauma, and this must be managed carefully by teaching staf f to provide appropriate care while maintaining boundaries. This leads to an inevitable increase in the amount of time required for pastoral and professional support to ensure the safety and well-being of the student and current/ future clients. For all the above reasons, training providers must therefore ensure that staf f:student ratios are appropriate to the learning needs of students and facilitate the development of requisite practical skills and criteria. Combined industry experience, based on that of the advisory group and consultation with the counselling and psychotherapy training community, supports that actual staff:student ratios (not FTEs) do not normally exceed an overall ratio of 1:16 for experiential classes (for example, skills practice sessions) and in all cases training providers need to have a clear rationale for the way staf f:student ratios are managed."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["delivered", "managed", "ensure"]
  about: "qualified staff and suitable staff to student ratios"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should be run by suitably qualified and experienced staff; because experiential work needs close containment, observation and care, staff to student ratios must suit students' learning needs, and the sector's experience supports ratios no higher than one to sixteen in experiential classes, with a clear rationale in all cases."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.23
  locator: { number: "3.23", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 55910, end: 56609 }
  source: "3.23 Assessment will address both theory and skills and evaluate knowledge and competencies in relation to the learning outcomes for the course. In all professional practice training courses, considerable weight will need to be given to practitioner competencies and a satisfactory level of achievement will be a prerequisite to the conferment of the award. The implication is that the candidate is ready to engage in counselling/psychotherapy practice as a fully qualified practitioner immediately after the qualification is awarded. Methods of assessment reflect the independent learning and teaching methods employed and ensure that the student's work is evaluated from a variety of perspectives."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Counselling and Psychotherapy courses and their trainees"
  addressee: both
  verbs: ["address", "evaluate"]
  about: "assessing theory and practice competence for the award"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Assessment will cover theory and skills against the course outcomes; in professional training practitioner competence will carry heavy weight and a satisfactory level will be a condition of the award, since the graduate is expected to be ready to practise at once."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.25
  locator: { number: "3.25", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 57211, end: 57866 }
  source: "3.25 Such methods could be used in a formative or summative way. Assessments can be carried out in person face-to-face or, if necessary, using appropriate digital online secure platforms. These assessments should be inclusive and authentic to the profession of counselling/psychotherapy while maintaining the academic standards appropriate to the award. Assessment criteria should evaluate core counselling skills and knowledge, alongside more general professional skills such as risk awareness, working with others,\n\n18\nacting within a professional and/or ethical framework, and making appropriate judgements by determining viable solutions to a problem."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["evaluate"]
  about: "inclusive, authentic assessment and its criteria"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment may be formative or summative, in person or on secure platforms; it should be inclusive and true to the profession while keeping academic standards, and criteria should cover core skills and knowledge and broader professional skills such as risk awareness, teamwork, ethics and judgement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.26
  locator: { number: "3.26", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 57867, end: 58258 }
  source: "3.26 Quality assurance of assessments should be given full consideration during the design, moderation and ongoing review of the processes. This should be considered in collaboration with external examiners, critical friends, reviewers, placement providers, employers and moderators as part of the effort to share best practice and disseminate effective assessment methods across the sector."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["considered"]
  about: "quality assurance of assessment"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Quality assurance of assessment should be planned into design, moderation and review, with external examiners, critical friends, placements, employers and moderators, to share good practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/3.27
  locator: { number: "3.27", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 58259, end: 58593 }
  source: "3.27 Assessment should be used formatively to assess suitability for practice on placement during the course of the programme, in addition to being used summatively to confer the final degree. Students must be assessed in terms of skills, knowledge and personal resilience before being approved to work with real clients on placement."
  stem: none
  statementType: expectation
  rung: none
  force: must
  level: none
  appliesTo: "Counselling and Psychotherapy courses and their trainees"
  addressee: both
  verbs: ["assess", "assessed", "approved"]
  about: "readiness assessed before client work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Assessment should be used formatively to judge readiness for placement and summatively for the award; students must be assessed on skills, knowledge and personal resilience before they are approved to see real clients."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 59550, end: 60033 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Counselling and Psychotherapy courses"
  addressee: provider
  verbs: ["refer"]
  about: "Annex D for achievement above the threshold"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Most students will do much better than the minimum; each institution decides what evidence shows this and should refer to Annex D, which describes the honours degree classes at FHEQ level 6 and FQHEIS level 10."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.4
  locator: { number: "4.4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60504, end: 61293 }
  source: "4.4 The following benchmark standards are set at the threshold level for graduates with honours at Level 6 in The Framework for Higher Education Qualifications in England, Wales, and Northern Ireland or Level 10 within The Framework for Qualifications of Higher Education Institutions in Scotland. With a focus on practice-facing courses, these standards represent the minimum expectations in terms of what counselling and psychotherapy students on professional courses need to know, be and do, in order to practise safely, ethically and effectively in contemporary changeable contexts. Authentic and inclusive assessment of these areas is conducted by training providers and successf ul students should be competent in all aspects of the standard before completion of their qualification."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students on practice-facing honours courses"
  addressee: learner
  verbs: ["practise", "need"]
  about: "competence in every part of the standard before completion"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The standards below are the threshold for honours at FHEQ level 6 or FQHEIS level 10, the least that students on professional courses must know, be and do to practise safely, ethically and effectively; successful students should be competent in every aspect before they complete."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 61670, end: 61890 }
  source: "Understand how philosophical assumptions influence different approaches to research and practice in counselling and psychotherapy and critically evaluate the implications for interdisciplinary professional group working."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand", "influence", "evaluate"]
  about: "philosophical assumptions behind research and practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Grasp how underlying philosophical positions shape the different approaches to counselling research and practice, and weigh critically what this means for working in teams across disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 61891, end: 62056 }
  source: "Critically evaluate and apply relevant professional codes and organisational policies for practice, including those respecting diversity and equality of opportunity."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["evaluate", "apply"]
  about: "professional codes and organisational policies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Judge critically and put into practice the professional codes and organisational policies that govern practice, including those on diversity and equal opportunity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 62057, end: 62377 }
  source: "Be aware of the various impacts and implications of government policies and recommendations, such as those in the National Institute for Health and Clinical Excellence (NICE) guidelines, for counselling and psychotherapy provision, research and the wider context of mental health service provision and client well-being."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "government policy and guidance such as NICE"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know how government policy and guidance, such as NICE guidelines, affect counselling services, research, mental health provision more widely and the well-being of clients."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 62382, end: 62564 }
  source: "Recognise and understand the ways in which power may be expressed in relationships and reflect on how power dynamics operate and impact outcomes in groups, organisations and therapy."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "understand", "reflect", "operate", "impact"]
  about: "power in relationships, groups and organisations"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "See and understand how power shows itself in relationships, and reflect on how power dynamics work in groups, organisations and therapy and what they do to outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 62568, end: 62681 }
  source: "Reflective of the role, contribution and challenges facing counselling and psychotherapy in contemporary society."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "the profession's place in society"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be reflective about what counselling and psychotherapy do in present-day society, what they add and what pressures they face."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 62682, end: 62821 }
  source: "Considerate, challenging and reflective of own values, beliefs, attitudes and behaviours and upon how these impact on the therapeutic work."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "examining one's own values and their effect on therapy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be thoughtful about, question and reflect on one's own values, beliefs, attitudes and behaviour, and on how they bear on therapeutic work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b7
  locator: { number: "4.6.b7", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 62822, end: 62992 }
  source: "Able to recognise and act with professional responsibility towards the client, employers, trainers, the counselling and psychotherapy professions and to society at large."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["recognise", "act"]
  about: "professional responsibility to all parties"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be able to see, and act on, professional responsibility to clients, employers, trainers, the professions and society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b8
  locator: { number: "4.6.b8", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 62993, end: 63219 }
  source: "Open to diversity and embrace difference in relation to the rights and responsibilities of all clients regardless of their personal characteristics or aspects of identity, including, but not limited to, those protected in law."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["embrace"]
  about: "openness to diversity and to every client's rights"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be open to diversity and welcome difference with regard to every client's rights and responsibilities, whatever their characteristics or identity, including but not only those the law protects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b9
  locator: { number: "4.6.b9", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 63223, end: 63329 }
  source: "Recognise and work within the social, cultural and political context of their practice and the profession."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "work"]
  about: "working within the social and political context"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "See and work within the social, cultural and political setting of one's own practice and of the profession."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b10
  locator: { number: "4.6.b10", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 63330, end: 63677 }
  source: "Build and sustain professional relationships as appropriate to the context and work collaboratively with supervisor and other multi-disciplinary professionals, where relevant, in order to support and evaluate therapeutic work with individuals, practice as a whole, and to contribute to service development at an organisational or systematic level."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Build", "sustain", "work", "support", "evaluate", "contribute"]
  about: "collaboration with supervisors and other professionals"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Form and keep professional relationships that suit the setting, and work with a supervisor and other professions to support and review client work, the wider practice and the growth of services."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b11
  locator: { number: "4.6.b11", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 63678, end: 63870 }
  source: "Critically appraise and evaluate published research on counselling and psychotherapy and apply a comprehensive, in-depth and research-informed body of knowledge consistently in their practice."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["appraise", "evaluate", "apply"]
  about: "using research in practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Judge published counselling research critically and use a thorough, research-based body of knowledge consistently in practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b12
  locator: { number: "4.6.b12", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 63871, end: 64043 }
  source: "Actively seek to promote equality, diversity and inclusivity in practice and challenge discrimination and prejudice on a professional, organisational, and systematic level."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["promote", "challenge"]
  about: "promoting equality and challenging discrimination"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Work actively for equality, diversity and inclusion in practice and confront discrimination and prejudice at professional, organisational and systemic levels."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b13
  locator: { number: "4.6.b13", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 64044, end: 64167 }
  source: "Develop competencies to lead a rewarding, self-determined professional life (academic, therapeutic and digital technology)."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Develop", "lead"]
  about: "competencies for a self-directed professional life"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Build the academic, therapeutic and digital competencies for a fulfilling professional life that one directs oneself."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.6.b14
  locator: { number: "4.6.b14", headingPath: ["Benchmark standards", "Threshold level (3rd class): Professional context"] }
  span: { start: 64168, end: 64249 }
  source: "Develop the ability to reasonably adapt to changing environments and uncertainty."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Develop", "adapt"]
  about: "adapting to change and uncertainty"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Grow the capacity to adjust sensibly to changing settings and to uncertainty."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Threshold level (3rd class): Understanding people and their experiences"] }
  span: { start: 64389, end: 64627 }
  source: "Understand and engage with multifaceted models of mental distress that recognise different worldviews, theoretical frameworks, and the client’s experience and viewpoint, including biomedical, psychological, social, political and cultural."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand", "engage", "recognise"]
  about: "models of mental distress"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand and work with many-sided models of mental distress that respect different worldviews and frameworks and the client's own view, across biomedical, psychological, social, political and cultural accounts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Threshold level (3rd class): Understanding people and their experiences"] }
  span: { start: 64628, end: 64787 }
  source: "Recognise potential limitations of their chosen theoretical model or models in work with specific clients and seek to mitigate such limitations where possible."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "seek", "mitigate"]
  about: "the limits of one's chosen model"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "See where one's chosen model may fall short with particular clients and try to reduce those shortfalls where possible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Threshold level (3rd class): Understanding people and their experiences"] }
  span: { start: 64788, end: 64906 }
  source: "Recognise and respect diverse perspectives, including inter-professional and multi-agency approaches to mental health."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "respect"]
  about: "other professional perspectives on mental health"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Acknowledge and respect a range of views on mental health, including those of other professions and agencies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Threshold level (3rd class): Understanding people and their experiences"] }
  span: { start: 64907, end: 65133 }
  source: "Understand and evaluate the role that mental health and counselling services play in society, and critically consider how social, political, and economic forces impact on contemporary practice in counselling and psychotherapy."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand", "evaluate", "consider", "impact"]
  about: "the social role of mental health services"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand and judge what mental health and counselling services do in society, and consider critically how social, political and economic forces affect present-day practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Threshold level (3rd class): Understanding people and their experiences"] }
  span: { start: 65134, end: 65341 }
  source: "Understand and critically evaluate the concept of relationship as expressed in a range of different theoretical approaches and consider its implications for skilful client work and interprofessional working."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand", "evaluate", "consider"]
  about: "the relationship across theoretical approaches"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand and critically weigh how different theories treat the relationship, and what follows for skilled client work and for work with other professions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.7.b6
  locator: { number: "4.7.b6", headingPath: ["Benchmark standards", "Threshold level (3rd class): Understanding people and their experiences"] }
  span: { start: 65345, end: 65573 }
  source: "Open to and appreciative of a range of theoretical approaches to practice with a view to building and maintaining collaborative, respectful and constructive relationships with colleagues and useful working alliances with clients"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["building", "maintaining"]
  about: "openness to other approaches for good working relationships"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be open to, and value, a range of approaches, so as to build and keep respectful working relationships with colleagues and good alliances with clients."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.7.b7
  locator: { number: "4.7.b7", headingPath: ["Benchmark standards", "Threshold level (3rd class): Understanding people and their experiences"] }
  span: { start: 65578, end: 65808 }
  source: "Consciously aware of one’s own bias and alert to the workings of unconscious bias in relation to social context, gender, age, ethnicity, national or ethnic origin, culture, class, ability, sexual orientation, religion and beliefs."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "awareness of one's own and unconscious bias"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be consciously aware of one's own biases and alert to unconscious bias linked to context, gender, age, ethnicity, origin, culture, class, ability, sexual orientation, religion and belief."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.7.b8
  locator: { number: "4.7.b8", headingPath: ["Benchmark standards", "Threshold level (3rd class): Understanding people and their experiences"] }
  span: { start: 65812, end: 65989 }
  source: "Draw on a range of research-informed therapeutic responses, strategies and interventions to inform practice which is sensitive to and respectful of client needs and preferences."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Draw", "inform"]
  about: "research-informed responses that respect client preference"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use a range of responses, strategies and interventions grounded in research to shape practice that is sensitive to what clients need and prefer."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.7.b9
  locator: { number: "4.7.b9", headingPath: ["Benchmark standards", "Threshold level (3rd class): Understanding people and their experiences"] }
  span: { start: 65990, end: 66268 }
  source: "Use opportunities for reflective practice, for example supervision, to recognise and demonstrate awareness of one’s own conscious bias and to monitor practice for evidence of unconscious bias, so that anti-discriminatory practice within the therapeutic relationship is achieved."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Use", "recognise", "demonstrate", "monitor"]
  about: "using supervision to check bias"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use reflective practice, such as supervision, to notice and show awareness of one's own conscious bias and to check practice for signs of unconscious bias, so that therapy is anti-discriminatory."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.7.b10
  locator: { number: "4.7.b10", headingPath: ["Benchmark standards", "Threshold level (3rd class): Understanding people and their experiences"] }
  span: { start: 66269, end: 66484 }
  source: "Develop self-awareness of own enterprising and entrepreneurial capabilities in a therapeutic context, as well as the motivation and self-discipline to apply these flexibly in different ways and in changing contexts."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Develop", "apply"]
  about: "enterprising capabilities in therapeutic work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Become aware of one's own enterprising capacities in therapeutic work, with the drive and discipline to use them flexibly as contexts change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.7.b11
  locator: { number: "4.7.b11", headingPath: ["Benchmark standards", "Threshold level (3rd class): Understanding people and their experiences"] }
  span: { start: 66485, end: 66537 }
  source: "Demonstrate initiative, autonomy and responsibility."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Demonstrate"]
  about: "initiative, autonomy and responsibility"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show initiative, independence and responsibility."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapist"] }
  span: { start: 66648, end: 66757 }
  source: "Recognise their own personal and professional strengths and limitations that may affect therapeutic practice."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "affect"]
  about: "one's own strengths and limits"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know one's personal and professional strengths and limits as they bear on practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapist"] }
  span: { start: 66758, end: 66856 }
  source: "Recognise their own self-care needs and develop appropriate self-support and self-care strategies."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "develop"]
  about: "self-care needs and strategies"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know what one needs to look after oneself and build suitable ways of supporting and caring for oneself."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapist"] }
  span: { start: 66857, end: 66915 }
  source: "Recognise when it is appropriate to make referrals onward."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "make"]
  about: "when to refer on"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know when referring a client to another service is the right step."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapist"] }
  span: { start: 66919, end: 67066 }
  source: "Able to engage with the role of supervision as an essential aspect of practice to support the therapeutic work and development of the practitioner."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["engage", "support"]
  about: "supervision as central to practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be able to use supervision as a core part of practice that supports both the client work and the practitioner's growth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapist"] }
  span: { start: 67067, end: 67222 }
  source: "Able to apply self-supervision skills to consider and challenge own values, beliefs, attitudes and behaviours and how these impact on the therapeutic work."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["apply", "consider", "challenge", "impact"]
  about: "self-supervision"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be able to supervise oneself, questioning one's values, beliefs, attitudes and behaviour and their effect on the work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.8.b6
  locator: { number: "4.8.b6", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapist"] }
  span: { start: 67226, end: 67359 }
  source: "Ensure a consistent commitment to continuing professional and personal development, including self-awareness and fitness to practice."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Ensure"]
  about: "commitment to ongoing development and fitness to practise"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Keep up a steady commitment to growing personally and professionally, self-awareness and fitness to practise included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.8.b7
  locator: { number: "4.8.b7", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapist"] }
  span: { start: 67360, end: 67458 }
  source: "Recognise the need for, and engage with, their own personal support and/or therapy as appropriate."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "engage"]
  about: "personal support or therapy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "See when one needs personal support or therapy and take it up as fitting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.8.b8
  locator: { number: "4.8.b8", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapist"] }
  span: { start: 67459, end: 67573 }
  source: "Make use of supervision to develop their understanding about practice and to enhance and protect their well-being."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Make", "develop", "enhance", "protect"]
  about: "supervision for understanding and well-being"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use supervision to deepen understanding of practice and to strengthen and safeguard one's own well-being."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b1
  locator: { number: "4.9.b1", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 67684, end: 67834 }
  source: "Understand the main ethical and legal contexts within which counselling or psychotherapy practice will happen. This means knowing about the following:"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand", "happen"]
  about: "the ethical and legal contexts of practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand the main ethical and legal settings of practice, which means knowing the points that follow."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b2
  locator: { number: "4.9.b2", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 67837, end: 68088 }
  source: "principles of law as they relate to practice, such as general data protection or child protection legislation and be conversant with regional variations, devolved arrangements and relevant international legislation as may be relevant if working online"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["relate"]
  about: "law relevant to practice, including online work"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know the legal principles that bear on practice, such as data protection and child protection, including differences across the UK nations and international law when working online."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b3
  locator: { number: "4.9.b3", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 68091, end: 68308 }
  source: "ethical frameworks or codes of practice and guidance for good practice issued by professional associations and understand professional requirements, such as those for supervision, which are set out by relevant bodies."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["understand"]
  about: "ethical frameworks and professional requirements"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know the ethical frameworks, codes and good-practice guidance of professional associations, and the professional requirements, such as for supervision, that relevant bodies set."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b4
  locator: { number: "4.9.b4", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 68311, end: 68357 }
  source: "agency policies and procedures, where relevant"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "agency policies and procedures"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know, where they apply, the policies and procedures of the agency one works in."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b5
  locator: { number: "4.9.b5", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 68360, end: 68524 }
  source: "changes in legislation, having an awareness of key sources of information to ensure ongoing practice is informed by the most recent ethical and legislative guidance"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["ensure", "informed"]
  about: "keeping up with changes in law and guidance"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know about changes in the law and where to find current information, so that practice follows the latest ethical and legal guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b6
  locator: { number: "4.9.b6", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 68531, end: 68648 }
  source: "the implications of needing to breach confidentiality, being clear about what information must be shared and to whom."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["shared"]
  about: "breaching confidentiality"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know what follows from having to break confidentiality, and be clear what must be disclosed and to whom."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b7
  locator: { number: "4.9.b7", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 68649, end: 68768 }
  source: "Understand the implications of at least one model of ethical decision-making relevant to counselling and psychotherapy."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand"]
  about: "a model of ethical decision-making"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand what follows from at least one ethical decision-making model suited to counselling and psychotherapy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b8
  locator: { number: "4.9.b8", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 68772, end: 68919 }
  source: "Committed to working ethically, aligning practice to principles of justice, integrity, trustworthiness, beneficence, non-maleficence and self-care."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["aligning"]
  about: "commitment to ethical principles"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be committed to ethical work, matching practice to justice, integrity, trustworthiness, doing good, avoiding harm and self-care."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b9
  locator: { number: "4.9.b9", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 68923, end: 69034 }
  source: "Work within a named ethical code, acting in a considered way which reflects the principles of that stated code."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Work", "reflects"]
  about: "working within a named code"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Practise under a named ethical code and act with care in line with its principles."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b10
  locator: { number: "4.9.b10", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 69035, end: 69211 }
  source: "Critically analyse, question, and consider the implications of ethical dilemmas arising in practice, work ing with a supervisor or other appropriate professionals as necessary."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["analyse", "question", "consider"]
  about: "ethical dilemmas in practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Analyse, question and think through ethical dilemmas that arise in practice, with a supervisor or other suitable professionals as needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b11
  locator: { number: "4.9.b11", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 69212, end: 69361 }
  source: "Deliver the counselling/psychotherapy services with due regard to the safety of client and therapist and the appropriateness of the practice setting."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Deliver"]
  about: "safety of client, therapist and setting"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Provide therapy with proper attention to the safety of client and therapist and to whether the setting is suitable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b12
  locator: { number: "4.9.b12", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 69362, end: 69498 }
  source: "Apply diligence in record-keeping of practice, whereby records play an essential role in the quality and safety of therapeutic practice."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Apply", "play"]
  about: "diligent record-keeping"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Keep records with diligence, since records matter for the quality and safety of therapy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b13
  locator: { number: "4.9.b13", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 69499, end: 69649 }
  source: "Manage records in accordance with legislation, statutory requirements, professional information governance standards and the lawful rights of clients."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Manage"]
  about: "records and the law"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Handle records in line with the law, statutory requirements, professional information-governance standards and clients' legal rights."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b14
  locator: { number: "4.9.b14", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 69650, end: 69872 }
  source: "Manage records appropriately, including keeping accurate records of relevant information (electronically or on paper); storing records securely; timely and purposeful sharing of information and securely destroying records."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Manage", "storing", "destroying"]
  about: "the life cycle of records"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Handle records properly across their life: accurate notes on paper or screen, secure storage, timely and purposeful sharing, and secure destruction."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b15
  locator: { number: "4.9.b15", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 69873, end: 70038 }
  source: "Manage and appropriately respond to the practical, ethical and legal demands of online therapeutic provision and all forms of technologically mediated communication."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Manage", "respond"]
  about: "demands of online and technology-mediated work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Handle and meet suitably the practical, legal and ethical demands of online therapy and of all communication through technology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b16
  locator: { number: "4.9.b16", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 70039, end: 70204 }
  source: "Work within ethical and legal constraints, contracting around matters of confidentiality and data protection related to a variety of working environments, including:"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Work"]
  about: "contracting on confidentiality and data across settings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Work within ethical and legal limits, contracting with clients on confidentiality and data protection in different working environments, including the points that follow."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b17
  locator: { number: "4.9.b17", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 70207, end: 70265 }
  source: "limits to confidentiality, including when working remotely"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["working"]
  about: "limits to confidentiality, including remotely"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Set out the limits of confidentiality, remote work included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b18
  locator: { number: "4.9.b18", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 70268, end: 70408 }
  source: "being able to inform the client of how to achieve safety in relation to data protection, platforms, equipment and their physical environment"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["inform", "achieve"]
  about: "helping clients stay safe with data and platforms"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be able to tell clients how to keep safe as to data, platforms, equipment and their physical surroundings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b19
  locator: { number: "4.9.b19", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 70411, end: 70602 }
  source: "knowledge of contemporary digital platforms, digital accessibility and technology appropriate for use in the profession and the related limitations of security in relation to working remotely"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "digital platforms, accessibility and security"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know current digital platforms, digital accessibility and suitable technology for the profession, and the limits of their security for remote work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b20
  locator: { number: "4.9.b20", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 70605, end: 70784 }
  source: "negotiating careful agreement concerning any recording of sessions by either practitioner or client and being able to communicate the implications of any such recording being made"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["negotiating", "communicate"]
  about: "agreements on recording sessions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Agree carefully on any recording of sessions by either party, and be able to explain what such recording means."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b21
  locator: { number: "4.9.b21", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 70787, end: 70915 }
  source: "discussing data security and privacy in relation to working remotely and the client’s circumstances and possible vulnerabilities"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["discussing"]
  about: "data security in remote work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Talk through data security and privacy for remote work, in light of the client's circumstances and any vulnerabilities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b22
  locator: { number: "4.9.b22", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 70918, end: 71001 }
  source: "maintaining integrity in the remote therapeutic relationship when technology fails."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["maintaining", "fails"]
  about: "when technology fails"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Keep the remote relationship intact when the technology breaks down."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.9.b23
  locator: { number: "4.9.b23", headingPath: ["Benchmark standards", "Threshold level (3rd class): Ethical/legal"] }
  span: { start: 71002, end: 71146 }
  source: "Apply intuitive decision-making and develop creative and innovative ways to address problems and ethical dilemmas with integrity and compassion."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Apply", "develop", "address"]
  about: "creative responses to dilemmas"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use intuitive judgement and find creative, new ways to deal with problems and ethical dilemmas, with integrity and compassion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b1
  locator: { number: "4.10.b1", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 71274, end: 71445 }
  source: "Understand what constitutes safe, responsive, therapeutic boundaries in all relationships, including those with:\n• clients\n• supervisors\n• tutors\n• colleagues\n• employers."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand", "constitutes"]
  about: "safe boundaries in all professional relationships"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand what makes boundaries safe, responsive and therapeutic in every relationship: with clients, supervisors, tutors, colleagues and employers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b2
  locator: { number: "4.10.b2", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 71446, end: 71582 }
  source: "Consider how to recognise boundary breaches, in order to maintain clear professional boundaries to support saf e and effective practice."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Consider", "recognise", "maintain", "support"]
  about: "recognising boundary breaches"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Think about how to spot breaches of boundaries so that clear professional limits keep practice safe and effective."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b3
  locator: { number: "4.10.b3", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 71583, end: 71729 }
  source: "The concept of contracting as part of an ethical and professional process and understand the purpose and key components of a therapeutic contract."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["understand"]
  about: "contracting and the therapeutic contract"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know contracting as part of an ethical, professional process and understand what a therapeutic contract is for and what it contains."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b4
  locator: { number: "4.10.b4", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 71730, end: 71955 }
  source: "Recognise and understand the complexities of working therapeutically with boundaries and ensure that boundaries are maintained in an appropriately responsive manner while also ensuring safety and appropriate ethical practice."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "understand", "ensure"]
  about: "responsive boundaries that keep practice safe"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Recognise and understand how complex boundary work is, keeping boundaries responsive while making sure practice stays safe and ethical."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b5
  locator: { number: "4.10.b5", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 71956, end: 72135 }
  source: "Understand the implications of employment legislation, policy and guidance in relation to therapeutic service provision within voluntary, community, statutory and private sectors."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand"]
  about: "employment law across sectors"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand what employment law, policy and guidance mean for providing therapy in voluntary, community, statutory and private settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b6
  locator: { number: "4.10.b6", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 72136, end: 72361 }
  source: "Understand the complexities and potential risks when working with sexual issues and sexual dynamics and use this understanding to ensure the saf e maintenance of appropriate boundaries and to avoid sexual boundary violations."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand", "use", "ensure", "avoid"]
  about: "sexual dynamics and boundary violations"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand the complexity and risk of sexual issues and dynamics in therapy and use this to keep boundaries safe and prevent sexual boundary violations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b7
  locator: { number: "4.10.b7", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 72365, end: 72443 }
  source: "Aware of the potential challenges which may arise within the therapeutic work."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "awareness of challenges in the work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be aware of the difficulties that may come up in therapeutic work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b8
  locator: { number: "4.10.b8", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 72444, end: 72578 }
  source: "Confident in responding therapeutically to changes and challenges in the therapeutic relationship, while maintaining clear boundaries."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["responding", "maintaining"]
  about: "confidence with change while holding boundaries"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be confident in meeting changes and difficulties in the relationship therapeutically while keeping clear boundaries."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b9
  locator: { number: "4.10.b9", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 72582, end: 72695 }
  source: "Set and maintain appropriate professional boundaries throughout the therapy process and after the end of therapy."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Set", "maintain"]
  about: "boundaries during and after therapy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Set and keep suitable professional boundaries throughout therapy and once it has ended."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b10
  locator: { number: "4.10.b10", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 72696, end: 72791 }
  source: "Work with and make therapeutic use of the constraints and benefits of the therapeutic contract."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Work", "make"]
  about: "using the therapeutic contract"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Work with the contract's limits and benefits and turn them to therapeutic use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b11
  locator: { number: "4.10.b11", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 72792, end: 72930 }
  source: "Establish and maintain appropriate professional and personal boundaries in online relationships with clients or patients by ensuring that:"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Establish", "maintain", "ensuring"]
  about: "online boundaries with clients"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Set and keep fitting personal and professional limits in online relationships with clients or patients, by making sure of the points that follow."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b12
  locator: { number: "4.10.b12", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 72933, end: 73134 }
  source: "reasonable care is taken to separate and maintain a distinction between personal and professional presence on social media where this could result in harmful dual relationships with clients or patients"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["taken", "separate", "maintain"]
  about: "separating personal and professional presence online"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Take reasonable care to keep one's personal and professional presence on social media apart where mixing them could create harmful dual relationships."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b13
  locator: { number: "4.10.b13", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 73137, end: 73255 }
  source: "any public, online communication is carried out in a manner consistent with own ethical framework or code of practice."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["carried"]
  about: "public online communication"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Make sure any public online communication fits one's own ethical framework or code."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b14
  locator: { number: "4.10.b14", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 73256, end: 73319 }
  source: "Establish and maintain a secure frame for the therapeutic work."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Establish", "maintain"]
  about: "a secure frame for the work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Create and keep a secure frame for therapy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b15
  locator: { number: "4.10.b15", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 73320, end: 73398 }
  source: "Negotiate an appropriate therapeutic contract using all available information."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Negotiate", "using"]
  about: "negotiating the contract"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Agree a suitable contract with the client using all the information available."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b16
  locator: { number: "4.10.b16", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 73399, end: 73591 }
  source: "Recognise and work with breaks and holidays and how these may affect the therapeutic relationship and process, making appropriate arrangements for clients to seek support in case of emergency."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "work", "affect", "making"]
  about: "breaks, holidays and emergency cover"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Recognise and work with breaks and holidays and their effect on the relationship and process, arranging for clients to get support in an emergency."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b17
  locator: { number: "4.10.b17", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 73592, end: 73799 }
  source: "Understand the need for and have made professional arrangements in the event of the counsellor/psychotherapist’s sudden or unplanned break or ending and communicate the arrangements to the client or patient."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand", "made", "communicate"]
  about: "arrangements for a sudden ending"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand why arrangements are needed for one's own sudden or unplanned absence or ending, have made them, and tell the client about them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b18
  locator: { number: "4.10.b18", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 73800, end: 73911 }
  source: "Adapt appropriately to manage different contracted time-frames, including open- ended and time-limited therapy."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Adapt", "manage"]
  about: "open-ended and time-limited work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Adjust suitably to different contracted time frames, both open-ended and time-limited."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b19
  locator: { number: "4.10.b19", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 73912, end: 74014 }
  source: "Manage contact with external agencies and professionals, as appropriate to the interest of the client."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Manage"]
  about: "contact with outside agencies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Handle contact with outside agencies and professionals as the client's interest requires."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.10.b20
  locator: { number: "4.10.b20", headingPath: ["Benchmark standards", "Threshold level (3rd class): Boundaries and contracting"] }
  span: { start: 74015, end: 74173 }
  source: "Adopt an enquiring, critical awareness and future oriented approach to professional challenges, along with awareness of social and therapeutic responsibility."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Adopt"]
  about: "an enquiring, forward-looking stance"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Take an enquiring, critical and forward-looking approach to professional challenges, aware of social and therapeutic responsibility."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b1
  locator: { number: "4.11.b1", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 74285, end: 74344 }
  source: "Understand the concepts and processes of client assessment:"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand"]
  about: "client assessment concepts and processes"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand the ideas and steps of client assessment, as the points that follow set out."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b2
  locator: { number: "4.11.b2", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 74347, end: 74399 }
  source: "define and describe the concept of client assessment"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["define", "describe"]
  about: "defining client assessment"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be able to define and explain client assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b3
  locator: { number: "4.11.b3", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 74402, end: 74636 }
  source: "understand different political, philosophical and theoretical perspectives on use of assessment tools and outcome measures and critically appraise their implications for practice in contemporary contexts based on research in the field"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["understand", "appraise"]
  about: "perspectives on assessment tools and outcome measures"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand the political, philosophical and theoretical views on assessment tools and outcome measures and judge, from research, what they mean for present-day practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b4
  locator: { number: "4.11.b4", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 74639, end: 74787 }
  source: "critically discuss the contexts in which client assessment happens, considering ethical and legal frameworks as well as agency policy and procedures"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["discuss", "considering"]
  about: "contexts of assessment, law and agency policy"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Discuss critically the settings in which assessment takes place, with regard to ethics, law and agency policy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b5
  locator: { number: "4.11.b5", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 74790, end: 75022 }
  source: "demonstrate a working knowledge of at least one approach to assessment compatible with one’s own core theoretical model, discussing how this approach may influence the focus and agreed process of the therapeutic work with the client"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["demonstrate", "discussing", "influence"]
  about: "an assessment approach that fits one's model"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show working knowledge of at least one assessment approach that fits one's core model, and discuss how it shapes the focus and agreed process of the work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b6
  locator: { number: "4.11.b6", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 75025, end: 75161 }
  source: "understand the risks and challenges experienced by individual clients in terms of their suitability for technologically mediated therapy"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["understand"]
  about: "suitability for technology-mediated therapy"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand the risks and difficulties some clients face in being suited to therapy by technology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b7
  locator: { number: "4.11.b7", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 75164, end: 75279 }
  source: "understand the risk and protective factors in relation to client safety, deliberate self-harm and suicide potential"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["understand"]
  about: "risk and protective factors for client safety"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand the factors that raise and lower risk to client safety, including self-harm and suicide."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b8
  locator: { number: "4.11.b8", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 75282, end: 75436 }
  source: "understand differences between suicidal ideation (thoughts of suicide) and suicidal intent (an intention to act on thoughts) in determining levels of risk"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["understand", "determining"]
  about: "thoughts and intent in judging risk"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand how thinking about suicide differs from intending to act, in judging the level of risk."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b9
  locator: { number: "4.11.b9", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 75439, end: 75585 }
  source: "demonstrate a working knowledge of legislative, policy or procedural expectations in how best to respond to a client presenting at immediate risk."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["demonstrate", "respond"]
  about: "responding to immediate risk"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show working knowledge of the legal, policy or procedural steps for responding to a client at immediate risk."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b10
  locator: { number: "4.11.b10", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 75586, end: 75893 }
  source: "Recognise that specific knowledge and skills are required, and additional training may be needed, to work with particular client groups and diverse client populations, especially where there are additional considerations relating to client competence, capacity, understanding, awareness and decision making."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "work"]
  about: "extra training for particular client groups"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Recognise that working with certain client groups and populations needs particular knowledge and skills, and may need more training, above all where competence, capacity, understanding or decision-making are in question."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b11
  locator: { number: "4.11.b11", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 75894, end: 76093 }
  source: "Recognise own competencies in relation to working with specific client groups, approaches, techniques, methods, and modes of delivery (including remote, technically mediated and in-person therapies)."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise"]
  about: "one's own competence across groups and modes"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know one's own competence with particular client groups, approaches, techniques and methods, and with each mode of delivery, remote and in person."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b12
  locator: { number: "4.11.b12", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 76097, end: 76217 }
  source: "Critically aware of the diverse therapeutic perspectives around notions of assessment and formulation/conceptualisation:"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "perspectives on assessment and formulation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be critically aware of the different views on assessment and on formulation or conceptualisation, as the points that follow set out."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b13
  locator: { number: "4.11.b13", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 76220, end: 76293 }
  source: "understand arguments for and against these as formal processes in therapy"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["understand"]
  about: "arguments for and against formal assessment"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand the case for and against treating these as formal processes in therapy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b14
  locator: { number: "4.11.b14", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 76296, end: 76397 }
  source: "critically reflect about how these perspectives may influence therapy provision and client experience"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["reflect", "influence"]
  about: "how these views shape services and experience"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Reflect critically on how these views may shape services and clients' experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b15
  locator: { number: "4.11.b15", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 76400, end: 76532 }
  source: "able to articulate a coherent personal approach to counselling which addresses how client presentations are assessed and worked with"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["articulate", "addresses", "assessed"]
  about: "a personal approach to assessment"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be able to set out a coherent personal approach to counselling that covers how client presentations are assessed and worked with."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b16
  locator: { number: "4.11.b16", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 76535, end: 76695 }
  source: "aware of the limitations of one’s own training and experience in relation to evaluating the complexity of client work and the possible risks arising in the work"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "the limits of one's training in complex work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be aware of the limits of one's training and experience in judging complex client work and its risks."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b17
  locator: { number: "4.11.b17", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 76698, end: 76763 }
  source: "knowledgeable about networks of support and referral for clients."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "support and referral networks"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know the networks of support and referral open to clients."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b18
  locator: { number: "4.11.b18", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 76767, end: 76922 }
  source: "Understand and be able to discuss the client’s concerns with them and articulate the way in which counselling/psychotherapy can address these difficulties."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand", "discuss", "articulate", "address"]
  about: "discussing the client's concerns and how therapy helps"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand and talk through the client's concerns with them and explain how therapy can help with them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b19
  locator: { number: "4.11.b19", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 76923, end: 77118 }
  source: "Determine whether each individual client has competence and capacity to engage with and make use of the therapeutic approach offered, including in the context in which therapy is to be delivered."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Determine", "engage", "make"]
  about: "client competence and capacity for the approach"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Judge whether each client has the competence and capacity to engage with and use the approach offered, in the setting where it is delivered."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b20
  locator: { number: "4.11.b20", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 77119, end: 77243 }
  source: "Provide a clear explanation of the stated therapeutic approach, including the rationale for each participant’s contribution."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Provide"]
  about: "explaining the approach and each role"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Explain the approach clearly, including why each party contributes as they do."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b21
  locator: { number: "4.11.b21", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 77248, end: 77473 }
  source: "Actively seek to work within one’s own competencies in relation to working with specific client groups, approaches, techniques, methods, and modes of delivery (including remote, technically mediated, and in-person therapies)."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["seek", "work"]
  about: "staying within one's competence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Make an active effort to stay within one's competence, whatever the client group, approach, technique, method or delivery mode."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b22
  locator: { number: "4.11.b22", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 77474, end: 77723 }
  source: "Competently conduct an episode of therapy which is consistent with a stated therapeutic approach and includes an assessment of the client’s needs, goals, identification of risk and the design of a coherent plan for the work based on that assessment:"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["conduct", "includes"]
  about: "conducting an episode of therapy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Carry out an episode of therapy competently and in keeping with a stated approach, including assessment of needs and goals, identifying risk and a coherent plan, as the points that follow set out."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b23
  locator: { number: "4.11.b23", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 77726, end: 77800 }
  source: "undertake a comprehensive evaluation of client needs and goals for therapy"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["undertake"]
  about: "evaluating needs and goals"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Carry out a thorough evaluation of the client's needs and goals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b24
  locator: { number: "4.11.b24", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 77803, end: 77964 }
  source: "develop a conceptualisation or formulation about what may be happening for the client, based on initial and evolving work together and drawing on relevant theory"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["develop"]
  about: "building a formulation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Build a conceptualisation or formulation of what may be going on for the client, drawing on theory and on the work as it unfolds."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b25
  locator: { number: "4.11.b25", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 77967, end: 78020 }
  source: "identify and evaluate presenting risks for the client"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["identify", "evaluate"]
  about: "identifying presenting risk"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Identify and weigh the risks the client presents with."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b26
  locator: { number: "4.11.b26", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 78023, end: 78222 }
  source: "devise and agree a contract and a plan for working together, including what, how and when that work will happen and setting review points in order to re-evaluate and establish when work is completed."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["devise", "agree"]
  about: "a contract and plan with review points"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Draw up and agree a contract and plan for the work, covering what, how and when, with review points to reassess and decide when the work is done."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b27
  locator: { number: "4.11.b27", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 78223, end: 78367 }
  source: "Apply appropriate strategies and interventions (as appropriate to the modality) in work with specific client populations and client experiences."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Apply"]
  about: "interventions for particular populations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use strategies and interventions suited to the modality with particular client populations and experiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.11.b28
  locator: { number: "4.11.b28", headingPath: ["Benchmark standards", "Threshold level (3rd class): Assessment"] }
  span: { start: 78368, end: 78431 }
  source: "Make informed decisions about referral to appropriate agencies."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Make"]
  about: "referral decisions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Make well-founded decisions about referring clients to suitable agencies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b1
  locator: { number: "4.12.b1", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 78558, end: 78673 }
  source: "Understand the concept of the therapeutic relationship from the perspective of a variety of theoretical approaches."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand"]
  about: "the relationship across approaches"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand the therapeutic relationship as several theoretical approaches see it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b2
  locator: { number: "4.12.b2", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 78674, end: 78963 }
  source: "Demonstrate understanding of a range of therapeutic approaches, the theory that informs them, and the evidence base relating to their effectiveness, in order to help clients, make appropriate choices or voice therapeutic preference in the therapeutic relationship according to their needs."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Demonstrate", "help", "make", "voice"]
  about: "approaches and evidence to support client choice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show understanding of a range of approaches, their theory and the evidence for their effectiveness, so that clients can make informed choices or state preferences that suit their needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b3
  locator: { number: "4.12.b3", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 78964, end: 79089 }
  source: "Understand the theoretical dynamics of power, oppression and privilege and how these may affect the therapeutic relationship."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Understand", "affect"]
  about: "power, oppression and privilege in the relationship"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand the theory of power, oppression and privilege and how they may bear on the relationship."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b4
  locator: { number: "4.12.b4", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 79093, end: 79239 }
  source: "Respectful of difference, for example embracing sexual diversity, respecting, accepting and honouring the client’s sexual orientation and choices."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["embracing", "respecting", "accepting", "honouring"]
  about: "respect for sexual diversity and difference"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Respect difference, for instance by welcoming sexual diversity and respecting and honouring each client's sexual orientation and choices."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b5
  locator: { number: "4.12.b5", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 79240, end: 79488 }
  source: "Open to ensuring a saf e space for the honest discussion of clients’ experience as relevant to them, to support the development and maintenance of healthy self- identities without the imposition of the therapist’s own values, view and expectations."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["ensuring", "support"]
  about: "a safe space for identity without imposing one's views"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be willing to provide a safe space for clients to talk honestly about their experience, supporting healthy self-identities without imposing one's own values, views or expectations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b6
  locator: { number: "4.12.b6", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 79489, end: 79667 }
  source: "Competent to work therapeutically and non-defensively with challenging situations, taking own limitations into account in the repair of empathic failures and relational ruptures."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["work", "taking"]
  about: "repairing ruptures without defensiveness"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Be competent to work therapeutically and without defensiveness in hard situations, taking account of one's own limits when repairing empathic failures and ruptures."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b7
  locator: { number: "4.12.b7", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 79671, end: 79758 }
  source: "Monitor own bias through the use of self-supervision, supervision and personal therapy."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Monitor"]
  about: "monitoring bias through supervision and therapy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Keep watch on one's own bias through self-supervision, supervision and personal therapy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b8
  locator: { number: "4.12.b8", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 79759, end: 79940 }
  source: "Identify, reflect on and work openly and non-defensively with socio-cultural and identity differences between client and counsellor and their impact on the therapeutic relationship."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Identify", "reflect", "work"]
  about: "differences between client and counsellor"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Identify, reflect on and work openly with differences of social position, culture and identity between client and counsellor, and their effect on the relationship."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b9
  locator: { number: "4.12.b9", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 79941, end: 80105 }
  source: "Recognise and work with component aspects of the therapeutic alliance such as client motivation, commitment to the therapeutic process and contractual arrangements."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "work"]
  about: "the parts of the therapeutic alliance"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Recognise and work with the parts of the alliance, such as client motivation, commitment to the process and the contract."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b10
  locator: { number: "4.12.b10", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 80106, end: 80218 }
  source: "Recognise and take steps to mitigate the implicit power imbalance in the counselling/psychotherapy relationship."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "take", "mitigate"]
  about: "the power imbalance in therapy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Recognise the power imbalance built into the therapy relationship and act to reduce it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b11
  locator: { number: "4.12.b11", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 80219, end: 80583 }
  source: "Recognise own conscious and unconscious bias and demonstrate anti- discriminatory practice within the therapeutic relationship in relation to diversity and the rights and responsibilities of all clients, regardless of their social context,\n\n26\ngender, age, ethnicity, national or ethnic origin, culture, class, disability, sexual orientation, religion and beliefs."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "demonstrate"]
  about: "anti-discriminatory practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Recognise one's own conscious and unconscious bias and show anti-discriminatory practice in the relationship, respecting every client's rights and responsibilities whatever their background, identity or beliefs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b12
  locator: { number: "4.12.b12", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 80584, end: 80705 }
  source: "Establish and sustain a therapeutic alliance which respects clients’ goals and preferences for a way of working together."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Establish", "sustain", "respects"]
  about: "an alliance that respects client goals"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Build and keep an alliance that respects the client's goals and preferred way of working together."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b13
  locator: { number: "4.12.b13", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 80706, end: 80804 }
  source: "Recognise and work therapeutically with difficulties and ruptures in the therapeutic relationship."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Recognise", "work"]
  about: "difficulties and ruptures"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Notice and work therapeutically with ruptures and other difficulties in the relationship."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b14
  locator: { number: "4.12.b14", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 80805, end: 80929 }
  source: "Regularly review and work therapeutically with the client’s perceptions and experiences of the therapist and therapy itself."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["review", "work"]
  about: "the client's view of therapist and therapy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Review regularly, and work with, how the client sees the therapist and the therapy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.12.b15
  locator: { number: "4.12.b15", headingPath: ["Benchmark standards", "Threshold level (3rd class): The therapeutic relationship"] }
  span: { start: 80930, end: 81137 }
  source: "Practise in a way that is transparent, inclusive and non-discriminatory, including in advertising and marketing services, in line with professional body guidance and working within relevant legal frameworks."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["Practise"]
  about: "transparent, inclusive practice including marketing"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Practise openly, inclusively and without discrimination, including in advertising and marketing, following professional body guidance and the law."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b1
  locator: { number: "4.13.b1", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 81221, end: 81291 }
  source: "perf orm assigned tasks as part of a team, participating in discussion"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["assigned", "participating"]
  about: "teamwork and discussion"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Carry out allocated tasks in a team and take part in discussion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b2
  locator: { number: "4.13.b2", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 81294, end: 81359 }
  source: "bri ng together information and materi als from different sources"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "drawing information together from sources"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Gather information and material from different sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b3
  locator: { number: "4.13.b3", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 81362, end: 81394 }
  source: "identi fy problems and questions"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "identifying problems and questions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Pick out problems and questions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b4
  locator: { number: "4.13.b4", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 81397, end: 81442 }
  source: "undertake the analysis of factual information"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["undertake"]
  about: "analysing factual information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Analyse factual information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b5
  locator: { number: "4.13.b5", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 81445, end: 81507 }
  source: "recognise strengths and weaknesses in the arg uments of others"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["recognise"]
  about: "weighing others' arguments"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "See the strong and weak points in other people's arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b6
  locator: { number: "4.13.b6", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 81510, end: 81588 }
  source: "produce a synthesis of the state of knowledge on a particular subject or topic"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["produce"]
  about: "synthesising knowledge on a topic"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Bring together the current state of knowledge on a topic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b7
  locator: { number: "4.13.b7", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 81591, end: 81636 }
  source: "with guidance, undert ake tasks independently"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "working independently with guidance"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Work on tasks independently, with guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b8
  locator: { number: "4.13.b8", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 81639, end: 81703 }
  source: "re flect on their own progress and make use of feedback provided"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["make"]
  about: "reflecting on progress and using feedback"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Reflect on one's own progress and use the feedback given."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b9
  locator: { number: "4.13.b9", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 81706, end: 81764 }
  source: "express themselves effectively both orally and in wri ting"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["express"]
  about: "oral and written expression"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Express oneself well in speech and in writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b10
  locator: { number: "4.13.b10", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 81767, end: 81842 }
  source: "present knowledge or an arg ument in a way that is comprehensible to others"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["present"]
  about: "presenting knowledge or argument clearly"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Put knowledge or an argument across in a way others understand."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b11
  locator: { number: "4.13.b11", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 81845, end: 81931 }
  source: "use relevant IT to collate, analyse, select and present information (digital literacy)"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["use", "collate", "analyse", "select", "present"]
  about: "digital literacy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use suitable IT to collect, analyse, choose and present information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b12
  locator: { number: "4.13.b12", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 81934, end: 81962 }
  source: "make effective presentations"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["make"]
  about: "presentations"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Give effective presentations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b13
  locator: { number: "4.13.b13", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 81965, end: 82096 }
  source: "think critically and show critical awareness and evaluation of theoretical concepts and therapeutic modalities and research methods"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["think", "show"]
  about: "critical evaluation of theory, modalities and methods"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Think critically and evaluate theoretical concepts, therapeutic modalities and research methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b14
  locator: { number: "4.13.b14", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 82099, end: 82180 }
  source: "demonstrate an ability to comprehend when presented with new ideas or information"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["demonstrate", "comprehend"]
  about: "grasping new ideas"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show that one can grasp new ideas or information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b15
  locator: { number: "4.13.b15", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 82183, end: 82241 }
  source: "demonstrate skills in recognising and describing materi al"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["demonstrate", "recognising", "describing"]
  about: "recognising and describing material"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show skill in recognising and describing material."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b16
  locator: { number: "4.13.b16", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 82244, end: 82326 }
  source: "demonstrate classification skills in describing, categori sing and collati ng data"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["demonstrate", "describing"]
  about: "classifying data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show skill in classifying data by describing, sorting and collating it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b17
  locator: { number: "4.13.b17", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 82329, end: 82444 }
  source: "understand the importance of health and safety and of equality, diversity and inclusiveness in the work environment"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["understand"]
  about: "health, safety and inclusion at work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand why health and safety and equality, diversity and inclusion matter at work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b18
  locator: { number: "4.13.b18", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 82447, end: 82611 }
  source: "appreciate and engage in contempora ry debates relati ng to global sustainabilit y, employabilit y and global perspectives, including decolonisation and anti-racism"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["appreciate", "engage"]
  about: "debates on sustainability, employability and global perspectives"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Value and take part in current debates on global sustainability, employability and global perspectives, including decolonisation and anti-racism."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.13.b19
  locator: { number: "4.13.b19", headingPath: ["Benchmark standards", "Threshold level (3rd class): Generic skills"] }
  span: { start: 82614, end: 82665 }
  source: "appreciate the need to act in a sustainable manner."
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates with honours in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["appreciate", "act"]
  about: "acting sustainably"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Value the need to act sustainably."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.14
  locator: { number: "4.14", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 82693, end: 82873 }
  source: "4.14 Criteria for achievement above threshold level at 2:2 and 2:1 will be in line with the higher education provider’s common or generic marking schemes for undergraduate courses."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "honours courses in the subject"
  addressee: provider
  verbs: []
  about: "typical-level criteria left to institutional marking schemes"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Criteria for 2:2 and 2:1 performance above the threshold will follow each institution's common or generic undergraduate marking schemes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.15
  locator: { number: "4.15", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 82902, end: 83067 }
  source: "4.15 Criteria for excellent (1st class) achievement will be in line with the higher education provider’s common or generic marking schemes for undergraduate courses."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "honours courses in the subject"
  addressee: provider
  verbs: []
  about: "excellent-level criteria left to institutional marking schemes"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Criteria for first-class performance will follow each institution's common or generic undergraduate marking schemes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.16.b1
  locator: { number: "4.16.b1", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 83499, end: 83552 }
  source: "understand how knowledge is advanced through research"
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["understand", "advanced"]
  about: "how research advances knowledge"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Understand how research moves knowledge forward."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.16.b2
  locator: { number: "4.16.b2", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 83555, end: 83587 }
  source: "identify boundaries of knowledge"
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["identify"]
  about: "the boundaries of knowledge"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Identify where current knowledge ends."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.16.b3
  locator: { number: "4.16.b3", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 83590, end: 83631 }
  source: "create new insights in the field of study"
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["create"]
  about: "new insight in the field"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Create new insight in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.16.b4
  locator: { number: "4.16.b4", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 83634, end: 83722 }
  source: "develop higher level skills through self-directed academic and professional development."
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["develop"]
  about: "self-directed higher-level development"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Build higher-level skills by directing one's own academic and professional growth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.16.b5
  locator: { number: "4.16.b5", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 83723, end: 83957 }
  source: "At this level, award holders must demonstrate a knowledge base that extends to a systematic understanding and critical awareness of topics which are informed by research at the forefront of the discipline of counselling/psychotherapy."
  stem: "4.16"
  statementType: threshold
  rung: threshold
  force: must
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["demonstrate", "extends"]
  about: "a systematic, research-informed knowledge base"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Holders of the award must show systematic understanding and critical awareness of topics informed by research at the forefront of counselling and psychotherapy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.17.b1
  locator: { number: "4.17.b1", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 84145, end: 84261 }
  source: "critical discussion and analysis of complex concepts and work is carried out independently and with some originality"
  stem: "4.17"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["carried"]
  about: "independent, original critical analysis"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Discuss and analyse complex concepts critically, working independently and with some originality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.17.b2
  locator: { number: "4.17.b2", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 84264, end: 84501 }
  source: "critical awareness of the history of ideas, the cultural context, philosophical basis, social and political theories that inform and influence the development of counselling and psychotherapy, and underpin a personal approach to practice"
  stem: "4.17"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["inform", "influence", "underpin"]
  about: "the history, culture and philosophy of the field"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Be critically aware of the history of ideas, culture, philosophy and social and political theory behind the field's development and one's own approach."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.17.b3
  locator: { number: "4.17.b3", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 84504, end: 84614 }
  source: "conceptualising and/or formulating ways of working with clients with chronic and enduring mental health issues"
  stem: "4.17"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["conceptualising", "formulating"]
  about: "formulating work with long-term mental health issues"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Conceptualise or formulate ways of working with clients whose mental health problems are chronic and lasting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.17.b4
  locator: { number: "4.17.b4", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 84617, end: 84727 }
  source: "a critical understanding of the language and discourses around diagnosis, psychopathology and mental disorders"
  stem: "4.17"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: []
  about: "discourses of diagnosis and psychopathology"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Understand critically the language and discourses of diagnosis, psychopathology and mental disorder."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.17.b5
  locator: { number: "4.17.b5", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 84730, end: 84920 }
  source: "communicating about the harm caused by discriminatory practices and aim to reduce insensitivity to power differentials within therapeutic service provision, training and supervisory contexts"
  stem: "4.17"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["communicating", "reduce"]
  about: "speaking about discriminatory harm and power"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Speak about the harm done by discriminatory practice and work to reduce insensitivity to power differences in services, training and supervision."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.17.b6
  locator: { number: "4.17.b6", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 84923, end: 85216 }
  source: "a critical understanding and awareness of how ‘unconscious’ or ‘out of awareness’ processes in both the client and therapist may shape perceptions, experiences and the therapeutic process and work therapeutically with ruptures or difficulties within the therapeutic relationship that may arise"
  stem: "4.17"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["shape", "work"]
  about: "unconscious processes and ruptures"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Understand critically how processes outside awareness in client and therapist may shape perception and the work, and work therapeutically with ruptures that arise."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.17.b7
  locator: { number: "4.17.b7", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 85219, end: 85321 }
  source: "integrating relevant theory and research in the areas of diversity and equality into clinical practice"
  stem: "4.17"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["integrating"]
  about: "bringing diversity research into practice"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Bring theory and research on diversity and equality into clinical practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.17.b8
  locator: { number: "4.17.b8", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 85324, end: 85431 }
  source: "utilising audit and evaluation methodologies to contribute to improving the process and outcomes of therapy"
  stem: "4.17"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["utilising", "contribute", "improving"]
  about: "audit and evaluation to improve therapy"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Use audit and evaluation methods to help improve the process and outcomes of therapy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.17.b9
  locator: { number: "4.17.b9", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 85434, end: 85823 }
  source: "successf ully developing, planning, implementing and evaluating a substantial empirical research study, in response to a relevant research question. This might be a qualitative, quantitative or mixed methods research study or systematic review, which will contribute knowledge to the field of study in counselling and psychotherapy informed by wide current understandings of the discipline"
  stem: "4.17"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["developing", "planning", "implementing", "evaluating"]
  about: "a substantial research study"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Design, plan, carry out and evaluate a substantial empirical study or systematic review that answers a relevant question and adds to knowledge in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.17.b10
  locator: { number: "4.17.b10", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 85826, end: 85962 }
  source: "reflexivity, self-awareness and the therapeutic use of self to work at depth in the therapeutic relationship and the therapeutic process"
  stem: "4.17"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["work"]
  about: "reflexive use of self for in-depth work"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Use reflexivity, self-awareness and the self therapeutically to work in depth in the relationship and process."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/counselling-and-psychotherapy-2022/4.17.b11
  locator: { number: "4.17.b11", headingPath: ["Benchmark standards", "Benchmark standard for master's degrees"] }
  span: { start: 85965, end: 86079 }
  source: "facilitating and/or containing the intense emotions that may emerge within a highly charged therapeutic encounter."
  stem: "4.17"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in Counselling and Psychotherapy"
  addressee: learner
  verbs: ["facilitating", "containing", "emerge"]
  about: "holding intense emotion"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Facilitate or contain intense emotion in a highly charged encounter."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/counselling-and-psychotherapy-2022/1.4
  forPractitioner: { text: "Teach the places of practice as shaped by history and by social, economic and political forces, not as neutral venues.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should learn to read any service you work in against its history, culture, economics and politics.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on therapy settings read in their wider context; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 1.4). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 1 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about therapy settings read in their wider context. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: Pick a service you know: what history and politics shaped the therapy it offers? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/1.5
  forPractitioner: { text: "Make sure trainees learn to weigh in-person and remote modes against client need, their own competence and the relationship before choosing how to work.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Before you choose to work in person or by video, phone or text, you must weigh the risks and benefits for that client and for your own competence.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" for both the honours degree and the master's degree, on choosing a mode of delivery with care; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 1.5). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 1 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about choosing a mode of delivery with care. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as a requirement worded with \"must\". Ask: How would you decide whether a given client is better seen in person or online? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/1.7
  forPractitioner: { text: "Design the course so that its academic, personal and skills strands all lead towards a supervised, assessed placement, and plan where the UNESCO sustainability competencies are built.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your course will bring together study, personal growth and skills work to ready you for a supervised placement with clients, and should leave you able to keep learning about yourself and your practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" for both the honours degree and the master's degree, on training that joins study, growth and a supervised placement; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 1.7). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 1 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about training that joins study, growth and a supervised placement. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expected feature worded with \"will\". Ask: Where in the course do the academic, personal and skills strands meet before placement? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/1.8
  forPractitioner: { text: "Check that the course gives every trainee the literature, research methods, client skills and personal growth, whatever the modality, and that graduates leave able to work safely under contract and look after themselves.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Whatever approach you train in, you will meet the research literature, learn how research is done, build skills with clients and grow as a person; by the end you will be able to work well with clients within a safe agreement while looking after yourself.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" for both the honours degree and the master's degree, on what all training offers and what the competent graduate can do; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 1.8). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 1 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about what all training offers and what the competent graduate can do. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expected feature worded with \"will\". Ask: Which of these four strands feels thinnest in your training so far? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/1.10
  forPractitioner: { text: "Build in experiential learning that allows vulnerability, test the curriculum for majority-culture bias, and make each assessment authentic, accessible and close to real therapeutic work.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expectation stated without one of the five obliging words (force recorded as describes) on the course and its team, on experiential learning, inclusive content and authentic assessment, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 1.10). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 1, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles experiential learning, inclusive content and authentic assessment. Frame it for staff as an expectation stated without one of the five obliging words (force recorded as describes), and ask: Which assessment on the course is furthest from what a therapist actually does? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/1.12
  forPractitioner: { text: "Invite students to critique the profession's institutions and dominant ideas about mental illness, research and treatment, and to imagine how therapy can grow in ways that benefit individuals, communities and society.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be asked to look critically at how your profession is organised and talked about, and to think about how it, and you, can keep doing good for people and communities over time.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" for both the honours degree and the master's degree, on a reflective view of the profession's sustainable future; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 1.12). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 1 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about a reflective view of the profession's sustainable future. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expected feature worded with \"will\". Ask: What would a more sustainable future for counselling services look like where you live? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/1.13
  forPractitioner: { text: "Map the eight UNESCO competencies across modules and placement, and make sure the course's own facilities and ways of working model them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will need to use all eight sustainability competencies, such as systems thinking, collaboration and self-awareness, in your work as a therapist, and your course should let you see and practise them.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expectation stated without one of the five obliging words (force recorded as describes) for both the honours degree and the master's degree, on the eight UNESCO sustainability competencies; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 1.13). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 1 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about the eight UNESCO sustainability competencies. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation stated without one of the five obliging words (force recorded as describes). Ask: Which of the eight competencies can you already show an example of in your practice? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/1.14
  forPractitioner: { text: "Provide spaces for experiential and adult learning across digital, personal, group and community settings, and make students' growing responsibility for their own and others' well-being an explicit aim of the course.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course must help you grow a sense of responsibility for other people's psychological well-being and for your own.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" for both the honours degree and the master's degree, on responsibility for one's own and others' well-being as a developmental aim; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 1.14). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 1 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about responsibility for one's own and others' well-being as a developmental aim. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as a requirement worded with \"must\". Ask: How does the course show students that it is building their responsibility for well-being? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/1.16
  forPractitioner: { text: "Give students tasks that make them state the market and practical value of their therapeutic skills, for job applications and for private practice plans, and help them notice their own enterprising strengths.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to explain and show what your skills are worth, both to an employer and in a plan for your own practice, and to notice where you are enterprising.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on knowing and showing the value of therapeutic skills; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 1.16). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 1 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about knowing and showing the value of therapeutic skills. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: How would you describe the value of your skills to an agency that is hiring? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/1.22
  forPractitioner: { text: "Set tasks in which students use digital tools to present ideas creatively and accessibly, and link them to study success and employability.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should learn to use digital tools to put your ideas across creatively and accessibly, in ways that help your studies and your job prospects.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on digital competency for communication and employability; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 1.22). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 1 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about digital competency for communication and employability. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: Which digital tools will you need for remote client work and for finding work? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/1.23
  forPractitioner: { text: "Plan employability and enterprise into the curriculum from the start, through dedicated modules, threads across modules or both, with matching outcomes and authentic assessment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on employability and enterprise in curriculum design, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 1.23). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 1, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles employability and enterprise in curriculum design. Frame it for staff as an expectation worded with \"should\", and ask: Where are employability and enterprise assessed, not just mentioned? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/1.24
  forPractitioner: { text: "Invite practitioners, agencies and alumni into teaching so that students meet the working world and learn to promote themselves ethically.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Write about this as an expectation stated without one of the five obliging words (force recorded as describes) on the course and its team, on speakers from the profession and contact with agencies, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 1.24). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 1, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles speakers from the profession and contact with agencies. Frame it for staff as an expectation stated without one of the five obliging words (force recorded as describes), and ask: Which voices from practice do students hear before they qualify? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.1
  forPractitioner: { text: "Confirm the course joins the five strands and contains a supervised client placement; the methods are the course team's to choose.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" on the course and its team, on an integrated curriculum and a supervised placement in every course, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.1). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 2, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles an integrated curriculum and a supervised placement in every course. Frame it for staff as an expected feature worded with \"will\", and ask: Where does each of the five strands appear in the course map? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b1
  forPractitioner: { text: "Make students responsible for planning and reviewing their own learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your personal development work should help you take charge of your own learning.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on owning one's learning; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 1). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b2 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about owning one's learning. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: What have you chosen to learn beyond what was set? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b2
  forPractitioner: { text: "Link personal development activities to safe, ethical client work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should help you work with clients safely and ethically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on safe and ethical client work; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 2). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b1 and qaa/counselling-and-psychotherapy-2022/2.2.b3 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about safe and ethical client work. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: What in your personal work has made your client work safer? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b3
  forPractitioner: { text: "Use process work to help students separate their own reactions from the client's.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should help you tell your own feelings apart from your client's and see yourself in relation to others.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on telling self from client; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 3). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b2 and qaa/counselling-and-psychotherapy-2022/2.2.b4 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about telling self from client. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: How do you know whether a feeling in session is yours or the client's? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b4
  forPractitioner: { text: "Help students explore how they use themselves in therapy.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should help you see yourself as a resource in the work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on the self as a resource; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 4). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b3 and qaa/counselling-and-psychotherapy-2022/2.2.b5 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about the self as a resource. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: How do you use yourself in sessions? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b5
  forPractitioner: { text: "Include identity work in personal development groups.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should help you become aware of your own personal and social identity.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on awareness of personal and social identity; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 5). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b4 and qaa/counselling-and-psychotherapy-2022/2.2.b6 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about awareness of personal and social identity. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: Which parts of your identity are most visible to clients? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b6
  forPractitioner: { text: "Give students structured ways to surface and tackle implicit bias.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should help you find and deal with hidden biases and prejudice in yourself and your work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on hidden bias in self and practice; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 6). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b5 and qaa/counselling-and-psychotherapy-2022/2.2.b7 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about hidden bias in self and practice. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: What hidden bias have you found in yourself? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b7
  forPractitioner: { text: "Calibrate students' self-assessment against feedback.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should give you a true sense of how competent you are.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on an accurate view of own competence; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 7). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b6 and qaa/counselling-and-psychotherapy-2022/2.2.b8 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about an accurate view of own competence. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: Where does your own view of your skill differ from your tutor's? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b8
  forPractitioner: { text: "Make room for self-acceptance work alongside skills training.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should help you accept yourself, which helps you accept your clients.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on self-acceptance as a base for accepting clients; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 8). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b7 and qaa/counselling-and-psychotherapy-2022/2.2.b9 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about self-acceptance as a base for accepting clients. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: How does accepting yourself change how you meet clients? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b9
  forPractitioner: { text: "Require a self-care plan and review it over the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should help you build a self-care plan that guards against burnout and keeps you emotionally strong.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on a self-care strategy against burnout; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 9). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b8 and qaa/counselling-and-psychotherapy-2022/2.2.b10 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about a self-care strategy against burnout. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: What is in your self-care plan, and do you follow it? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b10
  forPractitioner: { text: "Use placement demands to build organisation and resilience.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should help you become organised, adaptable and resilient.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on being organised, flexible and resilient; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 10). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b9 and qaa/counselling-and-psychotherapy-2022/2.2.b11 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about being organised, flexible and resilient. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: How do you recover after a hard week on placement? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b11
  forPractitioner: { text: "Model lifelong reflective practice in teaching and supervision.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should lead you to keep building self-awareness through reflection all your working life.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on lifelong reflection and reflexivity; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 11). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b10 and qaa/counselling-and-psychotherapy-2022/2.2.b12 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about lifelong reflection and reflexivity. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: How will you keep reflecting once the course ends? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b12
  forPractitioner: { text: "Link personal development to the professional and social setting of practice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should help you see yourself as a whole person within your profession and society.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on self-awareness in wider context; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 12). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b11 and qaa/counselling-and-psychotherapy-2022/2.2.b13 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about self-awareness in wider context. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: How does your place in society shape you as a therapist? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b13
  forPractitioner: { text: "Let students meet uncertainty safely in experiential work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should help you live with uncertainty, ambiguity, risk and failure.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on tolerating uncertainty and failure; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 13). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b12 and qaa/counselling-and-psychotherapy-2022/2.2.b14 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about tolerating uncertainty and failure. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: How do you respond when you do not know what to do in a session? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b14
  forPractitioner: { text: "Explore values explicitly, including environmental ones.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should make you sensitive to your values, including ethical, social, diversity and environmental ones.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on sensitivity to personal values; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 14). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b13 and qaa/counselling-and-psychotherapy-2022/2.2.b15 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about sensitivity to personal values. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: Which of your values most affects your work? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.2.b15
  forPractitioner: { text: "Connect personal development to students' enterprising strengths.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "It should help you see your enterprising strengths and use them flexibly.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on enterprising capabilities; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.2, bullet 15). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/2.2.b14 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about enterprising capabilities. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: Where could your enterprising strengths take your career? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.3.b1
  forPractitioner: { text: "Audit both campus and online access for every student.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on access in person and online, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.3, bullet 1). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.3.b2, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles access in person and online. Frame it for staff as an expectation worded with \"should\", and ask: Which students would struggle to reach this part of the course, and what is done about it? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.3.b2
  forPractitioner: { text: "Check that each student has the resources and devices they need.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on resources and technology for each learner, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.3, bullet 2). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.3.b1 and qaa/counselling-and-psychotherapy-2022/2.3.b3, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles resources and technology for each learner. Frame it for staff as an expectation worded with \"should\", and ask: Which students would struggle to reach this part of the course, and what is done about it? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.3.b3
  forPractitioner: { text: "Review curriculum content for accessibility.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on accessible curriculum and content, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.3, bullet 3). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.3.b2 and qaa/counselling-and-psychotherapy-2022/2.3.b4, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles accessible curriculum and content. Frame it for staff as an expectation worded with \"should\", and ask: Which students would struggle to reach this part of the course, and what is done about it? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.3.b4
  forPractitioner: { text: "Check rooms used for skills practice for access, safety and privacy.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on an accessible, safe and private space for practice, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.3, bullet 4). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.3.b3 and qaa/counselling-and-psychotherapy-2022/2.3.b5, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles an accessible, safe and private space for practice. Frame it for staff as an expectation worded with \"should\", and ask: Which students would struggle to reach this part of the course, and what is done about it? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.3.b5
  forPractitioner: { text: "Provide materials in accessible formats as standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on accessible formats, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.3, bullet 5). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.3.b4 and qaa/counselling-and-psychotherapy-2022/2.3.b6, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles accessible formats. Frame it for staff as an expectation worded with \"should\", and ask: Which students would struggle to reach this part of the course, and what is done about it? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.3.b6
  forPractitioner: { text: "Make inclusive design, accessible delivery and equal opportunity explicit checks at approval and review.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" on the course and its team, on inclusive design and parity of opportunity, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.3, bullet 6). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.3.b5 and qaa/counselling-and-psychotherapy-2022/2.3.b7, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles inclusive design and parity of opportunity. Frame it for staff as a requirement worded with \"must\", and ask: Which students would struggle to reach this part of the course, and what is done about it? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.3.b7
  forPractitioner: { text: "Vary assessment types so that no group is disadvantaged.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on a range of assessment strategies, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.3, bullet 7). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.3.b6 and qaa/counselling-and-psychotherapy-2022/2.3.b8, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles a range of assessment strategies. Frame it for staff as an expectation worded with \"should\", and ask: Which students would struggle to reach this part of the course, and what is done about it? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.3.b8
  forPractitioner: { text: "Screen every placement for safety and accessibility before use.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on checking placements for safety and access, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.3, bullet 8). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.3.b7 and qaa/counselling-and-psychotherapy-2022/2.3.b9, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles checking placements for safety and access. Frame it for staff as an expectation worded with \"should\", and ask: Which students would struggle to reach this part of the course, and what is done about it? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.3.b9
  forPractitioner: { text: "Monitor barriers like lack of devices or data.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on barriers such as digital poverty, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.3, bullet 9). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.3.b8 and qaa/counselling-and-psychotherapy-2022/2.3.b10, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles barriers such as digital poverty. Frame it for staff as an expectation worded with \"should\", and ask: Which students would struggle to reach this part of the course, and what is done about it? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.3.b10
  forPractitioner: { text: "Offer practical support, such as bursaries, laptops and data, where access is at risk.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on practical help for marginalised groups, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.3, bullet 10). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.3.b9, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles practical help for marginalised groups. Frame it for staff as an expectation worded with \"should\", and ask: Which students would struggle to reach this part of the course, and what is done about it? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.4
  forPractitioner: { text: "Set out how reasonable adjustments are decided and how fitness-to-practise concerns are raised and acted on.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on reasonable adjustments and fitness to practise, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.4). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 2, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles reasonable adjustments and fitness to practise. Frame it for staff as an expectation worded with \"should\", and ask: How are adjustments balanced against fitness to practise with clients? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.5.b1
  forPractitioner: { text: "Check every stage against both its academic level and its professional expectations.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" on the course and its team, on each stage set at the right academic and professional level, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.5, bullet 1). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.5.b2, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles each stage set at the right academic and professional level. Frame it for staff as a requirement worded with \"must\", and ask: What would a student leaving early, or moving on, actually be offered? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.5.b2
  forPractitioner: { text: "Provide non-practitioner exit awards and make clear they do not license practice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on non-practitioner exit awards, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.5, bullet 2). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.5.b1 and qaa/counselling-and-psychotherapy-2022/2.5.b3, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles non-practitioner exit awards. Frame it for staff as an expectation worded with \"should\", and ask: What would a student leaving early, or moving on, actually be offered? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.5.b3
  forPractitioner: { text: "Publish progression routes and keep links with feeder and onward courses.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on clear progression routes, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.5, bullet 3). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.5.b2 and qaa/counselling-and-psychotherapy-2022/2.5.b4, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles clear progression routes. Frame it for staff as an expectation worded with \"should\", and ask: What would a student leaving early, or moving on, actually be offered? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.5.b4
  forPractitioner: { text: "Set up articulation agreements where internal progression is missing.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on articulation routes elsewhere, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.5, bullet 4). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.5.b3 and qaa/counselling-and-psychotherapy-2022/2.5.b5, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles articulation routes elsewhere. Frame it for staff as an expectation worded with \"should\", and ask: What would a student leaving early, or moving on, actually be offered? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.5.b5
  forPractitioner: { text: "Remove gaps between awards so that students can move on without repeating learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on seamless moves between awards, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.5, bullet 5). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.5.b4, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles seamless moves between awards. Frame it for staff as an expectation worded with \"should\", and ask: What would a student leaving early, or moving on, actually be offered? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.6
  forPractitioner: { text: "Plan what each year adds towards the threshold standards, and tell students what a second-class result or better prepares them for.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Each year of your course is expected to build towards the full set of minimum skills you need by the end, and a good second-class degree or better should ready you for postgraduate study.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Write about this as an expectation stated without one of the five obliging words (force recorded as describes) for the honours degree, on progress across the years towards the threshold; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.6). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 2 and the framework descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Bring it up when a student or a course team asks about progress across the years towards the threshold. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation stated without one of the five obliging words (force recorded as describes). Ask: What does each year of the course add towards the final standards? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.7
  forPractitioner: { text: "Make clear which subject and generic skills a joint honours route covers and which it leaves to the partner subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study the subject jointly with another, you will gain some of its specific and general skills and add others from your other subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" for the honours degree, on what joint honours students achieve; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.7). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 2 and the framework descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Bring it up when a student or a course team asks about what joint honours students achieve. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expected feature worded with \"will\". Ask: Which of the subject's skills does a joint route leave out? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/2.9.b1
  forPractitioner: { text: "Consider offering part-time routes alongside full-time ones.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: may, status: drafted }
  author-agent-written: "Write about this as an option worded with \"may\" on the course and its team, on full-time and part-time study, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.9, bullet 1). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.9.b2, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles full-time and part-time study. Frame it for staff as an option worded with \"may\", and ask: Which students does this mode of study open the course to, and who does it shut out? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.9.b2
  forPractitioner: { text: "If you admit with recognition of prior learning, support those it may disadvantage and give clear information on costs, time and failure.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: may, status: drafted }
  author-agent-written: "Write about this as an option worded with \"may\" on the course and its team, on recognition of prior learning, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.9, bullet 2). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.9.b1 and qaa/counselling-and-psychotherapy-2022/2.9.b3, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles recognition of prior learning. Frame it for staff as an option worded with \"may\", and ask: Which students does this mode of study open the course to, and who does it shut out? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.9.b3
  forPractitioner: { text: "Keep some live contact in any delivery mode, or the course cannot gain professional recognition.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: may, status: drafted }
  author-agent-written: "Write about this as an option worded with \"may\" on the course and its team, on face-to-face, blended or hybrid delivery, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.9, bullet 3). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.9.b2, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles face-to-face, blended or hybrid delivery. Frame it for staff as an option worded with \"may\", and ask: Which students does this mode of study open the course to, and who does it shut out? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.10
  forPractitioner: { text: "Put a written agreement in place for every placement, signed by supervisor, course, placement and student.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on a written agreement with placement partners, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.10). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 2, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles a written agreement with placement partners. Frame it for staff as an expectation worded with \"should\", and ask: Does every placement have a signed four-way agreement? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.11
  forPractitioner: { text: "Choose the professional body that fits the modality and align the course with its requirements.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on alignment with a professional body, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.11). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 2, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles alignment with a professional body. Frame it for staff as an expectation worded with \"should\", and ask: Which professional body's requirements does the course follow, and why that one? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.16.b1
  forPractitioner: { text: "Show in the course's monitoring and review cycle where this happens and what changed as a result.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on feedback from students, stakeholders and alumni, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.16, bullet 1). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.16.b2, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles feedback from students, stakeholders and alumni. Frame it for staff as an expectation worded with \"should\", and ask: What changed in the course the last time this source was used? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.16.b2
  forPractitioner: { text: "Show in the course's monitoring and review cycle where this happens and what changed as a result.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on feedback from service users, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.16, bullet 2). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.16.b1 and qaa/counselling-and-psychotherapy-2022/2.16.b3, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles feedback from service users. Frame it for staff as an expectation worded with \"should\", and ask: What changed in the course the last time this source was used? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.16.b3
  forPractitioner: { text: "Show in the course's monitoring and review cycle where this happens and what changed as a result.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on embedding sustainability education, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.16, bullet 3). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.16.b2 and qaa/counselling-and-psychotherapy-2022/2.16.b4, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles embedding sustainability education. Frame it for staff as an expectation worded with \"should\", and ask: What changed in the course the last time this source was used? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.16.b4
  forPractitioner: { text: "Show in the course's monitoring and review cycle where this happens and what changed as a result.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on internal moderation, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.16, bullet 4). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.16.b3 and qaa/counselling-and-psychotherapy-2022/2.16.b5, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles internal moderation. Frame it for staff as an expectation worded with \"should\", and ask: What changed in the course the last time this source was used? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.16.b5
  forPractitioner: { text: "Show in the course's monitoring and review cycle where this happens and what changed as a result.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on external examiners or assessors, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.16, bullet 5). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.16.b4 and qaa/counselling-and-psychotherapy-2022/2.16.b6, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles external examiners or assessors. Frame it for staff as an expectation worded with \"should\", and ask: What changed in the course the last time this source was used? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.16.b6
  forPractitioner: { text: "Show in the course's monitoring and review cycle where this happens and what changed as a result.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on institutional internal review, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.16, bullet 6). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.16.b5 and qaa/counselling-and-psychotherapy-2022/2.16.b7, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles institutional internal review. Frame it for staff as an expectation worded with \"should\", and ask: What changed in the course the last time this source was used? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.16.b7
  forPractitioner: { text: "Show in the course's monitoring and review cycle where this happens and what changed as a result.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on monitoring against professional body requirements, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.16, bullet 7). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.16.b6 and qaa/counselling-and-psychotherapy-2022/2.16.b8, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles monitoring against professional body requirements. Frame it for staff as an expectation worded with \"should\", and ask: What changed in the course the last time this source was used? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.16.b8
  forPractitioner: { text: "Show in the course's monitoring and review cycle where this happens and what changed as a result.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on minuted communication in the teaching team, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.16, bullet 8). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.16.b7 and qaa/counselling-and-psychotherapy-2022/2.16.b9, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles minuted communication in the teaching team. Frame it for staff as an expectation worded with \"should\", and ask: What changed in the course the last time this source was used? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/2.16.b9
  forPractitioner: { text: "Show in the course's monitoring and review cycle where this happens and what changed as a result.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on national surveys and quality exercises, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 2.16, bullet 9). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside qaa/counselling-and-psychotherapy-2022/2.16.b8, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles national surveys and quality exercises. Frame it for staff as an expectation worded with \"should\", and ask: What changed in the course the last time this source was used? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/3.4
  forPractitioner: { text: "Structure the curriculum around the five pillars and show how they connect.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" on the course and its team, on the five pillars of the curriculum, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.4). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 3, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles the five pillars of the curriculum. Frame it for staff as an expected feature worded with \"will\", and ask: Which pillar is weakest in the current course design? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/3.8.b1
  forPractitioner: { text: "Assess emotional competence and warmth in practice, and support students to work through what the work stirs up.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must be able to show emotional competence and warmth, and to work through personal issues that therapy work raises in you.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" for both the honours degree and the master's degree, on emotional competence and warmth; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.8, bullet 1). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/3.8.b2 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about emotional competence and warmth. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as a requirement worded with \"must\". Ask: What has client work stirred up in you, and how did you deal with it? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.8.b2
  forPractitioner: { text: "Look for flexible use of self and skills across different clients.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must be able to use your personal and professional resources creatively to meet many kinds of client.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" for both the honours degree and the master's degree, on using personal resources creatively; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.8, bullet 2). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/3.8.b1 and qaa/counselling-and-psychotherapy-2022/3.8.b3 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about using personal resources creatively. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as a requirement worded with \"must\". Ask: How did you adapt yourself for a client unlike you? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.8.b3
  forPractitioner: { text: "Teach students to name triggers and act on them through supervision or therapy.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must be able to spot what triggers you in client work and deal with it through self-care, supervision or your own therapy.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" for both the honours degree and the master's degree, on personal triggers and how to manage them; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.8, bullet 3). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/3.8.b2 and qaa/counselling-and-psychotherapy-2022/3.8.b4 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about personal triggers and how to manage them. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as a requirement worded with \"must\". Ask: What triggers you in sessions, and what do you do about it? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.8.b4
  forPractitioner: { text: "Give students ways to experience the client's position, such as experiential groups or personal therapy.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must be able to show that you know what being a client feels like, from group work, supervision or your own therapy.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" for both the honours degree and the master's degree, on knowing what it is to be a client; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.8, bullet 4). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/3.8.b3 and qaa/counselling-and-psychotherapy-2022/3.8.b5 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about knowing what it is to be a client. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as a requirement worded with \"must\". Ask: What did being on the client side teach you? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.8.b5
  forPractitioner: { text: "Explore students' life experience and identity and how these enter the work.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must be able to show that you know how your own life and identity can affect the therapy you offer.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" for both the honours degree and the master's degree, on how one's own history affects therapy; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.8, bullet 5). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/3.8.b4 and qaa/counselling-and-psychotherapy-2022/3.8.b6 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about how one's own history affects therapy. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as a requirement worded with \"must\". Ask: Which part of your history most often enters the room? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.8.b6
  forPractitioner: { text: "Assess reflective practice and the use of supervision and personal support throughout placement.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must be able to reflect on yourself and the relationship in all your client work, keep your needs apart from your client's, and use supervision and personal support when you need it.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" for both the honours degree and the master's degree, on reflection, supervision and personal support; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.8, bullet 6). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/3.8.b5 and qaa/counselling-and-psychotherapy-2022/3.8.b7 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about reflection, supervision and personal support. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as a requirement worded with \"must\". Ask: How do you keep your own needs out of the client's session? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.8.b7
  forPractitioner: { text: "Assess how students respond to and act on feedback.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must be able to take responsibility and use feedback well.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" for both the honours degree and the master's degree, on personal responsibility and use of feedback; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.8, bullet 7). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/3.8.b6 and qaa/counselling-and-psychotherapy-2022/3.8.b8 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about personal responsibility and use of feedback. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as a requirement worded with \"must\". Ask: What feedback have you acted on recently? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.8.b8
  forPractitioner: { text: "Ask students to name their limits, power and strengths with evidence.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must be able to recognise your limits, your power and your strengths.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" for both the honours degree and the master's degree, on knowing one's limits, power and strengths; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.8, bullet 8). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/3.8.b7 and qaa/counselling-and-psychotherapy-2022/3.8.b9 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about knowing one's limits, power and strengths. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as a requirement worded with \"must\". Ask: Where do you hold power with clients without meaning to? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.8.b9
  forPractitioner: { text: "Give room for autonomous, creative work in placement and projects.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must be able to build creativity, flexibility, motivation and independence, and work proactively.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" for both the honours degree and the master's degree, on creativity, autonomy and proactive working; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.8, bullet 9). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/3.8.b8 and qaa/counselling-and-psychotherapy-2022/3.8.b10 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about creativity, autonomy and proactive working. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as a requirement worded with \"must\". Ask: When did you take the initiative on placement? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.8.b10
  forPractitioner: { text: "Track professional development across the course.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must be able to show your professional development.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" for both the honours degree and the master's degree, on professional development; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.8, bullet 10). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside qaa/counselling-and-psychotherapy-2022/3.8.b9 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about professional development. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as a requirement worded with \"must\". Ask: How have you grown professionally since you started? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.11
  forPractitioner: { text: "Make sure the course has an assessed, supervised placement as well as the integrated academic, skills and development strands.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" on the course and its team, on an integrated curriculum with an assessed, supervised placement, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.11). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 3, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles an integrated curriculum with an assessed, supervised placement. Frame it for staff as a requirement worded with \"must\", and ask: How is the placement assessed, and by whom? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/3.15
  forPractitioner: { text: "Match the training mode to how students will practise on placement and after, and include core digital training whatever the mode.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on in-person and remote skills and core digital training, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.15). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 3, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles in-person and remote skills and core digital training. Frame it for staff as an expectation worded with \"should\", and ask: Does the way students are trained match the way they will see clients? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/3.16
  forPractitioner: { text: "Check every teaching activity for barriers in advance, and raise equality, diversity and inclusion with staff, students and placements alike.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on inclusive teaching by a diverse team, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.16). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 3, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles inclusive teaching by a diverse team. Frame it for staff as an expectation worded with \"should\", and ask: Which teaching activity was last changed because it excluded someone? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/3.17
  forPractitioner: { text: "Teach the chosen modality's view of human nature and its cultural history as well as its methods; if the course is integrative, set out its components and how they cohere.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should understand how your chosen approach sees human nature and where it comes from culturally, as well as how to use it with clients.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on depth in a modality, its view of people and its heritage; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.17). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 3 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about depth in a modality, its view of people and its heritage. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: Where does your approach come from, and whose experience does it reflect? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.18
  forPractitioner: { text: "Shape training to the needs of the modality and the professional body, while making sure students learn to respect other approaches.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You need to learn about and respect approaches to therapy and mental health other than your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" for both the honours degree and the master's degree, on respect for other approaches and modality-specific training; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.18). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 3 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about respect for other approaches and modality-specific training. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expected feature worded with \"will\". Ask: What do you respect in an approach you would not choose yourself? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.19
  forPractitioner: { text: "Teach the three families of research method, and give each student at least one small study, whether empirical, a systematic case study or a review.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should know the main kinds of research method used in therapy, be able to judge research in your field, and usually carry out at least one small study yourself.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for both the honours degree and the master's degree, on research awareness and methods; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.19). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 3 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about research awareness and methods. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: What small study could you carry out on your own practice? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.20
  forPractitioner: { text: "Build personal development into every course, using groups, journals, residentials or personal therapy as suits the modality.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" on the course and its team, on provision for personal development, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.20). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 3, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles provision for personal development. Frame it for staff as an expected feature worded with \"will\", and ask: What does the course require for personal development, and why that? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/3.21
  forPractitioner: { text: "Vet placements and supervisors, require regular supervision, and set out how placement evidence counts towards assessment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on placements, supervision and their oversight, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.21). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 3, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles placements, supervision and their oversight. Frame it for staff as an expectation worded with \"should\", and ask: How do you know a placement's supervision is good enough? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/3.22
  forPractitioner: { text: "Set and justify staff to student ratios for experiential work, keeping skills classes small enough for observation and feedback.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" on the course and its team, on qualified staff and suitable staff to student ratios, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.22). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 3, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles qualified staff and suitable staff to student ratios. Frame it for staff as a requirement worded with \"must\", and ask: What is the ratio in skills practice sessions, and how is it justified? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/3.23
  forPractitioner: { text: "Weight practitioner competence heavily in assessment and make a satisfactory level a condition of the award.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your assessment will cover both theory and skills, and you will need to reach a satisfactory level of practice competence to get your award.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" for both the honours degree and the master's degree, on assessing theory and practice competence for the award; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.23). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 3 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about assessing theory and practice competence for the award. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expected feature worded with \"will\". Ask: What would show that a student is ready to practise the day after the award? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/3.25
  forPractitioner: { text: "Write criteria that cover core counselling skills and wider professional skills, and make assessments inclusive and authentic.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on inclusive, authentic assessment and its criteria, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.25). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 3, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles inclusive, authentic assessment and its criteria. Frame it for staff as an expectation worded with \"should\", and ask: Do the criteria assess risk awareness and ethical judgement, or only core skills? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/3.26
  forPractitioner: { text: "Involve external examiners, placements and employers in designing and reviewing assessment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on quality assurance of assessment, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.26). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 3, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles quality assurance of assessment. Frame it for staff as an expectation worded with \"should\", and ask: Who outside the team has looked at the assessments this year? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/3.27
  forPractitioner: { text: "Put a formal readiness check on skills, knowledge and resilience before any student sees clients.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Before you can work with real clients on placement, you must be assessed on your skills, knowledge and personal resilience.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" for both the honours degree and the master's degree, on readiness assessed before client work; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 3.27). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 3 and the framework descriptor the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student or a course team asks about readiness assessed before client work. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as a requirement worded with \"must\". Ask: What does the course check before a student sees a first client? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/4.2
  forPractitioner: { text: "Use Annex D alongside your own marking schemes to judge performance above the threshold.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on Annex D for achievement above the threshold, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.2). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 4, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles Annex D for achievement above the threshold. Frame it for staff as an expectation worded with \"should\", and ask: How do your marking criteria line up with Annex D's descriptions of each class? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/4.4
  forPractitioner: { text: "Assess every threshold standard before the award; competence in each is expected, not an average across them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be competent in every part of the minimum standard for safe, ethical and effective practice, not just most of it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, on competence in every part of the standard before completion; it sits outside the rung lists of section 4. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.4). Do not claim it is a regulatory requirement or part of the threshold standard itself. Set it beside the statement's section 4 and the framework descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Bring it up when a student or a course team asks about competence in every part of the standard before completion. Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as an expectation worded with \"should\". Ask: Which part of the standard is least well evidenced for this student? Avoid long quotation of the issuer's text."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b1
  forPractitioner: { text: "Teach the philosophical roots of the main approaches and research paradigms, and ask students to judge what those roots mean for multidisciplinary teamwork.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand how the beliefs underneath each approach shape research and practice, and you can judge what that means when you work with other professions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on philosophical assumptions behind research and practice. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b2 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on philosophical assumptions behind research and practice by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which assumptions about people sit underneath the approach you are training in? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b2
  forPractitioner: { text: "Have students test professional codes and agency policies against cases, including the parts on diversity and equal opportunity, and then apply them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can weigh up the codes and policies that govern your practice, including those on diversity and equality, and use them in real situations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on professional codes and organisational policies. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b1 and qaa/counselling-and-psychotherapy-2022/4.6.b3 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on professional codes and organisational policies by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which part of your professional code have you had to apply in a real decision? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b3
  forPractitioner: { text: "Include current policy and national clinical guidance in the curriculum, and ask students to trace their effects on services, research and clients.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know how government policy and national guidance, such as NICE guidelines, shape therapy services, research and the care clients receive.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on government policy and guidance such as NICE. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b2 and qaa/counselling-and-psychotherapy-2022/4.6.b4 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on government policy and guidance such as NICE by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How does a current national guideline affect which therapies clients can get? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b4
  forPractitioner: { text: "Use group work, placement and case material to help students name power dynamics and reflect on their effect on outcomes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can spot how power works in relationships, groups, organisations and therapy, and think about how it changes what happens.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on power in relationships, groups and organisations. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b3 and qaa/counselling-and-psychotherapy-2022/4.6.b5 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on power in relationships, groups and organisations by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Where did you notice power shaping a group or session you were part of? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b5
  forPractitioner: { text: "Give students space to debate the profession's role, value and current challenges.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You think carefully about what therapy does for society today and the pressures it faces.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on the profession's place in society. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b4 and qaa/counselling-and-psychotherapy-2022/4.6.b6 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on the profession's place in society by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What do you see as the biggest challenge facing the profession now? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b6
  forPractitioner: { text: "Use personal development groups and supervision for students to question their own values and trace their effect on client work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You question and reflect on your own values, beliefs and habits, and on how they affect your work with clients.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on examining one's own values and their effect on therapy. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b5 and qaa/counselling-and-psychotherapy-2022/4.6.b7 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on examining one's own values and their effect on therapy by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which of your values has most shaped how you respond to clients? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b7
  forPractitioner: { text: "Help students map their duties to each party, and use placement to show them acting on those duties.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can see where your professional responsibilities lie, to clients, employers, trainers, the profession and society, and you act on them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on professional responsibility to all parties. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b6 and qaa/counselling-and-psychotherapy-2022/4.6.b8 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on professional responsibility to all parties by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: When have two of these responsibilities pulled you in different directions? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b8
  forPractitioner: { text: "Make openness to difference something students show in practice and reflect on, going beyond the legally protected characteristics.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You are open to and welcome difference in every client, whatever their identity, not only in the ways the law protects.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on openness to diversity and to every client's rights. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b7 and qaa/counselling-and-psychotherapy-2022/4.6.b9 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on openness to diversity and to every client's rights by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which aspects of identity do you find harder to stay open to, and why? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b9
  forPractitioner: { text: "Ask students to locate their placement practice in its social, cultural and political context and show that they work with it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You work with awareness of the social, cultural and political setting of your practice and of the profession.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on working within the social and political context. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b8 and qaa/counselling-and-psychotherapy-2022/4.6.b10 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on working within the social and political context by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How does the community your placement serves shape the work you do there? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b10
  forPractitioner: { text: "Assess how students collaborate with supervisors and other professionals on placement, including any contribution to how the service develops.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You build and keep working relationships with your supervisor and other professionals, and use them to support your client work and help the service improve.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on collaboration with supervisors and other professionals. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b9 and qaa/counselling-and-psychotherapy-2022/4.6.b11 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on collaboration with supervisors and other professionals by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Who outside therapy have you worked with on a client's behalf, and how did it go? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b11
  forPractitioner: { text: "Require students to appraise studies and show, in case work, how research informs what they do with clients.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can judge published research critically and let a sound, research-based understanding guide your work every time.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on using research in practice. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b10 and qaa/counselling-and-psychotherapy-2022/4.6.b12 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on using research in practice by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which study has changed something you do with clients? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b12
  forPractitioner: { text: "Look for evidence that students act on equality and challenge prejudice, not only discuss it, on placement and in course life.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You actively promote equality and inclusion in your work and challenge discrimination and prejudice where you meet it, including in organisations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on promoting equality and challenging discrimination. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b11 and qaa/counselling-and-psychotherapy-2022/4.6.b13 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on promoting equality and challenging discrimination by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: When have you challenged something unfair in a setting you worked in? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b13
  forPractitioner: { text: "Help students plan the academic, therapeutic and digital skills they will need to shape their own careers.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You build the academic, therapeutic and digital skills to shape a rewarding career of your own choosing.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on competencies for a self-directed professional life. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b12 and qaa/counselling-and-psychotherapy-2022/4.6.b14 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on competencies for a self-directed professional life by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What does a rewarding professional life look like for you in five years? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.6.b14
  forPractitioner: { text: "Expose students to change, such as a move to remote work, and assess how they adapt.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can adjust sensibly when your setting changes or when things are uncertain.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on adapting to change and uncertainty. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.6, Professional context, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.6.b13 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on adapting to change and uncertainty by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How did you cope the last time your placement or plans changed suddenly? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.7.b1
  forPractitioner: { text: "Teach biomedical, psychological, social, political and cultural accounts of distress side by side, with the client's own account at the centre.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand several ways of explaining mental distress, from medical to social and cultural, and you keep the client's own view at the centre.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on models of mental distress. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.7, Understanding people and their experiences, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.7.b2 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on models of mental distress by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How would a medical account and a social account explain the same client's distress? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.7.b2
  forPractitioner: { text: "Ask students to name cases where their core model struggles and say what they would do about it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can see where your chosen approach may not fit a particular client and look for ways to make up for that.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on the limits of one's chosen model. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.7, Understanding people and their experiences, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.7.b1 and qaa/counselling-and-psychotherapy-2022/4.7.b3 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on the limits of one's chosen model by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: With which kind of client does your approach work least well? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.7.b3
  forPractitioner: { text: "Bring in other professions' views of mental health and ask students to engage with them respectfully.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You recognise and respect other views on mental health, including those of other professions and agencies.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on other professional perspectives on mental health. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.7, Understanding people and their experiences, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.7.b2 and qaa/counselling-and-psychotherapy-2022/4.7.b4 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on other professional perspectives on mental health by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How does a psychiatrist's view of a client differ from yours? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.7.b4
  forPractitioner: { text: "Ask students to analyse a service in its policy and economic setting and judge how those forces shape practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand what therapy services do in society and can think critically about how money, politics and social change shape them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on the social role of mental health services. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.7, Understanding people and their experiences, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.7.b3 and qaa/counselling-and-psychotherapy-2022/4.7.b5 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on the social role of mental health services by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How has funding shaped the therapy offered where you are on placement? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.7.b5
  forPractitioner: { text: "Compare how several approaches treat the relationship and link each to practice with clients and colleagues.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand and can compare how different approaches think about the relationship, and what that means for your work with clients and colleagues.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on the relationship across theoretical approaches. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.7, Understanding people and their experiences, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.7.b4 and qaa/counselling-and-psychotherapy-2022/4.7.b6 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on the relationship across theoretical approaches by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How does your approach's idea of the relationship shape what you do in a first session? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.7.b6
  forPractitioner: { text: "Encourage students to learn from approaches other than their own and show that openness with peers and clients.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You are open to approaches other than your own, which helps you work well with colleagues and build alliances with clients.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on openness to other approaches for good working relationships. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.7, Understanding people and their experiences, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.7.b5 and qaa/counselling-and-psychotherapy-2022/4.7.b7 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on openness to other approaches for good working relationships by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What have you learned from a colleague who works in a different way? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.7.b7
  forPractitioner: { text: "Use reflective tasks and supervision for students to name their biases and watch for unconscious ones across the full range of identities.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You are aware of your own biases and alert to hidden ones about people's identity, background, ability, sexuality or faith.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on awareness of one's own and unconscious bias. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.7, Understanding people and their experiences, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.7.b6 and qaa/counselling-and-psychotherapy-2022/4.7.b8 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on awareness of one's own and unconscious bias by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which bias of yours surprised you when you first noticed it? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.7.b8
  forPractitioner: { text: "Teach a repertoire of evidence-based interventions and assess whether students choose among them with the client's needs and wishes in mind.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You use a range of research-based responses and techniques, chosen with care for what each client needs and wants.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on research-informed responses that respect client preference. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.7, Understanding people and their experiences, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.7.b7 and qaa/counselling-and-psychotherapy-2022/4.7.b9 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on research-informed responses that respect client preference by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How did a client's preference change the intervention you chose? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.7.b9
  forPractitioner: { text: "Make bias a standing item in supervision and reflective logs, and look for evidence that students act on what they find.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You use supervision and reflection to notice your own bias and check your work for hidden bias, so that your practice treats every client fairly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on using supervision to check bias. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.7, Understanding people and their experiences, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.7.b8 and qaa/counselling-and-psychotherapy-2022/4.7.b10 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on using supervision to check bias by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What did supervision help you see about your own bias? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.7.b10
  forPractitioner: { text: "Help students identify their own enterprising strengths in therapy settings and plan how to use them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know your own enterprising strengths in therapy work and have the drive to use them as situations change.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on enterprising capabilities in therapeutic work. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.7, Understanding people and their experiences, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.7.b9 and qaa/counselling-and-psychotherapy-2022/4.7.b11 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on enterprising capabilities in therapeutic work by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Where have you shown initiative in setting up or improving a service? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.7.b11
  forPractitioner: { text: "Assess initiative and independent judgement on placement and in projects.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You show initiative, work independently and take responsibility.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on initiative, autonomy and responsibility. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.7, Understanding people and their experiences, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.7.b10 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on initiative, autonomy and responsibility by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: When did you act on your own judgement without waiting to be told? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.8.b1
  forPractitioner: { text: "Ask students to assess their own strengths and limits with evidence from practice and feedback.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know your strengths and limits as a person and as a practitioner, and how they affect your work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on one's own strengths and limits. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.8, The therapist, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.8.b2 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on one's own strengths and limits by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which limit of yours most needs watching in client work? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.8.b2
  forPractitioner: { text: "Have students write and review a self-care plan, and check it in supervision.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know what you need to stay well and have workable ways to look after yourself.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on self-care needs and strategies. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.8, The therapist, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.8.b1 and qaa/counselling-and-psychotherapy-2022/4.8.b3 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on self-care needs and strategies by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What tells you that you need to step back and look after yourself? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.8.b3
  forPractitioner: { text: "Use case discussion to rehearse referral decisions and the routes available.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can tell when it is right to refer a client to another service.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on when to refer on. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.8, The therapist, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.8.b2 and qaa/counselling-and-psychotherapy-2022/4.8.b4 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on when to refer on by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What would make you refer a client on rather than keep working with them? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.8.b4
  forPractitioner: { text: "Make the use of supervision visible in assessment, not only the hours logged.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You use supervision as a central part of your practice, for your clients' sake and for your own growth.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on supervision as central to practice. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.8, The therapist, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.8.b3 and qaa/counselling-and-psychotherapy-2022/4.8.b5 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on supervision as central to practice by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What do you bring to supervision, and what do you hold back? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.8.b5
  forPractitioner: { text: "Teach self-supervision methods and ask students to show them in process notes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can supervise yourself, questioning your own values and habits and how they affect your work with clients.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on self-supervision. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.8, The therapist, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.8.b4 and qaa/counselling-and-psychotherapy-2022/4.8.b6 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on self-supervision by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How do you check your own reactions between sessions? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.8.b6
  forPractitioner: { text: "Track personal and professional development through the course and treat fitness to practise as an ongoing matter.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You stay committed to your own development, personal and professional, including your self-awareness and fitness to practise.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on commitment to ongoing development and fitness to practise. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.8, The therapist, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.8.b5 and qaa/counselling-and-psychotherapy-2022/4.8.b7 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on commitment to ongoing development and fitness to practise by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What will you do to keep developing once the course ends? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.8.b7
  forPractitioner: { text: "Make routes to personal therapy and support clear, and help students judge when to use them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can tell when you need personal support or therapy and you take it up.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on personal support or therapy. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.8, The therapist, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.8.b6 and qaa/counselling-and-psychotherapy-2022/4.8.b8 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on personal support or therapy by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How would you know it was time to seek therapy for yourself? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.8.b8
  forPractitioner: { text: "Look for evidence that students use supervision to learn and to protect themselves, not only to report cases.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You use supervision to understand your practice better and to protect your own well-being.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on supervision for understanding and well-being. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.8, The therapist, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.8.b7 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on supervision for understanding and well-being by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: When did supervision help you stay well during difficult work? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b1
  forPractitioner: { text: "Cover the ethical and legal ground in the points that follow explicitly and check it in assessment.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand the main ethical and legal rules your practice works within.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on the ethical and legal contexts of practice. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b2 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on the ethical and legal contexts of practice by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which law has the biggest effect on your day-to-day practice? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b2
  forPractitioner: { text: "Teach the law on data and child protection with its devolved variations and the international issues of online work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know the legal principles that affect your practice, such as data and child protection, including how they differ across the UK and abroad when you work online.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on law relevant to practice, including online work. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b1 and qaa/counselling-and-psychotherapy-2022/4.9.b3 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on law relevant to practice, including online work by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What changes legally if your online client lives in another nation? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b3
  forPractitioner: { text: "Teach the main professional codes and the requirements they set, such as for supervision, and compare them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know the ethical codes and guidance of the professional associations and what they require of you, for example in supervision.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on ethical frameworks and professional requirements. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b2 and qaa/counselling-and-psychotherapy-2022/4.9.b4 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on ethical frameworks and professional requirements by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What does your professional body require of you in supervision? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b4
  forPractitioner: { text: "Ask students to learn and use their placement agency's policies.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know the policies and procedures of the agency you work in.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on agency policies and procedures. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b3 and qaa/counselling-and-psychotherapy-2022/4.9.b5 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on agency policies and procedures by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which agency policy have you had to follow most often? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b5
  forPractitioner: { text: "Teach students where to find updates on law and ethics and how to keep their practice current.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You keep up with changes in law and guidance and know where to look so your practice stays current.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on keeping up with changes in law and guidance. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b4 and qaa/counselling-and-psychotherapy-2022/4.9.b6 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on keeping up with changes in law and guidance by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Where would you check for a change in the law that affects you? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b6
  forPractitioner: { text: "Rehearse confidentiality breaches through cases, with clear lines on what must be passed on and to whom.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know what it means to have to break confidentiality, and you are clear what you must pass on and to whom.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on breaching confidentiality. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b5 and qaa/counselling-and-psychotherapy-2022/4.9.b7 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on breaching confidentiality by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: In what situation would you have to break confidentiality, and who would you tell? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b7
  forPractitioner: { text: "Teach at least one decision-making model and have students apply it to dilemmas.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand at least one model for making ethical decisions in therapy and can use it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on a model of ethical decision-making. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b6 and qaa/counselling-and-psychotherapy-2022/4.9.b8 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on a model of ethical decision-making by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How would you use a decision-making model on a real dilemma? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b8
  forPractitioner: { text: "Ask students to show how core ethical principles guide their placement decisions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You are committed to working ethically, guided by justice, integrity, trust, doing good, avoiding harm and caring for yourself.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on commitment to ethical principles. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b7 and qaa/counselling-and-psychotherapy-2022/4.9.b9 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on commitment to ethical principles by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which ethical principle do you find hardest to hold to in practice? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b9
  forPractitioner: { text: "Require students to name the code they work under and show its principles in their decisions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You work under a named ethical code and act thoughtfully in line with its principles.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on working within a named code. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b8 and qaa/counselling-and-psychotherapy-2022/4.9.b10 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on working within a named code by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which code do you work under, and how did it shape a recent decision? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b10
  forPractitioner: { text: "Use real or simulated dilemmas and assess how students reason through them with supervisory input.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can analyse and think through ethical dilemmas that come up in practice, drawing on your supervisor or others when needed.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on ethical dilemmas in practice. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b9 and qaa/counselling-and-psychotherapy-2022/4.9.b11 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on ethical dilemmas in practice by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Tell me about a dilemma you took to supervision. Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b11
  forPractitioner: { text: "Check placement settings and students' risk practice for the safety of both client and therapist.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You provide therapy with care for your client's safety and your own, and for whether the setting is right.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on safety of client, therapist and setting. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b10 and qaa/counselling-and-psychotherapy-2022/4.9.b12 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on safety of client, therapist and setting by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What do you check about a room or platform before a session? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b12
  forPractitioner: { text: "Assess the quality of students' notes as part of practice competence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You keep careful records, knowing they matter for the quality and safety of therapy.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on diligent record-keeping. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b11 and qaa/counselling-and-psychotherapy-2022/4.9.b13 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on diligent record-keeping by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What makes a good session note? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b13
  forPractitioner: { text: "Teach the legal and governance rules for records, including clients' rights of access.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You handle records in line with the law, professional standards and your clients' legal rights.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on records and the law. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b12 and qaa/counselling-and-psychotherapy-2022/4.9.b14 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on records and the law by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What rights does a client have to see their notes? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b14
  forPractitioner: { text: "Cover the full record cycle, from writing to secure disposal, and check it on placement.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You handle records properly from start to finish: accurate notes, safe storage, careful sharing and secure disposal.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on the life cycle of records. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b13 and qaa/counselling-and-psychotherapy-2022/4.9.b15 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on the life cycle of records by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How long do you keep notes, and how do you dispose of them? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b15
  forPractitioner: { text: "Include online practice in teaching on ethics and law, and assess students' handling of it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You handle the practical, ethical and legal demands of working online and of any contact with clients through technology.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on demands of online and technology-mediated work. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b14 and qaa/counselling-and-psychotherapy-2022/4.9.b16 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on demands of online and technology-mediated work by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What extra steps do you take when a session is online? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b16
  forPractitioner: { text: "Teach contracting on confidentiality and data for in-person and remote work, and assess it in practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You agree with clients how confidentiality and data protection work in your setting, staying within ethical and legal limits.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on contracting on confidentiality and data across settings. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b15 and qaa/counselling-and-psychotherapy-2022/4.9.b17 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on contracting on confidentiality and data across settings by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How do you explain confidentiality to a new client? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b17
  forPractitioner: { text: "Check that students state confidentiality limits clearly, including for remote work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You make clear to clients where confidentiality ends, including when you work remotely.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on limits to confidentiality, including remotely. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b16 and qaa/counselling-and-psychotherapy-2022/4.9.b18 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on limits to confidentiality, including remotely by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Where does confidentiality end when you work by video? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b18
  forPractitioner: { text: "Give students a checklist for advising clients on safe remote set-ups.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can tell clients how to stay safe with their data, devices, platform and surroundings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on helping clients stay safe with data and platforms. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b17 and qaa/counselling-and-psychotherapy-2022/4.9.b19 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on helping clients stay safe with data and platforms by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What would you tell a client about where to sit for an online session? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b19
  forPractitioner: { text: "Review platforms with students for accessibility and security, and keep this current.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know the main digital platforms and tools for therapy, how accessible they are, and where their security falls short.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on digital platforms, accessibility and security. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b18 and qaa/counselling-and-psychotherapy-2022/4.9.b20 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on digital platforms, accessibility and security by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What makes one video platform safer than another? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b20
  forPractitioner: { text: "Include recording in contracting role-plays.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You agree carefully with clients about any recording of sessions and can explain what it means.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on agreements on recording sessions. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b19 and qaa/counselling-and-psychotherapy-2022/4.9.b21 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on agreements on recording sessions by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What would you say if a client asked to record a session? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b21
  forPractitioner: { text: "Teach students to tailor privacy discussions to each client's situation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You talk through data security and privacy with clients you see remotely, taking account of their situation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on data security in remote work. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b20 and qaa/counselling-and-psychotherapy-2022/4.9.b22 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on data security in remote work by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Who else might overhear your client at home? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b22
  forPractitioner: { text: "Agree with students a plan for dropped connections and rehearse it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You keep the therapeutic relationship safe and steady when the technology breaks down.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on when technology fails. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b21 and qaa/counselling-and-psychotherapy-2022/4.9.b23 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on when technology fails by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What is your plan if the call drops at a difficult moment? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.9.b23
  forPractitioner: { text: "Value creative problem-solving in case work, alongside rule-based ethics.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You use your judgement and find creative ways to handle problems and dilemmas, with integrity and compassion.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on creative responses to dilemmas. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.9, Ethical/legal, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.9.b22 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on creative responses to dilemmas by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: When has a rule not been enough, and what did you do? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b1
  forPractitioner: { text: "Teach boundaries across all the relationships of training, not only those with clients.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand what safe, responsive boundaries look like with clients, supervisors, tutors, colleagues and employers.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on safe boundaries in all professional relationships. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b2 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on safe boundaries in all professional relationships by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Where are boundaries hardest for you: with clients, tutors or colleagues? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b2
  forPractitioner: { text: "Use cases of breaches, small and large, for students to learn the warning signs.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You think about how to spot when a boundary is crossed, so you can keep clear limits and work safely.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on recognising boundary breaches. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b1 and qaa/counselling-and-psychotherapy-2022/4.10.b3 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on recognising boundary breaches by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What early signs might tell you a boundary is slipping? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b3
  forPractitioner: { text: "Have students draft and critique a therapeutic contract.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know why contracting matters ethically and what a therapeutic contract is for and should include.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on contracting and the therapeutic contract. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b2 and qaa/counselling-and-psychotherapy-2022/4.10.b4 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on contracting and the therapeutic contract by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What are the parts of your contract with clients, and why each? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b4
  forPractitioner: { text: "Discuss cases where flexibility and firmness pull against each other.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand how complicated boundaries can be, and keep them responsive while staying safe and ethical.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on responsive boundaries that keep practice safe. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b3 and qaa/counselling-and-psychotherapy-2022/4.10.b5 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on responsive boundaries that keep practice safe by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: When did you bend a boundary, and was it right? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b5
  forPractitioner: { text: "Include employment law and policy in teaching on service settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand how employment law and policy affect therapy work in voluntary, community, public and private settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on employment law across sectors. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b4 and qaa/counselling-and-psychotherapy-2022/4.10.b6 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on employment law across sectors by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How does being employed differ from being self-employed for a therapist, in law? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b6
  forPractitioner: { text: "Teach sexual dynamics in therapy directly, with clear guidance on preventing violations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand the risks when sexual issues or feelings arise in therapy and use that to keep boundaries safe.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on sexual dynamics and boundary violations. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b5 and qaa/counselling-and-psychotherapy-2022/4.10.b7 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on sexual dynamics and boundary violations by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How would you handle feelings of attraction in the therapy room? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b7
  forPractitioner: { text: "Prepare students for common difficulties before placement.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You are aware of the difficulties that can come up in therapy.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on awareness of challenges in the work. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b6 and qaa/counselling-and-psychotherapy-2022/4.10.b8 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on awareness of challenges in the work by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What challenge are you least prepared for? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b8
  forPractitioner: { text: "Assess how students respond to shifts in the relationship without losing boundaries.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You respond with confidence when the relationship changes or gets difficult, while keeping clear boundaries.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on confidence with change while holding boundaries. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b7 and qaa/counselling-and-psychotherapy-2022/4.10.b9 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on confidence with change while holding boundaries by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How did you respond when a client tested a boundary? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b9
  forPractitioner: { text: "Include contact after ending in teaching on boundaries.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You set and keep proper boundaries throughout therapy and after it ends.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on boundaries during and after therapy. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b8 and qaa/counselling-and-psychotherapy-2022/4.10.b10 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on boundaries during and after therapy by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What would you do if you met a former client socially? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b10
  forPractitioner: { text: "Ask students to show how they used the contract in the work, not only that they had one.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You use the limits and benefits of your contract with clients as part of the therapy.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on using the therapeutic contract. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b9 and qaa/counselling-and-psychotherapy-2022/4.10.b11 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on using the therapeutic contract by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: When did the contract itself become useful in the work? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b11
  forPractitioner: { text: "Teach online boundaries, including social media, as part of professional conduct.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You set and keep proper boundaries with clients online, as the points that follow describe.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on online boundaries with clients. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b10 and qaa/counselling-and-psychotherapy-2022/4.10.b12 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on online boundaries with clients by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What would you do if a client found you on social media? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b12
  forPractitioner: { text: "Review students' social media practice as part of professional readiness.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You take care to keep your personal and professional social media apart, so that clients cannot be harmed by a dual relationship.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on separating personal and professional presence online. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b11 and qaa/counselling-and-psychotherapy-2022/4.10.b13 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on separating personal and professional presence online by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What can a client see about you online today? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b13
  forPractitioner: { text: "Check students' public posts and profiles against their code.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You make sure anything you post publicly online fits your ethical code.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on public online communication. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b12 and qaa/counselling-and-psychotherapy-2022/4.10.b14 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on public online communication by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Does your public profile fit your ethical code? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b14
  forPractitioner: { text: "Teach the elements of the frame and assess how students hold it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You create and hold a secure frame for the work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on a secure frame for the work. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b13 and qaa/counselling-and-psychotherapy-2022/4.10.b15 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on a secure frame for the work by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What makes up the frame of your sessions? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b15
  forPractitioner: { text: "Assess contracting in recorded or observed practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You agree a suitable contract with each client, using everything you know about them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on negotiating the contract. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b14 and qaa/counselling-and-psychotherapy-2022/4.10.b16 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on negotiating the contract by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What information shaped the last contract you agreed? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b16
  forPractitioner: { text: "Teach planning for breaks, including emergency cover for clients.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You plan for breaks and holidays, notice how they affect the work, and make sure clients can get help in an emergency.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on breaks, holidays and emergency cover. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b15 and qaa/counselling-and-psychotherapy-2022/4.10.b17 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on breaks, holidays and emergency cover by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How do you prepare a client for your holiday? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b17
  forPractitioner: { text: "Require students to have arrangements in place, such as a clinical will, while on placement.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You have arrangements in place in case you suddenly cannot work, and you tell your clients about them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on arrangements for a sudden ending. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b16 and qaa/counselling-and-psychotherapy-2022/4.10.b18 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on arrangements for a sudden ending by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Who would contact your clients if you were taken ill tomorrow? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b18
  forPractitioner: { text: "Give students experience of both time-limited and open-ended work where possible.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You adjust your work to fit both open-ended and time-limited contracts.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on open-ended and time-limited work. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b17 and qaa/counselling-and-psychotherapy-2022/4.10.b19 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on open-ended and time-limited work by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How does a six-session limit change the way you work? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b19
  forPractitioner: { text: "Teach the protocols for liaising with other agencies, with consent.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You handle contact with outside agencies and professionals in your client's interest.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on contact with outside agencies. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b18 and qaa/counselling-and-psychotherapy-2022/4.10.b20 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on contact with outside agencies by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: When would you contact a client's GP, and with whose consent? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.10.b20
  forPractitioner: { text: "Encourage students to treat professional problems as questions to explore.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You meet professional challenges with curiosity, a critical eye and a view to the future, mindful of your responsibilities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on an enquiring, forward-looking stance. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.10, Boundaries and contracting, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.10.b19 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on an enquiring, forward-looking stance by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What professional question are you curious about right now? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b1
  forPractitioner: { text: "Teach client assessment as a topic in its own right.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand what client assessment is and how it is done, as the points that follow set out.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on client assessment concepts and processes. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b2 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on client assessment concepts and processes by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What do you assess in a first meeting with a client? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b2
  forPractitioner: { text: "Ask students to define assessment in the terms of their own model.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can define and explain what client assessment means.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on defining client assessment. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b1 and qaa/counselling-and-psychotherapy-2022/4.11.b3 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on defining client assessment by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How would you explain assessment to a new client? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b3
  forPractitioner: { text: "Debate outcome measures from several viewpoints, drawing on research.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand the arguments about assessment tools and outcome measures and can judge from research what they mean for practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on perspectives on assessment tools and outcome measures. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b2 and qaa/counselling-and-psychotherapy-2022/4.11.b4 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on perspectives on assessment tools and outcome measures by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What do outcome measures capture, and what do they miss? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b4
  forPractitioner: { text: "Compare assessment across settings, with their legal and policy frames.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can discuss critically where and how assessment happens, with attention to ethics, law and agency rules.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on contexts of assessment, law and agency policy. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b3 and qaa/counselling-and-psychotherapy-2022/4.11.b5 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on contexts of assessment, law and agency policy by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How does assessment differ between your placement and private practice? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b5
  forPractitioner: { text: "Require students to use and explain an assessment approach consistent with their core model.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know at least one way of assessing that fits your approach and can explain how it shapes your work with a client.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on an assessment approach that fits one's model. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b4 and qaa/counselling-and-psychotherapy-2022/4.11.b6 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on an assessment approach that fits one's model by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How does your way of assessing shape what you agree to work on? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b6
  forPractitioner: { text: "Teach screening for remote work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand why some clients may not be suited to therapy online or by phone.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on suitability for technology-mediated therapy. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b5 and qaa/counselling-and-psychotherapy-2022/4.11.b7 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on suitability for technology-mediated therapy by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which clients might you not see online, and why? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b7
  forPractitioner: { text: "Teach risk and protective factors with current evidence and practice cases.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand what raises and lowers a client's risk of harming themselves.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on risk and protective factors for client safety. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b6 and qaa/counselling-and-psychotherapy-2022/4.11.b8 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on risk and protective factors for client safety by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What protective factors would you look for with a client at risk? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b8
  forPractitioner: { text: "Train students to tell thoughts from intent in risk assessment.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand the difference between having thoughts of suicide and intending to act, and why it matters for judging risk.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on thoughts and intent in judging risk. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b7 and qaa/counselling-and-psychotherapy-2022/4.11.b9 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on thoughts and intent in judging risk by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What questions help you tell thoughts apart from intent? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b9
  forPractitioner: { text: "Rehearse the procedures for immediate risk, including whom to contact.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know the legal and procedural steps to take when a client is at immediate risk.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on responding to immediate risk. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b8 and qaa/counselling-and-psychotherapy-2022/4.11.b10 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on responding to immediate risk by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What would you do, step by step, if a client was at immediate risk? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b10
  forPractitioner: { text: "Signpost specialist training routes and the limits of a generic qualification.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You recognise that some client groups need extra knowledge and training, especially where capacity or understanding is in question.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on extra training for particular client groups. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b9 and qaa/counselling-and-psychotherapy-2022/4.11.b11 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on extra training for particular client groups by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which client group would you need more training to work with? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b11
  forPractitioner: { text: "Ask students to map their competence across groups and modes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know where your competence lies with different client groups, techniques and ways of delivering therapy.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on one's own competence across groups and modes. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b10 and qaa/counselling-and-psychotherapy-2022/4.11.b12 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on one's own competence across groups and modes by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Where does your competence stop? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b12
  forPractitioner: { text: "Present competing views of assessment and formulation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You are critically aware of the different views on assessment and formulation, as the points that follow set out.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on perspectives on assessment and formulation. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b11 and qaa/counselling-and-psychotherapy-2022/4.11.b13 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on perspectives on assessment and formulation by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Is formulation helpful or harmful in your approach? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b13
  forPractitioner: { text: "Hold a debate on formal assessment in therapy.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand the arguments for and against formal assessment and formulation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on arguments for and against formal assessment. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b12 and qaa/counselling-and-psychotherapy-2022/4.11.b14 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on arguments for and against formal assessment by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which side of the argument convinces you more? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b14
  forPractitioner: { text: "Ask students to reflect on how assessment practice affects clients.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You reflect critically on how these views shape services and what clients go through.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on how these views shape services and experience. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b13 and qaa/counselling-and-psychotherapy-2022/4.11.b15 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on how these views shape services and experience by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How might a formal assessment feel from the client's chair? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b15
  forPractitioner: { text: "Assess a written or spoken account of each student's own approach.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can set out your own coherent approach, including how you assess and work with what clients bring.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on a personal approach to assessment. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b14 and qaa/counselling-and-psychotherapy-2022/4.11.b16 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on a personal approach to assessment by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How would you describe your approach in two minutes? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b16
  forPractitioner: { text: "Encourage students to name limits early in supervision.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You are aware of where your training and experience fall short in complex or risky work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on the limits of one's training in complex work. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b15 and qaa/counselling-and-psychotherapy-2022/4.11.b17 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on the limits of one's training in complex work by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What kind of case would you hand on? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b17
  forPractitioner: { text: "Have students map local support and referral options.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You know the support and referral networks available to your clients.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on support and referral networks. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b16 and qaa/counselling-and-psychotherapy-2022/4.11.b18 and the descriptor qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on support and referral networks by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Where could you refer a client locally? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b18
  forPractitioner: { text: "Assess how students open the work and explain therapy to clients.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can talk through a client's concerns with them and explain how therapy could help.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on discussing the client's concerns and how therapy helps. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b17 and qaa/counselling-and-psychotherapy-2022/4.11.b19 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on discussing the client's concerns and how therapy helps by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How do you explain what therapy can offer? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b19
  forPractitioner: { text: "Teach capacity checks within assessment.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You judge whether each client can engage with and use the therapy you offer, in the setting it is offered in.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on client competence and capacity for the approach. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b18 and qaa/counselling-and-psychotherapy-2022/4.11.b20 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on client competence and capacity for the approach by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How would you know a client cannot use what you offer? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b20
  forPractitioner: { text: "Assess the clarity of students' explanations to clients.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You explain your approach clearly, including what you and the client each bring.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on explaining the approach and each role. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b19 and qaa/counselling-and-psychotherapy-2022/4.11.b21 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on explaining the approach and each role by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What do you tell a client about their part in the work? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b21
  forPractitioner: { text: "Monitor in supervision that students take on only work within their competence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You make a point of staying within your competence, whatever the client group or way of working.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on staying within one's competence. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b20 and qaa/counselling-and-psychotherapy-2022/4.11.b22 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on staying within one's competence by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: When did you decline or refer work because it was beyond you? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b22
  forPractitioner: { text: "Assess at least one full episode of therapy from assessment through plan to ending.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can carry out a full episode of therapy in line with your approach, from assessing needs, goals and risk to a clear plan.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on conducting an episode of therapy. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b21 and qaa/counselling-and-psychotherapy-2022/4.11.b23 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on conducting an episode of therapy by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Take me through one client's work from first meeting to ending. Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b23
  forPractitioner: { text: "Assess the depth of students' needs assessment.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You evaluate thoroughly what each client needs and wants from therapy.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on evaluating needs and goals. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b22 and qaa/counselling-and-psychotherapy-2022/4.11.b24 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on evaluating needs and goals by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What does this client want from therapy, in their words? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b24
  forPractitioner: { text: "Require a written formulation revised as the work proceeds.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You build an understanding of what may be going on for a client, drawing on theory and on the work as it develops.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on building a formulation. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b23 and qaa/counselling-and-psychotherapy-2022/4.11.b25 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on building a formulation by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How has your formulation of this client changed over time? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b25
  forPractitioner: { text: "Assess risk identification in casework.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You identify and weigh any risks a client brings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on identifying presenting risk. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b24 and qaa/counselling-and-psychotherapy-2022/4.11.b26 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on identifying presenting risk by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What risks did this client bring at the start? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b26
  forPractitioner: { text: "Check that plans include review points and a route to ending.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You draw up and agree a plan with each client, covering what you will do, how and when, with points to review it and decide when to finish.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on a contract and plan with review points. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b25 and qaa/counselling-and-psychotherapy-2022/4.11.b27 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on a contract and plan with review points by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: When will you and this client next review the work? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b27
  forPractitioner: { text: "Assess how students adapt interventions to particular populations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You use strategies and techniques suited to your approach and to particular groups of clients.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on interventions for particular populations. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b26 and qaa/counselling-and-psychotherapy-2022/4.11.b28 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on interventions for particular populations by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How did you adapt your work for a particular client group? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.11.b28
  forPractitioner: { text: "Review referral decisions in supervision.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You make well-founded decisions about referring clients to other services.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on referral decisions. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.11, Assessment, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.11.b27 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on referral decisions by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What did you weigh up in your last referral decision? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b1
  forPractitioner: { text: "Compare accounts of the relationship across approaches.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand how different approaches see the therapeutic relationship.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on the relationship across approaches. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b2 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on the relationship across approaches by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What does your approach say heals in the relationship? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b2
  forPractitioner: { text: "Teach the evidence base across approaches so that students can support informed client choice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand a range of approaches, their theory and the evidence for them, so you can help clients choose what suits them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on approaches and evidence to support client choice. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b1 and qaa/counselling-and-psychotherapy-2022/4.12.b3 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on approaches and evidence to support client choice by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How would you help a client choose between two kinds of therapy? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b3
  forPractitioner: { text: "Teach theories of power and privilege and apply them to the therapy room.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand how power, oppression and privilege can affect the therapeutic relationship.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Know: the minimum every graduate meets on power, oppression and privilege in the relationship. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Know). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b2 and qaa/counselling-and-psychotherapy-2022/4.12.b4 and the descriptor qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on power, oppression and privilege in the relationship by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Where does privilege show up between you and your clients? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b4
  forPractitioner: { text: "Address sexual diversity directly in teaching and in practice assessment.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You respect difference, including welcoming and honouring each client's sexual orientation and choices.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on respect for sexual diversity and difference. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b3 and qaa/counselling-and-psychotherapy-2022/4.12.b5 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on respect for sexual diversity and difference by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How do you make sure clients of any orientation feel safe with you? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b5
  forPractitioner: { text: "Assess whether students hold their own views back while supporting clients' identities.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You offer a safe space for clients to talk honestly about who they are, without pushing your own values or expectations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on a safe space for identity without imposing one's views. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b4 and qaa/counselling-and-psychotherapy-2022/4.12.b6 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on a safe space for identity without imposing one's views by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How do you notice when your own views are creeping in? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b6
  forPractitioner: { text: "Use recorded sessions to assess how students repair ruptures.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can work openly and without getting defensive in hard moments, and repair misunderstandings and ruptures with clients.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Be: the minimum every graduate meets on repairing ruptures without defensiveness. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Be). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b5 and qaa/counselling-and-psychotherapy-2022/4.12.b7 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on repairing ruptures without defensiveness by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Tell me about a rupture you repaired. Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b7
  forPractitioner: { text: "Make monitoring bias a routine part of supervision.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You keep watch on your own bias through self-reflection, supervision and your own therapy.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on monitoring bias through supervision and therapy. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b6 and qaa/counselling-and-psychotherapy-2022/4.12.b8 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on monitoring bias through supervision and therapy by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How do you check your bias between sessions? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b8
  forPractitioner: { text: "Assess how students name and work with difference in sessions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You notice, reflect on and talk openly about differences between you and your client and how they affect the work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on differences between client and counsellor. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b7 and qaa/counselling-and-psychotherapy-2022/4.12.b9 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on differences between client and counsellor by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: When did you raise a difference between you and a client? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b9
  forPractitioner: { text: "Teach the components of the alliance and assess students' work with them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You recognise and work with what holds the alliance together, such as motivation, commitment and the contract.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on the parts of the therapeutic alliance. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b8 and qaa/counselling-and-psychotherapy-2022/4.12.b10 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on the parts of the therapeutic alliance by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What is this client's motivation, and how do you know? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b10
  forPractitioner: { text: "Discuss practical ways to reduce power imbalance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You recognise the built-in power imbalance in therapy and take steps to reduce it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on the power imbalance in therapy. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b9 and qaa/counselling-and-psychotherapy-2022/4.12.b11 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on the power imbalance in therapy by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What do you do to share power in sessions? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b11
  forPractitioner: { text: "Assess anti-discriminatory practice directly on placement and in recorded work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You recognise your own biases and show in your work that you treat every client fairly, whatever their background, identity or beliefs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on anti-discriminatory practice. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b10 and qaa/counselling-and-psychotherapy-2022/4.12.b12 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on anti-discriminatory practice by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What does anti-discriminatory practice look like in your sessions? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b12
  forPractitioner: { text: "Check that students ask about and honour client preferences.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You build and keep a working alliance that respects what each client wants and how they want to work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on an alliance that respects client goals. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b11 and qaa/counselling-and-psychotherapy-2022/4.12.b13 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on an alliance that respects client goals by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How did you find out how this client likes to work? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b13
  forPractitioner: { text: "Teach rupture and repair with case examples.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You notice and work through difficulties and ruptures in the relationship.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on difficulties and ruptures. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b12 and qaa/counselling-and-psychotherapy-2022/4.12.b14 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on difficulties and ruptures by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What signals a rupture for you? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b14
  forPractitioner: { text: "Encourage routine client feedback within sessions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You check regularly how your client sees you and the therapy, and work with what they say.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on the client's view of therapist and therapy. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b13 and qaa/counselling-and-psychotherapy-2022/4.12.b15 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on the client's view of therapist and therapy by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How do you ask clients what they think of the work? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.12.b15
  forPractitioner: { text: "Include ethical marketing in teaching on professional practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You practise openly and fairly, including in how you advertise, following professional guidance and the law.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Do: the minimum every graduate meets on transparent, inclusive practice including marketing. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.12, The therapeutic relationship, under Do). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.12.b14 and the descriptor qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on transparent, inclusive practice including marketing by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Does the way you would advertise your practice include everyone? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b1
  forPractitioner: { text: "Assess group tasks for each student's own contribution.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You carry out your share of a team's work and join in discussion.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on teamwork and discussion. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 1). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b2 and the descriptor qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/annex-d/transferable/r3/3rd at spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on teamwork and discussion by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What did you contribute to your last group task? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b2
  forPractitioner: { text: "Set tasks that need several kinds of source.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You gather information and material from different sources.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on drawing information together from sources. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 2). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b1 and qaa/counselling-and-psychotherapy-2022/4.13.b3 and the descriptor qaa/fheq-2024/4.15.b8 (qaa/fqheis-2024/4.16.b7) at spine:6, with qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on drawing information together from sources by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How do you pull sources together for an essay? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b3
  forPractitioner: { text: "Ask students to frame questions from cases.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You pick out problems and questions to pursue.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on identifying problems and questions. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 3). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b2 and qaa/counselling-and-psychotherapy-2022/4.13.b4 and the descriptor qaa/fheq-2024/4.15.b7 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on identifying problems and questions by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What question did your last case raise for you? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b4
  forPractitioner: { text: "Include data or factual analysis in assessment.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You analyse factual information.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on analysing factual information. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 4). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b3 and qaa/counselling-and-psychotherapy-2022/4.13.b5 and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on analysing factual information by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What did the facts of a case tell you that your first impression missed? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b5
  forPractitioner: { text: "Use critique of published arguments in seminars.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can see the strong and weak points in other people's arguments.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on weighing others' arguments. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 5). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b4 and qaa/counselling-and-psychotherapy-2022/4.13.b6 and the descriptor qaa/fheq-2024/4.15.b7 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on weighing others' arguments by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Whose argument have you questioned recently, and why? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b6
  forPractitioner: { text: "Set literature reviews that require synthesis, not summary.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can bring together what is known on a topic.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on synthesising knowledge on a topic. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 6). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b5 and qaa/counselling-and-psychotherapy-2022/4.13.b7 and the descriptor qaa/fheq-2024/4.15.b5 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on synthesising knowledge on a topic by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What is the current state of knowledge on a topic you care about? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b7
  forPractitioner: { text: "Give supervised independent tasks with clear check-ins.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can work on tasks on your own, with guidance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on working independently with guidance. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 7). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b6 and qaa/counselling-and-psychotherapy-2022/4.13.b8 and the descriptor qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/annex-d/transferable/r4/3rd at spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on working independently with guidance by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which task did you complete mostly on your own? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b8
  forPractitioner: { text: "Ask students to log feedback and what they did with it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You reflect on your progress and use the feedback you get.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on reflecting on progress and using feedback. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 8). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b7 and qaa/counselling-and-psychotherapy-2022/4.13.b9 and the descriptor qaa/fheq-2024/annex-d/transferable/r5/3rd at spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on reflecting on progress and using feedback by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What did you change after your last piece of feedback? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b9
  forPractitioner: { text: "Assess both oral and written communication.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You express yourself well in speech and in writing.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on oral and written expression. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 9). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b8 and qaa/counselling-and-psychotherapy-2022/4.13.b10 and the descriptor qaa/fheq-2024/4.15.b8 (qaa/fqheis-2024/4.16.b7) at spine:6, with qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on oral and written expression by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which do you find harder, speaking or writing, and why? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b10
  forPractitioner: { text: "Assess clarity for a non-specialist audience.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You put knowledge or an argument across so others understand it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on presenting knowledge or argument clearly. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 10). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b9 and qaa/counselling-and-psychotherapy-2022/4.13.b11 and the descriptor qaa/fheq-2024/4.15.b8 (qaa/fqheis-2024/4.16.b7) at spine:6, with qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on presenting knowledge or argument clearly by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How would you explain your approach to someone outside the field? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b11
  forPractitioner: { text: "Build digital literacy into assessed tasks.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You use the right digital tools to collect, analyse, choose and present information.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on digital literacy. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 11). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b10 and qaa/counselling-and-psychotherapy-2022/4.13.b12 and the descriptor qaa/fheq-2024/annex-d/transferable/r2/3rd at spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on digital literacy by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: Which digital tools do you rely on for study? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b12
  forPractitioner: { text: "Include assessed presentations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You give effective presentations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on presentations. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 12). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b11 and qaa/counselling-and-psychotherapy-2022/4.13.b13 and the descriptor qaa/fheq-2024/4.15.b8 (qaa/fqheis-2024/4.16.b7) at spine:6, with qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on presentations by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What feedback did your last presentation get? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b13
  forPractitioner: { text: "Assess critical evaluation of theory, approaches and methods.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You think critically about theory, approaches to therapy and research methods.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on critical evaluation of theory, modalities and methods. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 13). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b12 and qaa/counselling-and-psychotherapy-2022/4.13.b14 and the descriptor qaa/fheq-2024/4.15.b7 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on critical evaluation of theory, modalities and methods by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What is the weakest point of your favourite approach? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b14
  forPractitioner: { text: "Introduce unfamiliar material and check understanding.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can grasp new ideas or information when they come up.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on grasping new ideas. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 14). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b13 and qaa/counselling-and-psychotherapy-2022/4.13.b15 and the descriptor qaa/fheq-2024/4.15.b4 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on grasping new ideas by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What new idea did you have to get to grips with recently? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b15
  forPractitioner: { text: "Use observation tasks that need accurate description.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can recognise and describe material accurately.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on recognising and describing material. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 15). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b14 and qaa/counselling-and-psychotherapy-2022/4.13.b16 and the descriptor qaa/fheq-2024/4.15.b8 (qaa/fqheis-2024/4.16.b7) at spine:6, with qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on recognising and describing material by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How would you describe what happened in a session without judging it? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b16
  forPractitioner: { text: "Include tasks that sort and categorise data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can sort, group and describe data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on classifying data. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 16). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b15 and qaa/counselling-and-psychotherapy-2022/4.13.b17 and the descriptor qaa/fheq-2024/4.15.b8 (qaa/fqheis-2024/4.16.b7) at spine:6, with qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on classifying data by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How did you organise the data in your last project? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b17
  forPractitioner: { text: "Cover workplace safety and inclusion in preparation for placement.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand why health and safety, equality and inclusion matter at work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on health, safety and inclusion at work. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 17). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b16 and qaa/counselling-and-psychotherapy-2022/4.13.b18 and the descriptor qaa/fheq-2024/4.15.b8 (qaa/fqheis-2024/4.16.b7) at spine:6, with qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on health, safety and inclusion at work by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What safety and inclusion checks does your placement make? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b18
  forPractitioner: { text: "Bring debates on sustainability, decolonisation and anti-racism into the curriculum.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You take part in current debates on sustainability, work and global questions, including decolonisation and anti-racism.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on debates on sustainability, employability and global perspectives. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 18). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b17 and qaa/counselling-and-psychotherapy-2022/4.13.b19 and the descriptor qaa/fheq-2024/4.15.b8 (qaa/fqheis-2024/4.16.b7) at spine:6, with qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on debates on sustainability, employability and global perspectives by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: How does decolonisation bear on the theories you are taught? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.13.b19
  forPractitioner: { text: "Make sustainable practice part of course life and placement.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You see why you need to act sustainably.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), listed under Generic skills: the minimum every graduate meets on acting sustainably. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.13, bullet 19). Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.13.b18 and the descriptor qaa/fheq-2024/4.15.b8 (qaa/fqheis-2024/4.16.b7) at spine:6, with qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to show on acting sustainably by the end of training, or when staff check a module, placement or portfolio against it. Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. Ask: What could you change to practise more sustainably? Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass."
- statement: qaa/counselling-and-psychotherapy-2022/4.14
  forPractitioner: { text: "Use your institution's generic marking scheme for 2:2 and 2:1 work; the statement gives no subject-specific typical standards.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" on the course and its team, on typical-level criteria left to institutional marking schemes, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.14). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 4, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles typical-level criteria left to institutional marking schemes. Frame it for staff as an expected feature worded with \"will\", and ask: Does the generic marking scheme say enough about practice competence at 2:2 and 2:1? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/4.15
  forPractitioner: { text: "Use your institution's generic marking scheme for first-class work; the statement gives no subject-specific excellent standards.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" on the course and its team, on excellent-level criteria left to institutional marking schemes, holding for any Counselling and Psychotherapy course the statement covers. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.15). Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. Set it beside the statement's section 4, and where it shapes outcomes beside the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles excellent-level criteria left to institutional marking schemes. Frame it for staff as an expected feature worded with \"will\", and ask: What would first-class practice look like under your scheme? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/counselling-and-psychotherapy-2022/4.16.b1
  forPractitioner: { text: "Teach how knowledge in the field is built through research.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand how research moves knowledge in your field forward.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on how research advances knowledge; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.16, bullet 1). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.16.b2, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b3 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for how research advances knowledge. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: How has research changed practice in your field in the last decade? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.16.b2
  forPractitioner: { text: "Ask students to locate the edges of knowledge on their topic.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can tell where current knowledge ends.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on the boundaries of knowledge; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.16, bullet 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.16.b1 and qaa/counselling-and-psychotherapy-2022/4.16.b3, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for the boundaries of knowledge. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: Where does what is known about your topic run out? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.16.b3
  forPractitioner: { text: "Value original insight in assessment.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You create new insight in your field.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on new insight in the field; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.16, bullet 3). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.16.b2 and qaa/counselling-and-psychotherapy-2022/4.16.b4, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b3 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for new insight in the field. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: What new insight has your work produced? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.16.b4
  forPractitioner: { text: "Give students room to direct their own development.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You build higher-level skills by directing your own academic and professional development.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on self-directed higher-level development; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.16, bullet 4). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.16.b3 and qaa/counselling-and-psychotherapy-2022/4.16.b5, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b6 and qaa/fheq-2024/4.17.b8.3 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for self-directed higher-level development. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: What are you developing on your own initiative? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.16.b5
  forPractitioner: { text: "Assess systematic, critical command of current research across the key topics.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must show a systematic, critical grasp of topics shaped by the newest research in your field.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on a systematic, research-informed knowledge base; it is a requirement worded with \"must\". Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.16, bullet 5). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.16.b4, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for a systematic, research-informed knowledge base. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: Which topic could you speak on at the forefront of current research? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.17.b1
  forPractitioner: { text: "Assess independent, original critical analysis of complex ideas.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You discuss and analyse complex ideas critically, on your own and with some originality.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on independent, original critical analysis; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.17, bullet 1). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.17.b2, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b6 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for independent, original critical analysis. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: Where has your own thinking gone beyond what you were taught? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.17.b2
  forPractitioner: { text: "Teach the intellectual history of therapy and link it to each student's approach.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand critically where the field's ideas came from and how they underpin your own approach.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on the history, culture and philosophy of the field; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.17, bullet 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.17.b1 and qaa/counselling-and-psychotherapy-2022/4.17.b3, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for the history, culture and philosophy of the field. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: Which ideas from history shape your approach most? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.17.b3
  forPractitioner: { text: "Include chronic and enduring presentations in case teaching.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can work out ways of working with clients who have long-lasting mental health problems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on formulating work with long-term mental health issues; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.17, bullet 3). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.17.b2 and qaa/counselling-and-psychotherapy-2022/4.17.b4, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b5 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for formulating work with long-term mental health issues. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: How would your formulation change for a client with a long-term condition? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.17.b4
  forPractitioner: { text: "Examine diagnostic language critically in teaching.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand critically how diagnosis and mental disorder are talked about.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on discourses of diagnosis and psychopathology; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.17, bullet 4). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.17.b3 and qaa/counselling-and-psychotherapy-2022/4.17.b5, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b4.1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for discourses of diagnosis and psychopathology. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: What does a diagnostic label do to the way a client is seen? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.17.b5
  forPractitioner: { text: "Assess how students address discrimination and power across services, training and supervision.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You speak up about the harm discrimination causes and work to reduce blindness to power in services, training and supervision.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on speaking about discriminatory harm and power; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.17, bullet 5). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.17.b4 and qaa/counselling-and-psychotherapy-2022/4.17.b6, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b8.2 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for speaking about discriminatory harm and power. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: Where have you named a power difference others had missed? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.17.b6
  forPractitioner: { text: "Teach processes outside awareness and their part in ruptures, with case material.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You understand how processes outside awareness in you and your client shape the work, and you work with ruptures when they happen.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on unconscious processes and ruptures; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.17, bullet 6). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.17.b5 and qaa/counselling-and-psychotherapy-2022/4.17.b7, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b5 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for unconscious processes and ruptures. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: What might be going on outside awareness in a stuck piece of work? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.17.b7
  forPractitioner: { text: "Look for diversity research in students' clinical reasoning.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You bring theory and research on diversity and equality into your clinical work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on bringing diversity research into practice; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.17, bullet 7). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.17.b6 and qaa/counselling-and-psychotherapy-2022/4.17.b8, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b3 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for bringing diversity research into practice. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: Which piece of research on diversity has changed your practice? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.17.b8
  forPractitioner: { text: "Include a service audit or evaluation task.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You use audit and evaluation to help improve how therapy is done and what it achieves.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on audit and evaluation to improve therapy; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.17, bullet 8). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.17.b7 and qaa/counselling-and-psychotherapy-2022/4.17.b9, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b2 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for audit and evaluation to improve therapy. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: What would you audit in your service first? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.17.b9
  forPractitioner: { text: "Supervise a substantial study through each stage, from question to evaluation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You design, carry out and evaluate a substantial research study that answers a real question and adds to what is known.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on a substantial research study; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.17, bullet 9). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.17.b8 and qaa/counselling-and-psychotherapy-2022/4.17.b10, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b2 and qaa/fheq-2024/4.17.b3 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for a substantial research study. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: What question will your research study answer, and why does it matter? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.17.b10
  forPractitioner: { text: "Assess depth of reflexive work in recorded sessions and supervision.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You use reflexivity, self-awareness and yourself to work in depth with clients.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on reflexive use of self for in-depth work; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.17, bullet 10). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.17.b9 and qaa/counselling-and-psychotherapy-2022/4.17.b11, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b6 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for reflexive use of self for in-depth work. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: How do you use yourself to deepen the work? Do not read the issuer's list aloud at length or present it as the honours standard."
- statement: qaa/counselling-and-psychotherapy-2022/4.17.b11
  forPractitioner: { text: "Prepare students to hold strong emotion, with supervision close at hand.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You can stay with and contain strong emotion when a session becomes highly charged.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on holding intense emotion; it is a minimum the award requires. Cite it as (QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, para 4.17, bullet 11). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. Set it beside qaa/counselling-and-psychotherapy-2022/4.17.b10, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor qaa/fheq-2024/4.17.b8.2 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for holding intense emotion. Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. Ask: How do you stay steady when a client's feelings are overwhelming? Do not read the issuer's list aloud at length or present it as the honours standard."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.6; 4.2 (title of Annex D); 4.4" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.6; 4.2 (title of Annex D); 4.4" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.8 (master's degrees)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.8 (master's degrees)" }
  - { id: "spine:6", role: "refers", locator: "std:ref:uk-framework R2 and R8 (inferred: Part E)" }
  - { id: "spine:7", role: "refers", locator: "std:ref:uk-framework R2 and R8 (inferred: Part E)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.6: \"FHEQ Level 6; FQHEIS Level 10\"; 4.4; 4.2, the title of Annex D)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.8: \"FHEQ Level 7; FQHEIS Level 11\")" }
  - { from: "fheq:6", to: "spine:6", relation: "equivalent", basis: "inferred from std:ref:uk-framework R2 (Part E)" }
  - { from: "fheq:7", to: "spine:7", relation: "equivalent", basis: "inferred from std:ref:uk-framework R2 (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.6", "1.9", "1.10", "1.11", "2.3", "3.3", "3.9", "3.10", "3.16", "4.3", "4.6", "4.7", "4.12", "4.13", "4.17"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.10", "1.11", "1.22", "2.3", "2.4", "3.18", "4.9"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.6", "1.7", "1.12", "1.13", "1.14", "2.9", "2.16", "3.3", "4.3", "4.13"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.15", "1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "1.28", "2.2", "2.12", "3.3", "4.3", "4.7"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-counselling-and-psychotherapy-2013-benchmarks (not yet ingested)", note: "the first edition (2013), named in section 6; the front matter lists the key changes" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees, for performance above the threshold (4.2); SL6" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "levels 6 and 7 (2.6, 2.8, 4.4)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "levels 10 and 11 (2.6, 2.8, 4.4)" }
- { rel: "refersTo", target: "std:doc:welsh-government-cqfw-2009-framework", note: "named in 3.1 for earlier vocational awards in Wales; no level cited" }
- { rel: "thresholdAt", target: "std:ref:uk-framework, spine:6 and spine:7", note: "inferred: the honours threshold at spine:6, the master's threshold at spine:7 (Part E)" }
- { rel: "readWith", target: "std:doc:qaa-psychology-2023-benchmarks; std:doc:qaa-health-studies-2024-benchmarks; std:doc:qaa-social-work-2026-benchmarks; std:doc:qaa-education-studies-2025-benchmarks", note: "1.8: providers may refer to the statements for allied professions (medicine, health sciences, nursing, social work, education, psychology); editions as held, which may differ from those of 2022 (Part E)" }
- { rel: "refersTo", target: "UNESCO (2017) key competencies for sustainability (not yet ingested: Part E)", note: "1.6, 1.7, 1.13" }
- { rel: "refersTo", target: "PSA accredited registers and the professional bodies holding them (not yet ingested: Part E)", note: "1.8; section 5" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2022-03"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "none-stated (advisory group of 2022 listed in section 6)"
previousEditions: "2013 (first edition, advisory group in section 6)"
replacedBy: "none"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- counsellors and psychotherapists work to ease psychological distress and help clients build self-awareness, insight, skill and confidence to live more effectively (D1, 1.1)
- training forms knowledgeable, self-reflective and reflexive practitioners committed to lifelong development and professional standards, working safely, ethically and effectively while keeping well themselves (D1, 1.2, 2.1)
- practice happens in many settings, from private practice and agencies to schools, prisons, faith communities, businesses, charities and the NHS, with individuals, couples, families, groups and communities, in person or remotely (D1, 1.3 to 1.5)
- reflective self-awareness (of one's biases and preferences) and reflexive self-awareness (of how one's history and culture shape interaction) are both central and are distinguished (D1, 1.7)
- the statement favours no modality; courses vary by modality (such as gestalt, person-centred, CBT, psychodynamic, integrative) and mode, but all join literature, research, client skills and personal and professional growth (D1, front matter; 1.8; 3.6)
- there is no single PSRB; courses align with differing professional standards that may lead to accreditation and registration (D1, 1.8)
- the curriculum rests on five pillars, theory, professional skills practice, personal development, professional development and research, and every professional course includes an assessed, supervised placement (D1, 2.1, 3.4, 3.11)
- experiential work needs close containment, small groups and suitable staff to student ratios (D1, 3.22)
- the threshold standards are framed as what a graduate needs to know, be and do to practise safely, ethically and effectively (D1, 4.4, 4.5)

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "inclusive training as an ethical duty to safeguard students and clients; diverse trainers for diverse clients; content that questions majority-culture theory; anti-discriminatory practice, awareness of bias and of power and privilege in the relationship (D1, 1.6, 1.9 to 1.11, 3.16, 4.6, 4.7, 4.12)"
  statements: ["qaa/counselling-and-psychotherapy-2022/1.10", "qaa/counselling-and-psychotherapy-2022/2.3.b6", "qaa/counselling-and-psychotherapy-2022/3.16", "qaa/counselling-and-psychotherapy-2022/4.6.b8", "qaa/counselling-and-psychotherapy-2022/4.6.b12", "qaa/counselling-and-psychotherapy-2022/4.7.b7", "qaa/counselling-and-psychotherapy-2022/4.7.b9", "qaa/counselling-and-psychotherapy-2022/4.12.b3", "qaa/counselling-and-psychotherapy-2022/4.12.b4", "qaa/counselling-and-psychotherapy-2022/4.12.b8", "qaa/counselling-and-psychotherapy-2022/4.12.b11", "qaa/counselling-and-psychotherapy-2022/4.13.b17", "qaa/counselling-and-psychotherapy-2022/4.17.b5", "qaa/counselling-and-psychotherapy-2022/4.17.b7"]
- theme: theme:accessibility
  inThisSubject: "headed Accessibility in section 2: access in person and online, safe and private practice spaces, accessible formats, placement screening, digital poverty and practical help such as bursaries and laptops; reasonable adjustments with fitness to practise; digital accessibility in remote work (D1, 2.3, 2.4, 4.9)"
  statements: ["qaa/counselling-and-psychotherapy-2022/2.3.b1", "qaa/counselling-and-psychotherapy-2022/2.3.b2", "qaa/counselling-and-psychotherapy-2022/2.3.b3", "qaa/counselling-and-psychotherapy-2022/2.3.b4", "qaa/counselling-and-psychotherapy-2022/2.3.b5", "qaa/counselling-and-psychotherapy-2022/2.3.b6", "qaa/counselling-and-psychotherapy-2022/2.3.b7", "qaa/counselling-and-psychotherapy-2022/2.3.b8", "qaa/counselling-and-psychotherapy-2022/2.3.b9", "qaa/counselling-and-psychotherapy-2022/2.3.b10", "qaa/counselling-and-psychotherapy-2022/2.4", "qaa/counselling-and-psychotherapy-2022/4.9.b19"]
- theme: theme:esd
  inThisSubject: "headed Sustainability: sustainable development knowledge of the profession and its future, the eight UNESCO competencies held essential for practitioners, learning environments that foster responsibility for well-being; ESD embedded across the curriculum and monitored (D1, 1.6, 1.7, 1.12 to 1.14, 2.16, 4.13)"
  statements: ["qaa/counselling-and-psychotherapy-2022/1.7", "qaa/counselling-and-psychotherapy-2022/1.12", "qaa/counselling-and-psychotherapy-2022/1.13", "qaa/counselling-and-psychotherapy-2022/1.14", "qaa/counselling-and-psychotherapy-2022/2.16.b3", "qaa/counselling-and-psychotherapy-2022/4.13.b18", "qaa/counselling-and-psychotherapy-2022/4.13.b19"]
- theme: theme:enterprise
  inThisSubject: "headed Employability, enterprise and entrepreneurship education: growth in paid, voluntary and private practice; knowing the value of one's skills; an entrepreneurial mindset; placements as a bridge to service provision; enterprising capability in the threshold standards (D1, 1.15 to 1.28, 2.2, 4.7)"
  statements: ["qaa/counselling-and-psychotherapy-2022/1.16", "qaa/counselling-and-psychotherapy-2022/1.22", "qaa/counselling-and-psychotherapy-2022/1.23", "qaa/counselling-and-psychotherapy-2022/1.24", "qaa/counselling-and-psychotherapy-2022/2.2.b15", "qaa/counselling-and-psychotherapy-2022/4.6.b13", "qaa/counselling-and-psychotherapy-2022/4.7.b10"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.3", gloss: "eleven areas of knowledge, from philosophy of human nature to mental health systems, framed by epistemic justice" }
  - { component: "3.4", gloss: "the five pillars of the curriculum" }
  - { component: "3.5", gloss: "theory: knowledge common to all orientations and knowledge proper to each" }
  - { component: "3.6", gloss: "theory: a range of approaches and their evidence; modality-neutral wording" }
  - { component: "3.7", gloss: "professional skills practice: ten elements from relationship building to digital delivery" }
  - { component: "3.9", gloss: "professional development: eleven elements from ethics to supervision" }
  - { component: "3.10", gloss: "research: five elements from appraisal to formal projects" }
practices:
  - { component: "3.12", kind: "teaching", gloss: "core methods: seminars, skills practice, research workshops, development activities, supervised placement" }
  - { component: "3.13", kind: "learning", gloss: "experiential activities: modelling, group practice, projects, peer learning, case forums, presentations" }
  - { component: "3.15", kind: "teaching", gloss: "in-person and remote training matched to the mode of practice; core digital training" }
  - { component: "3.19", kind: "learning", gloss: "research skills and at least one small-scale study" }
  - { component: "3.20", kind: "learning", gloss: "personal development through groups, journals, residentials or personal therapy" }
  - { component: "3.21", kind: "learning", gloss: "placements with regular supervision, vetted by the course" }
  - { component: "3.22", kind: "teaching", gloss: "qualified staff and small experiential groups, ratios normally not above one to sixteen" }
  - { component: "3.23", kind: "assessment", gloss: "theory and competence assessed; competence a condition of the award" }
  - { component: "3.24", kind: "assessment", gloss: "typical methods, from essays and portfolios to annotated transcripts and client formulations" }
  - { component: "3.25", kind: "assessment", gloss: "formative and summative, inclusive and authentic; criteria include professional skills" }
  - { component: "3.27", kind: "assessment", gloss: "readiness assessed before client work" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.6 to 4.13 under the heading Threshold level (3rd class); 4.4 sets them as minimum expectations", award: "bachelor's with honours", items: 138 }
  - { rung: "typical", leadIn: "4.14 (heading Typical level (2:2 or 2:1); no items)", award: "bachelor's with honours", items: 0 }
  - { rung: "excellent", leadIn: "4.15 (heading Excellent level (1st class); no items)", award: "bachelor's with honours", items: 0 }
  - { rung: "threshold", leadIn: "4.16 and 4.17 under the heading Benchmark standard for master's degrees", award: "master's", items: 16 }
rungBases: "4.1 and 4.4: the standards are the minimum threshold for honours at FHEQ level 6 or FQHEIS level 10; 4.2: most students do significantly better, judged by each institution with reference to Annex D; 4.14 and 4.15: typical (2:2 or 2:1) and excellent (1st) criteria follow each institution's generic marking schemes; 4.17: the master's statements describe its threshold"
outcomeLists:
  - { leadIn: "2.2", gloss: "what personal development should enable the learner to do", items: 15, award: ["bachelor's with honours", "master's"] }
  - { leadIn: "3.8", gloss: "what trainings must ensure trainees can demonstrate in personal development", items: 10, award: ["bachelor's with honours", "master's"] }
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
- { body: "professional, statutory and regulatory bodies (PSRBs), none named as the single body", says: "there is no single PSRB for counselling and psychotherapy; courses may align with differing standards that can lead to accreditation and registration (D1, 1.8)", requirements: "not yet ingested (Part E)" }
- { body: "the relevant professional body (by modality), unnamed", says: "courses should be written in line with a suitable professional body's requirements; monitoring aligns with them; training follows them; graduates practise in line with professional body guidance (D1, 2.11, 2.16, 3.18, 3.21, 4.12)", requirements: "not yet ingested (Part E)" }
- { body: "Professional Standards Authority (PSA)", says: "approves the accredited registers whose holders are listed in section 5 (D1, section 5)", requirements: "not yet ingested (Part E)" }
- { body: "National Institute for Health and Clinical Excellence (NICE)", says: "its guidelines are an example of government policy and recommendations whose effects graduates should know (D1, 4.6)", requirements: "not yet ingested (Part E)" }
- { body: "Association of Child Psychotherapists", says: "holds a register accredited by the PSA, listed in the references (D1, section 5)", requirements: "not yet ingested (Part E)" }
- { body: "Association of Christian Counsellors", says: "holds a register accredited by the PSA, listed in the references (D1, section 5)", requirements: "not yet ingested (Part E)" }
- { body: "British Association for Counselling & Psychotherapy", says: "holds a register accredited by the PSA, listed in the references (D1, section 5)", requirements: "not yet ingested (Part E)" }
- { body: "British Psychoanalytic Council", says: "holds a register accredited by the PSA, listed in the references (D1, section 5)", requirements: "not yet ingested (Part E)" }
- { body: "COSCA (Counselling & Psychotherapy in Scotland)", says: "holds a register accredited by the PSA, listed in the references (D1, section 5)", requirements: "not yet ingested (Part E)" }
- { body: "Human Givens Institute", says: "holds a register accredited by the PSA, listed in the references (D1, section 5)", requirements: "not yet ingested (Part E)" }
- { body: "National Counselling Society", says: "holds a register accredited by the PSA, listed in the references (D1, section 5)", requirements: "not yet ingested (Part E)" }
- { body: "National Hypnotherapy Society", says: "holds a register accredited by the PSA, listed in the references (D1, section 5)", requirements: "not yet ingested (Part E)" }
- { body: "UK Association for Humanistic Psychology Practitioners", says: "holds a register accredited by the PSA, listed in the references (D1, section 5)", requirements: "not yet ingested (Part E)" }
- { body: "UK Council for Psychotherapy", says: "holds a register accredited by the PSA, listed in the references (D1, section 5)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.6", "1.9", "1.10", "1.11", "2.3", "3.3", "3.9", "3.10", "3.16", "4.3", "4.6", "4.7", "4.12", "4.13", "4.17"], statements: ["1.10", "2.3.b6", "3.16", "4.6.b8", "4.6.b12", "4.7.b7", "4.7.b9", "4.12.b3", "4.12.b4", "4.12.b8", "4.12.b11", "4.13.b17", "4.17.b5", "4.17.b7"] }
  - { id: "theme:accessibility", named: "Accessibility", carriedIn: ["1.10", "1.11", "1.22", "2.3", "2.4", "3.18", "4.9"], statements: ["2.3.b1", "2.3.b2", "2.3.b3", "2.3.b4", "2.3.b5", "2.3.b6", "2.3.b7", "2.3.b8", "2.3.b9", "2.3.b10", "2.4", "4.9.b19"] }
  - { id: "theme:esd", named: "Sustainability (front matter and 2.16: education for sustainable development)", carriedIn: ["1.6", "1.7", "1.12", "1.13", "1.14", "2.9", "2.16", "3.3", "4.3", "4.13"], statements: ["1.7", "1.12", "1.13", "1.14", "2.16.b3", "4.13.b18", "4.13.b19"] }
  - { id: "theme:enterprise", named: "Employability, enterprise and entrepreneurship education (EEEE)", carriedIn: ["1.15", "1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "1.28", "2.2", "2.12", "3.3", "4.3", "4.7"], statements: ["1.16", "1.22", "1.23", "1.24", "2.2.b15", "4.6.b13", "4.7.b10"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.6", "2.8", "4.2", "4.4"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.6", "2.8", "3.1", "4.2", "4.4"] }
  - { framework: "cqfw", levels: [], citedIn: ["3.1"] }
  - { framework: "other: Regulated Qualifications Framework (RQF), England and Northern Ireland", levels: [], citedIn: ["3.1"] }
bodies:
  - { body: "PSRBs (no single body)", citedIn: ["1.8"] }
  - { body: "the relevant professional body, unnamed", citedIn: ["2.11", "2.16", "3.18", "3.21", "4.12"] }
  - { body: "National Institute for Health and Clinical Excellence (NICE)", citedIn: ["4.6"] }
  - { body: "Professional Standards Authority (PSA)", citedIn: ["section 5 (back matter)"] }
  - { body: "Association of Child Psychotherapists", citedIn: ["section 5 (back matter)"] }
  - { body: "Association of Christian Counsellors", citedIn: ["section 5 (back matter)"] }
  - { body: "British Association for Counselling & Psychotherapy", citedIn: ["section 5 (back matter)"] }
  - { body: "British Psychoanalytic Council", citedIn: ["section 5 (back matter)"] }
  - { body: "COSCA (Counselling & Psychotherapy in Scotland)", citedIn: ["section 5 (back matter)"] }
  - { body: "Human Givens Institute", citedIn: ["section 5 (back matter)"] }
  - { body: "National Counselling Society", citedIn: ["section 5 (back matter)"] }
  - { body: "National Hypnotherapy Society", citedIn: ["section 5 (back matter)"] }
  - { body: "UK Association for Humanistic Psychology Practitioners", citedIn: ["section 5 (back matter)"] }
  - { body: "UK Council for Psychotherapy", citedIn: ["section 5 (back matter)"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "how institutions judge achievement above the threshold, by the four honours classes" }
  - { document: "not yet ingested: listed in Part E", named: "Subject Benchmark Statements for these various professions (medicine, health sciences, nursing, social work, education, psychology)", citedIn: ["1.8"], role: "reading for collaboration with allied professions" }
  - { document: "not yet ingested: listed in Part E", named: "UNESCO, 2017 (the key competencies for sustainability)", citedIn: ["1.6", "1.7", "1.13"], role: "the eight competencies held essential for practitioners" }
  - { document: "not yet ingested: listed in Part E", named: "Teaching Excellence Framework (TEF), National Student Survey (NSS), PTES and PRES", citedIn: ["2.16"], role: "external exercises whose feedback monitoring should draw on" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "reflective-self-awareness", definition: "awareness of one's own biases and preferences (D1, 1.7)", beneficiaryDefinition: "noticing your own biases and preferences", scopeNote: "paired with reflexive self-awareness; the two overlap and complement each other", category: "unknown", practices: ["counselling", "psychotherapy"] }
- { slug: "reflexive-self-awareness", definition: "awareness of how one's own history and culture shape the way one relates to others (D1, 1.7)", beneficiaryDefinition: "seeing how your own past and culture affect how you relate to people", scopeNote: "paired with reflective self-awareness", category: "unknown", practices: ["counselling", "psychotherapy"] }
- { slug: "suicidal-ideation", definition: "thoughts of suicide, set apart from intent in judging risk (D1, 4.11)", beneficiaryDefinition: "having thoughts of suicide", scopeNote: "contrasted with suicidal intent", category: "unknown", practices: ["counselling", "psychotherapy"] }
- { slug: "suicidal-intent", definition: "an intention to act on thoughts of suicide (D1, 4.11)", beneficiaryDefinition: "intending to act on thoughts of suicide", scopeNote: "contrasted with suicidal ideation", category: "unknown", practices: ["counselling", "psychotherapy"] }
- { slug: "eeee", definition: "employability, enterprise and entrepreneurship education, which builds the behaviours, attributes and competencies for a career, employed or self-employed (D1, 1.18 to 1.21)", beneficiaryDefinition: "learning that prepares you for work and for running your own practice", scopeNote: "the statement abbreviates it EEEE", category: "unknown", practices: ["education"] }
- { slug: "experts-by-experience", definition: "people who use services, whose feedback informs course review (D1, 2.16)", beneficiaryDefinition: "people with lived experience of using services", scopeNote: "", category: "unknown", practices: ["counselling", "psychotherapy"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "reflective-self-awareness", form: "Reflective self-awareness", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "reflexive-self-awareness", form: "reflexive self-awareness", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "suicidal-ideation", form: "suicidal ideation", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "suicidal-intent", form: "suicidal intent", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "eeee", form: "EEEE", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "experts-by-experience", form: "Experts by Experience", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Counselling and Psychotherapy"
  edition: "March 2022 (second edition)"
  year: 2022
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/counselling-and-psychotherapy-2022/counselling-and-psychotherapy-2022.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 44e7c19f2b1ff0fe9f79a112c44746b22f9ac7b69983b88abfd73a49bfe7b4f0
  heldFiles: ["wkspc2601-library/txt/qaa-2022-counselling-psychotherapy-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2022-counselling-psychotherapy-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2022-counselling-psychotherapy-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2022-counselling-psychotherapy-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0046", source: "the professional bodies' accreditation standards (such as BACP and UKCP) and the PSA accredited registers standards", why: "the bodies named in 1.8 and section 5 (SB5)", status: "wanted" }
- { w: "W-std-0043", source: "UNESCO (2017), the key competencies for sustainability", why: "cited in 1.6, 1.7 and 1.13 (SB6)", status: "wanted" }
- { w: "W-std-0047", source: "Subject Benchmark Statement: Counselling and Psychotherapy (2013, first edition)", why: "superseded edition (S7)", status: "wanted" }
```

## Part E Gaps and questions
- Rungs: the honours standards are threshold only. Section 4 lists threshold items under seven practice headings (4.6 to 4.12) and generic skills (4.13); 'Typical level (2:2 or 2:1)' (4.14) and 'Excellent level (1st class)' (4.15) are headings with no items, deferring to each institution's generic marking schemes, and 4.2 points to Annex D. SB4 records typical and excellent with items 0, `outcomes` is empty and no gradeOf link is drawn. Differs from Psychology (three listed rungs).
- New rung shape: each threshold paragraph 4.6 to 4.12 opens 'The graduate will have the relevant professional knowledge, abilities and skills to:' and then runs unbulleted sentences under the in-line markers Know, Be and Do. Each sentence is cut as its own record (<n>.b<k> in text order, our numbering within the issuer's paragraph); where a sentence introduces bullets (4.9, 4.10, 4.11), the lead sentence and each bullet are separate records, except 4.10.b1, whose bullets are single nouns (clients, supervisors, tutors, colleagues, employers) and stay in its span. The Know, Be or Do marker is recorded in the agent instructions' locator, not in the span.
- Domain for Know, Be, Do: Know sentences are knowledge, or understanding where the verb is understand or evaluate; Be sentences (professional attributes such as 'Reflective of', 'Open to', 'Committed to') and Do sentences are recorded as subject-skill. P3 to confirm Be as subject-skill rather than a domain of its own.
- Force of threshold items: recorded as threshold (brief convention: the issuer defines the rung as the minimum, 4.1 and 4.4), with forceFrom 4.4; the lead-in's own modal is will ('will have'). 4.13's lead-in is 'should be able to' but sits under the threshold heading, so it too is recorded as threshold; P3 to confirm should against threshold for 4.13.
- Master's: 4.16 (stem 'requires additional critical and conceptual understanding that enables students to', four items) and 4.17 ('The following additional statements describe the threshold level of competence', eleven items, 'will be capable of') are recorded as rung threshold, award master's, level fheq:7, force threshold with forceFrom 4.17. Skeleton correction: 4.16.b4 held both the fourth bullet (marked '-' not a bullet sign) and the closing sentence; recut so that 4.16.b4 is the bullet and 4.16.b5 is the closing sentence ('award holders must demonstrate'), force must; 4.16.b5 is not a bullet in the issuer's text.
- Skeleton corrections: 2.2.b15, 2.9.b3, 3.8.b10 and 4.13.b19 carried the next sub-heading (Accessibility, Partnership, Professional development, Typical level); recut with `find`. The skeleton's 4.9, 4.10 and 4.11 bullet cuts (b5 of 4.9 ran over 1,600 characters across many sentences) are replaced by the sentence cut above. Paragraph spans for paragraph records are tidied of trailing sub-headings and page numbers.
- Skeleton false hits: 3.24 was flagged as a typical rung lead-in ('Typically, courses of study ...'); its list is assessment methods ('can include') and is an S3 practice, not statements. 4.16 and 4.17 were flagged threshold correctly. The skeleton's typical count (12) is therefore wrong; the true honours rung counts are threshold only.
- Outcome lists outside section 4: 2.2 (personal development 'should underpin ... to enable the learner to', 15 items, force should) and 3.8 ('Trainings must ensure that trainees are able to demonstrate', 10 items, force must), recorded as type outcome, rung none. New lead-in wordings against Psychology.
- Lists not cut as statements, with reasons: 1.3 (settings, 'may occur'), 1.13 bullets (names of the eight UNESCO competencies; the paragraph is one record), 1.17 (what an entrepreneurial mindset 'means becoming', a definition), 3.3 (areas of knowledge, plain present 'ensures that graduates have'), 3.7, 3.9 and 3.10 ('incorporates the following', content), 3.12 and 3.13 (training methods), 3.24 (assessment methods, 'can include'). 3.3, 3.9 and 3.10 read close to outcomes; P3 to confirm they are content, not standards.
- Obliging words outside the five, recorded as describes for Abbott: 1.10 ('Assessments need to be authentic'), 1.13 ('requires practical operation of all the competencies'; read as must, but the builder's force pattern knows only 'require' and 'required'), 1.24 ('is recommended'), 2.6 ('it is expected', 'would be expected'). Also noted, inside records with another force: 3.18 ('it is essential that students develop'), 3.19 ('graduates require sufficient awareness'), 3.21 ('should be required').
- Plain-present provider norms not cut (benchmark template open point 5, for P3): 1.2 ('Courses ... prepare students'), 1.9, 1.11 (strive, encouraged), 2.4 second sentence ('courses include ethical responsibilities for monitoring student fitness to practice', kept inside the 2.4 record), 2.12, 2.13 to 2.15 (institutional practice with will), 3.5, 3.6 ('A typical course of study will offer'), 3.14, 3.28. 1.25 ('will help students develop') and 1.26 to 1.28 describe benefits, not standards.
- Mixed modals within one record: 1.7 (will and should) recorded at will; 1.14 (aim and must) at must; 2.3.b6 holds must inside a should list, recorded at must; 3.11 (will and must) at must; 3.22 (should and must) at must; 3.27 (should and must) at must; 2.9 items take 'may' from the lead-in 'may be', though the stem opens with 'should consider'.
- Broken words in the held text (extraction spacing: 'perf orm', 'bri ng', 'identi fy', 'undert ake', 're flect', 'wri ting', 'arg ument', 'materi al', 'categori sing', 'collati ng', 'contempora ry', 'relati ng', 'saf e', 'staf f', 'successf ul', 'self -awareness') mean some verbs cannot be listed as they appear: 4.13.b2, b3, b7 list none; 4.13.b1 lists 'assigned' and 'participating'. Spans keep the text as held.
- The 2.2 list repeats 1.17's mindset items (self-organised, tolerant of uncertainty, sensitive to personal values) and 4.7.b10 repeats 1.16's wording on enterprising capabilities; each is kept where the issuer places it. 3.9 and 4.8 share wording on strengths, limitations and self-care, and 3.8.b6 and 4.8.b7 on personal support; kept as issued.
- The statement names sexual dynamics, suicide risk and self-harm as professional knowledge (4.10.b6, 4.11.b7 to b9); the versions keep these at the level of practice competence.
- Inferred: the crosswalks fheq:6 to spine:6 and fheq:7 to spine:7 are read from std:ref:uk-framework R2. The S7 readWith targets are the editions held now (Psychology 2023, Health Studies 2024, Social Work 2026, Education Studies 2025), not those current in 2022; medicine and nursing have no matching statement held.
- Subjects: HECoS 100495 (counselling), 100254 (psychotherapy) and CAH02-06-07 are recorded as stated because the title names both subjects; the statement names no code. Joint honours (2.7) carries no partner code.
- SB5 and SB6: the ten bodies holding PSA accredited registers and the PSA itself are named only in section 5 (back matter, otherwise excluded); recorded so the bodies can be read across, with citedIn 'section 5 (back matter)'. BACP and UKCP also appear in the 2022 advisory group. No body's requirements are ingested (D3).
- SB6: the front matter also names the OfS regulatory framework, the Quality Assessment Framework for Wales, the Quality Enhancement Framework (Scotland), the Quality Code's Advice and Guidance and QAA's Glossary; these are excluded matter and not level frameworks, so they are not in SB6. 2.16.b9 names the TEF, NSS, PTES and PRES, recorded as a shared document entry not yet ingested. CQFW and the RQF are named in 3.1 for earlier vocational awards, with no level.
- Levels: the threshold standards (4.4) apply to 'practice-facing courses' and 'students on professional courses'; it is not stated how a non-practice honours route (if any) relates to them. 2.8 mentions exit awards (Postgraduate Certificate or Diploma) with no standards.
- Section order: section 1 holds the cross-cutting themes (EDI, Sustainability, EEEE); section 2 holds Personal development, Accessibility, Progression, Flexibility, Partnership, Monitoring and review; section 3 Content is subdivided by the five pillars; filled by function.
- Supersedes: the 2013 first edition is named only in the advisory group list (section 6); the back matter says 'Second edition, Published 30 March 2022'.
- Licence: QAA copyright notice only; re-use terms not stated in the text.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:58: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0096 (P1); built by tools/bm_build.py.
