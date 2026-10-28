---
id: std:doc:qaa-masters-degrees-in-business-and-management-2023-benchmarks
title: "Subject Benchmark Statement Master's Degrees in Business and Management"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100078", label: "business and management", basis: "stated" }
  - { scheme: "cah", code: "CAH17-01-01", label: "business and management (non-specific)", basis: "stated" }
  - { scheme: "cah", code: "CAH17-01", label: "business and management", basis: "stated" }
  - { scheme: "cah", code: "CAH17", label: "business and management", basis: "stated" }
  - { scheme: "hecos", code: "100089", label: "management studies", basis: "inferred" }
  - { scheme: "hecos", code: "100079", label: "business studies", basis: "inferred" }
  - { scheme: "hecos", code: "100088", label: "leadership", basis: "inferred" }
  - { scheme: "hecos", code: "100090", label: "public administration", basis: "inferred" }
edition: "March 2023 (fourth edition)"
published: 2023-03
status: current
supersedes: "the previous Subject Benchmark Statement for this subject (D1, front matter: 'Key changes from the previous'); its edition is not named in the text (the membership lists name review groups of 2015, 2007 and 2000)"
heldText: { method: sha256-bytes, raw: 7be2e11f74450418fbfd682e923df45e06b4528ec2b7205fc26a6eda34122777, normalised: 148245997f660f8f7409fc1f7606ec7e451f51427abee0ffa5b395f5c7fb2313 }
heldTextStan: { method: sha256-stan, raw: 7be2e11f74450418fbfd682e923df45e06b4528ec2b7205fc26a6eda34122777, normalised: af5abda3b4ec9d269ebe3d2e243dcef16ba38d7d5f3a1d4db8aea3413abfc7d1 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, the 2022 onward revision with cross-cutting themes (recall, to check)"
awardsCovered: ["master's"]
levelsCovered: ["fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document; terms it defines in passing (1.9 to 1.12) and its course typology (1.20 to 1.30)"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0119 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:01"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Master's Degrees in Business and Management (QAA, March 2023)

> Run 0119, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2023-masters-degrees-business-management-subject-benchmark-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for taught master's study in business and management at FHEQ level 7 (SCQF level 11): what a holder of the award should know, understand and be able to do, set out as one list of minimum threshold standards, with the subject's content areas, skills and a four-type typology of courses (generalist or specialist, for career entry or career development).

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2023 for the sector, this statement covers every kind of taught master's in business and management, from MSc and MA to MBA, MPA and MRes, and related level 7 awards such as postgraduate certificates and diplomas. It sorts courses into four types, describes their purposes and characteristics, sets out distinctive features of design, progression, flexibility, partnership and review, and lists content areas, subject skills and generic skills. Its standards are a single threshold list in 4.4 (twelve items under knowledge and understanding, skills, critical perspective, application and values); it states no typical or excellent rung and does not cite the degree classification descriptions (Annex D). It treats four cross-cutting themes (equality, diversity and inclusion; accessibility; education for sustainable development; enterprise and entrepreneurship education, joined to employability) and names professional and accrediting bodies such as CMI, CIPD, the Chartered Institute of Marketing and the public administration accreditors.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Master's Degrees in Business and Management"
edition: "March 2023 (fourth edition)"
dates:
  published: 2023-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement; a key reference point in Wales and Scotland and part of the quality requirements in Northern Ireland, not a sector-recognised standard in England (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2023", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "taught master's courses in business and management, generalist and specialist, and other provision at FHEQ level 7 and SCQF level 11 (postgraduate certificates and diplomas; the level 7 part of integrated master's)"
appliesTo:
  awards: ["master's", "postgraduate diploma", "postgraduate certificate", "integrated master's (level 7 components)"]
  levels: ["fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This Subject Benchmark Statement covers all types of master's degrees in Business and Management, including both specialist and generalist degrees for a range of participants, from new graduates to those with considerable work experience.\" (D1, 1.1)"
statedSubjects:
  - { name: "Business and Management", locator: "(D1, 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100078", label: "business and management" }, { scheme: "cah", code: "CAH17-01-01", label: "business and management (non-specific)" }] }
  - { name: "Master of Business Administration (MBA)", locator: "(D1, 1.4; 1.24)", kind: "programme title", codes: [{ scheme: "hecos", code: "100078", label: "business and management" }] }
  - { name: "Master of Public Administration (MPA)", locator: "(D1, 1.25)", kind: "programme title", codes: [{ scheme: "hecos", code: "100090", label: "public administration" }] }
  - { name: "specialist master's (for example marketing, project management, strategic retailing)", locator: "(D1, 1.4; 1.27)", kind: "specialism", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Introduction", gloss: "covers every kind of taught master's in the subject; a typology guides, it does not fix categories" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Introduction", gloss: "intended users; level 7 and SCQF 11; no national curriculum; joint subjects left to providers" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Introduction", gloss: "courses differ by content and by career stage; Table 1 typology" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Introduction", gloss: "typical award titles; the title alone does not fix the type" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Introduction", gloss: "research-based and taught master's; the MRes" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Introduction", gloss: "also relevant to postgraduate certificates, diplomas and integrated master's" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Introduction", gloss: "documents the statement was written to relate to" }
  - { number: "1.8", order: 10, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Purposes", gloss: "purposes a course may serve, one or more" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Purposes", gloss: "what organisations and business are taken to include" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Purposes", gloss: "what responsible leadership is taken to include" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Purposes", gloss: "what career preparation and development is taken to mean" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Purposes", gloss: "what skills and attributes are taken to include" }
  - { number: "1.13", order: 15, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Purposes", gloss: "purposes by course type, 1 to 4" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Purposes", gloss: "general courses are expected to cover the purposes; balance varies by type" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "diversity of content, disciplines and perspectives" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "theory together with practice" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "the capstone project and methods training" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "a changing discipline shapes course design" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "the three new theme sections apply throughout" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "characteristics follow the course type" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "Type 1: generalist, career entry" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "Type 1 with some specialisation; methods of linking theory to practice" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "Type 1 combined with other subjects" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "Type 2: generalist, post-experience, such as the MBA" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "the MPA and its accreditors" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "MBA and MPA largely generalist; sectoral MBAs allowed" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "Type 3: specialist, career entry" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "Type 3 entry, content and links to professional bodies" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "Type 4: specialist, post-experience" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of taught master's courses: Characteristics", gloss: "Type 4 entry and emphasis on practice" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "what EDI covers; embedded in the subject's culture" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "principles for an inclusive learning community" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "why the subject is taught: EDI and the SDGs" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "what is taught: EDI in content and perspectives" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "how the subject is taught: inclusive design and modes" }
  - { number: "1.36", order: 38, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "examples of ways to consider EDI" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI as continuing review with students" }
  - { number: "1.38", order: 40, componentType: stem, parent: "section 1", heading: "Accessibility", gloss: "what accessibility covers and its minimum" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "designing out barriers in advance" }
  - { number: "1.40", order: 42, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "equal access to work-based, international and digital learning" }
  - { number: "1.41", order: 43, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development", gloss: "sustainability, the SDGs and PRME in the subject" }
  - { number: "1.42", order: 44, componentType: stem, parent: "section 1", heading: "Education for Sustainable Development", gloss: "sustainable management in the curriculum; example topics" }
  - { number: "1.43", order: 45, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development", gloss: "ethics, responsibility and sustainability, dedicated and embedded" }
  - { number: "1.44", order: 46, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development", gloss: "core skills that match the ESD guidance outcomes" }
  - { number: "1.45", order: 47, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "what EED does for students' careers" }
  - { number: "1.46", order: 48, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "entrepreneurial capacity and theory in courses" }
  - { number: "1.47", order: 49, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "theory and practice of enterprise across sectors" }
  - { number: "1.48", order: 50, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "experiential learning for venture and portfolio careers" }
  - { number: "1.49", order: 51, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "EED beyond employment" }
  - { number: "2.1", order: 53, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "design reflects interdisciplinarity and course type" }
  - { number: "2.2", order: 54, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "interdisciplinary, specialist or generalist, pre- or post-experience" }
  - { number: "2.3", order: 55, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "knowledge joined to skills for responsible work" }
  - { number: "2.4", order: 56, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "employability and professional, responsible behaviour" }
  - { number: "2.5", order: 57, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "responsible management practice designed in" }
  - { number: "2.6", order: 58, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "all kinds of organisation covered" }
  - { number: "2.7", order: 59, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "readiness for changing working life" }
  - { number: "2.8", order: 60, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "a full master's: one year, usually 180 credits" }
  - { number: "2.9", order: 61, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "postgraduate certificates and diplomas as stages or exits" }
  - { number: "2.10", order: 62, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's: length and level 7 study" }
  - { number: "2.11", order: 63, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "advanced standing with professional bodies; microcredits" }
  - { number: "2.12", order: 64, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "a route to research degrees" }
  - { number: "2.13", order: 65, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible approaches and inclusive design" }
  - { number: "2.14", order: 66, componentType: stem, parent: "section 2", heading: "Flexibility", gloss: "kinds of flexibility there may need to be" }
  - { number: "2.15", order: 67, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexibility kept coherent" }
  - { number: "2.16", order: 68, componentType: stem, parent: "section 2", heading: "Partnership", gloss: "partnerships with organisations" }
  - { number: "2.17", order: 69, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "recognition by professional bodies" }
  - { number: "2.18", order: 70, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "networks, bodies and learned societies" }
  - { number: "2.19", order: 71, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review with students" }
  - { number: "2.20", order: 72, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.21", order: 73, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "the external examining system" }
  - { number: "2.22", order: 74, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "advisory boards and employer panels" }
  - { number: "2.23", order: 75, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation of vocational courses" }
  - { number: "3.1", order: 77, componentType: paragraph, parent: "section 3", heading: "Content: Knowledge and understanding", gloss: "generalist and specialist scope; consistency with the level 7 descriptor" }
  - { number: "3.2", order: 78, componentType: paragraph, parent: "section 3", heading: "Content: Knowledge and understanding", gloss: "knowledge of organisations, context and management" }
  - { number: "3.3", order: 79, componentType: paragraph, parent: "section 3", heading: "Content: Knowledge and understanding", gloss: "integrating the three areas" }
  - { number: "3.4", order: 80, componentType: area, parent: "section 3", heading: "Content: Knowledge and understanding", gloss: "area: the business environment" }
  - { number: "3.5", order: 81, componentType: area, parent: "section 3", heading: "Content: Knowledge and understanding", gloss: "area: organisations" }
  - { number: "3.6", order: 82, componentType: area, parent: "section 3", heading: "Content: Knowledge and understanding", gloss: "area: responsible leadership and management" }
  - { number: "3.7", order: 83, componentType: paragraph, parent: "section 3", heading: "Content: Knowledge and understanding", gloss: "learning outcomes define knowledge and skills by type" }
  - { number: "3.8", order: 84, componentType: paragraph, parent: "section 3", heading: "Content: Knowledge and understanding", gloss: "broad knowledge, change and integrative links" }
  - { number: "3.9", order: 85, componentType: paragraph, parent: "section 3", heading: "Content: Knowledge and understanding", gloss: "knowledge differs by course type" }
  - { number: "3.10", order: 86, componentType: area, parent: "section 3", heading: "Content: Knowledge and understanding", gloss: "areas for generalist courses (Types 1 and 2)" }
  - { number: "3.11", order: 87, componentType: area, parent: "section 3", heading: "Content: Knowledge and understanding", gloss: "added knowledge for specialist courses (Types 3 and 4)" }
  - { number: "3.12", order: 88, componentType: paragraph, parent: "section 3", heading: "Content: Knowledge and understanding", gloss: "Types 2 and 4 ground learning in experience" }
  - { number: "3.13", order: 89, componentType: paragraph, parent: "section 3", heading: "Skills and practice", gloss: "skills tied closely to practice and employability" }
  - { number: "3.14", order: 90, componentType: paragraph, parent: "section 3", heading: "Skills and practice", gloss: "cognitive, subject, personal and team skills" }
  - { number: "3.15", order: 91, componentType: stem, parent: "section 3", heading: "Skills and practice", gloss: "skills particular to the subject" }
  - { number: "3.16", order: 92, componentType: stem, parent: "section 3", heading: "Skills and practice", gloss: "other generic skills and attributes" }
  - { number: "3.17", order: 93, componentType: paragraph, parent: "section 3", heading: "Skills and practice", gloss: "skills vary by type; reflection on experience" }
  - { number: "3.18", order: 94, componentType: practice, parent: "section 3", heading: "Learning and teaching", gloss: "diverse teaching and learning methods" }
  - { number: "3.19", order: 95, componentType: practice, parent: "section 3", heading: "Learning and teaching", gloss: "theory and practice joined through practitioners" }
  - { number: "3.20", order: 96, componentType: practice, parent: "section 3", heading: "Learning and teaching", gloss: "inclusive, engaging methods; typical activities" }
  - { number: "3.21", order: 97, componentType: practice, parent: "section 3", heading: "Learning and teaching", gloss: "teaching adapted to course type" }
  - { number: "3.22", order: 98, componentType: practice, parent: "section 3", heading: "Learning and teaching", gloss: "skills development embedded and assessed" }
  - { number: "3.23", order: 99, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment for learning; timely feedback" }
  - { number: "3.24", order: 100, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "inclusive assessment design" }
  - { number: "3.25", order: 101, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "reliable, varied assessment methods" }
  - { number: "3.26", order: 102, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "where and how assessment takes place" }
  - { number: "3.27", order: 103, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "authentic assessment" }
  - { number: "3.28", order: 104, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment design by learning outcomes and type" }
  - { number: "3.29", order: 105, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "group work and its marking" }
  - { number: "3.30", order: 106, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "peer review and peer assessment" }
  - { number: "3.31", order: 107, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "transparent assessment and co-design" }
  - { number: "3.32", order: 108, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "student workload in assessment design" }
  - { number: "4.1", order: 110, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the list sets the minimum threshold for the award" }
  - { number: "4.2", order: 111, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "achievement above the threshold; the level 7 descriptor" }
  - { number: "4.3", order: 112, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "five factors that mark master's achievement" }
  - { number: "4.4", order: 113, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "the threshold standards, under five headings" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a master's degree in Business and Management", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a master's in Business and Management", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1 and S2" }
  - { number: "none", heading: "section heading lines (sections 1 to 4)", kind: "other: headings, recorded as sections in S3" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for SB6 and Part E" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for Master's Degrees in Business and Management", kind: "other: membership lists" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 79 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/masters-degrees-in-business-and-management-2023/1.14
  locator: { number: "1.14", headingPath: ["Context and purposes of a master's degree in Business and Management", "Purposes and characteristics of taught master's courses: Purposes"] }
  span: { start: 18833, end: 19442 }
  source: "1.14 While there is an expectation that all general Business and Management master's courses should cover the purposes as outlined in paragraph 1.8, the actual balance will vary among higher education providers depending on the type of course (see paragraph 1.3) and any requirements for recognition by relevant professional bodies. This will be explicable and demonstrable in terms of the intended learning outcomes of each course. It is the responsibility of individual providers to decide which of their particular course specifications are appropriate to this Subject Benchmark Statement. Characteristics\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "general business and management master's courses"
  addressee: provider
  verbs: ["cover"]
  about: "covering the purposes of a master's"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "General master's courses in the subject should cover the purposes listed in 1.8, though the balance will vary with the course type and any professional recognition sought, and the intended learning outcomes will show it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/1.21
  locator: { number: "1.21", headingPath: ["Context and purposes of a master's degree in Business and Management", "Purposes and characteristics of taught master's courses: Characteristics"] }
  span: { start: 21356, end: 22165 }
  source: "1.21 Generalist master's courses provide a broad foundation on which students will be prepared for a range of future careers and roles in a wide range of organisations. This type of master's course is usually chosen by students who have a bachelor's degree in a non- related subject with little or no experience in business and management. The courses are designed to develop master's level knowledge and skills in business and management subjects to enhance the utility and employability of the first discipline. The courses aim to prepare individuals for employment that may well be related to their first degree discipline. Postgraduate students will develop a sound understanding of business/organisational contexts and thus should be able to make an early and significant contribution to their employer.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "students on Type 1 generalist career-entry courses"
  addressee: learner
  verbs: ["develop", "make"]
  about: "understanding of business contexts for early contribution"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Type 1 courses suit graduates of other subjects with little business experience; their postgraduates will develop a sound grasp of business and organisational contexts and so should be able to contribute early and significantly to an employer."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of a master's degree in Business and Management", "Purposes and characteristics of taught master's courses: Characteristics"] }
  span: { start: 23043, end: 23923 }
  source: "1.24 These courses are defined as generalist courses that enhance the career development of those who have significant postgraduation and/or relevant work experience on which the learning process should build. Normally, the experience required will be at least two years with the typical entrant having substantially more than this (note that pre- experience courses typically do not use the MBA title but prefer to use one such as MSc Business and Management). These courses are distinguished by an emphasis on leadership and strategic management. They are characterised by reflective learning based on prior experience and by peer-to-peer shared experiences. Due to the expectation of prior work experience of the students, MBA courses are expected to be different in their objectives, recruitment and pedagogical processes to other master's degrees in Business and Management.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Type 2 generalist post-experience courses, including the MBA"
  addressee: provider
  verbs: ["build"]
  about: "building on prior work experience"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Type 2 generalist courses serve people with substantial work experience, usually at least two years, and learning should build on it; they stress leadership and strategy and use reflective and peer learning, and MBAs differ from other master's in aims, recruitment and teaching."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/1.28
  locator: { number: "1.28", headingPath: ["Context and purposes of a master's degree in Business and Management", "Purposes and characteristics of taught master's courses: Characteristics"] }
  span: { start: 25673, end: 26303 }
  source: "1.28 Entry requirements often, but not always, require a previous degree that is relevant or cognate to the specialism. The courses do not usually require previous work experience and are designed for career entrants. They offer in-depth study in a particular specialist area and often include ancillary subjects relevant to the specialism. The content of the programme usually has a strong theoretical base, but it should also provide a range of skills relevant to practice and some Type 3 courses are linked to professional body qualifications and membership. Type 4: Specialist master's (career development or post-experience)\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Type 3 specialist career-entry courses"
  addressee: provider
  verbs: ["provide"]
  about: "practice-relevant skills in specialist courses"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Type 3 specialist courses usually rest on strong theory but should also give a range of skills relevant to practice; they seldom need work experience, and some link to professional body qualifications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/1.31
  locator: { number: "1.31", headingPath: ["Context and purposes of a master's degree in Business and Management", "Equality, diversity and inclusion"] }
  span: { start: 27352, end: 27915 }
  source: "1.31 Equality, diversity and inclusion (EDI) encompass a wide range of identity characteristics, including, but not limited to, race/ethnicity, gender, sexual orientation, religion and belief, disability, age, and socio-economic background. It is recognised that there are many forms of difference and that these are, in part, reflected in legal equality duties but go beyond that to recognise intersectionalities across the student and staff population. EDI should be a meaningful concept that is embedded within the culture and practice of the subject area.\n\n9\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the subject area and its courses"
  addressee: provider
  verbs: ["embedded"]
  about: "EDI embedded in the subject"
  themes: [theme:edi]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Equality, diversity and inclusion reach across many identity characteristics and beyond legal duties to intersections in the student and staff body, and the subject area should make EDI a real concept built into its culture and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/1.33
  locator: { number: "1.33", headingPath: ["Context and purposes of a master's degree in Business and Management", "Equality, diversity and inclusion"] }
  span: { start: 28442, end: 29305 }
  source: "1.33 Why the subject is taught: Through a focus on equality, diversity and inclusion, Business and Management education can support the progress of organisations (including private, public and third sector) in addressing inequality and disadvantage as captured by the UN Sustainable Development Goals , such as decent work and economic growth, gender equality and reduced inequalities. Instilling in students the principles of equality, diversity and inclusion, along with an appreciation of the importance of continued reflective practice, equips students to flourish in an increasingly diverse and global world, and to foster an inclusive approach in their future contributions to organisations and society. The study of Business and Management will embed the principles of equality, diversity and inclusion in future managers and leaders (see paragraph 1.10).\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "students of the subject, as future managers and leaders"
  addressee: learner
  verbs: ["embed"]
  about: "EDI principles carried into management and leadership"
  themes: [theme:edi]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Business and management education can help organisations tackle inequality, in line with the UN SDGs, and studying the subject will build the principles of equality, diversity and inclusion into future managers and leaders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/1.34
  locator: { number: "1.34", headingPath: ["Context and purposes of a master's degree in Business and Management", "Equality, diversity and inclusion"] }
  span: { start: 29305, end: 30692 }
  source: "1.34 What is taught: Master's courses in Business and Management ensure that students gain a critical understanding of the role that organisations, and the leaders within them, play in promoting EDI. Business and Management postgraduates should not only be aware of the legal requirement to protect people from discrimination, but also equipped with the knowledge and skills needed to foster inclusive workplaces to meet the economic, social and environmental objectives of organisations and wider stakeholders. Courses can ensure that students have an appreciation of the role of business and management in addressing the global challenges. As part of a commitment to EDI, courses should also ensure that the content covered is diverse and offers a critical examination of dominant approaches to the discipline, raising awareness of the ways in which they can perpetuate exclusion and exploring alternatives to such approaches. In doing so, it is important that a wide and diverse range of perspectives is recognised and drawn upon, such as from the Global South, marginalised communities and local/regional/national issues. Using examples and cases that are representative of both the diversity of the student cohort and society more widely not only enriches the educational provision for all students, but also helps foster greater engagement and a sense of belonging among students.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "postgraduates and the courses they take"
  addressee: both
  verbs: ["gain", "foster", "ensure"]
  about: "EDI in what is taught"
  themes: [theme:edi]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Courses make sure students understand critically how organisations and leaders promote EDI; postgraduates should know the legal duty not to discriminate and be equipped to build inclusive workplaces, and content should be diverse and critical of dominant approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/1.35
  locator: { number: "1.35", headingPath: ["Context and purposes of a master's degree in Business and Management", "Equality, diversity and inclusion"] }
  span: { start: 30692, end: 31967 }
  source: "1.35 How the subject is taught: Master's courses in Business and Management should be designed to enable students from all backgrounds to realise their potential and for all students regardless of their race/ethnicity, religion, gender, sexual orientation, disability or social background to feel represented and included. It is also important that how the subject is taught and assessed is reflective of inclusive principles and that issues such as the mode of learning (for example, in-person, digital, blended, hybrid, hyflex, experiential, block release, full/part-t ime; synchronous/asynchronous) are considered carefully as all pose different opportunities and challenges. The mode of learning and course structure can help make education more accessible and inclusive (see also paragraph 1.38-1.40). Similarly, the assessment design can provide opportunities for different types of students to succeed. How the subject is taught should reflect an awareness of EDI in terms of different pedagogical approaches, and the learning approaches adopted can enable the diversity of the cohort to enrich the experience for all students. Approaches to teaching and learning should also include the ethical consideration of each person's multiple identities and experiences.\n\n10\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the design of courses and teaching"
  addressee: provider
  verbs: ["designed", "realise"]
  about: "inclusive design of teaching and assessment"
  themes: [theme:edi]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Courses should be designed so students from every background can reach their potential and feel represented; teaching, assessment and modes of learning should reflect inclusive principles and pedagogy aware of EDI."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/1.37
  locator: { number: "1.37", headingPath: ["Context and purposes of a master's degree in Business and Management", "Equality, diversity and inclusion"] }
  span: { start: 33763, end: 34227 }
  source: "1.37 Consideration of EDI within courses is not a one-off activity. Course teams should regularly reflect upon how EDI can be further enhanced and where possible, work in partnership with students in doing so. Equality and diversity form the basis for disciplinary practice and inclusivity is an ongoing process of quality review and enhancement. The process to approve changes to courses can consider completing a formal equality impact assessment. Accessibility\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course teams"
  addressee: provider
  verbs: ["reflect", "work"]
  about: "continuing review of EDI with students"
  themes: [theme:edi]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "EDI is continuing work: course teams should reflect regularly on how to strengthen it and, where they can, do so with students; approval of changes may include an equality impact assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/1.38
  locator: { number: "1.38", headingPath: ["Context and purposes of a master's degree in Business and Management", "Accessibility"] }
  span: { start: 34227, end: 35093 }
  source: "1.38 Accessibility considers whether all aspects of the course can be understood by all, however they are encountered. Accessibility should, as a minimum, meet regulatory requirements but should also apply to all stages of the course, from providing pre-application information through to graduation and beyond. It may include, but is not limited to:\n• taking actions to ensure that all aspects of the course curriculum are accessible to all students\n• ensuring that all students have access to appropriate and safe learning spaces and resources that support their learning\n• confirming that a wide range of assessments are available and that reasonable adjustments to assessments are put in place to ensure that all students are given the opportunity to succeed\n\n11\n• remaining mindful of obstacles and barriers such as digital poverty and caring responsibilities.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses, from pre-application to after graduation"
  addressee: provider
  verbs: ["meet", "apply"]
  about: "accessibility from application to graduation"
  themes: [theme:accessibility]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Accessibility asks whether everyone can understand every part of a course however they meet it; it should at least satisfy regulatory requirements and should run from pre-application information to graduation and beyond, with examples given."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/1.39
  locator: { number: "1.39", headingPath: ["Context and purposes of a master's degree in Business and Management", "Accessibility"] }
  span: { start: 35093, end: 35334 }
  source: "1.39 Proactive approaches should be taken in the design of courses, modules, teaching practices and assessments in order to build in inclusivity and avoid creating barriers for students with specific learning difficulties or neurodiversity.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the design of courses, modules, teaching and assessment"
  addressee: provider
  verbs: ["build", "avoid"]
  about: "designing out barriers"
  themes: [theme:accessibility]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Courses, modules, teaching and assessment should be designed proactively to build in inclusivity and keep obstacles away from neurodivergent students and those with specific learning difficulties."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/1.40
  locator: { number: "1.40", headingPath: ["Context and purposes of a master's degree in Business and Management", "Accessibility"] }
  span: { start: 35334, end: 35591 }
  source: "1.40 Accessibility should include enabling the same opportunities for workplace and international learning for all students as well as providing all students with inclusive digital accessibility without discrimination. Education for Sustainable Development\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses and their learning opportunities"
  addressee: provider
  verbs: ["include", "enabling", "providing"]
  about: "equal access to work, international and digital learning"
  themes: [theme:accessibility]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Accessibility should cover giving every student the same chances of workplace and international learning and digital access that is inclusive and free of discrimination."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/1.42
  locator: { number: "1.42", headingPath: ["Context and purposes of a master's degree in Business and Management", "Education for Sustainable Development"] }
  span: { start: 36531, end: 38070 }
  source: "1.42 Sustainable management is a requirement for planetary survival. Organisations will play a key role in meeting targets set to halve global emissions by 2030 (IPCC , 2022). It is therefore imperative that future business leaders are equipped to engage meaningfully with and respond to climate challenges in order to embed climate solutions in all business functions and processes. This entails skills in boundary-spanning, cross-sectional leadership and partnerships with organisations and communities. While living conditions on the planet are important for survival, sustainable management also addresses wider sustainable development issues as captured in the UN Sustainable Development Goals. Management for economic, social and environmental sustainability needs to be integrated systematically within the Business and Management curriculum and across functional areas. The following examples are topics that are typically incorporated in Business and Management courses, but the list is by no means exhaustive:\n• sustainable supply chain management (including reducing waste, working conditions and effective distribution of resources)\n• carbon literacy and greenhouse gas management\n• sustainable digital technologies (including big data and GDPR)\n• accounting, financial management and integrated reporting\n• communications, including marketing and reporting\n• business ethics, public value and responsible leadership (see paragraph 1.10)\n• human resource management and development practices (for example, working conditions).\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "requirement" read as must
  level: none
  appliesTo: "the business and management curriculum"
  addressee: provider
  verbs: ["integrated", "equipped"]
  about: "sustainable management across the curriculum"
  themes: [theme:esd]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Organisations matter for meeting emissions targets, so future leaders need to be ready to respond to climate challenges; management for economic, social and environmental sustainability is to be built systematically into the curriculum and its functional areas, with example topics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/2.13
  locator: { number: "2.13", headingPath: ["Distinctive features of a master's in Business and Management", "Flexibility"] }
  span: { start: 45627, end: 46143 }
  source: "2.13 Flexible educational approaches enable students to adapt their education to their situational and contextual needs and individual constraints (Brennan, 2021 ). Such approaches may also play a key role in increasing access into higher education and thus social mobility. Courses should be designed with inclusivity in mind and may be offered in a variety of learning modes and assessment to suit students' learning and other needs. See also paragraphs 1.31-1.37 on EDI and paragraphs 1.38-1.40 on Accessibility.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the design of courses"
  addressee: provider
  verbs: ["designed", "offered"]
  about: "flexible, inclusive design"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Flexible approaches let students fit study to their circumstances and may widen access; courses should be designed for inclusivity and may offer varied learning modes and assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of a master's in Business and Management", "Monitoring and review"] }
  span: { start: 49400, end: 50174 }
  source: "2.19 Degree-awarding bodies and their collaborative partnerships routinely collect and analyse information and undertake periodic course review according to their own needs and students should form part of this monitoring and review process. They draw on a range of external reference points, including this Statement, to ensure that their provision aligns with sector norms. Monitoring and evaluation are a periodic assessment of a course, conducted internally or by external independent evaluators. Evaluation uses information from both current and historic monitoring to develop an understanding of student achievement or inform future course planning. It can also include regular monitoring and review of equality, diversity and inclusion within the learning community.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "degree-awarding bodies and their partners"
  addressee: provider
  verbs: ["collect", "analyse", "form"]
  about: "students in monitoring and review"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Awarding bodies and partners gather and analyse information and review courses periodically against external reference points, and students should take part in that monitoring and review, which can also cover EDI."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/2.20
  locator: { number: "2.20", headingPath: ["Distinctive features of a master's in Business and Management", "Monitoring and review"] }
  span: { start: 50174, end: 50486 }
  source: "2.20 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
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
  award: ["master's"]
  gradeOf: none
  paraphrase: "Externality is essential to UK quality assurance: providers will use external reviewers in periodic review to bring an outside view and to confirm that threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.1
  locator: { number: "3.1", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 52122, end: 52726 }
  source: "3.1 There is an expectation that generalist degree courses covered by this Subject Benchmark Statement will provide a broad, analytical and integrated study of business and management, covering a complex range of organisations and their interdependencies. The specialist courses will be expected to set the specialism within the context of the broader field of business and management. This Subject Benchmark Statement is consistent with the descriptors for Level 7 on the FHEQ and Level 11 on the FQHEIS, Section 4.17 of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies .\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "generalist and specialist courses"
  addressee: provider
  verbs: ["provide", "set"]
  about: "scope of generalist and specialist courses"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Generalist courses are expected to give a broad, analytical and joined-up study of business and management across complex organisations; specialist courses will place the specialism in the wider field; the statement matches the FHEQ level 7 and SCQF level 11 descriptors."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.2
  locator: { number: "3.2", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 52726, end: 53244 }
  source: "3.2 Graduates of taught master's courses will therefore be able to demonstrate relevant knowledge and understanding of organisations, the wider business context (including environmental and regulatory) in which they operate and their management. Courses emphasise understanding, responding to and shaping the dynamic and changing nature of business, and the consideration of the future of organisations within the global sustainable business environment, including the management of risk, and their impact on society.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of taught master's courses"
  addressee: learner
  verbs: ["demonstrate"]
  about: "knowledge of organisations, context and management"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates will be able to show what they know and understand about organisations, their wider business setting including its environmental and regulatory sides, and how organisations are managed; courses stress change, the future of organisations, risk and impact on society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 53244, end: 53506 }
  source: "3.3 The interrelationships among, and the integration between, the areas in paragraph\n3.2 are very important within the overall student learning experience and will be demonstrated in the capabilities of successful master's graduates from all modes of learning.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "successful master's graduates"
  addressee: learner
  verbs: ["demonstrated"]
  about: "integrating the areas of knowledge"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "How the areas named in 3.2 relate and fit together matters greatly, and successful graduates from every mode of study will show it in what they can do."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.7
  locator: { number: "3.7", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 54910, end: 55087 }
  source: "3.7 Subject knowledge, understanding and skills will be defined in learning outcomes and may also vary according to the type of master's degree (see typology in paragraph 1.3).\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses and their learning outcomes"
  addressee: provider
  verbs: ["defined", "vary"]
  about: "knowledge and skills set in learning outcomes"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Each course's learning outcomes will set out its subject knowledge, understanding and skills, which may differ with the type of master's."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.8
  locator: { number: "3.8", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 55087, end: 55630 }
  source: "3.8 Within the framework of the business environment, organisations and responsible leadership and management (set out in paragraphs 3.4-3 .6 above) master's graduates are typically able to demonstrate a broad knowledge and deep understanding of organisations, the external context in which they operate and how they are managed. They will understand and be able to respond to change. They will have intellectual breadth and be able to make integrative links across the various areas of organisations, even in specialist master's courses.\n\n18\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["demonstrate", "understand", "respond", "make"]
  about: "breadth, change and integrative links"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates are typically able to show broad knowledge and deep understanding of organisations, their external context and their management; they will understand change and respond to it, and will have the breadth to connect areas of an organisation, even on specialist courses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.10.b1
  locator: { number: "3.10.b1", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 56088, end: 56303 }
  source: "ethics, responsibility and sustainability: managing responsibly and behaving as ethical leaders, particularly in relation to social, cultural, legal, economic and environmental issues (see also paragraphs 1.41-1.44)"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of generalist courses (Types 1 and 2)"
  addressee: learner
  verbs: ["managing", "behaving"]
  about: "ethics, responsibility and sustainability"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will typically gain deep knowledge and critical understanding of ethics, responsibility and sustainability: managing responsibly and leading ethically on social, cultural, legal, economic and environmental questions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.10.b2
  locator: { number: "3.10.b2", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 56306, end: 56472 }
  source: "markets and economies: the development, access and operation of markets for resources, goods and services - this includes market failure, externalities and fair trade"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of generalist courses (Types 1 and 2)"
  addressee: learner
  verbs: []
  about: "markets and economies"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will typically gain deep knowledge and critical understanding of markets and economies: how markets for resources, goods and services form and work, including market failure, externalities and fair trade."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.10.b3
  locator: { number: "3.10.b3", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 56475, end: 56715 }
  source: "marketing, sales, negotiation and customers: management of customer relationships, consumer behaviour, different approaches for segmentation, targeting, positioning, generating sales and the need for innovation in product and service design"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of generalist courses (Types 1 and 2)"
  addressee: learner
  verbs: ["generating"]
  about: "marketing, sales, negotiation and customers"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will typically gain deep knowledge and critical understanding of marketing, sales, negotiation and customers: customer relationships, consumer behaviour, segmentation, targeting and positioning, sales and innovation in products and services."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.10.b4
  locator: { number: "3.10.b4", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 56718, end: 56908 }
  source: "finance and accounting: the sources, uses and management of finance and the use of accounting and other information systems for planning, control, decision-making and managing financial risk"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of generalist courses (Types 1 and 2)"
  addressee: learner
  verbs: ["managing"]
  about: "finance and accounting"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will typically gain deep knowledge and critical understanding of finance and accounting: where finance comes from and how it is used and managed, and how accounting and information systems serve planning, control, decisions and financial risk."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.10.b5
  locator: { number: "3.10.b5", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 56911, end: 57382 }
  source: "people and organisational behaviour: responsible, inclusive and ethical leadership (see paragraph 1.10), strategic management and development of people and organisations, including employee engagement and the implications of the legal context - this requires recognition of the design and development of organisations, grounded in an understanding of cross-cultural issues, equality, diversity and inclusion (see also paragraphs 1.31-1.37) and meeting future requirements"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of generalist courses (Types 1 and 2)"
  addressee: learner
  verbs: []
  about: "people and organisational behaviour"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will typically gain deep knowledge and critical understanding of people and organisational behaviour: responsible and inclusive leadership, strategic people management and development, engagement, the legal context, cross-cultural issues and EDI."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.10.b6
  locator: { number: "3.10.b6", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 57385, end: 57695 }
  source: "operations and business innovation: the management of resources, the supply chain, procurement, logistics, outsourcing, quality systems, development of service excellence and project management; tools and techniques for transforming (big) data into useful information for business analysis and decision support"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of generalist courses (Types 1 and 2)"
  addressee: learner
  verbs: ["transforming"]
  about: "operations and business innovation"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will typically gain deep knowledge and critical understanding of operations and business innovation: resources, supply chains, procurement, logistics, outsourcing, quality, service excellence and projects, and turning data into information for analysis and decisions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.10.b7
  locator: { number: "3.10.b7", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 57698, end: 58029 }
  source: "data analytics, statistics, digital business, information systems and business intelligence: the development of strategic priorities to deliver business at speed through the management, application and implementation of information systems and their impact upon organisations, and to enable data-driven and informed decision-making"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of generalist courses (Types 1 and 2)"
  addressee: learner
  verbs: ["deliver", "enable"]
  about: "data analytics, digital business and information systems"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will typically gain deep knowledge and critical understanding of analytics and statistics, digital business, information systems and business intelligence: setting digital priorities and using information systems to support decisions driven by data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.10.b8
  locator: { number: "3.10.b8", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 58032, end: 58352 }
  source: "business policy and strategy: the development of appropriate policies and strategies within a changing environment to meet stakeholder interests, and the use of risk and crisis management techniques, business continuity planning and communication techniques and tools to help maximise achievement of strategic objectives"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of generalist courses (Types 1 and 2)"
  addressee: learner
  verbs: ["maximise"]
  about: "business policy and strategy"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will typically gain deep knowledge and critical understanding of business policy and strategy: forming policies and strategies for a changing environment and stakeholders, with risk, crisis and continuity management and communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.10.b9
  locator: { number: "3.10.b9", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 58355, end: 58642 }
  source: "public and non-profit strategic management: the distinct roles and practices of public service organisations and the voluntary and community sector, including approaches to governance, financial management, public leadership, community empowerment, coproduction, public values and ethics"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of generalist courses (Types 1 and 2)"
  addressee: learner
  verbs: []
  about: "public and non-profit strategic management"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will typically gain deep knowledge and critical understanding of public and non-profit strategic management: how public services and the voluntary and community sector work, including governance, finance, leadership, co-production, public value and ethics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.10.b10
  locator: { number: "3.10.b10", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 58645, end: 58973 }
  source: "entrepreneurship and enterprise development: taking innovative business ideas to create or co-create new products, services or organisations that will generate a return on investment - this includes, but is not limited to, the identification of intellectual property and appreciation of its value (see also paragraphs 1.45-1.49)"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of generalist courses (Types 1 and 2)"
  addressee: learner
  verbs: ["taking", "create", "generate"]
  about: "entrepreneurship and enterprise development"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will typically gain deep knowledge and critical understanding of entrepreneurship and enterprise development: turning innovative ideas into new products, services or organisations that earn a return, including identifying and valuing intellectual property."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.10.b11
  locator: { number: "3.10.b11", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 58980, end: 59088 }
  source: "MPA courses will have a greater focus on content related to governance, public policy and public management."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "MPA courses"
  addressee: provider
  verbs: ["have"]
  about: "MPA content focus"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "MPA courses will give more weight to governance, public policy and public management content."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.11.b1
  locator: { number: "3.11.b1", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 59436, end: 59546 }
  source: "the specialist subject area, while placing that subject within a wider organisational and contextual framework"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of specialist courses (Types 3 and 4)"
  addressee: learner
  verbs: ["placing"]
  about: "the specialist subject in its wider setting"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will acquire knowledge of the specialist subject and set it within its wider organisational and contextual frame."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.11.b2
  locator: { number: "3.11.b2", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 59549, end: 59652 }
  source: "specific current issues and thinking, along with techniques applicable to research, in the subject area"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of specialist courses (Types 3 and 4)"
  addressee: learner
  verbs: []
  about: "current issues and research techniques in the specialism"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will acquire knowledge of current issues and thinking in the specialist area and of the research techniques used in it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.11.b3
  locator: { number: "3.11.b3", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 59655, end: 59831 }
  source: "both theoretical and applied perspectives enabling them to apply a range of specialist skills to the organisations (and their context) in which they as specialists may operate."
  stem: "3.11"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of specialist courses (Types 3 and 4)"
  addressee: learner
  verbs: ["apply"]
  about: "theory and application of specialist skills"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will acquire theoretical and applied perspectives that let them use specialist skills in the organisations and settings where they may work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.12
  locator: { number: "3.12", headingPath: ["Content, structure and delivery", "Content: Knowledge and understanding"] }
  span: { start: 59887, end: 60089 }
  source: "3.12 Students of Types 2 and 4 master's courses for career development will be able to ground their new knowledge and understanding within the base of their professional experience. Skills and practice\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "students of Types 2 and 4 career-development courses"
  addressee: learner
  verbs: ["ground"]
  about: "new knowledge grounded in professional experience"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "On career-development courses of Types 2 and 4, students will be able to root what they newly learn in their own professional experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.14
  locator: { number: "3.14", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 60269, end: 60666 }
  source: "3.14 Graduates of master's courses in Business and Management will be able to demonstrate a range of cognitive and intellectual skills together with competencies specific to business and management. They will have strongly developed personal, interpersonal and team working skills. They will have an additional range of skills beyond those general skills expected of undergraduate degree holders.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["demonstrate"]
  about: "cognitive, subject, personal and team skills"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates will be able to show cognitive and intellectual skills and business and management competencies, with well-developed personal, interpersonal and teamwork skills that go beyond those of a first degree."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.15.b1
  locator: { number: "3.15.b1", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 60758, end: 61034 }
  source: "People management: team building, resilience and well-being, leadership and motivating others; selecting the appropriate leadership style for different situations; nurturing equality, diversity and inclusion; performance management; setting objectives, coaching and mentoring."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["setting", "selecting", "nurturing", "motivating"]
  about: "people management"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to manage people: building teams, resilience and well-being, leading and motivating, choosing a fitting leadership style, fostering EDI, managing performance, setting objectives, coaching and mentoring."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.15.b2
  locator: { number: "3.15.b2", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 61037, end: 61738 }
  source: "Problem-solving and critical analysis: collecting relevant information relating to a current situation, analysing facts and circumstances to determine the cause of a problem, identifying and evaluating possible solutions; decision-making and selecting appropriate, sustainable solutions; being able to think critically and be creative; managing the creative processes in self and others; organising thoughts, analysing, synthesising and critically appraising; the capability to identify assumptions, evaluate statements in terms of evidence, detect false logic or reasoning, identify implicit values, define terms adequately and generalise appropriately; the ability to implement and review decisions."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["collecting", "analysing", "identifying", "evaluating"]
  about: "problem-solving and critical analysis"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to solve problems and analyse critically: gather information, find causes, weigh and choose sustainable solutions, think critically and creatively, test assumptions and logic, and carry out and review decisions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.15.b3
  locator: { number: "3.15.b3", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 61745, end: 62366 }
  source: "Research: the ability to conduct research and enquiry into business and management issues either individually or as part of a team through research design, the collection and analysis of qualitative and quantitative data, synthesis and reporting; analysing and evaluating a range of data, sources of information and appropriate methodologies, which includes the need for strong digital literacy, and to use that research for evidence-based, responsible and ethical decision-making; an ability to evaluate the rigour and validity of published research in business and management and assess its relevance to new situations."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["conduct", "analysing", "evaluating", "evaluate", "assess"]
  about: "research"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to research business and management issues alone or in teams: design, collect and analyse qualitative and quantitative data, synthesise and report, with strong digital literacy, and judge the rigour and relevance of published research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.15.b4
  locator: { number: "3.15.b4", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 62369, end: 62573 }
  source: "Commercial acumen: based on an awareness of the key drivers for business success, causes of failure and the importance of providing customer satisfaction and building customer loyalty in sustainable ways."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["providing", "building"]
  about: "commercial acumen"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have commercial acumen grounded in knowing what drives business success and failure and why sustainable customer satisfaction and loyalty matter."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.15.b5
  locator: { number: "3.15.b5", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 62576, end: 62799 }
  source: "Innovation, creativity and enterprise: the ability to act entrepreneurially to generate, develop and communicate ideas, manage and exploit intellectual property, gain support and deliver successful and sustainable outcomes."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["act", "generate", "develop", "communicate"]
  about: "innovation, creativity and enterprise"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to act entrepreneurially: produce, develop and communicate ideas, handle intellectual property, win support and achieve sustainable results."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.15.b6
  locator: { number: "3.15.b6", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 62802, end: 62935 }
  source: "Numeracy: the use of quantitative skills to manipulate data, evaluate, estimate and model business problems, functions and phenomena."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["manipulate", "evaluate", "estimate", "model"]
  about: "numeracy"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to use quantitative skills to work with data and to evaluate, estimate and model business problems and processes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.15.b7
  locator: { number: "3.15.b7", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 62938, end: 63228 }
  source: "Managing complexity: the ability to challenge preconceptions and to remove subject and functional boundaries so as to handle complex situations in business and management holistically; analysing, synthesising and solving complex unstructured business problems systematically and creatively."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["challenge", "remove", "handle"]
  about: "managing complexity"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to manage complexity: question preconceptions, cross subject and functional boundaries to deal with complex situations as a whole, and solve unstructured problems systematically and creatively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.15.b8
  locator: { number: "3.15.b8", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 63231, end: 63396 }
  source: "Networking: an awareness of the interpersonal skills of effective listening, negotiating, persuasion and presentation and their use in cultivating business contacts."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["cultivating"]
  about: "networking"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be aware of the interpersonal skills of listening, negotiation, persuasion and presentation and how they build business contacts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.15.b9
  locator: { number: "3.15.b9", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 63399, end: 63618 }
  source: "Effective business communication: verbal and/or non-verbal communication of complex ideas and arguments, using a range of media (for example, digital media) and technology, including the preparation of business reports."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: []
  about: "effective business communication"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to communicate complex ideas and arguments verbally and non-verbally through a range of media and technology, including business reports."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.15.b10
  locator: { number: "3.15.b10", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 63621, end: 63875 }
  source: "Current issues: awareness of current problems and/or new insights, much of which is at, or informed by, the forefront of the relevant field of the business and management academic discipline, specialism within it or similar area of professional practice."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: []
  about: "awareness of current issues"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be aware of current problems and new insights, much of it at or shaped by the forefront of the discipline, a specialism or related professional practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.15.b11
  locator: { number: "3.15.b11", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 63878, end: 64165 }
  source: "Teamwork: to operate effectively in a variety of team roles; performance within team environments and the ability to recognise and use individuals’ contributions in group processes and to negotiate and persuade or influence others; team selection, delegation, development and management."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["operate", "recognise", "negotiate", "persuade", "influence"]
  about: "teamwork"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to work well in varied team roles, recognise and use members' contributions, negotiate and influence, and select, delegate to, develop and manage a team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.15.b12
  locator: { number: "3.15.b12", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 64168, end: 64259 }
  source: "Relationship-building and influencing: across private, public and non-profit organisations."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: []
  about: "relationship-building and influencing"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to build relationships and exert influence across private, public and non-profit organisations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.15.b13
  locator: { number: "3.15.b13", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 64262, end: 64510 }
  source: "Leadership and managing change: take on leadership roles and carry them out responsibly and effectively. This includes having the capacity to recognise the need for change, the ability and proactivity to initiate change, as well as managing change."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["take", "carry", "recognise", "initiate"]
  about: "leadership and managing change"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to take on leadership roles and fulfil them responsibly and well, seeing when change is needed, starting it and managing it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.16.b1
  locator: { number: "3.16.b1", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 64563, end: 64683 }
  source: "ability to work collaboratively and inclusively with both internal and external stakeholders with professional integrity"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["work"]
  about: "collaborative and inclusive working with stakeholders"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to collaborate inclusively with internal and external stakeholders and with professional integrity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.16.b2
  locator: { number: "3.16.b2", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 64690, end: 64734 }
  source: "verbal, non-verbal and digital communication"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: []
  about: "verbal, non-verbal and digital communication"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to communicate verbally, non-verbally and digitally."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.16.b3
  locator: { number: "3.16.b3", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 64737, end: 64767 }
  source: "digital literacy and etiquette"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: []
  about: "digital literacy and etiquette"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have digital literacy and good digital etiquette."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.16.b4
  locator: { number: "3.16.b4", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 64770, end: 64848 }
  source: "conceptual, systemic and critical thinking, analysis, synthesis and evaluation"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: []
  about: "conceptual, systemic and critical thinking"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to think conceptually, systemically and critically, and to analyse, synthesise and evaluate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.16.b5
  locator: { number: "3.16.b5", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 64851, end: 64870 }
  source: "conflict resolution"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: []
  about: "conflict resolution"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to resolve conflict."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.16.b6
  locator: { number: "3.16.b6", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 64873, end: 65081 }
  source: "self-management: a readiness to accept responsibility, flexibility and adaptability, to tolerate uncertainty, challenge assumptions, handle complexity, be resilient, self- starting and appropriately assertive"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["accept", "tolerate", "challenge", "handle"]
  about: "self-management"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will manage themselves: taking responsibility, staying flexible and adaptable, coping with uncertainty and complexity, questioning assumptions, being resilient, self-starting and suitably assertive."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.16.b7
  locator: { number: "3.16.b7", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 65084, end: 65359 }
  source: "self-reflection: self-analysis and an awareness/sensitivity to diversity in terms of people and cultures - this includes a continuing appetite for development and critical reflective abilities, a responsibility for continuing to develop their own new skills at a higher level"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["develop"]
  about: "self-reflection"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to reflect on themselves, be aware of and sensitive to diversity in people and cultures, keep wanting to develop and take responsibility for building new skills to a higher level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.16.b8
  locator: { number: "3.16.b8", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 65362, end: 65518 }
  source: "interpersonal skills: understanding the needs of others and empathy towards them; sensitivity to diversity in people and inclusivity in different situations"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["understanding"]
  about: "interpersonal skills"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have interpersonal skills: understanding and empathising with others' needs, and sensitivity to diversity and inclusion in different settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.16.b9
  locator: { number: "3.16.b9", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 65521, end: 65660 }
  source: "initiative: the qualities and transferable skills necessary for employment requiring the exercise of initiative and personal responsibility"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: []
  about: "initiative"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have the qualities and transferable skills for employment that calls for initiative and personal responsibility."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.16.b10
  locator: { number: "3.16.b10", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 65663, end: 65848 }
  source: "independent learning: the learning ability required for continuing professional development and ability to act independently in planning and implementing projects at professional level."
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject's master's courses"
  addressee: learner
  verbs: ["act", "planning", "implementing"]
  about: "independent learning"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have the learning ability needed for continuing professional development and be able to plan and deliver projects independently at a professional level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.17
  locator: { number: "3.17", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 65849, end: 66295 }
  source: "3.17 Skills and practice developed in master's graduates will vary depending on the type of course (see paragraph 1.3). For example, students of Types 2 and 4 master's courses (for career development) will be able to reflect on and learn from their prior experiences and thus be able to integrate new knowledge with past experience, applying it to new situations, and acquire new skills as well as developing existing ones. Learning and teaching\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "students of Types 2 and 4 career-development courses"
  addressee: learner
  verbs: ["reflect", "learn", "integrate", "applying", "acquire"]
  about: "learning from prior experience"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Skills differ with course type; on Types 2 and 4, students will be able to learn from earlier experience by reflecting on it, combine new knowledge with it, apply it to new situations and gain new skills while building existing ones."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.23
  locator: { number: "3.23", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 69780, end: 70064 }
  source: "3.23 Assessment should form part of the learning process and student learning should be assisted through the provision of feedback on formative and summative work. Feedback should be provided in a timely actionable manner, enabling both development within a module/unit and a course.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment and feedback"
  addressee: provider
  verbs: ["form", "provided"]
  about: "assessment for learning and timely feedback"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Assessment should be part of learning, with feedback on formative and summative work that should be timely and usable for development within a module and across the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.29
  locator: { number: "3.29", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 72393, end: 72622 }
  source: "3.29 Where assessment is completed in groups, careful consideration should be given to the extent of group work in a course, to its authenticity and fit for the task assigned and the attribution of group versus individual marks.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "group assessment"
  addressee: provider
  verbs: ["given"]
  about: "group work and its marking"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Where work is assessed in groups, the amount of group work, its authenticity, its fit to the task and the split between group and individual marks should all be considered with care."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.30
  locator: { number: "3.30", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 72622, end: 72922 }
  source: "3.30 Peer review and assessment can play an important role in assessment and learning, particularly by helping engage students. Whether undertaken for formative or summative purposes, clear guidance should be provided to students, and limits set on the weighting of peer assessment in a unit/module.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "peer review and peer assessment"
  addressee: provider
  verbs: ["provided", "set"]
  about: "guidance and limits for peer assessment"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Peer review and assessment can engage students; whether formative or summative, students should get clear guidance and the weighting of peer assessment in a module should be capped."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.31
  locator: { number: "3.31", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 72922, end: 73191 }
  source: "3.31 Details of assessment should be transparent and shared with students along with the relevant marking criteria. There may also be opportunities for collaborative or participative approaches whereby students may co-design assessments with their tutors and/or peers.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment information"
  addressee: provider
  verbs: ["shared", "co-design"]
  about: "transparent assessment and co-design"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Assessment details should be open and given to students with the marking criteria, and there may be room for students to co-design assessments with tutors or peers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/3.32
  locator: { number: "3.32", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 73191, end: 73265 }
  source: "3.32 Assessment should be designed with the student workload in mind.\n\n24\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["designed"]
  about: "student workload"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Assessment should be planned with the load it places on students in mind."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 73805, end: 74405 }
  source: "4.2 Many students will perform better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to QAA's Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Standard sets out the descriptor for a qualification at Level 7 on the FHEQ and SCQF Level 11 on the FQHEIS: master's degree. It can be used as a reference point for other qualifications at FHEQ Level 7/SCQF Level 11 on the FQHEIS, including postgraduate certifications and postgraduate diplomas.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["perform", "refer"]
  about: "evidence of achievement above the threshold"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Many students will go beyond the threshold; each provider decides what evidence shows this and should refer to the qualification frameworks; the standards match the master's descriptor at FHEQ level 7 and SCQF level 11 and can guide postgraduate certificates and diplomas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 75180, end: 75382 }
  source: "A systematic and deep understanding of relevant knowledge about organisations, their external context, how they are managed and the detailed relationship between these and their application to practice."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in business and management at the threshold"
  addressee: learner
  verbs: []
  about: "systematic, deep understanding of organisations and their management"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown a systematic and deep understanding of organisations, their external context and management, and how these relate to each other and to practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 75385, end: 75606 }
  source: "Comprehensive understanding of appropriate techniques sufficient to allow detailed investigation, research or advanced scholarship into relevant business and management issues or specialism within business and management."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in business and management at the threshold"
  addressee: learner
  verbs: ["allow"]
  about: "understanding of techniques for investigation and research"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown full understanding of the techniques needed for detailed investigation, research or advanced scholarship into issues in business and management or a specialism."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 75616, end: 75818 }
  source: "An excellent command of subject-specific academic and professional skills relevant to the appropriate field of business and management as well as consistent proficiency in generic skills and attributes."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in business and management at the threshold"
  addressee: learner
  verbs: []
  about: "command of subject and professional skills, with generic skills"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown strong command of the subject's academic and professional skills in the relevant field and steady proficiency in generic skills and attributes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 75842, end: 76040 }
  source: "A critical awareness of current issues in business and management which is informed by leading edge research and practice in the field as well as by a proactive and independent approach to learning."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in business and management at the threshold"
  addressee: learner
  verbs: ["informed"]
  about: "critical awareness of current issues"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown critical awareness of current issues in the field, drawn from leading research and practice and from a proactive, independent approach to learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 76047, end: 76225 }
  source: "Conceptual understanding that enables students to evaluate critically current research and advanced scholarship in the field of business and management or a specialism within it."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in business and management at the threshold"
  addressee: learner
  verbs: ["evaluate"]
  about: "critical evaluation of current research and scholarship"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown conceptual understanding that allows critical evaluation of current research and advanced scholarship in the field or a specialism."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 76240, end: 76408 }
  source: "Application of relevant knowledge to a range of complex situations, taking account of its relationship and interaction with other areas of the business or organisation."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in business and management at the threshold"
  addressee: learner
  verbs: ["taking"]
  about: "applying knowledge to complex situations"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown that they can apply relevant knowledge to a range of complex situations, allowing for its links with other parts of the business or organisation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 76411, end: 76671 }
  source: "Originality and creativity in the application of knowledge, together with a practical understanding of how established techniques of research and enquiry are used to create and interpret knowledge in business and management, or in a specialist field within it."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in business and management at the threshold"
  addressee: learner
  verbs: ["used", "create", "interpret"]
  about: "originality in applying knowledge and research practice"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown originality and creativity in applying knowledge, with a practical grasp of how established research and enquiry techniques produce and interpret knowledge in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 76674, end: 76758 }
  source: "Ability to evaluate and integrate theory and practice in a wide range of situations."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in business and management at the threshold"
  addressee: learner
  verbs: ["evaluate", "integrate"]
  about: "evaluating and joining theory and practice"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown that they can evaluate and integrate theory and practice across many situations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 76761, end: 76843 }
  source: "An understanding of how the boundaries of knowledge are advanced through research."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in business and management at the threshold"
  addressee: learner
  verbs: ["advanced"]
  about: "how research advances knowledge"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown understanding of how research pushes forward the limits of knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/4.4.b10
  locator: { number: "4.4.b10", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 76853, end: 76968 }
  source: "A commitment to championing the values of global social responsibility, ethical values and behaving with integrity."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in business and management at the threshold"
  addressee: learner
  verbs: ["championing", "behaving"]
  about: "commitment to global social responsibility and integrity"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown commitment to championing global social responsibility and ethical values and to acting with integrity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/4.4.b11
  locator: { number: "4.4.b11", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 76971, end: 77146 }
  source: "An ability to take an international perspective, including understanding the impact of globalisation on businesses, societies and the environment and the ethical implications."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in business and management at the threshold"
  addressee: learner
  verbs: ["take"]
  about: "an international perspective on globalisation"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown the ability to take an international view, including the effects of globalisation on business, society and the environment and their ethical implications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/masters-degrees-in-business-and-management-2023/4.4.b12
  locator: { number: "4.4.b12", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 77149, end: 77336 }
  source: "An ability to manage and lead with a strong sense of global social responsibility, appreciating the contradictory challenges this presents in complex business and management environments."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in business and management at the threshold"
  addressee: learner
  verbs: ["manage", "lead", "appreciating"]
  about: "managing and leading with global social responsibility"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown they can lead and manage with a firm sense of social responsibility worldwide, aware of the conflicting pressures this brings in complex settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/masters-degrees-in-business-and-management-2023/1.14
  forPractitioner: { text: "Check the course against the purposes in 1.8: a general master's should address them, weighting them to its type and to any professional accreditation, and its intended outcomes should make that weighting visible.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) for the master's award at FHEQ level 7 (SCQF level 11): general courses address the listed purposes, weighted by course type. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 1.14. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside the purposes in 1.8, the typology in 1.3 and 1.20 to 1.30, and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team is writing or revising course aims; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: Which of the purposes in 1.8 does your course weight most, and where do your outcomes show it? Avoid quoting paragraph 1.14 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/1.21
  forPractitioner: { text: "On a career-entry generalist course, aim for a sound grasp of how organisations work that lets students add value to an employer quickly.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will build a sound understanding of how businesses and organisations work, so that you can contribute to an employer early on.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) for Type 1 courses for the master's award at FHEQ level 7 (SCQF level 11): a sound understanding of organisational contexts that supports early contribution at work. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 1.21. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.2, 3.8 and 4.4.b1."
  author-agent-dialogue: "Raise this when a student new to business asks what the course will give them. Put it in plain words: second person for a student, the course outcome for staff. Ask: Which parts of how an organisation works do you feel least sure about yet? Avoid reading paragraph 1.21 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/1.24
  forPractitioner: { text: "For a post-experience generalist course such as an MBA, design learning that builds on what entrants bring from at least two years of work, with leadership, strategy, reflection and peer exchange at its centre.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) for one course type for the master's award at FHEQ level 7 (SCQF level 11): post-experience generalist learning draws on entrants' work experience. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 1.24. Do not claim that every master's must require work experience or that the two-year figure is a fixed rule. Set it beside 1.29 and 1.30 (Type 4), 3.12 and 3.17 (learning from experience) and 3.21."
  author-agent-dialogue: "Raise this with a programme team or teacher when an MBA or similar post-experience course is being designed or reviewed; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: How does each module draw on what participants already know from work? Avoid quoting paragraph 1.24 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/1.28
  forPractitioner: { text: "In a pre-experience specialist course, pair the theory base with skills students can use in practice, and note any professional body qualification the course connects to.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) for one course type for the master's award at FHEQ level 7 (SCQF level 11): specialist career-entry courses add practice-relevant skills to theory. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 1.28. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 1.27, 3.11 (specialist knowledge) and 3.15 (subject skills)."
  author-agent-dialogue: "Raise this with a programme team or teacher when a specialist pre-experience course looks heavy on theory; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: Where in the course do students practise skills they will use in the job the course prepares them for? Avoid quoting paragraph 1.28 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/1.31
  forPractitioner: { text: "Treat equality, diversity and inclusion as part of how the subject is taught and practised, not as a compliance add-on, recognising differences that overlap and go beyond the protected characteristics.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) under the EDI theme for the master's award at FHEQ level 7 (SCQF level 11): EDI is to be part of the subject's culture and practice. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 1.31. Do not claim that it lists every characteristic a course must monitor or that it is a statutory duty in itself. Set it beside 1.33 to 1.37, 2.13 and theme:edi."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team discusses inclusion in its subject; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: Where would a student see inclusion in the everyday practice of your course, not only in its policies? Avoid quoting paragraph 1.31 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/1.33
  forPractitioner: { text: "Expect graduates to leave with EDI principles as part of how they will manage and lead; teach the link between inclusion, reflective practice and organisations' work on inequality and the SDGs.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your studies will build the principles of equality, diversity and inclusion into how you manage and lead, so that you can help organisations tackle inequality.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) under the EDI theme for the master's award at FHEQ level 7 (SCQF level 11): study builds EDI principles into future managers and leaders. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 1.33. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 1.10 (responsible leadership), 1.34, 3.16.b8 and qaa/fheq-2024/4.17.b8.2."
  author-agent-dialogue: "Raise this when a student asks why inclusion matters in a management course. Put it in plain words: second person for a student, the course outcome for staff. Ask: How would you show inclusion in a team you led? Avoid reading paragraph 1.33 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/1.34
  forPractitioner: { text: "Teach the legal duties on discrimination and the skills to build inclusive workplaces; choose content and cases that draw on varied perspectives, including the Global South and marginalised communities, and examine critically how dominant approaches can exclude.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should come to know the law that protects people from discrimination and gain the skills to build inclusive workplaces, studying a wide range of perspectives and questioning approaches that leave people out.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on both students and courses under the EDI theme for the master's award at FHEQ level 7 (SCQF level 11): critical understanding of EDI in organisations, with diverse and critical content. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 1.34. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 1.33, 1.35, 3.10.b5 and theme:edi."
  author-agent-dialogue: "Raise this when content choices or inclusive leadership come up with a student or a course team. For a student, ask what perspectives their reading leaves out; for staff, frame it as a curriculum review. Ask: Which cases in the course come from outside the usual dominant settings? Avoid reading paragraph 1.34 aloud at length or treating it as a legal checklist."
- statement: qaa/masters-degrees-in-business-and-management-2023/1.35
  forPractitioner: { text: "Design so every student can reach their potential and see themselves in the course: weigh the effects of each mode of study, plan assessment that lets different students succeed, and take account of people's multiple identities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) under the EDI theme for the master's award at FHEQ level 7 (SCQF level 11): inclusive design of teaching, modes of study and assessment. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 1.35. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 1.38 to 1.40, 2.13, 3.24 and theme:edi."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team chooses delivery modes or assessment formats; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: Which students might the current mode or assessment disadvantage, and what would change that? Avoid quoting paragraph 1.35 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/1.37
  forPractitioner: { text: "Put EDI on the regular review cycle, involve students in it where possible, and consider an equality impact assessment when course changes go for approval.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) under the EDI theme for the master's award at FHEQ level 7 (SCQF level 11): regular reflection on EDI, in partnership with students. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 1.37. Do not claim that an equality impact assessment is required. Set it beside 2.19 (monitoring and review) and 1.31."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team plans annual review or a course change; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: When did the team last review inclusion with students, and what changed as a result? Avoid quoting paragraph 1.37 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/1.38
  forPractitioner: { text: "Meet the regulatory minimum for accessibility and go further: check information, curriculum, spaces, resources and assessments at every stage, with reasonable adjustments and attention to barriers such as digital poverty and caring duties.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) under the accessibility theme for the master's award at FHEQ level 7 (SCQF level 11): accessibility at least to the regulatory minimum, across the whole student journey. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 1.38. Do not claim that its examples are a complete list. Set it beside 1.39, 1.40, 2.14 and theme:accessibility."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team reviews information, spaces or assessment for access; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: At which stage, from application to graduation, is access least certain for your students? Avoid quoting paragraph 1.38 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/1.39
  forPractitioner: { text: "Anticipate the needs of neurodivergent students and those with specific learning difficulties at design stage rather than waiting for adjustments to be requested.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) under the accessibility theme for the master's award at FHEQ level 7 (SCQF level 11): barriers are designed out in advance. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 1.39. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 1.38, 3.24 and theme:accessibility."
  author-agent-dialogue: "Raise this with a programme team or teacher when a module is being designed or redesigned; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: What would a neurodivergent student find hardest in this module as it stands? Avoid quoting paragraph 1.39 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/1.40
  forPractitioner: { text: "Make placements, international experiences and digital provision open to every student on equal terms.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) under the accessibility theme for the master's award at FHEQ level 7 (SCQF level 11): equal access to workplace, international and digital learning. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 1.40. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 1.38, 2.16 and theme:accessibility."
  author-agent-dialogue: "Raise this with a programme team or teacher when placements, study abroad or online provision are planned; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: Who on the course could not take up a placement or trip as it is now arranged? Avoid quoting paragraph 1.40 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/1.42
  forPractitioner: { text: "Build sustainability into each functional area of the curriculum, not one module alone, using topics such as sustainable supply chains, carbon literacy, integrated reporting and responsible leadership.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a provider expectation under the sustainability theme, worded with 'needs to' and 'imperative' rather than must or should for the master's award at FHEQ level 7 (SCQF level 11): sustainable management across the curriculum, with example topics. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 1.42. Do not claim that the example topics are required or complete. Set it beside 1.41, 1.43, 3.10.b1 and theme:esd."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team maps sustainability across its modules; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: In which functional areas of the course does climate and sustainability content not yet appear? Avoid quoting paragraph 1.42 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/2.13
  forPractitioner: { text: "Design with inclusivity in mind and consider offering a choice of study modes and assessment so students can fit learning to their circumstances.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) with permissive options (may) for the master's award at FHEQ level 7 (SCQF level 11): inclusive design and optional flexibility in mode and assessment. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 2.13. Do not claim that any particular mode must be offered. Set it beside 2.14, 2.15, 1.35 and theme:accessibility."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team weighs part-time, blended or block delivery; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: Which students could join the course only if it were offered differently? Avoid quoting paragraph 2.13 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/2.19
  forPractitioner: { text: "Involve students in monitoring and periodic review, use this statement among the external reference points, and include equality, diversity and inclusion in what is reviewed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) on review for the master's award at FHEQ level 7 (SCQF level 11): students take part in course monitoring and review. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 2.19. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 2.20, 2.21, 1.37."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team prepares for periodic review; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: How do students shape the evidence and the actions in your review? Avoid quoting paragraph 2.19 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/2.20
  forPractitioner: { text: "Include external reviewers in periodic review to test proposed changes, confirm threshold standards and check that content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider expectation (will) on externality for the master's award at FHEQ level 7 (SCQF level 11): periodic review uses external reviewers to confirm threshold standards. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 2.20. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 2.21, 4.1 and 4.4."
  author-agent-dialogue: "Raise this with a programme team or teacher when a periodic review panel is being set up; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: Who outside the institution will judge whether the threshold in 4.4 is met? Avoid quoting paragraph 2.20 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.1
  forPractitioner: { text: "In a generalist course, cover organisations broadly, analytically and in an integrated way; in a specialist course, set the specialism in the context of the wider field; read both against the level 7 descriptor.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider expectation (will) on course scope for the master's award at FHEQ level 7 (SCQF level 11): breadth for generalist courses and wider context for specialist ones. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.1. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.2, 3.8, 3.10, 3.11 and the level 7 descriptor qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team defines the scope of a generalist or specialist course; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: Where does a specialist student meet the wider field of business and management? Avoid quoting paragraph 3.1 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.2
  forPractitioner: { text: "Ensure graduates can show knowledge of organisations, their environmental and regulatory context and their management, with attention to change, risk, sustainability and social impact.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to show what you know about organisations, the wider business world they operate in, including its environmental and legal sides, and how they are managed.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) for the master's award at FHEQ level 7 (SCQF level 11): knowledge of organisations, their context and their management. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.2. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.3 to 3.6, 4.4.b1 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when a student or team asks what core knowledge a master's covers. Put it in plain words: second person for a student, the course outcome for staff. Ask: Can you explain how an organisation you know is shaped by its environmental and regulatory context? Avoid reading paragraph 3.2 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.3
  forPractitioner: { text: "Teach and assess the links between organisations, their context and their management, not each area alone, whatever the mode of study.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to show how what you know about organisations, their context and their management fits together.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) for the master's award at FHEQ level 7 (SCQF level 11): integration across the areas of knowledge. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.3. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.2, 3.8 and 4.4.b1."
  author-agent-dialogue: "Raise this when a student treats modules as separate topics. Put it in plain words: second person for a student, the course outcome for staff. Ask: How does what you learned in one module change how you see another? Avoid reading paragraph 3.3 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.7
  forPractitioner: { text: "State the course's knowledge, understanding and skills in its learning outcomes, matched to its type in the typology.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider expectation (will) on learning outcomes for the master's award at FHEQ level 7 (SCQF level 11): outcomes set out knowledge, understanding and skills by course type. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.7. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 1.3, 3.9, 3.17 and 4.4."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team writes or revises course learning outcomes; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: Do your outcomes reflect the type of course you run, and could a reader tell which type from them? Avoid quoting paragraph 3.7 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.8
  forPractitioner: { text: "Expect graduates, specialists included, to understand and respond to change and to link the different areas of an organisation, with broad knowledge and deep understanding.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how organisations change and how to respond, and you will be able to connect different parts of an organisation, even if you specialise.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will; partly typical) for the master's award at FHEQ level 7 (SCQF level 11): breadth, response to change and integrative links across an organisation. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.8. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.4 to 3.6, 4.4.b1, 4.4.b6 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when a specialist student asks why wider organisational topics matter. Put it in plain words: second person for a student, the course outcome for staff. Ask: How does your specialism depend on other parts of the organisation? Avoid reading paragraph 3.8 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.10.b1
  forPractitioner: { text: "Where the course covers it, develop critical understanding of responsible management and ethical leadership across social, legal, economic and environmental issues.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You may study ethics, responsibility and sustainability in depth: how to manage responsibly and lead ethically on social, legal, economic and environmental questions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will, typically), one of a list of areas from which generalist courses draw some for the master's award at FHEQ level 7 (SCQF level 11): ethics, responsibility and sustainability. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.10.b1. Do not claim that every course must cover every area in the list. Set it beside 3.2, 3.11, 4.4.b1 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when ethics or sustainability modules are discussed. Put it in plain words: second person for a student, the course outcome for staff. Ask: Where have you seen a manager weigh profit against an environmental or social cost? Avoid reading paragraph 3.10.b1 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.10.b2
  forPractitioner: { text: "Where the course covers it, develop critical understanding of how markets develop and operate, including their failures, externalities and fair trade.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You may study markets and economies in depth, including why markets sometimes fail and what fair trade means.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will, typically), one of a list of areas from which generalist courses draw some for the master's award at FHEQ level 7 (SCQF level 11): markets and economies. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.10.b2. Do not claim that every course must cover every area in the list. Set it beside 3.2, 3.11, 4.4.b1 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when economics content is planned or questioned. Put it in plain words: second person for a student, the course outcome for staff. Ask: Can you name a market failure that affects a business you know? Avoid reading paragraph 3.10.b2 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.10.b3
  forPractitioner: { text: "Where the course covers it, develop critical understanding of customer relationships, consumer behaviour, segmentation and positioning, selling and product and service innovation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You may study marketing, sales, negotiation and customers in depth, from consumer behaviour to how products and services are positioned and improved.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will, typically), one of a list of areas from which generalist courses draw some for the master's award at FHEQ level 7 (SCQF level 11): marketing, sales, negotiation and customers. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.10.b3. Do not claim that every course must cover every area in the list. Set it beside 3.2, 3.11, 4.4.b1 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when marketing content is planned or questioned. Put it in plain words: second person for a student, the course outcome for staff. Ask: How would you decide which customers a new service should target first? Avoid reading paragraph 3.10.b3 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.10.b4
  forPractitioner: { text: "Where the course covers it, develop critical understanding of sources and uses of finance and of accounting information for planning, control, decisions and risk.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You may study finance and accounting in depth: where money comes from, how it is managed and how accounting supports planning, decisions and managing risk.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will, typically), one of a list of areas from which generalist courses draw some for the master's award at FHEQ level 7 (SCQF level 11): finance and accounting. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.10.b4. Do not claim that every course must cover every area in the list. Set it beside 3.2, 3.11, 4.4.b1 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when finance content is planned or a student is anxious about numbers. Put it in plain words: second person for a student, the course outcome for staff. Ask: Which financial report would you look at first to judge a business decision? Avoid reading paragraph 3.10.b4 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.10.b5
  forPractitioner: { text: "Where the course covers it, develop critical understanding of inclusive leadership, strategic people management, engagement, employment law, cross-cultural working and EDI.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You may study people and organisational behaviour in depth, including inclusive leadership, managing and developing people, employment law and working across cultures.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will, typically), one of a list of areas from which generalist courses draw some for the master's award at FHEQ level 7 (SCQF level 11): people and organisational behaviour. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.10.b5. Do not claim that every course must cover every area in the list. Set it beside 3.2, 3.11, 4.4.b1 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when people management or HR content is discussed. Put it in plain words: second person for a student, the course outcome for staff. Ask: How would you build engagement in a team drawn from several cultures? Avoid reading paragraph 3.10.b5 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.10.b6
  forPractitioner: { text: "Where the course covers it, develop critical understanding of operations, supply chains, quality and project management, and of tools that turn data into decision support.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You may study operations and innovation in depth, from supply chains and quality to managing projects and using data to support decisions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will, typically), one of a list of areas from which generalist courses draw some for the master's award at FHEQ level 7 (SCQF level 11): operations and business innovation. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.10.b6. Do not claim that every course must cover every area in the list. Set it beside 3.2, 3.11, 4.4.b1 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when operations content is planned. Put it in plain words: second person for a student, the course outcome for staff. Ask: Where would a delay in one supplier hurt an organisation you know most? Avoid reading paragraph 3.10.b6 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.10.b7
  forPractitioner: { text: "Where the course covers it, develop critical understanding of analytics, statistics, information systems and business intelligence for data-driven decisions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You may study data analytics, digital business and information systems in depth, and how they help organisations decide on the basis of evidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will, typically), one of a list of areas from which generalist courses draw some for the master's award at FHEQ level 7 (SCQF level 11): analytics, statistics, digital business and business intelligence. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.10.b7. Do not claim that every course must cover every area in the list. Set it beside 3.2, 3.11, 4.4.b1 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when digital or analytics content is discussed. Put it in plain words: second person for a student, the course outcome for staff. Ask: Which decision in your organisation could better data change? Avoid reading paragraph 3.10.b7 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.10.b8
  forPractitioner: { text: "Where the course covers it, develop critical understanding of strategy and policy making for stakeholders, with risk, crisis and continuity planning.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You may study business policy and strategy in depth, including how organisations plan for risk, crises and continuity.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will, typically), one of a list of areas from which generalist courses draw some for the master's award at FHEQ level 7 (SCQF level 11): business policy and strategy. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.10.b8. Do not claim that every course must cover every area in the list. Set it beside 3.2, 3.11, 4.4.b1 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when strategy content is planned. Put it in plain words: second person for a student, the course outcome for staff. Ask: How would you test a strategy against a sudden crisis? Avoid reading paragraph 3.10.b8 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.10.b9
  forPractitioner: { text: "Where the course covers it, develop critical understanding of public and voluntary sector governance, finance, leadership, co-production and public value.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You may study how public services and charities are run, including their governance, money, leadership and public value.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will, typically), one of a list of areas from which generalist courses draw some for the master's award at FHEQ level 7 (SCQF level 11): public and non-profit strategic management. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.10.b9. Do not claim that every course must cover every area in the list. Set it beside 3.2, 3.11, 4.4.b1 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when a student comes from or aims for the public or voluntary sector. Put it in plain words: second person for a student, the course outcome for staff. Ask: How does accountability differ between a charity and a company? Avoid reading paragraph 3.10.b9 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.10.b10
  forPractitioner: { text: "Where the course covers it, develop critical understanding of venture creation and of recognising and valuing intellectual property.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You may study entrepreneurship in depth: turning new ideas into products, services or organisations, and protecting and valuing intellectual property.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will, typically), one of a list of areas from which generalist courses draw some for the master's award at FHEQ level 7 (SCQF level 11): entrepreneurship and enterprise development. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.10.b10. Do not claim that every course must cover every area in the list. Set it beside 3.2, 3.11, 4.4.b1 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when a student is interested in starting a venture. Put it in plain words: second person for a student, the course outcome for staff. Ask: What would make an idea of yours worth investing in? Avoid reading paragraph 3.10.b10 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.10.b11
  forPractitioner: { text: "In an MPA, weight the content towards governance, public policy and public management.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a statement about MPA course content, not an outcome for the student", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider expectation (will) for MPA courses for the master's award at FHEQ level 7 (SCQF level 11): heavier content on governance, public policy and public management. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.10.b11. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 1.25, 3.10.b9 and the MPA accreditors in SB5."
  author-agent-dialogue: "Raise this with a programme team or teacher when an MPA is designed or reviewed; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: How much of the course addresses governance and public policy directly? Avoid quoting paragraph 3.10.b11 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.11.b1
  forPractitioner: { text: "Develop specialist knowledge and the ability to place the specialism within the wider organisation and its context.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will gain knowledge of your specialist subject and see how it fits into the wider organisation and its setting.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) for specialist courses for the master's award at FHEQ level 7 (SCQF level 11): specialist knowledge set within its wider organisational frame. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.11.b1. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.1, 3.8 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when a specialist student focuses only on their field. Put it in plain words: second person for a student, the course outcome for staff. Ask: Who else in an organisation depends on your specialism? Avoid reading paragraph 3.11.b1 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.11.b2
  forPractitioner: { text: "Cover the specialism's current debates and the research techniques its field uses.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will learn the current issues and debates in your specialism and the research techniques used in it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) for specialist courses for the master's award at FHEQ level 7 (SCQF level 11): current issues and research techniques in the specialism. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.11.b2. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 4.4.b2, 4.4.b4 and qaa/fheq-2024/4.17.b2."
  author-agent-dialogue: "Raise this when a student chooses a dissertation topic. Put it in plain words: second person for a student, the course outcome for staff. Ask: What is the most debated question in your specialism right now? Avoid reading paragraph 3.11.b2 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.11.b3
  forPractitioner: { text: "Combine theory and application so specialists can use their skills in the organisations they are likely to join.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will gain both theory and practice so that you can use your specialist skills in the organisations where you may work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) for specialist courses for the master's award at FHEQ level 7 (SCQF level 11): theoretical and applied perspectives for using specialist skills. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.11.b3. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 1.28, 4.4.b6 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise this when a specialist student asks how theory will help at work. Put it in plain words: second person for a student, the course outcome for staff. Ask: Which specialist skill have you applied in a real setting so far? Avoid reading paragraph 3.11.b3 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.12
  forPractitioner: { text: "On post-experience courses, ask students to connect new theory to their own working experience in teaching and assessment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to connect what you learn to your own experience at work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) for Types 2 and 4 for the master's award at FHEQ level 7 (SCQF level 11): new knowledge grounded in professional experience. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.12. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 1.24, 1.29, 3.17 and 3.28."
  author-agent-dialogue: "Raise this when an experienced student asks how theory relates to their job. Put it in plain words: second person for a student, the course outcome for staff. Ask: Which idea from the course best explains something you have seen at work? Avoid reading paragraph 3.12 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.14
  forPractitioner: { text: "Develop and assess intellectual skills, subject competencies and strong personal, interpersonal and team skills at a level beyond undergraduate study.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to show strong thinking skills, business and management competencies and well-developed personal and team-working skills, beyond what a first degree asks.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) and the lead-in for the skills lists 3.15 and 3.16 for the master's award at FHEQ level 7 (SCQF level 11): a range of intellectual, subject, personal and team skills above undergraduate level. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.14. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.15, 3.16, 4.4.b3, qaa/fheq-2024/4.17.b6 and spine:7."
  author-agent-dialogue: "Raise this when a student asks how master's skills differ from a first degree. Put it in plain words: second person for a student, the course outcome for staff. Ask: Which of your skills has moved furthest since your first degree? Avoid reading paragraph 3.14 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.15.b1
  forPractitioner: { text: "Develop people-management skills from team building and motivation to choosing leadership styles, managing performance, coaching and fostering inclusion.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to manage people: build and motivate teams, choose how to lead in different situations, support well-being and inclusion, and coach others.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject skill (will, from the lead-in 3.14) for the master's award at FHEQ level 7 (SCQF level 11): people management. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.15.b1. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 4.4.b12, 3.16.b8 and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Raise this when a student plans their skills development or a team maps skills to modules. Put it in plain words: second person for a student, the course outcome for staff. Ask: Which leadership style do you fall back on, and when would another work better? Avoid reading paragraph 3.15.b1 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.15.b2
  forPractitioner: { text: "Develop structured problem-solving and critical analysis: diagnosing causes, evaluating options, choosing sustainable solutions, checking assumptions and reasoning, and reviewing decisions once made.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to work out the cause of a problem, weigh possible solutions, choose sustainable ones, test the reasoning behind them and review how they worked.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject skill (will, from the lead-in 3.14) for the master's award at FHEQ level 7 (SCQF level 11): problem-solving and critical analysis. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.15.b2. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 4.4.b6, 3.16.b4 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise this when a student plans their skills development or a team maps skills to modules. Put it in plain words: second person for a student, the course outcome for staff. Ask: When did you last check the assumptions behind a decision before acting on it? Avoid reading paragraph 3.15.b2 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.15.b3
  forPractitioner: { text: "Develop research skills across design, mixed data collection and analysis, synthesis and reporting, with digital literacy, and the critical appraisal of published studies for evidence-based decisions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to plan and carry out research, analyse numbers and words, report what you find, and judge how sound and relevant published research is.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject skill (will, from the lead-in 3.14) for the master's award at FHEQ level 7 (SCQF level 11): research. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.15.b3. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 4.4.b2, 4.4.b5, 4.4.b7 and qaa/fheq-2024/4.17.b2."
  author-agent-dialogue: "Raise this when a student plans their skills development or a team maps skills to modules. Put it in plain words: second person for a student, the course outcome for staff. Ask: How would you judge whether a published study applies to your situation? Avoid reading paragraph 3.15.b3 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.15.b4
  forPractitioner: { text: "Develop commercial awareness of what makes organisations succeed or fail and how they keep customers satisfied and loyal in sustainable ways.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand what makes a business succeed or fail and why keeping customers satisfied and loyal, in sustainable ways, matters.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject skill (will, from the lead-in 3.14) for the master's award at FHEQ level 7 (SCQF level 11): commercial acumen. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.15.b4. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.10.b3, 4.4.b6 and spine:7."
  author-agent-dialogue: "Raise this when a student plans their skills development or a team maps skills to modules. Put it in plain words: second person for a student, the course outcome for staff. Ask: What would you say is the main driver of success for an organisation you know? Avoid reading paragraph 3.15.b4 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.15.b5
  forPractitioner: { text: "Develop enterprising behaviour: generating and pitching ideas, managing intellectual property, building support and delivering sustainable results.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to act in an enterprising way: come up with ideas, develop and share them, protect intellectual property and win support to deliver results.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject skill (will, from the lead-in 3.14) for the master's award at FHEQ level 7 (SCQF level 11): innovation, creativity and enterprise. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.15.b5. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.10.b10, 1.46 and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Raise this when a student plans their skills development or a team maps skills to modules. Put it in plain words: second person for a student, the course outcome for staff. Ask: What idea of yours could you develop and pitch this term? Avoid reading paragraph 3.15.b5 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.15.b6
  forPractitioner: { text: "Develop quantitative skills for handling data and for estimating and modelling business problems.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to use numbers and data to estimate, evaluate and model business problems.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject skill (will, from the lead-in 3.14) for the master's award at FHEQ level 7 (SCQF level 11): numeracy. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.15.b6. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.10.b7 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise this when a student plans their skills development or a team maps skills to modules. Put it in plain words: second person for a student, the course outcome for staff. Ask: Which business problem could you model with the data you have? Avoid reading paragraph 3.15.b6 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.15.b7
  forPractitioner: { text: "Develop the ability to work across functional boundaries and solve complex, unstructured problems both systematically and creatively.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to handle complex, messy problems by questioning assumptions, looking across functions and solving them in a careful but creative way.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject skill (will, from the lead-in 3.14) for the master's award at FHEQ level 7 (SCQF level 11): managing complexity. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.15.b7. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 4.4.b6 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise this when a student plans their skills development or a team maps skills to modules. Put it in plain words: second person for a student, the course outcome for staff. Ask: Which problem you face cuts across several departments, and how would you approach it? Avoid reading paragraph 3.15.b7 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.15.b8
  forPractitioner: { text: "Develop awareness of listening, negotiating, persuading and presenting as the skills that build professional networks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how listening, negotiating, persuading and presenting help you build professional contacts.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject skill (will, from the lead-in 3.14) for the master's award at FHEQ level 7 (SCQF level 11): networking. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.15.b8. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.15.b12 and 3.16.b8."
  author-agent-dialogue: "Raise this when a student plans their skills development or a team maps skills to modules. Put it in plain words: second person for a student, the course outcome for staff. Ask: Who would you most like in your professional network, and how might you reach them? Avoid reading paragraph 3.15.b8 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.15.b9
  forPractitioner: { text: "Develop communication of complex ideas across media and technologies, including the writing of business reports.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to communicate complex ideas clearly in speech, writing and other media, including business reports.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject skill (will, from the lead-in 3.14) for the master's award at FHEQ level 7 (SCQF level 11): effective business communication. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.15.b9. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.16.b2 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise this when a student plans their skills development or a team maps skills to modules. Put it in plain words: second person for a student, the course outcome for staff. Ask: Who is the audience for your next report, and what do they need first? Avoid reading paragraph 3.15.b9 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.15.b10
  forPractitioner: { text: "Keep students in touch with current problems and new insights from the leading edge of the field and of professional practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know the current problems and new ideas at the leading edge of business and management and your own specialism.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject skill (will, from the lead-in 3.14) for the master's award at FHEQ level 7 (SCQF level 11): awareness of current issues. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.15.b10. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 4.4.b4 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise this when a student plans their skills development or a team maps skills to modules. Put it in plain words: second person for a student, the course outcome for staff. Ask: What new insight in your field has changed how you think this year? Avoid reading paragraph 3.15.b10 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.15.b11
  forPractitioner: { text: "Develop teamwork across roles: drawing on members' contributions, negotiating and influencing, and selecting, delegating to and developing team members.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to work well in different team roles, make use of what each person brings, negotiate and influence, and lead and develop a team.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject skill (will, from the lead-in 3.14) for the master's award at FHEQ level 7 (SCQF level 11): teamwork. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.15.b11. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.15.b1, 3.16.b1 and 3.29."
  author-agent-dialogue: "Raise this when a student plans their skills development or a team maps skills to modules. Put it in plain words: second person for a student, the course outcome for staff. Ask: What role do you usually take in a team, and which role do you avoid? Avoid reading paragraph 3.15.b11 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.15.b12
  forPractitioner: { text: "Develop the ability to build relationships and influence across organisations in all three sectors.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to build working relationships and influence people in private, public and voluntary organisations.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject skill (will, from the lead-in 3.14) for the master's award at FHEQ level 7 (SCQF level 11): relationship-building and influencing. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.15.b12. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.15.b8 and 3.10.b9."
  author-agent-dialogue: "Raise this when a student plans their skills development or a team maps skills to modules. Put it in plain words: second person for a student, the course outcome for staff. Ask: Which relationship outside your own organisation would help your work most? Avoid reading paragraph 3.15.b12 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.15.b13
  forPractitioner: { text: "Develop responsible leadership, including recognising the need for change, initiating it and managing it through.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to take on leadership roles responsibly, see when change is needed, start it and manage it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject skill (will, from the lead-in 3.14) for the master's award at FHEQ level 7 (SCQF level 11): leadership and managing change. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.15.b13. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 4.4.b12, 1.10 and qaa/fheq-2024/4.17.b8.2."
  author-agent-dialogue: "Raise this when a student plans their skills development or a team maps skills to modules. Put it in plain words: second person for a student, the course outcome for staff. Ask: What change would you lead first if you had the authority? Avoid reading paragraph 3.15.b13 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.16.b1
  forPractitioner: { text: "Develop inclusive collaboration with stakeholders inside and outside the organisation, with professional integrity.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to work with people inside and outside an organisation inclusively and with integrity.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic skill (will, from the lead-in 3.14), refining the level 7 descriptor for the master's award at FHEQ level 7 (SCQF level 11): collaborative and inclusive working with stakeholders. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.16.b1. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.15.b11 and qaa/fheq-2024/4.17.b8.1."
  author-agent-dialogue: "Raise this when a student reflects on transferable skills or a team maps generic skills. Put it in plain words: second person for a student, the course outcome for staff. Ask: Which outside stakeholder have you worked with, and how did it go? Avoid reading paragraph 3.16.b1 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.16.b2
  forPractitioner: { text: "Develop communication in speech, in non-verbal forms and through digital channels.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to communicate in speech, in other non-verbal ways and online.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic skill (will, from the lead-in 3.14), refining the level 7 descriptor for the master's award at FHEQ level 7 (SCQF level 11): verbal, non-verbal and digital communication. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.16.b2. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.15.b9 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise this when a student reflects on transferable skills or a team maps generic skills. Put it in plain words: second person for a student, the course outcome for staff. Ask: Which form of communication do you find hardest? Avoid reading paragraph 3.16.b2 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.16.b3
  forPractitioner: { text: "Develop digital literacy and appropriate conduct in digital settings.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be confident with digital tools and know how to behave well online.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic skill (will, from the lead-in 3.14), refining the level 7 descriptor for the master's award at FHEQ level 7 (SCQF level 11): digital literacy and etiquette. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.16.b3. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.15.b3 and spine:7."
  author-agent-dialogue: "Raise this when a student reflects on transferable skills or a team maps generic skills. Put it in plain words: second person for a student, the course outcome for staff. Ask: Which digital tool would most improve your work? Avoid reading paragraph 3.16.b3 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.16.b4
  forPractitioner: { text: "Develop conceptual, systems and critical thinking, with analysis, synthesis and evaluation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to think in concepts and systems, think critically, and analyse, combine and judge ideas.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic skill (will, from the lead-in 3.14), refining the level 7 descriptor for the master's award at FHEQ level 7 (SCQF level 11): conceptual, systemic and critical thinking. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.16.b4. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.15.b2 and qaa/fheq-2024/4.17.b4.1."
  author-agent-dialogue: "Raise this when a student reflects on transferable skills or a team maps generic skills. Put it in plain words: second person for a student, the course outcome for staff. Ask: How would you map the system around a problem you face? Avoid reading paragraph 3.16.b4 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.16.b5
  forPractitioner: { text: "Develop the ability to resolve conflict between people and groups.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to help settle disagreements between people.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic skill (will, from the lead-in 3.14), refining the level 7 descriptor for the master's award at FHEQ level 7 (SCQF level 11): conflict resolution. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.16.b5. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.15.b11 and qaa/fheq-2024/4.17.b8.2."
  author-agent-dialogue: "Raise this when a student reflects on transferable skills or a team maps generic skills. Put it in plain words: second person for a student, the course outcome for staff. Ask: How did you handle the last disagreement in a team you were part of? Avoid reading paragraph 3.16.b5 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.16.b6
  forPractitioner: { text: "Develop self-management: responsibility, adaptability, tolerance of uncertainty, resilience, initiative and appropriate assertiveness.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to manage yourself: take responsibility, adapt, cope with uncertainty, bounce back, get started on your own and speak up when needed.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic skill (will, from the lead-in 3.14), refining the level 7 descriptor for the master's award at FHEQ level 7 (SCQF level 11): self-management. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.16.b6. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside qaa/fheq-2024/4.17.b6 and qaa/fheq-2024/4.17.b8.2."
  author-agent-dialogue: "Raise this when a student reflects on transferable skills or a team maps generic skills. Put it in plain words: second person for a student, the course outcome for staff. Ask: How do you respond when a task has no clear answer? Avoid reading paragraph 3.16.b6 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.16.b7
  forPractitioner: { text: "Develop self-reflection, sensitivity to diversity and a lasting commitment to building new skills to a higher level.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reflect on yourself, be aware of differences between people and cultures, and keep taking charge of building your skills further.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic skill (will, from the lead-in 3.14), refining the level 7 descriptor for the master's award at FHEQ level 7 (SCQF level 11): self-reflection. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.16.b7. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.17 and qaa/fheq-2024/4.17.b7."
  author-agent-dialogue: "Raise this when a student reflects on transferable skills or a team maps generic skills. Put it in plain words: second person for a student, the course outcome for staff. Ask: What has reflection on your work changed about how you act? Avoid reading paragraph 3.16.b7 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.16.b8
  forPractitioner: { text: "Develop empathy, understanding of others' needs and sensitivity to diversity and inclusion.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to understand and empathise with what others need and act inclusively in different situations.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic skill (will, from the lead-in 3.14), refining the level 7 descriptor for the master's award at FHEQ level 7 (SCQF level 11): interpersonal skills. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.16.b8. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.15.b1, 1.33 and theme:edi."
  author-agent-dialogue: "Raise this when a student reflects on transferable skills or a team maps generic skills. Put it in plain words: second person for a student, the course outcome for staff. Ask: How do you find out what a colleague needs from you? Avoid reading paragraph 3.16.b8 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.16.b9
  forPractitioner: { text: "Develop the qualities and transferable skills that roles needing initiative and personal responsibility require.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will have the qualities and skills to take initiative and personal responsibility at work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic skill (will, from the lead-in 3.14), refining the level 7 descriptor for the master's award at FHEQ level 7 (SCQF level 11): initiative. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.16.b9. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside qaa/fheq-2024/4.17.b8.1."
  author-agent-dialogue: "Raise this when a student reflects on transferable skills or a team maps generic skills. Put it in plain words: second person for a student, the course outcome for staff. Ask: When did you last act without being asked, and what happened? Avoid reading paragraph 3.16.b9 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.16.b10
  forPractitioner: { text: "Develop independent learning for continuing professional development and the ability to plan and run projects alone at professional level.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to keep learning on your own throughout your career and plan and run projects independently at a professional level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic skill (will, from the lead-in 3.14), refining the level 7 descriptor for the master's award at FHEQ level 7 (SCQF level 11): independent learning. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.16.b10. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside qaa/fheq-2024/4.17.b8.3 and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Raise this when a student reflects on transferable skills or a team maps generic skills. Put it in plain words: second person for a student, the course outcome for staff. Ask: How will you keep learning after the course ends? Avoid reading paragraph 3.16.b10 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.17
  forPractitioner: { text: "On career-development courses, build in reflection on prior experience so that students combine it with new knowledge, apply it in new settings and extend their skills.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reflect on your past experience, combine it with what you learn now, use it in new situations and build both new and existing skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) for Types 2 and 4 for the master's award at FHEQ level 7 (SCQF level 11): reflection on and learning from prior experience. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.17. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.12, 3.28, 3.16.b7 and qaa/fheq-2024/4.17.b7."
  author-agent-dialogue: "Raise this when an experienced student sets goals for the course. Put it in plain words: second person for a student, the course outcome for staff. Ask: What from your past work do you want to test against new ideas? Avoid reading paragraph 3.17 aloud at length or treating the course types as fixed boxes."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.23
  forPractitioner: { text: "Plan assessment as part of learning and return feedback on both formative and summative work quickly enough, and specifically enough, for students to act on it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) on assessment for the master's award at FHEQ level 7 (SCQF level 11): assessment supports learning through timely, actionable feedback. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.23. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.24, 3.31 and 3.32."
  author-agent-dialogue: "Raise this with a programme team or teacher when feedback timing or quality is discussed; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: Can students use the feedback on one task before they submit the next? Avoid quoting paragraph 3.23 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.29
  forPractitioner: { text: "Decide deliberately how much assessment is group-based, whether the task suits a group, and how group and individual marks are balanced.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) on assessment for the master's award at FHEQ level 7 (SCQF level 11): group assessment is weighed for extent, authenticity, fit and marking. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.29. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.15.b11 (teamwork), 3.27 and 3.30."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team plans group assessment; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: How will one student's mark reflect their own contribution to the group? Avoid quoting paragraph 3.29 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.30
  forPractitioner: { text: "When using peer assessment, brief students clearly and cap how much it counts in the module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) on assessment for the master's award at FHEQ level 7 (SCQF level 11): clear guidance and capped weighting for peer assessment. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.30. Do not claim that it fixes a particular weighting. Set it beside 3.29 and 3.31."
  author-agent-dialogue: "Raise this with a programme team or teacher when peer marking is proposed; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: What guidance will students get, and what share of the mark will peers decide? Avoid quoting paragraph 3.30 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.31
  forPractitioner: { text: "Publish assessment details and marking criteria to students, and consider letting students help design assessments.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) with a permissive option (may) for the master's award at FHEQ level 7 (SCQF level 11): transparent assessment details and criteria; optional co-design. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.31. Do not claim that co-design is required. Set it beside 3.23 and 3.30."
  author-agent-dialogue: "Raise this with a programme team or teacher when assessment briefs are prepared; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: Do students see the marking criteria when they start the task? Avoid quoting paragraph 3.31 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/3.32
  forPractitioner: { text: "Check the total assessment load on students when designing assessment, across modules as well as within them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) on assessment for the master's award at FHEQ level 7 (SCQF level 11): assessment design takes account of student workload. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 3.32. Do not claim that it is a regulatory requirement or that it holds below level 7. Set it beside 3.23 and 3.25."
  author-agent-dialogue: "Raise this with a programme team or teacher when deadlines cluster or a module adds tasks; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: How many assessments fall due in the same fortnight? Avoid quoting paragraph 3.32 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/4.2
  forPractitioner: { text: "Use the frameworks' master's descriptor when deciding what evidence shows achievement above the threshold, and treat these standards as a reference for postgraduate certificates and diplomas too.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) on standards above the threshold for the master's award at FHEQ level 7 (SCQF level 11): each provider sets the evidence for achievement beyond the minimum, with reference to the frameworks. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 4.2. Do not claim that the statement grades achievement above the threshold. Set it beside 4.1, 4.4 and the level 7 descriptor qaa/fheq-2024/4.17.b1 to qaa/fheq-2024/4.17.b8.3."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team discusses merit and distinction criteria; it is a course duty, so never hand it to a student as a target. Frame it in plain words as a design or review question. Ask: How do your merit and distinction criteria go beyond the threshold list in 4.4? Avoid quoting paragraph 4.2 at length or calling it a legal rule."
- statement: qaa/masters-degrees-in-business-and-management-2023/4.4.b1
  forPractitioner: { text: "At threshold, every graduate has shown systematic, deep understanding of organisations, their context and management, and of how these connect and apply in practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for the award, you will have shown a thorough, organised understanding of organisations, the world around them, how they are run and how all this applies in practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum every holder of the master's award at FHEQ level 7 (SCQF level 11) has shown, here systematic, deep understanding of organisations and their management. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 4.4 (item 1 of 12). Do not present it as typical or excellent performance, and do not claim it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b1, the factor in 4.3 it falls under and spine:7."
  author-agent-dialogue: "Raise this when someone asks what passing the master's requires, in particular on systematic, deep understanding of organisations and their management. Put it plainly as the floor, not the goal: second person for a student, the minimum outcome for staff. Ask: Can you explain how an organisation's context shapes the way it is run? Avoid reading 4.4 aloud at length or implying that meeting it earns a merit or distinction."
- statement: qaa/masters-degrees-in-business-and-management-2023/4.4.b2
  forPractitioner: { text: "At threshold, every graduate has shown comprehensive understanding of techniques for detailed investigation, research or advanced scholarship in the field or a specialism.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for the award, you will have shown that you understand the methods needed to investigate and research business and management questions in detail.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum every holder of the master's award at FHEQ level 7 (SCQF level 11) has shown, here understanding of techniques for investigation and research. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 4.4 (item 2 of 12). Do not present it as typical or excellent performance, and do not claim it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b2, the factor in 4.3 it falls under and spine:7."
  author-agent-dialogue: "Raise this when someone asks what passing the master's requires, in particular on understanding of techniques for investigation and research. Put it plainly as the floor, not the goal: second person for a student, the minimum outcome for staff. Ask: Which research method would suit the question you want to investigate, and why? Avoid reading 4.4 aloud at length or implying that meeting it earns a merit or distinction."
- statement: qaa/masters-degrees-in-business-and-management-2023/4.4.b3
  forPractitioner: { text: "At threshold, every graduate has shown a high command of subject-specific academic and professional skills and consistent proficiency in generic skills (see 3.15 and 3.16).", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for the award, you will have shown a strong command of the academic and professional skills of your field and steady ability in wider, transferable skills.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum every holder of the master's award at FHEQ level 7 (SCQF level 11) has shown, here command of subject and professional skills, with generic skills. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 4.4 (item 3 of 12). Do not present it as typical or excellent performance, and do not claim it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b7, 3.15 and 3.16, the factor in 4.3 it falls under and spine:7."
  author-agent-dialogue: "Raise this when someone asks what passing the master's requires, in particular on command of subject and professional skills, with generic skills. Put it plainly as the floor, not the goal: second person for a student, the minimum outcome for staff. Ask: Which subject skill and which general skill can you show most clearly? Avoid reading 4.4 aloud at length or implying that meeting it earns a merit or distinction."
- statement: qaa/masters-degrees-in-business-and-management-2023/4.4.b4
  forPractitioner: { text: "At threshold, every graduate has shown critical awareness of current issues, informed by leading research and practice and by their own proactive, independent learning.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for the award, you will have shown that you can think critically about current issues in business and management, drawing on leading research and practice and your own independent study.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum every holder of the master's award at FHEQ level 7 (SCQF level 11) has shown, here critical awareness of current issues. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 4.4 (item 4 of 12). Do not present it as typical or excellent performance, and do not claim it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b1, the factor in 4.3 it falls under and spine:7."
  author-agent-dialogue: "Raise this when someone asks what passing the master's requires, in particular on critical awareness of current issues. Put it plainly as the floor, not the goal: second person for a student, the minimum outcome for staff. Ask: Which current issue in your field could you discuss with evidence from recent research? Avoid reading 4.4 aloud at length or implying that meeting it earns a merit or distinction."
- statement: qaa/masters-degrees-in-business-and-management-2023/4.4.b5
  forPractitioner: { text: "At threshold, every graduate has shown the conceptual understanding needed to evaluate current research and advanced scholarship critically.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for the award, you will have shown that you understand the ideas well enough to judge current research and scholarship in your field critically.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum every holder of the master's award at FHEQ level 7 (SCQF level 11) has shown, here critical evaluation of current research and scholarship. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 4.4 (item 5 of 12). Do not present it as typical or excellent performance, and do not claim it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b4.1, the factor in 4.3 it falls under and spine:7."
  author-agent-dialogue: "Raise this when someone asks what passing the master's requires, in particular on critical evaluation of current research and scholarship. Put it plainly as the floor, not the goal: second person for a student, the minimum outcome for staff. Ask: How would you judge the strength of a recent study in your area? Avoid reading 4.4 aloud at length or implying that meeting it earns a merit or distinction."
- statement: qaa/masters-degrees-in-business-and-management-2023/4.4.b6
  forPractitioner: { text: "At threshold, every graduate has applied relevant knowledge to varied complex situations while accounting for links with other parts of the organisation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for the award, you will have shown that you can use what you know in complex situations, taking account of how one part of an organisation affects the others.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum every holder of the master's award at FHEQ level 7 (SCQF level 11) has shown, here applying knowledge to complex situations. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 4.4 (item 6 of 12). Do not present it as typical or excellent performance, and do not claim it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b5, the factor in 4.3 it falls under and spine:7."
  author-agent-dialogue: "Raise this when someone asks what passing the master's requires, in particular on applying knowledge to complex situations. Put it plainly as the floor, not the goal: second person for a student, the minimum outcome for staff. Ask: Where have you applied what you learned to a complex situation, and what else did it affect? Avoid reading 4.4 aloud at length or implying that meeting it earns a merit or distinction."
- statement: qaa/masters-degrees-in-business-and-management-2023/4.4.b7
  forPractitioner: { text: "At threshold, every graduate has applied knowledge with originality and creativity and understands in practice how established research techniques create and interpret knowledge.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for the award, you will have shown original, creative use of what you know and a practical understanding of how research creates and makes sense of knowledge in your field.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum every holder of the master's award at FHEQ level 7 (SCQF level 11) has shown, here originality in applying knowledge and research practice. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 4.4 (item 7 of 12). Do not present it as typical or excellent performance, and do not claim it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b3, the factor in 4.3 it falls under and spine:7."
  author-agent-dialogue: "Raise this when someone asks what passing the master's requires, in particular on originality in applying knowledge and research practice. Put it plainly as the floor, not the goal: second person for a student, the minimum outcome for staff. Ask: What is original about the way you applied an idea in your recent work? Avoid reading 4.4 aloud at length or implying that meeting it earns a merit or distinction."
- statement: qaa/masters-degrees-in-business-and-management-2023/4.4.b8
  forPractitioner: { text: "At threshold, every graduate has evaluated and integrated theory and practice across a wide range of situations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for the award, you will have shown that you can weigh up theory and practice and bring them together in many different situations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum every holder of the master's award at FHEQ level 7 (SCQF level 11) has shown, here evaluating and joining theory and practice. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 4.4 (item 8 of 12). Do not present it as typical or excellent performance, and do not claim it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b5, the factor in 4.3 it falls under and spine:7."
  author-agent-dialogue: "Raise this when someone asks what passing the master's requires, in particular on evaluating and joining theory and practice. Put it plainly as the floor, not the goal: second person for a student, the minimum outcome for staff. Ask: Which theory has held up, or failed, when you tested it against practice? Avoid reading 4.4 aloud at length or implying that meeting it earns a merit or distinction."
- statement: qaa/masters-degrees-in-business-and-management-2023/4.4.b9
  forPractitioner: { text: "At threshold, every graduate has shown understanding of how research extends the boundaries of knowledge.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for the award, you will have shown that you understand how research moves knowledge forward.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum every holder of the master's award at FHEQ level 7 (SCQF level 11) has shown, here how research advances knowledge. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 4.4 (item 9 of 12). Do not present it as typical or excellent performance, and do not claim it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b3, the factor in 4.3 it falls under and spine:7."
  author-agent-dialogue: "Raise this when someone asks what passing the master's requires, in particular on how research advances knowledge. Put it plainly as the floor, not the goal: second person for a student, the minimum outcome for staff. Ask: How has a piece of research changed what is known in your field? Avoid reading 4.4 aloud at length or implying that meeting it earns a merit or distinction."
- statement: qaa/masters-degrees-in-business-and-management-2023/4.4.b10
  forPractitioner: { text: "At threshold, every graduate has shown a commitment to global social responsibility and ethical values and has acted with integrity.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for the award, you will have shown that you are committed to social responsibility worldwide, to ethical values and to acting with integrity.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum every holder of the master's award at FHEQ level 7 (SCQF level 11) has shown, here commitment to global social responsibility and integrity. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 4.4 (item 10 of 12). Do not present it as typical or excellent performance, and do not claim it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b8.1, the factor in 4.3 it falls under and spine:7."
  author-agent-dialogue: "Raise this when someone asks what passing the master's requires, in particular on commitment to global social responsibility and integrity. Put it plainly as the floor, not the goal: second person for a student, the minimum outcome for staff. Ask: Where have your values shaped a decision you made in your studies or work? Avoid reading 4.4 aloud at length or implying that meeting it earns a merit or distinction."
- statement: qaa/masters-degrees-in-business-and-management-2023/4.4.b11
  forPractitioner: { text: "At threshold, every graduate has shown an international perspective, understanding how globalisation affects organisations, societies and the environment, with its ethical implications.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for the award, you will have shown that you can take an international view, including how globalisation affects business, society and the environment and what that means ethically.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum every holder of the master's award at FHEQ level 7 (SCQF level 11) has shown, here an international perspective on globalisation. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 4.4 (item 11 of 12). Do not present it as typical or excellent performance, and do not claim it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b5, the factor in 4.3 it falls under and spine:7."
  author-agent-dialogue: "Raise this when someone asks what passing the master's requires, in particular on an international perspective on globalisation. Put it plainly as the floor, not the goal: second person for a student, the minimum outcome for staff. Ask: How does globalisation affect an organisation you know, for better and worse? Avoid reading 4.4 aloud at length or implying that meeting it earns a merit or distinction."
- statement: qaa/masters-degrees-in-business-and-management-2023/4.4.b12
  forPractitioner: { text: "At threshold, every graduate has shown they can lead and manage with a firm sense of worldwide social responsibility, recognising the tensions it creates in complex environments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for the award, you will have shown that you can manage and lead with a strong sense of social responsibility, aware of the tensions this creates in complex settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum every holder of the master's award at FHEQ level 7 (SCQF level 11) has shown, here managing and leading with global social responsibility. Cite it as QAA (2023), Business and Management master's Subject Benchmark Statement, para 4.4 (item 12 of 12). Do not present it as typical or excellent performance, and do not claim it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b8.2, the factor in 4.3 it falls under and spine:7."
  author-agent-dialogue: "Raise this when someone asks what passing the master's requires, in particular on managing and leading with global social responsibility. Put it plainly as the floor, not the goal: second person for a student, the minimum outcome for staff. Ask: When might acting responsibly conflict with a business target, and how would you lead through it? Avoid reading 4.4 aloud at length or implying that meeting it earns a merit or distinction."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:7", role: "cites", locator: "D1, 1.2; 1.6; 2.8; 2.9; 2.10; 3.1; 4.2", descriptor: "std:doc:qaa-fheq-2024-framework, qaa/fheq-2024/4.17.*" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 1.2; 1.6; 2.8; 2.10; 3.1; 4.2", descriptor: "std:doc:qaa-fqheis-2024-framework (shares the FHEQ 4.17 descriptor)" }
  - { id: "fheq:6", role: "cites", locator: "D1, 1.6 (integrated master's combine levels 6 and 7)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 1.6 (integrated master's combine levels 10 and 11)" }
  - { id: "spine:7", role: "refers", locator: "std:ref:uk-framework R2 and R8; inferred (Part E)" }
crosswalks:
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 1.2; 2.8; 4.2)" }
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 1.6)" }
  - { from: "fheq:7", to: "spine:7", relation: "sits-at", basis: "inferred from std:ref:uk-framework R2 (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.19", "1.31", "1.32", "1.33", "1.34", "1.35", "1.36", "1.37", "2.5", "2.13", "2.19", "2.22", "3.10", "3.15", "3.16", "3.20", "3.24"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.35", "1.36", "1.38", "1.39", "1.40", "2.13", "2.14"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.10", "1.19", "1.33", "1.41", "1.42", "1.43", "1.44", "1.49", "2.5", "3.2", "3.4", "3.10"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.11", "1.19", "1.45", "1.46", "1.47", "1.48", "1.49", "3.10", "3.15", "3.19"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "the master's descriptor, FHEQ level 7 (4.17); cited in 1.6, 1.7, 2.8, 3.1, 4.2 (the statement cites the 2014 edition)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "SCQF level 11, sharing the FHEQ 4.17 descriptor" }
- { rel: "cites", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "ESD guidance and its learning outcomes (1.41, 1.44)" }
- { rel: "cites", target: "std:doc:qaa-enterprise-2018-guidance", note: "enterprise behaviours, attributes and competencies (1.48)" }
- { rel: "thresholdAt", target: "std:ref:uk-framework", note: "the threshold standards sit at spine:7; inferred" }
- { rel: "relatedTo", target: "std:doc:qaa-business-and-management-2023-benchmarks", note: "the bachelor's statement for the same subject, same year; inferred, not cited in the text" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2023-03"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "none-stated"
replacedBy: "none"
edition: "fourth edition, published 8 March 2023 (D1, back matter)"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- Taught master's in the subject vary widely in content, in how many disciplines they draw on and in the perspectives they take, and are often fast-paced, broad or specialist (D1, 1.15)
- Every course joins theory to the consideration of practice, with theory preparing students to tackle complex issues and act on opportunities (D1, 1.16)
- A capstone project, from a dissertation to a consultancy project or white paper, is a defining feature, with methods training to prepare for it (D1, 1.17)
- The discipline changes quickly, and course design and delivery are to follow that change (D1, 1.18)
- Courses fall into four types by content (generalist or specialist) and by career stage (entry or development), and a title alone does not fix the type (D1, 1.3; 1.4; 1.20 to 1.30)
- Courses are interdisciplinary, drawing on social sciences, humanities and sciences, and are designed to join subject knowledge to responsible, effective working (D1, 2.1 to 2.3)
- Responsible management, sustainability and inclusion are designed into courses, which cover private, public and non-profit organisations (D1, 2.5; 2.6)
- The subject is closely tied to practice and to employability, with skills developed for and assessed through practice (D1, 3.13; 3.22)

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "Inclusion is framed by why, what and how the subject is taught: future managers and leaders carry EDI into organisations, content draws on diverse and critical perspectives, and teaching, modes and assessment are inclusive (D1, 1.31 to 1.37)"
  statements: ["qaa/masters-degrees-in-business-and-management-2023/1.31", "qaa/masters-degrees-in-business-and-management-2023/1.33", "qaa/masters-degrees-in-business-and-management-2023/1.34", "qaa/masters-degrees-in-business-and-management-2023/1.35", "qaa/masters-degrees-in-business-and-management-2023/1.37", "qaa/masters-degrees-in-business-and-management-2023/2.13", "qaa/masters-degrees-in-business-and-management-2023/2.19", "qaa/masters-degrees-in-business-and-management-2023/3.10.b5", "qaa/masters-degrees-in-business-and-management-2023/3.15.b1", "qaa/masters-degrees-in-business-and-management-2023/3.16.b7", "qaa/masters-degrees-in-business-and-management-2023/3.16.b8"]
- theme: theme:accessibility
  inThisSubject: "Accessibility runs from pre-application to after graduation, at least to the regulatory minimum, with barriers designed out and equal access to placements, international and digital learning (D1, 1.38 to 1.40)"
  statements: ["qaa/masters-degrees-in-business-and-management-2023/1.38", "qaa/masters-degrees-in-business-and-management-2023/1.39", "qaa/masters-degrees-in-business-and-management-2023/1.40", "qaa/masters-degrees-in-business-and-management-2023/2.13"]
- theme: theme:esd
  inThisSubject: "Sustainable management, carbon literacy and responsible leadership are built into every functional area, drawing on the SDGs and PRME, with ethics, responsibility and sustainability as a knowledge area (D1, 1.41 to 1.44; 3.10)"
  statements: ["qaa/masters-degrees-in-business-and-management-2023/1.42", "qaa/masters-degrees-in-business-and-management-2023/3.2", "qaa/masters-degrees-in-business-and-management-2023/3.10.b1"]
- theme: theme:enterprise
  inThisSubject: "Enterprise and entrepreneurship education, joined to employability, builds entrepreneurial mindsets for new ventures and innovation in existing organisations, through theory and experiential learning (D1, 1.45 to 1.49; 3.10; 3.15)"
  statements: ["qaa/masters-degrees-in-business-and-management-2023/3.10.b10", "qaa/masters-degrees-in-business-and-management-2023/3.15.b5"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.4", gloss: "the business environment, local to global, and its effects on organisations" }
  - { component: "3.5", gloss: "organisations: functions, structures, governance, behaviour and culture" }
  - { component: "3.6", gloss: "responsible leadership and management, theory and ethical decision-making" }
  - { component: "3.10", gloss: "ten knowledge areas for generalist courses, plus the MPA focus" }
  - { component: "3.11", gloss: "specialist knowledge, current issues and applied perspectives" }
practices:
  - { component: "3.18", kind: "teaching", gloss: "diverse methods; research methods training in most courses" }
  - { component: "3.19", kind: "teaching", gloss: "practitioners and stakeholders in teaching and co-creation" }
  - { component: "3.20", kind: "learning", gloss: "inclusive modes and a range of learning activities" }
  - { component: "3.21", kind: "teaching", gloss: "teaching adapted to course type" }
  - { component: "3.22", kind: "assessment", gloss: "skills development embedded and formally assessed" }
  - { component: "3.23", kind: "assessment", gloss: "assessment for learning; timely feedback" }
  - { component: "3.24", kind: "assessment", gloss: "inclusive assessment design" }
  - { component: "3.25", kind: "assessment", gloss: "typical assessment methods, capstone included" }
  - { component: "3.26", kind: "assessment", gloss: "online, in situ and other settings" }
  - { component: "3.27", kind: "assessment", gloss: "authentic assessment and integrity" }
  - { component: "3.28", kind: "assessment", gloss: "reflective assessment on post-experience courses" }
  - { component: "3.29", kind: "assessment", gloss: "group work and its marks" }
  - { component: "3.30", kind: "assessment", gloss: "peer assessment guidance and weighting" }
  - { component: "3.31", kind: "assessment", gloss: "transparent criteria; co-designed assessment" }
  - { component: "3.32", kind: "assessment", gloss: "assessment workload" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.4", award: "master's", items: 12 }
rungBases: "4.1 defines the 4.4 list as the minimum threshold for the award; no typical or excellent rung is stated; 4.2 says many students will exceed the threshold and leaves the evidence for that to each provider with reference to the frameworks"
outcomeLists:
  - { leadIn: "3.10", gloss: "knowledge areas for generalist courses (will typically gain)", items: 10, award: ["master's"] }
  - { leadIn: "3.11", gloss: "added knowledge for specialist courses (will also acquire)", items: 3, award: ["master's"] }
  - { leadIn: "3.14", gloss: "subject skills listed in 3.15 (force from 3.14)", items: 13, award: ["master's"] }
  - { leadIn: "3.14", gloss: "generic skills listed in 3.16 (force from 3.14)", items: 10, award: ["master's"] }
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
- { body: "Chartered Management Institute (CMI)", says: "some courses give advanced standing towards its management and leadership qualifications (D1, 2.11)", requirements: "not yet ingested (Part E)" }
- { body: "Chartered Institute of Personnel and Development (CIPD)", says: "specialist post-experience courses often link to its qualifications, and some give accelerated progression to them (D1, 1.29; 2.11)", requirements: "not yet ingested (Part E)" }
- { body: "Chartered Institute of Marketing", says: "an example of a professional body whose qualifications Type 4 courses often link to (D1, 1.29)", requirements: "not yet ingested (Part E)" }
- { body: "International Commission on the Accreditation of Public Administration and Training (ICAPA)", says: "an academic accreditor an MPA may be accredited by (D1, 1.25)", requirements: "not yet ingested (Part E)" }
- { body: "European Association for Public Administration Accreditation (EAPAA)", says: "an academic accreditor an MPA may be accredited by (D1, 1.25)", requirements: "not yet ingested (Part E)" }
- { body: "Network of Schools of Public Policy, Affairs and Administration (NASPA, as the text names it)", says: "an academic accreditor an MPA may be accredited by (D1, 1.25)", requirements: "not yet ingested (Part E)" }
- { body: "professional, statutory and regulatory bodies (PSRBs) in general", says: "courses may reflect PSRB recognition requirements, which can help learners apply management skills and plan development; vocational courses may need PSRB evaluation and accreditation (D1, 1.14; 2.17; 2.23; front matter)", requirements: "not yet ingested (Part E)" }
- { body: "accrediting bodies (unnamed)", says: "some expect ethics, responsibility and sustainability to be integrated into business school curricula (D1, 1.41)", requirements: "not yet ingested (Part E)" }
- { body: "UN Principles for Responsible Management Education (PRME)", says: "courses can draw on it to build students' capacity to create sustainable value (D1, 1.41)", requirements: "not yet ingested (Part E)" }
- { body: "European Quality Link (EQUAL)", says: "its MBA guidelines are among the documents the statement was written to relate to (D1, 1.7)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.19", "1.31", "1.32", "1.33", "1.34", "1.35", "1.36", "1.37", "2.5", "2.13", "2.19", "2.22", "3.10", "3.15", "3.16", "3.20", "3.24"], statements: ["1.31", "1.33", "1.34", "1.35", "1.37", "2.13", "2.19", "3.10.b5", "3.15.b1", "3.16.b7", "3.16.b8"] }
  - { id: "theme:accessibility", named: "Accessibility", carriedIn: ["1.35", "1.36", "1.38", "1.39", "1.40", "2.13", "2.14"], statements: ["1.38", "1.39", "1.40", "2.13"] }
  - { id: "theme:esd", named: "Education for Sustainable Development", carriedIn: ["1.10", "1.19", "1.33", "1.41", "1.42", "1.43", "1.44", "1.49", "2.5", "3.2", "3.4", "3.10"], statements: ["1.42", "3.2", "3.10.b1"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (with employability in the front matter)", carriedIn: ["1.11", "1.19", "1.45", "1.46", "1.47", "1.48", "1.49", "3.10", "3.15", "3.19"], statements: ["3.10.b10", "3.15.b5"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:7", "fheq:6"], citedIn: ["1.2", "1.5", "1.6", "2.8", "2.9", "2.10", "3.1", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:11", "fqheis:10"], citedIn: ["1.2", "1.5", "1.6", "2.8", "2.10", "3.1", "4.2"] }
bodies:
  - { body: "Chartered Management Institute (CMI)", citedIn: ["2.11"] }
  - { body: "Chartered Institute of Personnel and Development (CIPD)", citedIn: ["1.29", "2.11"] }
  - { body: "Chartered Institute of Marketing", citedIn: ["1.29"] }
  - { body: "ICAPA", citedIn: ["1.25"] }
  - { body: "EAPAA", citedIn: ["1.25"] }
  - { body: "NASPA (as named)", citedIn: ["1.25"] }
  - { body: "PSRBs in general", citedIn: ["1.14", "2.17", "2.23"] }
  - { body: "accrediting bodies (unnamed)", citedIn: ["1.41", "3.26"] }
  - { body: "UN PRME", citedIn: ["1.41"] }
  - { body: "European Quality Link (EQUAL)", citedIn: ["1.7"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework", named: "Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies (the references list the 2014 edition)", citedIn: ["1.6", "1.7", "2.8", "3.1", "4.2"], role: "the level 7 master's descriptor and qualification lengths" }
  - { document: "not yet ingested: QAA Characteristics Statement: Master's Degree (2020), listed in Part E", named: "Characteristics Statement: Master's Degree(s)", citedIn: ["1.4", "1.7", "1.8", "2.8"], role: "award titles, purposes and lengths of master's" }
  - { document: "not yet ingested: QAA Characteristics Statement: Micro-credentials (2022), listed in Part E", named: "Characteristics Statement: Micro-Credentials", citedIn: ["2.11"], role: "level 7 microcredits" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA and Advance HE's Education for Sustainable Development Guidance, 2021", citedIn: ["1.41", "1.44"], role: "sustainability competencies and learning outcomes" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "enterprise behaviours, attributes and competencies (as defined by QAA, 2018)", citedIn: ["1.48"], role: "enterprise competencies reflected in subject skills" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "organisations", definition: "Read broadly: public, private, non-profit and social enterprises of every size and structure, from start-ups and micro businesses to global firms; business likewise is read broadly (D1, 1.9)", beneficiaryDefinition: "Any kind of organisation you might work in, from a start-up or charity to a public body or a global company.", scopeNote: "applies throughout the statement", category: "unknown", practices: ["business and management"] }
- { slug: "responsible-leadership", definition: "Leadership that is authentic, driven by values, inclusive, ethical, sustainable, systemic and transformative, weighing stakeholders now and in future and addressing climate change and fair, inclusive net zero (D1, 1.10)", beneficiaryDefinition: "Leading in a way that is ethical, inclusive and sustainable, and that thinks about everyone affected, now and later.", scopeNote: "used in 1.8, 3.6, 3.10 and 4.4", category: "unknown", practices: ["business and management"] }
- { slug: "career-preparation-and-development", definition: "Building professional-level knowledge and skills, or preparing for research and further study, with self-awareness, personal development and a positive stance on change and enterprise (D1, 1.11)", beneficiaryDefinition: "Getting ready for, or moving on in, a business career, or preparing for research.", scopeNote: "one of the purposes in 1.8", category: "unknown", practices: ["business and management"] }
- { slug: "skills-and-attributes", definition: "Transferable academic and professional skills suited to a business career but not limited to it, with continuing reflection, self-awareness, lifelong learning and regard for others' well-being (D1, 1.12)", beneficiaryDefinition: "The skills and qualities you build that are useful in business and beyond it.", scopeNote: "one of the purposes in 1.8", category: "unknown", practices: ["business and management"] }
- { slug: "course-typology", definition: "Four course types: Type 1 generalist for career entry, Type 2 generalist for career development (MBA, MPA), Type 3 specialist for career entry, Type 4 specialist for career development (D1, 1.3; 1.20 to 1.30)", beneficiaryDefinition: "Whether a course is broad or specialist, and whether it is for people starting a career or already working.", scopeNote: "the statement treats the types as guidance, not strict categories (1.1)", category: "unknown", practices: ["business and management"] }
- { slug: "capstone-project", definition: "A substantial final piece of independent work involving research, such as a dissertation, thesis, consultancy project, white paper or business project (D1, 1.17)", beneficiaryDefinition: "A large final project of your own, such as a dissertation or a consultancy report.", scopeNote: "a characteristic of the taught master's", category: "unknown", practices: ["business and management"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "organisations", form: "'Organisations'", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "responsible-leadership", form: "'responsible leadership'", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "career-preparation-and-development", form: "'Preparation for, and/or further development of, a career in business and management'", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "skills-and-attributes", form: "'Skills and attributes'", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "course-typology", form: "Type 1 to Type 4", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "capstone-project", form: "capstone project", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Master's Degrees in Business and Management"
  edition: "March 2023 (fourth edition)"
  year: 2023
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/masters-degrees-in-business-and-management-2023/masters-degrees-in-business-and-management-2023.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 7be2e11f74450418fbfd682e923df45e06b4528ec2b7205fc26a6eda34122777
  heldFiles: ["wkspc2601-library/txt/qaa-2023-masters-degrees-business-management-subject-benchmark-standard.txt", "wkspc2601-library/txt/qaa-2023-masters-degrees-business-management-subject-benchmark-standard.norm.txt", "wkspc2601-library/records/qaa-2023-masters-degrees-business-management-subject-benchmark-standard.chunks.json", "wkspc2601-library/records/qaa-2023-masters-degrees-business-management-subject-benchmark-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0026", source: "QAA (2020) Characteristics Statement: Master's Degree", why: "cited for award titles, purposes and length (1.4; 1.7; 1.8; 2.8)" }
- { w: "W-std-0038", source: "QAA (2022) Characteristics Statement: Micro-credentials", why: "cited for level 7 microcredits (2.11)" }
- { w: "W-std-0079", source: "European Quality Link (2014) Equal MBA Guidelines", why: "cited as a document the statement relates to (1.7)" }
```

## Part E Gaps and questions
- Master's only: the whole statement is at FHEQ level 7 and SCQF level 11; every learner statement carries award "master's" and level fheq:7 (no `.masters` suffix, since no bachelor's standards are present). Differs from Psychology.
- Rungs: one only. 4.4 is the threshold list, defined by 4.1 as the minimum ("minimum threshold standards that a student will have demonstrated"); no typical or excellent rung; 4.2 leaves achievement above the threshold to each provider. The skeleton counted no rungs. Force recorded as `threshold`, forceFrom 4.1. No gradeOf links.
- Rung lead-in wording: "On graduating with a master's degrees in the Business and Management field, students will have demonstrated:" with five sub-headings (Knowledge and understanding; Skills; Critical perspective; Application; Values) run into the list in the held text. A new lead-in shape.
- Skeleton cuts corrected by `find`: 4.4.b2, 4.4.b3, 4.4.b5 and 4.4.b9 carried the next sub-heading at their end; 3.10.b11 and 3.11.b3 carried the next typology heading. The spans now end at the item.
- Threshold item 4.4.b3 uses the word "excellent" ("An excellent command of ..."): this is the threshold rung, not the excellent rung (P3 to confirm).
- The 4.4 items follow the FHEQ master's descriptor closely (4.4.b2 with qaa/fheq-2024/4.17.b2; 4.4.b5 with 4.17.b4.1; 4.4.b7 and 4.4.b9 with 4.17.b3); the pointers in each author-agent-written instruction are inferred.
- 4.3 ("factors that distinguish a master's level of achievement can be articulated in the demonstration of") is read as a framing list naming the five dimensions of 4.4, not as statements; P3 to confirm.
- Skill lists 3.15 ("Skills particular to ... include the following") and 3.16 ("Other generic skills and attributes include") have no modal of their own; they are recorded as outcome statements with force will from the lead-in 3.14 ("Graduates ... will be able to demonstrate a range of ... competencies specific to business and management"), forceFrom 3.14. An inference for P3.
- Outcome lists 3.10 and 3.11 are typical ("will typically gain ... in some of the following areas"): no course need cover every area. Recorded as force will, rung none.
- Definitional "should" in 1.9 to 1.12 ("should be understood", "should be taken to mean", "should incorporate") read as definitions for Part B, not statements.
- Obliging words outside the five, recorded as `describes` or not as statements: 1.42 "needs to be integrated" and "It is therefore imperative" (recorded, force describes); 3.20 and 3.25 "need to" (not statements, provider norms); 1.24 "are expected to" (MBA differences; the record takes the paragraph's "should"); 1.41 "There is an expectation by some accrediting bodies" (description of others' expectations); 1.32, 3.24 "It is important that" (not statements).
- Plain-present provider norms not recorded as statements (template open point 5): 1.8 purposes list; 1.13 purposes by type (with descriptive "will include" and "will also instil" about course purposes); 1.17 capstone ("It will involve independent research"); 1.30 Type 4 ("will normally require", "will have an emphasis on practice"); 1.36 examples ("could consider"); 2.1 to 2.7 design; 2.14 ("there may need to be"); 2.16 partnerships; 2.21 external examiners; 3.18 to 3.22; 3.25 methods; 3.28 ("will be determined"). Abbott's P3 decides.
- Provider expectations with "will" recorded as statements: 2.20 (external reviewers), 3.1 (course scope), 3.7 (learning outcomes), 3.10.b11 (MPA focus). P3 to confirm they count.
- 1.34 records one paragraph with two addressees (postgraduates should be aware ...; courses should ensure ...): addressee both.
- Themes: the front matter names four cross-cutting themes, the fourth as "employability, entrepreneurship and enterprise education"; recorded under theme:enterprise, with employability not given its own id (a new id would go here). Employability also appears in 1.8, 1.21, 2.4, 2.22, 3.13, 3.27.
- No generative AI section and no mention of artificial intelligence.
- Annex D (degree classification descriptions) is not cited: the statement is at master's level and has no honours classes. The skeleton's doc:annex-d hits were empty.
- CQFW not cited; Wales appears only in the front matter (Quality Assessment Framework for Wales). SCQF is cited as "SCQF Level 11 on the FQHEIS".
- The statement cites the Frameworks in the 2014 edition (references list) and refers to "Section 4.17" for the level 7 descriptor; it is linked to the 2024 ingested edition, where 4.17 is the same descriptor. Inferred.
- S5 spine:7 and S7 thresholdAt std:ref:uk-framework are inferred from the reference framework (R2).
- S7 relatedTo std:doc:qaa-business-and-management-2023-benchmarks (the bachelor's statement) is inferred; the text does not cite it.
- Inferred subject codes, held back from lookup until P3: hecos 100089 management studies, hecos 100079 business studies, hecos 100088 leadership, hecos 100090 public administration (from the MPA in 1.25 and 3.10.b9).
- Bodies not yet ingested: CMI, CIPD, Chartered Institute of Marketing, ICAPA, EAPAA, NASPA (named so in 1.25; recall suggests NASPAA, to check), PRME, EQUAL. The references list (excluded matter) also names AACSB, CABS and EFMD, not in the body of the text.
- Shared documents not yet ingested: QAA Characteristics Statement: Master's Degree (2020) and Characteristics Statement: Micro-credentials (2022) (D3). The front matter also names QAA's Advice and Guidance and Glossary (excluded matter).
- Section order differs from Psychology: a long typology of four course types (1.20 to 1.30) and a section 2 on distinctive features (design, progression, flexibility, partnership, monitoring and review).
- Typing slips in the held text kept as found in `source`: "heathcare" (1.2), "a master's degrees" (4.4), "Section 4.17 of the Frameworks" for the descriptor, "paragraphs 1.31-37" (2.5).
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:01: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0119 (P1); built by tools/bm_build.py.
