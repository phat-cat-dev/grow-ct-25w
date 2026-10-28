---
id: std:doc:qaa-biomedical-science-and-biomedical-sciences-2023-benchmarks
title: "Subject Benchmark Statement Biomedical Science and Biomedical Sciences"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "cah", code: "CAH02-05-03", label: "biomedical sciences (non-specific)", basis: "inferred" }
  - { scheme: "hecos", code: "100265", label: "biomedical sciences", basis: "inferred" }
  - { scheme: "hecos", code: "100260", label: "healthcare science", basis: "inferred" }
  - { scheme: "hecos", code: "100250", label: "pharmacology", basis: "inferred" }
  - { scheme: "hecos", code: "100247", label: "nutrition", basis: "inferred" }
  - { scheme: "hecos", code: "100262", label: "physiology", basis: "inferred" }
edition: "March 2023"
published: 2023-03
status: current
supersedes: "the fourth edition, Biomedical Sciences (2019), as the back matter states; this is the fifth edition, published 8 March 2023"
heldText: { method: sha256-bytes, raw: 5a6dbd79e6d960dbd60e18f820da36dd685b4c933f3c4e5f4e0629614d9284d0, normalised: 41e4280c6def4c5af31234b2ed93bbb9dc72eb4f56843e866947fc15711d553f }
heldTextStan: { method: sha256-stan, raw: 5a6dbd79e6d960dbd60e18f820da36dd685b4c933f3c4e5f4e0629614d9284d0, normalised: a75429fa3d87ac8c221765ea5bde64e786db447d60ebd16d29b07fbddadc600a }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, the revision with cross-cutting themes; this statement's fifth edition (D1, front matter; back cover)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0089 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:39"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Biomedical Science and Biomedical Sciences (QAA, March 2023)

> Run 0089, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2023-biomedical-science-biomedical-sciences-subject-benchmark-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in Biomedical Science (singular: the IBMS-accredited route to HCPC registration as a Biomedical Scientist) or Biomedical Sciences (plural: the broader human biology degrees, including Pharmacology, Human Nutrition and Physiology) should know, understand and be able to do. Reach for it when designing, approving, reviewing or describing an honours or master's course in these subjects, when placing a student's work against its threshold and excellent standards, or when explaining how an accredited degree leads to registration. It is a sector reference point, not a regulation, and not the IBMS's accreditation criteria or the HCPC's standards of proficiency.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2023 as the fifth edition, the statement separates Biomedical Science (accredited by the Institute of Biomedical Science, leading with clinical training to registration with the Health and Care Professions Council) from the broader Biomedical Sciences. It sets out context and purposes, with the four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability; enterprise and entrepreneurship education); distinctive features of design, progression, flexibility, partnership and review; and content, teaching and assessment, including outcome lists for the nine clinical pathology specialisms of an accredited degree and for Pharmacology, Human Nutrition and Physiology courses. Its benchmark standards are two tables: Table 1, sixteen outcomes for the honours degree, fifteen of them graded at threshold and excellent; Table 2, master's outcomes in addition, graded only by the support or independence they are shown with. It cites the FHEQ and FQHEIS levels, Annex D for degree classes, the QAA and Advance HE ESD guidance and QAA's enterprise guidance, and names IBMS, HCPC, the Royal Society of Biology, the Association for Nutrition and the British Pharmacological Society. An appendix of draft threshold suggestions drawn from the HCPC standards of proficiency is held but not ingested as statements.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Biomedical Science and Biomedical Sciences"
edition: "March 2023"
dates:
  published: 2023-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector-owned reference point, not a regulatory requirement; a key reference point in Wales and Scotland and part of the quality arrangements in Northern Ireland, not a sector-recognised standard in England (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2023", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what honours graduates in Biomedical Science and Biomedical Sciences, and master's graduates in addition, can be expected to know, understand and do, at threshold and excellent standards; the clinical pathology content of an IBMS-accredited degree; core content for Pharmacology, Human Nutrition and Physiology courses; and the context for course design, teaching and assessment"
appliesTo:
  awards: ["bachelor's with honours", "master's"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This Subject Benchmark Statement offers clarification between Biomedical Science (singular) and Biomedical Sciences (plural) courses.\" (D1, 1.1)"
statedSubjects:
  - { name: "Biomedical Science", locator: "(D1, front matter; 1.2; 1.6; 3.2 to 3.4)", kind: "subject", codes: [{ scheme: "hecos", code: "100265", label: "biomedical sciences" }] }
  - { name: "Biomedical Sciences", locator: "(D1, front matter; 1.3; 2.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100265", label: "biomedical sciences" }] }
  - { name: "Healthcare Science", locator: "(D1, 2.6; 3.2; 3.4)", kind: "programme title", codes: [{ scheme: "hecos", code: "100260", label: "healthcare science" }] }
  - { name: "Pharmacology", locator: "(D1, 1.3; 2.5; 3.5; 3.6)", kind: "specialism", codes: [{ scheme: "hecos", code: "100250", label: "pharmacology" }] }
  - { name: "Human Nutrition", locator: "(D1, 2.5; 3.7 to 3.9)", kind: "specialism", codes: [{ scheme: "hecos", code: "100247", label: "nutrition" }] }
  - { name: "Human/Medical Physiology", locator: "(D1, 2.5; 3.10; 3.11)", kind: "specialism", codes: [{ scheme: "hecos", code: "100262", label: "physiology" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes", gloss: "the statement tells the singular and plural degrees apart" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes", gloss: "the singular degree covers every clinical laboratory specialism, the academic basis for registration" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context and purposes", gloss: "the plural degree is broader; top-up modules and clinical time as a route to registration" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context and purposes", gloss: "honours courses give a broad scientific basis for health and disease and qualities for demanding work" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context and purposes", gloss: "who the statement is meant for" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of Biomedical Science/Biomedical Sciences degrees", gloss: "accreditation, approval and close work with practising scientists" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of Biomedical Science/Biomedical Sciences degrees", gloss: "lifelong learning and further qualifications after the degree" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of Biomedical Science/Biomedical Sciences degrees", gloss: "the accredited degree aims at diagnostic pathology laboratories" }
  - { number: "1.9", order: 11, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of Biomedical Science/Biomedical Sciences degrees", gloss: "graduate career paths, listed" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of Biomedical Science/Biomedical Sciences degrees", gloss: "hands-on laboratory work as an essential part of every course" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of Biomedical Science/Biomedical Sciences degrees", gloss: "research skills and what they prepare students for" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of Biomedical Science/Biomedical Sciences degrees", gloss: "interpreting clinical test results; the training portfolio and registration" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Registration and protected title", gloss: "the protected title and what the role involves" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Registration and protected title", gloss: "registration by statute; the standards of proficiency" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Registration and protected title", gloss: "the professional body awards the certificate of competence" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "a commitment to equity and inclusive practice" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusion throughout; course teams, awareness and global healthcare" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "confronting the history of the field and its biases" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "diverse contributors, lived experience and the misuse of knowledge" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "equity of access, based on potential" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "fully accessible curricula, assessment and practical work" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "anticipating access needs, including fieldwork, laboratories and placements" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainability in the subject, in the laboratory and in the curriculum" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "ESD as defined by UNESCO; the SDGs" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "the ESD guidance as the reference for teaching sustainability" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "employability and entrepreneurship as competencies; employer links" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "what enterprise education does for careers" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "entrepreneurship beyond employment" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "co-creating enterprise education; topics and real examples" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "visiting speakers, teamwork and taking charge of one's own development" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "where to find the enterprise guidance" }
  - { number: "2.1", order: 35, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "the variety of courses; checking accreditation before applying" }
  - { number: "2.2", order: 36, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "routes into the degree, including foundation years" }
  - { number: "2.3", order: 37, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "the awards and their levels, bachelor's and integrated master's" }
  - { number: "2.4", order: 38, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "placements, the training portfolio and integrating credit-bearing placements" }
  - { number: "2.5", order: 39, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "common cores across related courses and late choice of award" }
  - { number: "2.6", order: 40, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "degree apprenticeships follow the statement" }
  - { number: "2.7", order: 41, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "equally accessible learning and assessment" }
  - { number: "2.8", order: 42, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "accessible design and support for the full range of skills" }
  - { number: "2.9", order: 43, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression from simple concepts to graduate competence" }
  - { number: "2.10", order: 44, componentType: stem, parent: "section 2", heading: "Progression", gloss: "progressive acquisition of knowledge and skills; strategies to support it" }
  - { number: "2.11", order: 45, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progressing between levels by meeting at least the threshold" }
  - { number: "2.12", order: 46, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "re-sits, exit awards and length of study" }
  - { number: "2.13", order: 47, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "diverse modes of delivery and credit transfer" }
  - { number: "2.14", order: 48, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "practical skills, at the bench and virtually" }
  - { number: "2.15", order: 49, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible and resilient courses" }
  - { number: "2.16", order: 50, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership delivery and oversight of partners" }
  - { number: "2.17", order: 51, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "employment-focused learning and inclusive placements" }
  - { number: "2.18", order: 52, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "student societies and learned bodies" }
  - { number: "2.19", order: 53, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "students as partners; student voice" }
  - { number: "2.20", order: 54, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review by degree-awarding bodies" }
  - { number: "2.21", order: 55, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "feedback that feeds review" }
  - { number: "2.22", order: 56, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "review checks ESD and EDI across the curriculum" }
  - { number: "2.23", order: 57, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "performance data and expert review together" }
  - { number: "2.24", order: 58, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.25", order: 59, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "the external examining system" }
  - { number: "2.26", order: 60, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "more than one external examiner may be needed" }
  - { number: "2.27", order: 61, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "regular monitoring and enhancement with students and others" }
  - { number: "2.28", order: 62, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "the bodies that accredit courses in the area" }
  - { number: "3.1", order: 64, componentType: area, parent: "section 3", heading: "Content common to Biomedical Science and/or Biomedical Sciences courses", gloss: "scientific content common to all the courses" }
  - { number: "3.2", order: 65, componentType: paragraph, parent: "section 3", heading: "Content specific to Biomedical Science courses - clinical pathology subjects", gloss: "the clinical specialisms the accredited degree must cover" }
  - { number: "3.3", order: 66, componentType: paragraph, parent: "section 3", heading: "Content specific to Biomedical Science courses - clinical pathology subjects", gloss: "integrating specialisms through a systems-led approach" }
  - { number: "3.4", order: 67, componentType: area, parent: "section 3", heading: "Content specific to Biomedical Science courses - clinical pathology subjects", gloss: "the clinical pathology subject areas and what graduates know in each" }
  - { number: "3.5", order: 68, componentType: area, parent: "section 3", heading: "Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses", gloss: "other specialisms; what pharmacology is" }
  - { number: "3.6", order: 69, componentType: area, parent: "section 3", heading: "Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses", gloss: "core outcomes for Pharmacology graduates" }
  - { number: "3.7", order: 70, componentType: area, parent: "section 3", heading: "Content in Human Nutrition courses", gloss: "Human Nutrition courses and the professional body's competencies" }
  - { number: "3.8", order: 71, componentType: paragraph, parent: "section 3", heading: "Content in Human Nutrition courses", gloss: "nutrition careers and registration" }
  - { number: "3.9", order: 72, componentType: area, parent: "section 3", heading: "Content in Human Nutrition courses", gloss: "core outcomes for Human Nutrition graduates" }
  - { number: "3.10", order: 73, componentType: area, parent: "section 3", heading: "Content in Human/Medical Physiology courses", gloss: "physiology as an integrative science, with disease as context" }
  - { number: "3.11", order: 74, componentType: area, parent: "section 3", heading: "Content in Human/Medical Physiology courses", gloss: "core outcomes for Physiology graduates" }
  - { number: "3.12", order: 75, componentType: area, parent: "section 3", heading: "Approaches to study in all courses", gloss: "approaches to study common to all the courses" }
  - { number: "3.13", order: 76, componentType: paragraph, parent: "section 3", heading: "Approaches to study in all courses", gloss: "graduate attributes and the changing state of knowledge" }
  - { number: "3.14", order: 77, componentType: stem, parent: "section 3", heading: "Approaches to study in all courses", gloss: "the graduate attributes, listed" }
  - { number: "3.15", order: 78, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "scaffolded, progressive teaching strategies" }
  - { number: "3.16", order: 79, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "adaptive, inclusive strategies; staff development; modes of delivery" }
  - { number: "3.17", order: 80, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "synchronous learning activities" }
  - { number: "3.18", order: 81, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "asynchronous learning activities" }
  - { number: "3.19", order: 82, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment strategy: progressive, varied, authentic and inclusive" }
  - { number: "3.20", order: 83, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "principles for designing assessment" }
  - { number: "3.21", order: 84, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "themes for authentic assessment" }
  - { number: "3.22", order: 85, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formats for examining the themes" }
  - { number: "3.23", order: 86, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "integrated master's: unfamiliar problems and research skills" }
  - { number: "3.24", order: 87, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "qualities of good feedback" }
  - { number: "4.1", order: 89, componentType: paragraph, parent: "section 4", heading: "Benchmark standards; Table 1 and Table 2", gloss: "the minimum standards for the honours degree, with excellence indicated" }
  - { number: "4.2", order: 90, componentType: paragraph, parent: "section 4", heading: "Benchmark standards; Table 1 and Table 2", gloss: "most students exceed the minimum; Annex D for classes" }
  - { number: "4.3", order: 91, componentType: paragraph, parent: "section 4", heading: "Benchmark standards; Table 1 and Table 2", gloss: "why the standards are broad and generic" }
  - { number: "4.4", order: 92, componentType: paragraph, parent: "section 4", heading: "Benchmark standards; Table 1 and Table 2", gloss: "standards for the accredited degree link to the regulator's proficiency standards" }
  - { number: "4.5", order: 93, componentType: paragraph, parent: "section 4", heading: "Benchmark standards; Table 1 and Table 2", gloss: "master's standards; the two tables of benchmark outcomes" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of Biomedical Science and Biomedical Sciences degrees", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of Biomedical Science/Biomedical Sciences degrees", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "section headings 1 to 4", heading: "the four section heading lines", kind: "other: heading lines" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for S7 and SB6" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement", kind: "other: back matter, read for S8 (editions)" }
  - { number: "Appendix 1", heading: "Draft suggestions for threshold levels of achievement for Biomedical Science degrees based on HCPC standards of proficiency", kind: "other: a draft drawn from a body's standards (HCPC SoP via the IBMS portfolio); not the statement's own standards; read for SB5 and Part E" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 192 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/biomedical-science-and-biomedical-sciences-2023/1.2
  locator: { number: "1.2", headingPath: ["Context and purposes of Biomedical Science and Biomedical Sciences degrees", "Context and purposes"] }
  span: { start: 8956, end: 9410 }
  source: "A Biomedical Science degree will include all the key clinical laboratory specialities (Medical Microbiology (including virology), Clinical Biochemistry, Haematology and Transfusion Science, Clinical Immunology, Cellular Pathology/Histopathology and Clinical Genetics), enabling graduates to achieve the academic requirements needed to apply for registration with the Health and Care Professions Council (HCPC) as a Biomedical Scientist (protected title)."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "Biomedical Science (singular) degrees"
  addressee: provider
  verbs: ["include", "enabling", "achieve", "apply"]
  about: "all the clinical laboratory specialisms in the singular degree"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A Biomedical Science degree will take in every key clinical laboratory specialism, so that graduates meet the academic part of what they need to seek registration as a Biomedical Scientist, a protected title."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/1.4
  locator: { number: "1.4", headingPath: ["Context and purposes of Biomedical Science and Biomedical Sciences degrees", "Context and purposes"] }
  span: { start: 10900, end: 11156 }
  source: "Graduates from these courses will develop the qualities needed for employment in situations which require the exercise of professionalism, critical independent thought, personal responsibility and decision-making in complex and unpredictable circumstances."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates of either degree"
  addressee: learner
  verbs: ["develop", "require"]
  about: "qualities for demanding professional work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours graduates of either degree will build the qualities that work calls for where professionalism, independent critical thinking, personal responsibility and decisions in complex, unpredictable settings are needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of Biomedical Science and Biomedical Sciences degrees", "Purposes and characteristics of Biomedical Science/Biomedical Sciences degrees"] }
  span: { start: 14296, end: 14638 }
  source: "Graduates from Biomedical Science courses will develop skills and knowledge to enable interpretation of clinical laboratory and near-patient test results through their taught modules, completing the IBMS Registration Training portfolio and being HCPC registered, which facilitates a contribution to multidisciplinary approaches to healthcare."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Biomedical Science (singular) courses"
  addressee: learner
  verbs: ["develop", "enable"]
  about: "interpreting clinical laboratory and near-patient results"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will build the skills and knowledge to interpret results from clinical laboratory and near-patient tests, through their modules, the registration training portfolio and registration, so they can contribute to multidisciplinary healthcare."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/1.16
  locator: { number: "1.16", headingPath: ["Context and purposes of Biomedical Science and Biomedical Sciences degrees", "Equality, diversity and inclusion"] }
  span: { start: 16064, end: 16289 }
  source: "This Subject Benchmark Statement expects the biomedical science and/or biomedical sciences learning communities to commit to equity, inclusive access and practices that anticipate the diverse needs of their community members."
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["expects", "commit", "anticipate"]
  about: "a commitment to equity and inclusion"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The statement looks to the learning communities in these subjects to commit to equity, inclusive access and practice that foresees the varied needs of their members."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of Biomedical Science and Biomedical Sciences degrees", "Equality, diversity and inclusion"] }
  span: { start: 16295, end: 17646 }
  source: "This Statement asks the learning community to address issues of inclusion throughout, and advocates intentional support for diverse student cohorts, acknowledging that equality and diversity are inter-dependent. Promoting equity of opportunities for all, through considered course design and development, is underpinned by valuing and harnessing differences and treating everyone with dignity and respect. Course teams should create an environment that encourages openness and participation, where everyone feels respected, supported, valued and understands their personal responsibility for equality and inclusive practice. Inclusive environments for learning anticipate and accommodate the varied requirements of learners and ensures equitable access to educational opportunities. Biomedical Science and/or Biomedical Sciences courses should proactively raise awareness of equality, equity, diversity and inclusivity through integrated activities and discussions. They should be designed to address issues in global healthcare, including factors affecting access to good quality diagnosis and treatment. Course providers, staf f and students all have a role in, and responsibility for, promoting equality and diversity and challenging biases and stereotypes, that is regularly reviewed and updated in line with institutional and government guidance."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["address", "create", "raise", "designed"]
  about: "an inclusive environment and awareness of equality"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Inclusion runs through the whole statement; course teams should build an open, participative and respectful environment, courses should raise awareness of equality, equity, diversity and inclusion through integrated activity and address global healthcare issues, and everyone shares responsibility for promoting equality and challenging bias."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of Biomedical Science and Biomedical Sciences degrees", "Equality, diversity and inclusion"] }
  span: { start: 17652, end: 18981 }
  source: "Biomedical Science and/or Biomedical Sciences are subjects whose underpinnings rely upon objective observation. It is important, however, to recognise and proactively discuss and confront the historical factors that have influenced many aspects of these subject areas. Courses should critically engage with how the field has contributed to and benefited from social injustice by, for example, presenting a balanced and informed history of the field and acknowledging that influential scientists might have benefited from and perpetuated misogyny, racism, homophobia, ableism and other prejudices. Students will be encouraged to consider how individual biases, culture and society as a whole influence biomedical science and/or biomedical sciences, including what science is done, what is considered ethical, who does that science, how data is interpreted and how biological knowledge is used. This should include critical examination of current practices and incorporation of a diverse range of underrepresented sources, including work from scientists from marginalised communities, plus case studies and learning materials representing the full range of human diversity. Courses should be regularly reviewed to consider whether teaching materials and subject matter covered might inadvertently perpetuate biases and stereotypes."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["engage", "consider", "reviewed"]
  about: "confronting the history and biases of the field"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Though the subjects rest on objective observation, courses should engage critically with how the field has gained from and added to social injustice, encourage students to consider how bias, culture and society shape the science, draw on under-represented sources and diverse case studies, and review materials regularly for bias."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/1.19
  locator: { number: "1.19", headingPath: ["Context and purposes of Biomedical Science and Biomedical Sciences degrees", "Equality, diversity and inclusion"] }
  span: { start: 18987, end: 19883 }
  source: "Curricula should recognise the discoveries and contributions of Biologists and Biomedical Scientists with diverse backgrounds and identities and acknowledge that different cultural backgrounds provide different insights and lead to new discoveries. Furthermore, learners should have the opportunity to explore Biomedical Science and/or Biomedical Sciences topics that inspire them and allow them to situate their knowledge in the light of their lived experiences or cultural backgrounds. Students should be encouraged to evaluate both the positive and negative impacts of potential applications of biological discoveries and reflect on the ways in which knowledge of Biomedical Science and/or Biomedical Sciences might be exploited for political, commercial or capital ends, for example drug development and targeting, in ways that can further gender-based, ethnicity-based or other inequalities."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["recognise", "explore", "evaluate", "reflect"]
  about: "diverse contributors and the uses of knowledge"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Curricula should credit the work of biologists and Biomedical Scientists from varied backgrounds; learners should be able to explore topics that inspire them in the light of their own experience, and students should be encouraged to weigh the good and harm of applying discoveries, including uses that deepen inequality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/1.20
  locator: { number: "1.20", headingPath: ["Context and purposes of Biomedical Science and Biomedical Sciences degrees", "Accessibility"] }
  span: { start: 19906, end: 20235 }
  source: "Equity involves enabling access to the programme of study for people who have differing individual requirements alongside eliminating arbitrary and unnecessary barriers to successf ul learning. Access should be equitable and based on an individual’s potential to complete the Biomedical Science and/or Biomedical Sciences course."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["enabling", "eliminating", "complete"]
  about: "equitable access based on potential"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Equity means opening the course to people with different needs and removing arbitrary barriers to success; access should be fair and rest on a person's potential to complete the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/1.21
  locator: { number: "1.21", headingPath: ["Context and purposes of Biomedical Science and Biomedical Sciences degrees", "Accessibility"] }
  span: { start: 20241, end: 20856 }
  source: "Biomedical Science and/or Biomedical Sciences course teams must pay attention to ensuring that curricula, pedagogy, assessments and practical elements of courses are designed to be fully accessible and flexibly designed. All students should be offered learning and assessment opportunities that are equally accessible to them, using inclusive design wherever possible and by means of reasonable individual adjustments where necessary. Learning and assessment experiences should be diverse to reflect the variety of the subject, to test a range of academic and practical skills and to increase accessibility for all."
  stem: none
  statementType: expectation
  rung: none
  force: must
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["pay", "designed", "offered"]
  about: "fully accessible curricula and assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Course teams must make sure curricula, teaching, assessment and practical work are designed to be fully accessible and flexible; all students should have equally accessible learning and assessment, by inclusive design where possible and individual adjustment where needed, and both should be varied."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of Biomedical Science and Biomedical Sciences degrees", "Accessibility"] }
  span: { start: 20862, end: 21589 }
  source: "Equitable access to the course for all students should be proactively and flexibly considered in an anticipatory way, including fieldwork, laboratory work and placements. Different requirements should be addressed with flexibility in assessment and teaching methods built in. Social capital, culture, sexuality, disability, neurodiversity and other characteristics should not prevent students from having equitable access to the entire curriculum. The team should refine and improve the course to remove barriers in response to feedback. Course teams should work in close collaboration with student support to ensure both the staf f member and student are fully supported to ensure the curriculum is accessible to all students."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["considered", "addressed", "prevent", "refine", "improve", "work"]
  about: "anticipating access in practical work and placements"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Equitable access for every student should be considered in advance and flexibly, including fieldwork, laboratory work and placements; teams should build flexibility into teaching and assessment, keep personal characteristics from limiting access to the curriculum, act on feedback, and work with student support."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/1.25
  locator: { number: "1.25", headingPath: ["Context and purposes of Biomedical Science and Biomedical Sciences degrees", "Sustainability"] }
  span: { start: 23433, end: 23765 }
  source: "To support the inclusion of sustainable development within Biomedical Science and/or Biomedical Sciences, users should refer to the QAA and Advance HE Education for Sustainable Development Guidance to address teaching and learning for sustainable development, key competencies, learning outcomes and assessment within the curricula."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["refer", "address"]
  about: "using the ESD guidance"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Those building sustainable development into these courses should use the QAA and Advance HE guidance on Education for Sustainable Development for teaching, key competencies, outcomes and assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/1.30
  locator: { number: "1.30", headingPath: ["Context and purposes of Biomedical Science and Biomedical Sciences degrees", "Enterprise and entrepreneurship education"] }
  span: { start: 26516, end: 26724 }
  source: "The student will take responsibility for continuing personal and professional development, demonstrating a commitment to learning and self-improvement and supporting the development of others, as appropriate."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subjects"
  addressee: learner
  verbs: ["take", "demonstrating", "supporting"]
  about: "continuing personal and professional development"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students will take charge of their own continuing personal and professional development, showing commitment to learning and self-improvement and, where fitting, helping others develop."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Design"] }
  span: { start: 27484, end: 27568 }
  source: "Students should confirm the accreditation status of the programme before they apply."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "prospective students"
  addressee: learner
  verbs: ["confirm", "apply"]
  about: "checking accreditation before applying"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Applicants should check whether a course is accredited before applying."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Design"] }
  span: { start: 30283, end: 30489 }
  source: "Credit-bearing placements should, however, be integrated within the programme of study, so that students can relate their experience to, and use the skills that they have developed in, their academic study."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["integrated", "relate", "use"]
  about: "integrating credit-bearing placements"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Where placements carry credit, they should be woven into the programme so students can connect what they experience with their academic work and use the skills they built there."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Design"] }
  span: { start: 31212, end: 31383 }
  source: "The academic component of degree apprenticeships in Biomedical Science or Healthcare Science Practitioner should follow the guidelines in this Subject Benchmark Statement."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["follow"]
  about: "degree apprenticeships follow the statement"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The academic part of Biomedical Science or Healthcare Science Practitioner degree apprenticeships should follow this statement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Design"] }
  span: { start: 31626, end: 32127 }
  source: "All degree courses covered in this Statement can ensure that all students are offered learning and assessment opportunities that are equally accessible to them, as described in the Equality, diversity and inclusion section. This should be incorporated by means of inclusive design wherever possible and by means of reasonable individual adjustments where necessary. Learning and assessment experiences should be diverse to both reflect the variety of the subject and to increase accessibility for all."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["ensure", "incorporated", "reflect", "increase"]
  about: "equally accessible learning and assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses can offer all students equally accessible learning and assessment; this should come through inclusive design where possible and reasonable adjustment where needed, and learning and assessment should be varied."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Design"] }
  span: { start: 32132, end: 32504 }
  source: "Biomedical Science and/or Biomedical Sciences course teams can also ensure that curricula, pedagogy, assessments and practical elements of courses are designed to be fully accessible. All learners should be supported in their development of the full range of verbal, spatial and numerical skills, alongside other approaches required to successf ully complete their course."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["ensure", "supported"]
  about: "support for verbal, spatial and numerical skills"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Course teams can make the course fully accessible, and all learners should be supported to develop the verbal, spatial and numerical skills, and other approaches, they need to complete it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Progression"] }
  span: { start: 32521, end: 33472 }
  source: "Biomedical Science and/or Biomedical Sciences degree course should be designed to promote academic and personal development. Initially, students will apply their knowledge and understanding of simple concepts to solve well-defined problems. As the course advances, they will develop confidence in their subject-specific knowledge and understanding, making connections between more challenging and complex concepts that enable them to analyse and evaluate data and problem solve effectively. On graduation, students will be competent in a range of knowledge, understanding, experience and skills. Graduates from Biomedical Science degrees only (following an appropriate period of clinical training, and completion of the IBMS Certificate of Competence) are equipped to begin a career as an HCPC-registered Biomedical Scientist. Graduates from both Biomedical Science and Biomedical Sciences programmes may find employment in a variety of other sectors."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject area"
  addressee: both
  verbs: ["designed", "promote", "apply", "develop", "analyse", "evaluate"]
  about: "progression from simple concepts to graduate competence"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Degree courses should be designed to foster academic and personal growth: students will move from applying simple ideas to well-defined problems to linking complex concepts, analysing and evaluating data and solving problems, and will be competent across knowledge, understanding, experience and skills on graduating."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.10.b1
  locator: { number: "2.10.b1", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Progression"] }
  span: { start: 33857, end: 33933 }
  source: "recognise the diversity of prior experience and the challenges of transition"
  stem: "2.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "learning, teaching and assessment methods"
  addressee: provider
  verbs: ["recognise"]
  about: "diverse prior experience and transition"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Progression should be reinforced by strategies that take account of how varied students' earlier experience is and how hard the move into university can be."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.10.b2
  locator: { number: "2.10.b2", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Progression"] }
  span: { start: 33936, end: 34117 }
  source: "allow all students to achieve their potential and realise their ambitions, irrespective of their background or motivations for studying Biomedical Science and/or Biomedical Sciences"
  stem: "2.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "learning, teaching and assessment methods"
  addressee: provider
  verbs: ["allow", "achieve", "realise"]
  about: "every student reaching their potential"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Progression should be reinforced by strategies that let every student reach their potential and ambitions, whatever their background or reasons for studying."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.10.b3
  locator: { number: "2.10.b3", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Progression"] }
  span: { start: 34120, end: 34185 }
  source: "support academic and personal development in addition to learning"
  stem: "2.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "learning, teaching and assessment methods"
  addressee: provider
  verbs: ["support"]
  about: "academic and personal development"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Progression should be reinforced by strategies that support academic and personal growth as well as learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.10.b4
  locator: { number: "2.10.b4", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Progression"] }
  span: { start: 34188, end: 34272 }
  source: "are matched to the course learning outcomes or competencies for each level of study."
  stem: "2.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "learning, teaching and assessment methods"
  addressee: provider
  verbs: ["matched"]
  about: "matched to outcomes at each level"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Progression should be reinforced by strategies that fit the course's learning outcomes or competencies at each level of study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Progression"] }
  span: { start: 34282, end: 35052 }
  source: "Students on a Biomedical Science and/or Biomedical Sciences degree course will progress from one level or academic stage to the next by satisf ying the regulations and processes for each institution. These require the students to demonstrate that they have met at least the threshold standard for the level of study. This will usually include successf ul completion and the award of credit for the full range of learning and assessment, including practical components. Students may also be required to meet additional criteria, such as passing all core clinical specialisms on an IBMS-approved Biomedical Science programme. The standard required to progress on a Biomedical Sciences integrated master’s degree course may also be higher than that for a bachelor’s course."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: fheq:6
  appliesTo: "courses in the subject area"
  addressee: learner
  verbs: ["progress", "demonstrate", "met"]
  about: "progressing by meeting at least the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students will progress between levels by meeting their institution's regulations, which require them to show at least the threshold standard for the level, usually with credit for all learning and assessment, practical work included; extra criteria may apply, such as passing every core clinical specialism on an accredited degree, and integrated master's courses may set a higher standard."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Flexibility"] }
  span: { start: 36812, end: 37156 }
  source: "Given that Biomedical Science and/or Biomedical Sciences courses must contain practical skills acquisition, course teams need to consider how they will support the development of practical skills, employing both bench practical sessions supported by online tutorials and virtual practical skills that may be acquired in a range of environments."
  stem: none
  statementType: expectation
  rung: none
  force: must
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["contain", "consider", "support"]
  about: "practical skills in every course"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Since the courses must include gaining practical skills, course teams need to plan how they will develop them, using bench practicals backed by online tutorials and virtual practice that can happen in various settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.15
  locator: { number: "2.15", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Flexibility"] }
  span: { start: 37162, end: 37570 }
  source: "Courses also need to be sufficiently flexible to be able to respond to and anticipate change, both in the advancement of the subject and its interface with other disciplines and in the needs of its graduates and their employers, as required. Courses should be sufficiently resilient to be able to adapt to unforeseen circumstances such as the Covid pandemic and other challenges that may arise in the future."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["respond", "anticipate", "adapt"]
  about: "flexible and resilient courses"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses need enough flexibility to respond to and anticipate change in the subject, its links with other disciplines and the needs of graduates and employers, and should be resilient enough to adapt to disruption such as a pandemic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.16
  locator: { number: "2.16", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Partnership"] }
  span: { start: 38048, end: 38334 }
  source: "Providers are expected to develop processes for oversight to ensure that partners involved in degree delivery meet all relevant standards and\n\n11\nexpectations. This should include effective communication and regular consultation to ensure that courses continue to meet employers’ needs."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["develop", "ensure", "meet"]
  about: "oversight of delivery partners"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Providers are expected to set up oversight so partners in degree delivery meet the relevant standards; this should include good communication and regular consultation so courses keep meeting employers' needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.17
  locator: { number: "2.17", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Partnership"] }
  span: { start: 38340, end: 39114 }
  source: "Courses should work with relevant stakeholders to incorporate work-based or work- like learning where possible. Enhancing student employability is a fundamental outcome for Biomedical Science and/or Biomedical Sciences courses. Therefore, engagement with the relevant employment sectors should be extensive. The courses should have a clear strategy for students to have the opportunity to develop employment-focused skills and engage with employers. Students may engage with employers through paid and/or unpaid placements of various durations during which students will be fully immersed in the workplace and experience the day-to-day routine of employment. Funding or payment should be considered to ensure that placement opportunities are inclusive and accessible to all."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["work", "incorporate", "develop", "engage", "considered"]
  about: "employability and inclusive placements"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses should bring in work-based or work-like learning with stakeholders, engage widely with employers, and have a clear strategy for employment-focused skills; funding or payment should be considered so placements are open to all."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Partnership"] }
  span: { start: 39667, end: 40569 }
  source: "Students should expect to be embraced as partners within their own courses. Student voice should play a significant role in course development, delivery, review and the overall student experience within Biomedical Science and/or Biomedical Sciences. Students are able to provide guidance, feedback and support for their own learning in several ways, this can be through departmental representatives, module, course and external student surveys such as the National Student Survey (NSS). Furthermore, students can feed into, and collaborate with, their students’ union, and many universities offer public social media platforms to receive feedback from students and discuss current trends in the student experience. Students should be involved in quality review processes and can be invaluable during the curriculum review and development of new courses where student steering groups may be established."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: both
  verbs: ["expect", "embraced", "play", "involved"]
  about: "students as partners in their courses"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should expect to be partners in their courses; student voice should shape course development, delivery and review, through representatives, surveys and other channels, and students should take part in quality review and the design of new courses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.21
  locator: { number: "2.21", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Monitoring and review"] }
  span: { start: 41185, end: 41474 }
  source: "Monitoring and review should include feedback from current students, external stakeholders, such as employers and placement providers, and alumni, to influence curriculum design, content and delivery. There should also be feedback from employers and apprentices for degree apprenticeships."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["include", "influence"]
  about: "feedback that informs review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Monitoring and review should draw on feedback from current students, employers, placement providers and alumni, and for degree apprenticeships from employers and apprentices, to shape the curriculum, its content and delivery."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.23
  locator: { number: "2.23", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Monitoring and review"] }
  span: { start: 41641, end: 41814 }
  source: "Evaluation of student performance data and various measures of the student experience should be integrated with expert review, including that provided by external examiners."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["integrated"]
  about: "data and expert review together"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Evaluation of student performance and experience data should be combined with expert review, including external examiners' views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.24
  locator: { number: "2.24", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Monitoring and review"] }
  span: { start: 41905, end: 42130 }
  source: "Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Providers will use external reviewers in periodic review to gain an outside view of proposed changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/2.27
  locator: { number: "2.27", headingPath: ["Distinctive features of Biomedical Science/Biomedical Sciences degrees", "Monitoring and review"] }
  span: { start: 43172, end: 43928 }
  source: "Programme and course teams should also conduct regular monitoring and evaluation, with the support of independent evaluators and student feedback, to ensure continuous quality enhancement. Evaluation of student performance data as well as student feedback and student voice alongside other measures of the student experience should be integrated with expert review, including that provided by external examiners, to ensure the curricula remain current, engaging and accessible. Historic data may also enable trend analysis to measure progress and identify emerging issues. Students and graduates, as well as employers, service users and relevant professional bodies, should be actively involved in designing and delivering enhancements to courses of study."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["conduct", "ensure", "integrated", "involved"]
  about: "regular monitoring and enhancement"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Programme and course teams should monitor and evaluate regularly, with independent evaluators and student feedback, combining performance data and student voice with expert review so curricula stay current, engaging and accessible; students, graduates, employers, service users and professional bodies should help design and deliver enhancements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.2
  locator: { number: "3.2", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 47422, end: 47852 }
  source: "Biomedical Science courses are required to cover all the clinical laboratory specialisms as detailed in the IBMS accreditation criteria which form an important basis for registration as a Biomedical Scientist. These degrees may be called either ‘Biomedical Science’ or ‘Healthcare Science’ but must be accredited by IBMS in order for graduates to meet the academic requirements for registration with HCPC as Biomedical Scientists."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["required", "cover", "accredited", "meet"]
  about: "full specialism coverage and accreditation"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science courses must cover all the clinical laboratory specialisms set out in the professional body's accreditation criteria, and such degrees, whether called Biomedical Science or Healthcare Science, must hold that body's accreditation so their graduates satisfy the academic conditions for registration."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 48127, end: 48673 }
  source: "Through a systems-led approach, students will integrate the clinical laboratory specialities with underpinning knowledge of Biomedical Science processes, investigation and treatment used for specific diseases. Biomedical Science graduates are aware of the current laboratory methods available for the study, investigation, diagnosis and monitoring of human health and disease in clinical and research environments. This includes an appreciation of the development and evaluation of new and current methods and therapeutic intervention strategies."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students and graduates of Biomedical Science (singular) courses"
  addressee: learner
  verbs: ["integrate"]
  about: "integrating the specialisms by body system"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Working system by system, students will bring the clinical laboratory specialisms together with the underlying science of disease processes, investigation and treatment; graduates know the current laboratory methods for studying, diagnosing and monitoring health and disease, and how new methods and therapies are developed and evaluated."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 48732, end: 49121 }
  source: "IBMS-accredited Biomedical Science or Healthcare Science courses will contain the following clinical pathology subject areas. Graduates are required to have studied and passed all subject specialisms in order to meet the education standards required for registration with HCPC, following completion of both the degree programme and verification of the IBMS Registration Training Portfolio."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "IBMS-accredited Biomedical Science or Healthcare Science courses and their graduates"
  addressee: both
  verbs: ["contain", "required", "studied", "passed", "meet"]
  about: "the clinical pathology subject areas, all studied and passed"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Accredited Biomedical Science or Healthcare Science courses will include the clinical pathology subject areas below, beyond the common content, and graduates are required to have studied and passed every specialism to meet the education standards for registration, once both the degree and the training portfolio are complete."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b2
  locator: { number: "3.4.b2", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 49331, end: 49455 }
  source: "the gross structure and ultrastructure of normal cells and tissues and the structural changes which may occur during disease"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "normal and diseased cell and tissue structure"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know how normal cells and tissues are built, at gross and fine scale, and how disease alters that structure."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b3
  locator: { number: "3.4.b3", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 49458, end: 49516 }
  source: "reproductive science, including infertility and embryology"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "reproductive science"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know reproductive science, with infertility and the study of embryos."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b4
  locator: { number: "3.4.b4", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 49519, end: 49583 }
  source: "the preparation of cells and tissues for microscopic examination"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "preparing cells and tissues for microscopy"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know how cells and tissues are prepared for examination under the microscope."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b5
  locator: { number: "3.4.b5", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 49586, end: 49722 }
  source: "the principles and applications of visualisation and imaging techniques, including microscopy, to aid diagnosis and treatment selection."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "visualisation and imaging in diagnosis"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the principles and uses of imaging and visualisation methods, microscopy among them, in supporting diagnosis and the choice of treatment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b7
  locator: { number: "3.4.b7", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 49930, end: 50014 }
  source: "the range of common methods used for the collection and analysis of clinical samples"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "collecting and analysing clinical samples"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the common methods for collecting clinical samples and analysing them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b8
  locator: { number: "3.4.b8", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 50017, end: 50162 }
  source: "investigations of major body and organ systems - for example, renal function tests, liver function tests, tumour marker tests, bone profile tests"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "investigating major organ systems"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know how the main body and organ systems are investigated, for example through kidney, liver, bone profile and tumour marker tests."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b9
  locator: { number: "3.4.b9", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 50165, end: 50293 }
  source: "the principles and applications of biochemical investigations used for screening, diagnosis, treatment and monitoring of disease"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "biochemical investigations across the course of disease"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the principles and uses of biochemical tests in screening for disease, diagnosing it, treating it and following its course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b10
  locator: { number: "3.4.b10", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 50296, end: 50361 }
  source: "therapeutic drug monitoring and investigation of substance abuse."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "drug monitoring and substance misuse"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know monitoring of therapeutic drugs and the investigation of substance misuse."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b12
  locator: { number: "3.4.b12", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 50516, end: 50598 }
  source: "the principles of the function and measurement of effectors of the immune response"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "immune effectors and their measurement"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know how the effectors of the immune response work and how they are measured."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b13
  locator: { number: "3.4.b13", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 50601, end: 50774 }
  source: "the causes and consequences of abnormal immune function, neoplastic diseases and transplantation reactions together with their detection, diagnosis, treatment and monitoring"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "abnormal immune function and its management"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know why immune function goes wrong and what follows, neoplastic disease and transplant reactions included, and how these are detected, diagnosed, treated and followed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b14
  locator: { number: "3.4.b14", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 50777, end: 50926 }
  source: "principles and practice of immunological techniques used for screening, diagnosis, treatment and monitoring of disease prophylaxis and immunotherapy."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "immunological techniques"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the principles and practice of immunological methods in screening, diagnosis, treatment and follow-up, with prophylaxis and immunotherapy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b16
  locator: { number: "3.4.b16", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 51136, end: 51189 }
  source: "the structure, function and production of blood cells"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "blood cells"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know how blood cells are formed, built and work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b17
  locator: { number: "3.4.b17", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 51192, end: 51228 }
  source: "the regulation of normal haemostasis"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "normal haemostasis"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know how normal haemostasis is regulated."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b18
  locator: { number: "3.4.b18", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 51231, end: 51337 }
  source: "blood cell morphology - identification of normal white blood cells and common red blood cell abnormalities"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "blood cell morphology"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the appearance of blood cells: recognising normal white cells and the usual red cell abnormalities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b19
  locator: { number: "3.4.b19", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 51340, end: 51438 }
  source: "nature and diagnosis of anaemias, haematological malignancies, haemorrhagic and thrombotic disease"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "anaemias, malignancies and bleeding and clotting disorders"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the nature and diagnosis of anaemias, blood cancers and disorders of bleeding and thrombosis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b20
  locator: { number: "3.4.b20", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 51441, end: 51561 }
  source: "principles and practice of haematological techniques used for screening, diagnosis, treatment and monitoring of disease."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "haematological techniques"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the principles and practice of haematology methods in screening, diagnosis, treatment and follow-up."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b22
  locator: { number: "3.4.b22", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 51761, end: 51844 }
  source: "interpretation of blood groups, causes of blood group anomalies, antibody screening"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "blood grouping and antibody screening"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know interpreting blood groups, the causes of grouping anomalies, and screening for antibodies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b23
  locator: { number: "3.4.b23", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 51847, end: 51913 }
  source: "the genetics, inheritance, structure and role of red cell antigens"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "red cell antigens"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the genetics, inheritance, structure and role of antigens on red cells."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b24
  locator: { number: "3.4.b24", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 51916, end: 51958 }
  source: "immune-mediated destruction of blood cells"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "immune destruction of blood cells"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the destruction of blood cells by the immune system."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b25
  locator: { number: "3.4.b25", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 51961, end: 52013 }
  source: "the preparation, storage and use of blood components"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "blood components"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know how blood components are prepared, stored and used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b26
  locator: { number: "3.4.b26", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 52016, end: 52040 }
  source: "patient blood management"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "patient blood management"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know patient blood management."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b27
  locator: { number: "3.4.b27", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 52043, end: 52134 }
  source: "the selection of appropriate blood components for transfusion and possible adverse effects."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "selecting components for transfusion"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know choosing suitable blood components for transfusion, and the adverse effects that can follow."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b29
  locator: { number: "3.4.b29", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 52314, end: 52408 }
  source: "genomic, transcriptomic, proteomic methods used to analyse and study human chromosomes and DNA"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "omic methods for chromosomes and DNA"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know genomic, transcriptomic and proteomic methods for analysing human chromosomes and DNA."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b30
  locator: { number: "3.4.b30", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 52411, end: 52478 }
  source: "the application of molecular biology and bioinformatics in medicine"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "molecular biology and bioinformatics in medicine"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know how molecular biology and bioinformatics are applied in medicine."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b31
  locator: { number: "3.4.b31", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 52481, end: 52523 }
  source: "pharmacogenetics and personalised medicine"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "pharmacogenetics"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know pharmacogenetics and personalised medicine."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b32
  locator: { number: "3.4.b32", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 52526, end: 52671 }
  source: "principles and practice of techniques used for genetic testing for screening, diagnosis and monitoring of disease, and associated ethical issues."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "genetic testing"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the principles and practice of genetic testing in screening, diagnosis and follow-up, and the ethical questions it raises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b34
  locator: { number: "3.4.b34", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 52926, end: 52980 }
  source: "the pathogenic mechanisms of a range of microorganisms"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "how microorganisms cause disease"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the mechanisms by which a range of microorganisms cause disease."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b35
  locator: { number: "3.4.b35", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 52983, end: 53089 }
  source: "public health microbiology (epidemiology and control of infectious diseases) and the concept of One Health"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "public health microbiology"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know public health microbiology, the epidemiology and control of infection, and the One Health concept."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b36
  locator: { number: "3.4.b36", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 53092, end: 53381 }
  source: "principles and practice of techniques used for screening, diagnosis, treatment and monitoring of a range of infectious diseases, involving a range of methods to detect and identify microorganisms, prevention and control of infection, including vaccination, environmental and vector control"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "detecting and controlling infection"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the principles and practice of methods for screening, diagnosing, treating and following infectious diseases, for detecting and identifying microorganisms, and for preventing and controlling infection, vaccination and environmental and vector control included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b37
  locator: { number: "3.4.b37", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 53384, end: 53493 }
  source: "antimicrobial chemotherapy, antimicrobial resistance (antibiotics, antivirals, antifungals, anti-parasitics)."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "antimicrobials and resistance"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know antimicrobial chemotherapy and resistance to antibiotics, antivirals, antifungals and anti-parasitic drugs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b39
  locator: { number: "3.4.b39", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 53724, end: 53859 }
  source: "the principles and applications of investigations used in screening, diagnosis, treatment and monitoring of disease using NPT equipment"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "near-patient investigations"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the principles and uses of investigations run on near-patient testing equipment for screening, diagnosis, treatment and follow-up."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b40
  locator: { number: "3.4.b40", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 53862, end: 53906 }
  source: "the application of NPT into patient pathways"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "near-patient testing in patient pathways"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know how near-patient testing fits into patient pathways."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b41
  locator: { number: "3.4.b41", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 53909, end: 53951 }
  source: "relevant quality assurance considerations."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "quality assurance in near-patient testing"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know the quality assurance points that bear on near-patient testing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b43
  locator: { number: "3.4.b43", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 54215, end: 54263 }
  source: "interpretation of quality control standards (QC)"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "quality control standards"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know how to interpret quality control standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b44
  locator: { number: "3.4.b44", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 54266, end: 54326 }
  source: "importance of quality assurance and pre-analytical variables"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "quality assurance and pre-analytical variables"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know why quality assurance and pre-analytical variables matter."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b45
  locator: { number: "3.4.b45", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 54329, end: 54400 }
  source: "an understanding of the importance of external quality assessment (EQA)"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "external quality assessment"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know why external quality assessment matters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b46
  locator: { number: "3.4.b46", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 54403, end: 54653 }
  source: "quality management (to include basic knowledge of the purpose of quality policy, audits, standard operating procedures, training and competency documentation, error logging and incident reporting, validation and verification, and reagent inventories)"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "quality management"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know quality management at a basic level: quality policy, audit, standard operating procedures, training and competency records, error and incident reporting, validation and verification, and reagent stock."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b47
  locator: { number: "3.4.b47", headingPath: ["Content, structure and delivery", "Content specific to Biomedical Science courses - clinical pathology subjects"] }
  span: { start: 54656, end: 54812 }
  source: "laboratory accreditation (to include basic awareness of UK Accreditation Service (UKAS) and International Organisation for Standardisation (ISO) standards)."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of IBMS-accredited Biomedical Science or Healthcare Science courses"
  addressee: learner
  verbs: []
  about: "laboratory accreditation"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Biomedical Science graduates will know laboratory accreditation, with a basic awareness of UKAS and ISO standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b2
  locator: { number: "3.6.b2", headingPath: ["Content, structure and delivery", "Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses"] }
  span: { start: 56036, end: 56127 }
  source: "molecular targets of drug action: receptors, enzymes, ion channels, transporters and others"
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Pharmacology courses"
  addressee: learner
  verbs: []
  about: "molecular drug targets"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Pharmacology graduates will know the molecular targets drugs act on, such as receptors, enzymes, ion channels and transporters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b3
  locator: { number: "3.6.b3", headingPath: ["Content, structure and delivery", "Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses"] }
  span: { start: 56130, end: 56253 }
  source: "drug-receptor relationships, including agonism, antagonism specificity, selectivity, potency, desensitisation and tolerance"
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Pharmacology courses"
  addressee: learner
  verbs: []
  about: "drug-receptor relationships"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Pharmacology graduates will know how drugs relate to receptors, covering agonism and antagonism, specificity and selectivity, potency, desensitisation and tolerance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b4
  locator: { number: "3.6.b4", headingPath: ["Content, structure and delivery", "Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses"] }
  span: { start: 56256, end: 56407 }
  source: "the main molecular targets for drugs, knowledge of their structure and function, and the ways in which drugs alter this function at the molecular level"
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Pharmacology courses"
  addressee: learner
  verbs: []
  about: "main drug targets and how drugs alter them"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Pharmacology graduates will know the structure and function of the main drug targets and how drugs change that function at molecular level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b5
  locator: { number: "3.6.b5", headingPath: ["Content, structure and delivery", "Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses"] }
  span: { start: 56410, end: 56546 }
  source: "how drug action affects the major organ systems of the body as well as drug effects on cell function, cell proliferation and cell death."
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Pharmacology courses"
  addressee: learner
  verbs: []
  about: "drug effects on organ systems and cells"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Pharmacology graduates will know how drugs act on the major organ systems and on cell function, proliferation and death."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b6
  locator: { number: "3.6.b6", headingPath: ["Content, structure and delivery", "Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses"] }
  span: { start: 56549, end: 56665 }
  source: "Pharmacokinetics (what the body does to drugs), including absorption, distribution, biotransformation and excretion."
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Pharmacology courses"
  addressee: learner
  verbs: []
  about: "pharmacokinetics"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Pharmacology graduates will know pharmacokinetics, what the body does to drugs: their absorption, distribution, biotransformation and excretion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b7
  locator: { number: "3.6.b7", headingPath: ["Content, structure and delivery", "Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses"] }
  span: { start: 56668, end: 56991 }
  source: "Individual variation in drug action and toxicity; for example, the effects of ethnicity, gender, age, pregnancy, genetic factors, disease and drug-drug interactions. Emerging technologies in personalised medicine (for example, small molecular inhibitors, antisense therapy, biopharmaceuticals, novel drug delivery systems)."
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Pharmacology courses"
  addressee: learner
  verbs: []
  about: "individual variation and personalised medicine"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Pharmacology graduates will know why people differ in drug response and toxicity, through ethnicity, gender, age, pregnancy, genes, disease and drug interactions, and the emerging technologies of personalised medicine."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b9
  locator: { number: "3.6.b9", headingPath: ["Content, structure and delivery", "Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses"] }
  span: { start: 57077, end: 57123 }
  source: "drug concentration/dose-response relationships"
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Pharmacology courses"
  addressee: learner
  verbs: []
  about: "concentration-response relationships"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Pharmacology graduates will know how drug concentration or dose relates to response."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b10
  locator: { number: "3.6.b10", headingPath: ["Content, structure and delivery", "Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses"] }
  span: { start: 57126, end: 57364 }
  source: "experimental methods and techniques applied to pharmacology (for example, bioassays, receptor binding, receptor cloning, recombinant proteins for therapy, animal models of disease, genetic manipulation of cells and animals and their uses)"
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Pharmacology courses"
  addressee: learner
  verbs: []
  about: "experimental methods in pharmacology"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Pharmacology graduates will know experimental methods used in pharmacology, such as bioassays, receptor binding and cloning, therapeutic recombinant proteins, animal disease models and genetic manipulation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b11
  locator: { number: "3.6.b11", headingPath: ["Content, structure and delivery", "Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses"] }
  span: { start: 57367, end: 57506 }
  source: "ethical and legal issues pertaining to the use of animals in research, with knowledge of approaches to replace, refine and reduce their use"
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Pharmacology courses"
  addressee: learner
  verbs: []
  about: "animals in research"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Pharmacology graduates will know the ethics and law of using animals in research, and ways to replace, refine and reduce that use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b12
  locator: { number: "3.6.b12", headingPath: ["Content, structure and delivery", "Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses"] }
  span: { start: 57509, end: 57657 }
  source: "drug discovery and development, including toxicology, with knowledge of the regulatory processes that monitor drug quality, safety and effectiveness"
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Pharmacology courses"
  addressee: learner
  verbs: []
  about: "drug discovery, development and regulation"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Pharmacology graduates will know how drugs are discovered and developed, toxicology included, and the regulation that oversees their quality, safety and effectiveness."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b13
  locator: { number: "3.6.b13", headingPath: ["Content, structure and delivery", "Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses"] }
  span: { start: 57660, end: 57902 }
  source: "principles of clinical trials; avoidance of bias, effect of sample size, placebo effect and the concept of therapeutic index. Ethical issues surrounding the use of human study participants and human tissues. Content in Human Nutrition courses"
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Pharmacology courses"
  addressee: learner
  verbs: []
  about: "clinical trials"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Pharmacology graduates will know the principles of clinical trials (bias, sample size, the placebo effect, therapeutic index) and the ethics of using human participants and tissues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b2
  locator: { number: "3.9.b2", headingPath: ["Content, structure and delivery", "Content in Human Nutrition courses"] }
  span: { start: 58905, end: 59085 }
  source: "the chemistry of living processes; the role of nutrients in the major metabolic pathways and the cellular and molecular basis of disease, including the processes of gene expression"
  stem: "3.9"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Human Nutrition courses"
  addressee: learner
  verbs: []
  about: "nutrients, metabolism and the cellular basis of disease"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Human Nutrition graduates will know the chemistry of life, how nutrients work in the main metabolic pathways, and the cellular and molecular roots of disease, gene expression included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b3
  locator: { number: "3.9.b3", headingPath: ["Content, structure and delivery", "Content in Human Nutrition courses"] }
  span: { start: 59088, end: 59199 }
  source: "the clinical biochemistry of human disease and its management, with a focus on the nutritional factors involved"
  stem: "3.9"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Human Nutrition courses"
  addressee: learner
  verbs: []
  about: "clinical biochemistry of disease and nutrition"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Human Nutrition graduates will know the clinical biochemistry of human disease and how it is managed, weighted towards nutritional factors."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b4
  locator: { number: "3.9.b4", headingPath: ["Content, structure and delivery", "Content in Human Nutrition courses"] }
  span: { start: 59202, end: 59450 }
  source: "the assessment of nutritional status and the key nutritional issues associated with different stages of the human life cycle as well as the relationship between socio-demographic, economic and environmental factors on dietary behaviour and patterns"
  stem: "3.9"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Human Nutrition courses"
  addressee: learner
  verbs: []
  about: "assessing nutritional status across the life cycle"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Human Nutrition graduates will know how nutritional status is assessed, the main nutritional issues at each life stage, and how socio-demographic, economic and environmental factors shape diet."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b5
  locator: { number: "3.9.b5", headingPath: ["Content, structure and delivery", "Content in Human Nutrition courses"] }
  span: { start: 59453, end: 59574 }
  source: "the concepts and processes associated with food science, food safety, food storage, food processing and food microbiology"
  stem: "3.9"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Human Nutrition courses"
  addressee: learner
  verbs: []
  about: "food science and safety"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Human Nutrition graduates will know the ideas and processes of food science, safety, storage, processing and microbiology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b6
  locator: { number: "3.9.b6", headingPath: ["Content, structure and delivery", "Content in Human Nutrition courses"] }
  span: { start: 59577, end: 59652 }
  source: "clinical nutrition, diet therapy and health promotion/nutritional education"
  stem: "3.9"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Human Nutrition courses"
  addressee: learner
  verbs: []
  about: "clinical nutrition and health promotion"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Human Nutrition graduates will know clinical nutrition, diet therapy, health promotion and nutrition education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b7
  locator: { number: "3.9.b7", headingPath: ["Content, structure and delivery", "Content in Human Nutrition courses"] }
  span: { start: 59655, end: 59733 }
  source: "nutritional issues associated with sports and exercise to maximise performance"
  stem: "3.9"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Human Nutrition courses"
  addressee: learner
  verbs: []
  about: "sport and exercise nutrition"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Human Nutrition graduates will know nutrition for sport and exercise performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b8
  locator: { number: "3.9.b8", headingPath: ["Content, structure and delivery", "Content in Human Nutrition courses"] }
  span: { start: 59736, end: 59831 }
  source: "gene nutrient interactions and their potential role in the prevention of diet-related diseases."
  stem: "3.9"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Human Nutrition courses"
  addressee: learner
  verbs: []
  about: "gene-nutrient interactions"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Human Nutrition graduates will know how genes and nutrients interact and what that may mean for preventing diet-related disease."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b9
  locator: { number: "3.9.b9", headingPath: ["Content, structure and delivery", "Content in Human Nutrition courses"] }
  span: { start: 59834, end: 60039 }
  source: "The impact of nutritional status on the nature of disease and core theoretical understanding of the multidisciplinary nature of human disease and its management. Content in Human/Medical Physiology courses"
  stem: "3.9"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Human Nutrition courses"
  addressee: learner
  verbs: []
  about: "nutrition and the nature of disease"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Human Nutrition graduates will know how nutritional status bears on disease, and a core theoretical sense that human disease and its care draw on many disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b2
  locator: { number: "3.11.b2", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 60902, end: 61044 }
  source: "chemical, cellular, tissue, organ, organ-system and organism levels, and the internal and external factors that regulate physiological systems"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "levels of organisation and regulation"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the levels of organisation from chemical to whole organism, and the internal and external factors that regulate body systems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b3
  locator: { number: "3.11.b3", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 61047, end: 61167 }
  source: "structure-function relationships and fundamental functions of each body system and interrelationships with other systems"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "structure and function of body systems"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know how structure relates to function in each body system, what each system fundamentally does and how the systems interrelate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b4
  locator: { number: "3.11.b4", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 61170, end: 61274 }
  source: "life processes, including metabolism, responsiveness, movement, growth, differentiation and reproduction"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "life processes"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the processes of life: metabolism, responsiveness, movement, growth, differentiation and reproduction."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b5
  locator: { number: "3.11.b5", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 61277, end: 61312 }
  source: "systems of cell-cell communication."
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "cell-cell communication"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the systems by which cells communicate with each other."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b7
  locator: { number: "3.11.b7", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 61351, end: 61404 }
  source: "homeostasis (autoregulation and extrinsic regulation)"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "homeostasis"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know homeostasis, both self-regulation and regulation from outside the organ."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b8
  locator: { number: "3.11.b8", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 61407, end: 61517 }
  source: "neural tissue, spinal cord, spinal nerves and spinal reflexes, brain and cranial nerves and neural integration"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "the nervous system"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know neural tissue, the spinal cord, spinal nerves and reflexes, the brain, cranial nerves and neural integration."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b9
  locator: { number: "3.11.b9", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 61520, end: 61626 }
  source: "fluid, electrolyte and acid-base balance, including control systems, and disturbances and impact on health"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "fluid, electrolyte and acid-base balance"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the balance of fluids, electrolytes, acids and bases, its control, its disturbances and their effect on health."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b10
  locator: { number: "3.11.b10", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 61629, end: 61725 }
  source: "the endocrine system, including hormone secretion, distribution and mechanisms of hormone action"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "the endocrine system"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the endocrine system: how hormones are secreted and distributed and how they act."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b11
  locator: { number: "3.11.b11", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 61728, end: 61771 }
  source: "response to internal and external stressors"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "stress responses"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know how the body responds to internal and external stressors."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b12
  locator: { number: "3.11.b12", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 61774, end: 61896 }
  source: "coordination, communication and integration of activity of body systems through neuronal, hormonal and chemical mechanisms"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "coordination of body systems"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know how neuronal, hormonal and chemical signals coordinate and integrate the work of body systems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b13
  locator: { number: "3.11.b13", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 61899, end: 61989 }
  source: "physiological response and regulation for adaption and survival in a changing environment."
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "adaptation and survival"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know how physiological responses and regulation allow adaptation and survival as the environment changes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b15
  locator: { number: "3.11.b15", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 62015, end: 62122 }
  source: "principal components of a human cell and the main transport processes and maintenance of cellular integrity"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "cell components and transport"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the main parts of a human cell, its chief transport processes and how it keeps itself intact."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b16
  locator: { number: "3.11.b16", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 62125, end: 62323 }
  source: "cellular differentiation, life cycle and diversity of cell types, and the complex intracellular chemical events that sustain life and underpin cellular response to the internal/external environment."
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "cell differentiation and diversity"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know how cells differentiate and cycle, the variety of cell types, and the intracellular chemistry that sustains life and drives cell responses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b18
  locator: { number: "3.11.b18", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 62359, end: 62481 }
  source: "structural and functional attributes of epithelial tissues, connective tissues and membranes, and tissue injury and repair"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "tissues, injury and repair"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the structure and function of epithelial and connective tissues and membranes, and how tissues are injured and repaired."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b19
  locator: { number: "3.11.b19", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 62484, end: 62560 }
  source: "fundamental appreciation of skin, bone structure, skeleton and articulations"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "skin, bone and joints"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the basics of skin, bone structure, the skeleton and joints."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b20
  locator: { number: "3.11.b20", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 62563, end: 62613 }
  source: "skeletal muscle and other types of muscular tissue"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "muscle"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know skeletal muscle and the other kinds of muscle tissue."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b21
  locator: { number: "3.11.b21", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 62616, end: 62691 }
  source: "exercise physiology and impact of exercise and related nutritional aspects."
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "exercise physiology"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know exercise physiology, the effects of exercise and the nutrition linked to it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b23
  locator: { number: "3.11.b23", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 62718, end: 62854 }
  source: "cardiovascular system, including nature of blood and haemostasis, heartbeat and cardiodynamics, cardiovascular physiology and regulation"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "the cardiovascular system"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the cardiovascular system: blood and haemostasis, the heartbeat and cardiodynamics, and cardiovascular physiology and its regulation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b24
  locator: { number: "3.11.b24", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 62857, end: 62921 }
  source: "lymphatic system, including organisation, defences and immunity."
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "the lymphatic system"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the lymphatic system, its organisation, defences and immunity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b26
  locator: { number: "3.11.b26", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 62950, end: 62983 }
  source: "respiratory system and physiology"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "respiration"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the respiratory system and its physiology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b27
  locator: { number: "3.11.b27", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 62986, end: 63124 }
  source: "digestive and hepatobiliary systems, including components/organs and processes of digestion and absorption, detoxification and elimination"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "digestion and the hepatobiliary system"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the digestive and hepatobiliary systems: their organs and the processes of digestion, absorption, detoxification and elimination."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b28
  locator: { number: "3.11.b28", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 63127, end: 63152 }
  source: "metabolism and energetics"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "metabolism and energetics"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know metabolism and energetics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b29
  locator: { number: "3.11.b29", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 63159, end: 63213 }
  source: "urinary system and the principles of renal physiology."
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "the urinary system"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the urinary system and the principles of kidney physiology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b31
  locator: { number: "3.11.b31", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 63238, end: 63293 }
  source: "reproductive systems and integration with other systems"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "reproductive systems"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the reproductive systems and how they integrate with other systems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b32
  locator: { number: "3.11.b32", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 63296, end: 63399 }
  source: "development and inheritance, including fertilisation, pregnancy, prenatal development and foetal growth"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "development and inheritance"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know development and inheritance, from fertilisation and pregnancy through prenatal development to foetal growth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b33
  locator: { number: "3.11.b33", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 63402, end: 63455 }
  source: "aspects of human inheritance, development and ageing."
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "inheritance, development and ageing"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know features of human inheritance, development and ageing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b35
  locator: { number: "3.11.b35", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 63533, end: 63644 }
  source: "ethical and legal issues pertaining to the use of humans or animals (or tissues) in research and other contexts"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "ethics and law of human and animal research"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the ethics and law of using people, animals or tissues in research and elsewhere."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b36
  locator: { number: "3.11.b36", headingPath: ["Content, structure and delivery", "Content in Human/Medical Physiology courses"] }
  span: { start: 63647, end: 63817 }
  source: "core physiological techniques and practical skills, including experimental design, measurement, data handling and statistical analysis. Approaches to study in all courses"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of Physiology courses"
  addressee: learner
  verbs: []
  about: "core physiological techniques"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Physiology graduates will know the core techniques and practical skills of physiology: experimental design, measurement, data handling and statistical analysis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.13
  locator: { number: "3.13", headingPath: ["Content, structure and delivery", "Approaches to study in all courses"] }
  span: { start: 66041, end: 66409 }
  source: "Graduate attributes integrated in all courses facilitate students to acquire graduate and professional attributes appropriate to Biomedical Science, Biomedical Sciences, Pharmacology, Nutrition and Human Physiology, and will recognise that much of what they\n\n20\nare taught is likely to change in the future, particularly in the light of continuing scientific advances."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of all the courses in the area"
  addressee: learner
  verbs: ["facilitate", "acquire", "recognise"]
  about: "graduate attributes and the provisional state of knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Graduate attributes built into every course help students gain the graduate and professional attributes fitting their subject, and students will recognise that much of what they learn is likely to change as science advances."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b1
  locator: { number: "3.14.b1", headingPath: ["Content, structure and delivery", "Approaches to study in all courses"] }
  span: { start: 66476, end: 66564 }
  source: "an appreciation of the complexity and diversity of human processes in health and disease"
  stem: "3.14"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of all the courses in the area"
  addressee: learner
  verbs: []
  about: "the complexity of human processes"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Graduates acquire an appreciation of how complex and varied human processes are in health and disease."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b2
  locator: { number: "3.14.b2", headingPath: ["Content, structure and delivery", "Approaches to study in all courses"] }
  span: { start: 66567, end: 66786 }
  source: "the ability to read and evaluate appropriate literature with a full and critical understanding, including the context, aims, objectives, experimental design, methodology, data interpretation and application of the study"
  stem: "3.14"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of all the courses in the area"
  addressee: learner
  verbs: ["read", "evaluate"]
  about: "reading and evaluating literature"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Graduates acquire the ability to read and judge relevant literature critically and in full, from its aims and design to its methods, data interpretation and use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b3
  locator: { number: "3.14.b3", headingPath: ["Content, structure and delivery", "Approaches to study in all courses"] }
  span: { start: 66789, end: 66996 }
  source: "the capacity to give a clear, current and accurate account of their subject area, the ability to critically discuss and debate both with specialists and non-specialists, using appropriate scientific language"
  stem: "3.14"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of all the courses in the area"
  addressee: learner
  verbs: ["give", "discuss", "debate"]
  about: "explaining and debating the subject"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Graduates acquire the capacity to explain the subject clearly, currently and accurately, and to discuss and debate it critically with specialists and non-specialists in suitable scientific language."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b4
  locator: { number: "3.14.b4", headingPath: ["Content, structure and delivery", "Approaches to study in all courses"] }
  span: { start: 66999, end: 67170 }
  source: "critical and analytical skills, including a recognition that statements and hypotheses should be tested, and that evidence is subject to assessment and critical evaluation"
  stem: "3.14"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of all the courses in the area"
  addressee: learner
  verbs: ["tested"]
  about: "critical and analytical skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Graduates acquire critical and analytical skills, with the recognition that claims and hypotheses need testing and evidence needs weighing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b5
  locator: { number: "3.14.b5", headingPath: ["Content, structure and delivery", "Approaches to study in all courses"] }
  span: { start: 67173, end: 67288 }
  source: "the ability to successf ully apply a variety of methods of study in investigating, recording and analysing material"
  stem: "3.14"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of all the courses in the area"
  addressee: learner
  verbs: ["apply"]
  about: "methods of study"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Graduates acquire the ability to use a variety of study methods to investigate, record and analyse material."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b6
  locator: { number: "3.14.b6", headingPath: ["Content, structure and delivery", "Approaches to study in all courses"] }
  span: { start: 67291, end: 67363 }
  source: "the ability to think independently, work autonomously and solve problems"
  stem: "3.14"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of all the courses in the area"
  addressee: learner
  verbs: ["think", "work", "solve"]
  about: "independent thinking and problem solving"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Graduates acquire the ability to think for themselves, work autonomously and solve problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b7
  locator: { number: "3.14.b7", headingPath: ["Content, structure and delivery", "Approaches to study in all courses"] }
  span: { start: 67366, end: 67494 }
  source: "an understanding of how to identify, protect and exploit intellectual property (IP) as part of the scientific innovation process"
  stem: "3.14"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of all the courses in the area"
  addressee: learner
  verbs: ["identify", "protect", "exploit"]
  about: "intellectual property"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Graduates acquire an understanding of how intellectual property is identified, protected and exploited in scientific innovation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b8
  locator: { number: "3.14.b8", headingPath: ["Content, structure and delivery", "Approaches to study in all courses"] }
  span: { start: 67497, end: 67682 }
  source: "an appreciation of the global reach of the subject area, the impact on human life and the environment and the ethical considerations implicit in their application. Teaching and learning"
  stem: "3.14"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of all the courses in the area"
  addressee: learner
  verbs: []
  about: "global reach, impact and ethics"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Graduates acquire an appreciation of the subject's global reach, its effects on human life and the environment, and the ethics of applying it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.16
  locator: { number: "3.16", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 68889, end: 69169 }
  source: "In this context, there is an expectation that all staf f who contribute to student learning – including demonstrators, and temporary and visiting lecturers, as well as permanent academic staf f – should have access to a range of educational professional development opportunities."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["contribute"]
  about: "professional development for all teaching staff"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "All staff who contribute to student learning, temporary and visiting staff and demonstrators as well as permanent academics, should be able to draw on a range of development in teaching and learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.19
  locator: { number: "3.19", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 71756, end: 71946 }
  source: "Assessments should be authentic, with real-world application to enhance employability skills and professional development; they should allow for reasonable adjustments to ensure inclusivity."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["enhance", "allow", "ensure"]
  about: "authentic and inclusive assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Assessments should be authentic, applied to real-world tasks that build employability and professional growth, and should allow reasonable adjustments so they are inclusive."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b1
  locator: { number: "3.20.b1", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 72028, end: 72109 }
  source: "assessment should be of, and for, learning and associated with effective feedback"
  stem: "3.20"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["associated"]
  about: "assessment of and for learning"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "In designing assessment, teams should consider the principle that assessment serves learning as well as measuring it, and comes with effective feedback."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b2
  locator: { number: "3.20.b2", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 72112, end: 72232 }
  source: "assessments should be valid, reliable and consistent, and provide a means for students to demonstrate mastery of a topic"
  stem: "3.20"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["provide", "demonstrate"]
  about: "valid, reliable, consistent assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "In designing assessment, teams should consider the principle that assessments are valid, reliable and consistent, and let students show mastery of a topic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b3
  locator: { number: "3.20.b3", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 72235, end: 72322 }
  source: "assessment and feedback should explicitly consider accessibility and EDI considerations"
  stem: "3.20"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["consider"]
  about: "accessibility and EDI in assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "In designing assessment, teams should consider the principle that assessment and feedback take explicit account of accessibility and EDI."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b4
  locator: { number: "3.20.b4", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 72325, end: 72422 }
  source: "information provided about assessment and feedback should be explicit, accessible and transparent"
  stem: "3.20"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: []
  about: "clear assessment information"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "In designing assessment, teams should consider the principle that information on assessment and feedback is explicit, accessible and transparent."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b5
  locator: { number: "3.20.b5", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 72425, end: 72535 }
  source: "assessment and feedback should be planned to ensure students and staf f can manage their workloads effectively"
  stem: "3.20"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["planned", "manage"]
  about: "manageable workloads"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "In designing assessment, teams should consider the principle that assessment and feedback are planned so that students and staff can manage their workloads."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b6
  locator: { number: "3.20.b6", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 72538, end: 72648 }
  source: "assessments and feedback should be integral to the course of study and clearly relate to the learning outcomes"
  stem: "3.20"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["relate"]
  about: "integral, aligned assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "In designing assessment, teams should consider the principle that assessment and feedback are part of the course and plainly tied to its learning outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b7
  locator: { number: "3.20.b7", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 72655, end: 72758 }
  source: "assessment and feedback should give the student the opportunity to validate knowledge and understanding"
  stem: "3.20"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["give", "validate"]
  about: "confirming knowledge through assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "In designing assessment, teams should consider the principle that assessment and feedback give students a chance to confirm what they know and understand."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b8
  locator: { number: "3.20.b8", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 72761, end: 72855 }
  source: "assessment and feedback should align with accreditation and approval requirements as necessary"
  stem: "3.20"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["align"]
  about: "alignment with accreditation"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "In designing assessment, teams should consider the principle that assessment and feedback meet accreditation and approval requirements where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b9
  locator: { number: "3.20.b9", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 72858, end: 72989 }
  source: "an appropriate balance of formative and summative assessments should be provided, with helpful interrelation between the two forms."
  stem: "3.20"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["provided"]
  about: "balancing formative and summative assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "In designing assessment, teams should consider the principle that formative and summative assessment are balanced and usefully linked."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/3.24
  locator: { number: "3.24", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 74044, end: 74476 }
  source: "Feedback should be personal/individual, understandable, empowering, manageable and developmental. It should be timely, relevant to the assessment brief and accompanied by access to interpretative support/advice. Feedback should allow students the opportunity for supportive reflection on their academic and professional development. The nature, extent and timing of feedback for each assessment task should be made clear in advance."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["allow", "made"]
  about: "qualities of good feedback"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Feedback should be personal, understandable, empowering, manageable and developmental, timely and relevant to the brief, with access to help in interpreting it; it should support reflection, and its nature, extent and timing should be made clear in advance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 75167, end: 75396 }
  source: "Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject area"
  addressee: provider
  verbs: ["refer"]
  about: "using Annex D for degree classes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do much better than the minimum; each provider decides how to evidence that, and should refer to Annex D, which describes the honours classes for degrees at FHEQ Level 6 and FQHEIS Level 10."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 76612, end: 76911 }
  source: "Describe and discuss the key concepts and phenomena relevant to the course (see section 3) confidently, accurately and in detail, using appropriate terminology, and be aware of the full breadth of Biomedical Science and/or Biomedical Sciences, from molecular to cellular, and from health to disease."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["describe", "discuss"]
  about: "key concepts across the subject"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will describe and discuss the main concepts and phenomena of the course accurately, confidently and in depth, in the right technical language, aware of the whole range of the subject from molecules to cells and from health to disease."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b1.excellent
  locator: { number: "4.5.b1.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 77086, end: 77289 }
  source: "Apply a comprehensive knowledge of concepts in Biomedical Science and/or Biomedical Sciences and phenomena to discuss and explain essential aspects of the course and show evidence of enquiry beyond this."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["apply", "discuss", "explain", "show"]
  about: "key concepts across the subject"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b1.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates apply a wide-ranging grasp of the subject's concepts to discuss and explain the core of the course, and show enquiry that goes past it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b1.threshold
  locator: { number: "4.5.b1.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 76912, end: 77085 }
  source: "Recall basic knowledge of key concepts in Biomedical Science and/or Biomedical Sciences and phenomena relevant to the course and explain these using appropriate terminology."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["recall", "explain"]
  about: "key concepts across the subject"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will recall the basics of the main concepts and phenomena met on the course and explain them in suitable technical terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 77290, end: 77522 }
  source: "Apply knowledge and understanding of human biological systems and methodologies to design experiments and to solve theoretical and practical problems, with awareness of appropriate controls, possible bias, ethics and sustainability."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["apply", "design", "solve"]
  about: "experimental design and problem solving"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will use knowledge of human biological systems and methods to plan experiments and solve problems in theory and practice, alert to controls, bias, ethics and sustainability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b2.excellent
  locator: { number: "4.5.b2.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 77745, end: 77933 }
  source: "Devise and evaluate solutions to solve both routine and unfamiliar problems using a range of methods, including awareness of appropriate controls, possible bias, ethics and sustainability."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["devise", "evaluate", "solve"]
  about: "experimental design and problem solving"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b2.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates devise and evaluate solutions to routine and unfamiliar problems by a range of methods, alert to controls, bias, ethics and sustainability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b2.threshold
  locator: { number: "4.5.b2.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 77523, end: 77744 }
  source: "Demonstrate an understanding of basic experimental design and application of methods to solve routine problems relevant to the course, with some awareness of appropriate controls, possible bias, ethics and sustainability."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "solve"]
  about: "experimental design and problem solving"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will show an understanding of basic experimental design and use methods on routine course problems, with some alertness to controls, bias, ethics and sustainability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 77934, end: 78129 }
  source: "Describe, document and enact saf e working practices in terms of managing biological, chemical, laboratory or sample-based risk, through knowledge-based risk assessments and practical activities."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["describe", "document", "enact"]
  about: "safe working and risk assessment"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will describe, record and practise safe working, managing biological, chemical, laboratory and sample risks through risk assessment and practical work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b3.excellent
  locator: { number: "4.5.b3.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 78241, end: 78351 }
  source: "Independently produce and apply risk assessments for completing practical work in a saf e and reliable manner."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["produce", "apply"]
  about: "safe working and risk assessment"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b3.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates write and apply risk assessments independently so that practical work is done safely and reliably."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b3.threshold
  locator: { number: "4.5.b3.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 78130, end: 78240 }
  source: "Produce and follow risk assessments for completing practical work in a saf e and reliable manner with support."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["produce", "follow"]
  about: "safe working and risk assessment"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will write and follow risk assessments so that practical work is done safely and reliably, with support."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 78352, end: 78564 }
  source: "Select and carry out appropriate quantitative and qualitative practical techniques to solve problems relevant to the course, including consideration of the theoretical basis and limitations of various techniques."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["select", "carry"]
  about: "practical laboratory techniques"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will choose and use suitable quantitative and qualitative practical techniques on course problems, weighing the theory behind each and its limits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b4.excellent
  locator: { number: "4.5.b4.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 78706, end: 78902 }
  source: "Design, optimise and demonstrate competence in a broad range of appropriate qualitative and quantitative practical techniques relevant to the course, with a high degree of autonomy and efficiency."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["design", "optimise", "demonstrate"]
  about: "practical laboratory techniques"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b4.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates design, refine and show competence in a broad range of suitable practical techniques, working with much autonomy and efficiency."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b4.threshold
  locator: { number: "4.5.b4.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 78565, end: 78705 }
  source: "Suggest and demonstrate competence in a broad range of appropriate qualitative and quantitative practical techniques relevant to the course."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["suggest", "demonstrate"]
  about: "practical laboratory techniques"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will propose, and show competence in, a broad range of suitable practical techniques, qualitative and quantitative, for the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 78903, end: 79065 }
  source: "Use appropriate databases, computational techniques and tools to aid further understanding and insight of Biomedical Science and/or Biomedical Sciences processes."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["use"]
  about: "databases and computational tools"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will use suitable databases and computational techniques and tools to deepen understanding of biomedical processes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b5.excellent
  locator: { number: "4.5.b5.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 79263, end: 79468 }
  source: "Select and apply appropriate computational techniques and tools to investigate complex Biomedical Science and/or Biomedical Sciences concepts and evaluate and report outcomes using appropriate terminology."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["select", "apply", "investigate", "evaluate", "report"]
  about: "databases and computational tools"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b5.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates choose and use suitable computational techniques and tools to investigate complex concepts, then evaluate and report the results in suitable terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b5.threshold
  locator: { number: "4.5.b5.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 79066, end: 79262 }
  source: "Apply computational techniques and tools to investigate familiar Biomedical Science and/or Biomedical Sciences concepts covered in course content and report outcomes using appropriate terminology."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["apply", "investigate", "report"]
  about: "databases and computational tools"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will use computational techniques and tools to investigate familiar course concepts and report the results in suitable terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 79473, end: 79587 }
  source: "Engage with literature from the Biomedical Science and/or Biomedical Sciences to develop insight into the subject."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["engage", "develop"]
  about: "engaging with the literature"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will read the literature of the subject to gain insight into it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b6.excellent
  locator: { number: "4.5.b6.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 79748, end: 79961 }
  source: "Identify and select appropriate sources of biological information, including primary literature, and appraise and evaluate the adequacy of methods, data and their interpretation with a high degree of independence."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["identify", "select", "appraise", "evaluate"]
  about: "engaging with the literature"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b6.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates find and choose suitable sources of biological information, primary literature among them, and judge the adequacy of their methods, data and interpretation with much independence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b6.threshold
  locator: { number: "4.5.b6.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 79588, end: 79747 }
  source: "Assess the evidence base for scientific claims, by accessing primary literature and commenting on the adequacy of the methods, data and interpretation therein."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["assess", "accessing", "commenting"]
  about: "engaging with the literature"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will judge the evidence behind scientific claims by going to primary literature and commenting on how adequate its methods, data and interpretation are."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 79962, end: 80081 }
  source: "Complete independent open-ended investigative work through a project/research- based assignment relevant to the course."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["complete"]
  about: "an independent investigative project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will complete open-ended investigative work independently through a project or research assignment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b7.excellent
  locator: { number: "4.5.b7.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 80331, end: 80595 }
  source: "Demonstrate highly independent and competent planning, execution and presentation of a piece of independently produced work which includes the analysis and critical evaluation of data, demonstrating high levels of time management, problem solving and independence."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "demonstrating"]
  about: "an independent investigative project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b7.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates plan, carry out and present a piece of independent work with marked independence and competence, analysing and critically evaluating data and showing strong time management, problem solving and independence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b7.threshold
  locator: { number: "4.5.b7.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 80082, end: 80330 }
  source: "Demonstrate planning, execution and presentation of a piece of independently produced work which includes analysis or evaluation of data within a supported framework, demonstrating some evidence of time management, problem solving and independence."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "demonstrating"]
  about: "an independent investigative project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will plan, carry out and present a piece of independent work that analyses or evaluates data within a supported framework, showing some time management, problem solving and independence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 80596, end: 80859 }
  source: "Appreciate the contribution of Biomedical Science and/or Biomedical Sciences to the innovations that characterise the modern world, and the potential of Biomedical Science and/or Biomedical Sciences graduates to develop solutions to current and future challenges."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["appreciate", "develop"]
  about: "the subject's contribution to world challenges"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will value what the subject brings to the innovations of the modern world and what its graduates can offer to present and future challenges."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b8.excellent
  locator: { number: "4.5.b8.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 81101, end: 81279 }
  source: "Explain, suggest and critique ways in which Biomedical Science and/or Biomedical Sciences and Biomedical Scientists can contribute to solving current and future world challenges."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["explain", "suggest", "critique"]
  about: "the subject's contribution to world challenges"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b8.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates explain, propose and critique ways in which the subject and its scientists can help solve present and future world challenges."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b8.threshold
  locator: { number: "4.5.b8.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 80860, end: 81100 }
  source: "Identify and discuss application of Biomedical Science and/or Biomedical Sciences in solving current and future challenges in the world and demonstrate some understanding of the role of Biomedical Scientists and research scientists in this."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["identify", "discuss", "demonstrate"]
  about: "the subject's contribution to world challenges"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will identify and discuss how the subject is applied to present and future world challenges, with some understanding of the part biomedical and research scientists play."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 81280, end: 81464 }
  source: "Recognise the relationships and interfaces between Biomedical Science and/or Biomedical Sciences and other subjects, enabling efficient interactions in a multidisciplinary environment."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["recognise", "enabling"]
  about: "links with other subjects"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will recognise how the subject relates to and meets other subjects, so as to work well in a multidisciplinary setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b9.excellent
  locator: { number: "4.5.b9.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 81605, end: 81806 }
  source: "Explain and evaluate the contribution of Biomedical Science and/or Biomedical Sciences to solving interdisciplinary challenges and the role of interdisciplinary thinking in solving scientific problems."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["explain", "evaluate"]
  about: "links with other subjects"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b9.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates explain and evaluate what the subject contributes to interdisciplinary challenges and how interdisciplinary thinking helps solve scientific problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b9.threshold
  locator: { number: "4.5.b9.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 81465, end: 81604 }
  source: "Identify and explain relationships between Biomedical Science and/or Biomedical Sciences and other subjects relevant to the course content."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["identify", "explain"]
  about: "links with other subjects"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will identify and explain how the subject relates to other subjects relevant to the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 81807, end: 81987 }
  source: "Deploy mathematical and statistical concepts, processes and tools, such as the manipulation of equations and graphical and statistical analysis, to solve problems or evaluate data."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["deploy", "solve", "evaluate"]
  about: "mathematics and statistics"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will use mathematical and statistical ideas, processes and tools, such as rearranging equations, graphs and statistical tests, for problem solving or data evaluation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b10.excellent
  locator: { number: "4.5.b10.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 82096, end: 82227 }
  source: "Select, use and evaluate appropriate mathematical and statistical concepts, processes and tools to solve problems or evaluate data."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["select", "use", "evaluate"]
  about: "mathematics and statistics"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b10.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates choose, use and evaluate suitable mathematical and statistical tools for problem solving or data evaluation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b10.threshold
  locator: { number: "4.5.b10.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 81988, end: 82095 }
  source: "Use mathematical and statistical concepts, processes and tools to solve familiar problems or evaluate data."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["use", "solve", "evaluate"]
  about: "mathematics and statistics"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will use mathematical and statistical tools on familiar problems or to evaluate data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b11
  locator: { number: "4.5.b11", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 82228, end: 83078 }
  source: "Collect qualitative and quantitative data from investigations relevant to the course, and analyse and interpret this data to allow testing of hypotheses, contextualising of findings, Demonstrate accurate data collection, including selection of appropriate methods for analysis, interpretation of findings to test hypotheses, consideration of further lines of Demonstrate independent and accurate data collection, including selection of appropriate methods for analysis, interpretation of findings to test hypotheses, consideration of further\n\n26\npresentation of findings, and suggestions for further lines of investigation. investigation and manipulation of data for effective presentation. lines of investigation and manipulation of data for effective presentation, with a thorough understanding of the context of the investigation within the field."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["collect", "analyse", "interpret"]
  about: "collecting and analysing data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will gather qualitative and quantitative data from course investigations, then analyse and interpret them to test hypotheses, set findings in context, present them and propose further lines of enquiry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b11.excellent
  locator: { number: "4.5.b11.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 82228, end: 83078 }
  source: "Collect qualitative and quantitative data from investigations relevant to the course, and analyse and interpret this data to allow testing of hypotheses, contextualising of findings, Demonstrate accurate data collection, including selection of appropriate methods for analysis, interpretation of findings to test hypotheses, consideration of further lines of Demonstrate independent and accurate data collection, including selection of appropriate methods for analysis, interpretation of findings to test hypotheses, consideration of further\n\n26\npresentation of findings, and suggestions for further lines of investigation. investigation and manipulation of data for effective presentation. lines of investigation and manipulation of data for effective presentation, with a thorough understanding of the context of the investigation within the field."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "collecting and analysing data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b11.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates collect data accurately and independently, with the same choices of analysis, interpretation, further enquiry and presentation, and a thorough sense of where the investigation sits in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b11.threshold
  locator: { number: "4.5.b11.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 82228, end: 83078 }
  source: "Collect qualitative and quantitative data from investigations relevant to the course, and analyse and interpret this data to allow testing of hypotheses, contextualising of findings, Demonstrate accurate data collection, including selection of appropriate methods for analysis, interpretation of findings to test hypotheses, consideration of further lines of Demonstrate independent and accurate data collection, including selection of appropriate methods for analysis, interpretation of findings to test hypotheses, consideration of further\n\n26\npresentation of findings, and suggestions for further lines of investigation. investigation and manipulation of data for effective presentation. lines of investigation and manipulation of data for effective presentation, with a thorough understanding of the context of the investigation within the field."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "collecting and analysing data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will collect data accurately, choosing suitable analysis, interpreting findings to test hypotheses, considering further enquiry and handling data to present them well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b12
  locator: { number: "4.5.b12", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 83079, end: 83191 }
  source: "Collaborate and work successf ully in a group environment, contributing positively and flexibly to team outputs."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["collaborate", "work", "contributing"]
  about: "teamwork"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will work well with others in a group, contributing positively and flexibly to what the team produces."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b12.excellent
  locator: { number: "4.5.b12.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 83286, end: 83476 }
  source: "Identify and apply effective strategies for working in a group environment and provide clear and valuable contributions to team outputs, demonstrating good teamwork and/or leadership skills."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["identify", "apply", "provide", "demonstrating"]
  about: "teamwork"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b12.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates find and use effective strategies for group work and make clear, valuable contributions to team outputs, showing good teamwork or leadership."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b12.threshold
  locator: { number: "4.5.b12.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 83192, end: 83285 }
  source: "Effectively participate in group and teamwork, demonstrating clear contributions to the work."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["participate", "demonstrating"]
  about: "teamwork"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will take an effective part in group and team work, with clear contributions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b13
  locator: { number: "4.5.b13", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 83477, end: 83589 }
  source: "Communicate effectively, selecting appropriate content, media and methods for the audience, purpose and subject."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["communicate", "selecting"]
  about: "communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will communicate well, choosing content, media and methods to suit audience, purpose and subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b13.excellent
  locator: { number: "4.5.b13.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 83708, end: 83916 }
  source: "Communicate information, ideas, problems and solutions to an accomplished level verbally and non-verbally, in an accurate, fluent and sophisticated style, at a level consistently appropriate for the audience."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["communicate"]
  about: "communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b13.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates convey information, ideas, problems and solutions to a high standard in speech and other forms, accurately, fluently and with sophistication, always pitched to the audience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b13.threshold
  locator: { number: "4.5.b13.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 83590, end: 83707 }
  source: "Communicate information, ideas, problems and solutions verbally and/or non-verbally, with clear expression and style."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["communicate"]
  about: "communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will convey information, ideas, problems and solutions in speech or other forms, expressed clearly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b14
  locator: { number: "4.5.b14", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 83917, end: 84141 }
  source: "Apply ethical awareness to working in Biomedical Science and/or Biomedical Sciences, appreciate the historical context of the subject and the societal impacts of advances in the Biomedical Science and/or Biomedical Sciences."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["apply", "appreciate"]
  about: "ethics, history and societal impact"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will bring ethical awareness to work in the subject and appreciate its history and the effects its advances have on society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b14.excellent
  locator: { number: "4.5.b14.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 84329, end: 84519 }
  source: "Understand and evaluate ethical issues and the societal impact of advances in Biomedical Science and/or Biomedical Sciences, with some understanding of the historical context of the subject."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["understand", "evaluate"]
  about: "ethics, history and societal impact"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b14.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates understand and evaluate the ethical issues and social effects of advances in the subject, with some understanding of its history."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b14.threshold
  locator: { number: "4.5.b14.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 84142, end: 84328 }
  source: "Describe some of the ethical issues and societal impacts of advances in Biomedical Science and/or Biomedical Sciences, with some acknowledgement of the historical context of the subject."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["describe"]
  about: "ethics, history and societal impact"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will describe some ethical issues and social effects of advances in the subject, with some acknowledgement of its history."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b15
  locator: { number: "4.5.b15", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 84520, end: 84680 }
  source: "Stay up to date with advances in Biomedical Science and/or Biomedical Sciences and appreciate the fluid nature of knowledge that evolves as new findings emerge."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["stay", "appreciate"]
  about: "keeping up with advances"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will keep up with advances in the subject and appreciate that knowledge shifts as new findings appear."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b15.excellent
  locator: { number: "4.5.b15.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 84938, end: 85135 }
  source: "Clear appreciation of the fluid nature of knowledge in Biomedical Science and/or Biomedical Sciences, including an ability to incorporate new findings into previous understanding of various topics."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates, at the excellent standard"
  addressee: learner
  verbs: ["incorporate"]
  about: "keeping up with advances"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b15.threshold, basis: stated }
  paraphrase: "At an excellent level, graduates show a clear grasp that knowledge in the subject is fluid, with the ability to fold new findings into earlier understanding."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b15.threshold
  locator: { number: "4.5.b15.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 84681, end: 84937 }
  source: "Awareness of how new findings may change current understandings of various topics in Biomedical Science and/or Biomedical Sciences, that many aspects of the subject are not fully understood and demonstrate some ability to stay up to date with new findings."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates, at the threshold standard"
  addressee: learner
  verbs: ["change", "demonstrate"]
  about: "keeping up with advances"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will show awareness that new findings may change how topics are understood and that much in the subject is not yet understood, with some ability to keep up to date."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b16
  locator: { number: "4.5.b16", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 85136, end: 85356 }
  source: "Act professionally, with due regard for legal, ethical and societal responsibilities, modelling good practice that promotes positive perceptions of Biomedical Science and/or Biomedical Sciences and Biomedical Scientists."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["act", "modelling", "promotes"]
  about: "professional conduct"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, graduates will act professionally, mindful of legal, ethical and social responsibilities, and model good practice that gives a positive view of the subject and its scientists."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b17
  locator: { number: "4.5.b17", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 85588, end: 85759 }
  source: "Develop, integrate, synthesise and apply the systematic and broad understanding of relevant and state-of-the-art biological/ biomedical concepts to solve complex problems."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["develop", "integrate", "synthesise", "apply", "solve"]
  about: "applying leading-edge understanding to complex problems"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "In addition to the honours outcomes, master's graduates should be able to develop, combine, synthesise and apply a systematic, broad understanding of current and leading-edge biomedical concepts to solve complex problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b17.excellent
  locator: { number: "4.5.b17.excellent", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 85799, end: 85847 }
  source: "With a high degree of independence and autonomy."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:7
  appliesTo: "master's graduates, at the excellent standard"
  addressee: learner
  verbs: []
  about: "leading-edge understanding, independently"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: { statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b17.threshold, basis: stated }
  paraphrase: "At an excellent level, the master's graduate does this with much independence and autonomy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b17.threshold
  locator: { number: "4.5.b17.threshold", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 85760, end: 85798 }
  source: "With significant support and guidance."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates, at the threshold standard"
  addressee: learner
  verbs: []
  about: "leading-edge understanding, with support"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "At threshold, the master's graduate does this with considerable support and guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b18
  locator: { number: "4.5.b18", headingPath: ["Benchmark standards", "Benchmark standards; Table 1 and Table 2"] }
  span: { start: 85848, end: 86466 }
  source: "Interrogate and integrate diverse sources of scientific literature alongside other information sources, in order to design and develop methods for investigation and analysis, including in areas at the forefront of knowledge and outside their current specialist knowledge. Project planning, including, as appropriate, evaluation of ethics, hazards, environmental effects, sustainability and appreciation of costs. Development of advanced experimental and investigative skills as appropriate for the project. Discussion of the background, context, methods, results and potential impact of a significant research project."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's graduates in Biomedical Science or Biomedical Sciences"
  addressee: learner
  verbs: ["interrogate", "integrate", "design", "develop"]
  about: "research from the literature to a significant project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates should be able to interrogate and combine varied scientific literature and other information to design and develop methods of investigation and analysis, at the forefront and beyond their own specialism; this takes in planning a project (ethics, hazards, environmental effects, sustainability and costs, as fits), building advanced experimental and investigative skills, and discussing the background, context, methods, results and likely impact of a substantial research project."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/1.2
  forPractitioner: { text: "Cover every one of the key clinical laboratory specialisms (microbiology with virology, clinical biochemistry, haematology and transfusion, immunology, cellular pathology and clinical genetics) so the degree gives the academic basis for registration.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated expectation (will) on the content of the singular Biomedical Science honours degree (FHEQ level 6): every key clinical laboratory specialism is taught. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 1.2. Do not claim it makes graduates registered or that it binds Biomedical Sciences (plural) courses; set it beside 3.2 and the specialism outcomes at 3.4.b2 to 3.4.b47 in this document."
  author-agent-dialogue: "Raise this with a team planning or reviewing an accredited Biomedical Science degree, or with a student unsure which degree leads to registration. For staff, frame it as complete coverage of the specialisms; for a student, explain that this degree is the academic step, with clinical training still to come. Ask: 'Which specialism is thinnest in your course at present?' Avoid suggesting the degree alone gives the protected title."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/1.4
  forPractitioner: { text: "Design the course so that graduates will leave with professionalism, critical independent judgement, personal responsibility and the ability to decide well in complex and unpredictable work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will have built the professionalism, independent critical thinking and sense of personal responsibility needed to make decisions at work when situations are complex and unpredictable.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for honours graduates of both the singular and plural degree, at FHEQ level 6 (FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 1.4. Do not claim it as a professional body competence or as a master's outcome. Set it beside the FHEQ honours descriptors qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.15.b9.2, spine:6 and 4.5.b16 in this document."
  author-agent-dialogue: "Raise this when a student asks what employers expect of a graduate, or when a team reviews how the course builds independence. To a student, put it as the professional habits you will be trusted with; to staff, as qualities the course has to grow over the years. Ask: 'Can you describe a time on the course when you had to make a decision without a clear right answer?' Avoid reading the issuer's text aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/1.12
  forPractitioner: { text: "Through taught modules, and with the training portfolio and registration, singular-degree graduates will be able to interpret clinical laboratory and point-of-care test results and take part in multidisciplinary care.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a Biomedical Science degree you will learn to interpret the results of clinical laboratory tests and tests done near the patient, so that you can play your part in a healthcare team.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for graduates of the singular Biomedical Science honours degree (FHEQ level 6), reached through modules together with the training portfolio and registration. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 1.12. Do not claim that the degree alone makes a graduate registered or that it holds for Biomedical Sciences (plural). Set it beside 3.4.b39 to 3.4.b41 (near-patient testing), 1.2 and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise this when a student on the accredited route asks what the degree prepares them to do in a laboratory, or when a team plans interpretation tasks. To a student, put it as reading test results with understanding and explaining them to colleagues. Ask: 'Given an abnormal result, what would you check before reporting it?' Do not tell a Biomedical Sciences (plural) student this is required of them."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/1.16
  forPractitioner: { text: "Commit the course community to equity and inclusive access, and plan for members' different needs in advance rather than waiting for requests.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a stated expectation, worded outside the five force words on the course team or provider, not a student outcome: learning communities commit to equity, inclusive access and practice that anticipates diverse needs. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 1.16. Do not present it as regulation or as a legal duty; set it beside 1.17 to 1.19 and the accessibility paragraphs 1.20 to 1.22."
  author-agent-dialogue: "Raise this when a team sets out its approach to equity and inclusion. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'How does the course find out about students' needs before they become barriers?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/1.17
  forPractitioner: { text: "Create a setting where everyone feels respected and knows their part in inclusive practice; weave equality and diversity into activities and discussion, address unequal access to diagnosis and treatment worldwide, and keep this under review.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: inclusion throughout, an open and respectful environment, awareness raised through integrated activity, and global healthcare inequality addressed. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 1.17. Do not present it as regulation or as a legal duty; set it beside 1.16, 1.18, 1.19 and 2.22."
  author-agent-dialogue: "Raise this with a team reviewing its curriculum or the climate of its labs and classes. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Where in the curriculum do students meet questions of access to diagnosis and treatment across the world?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/1.18
  forPractitioner: { text: "Present a balanced history of the field, including the prejudice some influential scientists held or benefited from; have students examine how bias shapes what science is done and how data are read; use diverse sources and cases, and check teaching materials regularly.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: the field's history, its links with social injustice and its present practices examined critically, with diverse sources and regular review of materials. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 1.18. Do not present it as regulation or as a legal duty; set it beside 1.17, 1.19 and the ethics row 4.5.b14 with its threshold and excellent cells."
  author-agent-dialogue: "Raise this when a team reviews reading lists, case studies or the history taught in a module. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Which scientists and cases does the course hold up as examples, and whose work is missing?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/1.19
  forPractitioner: { text: "Recognise discoveries by scientists of diverse identities; give students room to explore topics linked to their lived experience; ask them to judge how discoveries, such as drug development and targeting, can be turned to ends that widen inequality.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: diverse contributors recognised, students free to connect topics with their own experience, and the misuse of discoveries weighed. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 1.19. Do not present it as regulation or as a legal duty; set it beside 1.17, 1.18 and 4.5.b8."
  author-agent-dialogue: "Raise this when a team plans how students choose topics or discuss the uses of research. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Do students get to choose topics that connect with their own background, and how is that supported?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/1.20
  forPractitioner: { text: "Base access on each applicant's potential to finish the course, and remove barriers that serve no purpose.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: equitable access to the course, based on each person's potential to complete it, with needless barriers removed. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 1.20. Do not present it as regulation or as a legal duty; set it beside 1.21, 1.22 and 2.7."
  author-agent-dialogue: "Raise this when a team reviews admissions or the barriers students meet. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Which of your entry or course requirements could stop someone who could complete the course?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/1.21
  forPractitioner: { text: "Design curricula, teaching, assessment and practical work to be fully accessible from the start; use inclusive design first and reasonable adjustments where needed; vary learning and assessment to reflect the subject and widen access.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must-level requirement on the course team or provider, not a student outcome: curricula, teaching, assessment and practical work designed to be fully accessible, with inclusive design and reasonable adjustments, and varied learning and assessment. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 1.21. Do not present it as regulation or as a legal duty; set it beside 1.20, 1.22, 2.7, 2.8 and the assessment principle 3.20.b3."
  author-agent-dialogue: "Raise this when a team designs practical classes or assessments. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Which practical or assessment task in the course would be hardest for a disabled student, and what has been done about it?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/1.22
  forPractitioner: { text: "Plan access ahead for fieldwork, laboratories and placements; build flexibility into teaching and assessment; let no characteristic, such as disability, neurodiversity or social capital, limit access; act on feedback and work with student support so staff and students are both supported.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: access planned ahead and flexibly, fieldwork, laboratories and placements included, with barriers removed in response to feedback and close work with student support. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 1.22. Do not present it as regulation or as a legal duty; set it beside 1.20, 1.21 and 2.17."
  author-agent-dialogue: "Raise this when a team plans fieldwork, laboratory work or placements. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'How would the course find out, before term, that a student needs a different arrangement for laboratory work?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/1.25
  forPractitioner: { text: "Use the QAA and Advance HE ESD guidance when writing sustainability into teaching, competencies, learning outcomes and assessment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: the QAA and Advance HE ESD guidance used for teaching, competencies, outcomes and assessment in sustainability. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 1.25. Do not present it as regulation or as a legal duty; set it beside 1.23, 1.24 and std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise this when a team plans where sustainability sits in its outcomes or assessment. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Which learning outcomes in the course mention sustainability, and how are they assessed?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/1.30
  forPractitioner: { text: "Expect students to take responsibility for their continuing development: plan for reflection, goal setting and peer support so they can show commitment to learning and help others where appropriate.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will take charge of your own personal and professional development, keep learning and improving, and help others to develop where it fits.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for students on these courses, read at FHEQ level 6 for honours (inferred: the paragraph names no level). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 1.30. Do not present it as a registration requirement. Set it beside qaa/fheq-2024/4.15.b9.3, spine:6 and 4.5.b15 in this document."
  author-agent-dialogue: "Raise this when a student asks how to plan their development or what reflection is for, or when a team designs personal tutoring. To a student, frame it as owning your own learning and helping peers; to staff, as a habit the course should build. Ask: 'What is one skill you want to improve this year, and how will you know you have?' Avoid turning it into a checklist read out from the text."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.1
  forPractitioner: { text: "Make the accreditation status of the course clear in admissions material, since applicants are advised to check it before they apply.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Before you apply, check whether the course is accredited by the professional body, especially if you want to register as a Biomedical Scientist.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation addressed to prospective students: confirm a course's accreditation before applying. It sets no level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.1. Do not claim it puts a duty on the course; set it beside 1.2, 1.3 and 3.2 in this document, which explain why accreditation matters."
  author-agent-dialogue: "Raise this when a prospective student asks about routes to registration or compares courses. In plain words, explain that only an accredited Biomedical Science degree gives the academic basis for registration. Ask: 'Do you want to work in a hospital diagnostic laboratory, and does the course you are considering hold the accreditation for that?' Avoid implying an unaccredited course is a lesser degree."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.4
  forPractitioner: { text: "Integrate credit-bearing placements with the programme, with tasks that make students relate the placement to their study and use its skills.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: credit-bearing placements integrated with the programme so students link the experience to their academic study. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.4. Do not present it as regulation or as a legal duty; set it beside 2.17, 1.12 and 2.11."
  author-agent-dialogue: "Raise this when a team designs or reviews a placement year or module. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'How does a student's placement work come back into their final-year study?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.6
  forPractitioner: { text: "Design the academic component of the apprenticeship to the same standards as the degree.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: the academic part of Biomedical Science or Healthcare Science Practitioner degree apprenticeships follows this statement. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.6. Do not present it as regulation or as a legal duty; set it beside 2.21 and the Characteristics Statement for Higher Education in Apprenticeships (not yet ingested, Part E)."
  author-agent-dialogue: "Raise this with a team designing a degree apprenticeship in the area. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Which outcomes in Table 1 does the apprenticeship's academic part cover, and where?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.7
  forPractitioner: { text: "Make learning and assessment equally accessible, by inclusive design first and individual adjustment where necessary, and vary them to reflect the subject and widen access.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: equally accessible learning and assessment through inclusive design and reasonable adjustment, with varied experiences. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.7. Do not present it as regulation or as a legal duty; set it beside 1.21, 2.8 and 3.20.b3."
  author-agent-dialogue: "Raise this when a team reviews its learning and assessment for accessibility. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Which adjustments are made so often that they could be built into the design for everyone?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.8
  forPractitioner: { text: "Support every learner in the verbal, spatial and numerical skills the course depends on, alongside accessible design.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: accessible design, and support for every learner in verbal, spatial and numerical skills. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.8. Do not present it as regulation or as a legal duty; set it beside 1.21, 2.7 and the mathematics row 4.5.b10."
  author-agent-dialogue: "Raise this when a team plans support for numeracy or study skills. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Where do students who arrive with weaker numerical skills get help, and is it timely?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.9
  forPractitioner: { text: "Plan progression explicitly: early tasks apply simple concepts to defined problems; later ones ask students to connect complex concepts and analyse and evaluate data; by graduation students will be competent across the range.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course is designed to move you from using what you know on simple, well-defined problems towards handling complex ideas, analysing and evaluating data and solving problems with confidence, so that by graduation you are competent across knowledge, understanding, experience and skills.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: design that promotes academic and personal development, moving students from simple concepts to graduate competence. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.9. Do not present it as regulation or as a legal duty; set it beside 2.10, 3.15, 4.1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks why the course gets harder or what is expected by the final year, or when a team maps progression. To a student, put it as moving from simple, defined tasks to complex ones you handle with confidence; to staff, as the design of rising demand. Ask: 'Which task this year asked you to link ideas from different modules?' Avoid presenting the graduate end point as what is expected in the first year."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.10.b1
  forPractitioner: { text: "Back the progressive design of teaching and assessment with strategies that take account of how varied students' earlier experience is and how hard the move into university can be.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course's teaching and assessment strategies: they take account of how varied students' earlier experience is and how hard the move into university can be. It applies across the courses the statement covers, at every level of study. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.10 (item 1). Do not present it as a student outcome; set it beside the other 2.10 items, 2.9 and 3.15."
  author-agent-dialogue: "Raise this when a team reviews how students are supported through the transitions of the course. Frame it for staff as part of how progression is built: strategies that take account of how varied students' earlier experience is and how hard the move into university can be. Ask: 'What evidence shows that this strategy works for students who arrive with less preparation?' Do not give it to a student as their own task."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.10.b2
  forPractitioner: { text: "Back the progressive design of teaching and assessment with strategies that let every student reach their potential and ambitions, whatever their background or reasons for studying.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course's teaching and assessment strategies: they let every student reach their potential and ambitions, whatever their background or reasons for studying. It applies across the courses the statement covers, at every level of study. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.10 (item 2). Do not present it as a student outcome; set it beside the other 2.10 items, 2.9 and 3.15."
  author-agent-dialogue: "Raise this when a team reviews how students are supported through the transitions of the course. Frame it for staff as part of how progression is built: strategies that let every student reach their potential and ambitions, whatever their background or reasons for studying. Ask: 'What evidence shows that this strategy works for students who arrive with less preparation?' Do not give it to a student as their own task."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.10.b3
  forPractitioner: { text: "Back the progressive design of teaching and assessment with strategies that support academic and personal growth as well as learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course's teaching and assessment strategies: they support academic and personal growth as well as learning. It applies across the courses the statement covers, at every level of study. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.10 (item 3). Do not present it as a student outcome; set it beside the other 2.10 items, 2.9 and 3.15."
  author-agent-dialogue: "Raise this when a team reviews how students are supported through the transitions of the course. Frame it for staff as part of how progression is built: strategies that support academic and personal growth as well as learning. Ask: 'What evidence shows that this strategy works for students who arrive with less preparation?' Do not give it to a student as their own task."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.10.b4
  forPractitioner: { text: "Back the progressive design of teaching and assessment with strategies that fit the course's learning outcomes or competencies at each level of study.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course's teaching and assessment strategies: they fit the course's learning outcomes or competencies at each level of study. It applies across the courses the statement covers, at every level of study. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.10 (item 4). Do not present it as a student outcome; set it beside the other 2.10 items, 2.9 and 3.15."
  author-agent-dialogue: "Raise this when a team reviews how students are supported through the transitions of the course. Frame it for staff as part of how progression is built: strategies that fit the course's learning outcomes or competencies at each level of study. Ask: 'What evidence shows that this strategy works for students who arrive with less preparation?' Do not give it to a student as their own task."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.11
  forPractitioner: { text: "State progression rules plainly: at least the threshold for the level, credit across all components including practicals, any extra rules such as passing each core clinical specialism, and any higher standard for the integrated master's.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To move from one year or level to the next you will need to meet your university's rules, which ask you to show at least the threshold standard for that level; on an accredited Biomedical Science course you may also need to pass every core clinical specialism.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated expectation (will) on the course team or provider, not a student outcome: progression from one level to the next by meeting the institution's regulations, which require at least the threshold standard for the level. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.11. Do not present it as regulation or as a legal duty; set it beside 4.1, 4.5.b1 to 4.5.b16 and qaa/fheq-2024/annex-d/summary/lead/3rd."
  author-agent-dialogue: "Raise this when a student asks what they need to progress or worries about a failed component. To a student, say plainly that you must meet at least the minimum standard for your level and that some courses ask you to pass every core specialism; to staff, frame it as rules that must be clear and published. Ask: 'Do you know which of your modules must each be passed before you can move on?' Avoid presenting the excellent standard as what progression needs."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.14
  forPractitioner: { text: "Include practical skills in every course and plan how to develop them, combining bench sessions with online tutorials and virtual practicals.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must-level requirement on the course team or provider, not a student outcome: practical skills are a required part of every course, with teams planning how bench and virtual practice develop them. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.14. Do not present it as regulation or as a legal duty; set it beside 1.10, 4.5.b4 and its cells, and 4.5.b3."
  author-agent-dialogue: "Raise this when a team plans the balance of bench and virtual practicals. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Which practical skills can only be learned at the bench, and how much bench time do they get?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.15
  forPractitioner: { text: "Keep the course able to change with the subject and with employers' needs, and plan for disruption so teaching can adapt.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: courses flexible enough to respond to change in the subject and in employers' needs, and resilient enough to adapt to disruption. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.15. Do not present it as regulation or as a legal duty; set it beside 2.13 and 2.27."
  author-agent-dialogue: "Raise this when a team reviews how quickly its curriculum can change. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'How long would it take the course to add a new technique that has become standard in practice?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.16
  forPractitioner: { text: "Put oversight in place for every delivery partner, with clear communication and regular consultation, including with employers.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: oversight of partners in degree delivery, with effective communication and regular consultation so courses keep meeting employers' needs. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.16. Do not present it as regulation or as a legal duty; set it beside 2.17 and 2.21."
  author-agent-dialogue: "Raise this with a team delivering a course with a college, an overseas partner or an NHS or industry partner. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'How does the course know that a partner meets the same standards, and how often is that checked?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.17
  forPractitioner: { text: "Work with employers and other stakeholders on work-based learning, set out an employability strategy, and consider funding or paying placements so that every student can take one.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: work-based or work-like learning with stakeholders, extensive engagement with employment sectors, a clear employability strategy and placements made inclusive. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.17. Do not present it as regulation or as a legal duty; set it beside 1.26 to 1.30, 2.4 and 3.21.b1."
  author-agent-dialogue: "Raise this when a team reviews its employability strategy or its placements. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Which students miss out on placements now, and would funding or payment change that?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.19
  forPractitioner: { text: "Treat students as partners: give student voice real weight in developing, delivering and reviewing the course, and involve students in quality review and new course design, for example through steering groups.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You can expect to be treated as a partner in your course: your views should shape how it is developed, taught and reviewed, through representatives, surveys and other routes, and you should be able to take part in reviewing its quality.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: students treated as partners, with student voice playing a large part in course development, delivery and review, and students involved in quality review. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.19. Do not present it as regulation or as a legal duty; set it beside 2.21 and 2.27."
  author-agent-dialogue: "Raise this when a student asks how they can influence their course, or when a team plans review. To a student, explain plainly that your views count and how to raise them; to staff, frame it as partnership with evidence of change. Ask: 'Have you had a chance to say what should change in your course, and did anything happen?' Avoid treating partnership as only filling in surveys."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.21
  forPractitioner: { text: "Collect feedback from students, employers, placement providers and alumni, and from apprentices and their employers where relevant, and show how it shaped the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: monitoring and review drawing on current students, employers, placement providers and alumni, and on employers and apprentices for apprenticeships. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.21. Do not present it as regulation or as a legal duty; set it beside 2.19, 2.23 and 2.27."
  author-agent-dialogue: "Raise this when a team plans its periodic review. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Whose feedback is missing from the last review of the course?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.23
  forPractitioner: { text: "Bring performance and experience data together with expert and external examiner review when evaluating the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: student performance data and measures of experience integrated with expert review, external examiners included. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.23. Do not present it as regulation or as a legal duty; set it beside 2.21, 2.25 and 2.27."
  author-agent-dialogue: "Raise this when a team prepares its annual monitoring. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'How are external examiners' comments read alongside the course's own data?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.24
  forPractitioner: { text: "Involve external reviewers in periodic review to test proposed changes, threshold standards and the fit of content to the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated expectation (will) on the course team or provider, not a student outcome: external reviewers used in periodic review to give an outside view and check that threshold standards are met and content suits the subject. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.24. Do not present it as regulation or as a legal duty; set it beside 2.25, 4.1 and 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a team prepares for periodic review. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Which external reviewer will look at the course, and what will they check it against?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/2.27
  forPractitioner: { text: "Monitor and evaluate the course regularly with independent and student input, use data trends to spot issues, and involve students, graduates, employers, service users and professional bodies in improving it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: regular monitoring and evaluation with independent evaluators and student feedback, data integrated with expert review, and students, graduates, employers, service users and professional bodies involved in enhancement. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 2.27. Do not present it as regulation or as a legal duty; set it beside 2.21 and 2.23."
  author-agent-dialogue: "Raise this when a team sets its enhancement plan. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Have service users or professional bodies had any part in the last change to the course?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.2
  forPractitioner: { text: "Cover every clinical laboratory specialism the IBMS accreditation criteria list, and hold IBMS accreditation, so graduates meet the academic requirements for HCPC registration.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must-level requirement on the course team or provider, not a student outcome: the singular degree covers every clinical laboratory specialism in the professional body's accreditation criteria and must hold that accreditation so its graduates satisfy the academic conditions for registration. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.2. Do not present it as regulation or as a legal duty; set it beside 1.2, 3.4 and its items 3.4.b2 to 3.4.b47."
  author-agent-dialogue: "Raise this with a team seeking or renewing accreditation of a Biomedical Science or Healthcare Science degree. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Can you show where each specialism in the accreditation criteria is taught and assessed?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.3
  forPractitioner: { text: "Teach through a systems-led approach so students will join up the specialisms with the science of investigation and treatment of particular diseases, and know current laboratory methods and how new ones are developed and evaluated.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will learn to join up what you know from each laboratory specialism, disease by disease and system by system, and you will know the current laboratory methods used to investigate, diagnose and monitor health and disease, and how new methods and treatments are tested.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for students on the singular Biomedical Science honours degree (FHEQ level 6). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.3. Do not claim it holds for Biomedical Sciences (plural) or that it is an HCPC standard. Set it beside 3.4.b2 to 3.4.b47, 4.5.b9 and the FHEQ honours descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a student asks how the separate specialisms fit together, or when a team designs integrated case studies. To a student, put it as following one patient's disease across several laboratories; to staff, as the systems-led design. Ask: 'For a patient with suspected kidney disease, which laboratory specialisms would be involved, and what would each add?' Avoid reading the paragraph aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4
  forPractitioner: { text: "Include every listed clinical pathology area in the accredited course, and make sure each graduate has studied and passed every specialism: this, with the verified training portfolio, meets the education standards for registration.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "On an accredited Biomedical Science course you will study all the clinical pathology specialisms, and you must pass every one of them, as well as completing your training portfolio, to meet the education standards for registration.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a requirement (required, recorded as must) for IBMS-accredited Biomedical Science or Healthcare Science honours degrees (FHEQ level 6): the clinical pathology areas are taught, and every graduate has studied and passed each one. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4. Do not claim it holds for Biomedical Sciences (plural) courses or that passing the degree alone gives registration. Set it beside its items 3.4.b2 to 3.4.b47, 3.2 and 1.2."
  author-agent-dialogue: "Raise this when a student on the accredited route asks whether a weak result in one specialism matters, or when a team sets its progression and award rules. Say plainly to a student that every specialism has to be passed for the route to registration; to staff, frame it as a rule to build into regulations. Ask: 'Which specialism do you feel least sure of, and when is it assessed?' Avoid applying it to students on a broader Biomedical Sciences course."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b2
  forPractitioner: { text: "Teach and assess normal and diseased cell and tissue structure so that every Biomedical Science graduate will know how normal cells and tissues are built, at gross and fine scale, and how disease alters that structure.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how normal cells and tissues are built, at gross and fine scale, and how disease alters that structure.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of normal and diseased cell and tissue structure. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (cellular pathology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other cellular pathology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about normal and diseased cell and tissue structure, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met normal and diseased cell and tissue structure, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b3
  forPractitioner: { text: "Teach and assess reproductive science so that every Biomedical Science graduate will know reproductive science, with infertility and the study of embryos.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know reproductive science, with infertility and the study of embryos.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of reproductive science. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (cellular pathology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other cellular pathology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about reproductive science, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met reproductive science, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b4
  forPractitioner: { text: "Teach and assess preparing cells and tissues for microscopy so that every Biomedical Science graduate will know how cells and tissues are prepared for examination under the microscope.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how cells and tissues are prepared for examination under the microscope.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of preparing cells and tissues for microscopy. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (cellular pathology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other cellular pathology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about preparing cells and tissues for microscopy, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met preparing cells and tissues for microscopy, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b5
  forPractitioner: { text: "Teach and assess visualisation and imaging in diagnosis so that every Biomedical Science graduate will know the principles and uses of imaging and visualisation methods, microscopy among them, in supporting diagnosis and the choice of treatment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the principles and uses of imaging and visualisation methods, microscopy among them, in supporting diagnosis and the choice of treatment.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of visualisation and imaging in diagnosis. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (cellular pathology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other cellular pathology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about visualisation and imaging in diagnosis, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met visualisation and imaging in diagnosis, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b7
  forPractitioner: { text: "Teach and assess collecting and analysing clinical samples so that every Biomedical Science graduate will know the common methods for collecting clinical samples and analysing them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the common methods for collecting clinical samples and analysing them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of collecting and analysing clinical samples. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (clinical biochemistry). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other clinical biochemistry items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about collecting and analysing clinical samples, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met collecting and analysing clinical samples, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b8
  forPractitioner: { text: "Teach and assess investigating major organ systems so that every Biomedical Science graduate will know how the main body and organ systems are investigated, for example through kidney, liver, bone profile and tumour marker tests.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how the main body and organ systems are investigated, for example through kidney, liver, bone profile and tumour marker tests.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of investigating major organ systems. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (clinical biochemistry). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other clinical biochemistry items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about investigating major organ systems, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met investigating major organ systems, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b9
  forPractitioner: { text: "Teach and assess biochemical investigations across the course of disease so that every Biomedical Science graduate will know the principles and uses of biochemical tests in screening for disease, diagnosing it, treating it and following its course.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the principles and uses of biochemical tests in screening for disease, diagnosing it, treating it and following its course.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of biochemical investigations across the course of disease. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (clinical biochemistry). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other clinical biochemistry items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about biochemical investigations across the course of disease, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met biochemical investigations across the course of disease, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b10
  forPractitioner: { text: "Teach and assess drug monitoring and substance misuse so that every Biomedical Science graduate will know monitoring of therapeutic drugs and the investigation of substance misuse.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know monitoring of therapeutic drugs and the investigation of substance misuse.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of drug monitoring and substance misuse. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (clinical biochemistry). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other clinical biochemistry items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about drug monitoring and substance misuse, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met drug monitoring and substance misuse, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b12
  forPractitioner: { text: "Teach and assess immune effectors and their measurement so that every Biomedical Science graduate will know how the effectors of the immune response work and how they are measured.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how the effectors of the immune response work and how they are measured.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of immune effectors and their measurement. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (clinical immunology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other clinical immunology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about immune effectors and their measurement, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met immune effectors and their measurement, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b13
  forPractitioner: { text: "Teach and assess abnormal immune function and its management so that every Biomedical Science graduate will know why immune function goes wrong and what follows, neoplastic disease and transplant reactions included, and how these are detected, diagnosed, treated and followed.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know why immune function goes wrong and what follows, neoplastic disease and transplant reactions included, and how these are detected, diagnosed, treated and followed.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of abnormal immune function and its management. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (clinical immunology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other clinical immunology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about abnormal immune function and its management, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met abnormal immune function and its management, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b14
  forPractitioner: { text: "Teach and assess immunological techniques so that every Biomedical Science graduate will know the principles and practice of immunological methods in screening, diagnosis, treatment and follow-up, with prophylaxis and immunotherapy.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the principles and practice of immunological methods in screening, diagnosis, treatment and follow-up, with prophylaxis and immunotherapy.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of immunological techniques. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (clinical immunology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other clinical immunology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about immunological techniques, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met immunological techniques, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b16
  forPractitioner: { text: "Teach and assess blood cells so that every Biomedical Science graduate will know how blood cells are formed, built and work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how blood cells are formed, built and work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of blood cells. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (haematology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other haematology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about blood cells, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met blood cells, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b17
  forPractitioner: { text: "Teach and assess normal haemostasis so that every Biomedical Science graduate will know how normal haemostasis is regulated.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how normal haemostasis is regulated.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of normal haemostasis. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (haematology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other haematology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about normal haemostasis, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met normal haemostasis, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b18
  forPractitioner: { text: "Teach and assess blood cell morphology so that every Biomedical Science graduate will know the appearance of blood cells: recognising normal white cells and the usual red cell abnormalities.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the appearance of blood cells: recognising normal white cells and the usual red cell abnormalities.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of blood cell morphology. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (haematology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other haematology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about blood cell morphology, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met blood cell morphology, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b19
  forPractitioner: { text: "Teach and assess anaemias, malignancies and bleeding and clotting disorders so that every Biomedical Science graduate will know the nature and diagnosis of anaemias, blood cancers and disorders of bleeding and thrombosis.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the nature and diagnosis of anaemias, blood cancers and disorders of bleeding and thrombosis.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of anaemias, malignancies and bleeding and clotting disorders. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (haematology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other haematology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about anaemias, malignancies and bleeding and clotting disorders, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met anaemias, malignancies and bleeding and clotting disorders, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b20
  forPractitioner: { text: "Teach and assess haematological techniques so that every Biomedical Science graduate will know the principles and practice of haematology methods in screening, diagnosis, treatment and follow-up.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the principles and practice of haematology methods in screening, diagnosis, treatment and follow-up.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of haematological techniques. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (haematology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other haematology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about haematological techniques, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met haematological techniques, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b22
  forPractitioner: { text: "Teach and assess blood grouping and antibody screening so that every Biomedical Science graduate will know interpreting blood groups, the causes of grouping anomalies, and screening for antibodies.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know interpreting blood groups, the causes of grouping anomalies, and screening for antibodies.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of blood grouping and antibody screening. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (transfusion science). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other transfusion science items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about blood grouping and antibody screening, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met blood grouping and antibody screening, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b23
  forPractitioner: { text: "Teach and assess red cell antigens so that every Biomedical Science graduate will know the genetics, inheritance, structure and role of antigens on red cells.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the genetics, inheritance, structure and role of antigens on red cells.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of red cell antigens. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (transfusion science). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other transfusion science items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about red cell antigens, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met red cell antigens, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b24
  forPractitioner: { text: "Teach and assess immune destruction of blood cells so that every Biomedical Science graduate will know the destruction of blood cells by the immune system.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the destruction of blood cells by the immune system.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of immune destruction of blood cells. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (transfusion science). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other transfusion science items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about immune destruction of blood cells, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met immune destruction of blood cells, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b25
  forPractitioner: { text: "Teach and assess blood components so that every Biomedical Science graduate will know how blood components are prepared, stored and used.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how blood components are prepared, stored and used.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of blood components. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (transfusion science). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other transfusion science items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about blood components, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met blood components, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b26
  forPractitioner: { text: "Teach and assess patient blood management so that every Biomedical Science graduate will know patient blood management.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know patient blood management.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of patient blood management. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (transfusion science). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other transfusion science items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about patient blood management, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met patient blood management, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b27
  forPractitioner: { text: "Teach and assess selecting components for transfusion so that every Biomedical Science graduate will know choosing suitable blood components for transfusion, and the adverse effects that can follow.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know choosing suitable blood components for transfusion, and the adverse effects that can follow.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of selecting components for transfusion. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (transfusion science). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other transfusion science items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about selecting components for transfusion, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met selecting components for transfusion, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b29
  forPractitioner: { text: "Teach and assess omic methods for chromosomes and DNA so that every Biomedical Science graduate will know genomic, transcriptomic and proteomic methods for analysing human chromosomes and DNA.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know genomic, transcriptomic and proteomic methods for analysing human chromosomes and DNA.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of omic methods for chromosomes and DNA. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (clinical genetics). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other clinical genetics items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about omic methods for chromosomes and DNA, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met omic methods for chromosomes and DNA, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b30
  forPractitioner: { text: "Teach and assess molecular biology and bioinformatics in medicine so that every Biomedical Science graduate will know how molecular biology and bioinformatics are applied in medicine.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how molecular biology and bioinformatics are applied in medicine.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of molecular biology and bioinformatics in medicine. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (clinical genetics). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other clinical genetics items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about molecular biology and bioinformatics in medicine, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met molecular biology and bioinformatics in medicine, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b31
  forPractitioner: { text: "Teach and assess pharmacogenetics so that every Biomedical Science graduate will know pharmacogenetics and personalised medicine.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know pharmacogenetics and personalised medicine.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of pharmacogenetics. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (clinical genetics). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other clinical genetics items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about pharmacogenetics, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met pharmacogenetics, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b32
  forPractitioner: { text: "Teach and assess genetic testing so that every Biomedical Science graduate will know the principles and practice of genetic testing in screening, diagnosis and follow-up, and the ethical questions it raises.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the principles and practice of genetic testing in screening, diagnosis and follow-up, and the ethical questions it raises.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of genetic testing. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (clinical genetics). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other clinical genetics items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about genetic testing, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met genetic testing, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b34
  forPractitioner: { text: "Teach and assess how microorganisms cause disease so that every Biomedical Science graduate will know the mechanisms by which a range of microorganisms cause disease.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the mechanisms by which a range of microorganisms cause disease.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of how microorganisms cause disease. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (medical microbiology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other medical microbiology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about how microorganisms cause disease, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met how microorganisms cause disease, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b35
  forPractitioner: { text: "Teach and assess public health microbiology so that every Biomedical Science graduate will know public health microbiology, the epidemiology and control of infection, and the One Health concept.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know public health microbiology, the epidemiology and control of infection, and the One Health concept.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of public health microbiology. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (medical microbiology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other medical microbiology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about public health microbiology, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met public health microbiology, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b36
  forPractitioner: { text: "Teach and assess detecting and controlling infection so that every Biomedical Science graduate will know the principles and practice of methods for screening, diagnosing, treating and following infectious diseases, for detecting and identifying microorganisms, and for preventing and controlling infection, vaccination and environmental and vector control included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the principles and practice of methods for screening, diagnosing, treating and following infectious diseases, for detecting and identifying microorganisms, and for preventing and controlling infection, vaccination and environmental and vector control included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of detecting and controlling infection. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (medical microbiology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other medical microbiology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about detecting and controlling infection, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met detecting and controlling infection, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b37
  forPractitioner: { text: "Teach and assess antimicrobials and resistance so that every Biomedical Science graduate will know antimicrobial chemotherapy and resistance to antibiotics, antivirals, antifungals and anti-parasitic drugs.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know antimicrobial chemotherapy and resistance to antibiotics, antivirals, antifungals and anti-parasitic drugs.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of antimicrobials and resistance. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (medical microbiology). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other medical microbiology items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about antimicrobials and resistance, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met antimicrobials and resistance, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b39
  forPractitioner: { text: "Teach and assess near-patient investigations so that every Biomedical Science graduate will know the principles and uses of investigations run on near-patient testing equipment for screening, diagnosis, treatment and follow-up.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the principles and uses of investigations run on near-patient testing equipment for screening, diagnosis, treatment and follow-up.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of near-patient investigations. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (near-patient testing). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other near-patient testing items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about near-patient investigations, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met near-patient investigations, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b40
  forPractitioner: { text: "Teach and assess near-patient testing in patient pathways so that every Biomedical Science graduate will know how near-patient testing fits into patient pathways.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how near-patient testing fits into patient pathways.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of near-patient testing in patient pathways. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (near-patient testing). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other near-patient testing items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about near-patient testing in patient pathways, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met near-patient testing in patient pathways, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b41
  forPractitioner: { text: "Teach and assess quality assurance in near-patient testing so that every Biomedical Science graduate will know the quality assurance points that bear on near-patient testing.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the quality assurance points that bear on near-patient testing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of quality assurance in near-patient testing. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (near-patient testing). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other near-patient testing items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about quality assurance in near-patient testing, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met quality assurance in near-patient testing, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b43
  forPractitioner: { text: "Teach and assess quality control standards so that every Biomedical Science graduate will know how to interpret quality control standards.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how to interpret quality control standards.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of quality control standards. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (laboratory quality). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other laboratory quality items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about quality control standards, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met quality control standards, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b44
  forPractitioner: { text: "Teach and assess quality assurance and pre-analytical variables so that every Biomedical Science graduate will know why quality assurance and pre-analytical variables matter.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know why quality assurance and pre-analytical variables matter.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of quality assurance and pre-analytical variables. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (laboratory quality). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other laboratory quality items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about quality assurance and pre-analytical variables, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met quality assurance and pre-analytical variables, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b45
  forPractitioner: { text: "Teach and assess external quality assessment so that every Biomedical Science graduate will know why external quality assessment matters.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know why external quality assessment matters.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of external quality assessment. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (laboratory quality). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other laboratory quality items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about external quality assessment, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met external quality assessment, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b46
  forPractitioner: { text: "Teach and assess quality management so that every Biomedical Science graduate will know quality management at a basic level: quality policy, audit, standard operating procedures, training and competency records, error and incident reporting, validation and verification, and reagent stock.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know quality management at a basic level: quality policy, audit, standard operating procedures, training and competency records, error and incident reporting, validation and verification, and reagent stock.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of quality management. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (laboratory quality). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other laboratory quality items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about quality management, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met quality management, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.4.b47
  forPractitioner: { text: "Teach and assess laboratory accreditation so that every Biomedical Science graduate will know laboratory accreditation, with a basic awareness of UKAS and ISO standards.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know laboratory accreditation, with a basic awareness of UKAS and ISO standards.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Biomedical Science honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of laboratory accreditation. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.4 (laboratory quality). Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other laboratory quality items in 3.4, the lead-in 3.4 and 3.2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Biomedical Science student asks what they need to know about laboratory accreditation, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met laboratory accreditation, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b2
  forPractitioner: { text: "Teach and assess molecular drug targets so that every Pharmacology graduate will know the molecular targets drugs act on, such as receptors, enzymes, ion channels and transporters.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the molecular targets drugs act on, such as receptors, enzymes, ion channels and transporters.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Pharmacology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of molecular drug targets. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.6. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.6 items and 3.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Pharmacology student asks what they need to know about molecular drug targets, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met molecular drug targets, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b3
  forPractitioner: { text: "Teach and assess drug-receptor relationships so that every Pharmacology graduate will know how drugs relate to receptors, covering agonism and antagonism, specificity and selectivity, potency, desensitisation and tolerance.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how drugs relate to receptors, covering agonism and antagonism, specificity and selectivity, potency, desensitisation and tolerance.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Pharmacology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of drug-receptor relationships. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.6. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.6 items and 3.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Pharmacology student asks what they need to know about drug-receptor relationships, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met drug-receptor relationships, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b4
  forPractitioner: { text: "Teach and assess main drug targets and how drugs alter them so that every Pharmacology graduate will know the structure and function of the main drug targets and how drugs change that function at molecular level.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the structure and function of the main drug targets and how drugs change that function at molecular level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Pharmacology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of main drug targets and how drugs alter them. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.6. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.6 items and 3.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Pharmacology student asks what they need to know about main drug targets and how drugs alter them, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met main drug targets and how drugs alter them, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b5
  forPractitioner: { text: "Teach and assess drug effects on organ systems and cells so that every Pharmacology graduate will know how drugs act on the major organ systems and on cell function, proliferation and death.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how drugs act on the major organ systems and on cell function, proliferation and death.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Pharmacology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of drug effects on organ systems and cells. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.6. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.6 items and 3.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Pharmacology student asks what they need to know about drug effects on organ systems and cells, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met drug effects on organ systems and cells, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b6
  forPractitioner: { text: "Teach and assess pharmacokinetics so that every Pharmacology graduate will know pharmacokinetics, what the body does to drugs: their absorption, distribution, biotransformation and excretion.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know pharmacokinetics, what the body does to drugs: their absorption, distribution, biotransformation and excretion.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Pharmacology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of pharmacokinetics. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.6. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.6 items and 3.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Pharmacology student asks what they need to know about pharmacokinetics, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met pharmacokinetics, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b7
  forPractitioner: { text: "Teach and assess individual variation and personalised medicine so that every Pharmacology graduate will know why people differ in drug response and toxicity, through ethnicity, gender, age, pregnancy, genes, disease and drug interactions, and the emerging technologies of personalised medicine.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know why people differ in drug response and toxicity, through ethnicity, gender, age, pregnancy, genes, disease and drug interactions, and the emerging technologies of personalised medicine.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Pharmacology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of individual variation and personalised medicine. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.6. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.6 items and 3.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Pharmacology student asks what they need to know about individual variation and personalised medicine, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met individual variation and personalised medicine, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b9
  forPractitioner: { text: "Teach and assess concentration-response relationships so that every Pharmacology graduate will know how drug concentration or dose relates to response.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how drug concentration or dose relates to response.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Pharmacology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of concentration-response relationships. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.6. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.6 items and 3.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a Pharmacology student asks what they need to know about concentration-response relationships, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met concentration-response relationships, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b10
  forPractitioner: { text: "Teach and assess experimental methods in pharmacology so that every Pharmacology graduate will know experimental methods used in pharmacology, such as bioassays, receptor binding and cloning, therapeutic recombinant proteins, animal disease models and genetic manipulation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know experimental methods used in pharmacology, such as bioassays, receptor binding and cloning, therapeutic recombinant proteins, animal disease models and genetic manipulation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Pharmacology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of experimental methods in pharmacology. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.6. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.6 items and 3.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a Pharmacology student asks what they need to know about experimental methods in pharmacology, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met experimental methods in pharmacology, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b11
  forPractitioner: { text: "Teach and assess animals in research so that every Pharmacology graduate will know the ethics and law of using animals in research, and ways to replace, refine and reduce that use.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the ethics and law of using animals in research, and ways to replace, refine and reduce that use.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Pharmacology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of animals in research. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.6. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.6 items and 3.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Pharmacology student asks what they need to know about animals in research, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met animals in research, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b12
  forPractitioner: { text: "Teach and assess drug discovery, development and regulation so that every Pharmacology graduate will know how drugs are discovered and developed, toxicology included, and the regulation that oversees their quality, safety and effectiveness.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how drugs are discovered and developed, toxicology included, and the regulation that oversees their quality, safety and effectiveness.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Pharmacology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of drug discovery, development and regulation. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.6. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.6 items and 3.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Pharmacology student asks what they need to know about drug discovery, development and regulation, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met drug discovery, development and regulation, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.6.b13
  forPractitioner: { text: "Teach and assess clinical trials so that every Pharmacology graduate will know the principles of clinical trials (bias, sample size, the placebo effect, therapeutic index) and the ethics of using human participants and tissues.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the principles of clinical trials (bias, sample size, the placebo effect, therapeutic index) and the ethics of using human participants and tissues.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Pharmacology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of clinical trials. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.6. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.6 items and 3.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Pharmacology student asks what they need to know about clinical trials, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met clinical trials, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b2
  forPractitioner: { text: "Teach and assess nutrients, metabolism and the cellular basis of disease so that every Human Nutrition graduate will know the chemistry of life, how nutrients work in the main metabolic pathways, and the cellular and molecular roots of disease, gene expression included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the chemistry of life, how nutrients work in the main metabolic pathways, and the cellular and molecular roots of disease, gene expression included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Human Nutrition honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of nutrients, metabolism and the cellular basis of disease. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.9. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.9 items, 3.7 and 3.8, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Human Nutrition student asks what they need to know about nutrients, metabolism and the cellular basis of disease, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met nutrients, metabolism and the cellular basis of disease, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b3
  forPractitioner: { text: "Teach and assess clinical biochemistry of disease and nutrition so that every Human Nutrition graduate will know the clinical biochemistry of human disease and how it is managed, weighted towards nutritional factors.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the clinical biochemistry of human disease and how it is managed, weighted towards nutritional factors.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Human Nutrition honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of clinical biochemistry of disease and nutrition. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.9. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.9 items, 3.7 and 3.8, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Human Nutrition student asks what they need to know about clinical biochemistry of disease and nutrition, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met clinical biochemistry of disease and nutrition, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b4
  forPractitioner: { text: "Teach and assess assessing nutritional status across the life cycle so that every Human Nutrition graduate will know how nutritional status is assessed, the main nutritional issues at each life stage, and how socio-demographic, economic and environmental factors shape diet.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how nutritional status is assessed, the main nutritional issues at each life stage, and how socio-demographic, economic and environmental factors shape diet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Human Nutrition honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of assessing nutritional status across the life cycle. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.9. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.9 items, 3.7 and 3.8, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Human Nutrition student asks what they need to know about assessing nutritional status across the life cycle, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met assessing nutritional status across the life cycle, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b5
  forPractitioner: { text: "Teach and assess food science and safety so that every Human Nutrition graduate will know the ideas and processes of food science, safety, storage, processing and microbiology.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the ideas and processes of food science, safety, storage, processing and microbiology.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Human Nutrition honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of food science and safety. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.9. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.9 items, 3.7 and 3.8, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Human Nutrition student asks what they need to know about food science and safety, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met food science and safety, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b6
  forPractitioner: { text: "Teach and assess clinical nutrition and health promotion so that every Human Nutrition graduate will know clinical nutrition, diet therapy, health promotion and nutrition education.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know clinical nutrition, diet therapy, health promotion and nutrition education.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Human Nutrition honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of clinical nutrition and health promotion. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.9. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.9 items, 3.7 and 3.8, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Human Nutrition student asks what they need to know about clinical nutrition and health promotion, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met clinical nutrition and health promotion, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b7
  forPractitioner: { text: "Teach and assess sport and exercise nutrition so that every Human Nutrition graduate will know nutrition for sport and exercise performance.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know nutrition for sport and exercise performance.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Human Nutrition honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of sport and exercise nutrition. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.9. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.9 items, 3.7 and 3.8, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Human Nutrition student asks what they need to know about sport and exercise nutrition, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met sport and exercise nutrition, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b8
  forPractitioner: { text: "Teach and assess gene-nutrient interactions so that every Human Nutrition graduate will know how genes and nutrients interact and what that may mean for preventing diet-related disease.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how genes and nutrients interact and what that may mean for preventing diet-related disease.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Human Nutrition honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of gene-nutrient interactions. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.9. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.9 items, 3.7 and 3.8, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Human Nutrition student asks what they need to know about gene-nutrient interactions, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met gene-nutrient interactions, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.9.b9
  forPractitioner: { text: "Teach and assess nutrition and the nature of disease so that every Human Nutrition graduate will know how nutritional status bears on disease, and a core theoretical sense that human disease and its care draw on many disciplines.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how nutritional status bears on disease, and a core theoretical sense that human disease and its care draw on many disciplines.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Human Nutrition honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of nutrition and the nature of disease. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.9. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.9 items, 3.7 and 3.8, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Human Nutrition student asks what they need to know about nutrition and the nature of disease, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met nutrition and the nature of disease, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b2
  forPractitioner: { text: "Teach and assess levels of organisation and regulation so that every Physiology graduate will know the levels of organisation from chemical to whole organism, and the internal and external factors that regulate body systems.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the levels of organisation from chemical to whole organism, and the internal and external factors that regulate body systems.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of levels of organisation and regulation. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about levels of organisation and regulation, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met levels of organisation and regulation, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b3
  forPractitioner: { text: "Teach and assess structure and function of body systems so that every Physiology graduate will know how structure relates to function in each body system, what each system fundamentally does and how the systems interrelate.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how structure relates to function in each body system, what each system fundamentally does and how the systems interrelate.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of structure and function of body systems. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about structure and function of body systems, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met structure and function of body systems, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b4
  forPractitioner: { text: "Teach and assess life processes so that every Physiology graduate will know the processes of life: metabolism, responsiveness, movement, growth, differentiation and reproduction.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the processes of life: metabolism, responsiveness, movement, growth, differentiation and reproduction.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of life processes. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about life processes, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met life processes, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b5
  forPractitioner: { text: "Teach and assess cell-cell communication so that every Physiology graduate will know the systems by which cells communicate with each other.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the systems by which cells communicate with each other.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of cell-cell communication. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about cell-cell communication, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met cell-cell communication, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b7
  forPractitioner: { text: "Teach and assess homeostasis so that every Physiology graduate will know homeostasis, both self-regulation and regulation from outside the organ.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know homeostasis, both self-regulation and regulation from outside the organ.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of homeostasis. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about homeostasis, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met homeostasis, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b8
  forPractitioner: { text: "Teach and assess the nervous system so that every Physiology graduate will know neural tissue, the spinal cord, spinal nerves and reflexes, the brain, cranial nerves and neural integration.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know neural tissue, the spinal cord, spinal nerves and reflexes, the brain, cranial nerves and neural integration.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of the nervous system. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about the nervous system, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met the nervous system, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b9
  forPractitioner: { text: "Teach and assess fluid, electrolyte and acid-base balance so that every Physiology graduate will know the balance of fluids, electrolytes, acids and bases, its control, its disturbances and their effect on health.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the balance of fluids, electrolytes, acids and bases, its control, its disturbances and their effect on health.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of fluid, electrolyte and acid-base balance. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about fluid, electrolyte and acid-base balance, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met fluid, electrolyte and acid-base balance, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b10
  forPractitioner: { text: "Teach and assess the endocrine system so that every Physiology graduate will know the endocrine system: how hormones are secreted and distributed and how they act.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the endocrine system: how hormones are secreted and distributed and how they act.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of the endocrine system. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about the endocrine system, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met the endocrine system, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b11
  forPractitioner: { text: "Teach and assess stress responses so that every Physiology graduate will know how the body responds to internal and external stressors.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how the body responds to internal and external stressors.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of stress responses. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about stress responses, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met stress responses, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b12
  forPractitioner: { text: "Teach and assess coordination of body systems so that every Physiology graduate will know how neuronal, hormonal and chemical signals coordinate and integrate the work of body systems.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how neuronal, hormonal and chemical signals coordinate and integrate the work of body systems.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of coordination of body systems. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about coordination of body systems, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met coordination of body systems, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b13
  forPractitioner: { text: "Teach and assess adaptation and survival so that every Physiology graduate will know how physiological responses and regulation allow adaptation and survival as the environment changes.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how physiological responses and regulation allow adaptation and survival as the environment changes.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of adaptation and survival. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about adaptation and survival, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met adaptation and survival, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b15
  forPractitioner: { text: "Teach and assess cell components and transport so that every Physiology graduate will know the main parts of a human cell, its chief transport processes and how it keeps itself intact.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the main parts of a human cell, its chief transport processes and how it keeps itself intact.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of cell components and transport. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about cell components and transport, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met cell components and transport, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b16
  forPractitioner: { text: "Teach and assess cell differentiation and diversity so that every Physiology graduate will know how cells differentiate and cycle, the variety of cell types, and the intracellular chemistry that sustains life and drives cell responses.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know how cells differentiate and cycle, the variety of cell types, and the intracellular chemistry that sustains life and drives cell responses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of cell differentiation and diversity. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about cell differentiation and diversity, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met cell differentiation and diversity, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b18
  forPractitioner: { text: "Teach and assess tissues, injury and repair so that every Physiology graduate will know the structure and function of epithelial and connective tissues and membranes, and how tissues are injured and repaired.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the structure and function of epithelial and connective tissues and membranes, and how tissues are injured and repaired.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of tissues, injury and repair. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about tissues, injury and repair, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met tissues, injury and repair, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b19
  forPractitioner: { text: "Teach and assess skin, bone and joints so that every Physiology graduate will know the basics of skin, bone structure, the skeleton and joints.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the basics of skin, bone structure, the skeleton and joints.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of skin, bone and joints. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about skin, bone and joints, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met skin, bone and joints, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b20
  forPractitioner: { text: "Teach and assess muscle so that every Physiology graduate will know skeletal muscle and the other kinds of muscle tissue.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know skeletal muscle and the other kinds of muscle tissue.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of muscle. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about muscle, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met muscle, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b21
  forPractitioner: { text: "Teach and assess exercise physiology so that every Physiology graduate will know exercise physiology, the effects of exercise and the nutrition linked to it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know exercise physiology, the effects of exercise and the nutrition linked to it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of exercise physiology. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about exercise physiology, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met exercise physiology, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b23
  forPractitioner: { text: "Teach and assess the cardiovascular system so that every Physiology graduate will know the cardiovascular system: blood and haemostasis, the heartbeat and cardiodynamics, and cardiovascular physiology and its regulation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the cardiovascular system: blood and haemostasis, the heartbeat and cardiodynamics, and cardiovascular physiology and its regulation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of the cardiovascular system. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about the cardiovascular system, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met the cardiovascular system, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b24
  forPractitioner: { text: "Teach and assess the lymphatic system so that every Physiology graduate will know the lymphatic system, its organisation, defences and immunity.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the lymphatic system, its organisation, defences and immunity.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of the lymphatic system. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about the lymphatic system, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met the lymphatic system, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b26
  forPractitioner: { text: "Teach and assess respiration so that every Physiology graduate will know the respiratory system and its physiology.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the respiratory system and its physiology.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of respiration. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about respiration, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met respiration, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b27
  forPractitioner: { text: "Teach and assess digestion and the hepatobiliary system so that every Physiology graduate will know the digestive and hepatobiliary systems: their organs and the processes of digestion, absorption, detoxification and elimination.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the digestive and hepatobiliary systems: their organs and the processes of digestion, absorption, detoxification and elimination.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of digestion and the hepatobiliary system. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about digestion and the hepatobiliary system, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met digestion and the hepatobiliary system, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b28
  forPractitioner: { text: "Teach and assess metabolism and energetics so that every Physiology graduate will know metabolism and energetics.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know metabolism and energetics.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of metabolism and energetics. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about metabolism and energetics, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met metabolism and energetics, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b29
  forPractitioner: { text: "Teach and assess the urinary system so that every Physiology graduate will know the urinary system and the principles of kidney physiology.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the urinary system and the principles of kidney physiology.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of the urinary system. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about the urinary system, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met the urinary system, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b31
  forPractitioner: { text: "Teach and assess reproductive systems so that every Physiology graduate will know the reproductive systems and how they integrate with other systems.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the reproductive systems and how they integrate with other systems.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of reproductive systems. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about reproductive systems, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met reproductive systems, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b32
  forPractitioner: { text: "Teach and assess development and inheritance so that every Physiology graduate will know development and inheritance, from fertilisation and pregnancy through prenatal development to foetal growth.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know development and inheritance, from fertilisation and pregnancy through prenatal development to foetal growth.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of development and inheritance. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about development and inheritance, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met development and inheritance, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b33
  forPractitioner: { text: "Teach and assess inheritance, development and ageing so that every Physiology graduate will know features of human inheritance, development and ageing.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know features of human inheritance, development and ageing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of inheritance, development and ageing. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about inheritance, development and ageing, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met inheritance, development and ageing, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b35
  forPractitioner: { text: "Teach and assess ethics and law of human and animal research so that every Physiology graduate will know the ethics and law of using people, animals or tissues in research and elsewhere.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the ethics and law of using people, animals or tissues in research and elsewhere.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of ethics and law of human and animal research. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about ethics and law of human and animal research, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met ethics and law of human and animal research, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.11.b36
  forPractitioner: { text: "Teach and assess core physiological techniques so that every Physiology graduate will know the core techniques and practical skills of physiology: experimental design, measurement, data handling and statistical analysis.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On this course you will come to know the core techniques and practical skills of physiology: experimental design, measurement, data handling and statistical analysis.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for every Physiology honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of core physiological techniques. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.11. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. Set it beside the other 3.11 items and 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a Physiology student asks what they need to know about core physiological techniques, or when a team checks its modules against the core content. To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. Ask: 'Where in your course have you met core physiological techniques, and could you explain it to a colleague?' Do not read the list aloud or suggest it applies to every course in the area."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.13
  forPractitioner: { text: "Build graduate and professional attributes into the course, and make sure students will understand that much of what they are taught is provisional and will change.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your course will help you develop the attributes of a graduate and a professional in your subject, and you will come to see that much of what you learn now is likely to change as science moves on.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a stated outcome (will) for students across all the courses in the area, read at FHEQ level 6 for honours (inferred). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.13. Do not claim the attributes are a fixed or exhaustive list. Set it beside 3.14.b1 to 3.14.b8, 4.5.b15, qaa/fheq-2024/4.15.b4 and spine:6."
  author-agent-dialogue: "Raise this when a student is unsettled that a textbook account has been overturned, or when a team reviews its graduate attributes. To a student, put it plainly: much of what you learn will change, so learning how to update it matters. Ask: 'Can you think of something in your subject that was taught differently ten years ago?' Avoid suggesting current knowledge is unreliable."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b1
  forPractitioner: { text: "Plan the course so students acquire an appreciation of how complex and varied human processes are in health and disease, and show where it is developed and evidenced.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course aims to help you build an appreciation of how complex and varied human processes are in health and disease.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a graduate attribute the statement describes, in plain present with no modal, for all its courses at honours (FHEQ level 6, inferred): the complexity of human processes. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.14. Do not present it as a threshold every graduate must show or as a regulatory requirement. Set it beside 3.13 and the other 3.14 items, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what kind of graduate the course aims to produce, or when a team reviews its graduate attributes. To a student, put it plainly as a strength you can build and show; to staff, as an attribute to plan for and evidence. Ask: 'Where have you shown the complexity of human processes on your course so far?' Avoid presenting it as a pass requirement or reading the list aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b2
  forPractitioner: { text: "Plan the course so students acquire the ability to read and judge relevant literature critically and in full, from its aims and design to its methods, data interpretation and use, and show where it is developed and evidenced.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course aims to help you build the ability to read and judge relevant literature critically and in full, from its aims and design to its methods, data interpretation and use.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a graduate attribute the statement describes, in plain present with no modal, for all its courses at honours (FHEQ level 6, inferred): reading and evaluating literature. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.14. Do not present it as a threshold every graduate must show or as a regulatory requirement. Set it beside 3.13 and the other 3.14 items, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what kind of graduate the course aims to produce, or when a team reviews its graduate attributes. To a student, put it plainly as a strength you can build and show; to staff, as an attribute to plan for and evidence. Ask: 'Where have you shown reading and evaluating literature on your course so far?' Avoid presenting it as a pass requirement or reading the list aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b3
  forPractitioner: { text: "Plan the course so students acquire the capacity to explain the subject clearly, currently and accurately, and to discuss and debate it critically with specialists and non-specialists in suitable scientific language, and show where it is developed and evidenced.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course aims to help you build the capacity to explain the subject clearly, currently and accurately, and to discuss and debate it critically with specialists and non-specialists in suitable scientific language.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a graduate attribute the statement describes, in plain present with no modal, for all its courses at honours (FHEQ level 6, inferred): explaining and debating the subject. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.14. Do not present it as a threshold every graduate must show or as a regulatory requirement. Set it beside 3.13 and the other 3.14 items, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what kind of graduate the course aims to produce, or when a team reviews its graduate attributes. To a student, put it plainly as a strength you can build and show; to staff, as an attribute to plan for and evidence. Ask: 'Where have you shown explaining and debating the subject on your course so far?' Avoid presenting it as a pass requirement or reading the list aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b4
  forPractitioner: { text: "Plan the course so students acquire critical and analytical skills, with the recognition that claims and hypotheses need testing and evidence needs weighing, and show where it is developed and evidenced.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course aims to help you build critical and analytical skills, with the recognition that claims and hypotheses need testing and evidence needs weighing.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a graduate attribute the statement describes, in plain present with no modal, for all its courses at honours (FHEQ level 6, inferred): critical and analytical skills. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.14. Do not present it as a threshold every graduate must show or as a regulatory requirement. Set it beside 3.13 and the other 3.14 items, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what kind of graduate the course aims to produce, or when a team reviews its graduate attributes. To a student, put it plainly as a strength you can build and show; to staff, as an attribute to plan for and evidence. Ask: 'Where have you shown critical and analytical skills on your course so far?' Avoid presenting it as a pass requirement or reading the list aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b5
  forPractitioner: { text: "Plan the course so students acquire the ability to use a variety of study methods to investigate, record and analyse material, and show where it is developed and evidenced.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course aims to help you build the ability to use a variety of study methods to investigate, record and analyse material.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a graduate attribute the statement describes, in plain present with no modal, for all its courses at honours (FHEQ level 6, inferred): methods of study. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.14. Do not present it as a threshold every graduate must show or as a regulatory requirement. Set it beside 3.13 and the other 3.14 items, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what kind of graduate the course aims to produce, or when a team reviews its graduate attributes. To a student, put it plainly as a strength you can build and show; to staff, as an attribute to plan for and evidence. Ask: 'Where have you shown methods of study on your course so far?' Avoid presenting it as a pass requirement or reading the list aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b6
  forPractitioner: { text: "Plan the course so students acquire the ability to think for themselves, work autonomously and solve problems, and show where it is developed and evidenced.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course aims to help you build the ability to think for themselves, work autonomously and solve problems.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a graduate attribute the statement describes, in plain present with no modal, for all its courses at honours (FHEQ level 6, inferred): independent thinking and problem solving. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.14. Do not present it as a threshold every graduate must show or as a regulatory requirement. Set it beside 3.13 and the other 3.14 items, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what kind of graduate the course aims to produce, or when a team reviews its graduate attributes. To a student, put it plainly as a strength you can build and show; to staff, as an attribute to plan for and evidence. Ask: 'Where have you shown independent thinking and problem solving on your course so far?' Avoid presenting it as a pass requirement or reading the list aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b7
  forPractitioner: { text: "Plan the course so students acquire an understanding of how intellectual property is identified, protected and exploited in scientific innovation, and show where it is developed and evidenced.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course aims to help you build an understanding of how intellectual property is identified, protected and exploited in scientific innovation.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a graduate attribute the statement describes, in plain present with no modal, for all its courses at honours (FHEQ level 6, inferred): intellectual property. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.14. Do not present it as a threshold every graduate must show or as a regulatory requirement. Set it beside 3.13 and the other 3.14 items, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what kind of graduate the course aims to produce, or when a team reviews its graduate attributes. To a student, put it plainly as a strength you can build and show; to staff, as an attribute to plan for and evidence. Ask: 'Where have you shown intellectual property on your course so far?' Avoid presenting it as a pass requirement or reading the list aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b8
  forPractitioner: { text: "Plan the course so students acquire an appreciation of the subject's global reach, its effects on human life and the environment, and the ethics of applying it, and show where it is developed and evidenced.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course aims to help you build an appreciation of the subject's global reach, its effects on human life and the environment, and the ethics of applying it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a graduate attribute the statement describes, in plain present with no modal, for all its courses at honours (FHEQ level 6, inferred): global reach, impact and ethics. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.14. Do not present it as a threshold every graduate must show or as a regulatory requirement. Set it beside 3.13 and the other 3.14 items, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what kind of graduate the course aims to produce, or when a team reviews its graduate attributes. To a student, put it plainly as a strength you can build and show; to staff, as an attribute to plan for and evidence. Ask: 'Where have you shown global reach, impact and ethics on your course so far?' Avoid presenting it as a pass requirement or reading the list aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.16
  forPractitioner: { text: "Offer educational development to everyone who teaches on the course, demonstrators and visiting lecturers as well as permanent staff.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: everyone who teaches, demonstrators and visiting lecturers included, has access to educational professional development. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.16. Do not present it as regulation or as a legal duty; set it beside 3.15 and the PSF dimensions std:doc:advancehe-psf-dimensions-2023-framework."
  author-agent-dialogue: "Raise this when a team plans staff development or the use of demonstrators. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'What development in teaching do demonstrators and visiting lecturers get before they work with students?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.19
  forPractitioner: { text: "Set authentic, work-related assessment that builds professional skills, and allow reasonable adjustments to keep it inclusive.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: authentic assessment with real-world application, allowing reasonable adjustments for inclusivity. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.19. Do not present it as regulation or as a legal duty; set it beside 3.20, 3.21 and 1.21."
  author-agent-dialogue: "Raise this when a team designs or reviews an assessment. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Which assessment in the course looks most like a task done at work, and which least?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b1
  forPractitioner: { text: "Design assessment so that assessment serves learning as well as measuring it, and comes with effective feedback.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level principle for those designing assessment: assessment serves learning as well as measuring it, and comes with effective feedback. It applies across the courses the statement covers, at every level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.20 (principle 1). Do not present it as a student outcome or a regulation; set it beside the other 3.20 principles, 3.19 and 3.24."
  author-agent-dialogue: "Raise this when a team designs, reviews or moderates assessment. Frame it for staff as a design check: assessment serves learning as well as measuring it, and comes with effective feedback. Ask: 'How would you show an external examiner that this principle holds for your module?' Do not give it to a student as something they must do."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b2
  forPractitioner: { text: "Design assessment so that assessments are valid, reliable and consistent, and let students show mastery of a topic.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level principle for those designing assessment: assessments are valid, reliable and consistent, and let students show mastery of a topic. It applies across the courses the statement covers, at every level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.20 (principle 2). Do not present it as a student outcome or a regulation; set it beside the other 3.20 principles, 3.19 and 3.24."
  author-agent-dialogue: "Raise this when a team designs, reviews or moderates assessment. Frame it for staff as a design check: assessments are valid, reliable and consistent, and let students show mastery of a topic. Ask: 'How would you show an external examiner that this principle holds for your module?' Do not give it to a student as something they must do."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b3
  forPractitioner: { text: "Design assessment so that assessment and feedback take explicit account of accessibility and EDI.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level principle for those designing assessment: assessment and feedback take explicit account of accessibility and EDI. It applies across the courses the statement covers, at every level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.20 (principle 3). Do not present it as a student outcome or a regulation; set it beside the other 3.20 principles, 3.19 and 3.24."
  author-agent-dialogue: "Raise this when a team designs, reviews or moderates assessment. Frame it for staff as a design check: assessment and feedback take explicit account of accessibility and EDI. Ask: 'How would you show an external examiner that this principle holds for your module?' Do not give it to a student as something they must do."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b4
  forPractitioner: { text: "Design assessment so that information on assessment and feedback is explicit, accessible and transparent.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level principle for those designing assessment: information on assessment and feedback is explicit, accessible and transparent. It applies across the courses the statement covers, at every level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.20 (principle 4). Do not present it as a student outcome or a regulation; set it beside the other 3.20 principles, 3.19 and 3.24."
  author-agent-dialogue: "Raise this when a team designs, reviews or moderates assessment. Frame it for staff as a design check: information on assessment and feedback is explicit, accessible and transparent. Ask: 'How would you show an external examiner that this principle holds for your module?' Do not give it to a student as something they must do."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b5
  forPractitioner: { text: "Design assessment so that assessment and feedback are planned so that students and staff can manage their workloads.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level principle for those designing assessment: assessment and feedback are planned so that students and staff can manage their workloads. It applies across the courses the statement covers, at every level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.20 (principle 5). Do not present it as a student outcome or a regulation; set it beside the other 3.20 principles, 3.19 and 3.24."
  author-agent-dialogue: "Raise this when a team designs, reviews or moderates assessment. Frame it for staff as a design check: assessment and feedback are planned so that students and staff can manage their workloads. Ask: 'How would you show an external examiner that this principle holds for your module?' Do not give it to a student as something they must do."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b6
  forPractitioner: { text: "Design assessment so that assessment and feedback are part of the course and plainly tied to its learning outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level principle for those designing assessment: assessment and feedback are part of the course and plainly tied to its learning outcomes. It applies across the courses the statement covers, at every level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.20 (principle 6). Do not present it as a student outcome or a regulation; set it beside the other 3.20 principles, 3.19 and 3.24."
  author-agent-dialogue: "Raise this when a team designs, reviews or moderates assessment. Frame it for staff as a design check: assessment and feedback are part of the course and plainly tied to its learning outcomes. Ask: 'How would you show an external examiner that this principle holds for your module?' Do not give it to a student as something they must do."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b7
  forPractitioner: { text: "Design assessment so that assessment and feedback give students a chance to confirm what they know and understand.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level principle for those designing assessment: assessment and feedback give students a chance to confirm what they know and understand. It applies across the courses the statement covers, at every level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.20 (principle 7). Do not present it as a student outcome or a regulation; set it beside the other 3.20 principles, 3.19 and 3.24."
  author-agent-dialogue: "Raise this when a team designs, reviews or moderates assessment. Frame it for staff as a design check: assessment and feedback give students a chance to confirm what they know and understand. Ask: 'How would you show an external examiner that this principle holds for your module?' Do not give it to a student as something they must do."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b8
  forPractitioner: { text: "Design assessment so that assessment and feedback meet accreditation and approval requirements where needed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level principle for those designing assessment: assessment and feedback meet accreditation and approval requirements where needed. It applies across the courses the statement covers, at every level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.20 (principle 8). Do not present it as a student outcome or a regulation; set it beside the other 3.20 principles, 3.19 and 3.24."
  author-agent-dialogue: "Raise this when a team designs, reviews or moderates assessment. Frame it for staff as a design check: assessment and feedback meet accreditation and approval requirements where needed. Ask: 'How would you show an external examiner that this principle holds for your module?' Do not give it to a student as something they must do."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b9
  forPractitioner: { text: "Design assessment so that formative and summative assessment are balanced and usefully linked.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level principle for those designing assessment: formative and summative assessment are balanced and usefully linked. It applies across the courses the statement covers, at every level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.20 (principle 9). Do not present it as a student outcome or a regulation; set it beside the other 3.20 principles, 3.19 and 3.24."
  author-agent-dialogue: "Raise this when a team designs, reviews or moderates assessment. Frame it for staff as a design check: formative and summative assessment are balanced and usefully linked. Ask: 'How would you show an external examiner that this principle holds for your module?' Do not give it to a student as something they must do."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/3.24
  forPractitioner: { text: "Give feedback that is individual, clear, timely and tied to the brief, help students interpret it, and tell them in advance what form it will take and when it will arrive.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: feedback that is personal, understandable, empowering, manageable, developmental, timely and relevant, with support to interpret it and its timing made clear in advance. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 3.24. Do not present it as regulation or as a legal duty; set it beside 3.20.b1 and 3.19."
  author-agent-dialogue: "Raise this when a team sets its feedback policy or a student asks what feedback to expect. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'Do students know, before they submit, when and in what form their feedback will come?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.2
  forPractitioner: { text: "Use Annex D's class descriptions when setting how achievement above threshold is judged in the honours degree.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course team or provider, not a student outcome: each provider sets its own way of judging achievement above the minimum, referring to Annex D for the honours classes. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, para 4.2. Do not present it as regulation or as a legal duty; set it beside std:doc:qaa-fheq-2024-framework, Annex D (qaa/fheq-2024/annex-d/summary/lead/1st to 3rd), 4.1 and the Table 1 cells 4.5.b1.threshold to 4.5.b15.excellent."
  author-agent-dialogue: "Raise this when a team writes marking criteria or class descriptors for the honours degree. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: 'How do your marking criteria show the difference between a 2.1 and a first for the outcomes in Table 1?' Do not hand it to a student as a standard they must reach."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b1
  forPractitioner: { text: "Every honours graduate in either degree will describe and discuss the main concepts and phenomena of the course accurately, confidently and in depth, in the right technical language, aware of the whole range of the subject from molecules to cells and from health to disease. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will describe and discuss the main concepts and phenomena of the course accurately, confidently and in depth, in the right technical language, aware of the whole range of the subject from molecules to cells and from health to disease.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): key concepts across the subject. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 1, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b1.threshold and 4.5.b1.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about key concepts across the subject, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised key concepts across the subject, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b1.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who apply a wide-ranging grasp of the subject's concepts to discuss and explain the core of the course, and show enquiry that goes past it are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you apply a wide-ranging grasp of the subject's concepts to discuss and explain the core of the course, and show enquiry that goes past it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: key concepts across the subject, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 1, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b1.threshold and 4.5.b1 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in key concepts across the subject, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b1.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least recall the basics of the main concepts and phenomena met on the course and explain them in suitable technical terms. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will recall the basics of the main concepts and phenomena met on the course and explain them in suitable technical terms.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for key concepts across the subject (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 1, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b1 and the excellent cell 4.5.b1.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the Annex D third-class description qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about key concepts across the subject to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b2
  forPractitioner: { text: "Every honours graduate in either degree will use knowledge of human biological systems and methods to plan experiments and solve problems in theory and practice, alert to controls, bias, ethics and sustainability. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will use knowledge of human biological systems and methods to plan experiments and solve problems in theory and practice, alert to controls, bias, ethics and sustainability.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): experimental design and problem solving. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 2, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b2.threshold and 4.5.b2.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about experimental design and problem solving, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised experimental design and problem solving, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b2.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who devise and evaluate solutions to routine and unfamiliar problems by a range of methods, alert to controls, bias, ethics and sustainability are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you devise and evaluate solutions to routine and unfamiliar problems by a range of methods, alert to controls, bias, ethics and sustainability.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: experimental design and problem solving, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 2, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b2.threshold and 4.5.b2 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/cognitive/r3/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in experimental design and problem solving, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b2.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least show an understanding of basic experimental design and use methods on routine course problems, with some alertness to controls, bias, ethics and sustainability. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will show an understanding of basic experimental design and use methods on routine course problems, with some alertness to controls, bias, ethics and sustainability.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for experimental design and problem solving (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 2, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b2 and the excellent cell 4.5.b2.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D third-class description qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about experimental design and problem solving to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b3
  forPractitioner: { text: "Every honours graduate in either degree will describe, record and practise safe working, managing biological, chemical, laboratory and sample risks through risk assessment and practical work. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will describe, record and practise safe working, managing biological, chemical, laboratory and sample risks through risk assessment and practical work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): safe working and risk assessment. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 3, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b3.threshold and 4.5.b3.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about safe working and risk assessment, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised safe working and risk assessment, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b3.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who write and apply risk assessments independently so that practical work is done safely and reliably are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you write and apply risk assessments independently so that practical work is done safely and reliably.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: safe working and risk assessment, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 3, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b3.threshold and 4.5.b3 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/practical/r2/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in safe working and risk assessment, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b3.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least write and follow risk assessments so that practical work is done safely and reliably, with support. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will write and follow risk assessments so that practical work is done safely and reliably, with support.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for safe working and risk assessment (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 3, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b3 and the excellent cell 4.5.b3.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the Annex D third-class description qaa/fheq-2024/annex-d/practical/r2/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about safe working and risk assessment to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b4
  forPractitioner: { text: "Every honours graduate in either degree will choose and use suitable quantitative and qualitative practical techniques on course problems, weighing the theory behind each and its limits. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will choose and use suitable quantitative and qualitative practical techniques on course problems, weighing the theory behind each and its limits.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): practical laboratory techniques. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 4, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b4.threshold and 4.5.b4.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about practical laboratory techniques, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised practical laboratory techniques, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b4.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who design, refine and show competence in a broad range of suitable practical techniques, working with much autonomy and efficiency are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you design, refine and show competence in a broad range of suitable practical techniques, working with much autonomy and efficiency.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: practical laboratory techniques, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 4, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b4.threshold and 4.5.b4 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in practical laboratory techniques, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b4.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least propose, and show competence in, a broad range of suitable practical techniques, qualitative and quantitative, for the course. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will propose, and show competence in, a broad range of suitable practical techniques, qualitative and quantitative, for the course.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for practical laboratory techniques (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 4, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b4 and the excellent cell 4.5.b4.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the Annex D third-class description qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about practical laboratory techniques to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b5
  forPractitioner: { text: "Every honours graduate in either degree will use suitable databases and computational techniques and tools to deepen understanding of biomedical processes. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will use suitable databases and computational techniques and tools to deepen understanding of biomedical processes.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): databases and computational tools. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 5, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b5.threshold and 4.5.b5.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about databases and computational tools, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised databases and computational tools, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b5.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who choose and use suitable computational techniques and tools to investigate complex concepts, then evaluate and report the results in suitable terms are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you choose and use suitable computational techniques and tools to investigate complex concepts, then evaluate and report the results in suitable terms.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: databases and computational tools, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 5, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b5.threshold and 4.5.b5 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in databases and computational tools, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b5.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least use computational techniques and tools to investigate familiar course concepts and report the results in suitable terms. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will use computational techniques and tools to investigate familiar course concepts and report the results in suitable terms.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for databases and computational tools (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 5, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b5 and the excellent cell 4.5.b5.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the Annex D third-class description qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about databases and computational tools to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b6
  forPractitioner: { text: "Every honours graduate in either degree will read the literature of the subject to gain insight into it. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will read the literature of the subject to gain insight into it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): engaging with the literature. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 6, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b6.threshold and 4.5.b6.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about engaging with the literature, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised engaging with the literature, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b6.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who find and choose suitable sources of biological information, primary literature among them, and judge the adequacy of their methods, data and interpretation with much independence are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you find and choose suitable sources of biological information, primary literature among them, and judge the adequacy of their methods, data and interpretation with much independence.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: engaging with the literature, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 6, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b6.threshold and 4.5.b6 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/cognitive/r1/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in engaging with the literature, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b6.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least judge the evidence behind scientific claims by going to primary literature and commenting on how adequate its methods, data and interpretation are. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will judge the evidence behind scientific claims by going to primary literature and commenting on how adequate its methods, data and interpretation are.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for engaging with the literature (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 6, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b6 and the excellent cell 4.5.b6.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and the Annex D third-class description qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about engaging with the literature to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b7
  forPractitioner: { text: "Every honours graduate in either degree will complete open-ended investigative work independently through a project or research assignment. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will complete open-ended investigative work independently through a project or research assignment.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): an independent investigative project. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 7, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b7.threshold and 4.5.b7.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about an independent investigative project, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised an independent investigative project, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b7.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who plan, carry out and present a piece of independent work with marked independence and competence, analysing and critically evaluating data and showing strong time management, problem solving and independence are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you plan, carry out and present a piece of independent work with marked independence and competence, analysing and critically evaluating data and showing strong time management, problem solving and independence.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: an independent investigative project, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 7, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b7.threshold and 4.5.b7 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in an independent investigative project, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b7.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least plan, carry out and present a piece of independent work that analyses or evaluates data within a supported framework, showing some time management, problem solving and independence. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will plan, carry out and present a piece of independent work that analyses or evaluates data within a supported framework, showing some time management, problem solving and independence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for an independent investigative project (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 7, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b7 and the excellent cell 4.5.b7.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about an independent investigative project to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b8
  forPractitioner: { text: "Every honours graduate in either degree will value what the subject brings to the innovations of the modern world and what its graduates can offer to present and future challenges. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will value what the subject brings to the innovations of the modern world and what its graduates can offer to present and future challenges.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): the subject's contribution to world challenges. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 8, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b8.threshold and 4.5.b8.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about the subject's contribution to world challenges, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised the subject's contribution to world challenges, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b8.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who explain, propose and critique ways in which the subject and its scientists can help solve present and future world challenges are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you explain, propose and critique ways in which the subject and its scientists can help solve present and future world challenges.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: the subject's contribution to world challenges, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 8, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b8.threshold and 4.5.b8 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in the subject's contribution to world challenges, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b8.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least identify and discuss how the subject is applied to present and future world challenges, with some understanding of the part biomedical and research scientists play. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will identify and discuss how the subject is applied to present and future world challenges, with some understanding of the part biomedical and research scientists play.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for the subject's contribution to world challenges (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 8, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b8 and the excellent cell 4.5.b8.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and the Annex D third-class description qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about the subject's contribution to world challenges to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b9
  forPractitioner: { text: "Every honours graduate in either degree will recognise how the subject relates to and meets other subjects, so as to work well in a multidisciplinary setting. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will recognise how the subject relates to and meets other subjects, so as to work well in a multidisciplinary setting.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): links with other subjects. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 9, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b9.threshold and 4.5.b9.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about links with other subjects, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised links with other subjects, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b9.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who explain and evaluate what the subject contributes to interdisciplinary challenges and how interdisciplinary thinking helps solve scientific problems are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you explain and evaluate what the subject contributes to interdisciplinary challenges and how interdisciplinary thinking helps solve scientific problems.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: links with other subjects, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 9, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b9.threshold and 4.5.b9 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in links with other subjects, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b9.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least identify and explain how the subject relates to other subjects relevant to the course. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will identify and explain how the subject relates to other subjects relevant to the course.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for links with other subjects (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 9, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b9 and the excellent cell 4.5.b9.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the Annex D third-class description qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about links with other subjects to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b10
  forPractitioner: { text: "Every honours graduate in either degree will use mathematical and statistical ideas, processes and tools, such as rearranging equations, graphs and statistical tests, for problem solving or data evaluation. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will use mathematical and statistical ideas, processes and tools, such as rearranging equations, graphs and statistical tests, for problem solving or data evaluation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): mathematics and statistics. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 10, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b10.threshold and 4.5.b10.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about mathematics and statistics, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised mathematics and statistics, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b10.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who choose, use and evaluate suitable mathematical and statistical tools for problem solving or data evaluation are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you choose, use and evaluate suitable mathematical and statistical tools for problem solving or data evaluation.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: mathematics and statistics, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 10, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b10.threshold and 4.5.b10 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in mathematics and statistics, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b10.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least use mathematical and statistical tools on familiar problems or to evaluate data. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will use mathematical and statistical tools on familiar problems or to evaluate data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for mathematics and statistics (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 10, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b10 and the excellent cell 4.5.b10.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about mathematics and statistics to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b11
  forPractitioner: { text: "Every honours graduate in either degree will gather qualitative and quantitative data from course investigations, then analyse and interpret them to test hypotheses, set findings in context, present them and propose further lines of enquiry. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will gather qualitative and quantitative data from course investigations, then analyse and interpret them to test hypotheses, set findings in context, present them and propose further lines of enquiry.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): collecting and analysing data. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 11, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b11.threshold and 4.5.b11.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about collecting and analysing data, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised collecting and analysing data, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b11.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who collect data accurately and independently, with the same choices of analysis, interpretation, further enquiry and presentation, and a thorough sense of where the investigation sits in the field are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you collect data accurately and independently, with the same choices of analysis, interpretation, further enquiry and presentation, and a thorough sense of where the investigation sits in the field.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: collecting and analysing data, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 11, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b11.threshold and 4.5.b11 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/practical/r4/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in collecting and analysing data, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b11.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least collect data accurately, choosing suitable analysis, interpreting findings to test hypotheses, considering further enquiry and handling data to present them well. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will collect data accurately, choosing suitable analysis, interpreting findings to test hypotheses, considering further enquiry and handling data to present them well.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for collecting and analysing data (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 11, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b11 and the excellent cell 4.5.b11.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and the Annex D third-class description qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about collecting and analysing data to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b12
  forPractitioner: { text: "Every honours graduate in either degree will work well with others in a group, contributing positively and flexibly to what the team produces. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will work well with others in a group, contributing positively and flexibly to what the team produces.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): teamwork. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 12, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b12.threshold and 4.5.b12.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about teamwork, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised teamwork, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b12.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who find and use effective strategies for group work and make clear, valuable contributions to team outputs, showing good teamwork or leadership are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you find and use effective strategies for group work and make clear, valuable contributions to team outputs, showing good teamwork or leadership.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: teamwork, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 12, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b12.threshold and 4.5.b12 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/transferable/r2/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in teamwork, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b12.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least take an effective part in group and team work, with clear contributions. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will take an effective part in group and team work, with clear contributions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for teamwork (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 12, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b12 and the excellent cell 4.5.b12.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about teamwork to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b13
  forPractitioner: { text: "Every honours graduate in either degree will communicate well, choosing content, media and methods to suit audience, purpose and subject. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will communicate well, choosing content, media and methods to suit audience, purpose and subject.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): communication. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 13, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b13.threshold and 4.5.b13.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about communication, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised communication, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b13.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who convey information, ideas, problems and solutions to a high standard in speech and other forms, accurately, fluently and with sophistication, always pitched to the audience are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you convey information, ideas, problems and solutions to a high standard in speech and other forms, accurately, fluently and with sophistication, always pitched to the audience.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: communication, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 13, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b13.threshold and 4.5.b13 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in communication, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b13.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least convey information, ideas, problems and solutions in speech or other forms, expressed clearly. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will convey information, ideas, problems and solutions in speech or other forms, expressed clearly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for communication (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 13, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b13 and the excellent cell 4.5.b13.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about communication to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b14
  forPractitioner: { text: "Every honours graduate in either degree will bring ethical awareness to work in the subject and appreciate its history and the effects its advances have on society. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will bring ethical awareness to work in the subject and appreciate its history and the effects its advances have on society.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): ethics, history and societal impact. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 14, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b14.threshold and 4.5.b14.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about ethics, history and societal impact, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised ethics, history and societal impact, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b14.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who understand and evaluate the ethical issues and social effects of advances in the subject, with some understanding of its history are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you understand and evaluate the ethical issues and social effects of advances in the subject, with some understanding of its history.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: ethics, history and societal impact, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 14, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b14.threshold and 4.5.b14 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in ethics, history and societal impact, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b14.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least describe some ethical issues and social effects of advances in the subject, with some acknowledgement of its history. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will describe some ethical issues and social effects of advances in the subject, with some acknowledgement of its history.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for ethics, history and societal impact (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 14, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b14 and the excellent cell 4.5.b14.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and the Annex D third-class description qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Raise this when a student asks what they must show about ethics, history and societal impact to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b15
  forPractitioner: { text: "Every honours graduate in either degree will keep up with advances in the subject and appreciate that knowledge shifts as new findings appear. Teach and assess this across the course, grading it by the threshold and excellent cells beside it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will keep up with advances in the subject and appreciate that knowledge shifts as new findings appear.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): keeping up with advances. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 15, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside its threshold and excellent cells 4.5.b15.threshold and 4.5.b15.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about keeping up with advances, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised keeping up with advances, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b15.excellent
  forPractitioner: { text: "Use this to recognise excellent work: graduates who show a clear grasp that knowledge in the subject is fluid, with the ability to fold new findings into earlier understanding are at the top of the range. Design tasks that give the strongest students room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level, you show a clear grasp that knowledge in the subject is fluid, with the ability to fold new findings into earlier understanding.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: keeping up with advances, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 15, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. Set it beside 4.5.b15.threshold and 4.5.b15 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3 and, as an inferred reading only, the Annex D first-class description qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Raise this with a student aiming for the top of the range in keeping up with advances, or with a team designing stretch tasks. To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b15.threshold
  forPractitioner: { text: "This is the floor: every honours graduate will at least show awareness that new findings may change how topics are understood and that much in the subject is not yet understood, with some ability to keep up to date. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will show awareness that new findings may change how topics are understood and that much in the subject is not yet understood, with some ability to keep up to date.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold standard, the minimum every honours graduate will have shown for keeping up with advances (FHEQ level 6; FQHEIS level 10 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 15, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. Set it beside the benchmark outcome 4.5.b15 and the excellent cell 4.5.b15.excellent in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3 and the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise this when a student asks what they must show about keeping up with advances to pass, or when a team checks that every graduate meets the minimum. To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b16
  forPractitioner: { text: "Every honours graduate in either degree will act professionally, mindful of legal, ethical and social responsibilities, and model good practice that gives a positive view of the subject and its scientists. Teach and assess this across the course.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will act professionally, mindful of legal, ethical and social responsibilities, and model good practice that gives a positive view of the subject and its scientists.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): professional conduct. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 1, row 16, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. Set it beside 1.4 and 2.9 in this document, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours graduate should be able to do about professional conduct, or when a team maps its modules to the table. To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. Ask: 'Where in your course have you practised professional conduct, and what did you produce?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b17
  forPractitioner: { text: "At master's level, students should be able to bring a systematic, broad and current understanding of biomedical concepts to bear on complex problems, on top of the honours outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "On a master's course you should become able to pull together a broad, systematic understanding of current and cutting-edge biomedical ideas and use it to solve complex problems.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome for master's graduates, added to the honours outcomes of Table 1 (FHEQ level 7; FQHEIS level 11 in Scotland). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 2, row 1. Do not claim it holds at honours level or that it is regulation. Set it beside 4.5.b17.threshold and 4.5.b17.excellent, 3.23, the FHEQ master's descriptors qaa/fheq-2024/4.17.b1 and qaa/fheq-2024/4.17.b5, and spine:7."
  author-agent-dialogue: "Raise this when a master's student asks how the step up from honours shows, or when a team writes level 7 outcomes. To a student, put it as using leading-edge understanding on problems with no ready answer; to staff, as the master's addition to the honours outcomes. Ask: 'Which complex problem in your project needed ideas from more than one area, and how did you combine them?' Avoid reading the table aloud."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b17.excellent
  forPractitioner: { text: "Excellent master's work meets the first Table 2 outcome with a high degree of independence and autonomy.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At an excellent level on a master's course, you do this largely on your own, directing the work yourself.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the master's excellent standard for the first Table 2 outcome, which describes rather than requires: it is met with much independence and autonomy (FHEQ level 7; FQHEIS level 11). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 2, row 1, excellent standard. Do not present it as expected of every master's graduate; Part E notes the cell may span every Table 2 row. Set it beside 4.5.b17.threshold, 4.5.b17 and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Raise this with a master's student aiming high or a team designing distinction descriptors. To a student, describe excellent work as directing your own enquiry; to staff, as autonomy shown in the work. Ask: 'Where did you change the direction of your project on your own judgement?' Avoid implying that every student must reach it."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b17.threshold
  forPractitioner: { text: "The master's minimum: students meet the first Table 2 outcome while still relying on substantial support and guidance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum on a master's course, you can do this with a good deal of support and guidance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the master's threshold for the first Table 2 outcome: it is met with considerable support and guidance (FHEQ level 7; FQHEIS level 11). Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 2, row 1, threshold standard. Do not apply it at honours level or treat it as a mark scheme; Part E notes the cell may span every Table 2 row. Set it beside 4.5.b17 and 4.5.b17.excellent, and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Raise this when a master's student worries about how much help they are getting, or when a team sets its pass descriptors. To a student, explain that needing guidance is acceptable at the minimum; to staff, frame it as the support the floor allows. Ask: 'Which decisions in your project did you take yourself, and which with your supervisor?' Do not present the excellent cell as the minimum."
- statement: qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b18
  forPractitioner: { text: "At master's level, students should be able to design investigations from a critical synthesis of the literature, plan a project with its ethics, hazards, environmental and cost aspects, develop advanced experimental skills and discuss a substantial research project in full.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "On a master's course you should become able to draw on a wide range of scientific literature to design your own methods, plan a substantial research project with its ethical, safety, environmental and cost aspects, build advanced laboratory and investigative skills, and discuss your project's background, methods, results and impact.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome for master's graduates, added to Table 1 (FHEQ level 7; FQHEIS level 11 in Scotland): research from the literature through to a significant project. Cite it as QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement, Table 2, rows 2 to 5. Do not claim it holds at honours level, and note that the statement grades it only through the support or independence cells of row 1 (Part E). Set it beside 4.5.b17, 3.23, 4.5.b7, the FHEQ master's descriptors qaa/fheq-2024/4.17.b2 and qaa/fheq-2024/4.17.b4.2, and spine:7."
  author-agent-dialogue: "Raise this when a master's student is planning their research project, or when a team designs the project module. To a student, put it as owning the whole arc of a research project, from reading to discussing impact; to staff, as the master's research outcome. Ask: 'What did the literature leave open that your methods are designed to answer, and what are the costs and risks?' Avoid reading the table aloud."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.3; 4.2 (\"FHEQ Level 6\" for the bachelor's degree with honours)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.3; 4.2 (\"FQHEIS Level 10\")" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.3 (\"FHEQ Level 7\" for the integrated master's degree with honours); Table 2 (master's)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.3 (\"FQHEIS Level 11\")" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.3: \"FHEQ Level 6; FQHEIS Level 10\"; 4.2); matches std:doc:qaa-fheq-2024-framework Table 1" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.3: \"FHEQ Level 7; FQHEIS Level 11\"); matches std:doc:qaa-fheq-2024-framework 4.17 (one descriptor shared) and Table 1" }
  - { from: "fheq:6", to: "spine:6", relation: "equivalent", basis: "inferred from std:ref:uk-framework R2" }
  - { from: "fheq:7", to: "spine:7", relation: "equivalent", basis: "inferred from std:ref:uk-framework R2" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "2.7", "2.10", "2.17", "2.22", "3.16", "3.19", "3.20"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.19", "1.20", "1.21", "1.22", "2.7", "2.8", "2.17", "2.27", "3.16", "3.19", "3.20"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.23", "1.24", "1.25", "1.29", "2.22", "3.12", "4.5"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "2.17", "3.12", "3.14", "3.19"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-biomedical-sciences-2019-benchmarks (not yet ingested)", note: "the fourth edition (2019), named in the back matter; key changes listed in the front matter" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the honours classification descriptions (4.2); FHEQ and FQHEIS levels for the awards (2.3)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS Levels 10 and 11 (2.3, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "Education for Sustainable Development Guidance (1.25)" }
- { rel: "refersTo", target: "std:doc:qaa-enterprise-2018-guidance", note: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (1.31)" }
- { rel: "refersTo", target: "QAA Characteristics Statement: Higher Education in Apprenticeships (not yet ingested)", note: "2.6" }
- { rel: "refersTo", target: "HCPC Standards of Proficiency for Biomedical Scientists (not yet ingested)", note: "1.14, 1.15, 4.4; the source of Appendix 1" }
- { rel: "refersTo", target: "IBMS accreditation criteria and Registration Training Portfolio (not yet ingested)", note: "1.2, 1.15, 2.4, 3.2, 3.4" }
- { rel: "refersTo", target: "Association for Nutrition competency requirements for course accreditation (not yet ingested)", note: "3.7" }
- { rel: "refersTo", target: "UNESCO (2019), Education for Sustainable Development", note: "the ESD definition quoted (1.24)" }
- { rel: "refersTo", target: "United Nations, Sustainable Development Goals", note: "1.24" }
- { rel: "refersTo", target: "QAA Quality Code for Higher Education, Advice and Guidance (not yet ingested)", note: "front matter; references" }
- { rel: "refersTo", target: "QAA Glossary (not ingested)", note: "front matter" }
- { rel: "refersTo", target: "HEA (2016) Framework for embedding employability in higher education (not yet ingested)", note: "list of references only" }
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
- Two related degrees told apart: Biomedical Science (singular), built to the professional body's accreditation requirements and covering every clinical laboratory specialism, and Biomedical Sciences (plural), broader and reaching into other human biology, including named awards such as pharmacology, molecular or cell biology (D1, front matter; 1.1 to 1.3).
- Its object is the scientific basis of human health and disease, from molecules and cells to whole systems (D1, 1.4; 3.12; Table 1).
- The singular degree is the academic step towards registration as a Biomedical Scientist, a protected title; with verified clinical training, it leads to work in NHS and private diagnostic pathology laboratories (D1, 1.2; 1.6; 1.8; 1.12 to 1.15).
- Hands-on laboratory work is essential, giving technical skill and safe, accurate practice in clinical, industrial and research laboratories (D1, 1.10; 2.14).
- Research skills, critical appraisal and independent investigation run through the courses and prepare for employment or research degrees (D1, 1.11; Table 1).
- Related courses in the area, Pharmacology, Human Nutrition and Physiology, share a common core and have their own content and accrediting bodies (D1, 2.5; 2.28; 3.5 to 3.11).
- A systems-led approach integrates the clinical specialisms with the underlying science of investigation and treatment (D1, 3.3; 3.10).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "inclusion throughout the course; confronting the field's history of injustice and the biases in what science is done and how data are read; diverse contributors and case studies; global inequality in access to diagnosis and treatment; misuse of discoveries for unequal ends (D1, 1.16 to 1.19; 2.10; 2.22; 3.20)"
  statements: ["qaa/biomedical-science-and-biomedical-sciences-2023/1.16", "qaa/biomedical-science-and-biomedical-sciences-2023/1.17", "qaa/biomedical-science-and-biomedical-sciences-2023/1.18", "qaa/biomedical-science-and-biomedical-sciences-2023/1.19", "qaa/biomedical-science-and-biomedical-sciences-2023/2.10.b2", "qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b3", "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b14", "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b14.threshold", "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b14.excellent"]
- theme: theme:accessibility
  inThisSubject: "fully accessible curricula, assessment and practical work, anticipating needs in laboratories, fieldwork and placements, with inclusive design and reasonable adjustments, and placements funded so all can take part (D1, 1.20 to 1.22; 2.7; 2.8; 2.17; 3.19; 3.20)"
  statements: ["qaa/biomedical-science-and-biomedical-sciences-2023/1.20", "qaa/biomedical-science-and-biomedical-sciences-2023/1.21", "qaa/biomedical-science-and-biomedical-sciences-2023/1.22", "qaa/biomedical-science-and-biomedical-sciences-2023/2.7", "qaa/biomedical-science-and-biomedical-sciences-2023/2.8", "qaa/biomedical-science-and-biomedical-sciences-2023/2.17", "qaa/biomedical-science-and-biomedical-sciences-2023/3.19", "qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b3", "qaa/biomedical-science-and-biomedical-sciences-2023/3.20.b4"]
- theme: theme:esd
  inThisSubject: "sustainable laboratory practice (reducing paper and plastics, safer chemicals, the LEAF initiative), environmental impact and the SDGs, with ethics and sustainability a consideration in experimental design and project planning (D1, 1.23 to 1.25; 2.22; Table 1 row 2; Table 2)"
  statements: ["qaa/biomedical-science-and-biomedical-sciences-2023/1.25", "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b2", "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b2.threshold", "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b2.excellent", "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b18"]
- theme: theme:enterprise
  inThisSubject: "employability and entrepreneurship as competencies, employer links, placements, intellectual property and commercialisation, and taking charge of one's own professional development (D1, 1.26 to 1.31; 2.17; 3.12; 3.14)"
  statements: ["qaa/biomedical-science-and-biomedical-sciences-2023/1.30", "qaa/biomedical-science-and-biomedical-sciences-2023/2.17", "qaa/biomedical-science-and-biomedical-sciences-2023/3.14.b7", "qaa/biomedical-science-and-biomedical-sciences-2023/3.19", "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b8", "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b8.threshold", "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b8.excellent"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.1", gloss: "content common to all the courses: anatomy and physiology, cell biology, biochemistry, microbiology, immunology, developmental biology, supporting physics and chemistry, genetics and genomics, molecular biology, pathology of disease, bioinformatics, pharmacology" }
  - { component: "3.4", gloss: "the clinical pathology areas of the accredited degree: cellular pathology, clinical biochemistry, clinical immunology, haematology, transfusion science, clinical genetics, medical microbiology, near-patient testing, laboratory quality" }
  - { component: "3.5", gloss: "other specialisms in the area; pharmacology defined" }
  - { component: "3.6", gloss: "Pharmacology: pharmacodynamics, pharmacokinetics, individual variation, pharmacological methods" }
  - { component: "3.7", gloss: "Human Nutrition: nutritional science and its application to health" }
  - { component: "3.9", gloss: "Human Nutrition outcomes: metabolism, clinical biochemistry, nutritional assessment, food science, clinical nutrition" }
  - { component: "3.10", gloss: "Physiology as an integrative science" }
  - { component: "3.11", gloss: "Physiology outcomes, system by system, with experimentation and data" }
  - { component: "3.12", gloss: "approaches to study common to all the courses" }
practices:
  - { component: "3.15", kind: "teaching", gloss: "scaffolded teaching moving towards independent study; integration across the programme" }
  - { component: "3.16", kind: "teaching", gloss: "student-centred, accessible strategies; synchronous, asynchronous and blended delivery; staff development" }
  - { component: "3.17", kind: "learning", gloss: "synchronous activities: lectures, laboratory classes, problem-based learning, workshops, fieldwork, peer learning" }
  - { component: "3.18", kind: "learning", gloss: "asynchronous activities: self-study, recordings, virtual experiments, research projects, reflective portfolios, placements" }
  - { component: "3.19", kind: "assessment", gloss: "progressive, varied and authentic assessment, discriminating threshold from higher achievement" }
  - { component: "3.20", kind: "assessment", gloss: "principles for designing assessment" }
  - { component: "3.21", kind: "assessment", gloss: "themes for authentic assessment: practical, collaborative, integrative, communication, professional" }
  - { component: "3.22", kind: "assessment", gloss: "examination formats and coursework" }
  - { component: "3.23", kind: "assessment", gloss: "integrated master's assessment: unfamiliar problems and the full range of research skills" }
  - { component: "3.24", kind: "assessment", gloss: "qualities of feedback" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.1; Table 1 lead-in", award: "bachelor's with honours", items: 15 }
  - { rung: "threshold", leadIn: "4.5; Table 2 lead-in", award: "master's", items: 1 }
  - { rung: "typical", leadIn: "none", award: "none", items: 0 }
  - { rung: "excellent", leadIn: "4.1; Table 1 lead-in", award: "bachelor's with honours", items: 15 }
  - { rung: "excellent", leadIn: "4.5; Table 2 lead-in", award: "master's", items: 1 }
rungBases: "Two tables, each with three columns: Benchmark outcome, Threshold standard and Excellent standard. Table 1 (honours) has 16 rows: 15 graded at threshold and excellent, the last (acting professionally) an outcome only. Table 2 (master's, \"in addition to Table 1\") grades its first outcome only by support (threshold: with significant support and guidance) and independence (excellent: with a high degree of independence and autonomy). The benchmark outcome column is recorded as rung none, outcome; each threshold and excellent cell is its own S4 record, paired by row (gradeOf stated). No typical rung; 4.2 points to Annex D for the classes."
outcomeLists:
  - { leadIn: "Table 1", gloss: "benchmark outcomes for the honours degree (first column)", items: 16, award: ["bachelor's with honours"] }
  - { leadIn: "Table 2", gloss: "master's outcomes in addition to Table 1 (rows 2 to 5 recorded as one)", items: 2, award: ["master's"] }
  - { leadIn: "3.4", gloss: "clinical pathology knowledge for graduates of the accredited degree, in nine specialisms", items: 38, award: ["bachelor's with honours"] }
  - { leadIn: "3.6", gloss: "core outcomes for Pharmacology graduates", items: 11, award: ["bachelor's with honours"] }
  - { leadIn: "3.9", gloss: "core outcomes for Human Nutrition graduates", items: 8, award: ["bachelor's with honours"] }
  - { leadIn: "3.11", gloss: "core outcomes for Physiology graduates", items: 28, award: ["bachelor's with honours"] }
  - { leadIn: "3.14", gloss: "graduate attributes for all courses (plain present; force describes)", items: 8, award: ["bachelor's with honours", "master's"] }
outcomes:
  - { outcome: "key concepts across the subject", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b1.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b1.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "experimental design and problem solving", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b2.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b2.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "safe working and risk assessment", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b3.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b3.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "practical laboratory techniques", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b4.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b4.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "databases and computational tools", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b5.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b5.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "engaging with the literature", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b6.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b6.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "an independent investigative project", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b7.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b7.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "the subject's contribution to world challenges", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b8.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b8.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "links with other subjects", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b9.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b9.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "mathematics and statistics", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b10.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b10.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "collecting and analysing data", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b11.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b11.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "teamwork", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b12.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b12.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "communication", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b13.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b13.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "ethics, history and societal impact", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b14.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b14.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "keeping up with advances", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b15.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b15.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "applying leading-edge understanding to complex problems", threshold: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b17.threshold", typical: "none", excellent: "qaa/biomedical-science-and-biomedical-sciences-2023/4.5.b17.excellent", basis: "stated", domain: "understanding", award: "master's" }
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
- { body: "Institute of Biomedical Science (IBMS)", says: "the professional body that accredits Biomedical Science degrees and approves training laboratories, sets the clinical specialisms the degree must cover, runs the Registration Training Portfolio and awards the Certificate of Competence that makes graduates eligible to apply for registration; it also advises Biomedical Sciences graduates on top-up modules (D1, front matter; 1.2; 1.3; 1.6 to 1.8; 1.15; 2.4; 2.11; 2.28; 3.2; 3.4; 4.4)", requirements: "not yet ingested: IBMS accreditation criteria and Registration Training Portfolio (Part E)" }
- { body: "Health and Care Professions Council (HCPC)", says: "the statutory regulator under the Health Act 1999 that holds the register and protects the title Biomedical Scientist; registration rests on its Standards of Proficiency, which the standards of the accredited degree are linked to; it may also approve degrees with integrated placements directly, and registers dietitians (D1, 1.2; 1.3; 1.6; 1.12 to 1.15; 2.1; 2.4; 2.9; 3.2; 3.4; 3.8; 4.4; Appendix 1)", requirements: "not yet ingested: HCPC Standards of Proficiency for Biomedical Scientists (Part E)" }
- { body: "Royal Society of Biology", says: "accredits Biomedical Science and Biomedical Sciences programmes and Human Physiology programmes (D1, 2.28)", requirements: "not yet ingested (Part E)" }
- { body: "Association for Nutrition (AfN)", says: "accredits Nutrition courses against its competency requirements and holds a voluntary register for nutritionists (D1, 2.28; 3.7; 3.8)", requirements: "not yet ingested: AfN competency requirements (Part E)" }
- { body: "British Pharmacological Society", says: "accredits Pharmacology programmes (D1, 2.28)", requirements: "not yet ingested (Part E)" }
- { body: "professional, statutory and regulatory bodies (PSRBs) and professional bodies, in general", says: "the statement supports them with academic standards; they may add requirements, accredit other specialisms, help co-create enterprise education, and take part in course enhancement (D1, front matter; 1.29; 2.18; 2.27; 3.5)", requirements: "not applicable: no one body" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "2.7", "2.10", "2.17", "2.22", "3.16", "3.19", "3.20"], statements: ["1.16", "1.17", "1.18", "1.19", "2.10.b2", "3.20.b3", "4.5.b14", "4.5.b14.threshold", "4.5.b14.excellent"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["1.19", "1.20", "1.21", "1.22", "2.7", "2.8", "2.17", "2.27", "3.16", "3.19", "3.20"], statements: ["1.20", "1.21", "1.22", "2.7", "2.8", "2.17", "3.19", "3.20.b3", "3.20.b4"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.23", "1.24", "1.25", "1.29", "2.22", "3.12", "4.5"], statements: ["1.25", "4.5.b2", "4.5.b2.threshold", "4.5.b2.excellent", "4.5.b18"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "2.17", "3.12", "3.14", "3.19"], statements: ["1.30", "2.17", "3.14.b7", "3.19", "4.5.b8", "4.5.b8.threshold", "4.5.b8.excellent"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.3", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.3", "4.2"] }
bodies:
  - { body: "Institute of Biomedical Science (IBMS)", citedIn: ["1.2", "1.3", "1.6", "1.7", "1.8", "1.12", "1.15", "2.1", "2.4", "2.9", "2.11", "2.28", "3.2", "3.4", "4.4"] }
  - { body: "Health and Care Professions Council (HCPC)", citedIn: ["1.2", "1.3", "1.6", "1.12", "1.13", "1.14", "1.15", "2.1", "2.4", "2.9", "3.2", "3.4", "3.8", "4.4"] }
  - { body: "Royal Society of Biology", citedIn: ["2.28"] }
  - { body: "Association for Nutrition (AfN)", citedIn: ["2.28", "3.7", "3.8"] }
  - { body: "British Pharmacological Society", citedIn: ["2.28"] }
  - { body: "professional, statutory and regulatory bodies, unnamed", citedIn: ["1.29", "2.18", "2.27", "3.5"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "common descriptions of the four honours classes (1st, 2.1, 2.2, 3rd), for judging achievement above the minimum" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "the QAA and Advance HE Education for Sustainable Development Guidance", citedIn: ["1.25"], role: "teaching, key competencies, learning outcomes and assessment for sustainability" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers", citedIn: ["1.31"], role: "more information on enterprise and entrepreneurship education" }
  - { document: "not yet ingested: listed in Part E", named: "Characteristics Statement for Higher Education in Apprenticeships", citedIn: ["2.6"], role: "the general features of degree apprenticeships" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "biomedical-scientist", definition: "the protected title, given by the regulator, for those who carry out laboratory investigations on tissue and fluid samples to help diagnose and monitor disease, judge how well treatments work and advise on treatment and prevention (D1, 1.13)", beneficiaryDefinition: "a registered professional who runs laboratory tests on patient samples to help diagnose and monitor disease", scopeNote: "protected title; use requires registration (1.14)", category: "unknown", practices: ["health", "biomedical science"] }
- { slug: "certificate-of-competence", definition: "the professional body's award showing that a person meets the regulator's proficiency standards and is fit to practise, making them eligible to apply for registration (D1, 1.15)", beneficiaryDefinition: "the certificate you get after verified clinical training that lets you apply for registration", scopeNote: "awarded after the Registration Training Portfolio", category: "unknown", practices: ["health", "biomedical science"] }
- { slug: "near-patient-testing", definition: "analytical testing done for a patient by health professionals outside the usual laboratory (D1, 3.4)", beneficiaryDefinition: "tests done close to the patient, such as on a ward or in a clinic, rather than in the main laboratory", scopeNote: "NPT; also point-of-care testing", category: "unknown", practices: ["health", "biomedical science"] }
- { slug: "education-for-sustainable-development", definition: "after UNESCO (2019), holistic and transformational education covering content, outcomes, pedagogy and environment; in higher education, curriculum structures and content that support sustainable development (D1, 1.24)", beneficiaryDefinition: "learning that helps you understand and act on sustainability", scopeNote: "ESD; a cross-cutting theme", category: "unknown", practices: ["education"] }
- { slug: "employability", definition: "a set of competencies, combining knowledge, skills and behaviours, that make people more likely to gain work and succeed in it, to their own, society's and the economy's benefit (D1, 1.26)", beneficiaryDefinition: "the knowledge, skills and behaviours that help you get work and do well in it", scopeNote: "paired with entrepreneurship in 1.26", category: "unknown", practices: ["education"] }
- { slug: "equity", definition: "opening access to study for people with differing needs while removing arbitrary and needless barriers to success (D1, 1.20)", beneficiaryDefinition: "making sure everyone with the potential to succeed can take part on fair terms", scopeNote: "used with accessibility", category: "unknown", practices: ["education"] }
- { slug: "pharmacology", definition: "the science of drugs: their chemical and physical properties, their actions on living tissues and systems and their effects on health and disease (D1, 3.5)", beneficiaryDefinition: "the study of drugs and how they act on the body", scopeNote: "also pharmacodynamics and pharmacokinetics, 3.6", category: "unknown", practices: ["biomedical science"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "biomedical-scientist", form: "Biomedical Scientist", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "certificate-of-competence", form: "Certificate of Competence", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "near-patient-testing", form: "Near-patient testing (NPT)/point-of-care testing", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "education-for-sustainable-development", form: "Education for Sustainable Development (ESD)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "employability", form: "Employability", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "equity", form: "Equity", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "pharmacology", form: "Pharmacology", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Biomedical Science and Biomedical Sciences"
  edition: "March 2023"
  year: 2023
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/biomedical-science-and-biomedical-sciences-2023/biomedical-science-and-biomedical-sciences-2023.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 5a6dbd79e6d960dbd60e18f820da36dd685b4c933f3c4e5f4e0629614d9284d0
  heldFiles: ["wkspc2601-library/txt/qaa-2023-biomedical-science-biomedical-sciences-subject-benchmark-standard.txt", "wkspc2601-library/txt/qaa-2023-biomedical-science-biomedical-sciences-subject-benchmark-standard.norm.txt", "wkspc2601-library/records/qaa-2023-biomedical-science-biomedical-sciences-subject-benchmark-standard.chunks.json", "wkspc2601-library/records/qaa-2023-biomedical-science-biomedical-sciences-subject-benchmark-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0034", citation: "HCPC, Standards of Proficiency: Biomedical Scientists", settles: ["SB5", "S7", "Appendix 1"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0035", citation: "IBMS, accreditation criteria for Biomedical Science degrees and the Registration Training Portfolio", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0036", citation: "QAA (2019) Characteristics Statement: Higher Education in Apprenticeships", settles: ["SB6", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0037", citation: "QAA (2019) Subject Benchmark Statement: Biomedical Sciences (fourth edition)", settles: ["S7"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- SB4, rung shape: two three-column tables (Benchmark outcome; Threshold standard; Excellent standard), not separate rung lists as in Psychology. Table 1 (honours, 16 rows): 15 rows graded at threshold and excellent; row 16 (act professionally) has an outcome cell only. Table 2 (master's, "in addition to Table 1", lead-in "should be able to"): one outcome graded by support (threshold) and independence (excellent). No typical rung. The tables sit inside the skeleton's component 4.5 (after 4.5's own sentence); their rows are given ids 4.5.b1 to 4.5.b18, cells <id>.threshold and <id>.excellent.
- S4, the benchmark outcome column is recorded as its own record (type outcome, rung none), because its text differs from both graded cells. Its force is the table lead-in's "will have"; recorded as threshold (from 4.1, "minimum threshold standards that a student will have demonstrated"), since the builder's force check reads only 600 characters before a span and the lead-in is out of reach for most rows. For P3: whether the column should carry will.
- S4, force: threshold cells take threshold from 4.1; excellent cells take describes (4.1: the standards "indicate excellent levels of achievement"), as in Anthropology (run 0084). Table 2 rows take should from the lead-in; its threshold and excellent cells as Table 1's.
- S4, gradeOf: 16 links, each excellent cell to the threshold cell in the same row, basis stated (the issuer pairs them by row); the builder's S4 line reads them from GRADE with |stated.
- Text fault: Table 1 row 11 (data collection) is interleaved across a page break by extraction (outcome, threshold and excellent cells each split in two). Its three records share the whole row's span, so each `source` holds all three cells. For P3 or a re-extraction.
- Table 2 layout lost in extraction: after row 1 come "Interrogate and integrate ...", then three verbless noun phrases (project planning; development of advanced experimental and investigative skills; discussion of a significant research project). Read as one research outcome and recorded as one record, 4.5.b18. The threshold and excellent cells ("With significant support and guidance"; "With a high degree of independence and autonomy") are placed on row 1 only; they may be merged cells spanning every Table 2 row. For P3.
- Table 2 award: the lead-in says "master's degree"; 2.3 says integrated master's for Biomedical Sciences only (FHEQ 7, FQHEIS 11) and names standalone MSc and MRes courses; 3.23 speaks of integrated master's. Award recorded as master's; which master's awards Table 2 serves is for P3.
- Appendix 1 (draft threshold suggestions drawn from the HCPC Standards of Proficiency through the IBMS portfolio, 28 items under "Registered biomedical scientists must") is excluded as the body's requirements and a draft, though 4.4 says the standards for the accredited degree "are detailed in Appendix 1". Its items cite HCPC SoP numbers. For P3: ingest as a separate standards document from the HCPC SoP (D3).
- Outcome lists outside section 4 (new against Psychology): 3.4 (nine clinical pathology specialisms, 38 items under "A Biomedical Science graduate will have knowledge of"), 3.6 Pharmacology (11), 3.9 Human Nutrition (8), 3.11 Physiology (28), all "will have". Group headings that end in a colon (3.4.b1, b6, b11, b15, b21, b28, b33, b38, b42, each a definition plus lead-in; 3.6.b1, b8; 3.9.b1; 3.11.b1, b6, b14, b17, b22, b25, b30, b34) are not recorded as statements: they are stems for the items beneath. 3.6.b6 and b7 and 3.9.b9 have no sub-items and are recorded.
- 3.14 (graduate attributes, 8 items) has a plain-present lead-in ("These acquired attributes include"); recorded as outcome items with force describes, since they state what graduates acquire (3.13, "will recognise", is recorded on its own). For P3 with open point 5.
- Skeleton corrections: rung counts (excellent 7 for the 1.9 list) wrong: 1.9 is a list of career paths, not a rung list or a statement; the tables were not cut at all (all inside 4.5); 3.4 stem span runs to the end of the clinical lists; component spans for 1.12, 1.15, 1.19, 1.22, 1.25, 2.8, 2.12, 2.15, 2.19, 3.1, 3.5, 3.6, 3.9, 3.11, 3.14, 3.18 carry the next sub-heading at their end. Paragraph statements are cut by `find` to the obliging or outcome sentences.
- Plain-present or descriptive paragraphs not recorded (open point 5): 1.3 (top-up route; "will advise" of the body), 1.5 to 1.11, 1.13, 1.23, 1.24, 1.26 to 1.29, 1.31, 2.2, 2.3, 2.5, 2.12 ("will usually be offered"), 2.13, 2.18, 2.20, 2.22 ("A review ensures"), 2.25, 2.26, 2.28 ("will hold accreditation"), 3.1 (content "generally includes"), 3.5, 3.7, 3.10, 3.12 (approaches "likely to be common"), 3.15, 3.17, 3.18, 3.21 to 3.23, 4.1, 4.3 to 4.5 (4.5's own sentence).
- Statutory duties on practitioners, not course or student standards, recorded in SB5 not S4: 1.14 ("required by statute to register"), 3.8 (dietitians "must undertake statutory registration").
- Obliging words beyond the five: 1.16 "expects" (force describes); 2.15 "need to" (recorded with the paragraph's should); 2.16 "are expected to" (recorded with its should); 3.4 "are required" (recorded as must); 3.2 "are required" with "must"; 3.10 and 3.5 "are encouraged" and 3.3 "are encouraged" (not force); 3.16 "there is an expectation that ... should"; 3.23 "requiring", "considered crucial" (not recorded); 2.11 "require" (institutional regulations; recorded with the paragraph's will).
- 2.9 mixes a provider should (course design) with learner wills (progression to graduate competence): one record, addressee both, force should. 2.19 is addressed to students ("should expect") and to courses: addressee both.
- Levels: honours and integrated master's levels are stated in 2.3 (FHEQ 6, FQHEIS 10; FHEQ 7, FQHEIS 11) and checked against std:doc:qaa-fheq-2024-framework (Table 1; 4.17 shared with FQHEIS 11). Outcome-list items and attributes take fheq:6 from the honours award (3.4's "honours" route; inferred for 3.6 to 3.14). No CQFW name appears (the front matter names the Quality Assessment Framework for Wales, not the CQFW).
- Subject codes: the statement states none; all six (CAH02-05-03; HECoS 100265, 100260, 100250, 100247, 100262) are basis inferred. Biomedical Science and Biomedical Sciences both map to 100265 (its non-preferred term is biomedical science); Healthcare Science (100260) as the alternative title in 2.6, 3.2 and 3.4. For P3.
- The agent instructions read threshold cells against the Annex D third-class description and excellent cells against the first-class description, by the Annex D row nearest in content; this pairing is ours and inferred: the statement maps no cell to a class. Professional rows have one Annex D cell (3rd-1st).
- Bodies named in content but not as PSRBs: UKAS and ISO standards (3.4.b47, laboratory accreditation); NHS, Blood Transfusion Services and Public Health Wales (1.8) as employers. The advisory group lists further bodies only in the excluded back matter; not recorded as cited.
- Shared documents not yet ingested: Characteristics Statement for Higher Education in Apprenticeships (2.6); the 2019 fourth edition (supersedes); the Quality Code Advice and Guidance and QAA Glossary (front matter); the HEA employability framework (references only).
- Text faults noted, not acted on: extraction splits words ("successf ully", "saf e", "staf f", "f acts"); "an honour's degree" in the Table 1 lead-in and 2.2; "fungi protozoa" (3.4, medical microbiology); "agonism, antagonism specificity" (3.6.b3).
- S9 commentary not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:39: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0089 (P1); built by tools/bm_build.py.
