---
id: std:doc:qaa-archaeology-2022-benchmarks
title: "Subject Benchmark Statement Archaeology"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100299", label: "archaeology", basis: "stated" }
  - { scheme: "cah", code: "CAH20-01-03", label: "archaeology", basis: "stated" }
  - { scheme: "cah", code: "CAH20-01", label: "history and archaeology", basis: "stated" }
  - { scheme: "hecos", code: "100384", label: "archaeological sciences", basis: "inferred" }
edition: "March 2022 (fourth edition)"
published: 2022-03
status: current
supersedes: "the third edition (2014), named in the advisory group list (D1, section 6)"
heldText: { method: sha256-bytes, raw: c37a850bc9efdf101db0c38344fb46b3e70ccf63a72cd766af73b273b8d38c18, normalised: 3bb9190478bdb20aa451870daecc3e876db5afb26c40af2dd0659021a97ab444 }
heldTextStan: { method: sha256-stan, raw: c37a850bc9efdf101db0c38344fb46b3e70ccf63a72cd766af73b273b8d38c18, normalised: 8ef55041b7d8e14e98b0daacb01a1f33c3a036f2ed3c204fd4e97a6cead8965f }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2022 revision with cross-cutting themes (Archaeology fourth edition, March 2022)"
awardsCovered: ["bachelor's with honours"]
levelsCovered: ["fheq:6", "fqheis:10"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0085 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:14"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Archaeology (QAA, March 2022)

> Run 0085, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2022-archaeology-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
This document records what the QAA's 2022 Archaeology statement expects of an honours graduate in archaeology and of the courses that lead there. Read S4 for the standards: section 4 gives one rung only, the threshold, in two lists (subject knowledge, understanding and skills; generic skills), and section 3 adds two outcome lists of what students will be equipped to do. Every standard has a practitioner version, a student version and two instructions for AI agents who write about it or use it in conversation. Performance above the threshold is left to Annex D of the 2024 Frameworks, which this document points to and never copies.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Archaeology, bachelor's degree with honours (FHEQ level 6; FQHEIS level 10), fourth edition, March 2022. One rung is stated: the threshold, with 18 subject items (4.3) and 20 generic items (4.4); no typical or excellent lists, the provider being sent to Annex D for higher classes (4.2). Two further outcome lists in section 3 give the subject-specific (3.2, 16 items) and generic, transferable and employability skills (3.3, 19 items) students will be equipped with. Fourteen obliging paragraphs set expectations on courses and the discipline: the platform of knowledge, inclusion, sustainability, ethics, accessibility, assessment and the use of Annex D. Themes: equality, diversity and inclusion; accessibility; sustainability (education for sustainable development); enterprise and entrepreneurship. Bodies: the Chartered Institute for Archaeologists with University Archaeology UK (joint degree accreditation since 2019), BABAO, the Institute of Archaeologists of Ireland and others in the historic environment sector; the national heritage bodies are named as partners.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Archaeology"
edition: "March 2022 (fourth edition)"
dates:
  published: 2022-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement; a key reference point in Wales and Scotland and part of the quality requirements in Northern Ireland (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2022", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate in archaeology is expected to know, do and understand at the end of an honours degree, and the nature of courses in the subject"
appliesTo:
  awards: ["bachelor's with honours"]
  levels: ["fheq:6", "fqheis:10"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This document is a QAA Subject Benchmark Statement for Archaeology that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies.\" (D1, front matter); 4.1 applies the standards in full only to courses with at least 50% archaeology"
statedSubjects:
  - { name: "Archaeology", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100299", label: "archaeology" }, { scheme: "cah", code: "CAH20-01-03", label: "archaeology" }] }
  - { name: "joint or combined honours courses (with history, geography, anthropology, classics and cultural heritage, English, natural sciences or forensic science)", locator: "(D1, 1.4; 1.7; 2.23)", kind: "programme title", codes: [{ scheme: "hecos", code: "100299", label: "archaeology" }] }
  - { name: "archaeological science", locator: "(D1, 2.12 to 2.17)", kind: "specialism", codes: [{ scheme: "hecos", code: "100384", label: "archaeological sciences" }] }
  - { name: "integrated master's degrees (MArc)", locator: "(D1, 2.24)", kind: "programme title", codes: [{ scheme: "hecos", code: "100299", label: "archaeology" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "a unique view of the whole human past and of being human; time depth for present concerns" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "interpreting tangible and intangible remains; discovery, stories, debate and many voices" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "origins in colonial and national contexts; changing methods and theory; a distinct discipline today" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "between science, arts and professional practice; how it differs from Classics, History and Heritage Management" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes of an Archaeology degree", gloss: "purposes: foundations in the human past, transferable skills and varied careers" }
  - { number: "1.6", order: 8, componentType: area, parent: "section 1", heading: "Characteristics of an Archaeology degree", gloss: "the platform of knowledge any course with at least half archaeology offers" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Archaeology degree", gloss: "courses with half archaeology or less build the platform into each module" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusion: barriers to taking part and the duty to widen voices" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "under-represented groups, from outreach to careers; student feedback on barriers" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainability: alignment with ESD outcomes and the finite resource" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship", gloss: "enterprise education and its benefits for careers" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship", gloss: "the professional body and joint accreditation against occupational standards" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship", gloss: "the joint governance of accreditation" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship", gloss: "not only a vocational degree; wide career sectors" }
  - { number: "2.1", order: 18, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "research-led, broad and rigorous; students meet primary material and can discover" }
  - { number: "2.2", order: 19, componentType: stem, parent: "section 2", heading: "Design", gloss: "the four contexts courses are built on" }
  - { number: "2.3", order: 20, componentType: area, parent: "section 2", heading: "The social context", gloss: "the social context: narratives of past societies through present lenses" }
  - { number: "2.4", order: 21, componentType: area, parent: "section 2", heading: "The social context", gloss: "contested pasts, identity and the legacy of colonialism; decolonising the subject" }
  - { number: "2.5", order: 22, componentType: area, parent: "section 2", heading: "The ethical and professional context", gloss: "institutional ethics approval for any student project" }
  - { number: "2.6", order: 23, componentType: area, parent: "section 2", heading: "The ethical and professional context", gloss: "human remains, illicit material, overseas work and the ethics in curricula" }
  - { number: "2.7", order: 24, componentType: paragraph, parent: "section 2", heading: "The ethical and professional context", gloss: "professional bodies, heritage protection law and treaties, links with nature heritage" }
  - { number: "2.8", order: 25, componentType: paragraph, parent: "section 2", heading: "The ethical and professional context", gloss: "growing employment, public benefit and accreditation since 2019" }
  - { number: "2.9", order: 26, componentType: area, parent: "section 2", heading: "The theoretical context", gloss: "theory and practice intertwined; paradigm shifts and borrowing from other fields" }
  - { number: "2.10", order: 27, componentType: paragraph, parent: "section 2", heading: "The theoretical context", gloss: "big questions about being human, resilience and contemporary challenges" }
  - { number: "2.11", order: 28, componentType: area, parent: "section 2", heading: "The theoretical context", gloss: "four elements: scale, networks, wider context and self-reflexive theory" }
  - { number: "2.12", order: 29, componentType: area, parent: "section 2", heading: "The scientific context", gloss: "archaeological science and its ten research themes" }
  - { number: "2.13", order: 30, componentType: area, parent: "section 2", heading: "The scientific context", gloss: "artefact study and dating frameworks" }
  - { number: "2.14", order: 31, componentType: area, parent: "section 2", heading: "The scientific context", gloss: "conservation science and the care of tangible heritage" }
  - { number: "2.15", order: 32, componentType: area, parent: "section 2", heading: "The scientific context", gloss: "biological and environmental science and biomolecular methods" }
  - { number: "2.16", order: 33, componentType: area, parent: "section 2", heading: "The scientific context", gloss: "experimental archaeology" }
  - { number: "2.17", order: 34, componentType: area, parent: "section 2", heading: "The scientific context", gloss: "digital literacy, creativity and global ethical frameworks for science" }
  - { number: "2.18", order: 35, componentType: paragraph, parent: "section 2", heading: "Implications for the design of Archaeology degree courses", gloss: "the four contexts underpin all degrees; humanities and sciences integrated" }
  - { number: "2.19", order: 36, componentType: paragraph, parent: "section 2", heading: "Implications for the design of Archaeology degree courses", gloss: "courses placed within the humanities, science and practice triangle" }
  - { number: "2.20", order: 37, componentType: practice, parent: "section 2", heading: "Accessibility", gloss: "a varied mix of teaching and learning methods so no student is disadvantaged" }
  - { number: "2.21", order: 38, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "adjustments, transparency, equal access to fieldwork and extras, clear assessment criteria" }
  - { number: "2.22", order: 39, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression year by year towards the threshold skills; readiness for postgraduate study" }
  - { number: "2.23", order: 40, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint honours students reach part of the skills and add others" }
  - { number: "2.24", order: 41, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's (MArc), exit awards and the Scottish four-year honours degree" }
  - { number: "2.25", order: 42, componentType: practice, parent: "section 2", heading: "Flexibility", gloss: "a flexible mix of research-led teaching styles and pedagogic innovation" }
  - { number: "2.26", order: 43, componentType: practice, parent: "section 2", heading: "Flexibility", gloss: "independent research, project or dissertation, with ethical reflection" }
  - { number: "2.27", order: 44, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership with accrediting and national heritage bodies and museums" }
  - { number: "2.28", order: 45, componentType: practice, parent: "section 2", heading: "Partnership", gloss: "data services, commercial units, volunteers, community archaeology and European partners" }
  - { number: "2.29", order: 46, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review against external reference points" }
  - { number: "2.30", order: 47, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.31", order: 48, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and the security of threshold standards" }
  - { number: "2.32", order: 49, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "professional accreditation for vocational courses" }
  - { number: "3.1", order: 51, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "content varies with position in the triangle; single and combined honours" }
  - { number: "3.2", order: 52, componentType: stem, parent: "section 3", heading: "Subject-specific content", gloss: "what students will be equipped to do in the subject" }
  - { number: "3.3", order: 53, componentType: stem, parent: "section 3", heading: "Generic, transferable and employability content", gloss: "general, transferable and employability skills of graduates" }
  - { number: "3.4", order: 54, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "teaching environments reflect each department's position" }
  - { number: "3.5", order: 55, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "teaching, research and practice; competent staff" }
  - { number: "3.6", order: 56, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "the learning environment and its resources, equipment and laboratories" }
  - { number: "3.7", order: 57, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "course documentation, safety and ethics guidance" }
  - { number: "3.8", order: 58, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "engagement with the archaeological community; practical work in every course" }
  - { number: "3.9", order: 59, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "an explicit assessment strategy tied to outcomes" }
  - { number: "3.10", order: 60, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "accessible, mixed assessment; adjustments; formative feedback" }
  - { number: "3.11", order: 61, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "the range of assessment methods in current use" }
  - { number: "4.1", order: 63, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the minimum threshold standards and where they apply in full" }
  - { number: "4.2", order: 64, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most students exceed the threshold; Annex D for degree classes" }
  - { number: "4.3", order: 65, componentType: stem, parent: "section 4", heading: "Threshold level: Subject knowledge, understanding and skills", gloss: "threshold: subject knowledge, understanding and skills" }
  - { number: "4.4", order: 66, componentType: stem, parent: "section 4", heading: "Generic skills", gloss: "threshold: generic skills" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of an Archaeology degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of an Archaeology degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "none", heading: "Contents", kind: "other: contents list" }
  - { number: "1 to 4", heading: "section heading lines", kind: "other: headings, recorded in S3 as sections" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for SB5 and SB6" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for Archaeology", kind: "other: back matter, read for S8 (editions 2000, 2007, 2014, 2022)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 87 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/archaeology-2022/1.6
  locator: { number: "1.6", headingPath: ["Context and purposes of an Archaeology degree", "Characteristics of an Archaeology degree"] }
  span: { start: 15773, end: 17940 }
  source: "1.6 Despite the interdisciplinary nature of the subject, and the varied pathways taken by different Archaeology courses, all degree courses containing a substantial component (at least 50%) of archaeology will offer a platform of knowledge and understanding in certain areas. These will include the origins and development of archaeology and its value in the modern world, embracing the legal and policy frameworks for research and professional practice, and the historical, social, cultural, ethical and political contexts for archaeological investigation, management and interpretation. This content should recognise the wider public interest in, and value of, the fragile and non-renewable nature of the archaeological resource and the need for sustainable approaches to its use and conservation. In addition, students are expected to be familiar with the diverse sources of evidence used by archaeologists, as well as the theoretical basis of the discipline and current approaches to interpretation. While students will have a broad and comparative knowledge of the archaeology of geographical regions and chronological periods, they are expected to have a\n\n5\ndeeper understanding of one or more distinct classes of archaeological material, or of specific archaeological periods. They should also recognise the importance of the recovery, recording and management of primary data through practical experience in the field (with adjustments in place as required for disabled students) or through collections-based, records-based, or artefact-based study and skills development and be aware of methodologies for quantifying, analysing and interpreting this data. This will include the concepts and application of scientific methods, the integration of chronometric, environmental and materials science data with archaeological models, the use of analogy and experiment in archaeological analysis and interpretation, and an understanding of the causes of variation in the reliability (bias) of different classes of evidence from archaeological contexts (such as taphonomy; cultural and non-cultural transformations; depositional processes; and recovery procedures).\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "courses with at least 50% archaeology and their students"
  addressee: both
  verbs: ["offer", "include", "recognise"]
  about: "the platform of knowledge and understanding"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Any course that is at least half archaeology will give students a common base: where the discipline came from and why it matters now, its legal and policy setting, and the contexts of investigation; the content should stress that the resource is fragile and cannot be renewed. Students are expected to know the kinds of evidence, theory and interpretation, to know regions and periods broadly and one or more classes of material or periods in depth, and to recognise why recovering and managing primary data matters, through fieldwork (adjusted for disabled students) or work with collections, records or artefacts, including scientific methods and the sources of bias in evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/1.7
  locator: { number: "1.7", headingPath: ["Context and purposes of an Archaeology degree", "Characteristics of an Archaeology degree"] }
  span: { start: 17940, end: 18708 }
  source: "1.7 In the case of degree courses where archaeology constitutes 50% or less of the total (including joint and combined honours courses, and those cases where archaeology units are taken as optional components within other kinds of modularised courses), the delivery of an appropriate platform of knowledge and understanding should be integral to the design of each individual archaeology module. In such situations, both the knowledge and understanding attained by students, and the teaching environment, will be consistent with the standards expressed in this Subject Benchmark Statement. For those courses that include other subjects alongside archaeology, guidance on appropriate levels of attainment will be articulated in the relevant Subject Benchmark Statement."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "courses where archaeology is 50% or less"
  addressee: provider
  verbs: ["expressed"]
  about: "the platform in joint, combined and minor routes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Where archaeology is half a course or less, including joint and combined honours and optional modules in other courses, each archaeology module should be designed to deliver a suitable base of knowledge and understanding; what students attain and the teaching setting will match the standards of this statement, and other subjects follow their own statements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/archaeology-2022/1.8
  locator: { number: "1.8", headingPath: ["Context and purposes of an Archaeology degree", "Equality, diversity and inclusion"] }
  span: { start: 18743, end: 20734 }
  source: "1.8 Archaeology is an inherently interdisciplinary subject dealing with interpretations of the past and their relevance to the present and the future of humanity. Its deep-time and cross-cultural perspective offers unique potential for multivocality, but this is not always fulfilled, and archaeologists must take responsibility for improving this situation. Teaching, learning and assessment styles in the discipline are broad and emphasise equally practical field and laboratory practices as well as more traditional communication skills, including written assignments in a variety of different formats as well as oral and media presentations. Despite increasing efforts, archaeology still struggles with some traditional boundaries to participation, including ethnic diversity, access for disabled people and barriers on the basis of gender and socioeconomic background. In part, these are a legacy of the origins of archaeology as very hierarchical, traditional in outlook, fieldwork-based and focused on the past and material culture of a limited range of groups in society. In order to develop, archaeology takes a proactive approach to challenging negative stereotypes and emphasise the inherently diverse range of perspectives which exist on the human past. Archaeology should always emphasise the fluidity of our understandings of the past and the opportunity it offers to challenge our modern western conventions of practice. As explored in paragraph\n2.4 for instance, archaeology has the power to raise students' awareness of, and begin to address, the continuing impacts of colonialism. Archaeologists should reflect critically on their practices to ensure increased participation and must actively engage much more equitably with external communities, whether in schools, community groups, or in public spaces. Archaeology strives to develop a considered and thoughtful language with which to express ideas and concepts in ways that facilitate inclusion and reduce exclusivity.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must
  level: none
  appliesTo: "archaeologists and the discipline, including teaching staff"
  addressee: provider
  verbs: ["take", "emphasise", "reflect", "engage"]
  about: "widening voices and participation in the discipline"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The subject's deep-time, cross-cultural view could give voice to many groups, but it often does not, and archaeologists must take responsibility for changing that. Barriers remain around ethnicity, disability, gender and class, a legacy of the discipline's origins. Archaeology should stress that understanding of the past is fluid, help students see the continuing effects of colonialism, and its practitioners should reflect on their practice and must engage far more fairly with communities outside the academy, in inclusive language."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/archaeology-2022/1.9
  locator: { number: "1.9", headingPath: ["Context and purposes of an Archaeology degree", "Equality, diversity and inclusion"] }
  span: { start: 20734, end: 21856 }
  source: "1.9 Archaeology degrees have a long tradition of being open to people from non- standard academic backgrounds. However, much more remains to be done to ensure the equitable inclusion of under-represented groups, most notably ethnic minority students, students from less affluent backgrounds, and otherwise disadvantaged students, including students with caring responsibilities, neurodiverse students and students with physical and/or mental health considerations. Greater attention should be paid to under-represented groups at all stages from outreach to marketing and recruitment, to education and career\n\n6\nprogression after graduation, in order to provide externally visible role models who can convey the clear message that archaeology is a global and diverse subject of enormous relevance to contemporary society. In addition, robust feedback mechanisms should be in place for students to highlight deficiencies and co-create possible solutions to barriers to participation, including ensuring accessibility for all students, particularly for practical elements of teaching, learning and extracurricular experience."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "departments and courses in archaeology"
  addressee: provider
  verbs: ["paid", "provide", "highlight", "co-create"]
  about: "under-represented groups and feedback on barriers"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Though open to people from varied academic backgrounds, archaeology must do more to include under-represented students, among them ethnic minority, less affluent, disadvantaged, caring, neurodiverse and disabled students. Attention should go to them at every stage from outreach to careers, to give visible role models, and strong feedback routes should let students raise problems and help design fixes, including access to practical work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/archaeology-2022/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of an Archaeology degree", "Sustainability"] }
  span: { start: 21872, end: 23200 }
  source: "1.10 The core skills provided by all Archaeology degrees align with the learning outcomes suggested by the Education for Sustainable Development Guidance produced by Advance HE and QAA (March 2021). These include critical thinking, self-awareness, collaborative competencies, anticipatory and strategic thinking. Archaeology both encourages and embeds partnerships and interdependence between economic, social and environmental factors. By developing a deep understanding of what life was like in the past for people and non-humans, archaeology can actively contribute to the narratives about how we create a vision of a better world. Indeed, as the only subject that deals with the entirety of the human past, archaeology offers a critical perspective on how we now shape that future. In particular, the discipline is uniquely placed to foster an appreciation of the fragile and finite nature of the archaeological resource and the need for sustainable approaches to its use and conservation. Moreover, archaeology is directly involved with the development of sustainable and ethical heritage and tourism industries across the world. Emphasis should be placed on conveying this value to a wider society, both within local and regional communities and government organisations who are in a position to determine future outcomes."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the discipline and its teaching"
  addressee: provider
  verbs: ["placed", "conveying"]
  about: "conveying the value of sustainability and the finite resource"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The core skills of archaeology degrees match the outcomes the 2021 ESD guidance proposes, such as critical, anticipatory and strategic thinking, self-awareness and collaboration. The subject can shape stories of a better future, teaches that the resource is fragile and finite and serves sustainable heritage and tourism; emphasis should go on conveying this value to society, communities and government."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/archaeology-2022/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of an Archaeology degree", "Enterprise and entrepreneurship"] }
  span: { start: 23846, end: 24875 }
  source: "1.12 In relation to archaeology, the Chartered Institute for Archaeologists (CIfA) is the leading professional body representing archaeologists working in the UK and overseas. CIfA champions professionalism in archaeology by setting standards, improving career prospects and promoting best practice. In collaboration with UAUK (University Archaeology UK), it is now possible for providers of Archaeology degrees to apply for accreditation. University degrees are assessed through a competency matrix, which is aligned with the National Occupational Standards for Archaeological Practice (NOS). NOS are designed to be flexible, and therefore a good way of encompassing the great variety of subjects covered in UK Archaeology degrees and align directly to the design principles set out within this document. To gain accreditation, providers must demonstrate that the core relevant NOS are covered by a particular degree or pathway. Indeed, many of the key NOS are already successf ully covered by this Subject Benchmark Statement.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "providers seeking professional accreditation of a degree"
  addressee: provider
  verbs: ["apply", "demonstrate"]
  about: "accreditation against the occupational standards"
  themes: [theme:enterprise]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The Chartered Institute for Archaeologists sets standards for the profession and, with University Archaeology UK, accredits degrees through a competency matrix tied to the occupational standards for archaeological practice (NOS); to be accredited, a provider must show that the core relevant standards are covered by the degree or pathway, and the statement already covers many of them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/archaeology-2022/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of an Archaeology degree", "The ethical and professional context"] }
  span: { start: 29481, end: 31257 }
  source: "2.6 The treatment of human remains, in particular, requires ethical consideration and there are important debates around, for example, the finding, study and storage of human and non-human primate, including hominin, remains. These should always be treated with dignity and respect regardless of their age and provenance, and it is important to be open and transparent and to act with integrity in the treatment of all biological remains. The Chartered Institute for Archaeologists (CIfA) and the British Association for Biological Anthropology and Osteoarchaeology (BABAO) both publish useful guidelines and resources for further study. Ethical concerns also arise when working with cultural objects or human remains acquired illegally, trafficked or sold, and for any project which involves living participants and generates and stores personal information. For fieldwork overseas, it will be important to make appropriate collaborative arrangements with local scholars and organisations, and also to obtain appropriate research permits for any work undertaken. Ethics are also relevant to professional conduct - for example, damage to reputation or the misrepresentation of views - and to issues such as plagiarism of the work of others. Overall, archaeology curricula should explicitly embed consideration of the ethics of archaeological practice and the real-world uses of archaeology, particularly in relation to less privileged social groups, and the facilitation of equitable engagement with stakeholders beyond the traditional academic and professional archaeological community. Examples from around the world, suitably contextualised, can illustrate both the challenges and possible moves towards their solution and can be compared with contemporary local practice.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "students, staff and curricula in archaeology"
  addressee: both
  verbs: ["treated", "embed"]
  about: "ethics of human remains and of archaeological practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Human remains need ethical care: all human and non-human primate remains, hominins included, should always be treated with dignity and respect, whatever their age or origin, with openness and integrity. Ethical issues also arise with illicit material, personal data, overseas fieldwork and professional conduct, and curricula should explicitly build in the ethics of practice and of archaeology's real-world uses, especially for less privileged groups and for fair engagement beyond the profession."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of an Archaeology degree", "The scientific context"] }
  span: { start: 37224, end: 37857 }
  source: "2.12 Archaeological science is the application of scientific techniques to archaeological problems, whose methodologies and innovations are ultimately shared across a broad range of sciences, including physics, chemistry, biochemistry, biology, medicine, forensics and geoscience, alongside environmental, digital and materials science. The use of quantitative approaches, hypothesis testing and an awareness of scientific techniques should be part of the toolkit of every archaeologist. Archaeological science is interdisciplinary and collaborative by nature, contributing to a diverse range of major research themes. These include:"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "every archaeologist, students included"
  addressee: learner
  verbs: ["use"]
  about: "quantitative and scientific approaches in the toolkit"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Archaeological science applies techniques from many sciences to archaeological problems; quantitative methods, hypothesis testing and a grasp of scientific techniques should belong in every archaeologist's toolkit, in a field that is interdisciplinary and collaborative."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of an Archaeology degree", "Implications for the design of Archaeology degree courses"] }
  span: { start: 40977, end: 41452 }
  source: "2.19 Individual degree courses are located at different points within a triangle drawn between the complementary archaeologies of the humanities, sciences and professional practice. A department teaching single and combined honours degrees will inevitably position the courses it offers at different locations within this range. All courses will nevertheless stress the contexts, interdisciplinarity and overarching practice that departments seek to instil in their students."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "all archaeology courses"
  addressee: provider
  verbs: ["stress", "seek"]
  about: "every course stresses the contexts and practice"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses sit at different points between the humanities, the sciences and professional practice, and a department will place its single and combined honours courses differently, but all courses will stress the contexts, the interdisciplinarity and the practice that departments want students to take on."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/archaeology-2022/2.20
  locator: { number: "2.20", headingPath: ["Distinctive features of an Archaeology degree", "Accessibility"] }
  span: { start: 41467, end: 41953 }
  source: "2.20 The principal learning and teaching methods that an Archaeology student may experience will depend on the aims and objectives of the course, given the wide range of subject-specific and transferable skills being developed. To ensure students who struggle with particular forms of teaching and learning scenarios are not disadvantaged, methods used within an individual course should be as varied as possible. They are likely to comprise an appropriate combination of the following:"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "teaching and learning methods within a course"
  addressee: provider
  verbs: ["ensure", "varied"]
  about: "varied teaching methods so no student is disadvantaged"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The methods a student meets depend on the course's aims and the wide range of skills it develops; so that students who find some formats hard are not disadvantaged, the methods in a course should be as varied as possible, drawn from a list of typical methods with adjustments for access."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/archaeology-2022/2.21
  locator: { number: "2.21", headingPath: ["Distinctive features of an Archaeology degree", "Accessibility"] }
  span: { start: 43586, end: 44842 }
  source: "2.21 While there is a recognition that teaching and assessments may need to be adjusted or tailored to the requirements of individuals to ensure inclusiveness and well- being, different formats should be offered to all students and expectations should be\n\n13\ntransparent. Care must be taken not to create a two-tier system that singles out students with additional requirements. Fieldwork in particular may present practical difficulties for some students and no one-size-fits-all approach is likely to be sufficient; individual circumstances should be taken into account in agreeing adjustments to teaching and learning methods for disabled students. In addition, all practical efforts should be made to ensure equal access to extracurricular activities such as field trips, placements and volunteering opportunities, given the often hidden costs (including opportunity costs) involved. The timing of religious observances and school holidays may be considered when setting deadlines. It should be remembered that perceptions of assessment may differ according to the cultural and experiential backgrounds of both assessors and their students. Clear and accessible guidance outlining assessment criteria at different stages of the degree must be provided."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "teaching, assessment and extracurricular activity"
  addressee: provider
  verbs: ["offered", "taken", "agreeing", "provided"]
  about: "adjustments, equal access and clear assessment criteria"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Teaching and assessment may be tailored for inclusion, but different formats should be open to all and expectations clear; care must be taken not to single out students with extra needs. Fieldwork adjustments for disabled students should follow individual circumstances, equal access to trips, placements and volunteering should be pursued given hidden costs, cultural views of assessment should be remembered, and clear, accessible guidance on assessment criteria at each stage must be provided."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/archaeology-2022/2.23
  locator: { number: "2.23", headingPath: ["Distinctive features of an Archaeology degree", "Progression"] }
  span: { start: 45575, end: 46082 }
  source: "2.23 Joint honours undergraduate - for example, those studying archaeology and anthropology or archaeology and classics - will achieve only a proportion of the specific and generic skills listed below but will add others (see paragraph 1.4). Typically, there will be less emphasis on laboratory science and fieldwork in a joint honours course, but this is not always the case - for example, where archaeology is paired with a STEM or social science discipline such as geography or environmental geoscience.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint honours students with archaeology"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "joint honours reach part of the skills and add others"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students on joint honours routes, such as archaeology with anthropology or with classics, will reach only some of the subject-specific and generic skills and will add others from their partner subject; they usually do less laboratory science and fieldwork, though not where the partner is a STEM or social science subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b1
  locator: { number: "3.2.b1", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 53336, end: 53479 }
  source: "critically evaluate, challenge and apply appropriate scholarl y, theoretical and scientific pri nciples and concepts to archaeological problems"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["evaluate", "challenge", "apply"]
  about: "critical use of scholarly, theoretical and scientific ideas"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Judge, contest and use suitable scholarly, theoretical and scientific principles when tackling archaeological problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b2
  locator: { number: "3.2.b2", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 53482, end: 53643 }
  source: "practise core fieldwork techniques to observe, record and interpret primary archaeological evidence (with adjustments in place as required for disabled students)"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["practise", "observe", "record", "interpret"]
  about: "core fieldwork techniques"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use the core techniques of fieldwork to observe, record and interpret primary evidence, with adjustments where a disabled student needs them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b3
  locator: { number: "3.2.b3", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 53646, end: 53772 }
  source: "practise core post-e xcavation/post-s urv ey techniques such as stratigraphic analysis of field records, phasing and archiving"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["practise"]
  about: "post-excavation and post-survey techniques"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use the core techniques that follow excavation or survey, such as analysing stratigraphy from field records, phasing and archiving."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b4
  locator: { number: "3.2.b4", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 53775, end: 53891 }
  source: "practise core techniques of recording, measurement, analysis and interpretati on of archaeological material and data"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["practise"]
  about: "recording, measuring and analysing material and data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use core techniques to record, measure, analyse and interpret archaeological material and data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b5
  locator: { number: "3.2.b5", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 53894, end: 54010 }
  source: "recognise and communicate the archaeological significance of materi al re mains,\n• landscapes and environmental data"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["recognise", "communicate"]
  about: "the significance of remains, landscapes and environmental data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "See and explain why material remains, landscapes and environmental data matter archaeologically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b7
  locator: { number: "3.2.b7", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 54013, end: 54136 }
  source: "interpret spatial data by integrating theoretical models, traces surviving in present- day landscapes, and excavati on data"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["interpret", "integrating"]
  about: "interpreting spatial data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Read spatial data by combining theoretical models, the traces left in today's landscapes and the results of excavation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b8
  locator: { number: "3.2.b8", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 54139, end: 54280 }
  source: "observe and descri be different classes of pri mary archaeological data, and record their characteri stics according to defined methodologies"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["observe", "record"]
  about: "describing and recording classes of primary data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Look at and describe different kinds of primary data and record their features by set methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b9
  locator: { number: "3.2.b9", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 54283, end: 54461 }
  source: "select and apply appropriate qualitative, quantitative and statistical analyses to process archaeological data, while recognising the potential and limitations of such techniques"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["select", "apply", "process", "recognising"]
  about: "choosing qualitative, quantitative and statistical analyses"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Choose and use suitable qualitative, quantitative and statistical methods to process data, knowing what each can and cannot show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b10
  locator: { number: "3.2.b10", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 54464, end: 54720 }
  source: "understand how social, cultural and environmental factors interact to bring about change in coupled socio-ecological systems, and how humans and our societies and cultures have shaped and been shaped by these interactions over the course of human evolution"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["understand", "shaped"]
  about: "change in coupled socio-ecological systems"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Grasp how social, cultural and environmental factors interact to drive change in linked social and ecological systems, and how people have shaped and been shaped by them through human evolution."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b11
  locator: { number: "3.2.b11", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 54723, end: 54934 }
  source: "understand the nature, extent and some of the reasons for contemporary and historical human diversity as seen from a vari ety of perspectives (f or example, social, cultural, ecological, biological and temporal)"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["understand"]
  about: "human diversity, present and past"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand the extent and nature of human diversity today and in the past, and some of its causes, from several perspectives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b12
  locator: { number: "3.2.b12", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 54937, end: 55072 }
  source: "be able to identify and question cultural assumptions in a variety of contexts, such as those still shaped by the legacy of colonialism"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["identify", "question"]
  about: "questioning cultural assumptions, including colonial legacies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Spot and challenge cultural assumptions in varied settings, including those still marked by colonialism."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b13
  locator: { number: "3.2.b13", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 55075, end: 55161 }
  source: "be able to interpret and analyse a vari ety of textual, oral, visual and digital forms"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["interpret", "analyse"]
  about: "interpreting textual, oral, visual and digital forms"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Interpret and analyse many kinds of sources: written, spoken, visual and digital."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b14
  locator: { number: "3.2.b14", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 55164, end: 55268 }
  source: "be aware of the interactions of biological, environmental and socio-cultural influences in human ecology"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: []
  about: "how biology, environment and culture interact in human ecology"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know how biological, environmental and social or cultural influences interact in human ecology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b15
  locator: { number: "3.2.b15", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 55271, end: 55425 }
  source: "be able to evaluate, compare and synthesise a variety of different forms of evidence to make interpretations about human behaviour in the past and present"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["evaluate", "compare", "synthesise"]
  about: "weighing and combining different evidence about behaviour"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assess, compare and bring together different forms of evidence to interpret human behaviour, past and present."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b16
  locator: { number: "3.2.b16", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 55428, end: 55586 }
  source: "be aware of ethical issues surrounding the legacy and uses of the discipline and to critically evaluate and use relevant modes of communication and engagement"
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["evaluate", "use"]
  about: "ethics of the discipline and modes of communication"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know the ethical issues around the discipline's legacy and uses, and critically assess and use fitting ways of communicating and engaging."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.2.b17
  locator: { number: "3.2.b17", headingPath: ["Content, structure and delivery", "Subject-specific content"] }
  span: { start: 55593, end: 55717 }
  source: "understand the broader legislative and planning content in which archaeological work may be undertaken, now and in the past."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject, as the course allows"
  addressee: learner
  verbs: ["understand"]
  about: "legislative and planning context"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand the wider legal and planning setting in which archaeological work may happen, now and in the past."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b1
  locator: { number: "3.3.b1", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 55868, end: 56073 }
  source: "problem solving and lateral thinking to develop soluti ons through cre ati ve thinking in both practical and theoretical contexts, drawing from a range of techniques from across the humanities and sciences"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["develop", "drawing"]
  about: "creative problem solving across humanities and sciences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Solve problems by lateral and creative thinking in practical and theoretical settings, using methods from the humanities and sciences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b2
  locator: { number: "3.3.b2", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 56076, end: 56187 }
  source: "producing logical and structured arg uments supported by analytical and critical reference to relevant evidence"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["producing"]
  about: "structured, evidenced argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Build logical, well-ordered arguments backed by analytical and critical use of relevant evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b3
  locator: { number: "3.3.b3", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 56190, end: 56324 }
  source: "planning, designing, executing and documenting a course of pri mary research, working independently and collaboratively as appropriate"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["planning", "designing", "executing", "documenting", "working"]
  about: "designing and carrying out primary research"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Plan, design, carry out and record a programme of primary research, alone or with others as fits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b4
  locator: { number: "3.3.b4", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 56327, end: 56372 }
  source: "assembling coherent research/proj ect designs"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["assembling"]
  about: "coherent research or project designs"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Put together coherent designs for research or projects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b5
  locator: { number: "3.3.b5", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 56375, end: 56571 }
  source: "evaluating one's own and others' opinions cri tically , fr om an appreciati on of the practice of archaeology in its changing theoretical, methodological, professional, ethical and social contexts"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["evaluating"]
  about: "critical evaluation of own and others' views"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assess one's own and others' views critically, informed by archaeology's changing theoretical, methodological, professional, ethical and social settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b6
  locator: { number: "3.3.b6", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 56574, end: 56647 }
  source: "applying quantitative analysis and digital literacy in practical contexts"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["applying"]
  about: "quantitative analysis and digital literacy in practice"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use quantitative analysis and digital skills in practical work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b7
  locator: { number: "3.3.b7", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 56650, end: 56719 }
  source: "demonstrating a positive and confident approach to practical problems"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["demonstrating"]
  about: "a positive approach to practical problems"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Meet practical problems with a confident, positive attitude."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b8
  locator: { number: "3.3.b8", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 56722, end: 56805 }
  source: "demonstrating an innovati ve approach, creativity, colla boration and ri sk-t aking"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["demonstrating"]
  about: "innovation, creativity, collaboration and risk-taking"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show an inventive approach, creativity, cooperation and a willingness to take risks."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b9
  locator: { number: "3.3.b9", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 56808, end: 56875 }
  source: "presenting eff ective presentation for different kinds of audiences"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["presenting"]
  about: "presenting to different audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Give effective presentations to varied audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b10
  locator: { number: "3.3.b10", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 56878, end: 57057 }
  source: "effectively communicating with a wide range of audiences using a variety of media, including written and oral, and creating effective and appropri ate forms of visual presentation"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["communicating", "creating"]
  about: "communicating in many media, including visual"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Communicate well with many audiences in written, spoken and other media, and produce effective, suitable visual presentation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b11
  locator: { number: "3.3.b11", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 57060, end: 57189 }
  source: "making effective and appropri ate use of relevant digital technology and associated software for the manipulation of digital data"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["making"]
  about: "digital technology and software for digital data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use relevant digital technology and software well and suitably to handle digital data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b12
  locator: { number: "3.3.b12", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 57192, end: 57297 }
  source: "making cri tical and eff ective use of information retri eval skills using analogue and digital resources"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["making", "using"]
  about: "information retrieval from analogue and digital resources"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Find information critically and effectively from analogue and digital sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b13
  locator: { number: "3.3.b13", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 57300, end: 57361 }
  source: "working methodically and accurately, with attention to detail"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["working"]
  about: "method, accuracy and attention to detail"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Work methodically and accurately, paying attention to detail."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b14
  locator: { number: "3.3.b14", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 57364, end: 57459 }
  source: "reflecting on and being proactive in accessing continuing professional and personal development"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["reflecting", "accessing"]
  about: "continuing professional and personal development"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Reflect on and act early to seek continuing professional and personal development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b15
  locator: { number: "3.3.b15", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 57462, end: 57567 }
  source: "time-management, organisation and planning skills, including assembling coherent research/project designs"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["assembling"]
  about: "time management, organisation and planning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Manage time, organise and plan, including putting together coherent research or project designs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b16
  locator: { number: "3.3.b16", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 57570, end: 57754 }
  source: "colla borating effectively in a team via experi ence of work ing in a group; for example, in the laboratory, in the field or in proj ect work (with reasonable adjustments, if required)"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "teamwork in laboratory, field or project"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Work well in a team through group experience in the laboratory, the field or project work, with reasonable adjustments if needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b17
  locator: { number: "3.3.b17", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 57757, end: 57951 }
  source: "appreciati ng the importance of ethical and health and safety procedures and responsibilit ies (both personal and with re gard to others ) as well as broader professional frameworks and policies"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "ethics, health and safety and professional frameworks"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Value ethical and health and safety procedures and duties, for oneself and others, and wider professional frameworks and policies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b18
  locator: { number: "3.3.b18", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 57954, end: 58142 }
  source: "appreciati ng the need for inclusiveness and being sensitive, responsive and proactive in taking personal responsibility for making sure diverse others and different cultures are respected"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["taking", "making"]
  about: "inclusiveness and respect for others and cultures"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Value inclusion, respond with sensitivity and act early, owning the duty to see that diverse people and cultures are respected."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.3.b19
  locator: { number: "3.3.b19", headingPath: ["Content, structure and delivery", "Generic, transferable and employability content"] }
  span: { start: 58145, end: 58410 }
  source: "engaging with relevant aspects of the broader cultural context of professional practice in any given field, such as equality, diversity and inclusiveness, sustainability, global perspectives, inequality, public engagement, employability, enterpri se and creativity."
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["engaging"]
  about: "the wider cultural context of professional practice"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Engage with the wider cultural setting of professional practice in any field, such as equality, diversity and inclusion, sustainability, global views, inequality, public engagement, employability, enterprise and creativity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 61323, end: 61790 }
  source: "3.9 Each Archaeology course contains an explicit assessment strategy as part of its curriculum design. This strategy will clearly and directly reflect the learning outcomes of the course components, support student learning, and enable students to demonstrate progressive levels of attainment. The strategy will reflect the variety of abilities and skills developed within the curriculum tied to the methods of teaching and learning adopted by the particular course.\n"
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "each archaeology course"
  addressee: provider
  verbs: ["contains", "reflect", "support", "enable"]
  about: "an explicit assessment strategy"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Every archaeology course has an explicit assessment strategy in its design, which will mirror the outcomes of its components, support learning, let students show rising levels of attainment and reflect the range of abilities and the teaching methods used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/archaeology-2022/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65466, end: 65949 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours degree-awarding providers"
  addressee: provider
  verbs: ["perform", "refer"]
  about: "using Annex D above the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do much better than the minimum threshold; each provider decides how to evidence this and should refer to Annex D, which describes the four honours classes (1st, 2:1, 2:2, 3rd) at level 6 of the FHEQ, level 10 in Scotland."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b1
  locator: { number: "4.3.b1", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 66097, end: 66174 }
  source: "appreciate the chronological and conceptual scope of archaeological endeavour"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["appreciate"]
  about: "the time span and conceptual range of the discipline"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Grasp how far archaeology reaches in time and in the ideas it works with."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b2
  locator: { number: "4.3.b2", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 66177, end: 66254 }
  source: "demonstrate knowledge of the archaeology of a number of geographical re gions"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["demonstrate"]
  about: "regional breadth"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show knowledge of the archaeology of several geographical regions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b3
  locator: { number: "4.3.b3", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 66257, end: 66335 }
  source: "demonstrate knowledge of the archaeology of a number of chronological peri ods"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["demonstrate"]
  about: "period breadth"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show knowledge of the archaeology of several chronological periods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b4
  locator: { number: "4.3.b4", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 66338, end: 66449 }
  source: "demonstrate understanding of the pri nciples and methods by which archaeological data are acquired and analysed"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["demonstrate", "acquired", "analysed"]
  about: "how data are gathered and analysed"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show understanding of the principles and methods for obtaining and analysing archaeological data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b5
  locator: { number: "4.3.b5", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 66452, end: 66533 }
  source: "demonstrate practical experi ence of the recovery of pri mary archaeological data"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["demonstrate"]
  about: "practical experience of recovering primary data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show hands-on experience of recovering primary archaeological data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b6
  locator: { number: "4.3.b6", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 66536, end: 66656 }
  source: "describe the vari ety of theoretical and practical approaches to unders tanding, constructing, and interpreting the past"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["describe"]
  about: "theoretical and practical approaches to the past"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Describe the range of theoretical and practical ways of understanding, constructing and interpreting the past."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b7
  locator: { number: "4.3.b7", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 66659, end: 66742 }
  source: "recognise the range of archaeological data and relevant data from other disciplines"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["recognise"]
  about: "the range of data, including other disciplines"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Recognise the range of archaeological data and of relevant data from other subjects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b8
  locator: { number: "4.3.b8", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 66745, end: 66875 }
  source: "describe the problematic and vari ed nature of archaeological evidence and data and understand their possibilities and limitations"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["describe", "understand"]
  about: "the problems, possibilities and limits of evidence"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Describe why archaeological evidence is varied and problematic, and understand what it can and cannot show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b9
  locator: { number: "4.3.b9", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 66878, end: 66966 }
  source: "gather, analyse and present arc haeological evidence fro m primary and secondary sources"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["gather", "analyse", "present"]
  about: "working with primary and secondary evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Collect, analyse and present archaeological evidence from primary and secondary sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b10
  locator: { number: "4.3.b10", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 66969, end: 67011 }
  source: "recognise the range of archaeological data"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["recognise"]
  about: "the range of archaeological data (repeat of b7)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Recognise the range of archaeological data; this repeats the first half of bullet 7."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b11
  locator: { number: "4.3.b11", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 67014, end: 67120 }
  source: "recognise the finite nature of the archaeological resource and the need for its sustainable conserv ati on"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["recognise"]
  about: "a finite resource needing sustainable conservation"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Recognise that the archaeological resource is finite and needs to be conserved sustainably."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b12
  locator: { number: "4.3.b12", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 67123, end: 67188 }
  source: "research and present an extended piece of archaeological research"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["research", "present"]
  about: "an extended piece of research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Carry out and present a substantial piece of archaeological research of one's own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b13
  locator: { number: "4.3.b13", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 67191, end: 67344 }
  source: "demonstrate knowledge of archaeological and practical skills, part icularly in relati on to the observation, recording and interpretation of primary data"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["demonstrate"]
  about: "observing, recording and interpreting primary data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show knowledge of archaeological and practical skills, above all in observing, recording and interpreting primary data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b14
  locator: { number: "4.3.b14", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 67347, end: 67481 }
  source: "describe the development of archaeology as a subject and understand its implications for the discipline today and its cultural context"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["describe", "understand"]
  about: "the development of the discipline"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Describe how archaeology developed as a subject and understand what that means for the discipline now and its cultural setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b15
  locator: { number: "4.3.b15", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 67484, end: 67598 }
  source: "demonstrate awareness of the social, cultural and polit ical context of archaeological interpretation and practice"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the social, cultural and political context"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show awareness of the social, cultural and political setting of archaeological interpretation and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b16
  locator: { number: "4.3.b16", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 67601, end: 67855 }
  source: "demonstrate awareness of the impact of archaeological practice, interpretation and representation on other communities, including historically marginalised groups,\n\n21\nand appreciate the need to engage with communities thus affected on an equitable basis"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["demonstrate", "appreciate", "engage"]
  about: "impact on communities and fair engagement"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show awareness of how archaeological practice, interpretation and representation affect other communities, including historically marginalised groups, and appreciate the need to engage fairly with those affected."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b17
  locator: { number: "4.3.b17", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 67858, end: 67972 }
  source: "understand the need for an inclusive discipline and accord respect to diverse others within and beyond archaeology"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["understand", "accord"]
  about: "an inclusive discipline and respect for others"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand why the discipline must be inclusive and give respect to diverse others inside and outside archaeology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.3.b18
  locator: { number: "4.3.b18", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 67975, end: 68048 }
  source: "demonstrate awareness of the legal and ethical dimensions of archaeology."
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["demonstrate"]
  about: "legal and ethical dimensions"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show awareness of the legal and ethical sides of archaeology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 68151, end: 68254 }
  source: "demonstrate awareness of relevant archaeological concepts and methods in non- archaeological situations"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["demonstrate"]
  about: "using archaeological ideas outside archaeology"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show awareness of relevant archaeological concepts and methods in situations outside archaeology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 68257, end: 68327 }
  source: "perf orm assigned tasks as part of a team, participating in discussion"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["participating"]
  about: "teamwork and discussion"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Carry out set tasks as a team member, taking part in discussion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 68330, end: 68395 }
  source: "bri ng together information and materi als from different sources"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: []
  about: "bringing together information from different sources"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Bring together information and material from different sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 68398, end: 68430 }
  source: "identi fy problems and questions"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: []
  about: "identifying problems and questions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Identify problems and frame questions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 68433, end: 68478 }
  source: "undertake the analysis of factual information"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
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
- id: qaa/archaeology-2022/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 68481, end: 68543 }
  source: "recognise strengths and weaknesses in the arg uments of others"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["recognise"]
  about: "judging others' arguments"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Recognise the strengths and weaknesses of other people's arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 68546, end: 68624 }
  source: "produce a synthesis of the state of knowledge on a particular subject or topic"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["produce"]
  about: "synthesising the state of knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Produce a synthesis of what is known on a particular subject or topic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 68627, end: 68672 }
  source: "with guidance, undert ake tasks independently"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: []
  about: "independent work with guidance"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Carry out tasks independently, with guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 68675, end: 68739 }
  source: "re flect on their own progress and make use of feedback provided"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
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
- id: qaa/archaeology-2022/4.4.b10
  locator: { number: "4.4.b10", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 68742, end: 68801 }
  source: "express themselves effectively, both orally and in wri ting"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["express"]
  about: "speaking and writing effectively"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Express oneself well in speech and in writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b11
  locator: { number: "4.4.b11", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 68804, end: 68879 }
  source: "present knowledge or an arg ument in a way that is comprehensible to others"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["present"]
  about: "making knowledge or argument understood"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Present knowledge or an argument so that others can follow it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b12
  locator: { number: "4.4.b12", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 68882, end: 68968 }
  source: "use relevant IT to collate, analyse, select and present information (digital literacy)"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["use", "collate", "analyse", "select", "present"]
  about: "digital literacy with relevant IT"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use relevant IT to gather, analyse, choose and present information (digital literacy)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b13
  locator: { number: "4.4.b13", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 68971, end: 69018 }
  source: "make oral presentations uti lis ing visual aids"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["make"]
  about: "oral presentation with visual aids"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Give oral presentations supported by visual aids."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b14
  locator: { number: "4.4.b14", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 69021, end: 69102 }
  source: "demonstrate an ability to comprehend when presented with new ideas or information"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["demonstrate", "comprehend"]
  about: "taking in new ideas and information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show the ability to understand new ideas or information when they are presented."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b15
  locator: { number: "4.4.b15", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 69105, end: 69163 }
  source: "demonstrate skills in recognising and describing materi al"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["demonstrate"]
  about: "recognising and describing material"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show skill in recognising and describing material."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b16
  locator: { number: "4.4.b16", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 69166, end: 69248 }
  source: "demonstrate classification skills in describing, categori sing and collati ng data"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["demonstrate"]
  about: "classifying and collating data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show skill in classification: describing, sorting into categories and collating data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b17
  locator: { number: "4.4.b17", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 69251, end: 69366 }
  source: "understand the importance of health and safety and of equality, diversity and inclusiveness in the work environment"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["understand"]
  about: "health and safety and EDI at work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understand why health and safety and equality, diversity and inclusion matter in the workplace."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b18
  locator: { number: "4.4.b18", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 69369, end: 69518 }
  source: "appreciate contempora ry debates relati ng to global sustainabilit y, employabilit y and global perspectives including decolonisation and anti-racism"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["appreciate"]
  about: "current debates on sustainability, employability, decolonisation and anti-racism"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Appreciate current debates on global sustainability, employability and global perspectives, decolonisation and anti-racism among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b19
  locator: { number: "4.4.b19", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 69521, end: 69571 }
  source: "appreciate the need to act in a sustainable manner"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["appreciate", "act"]
  about: "acting sustainably"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Appreciate the need to act sustainably."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/archaeology-2022/4.4.b20
  locator: { number: "4.4.b20", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 69574, end: 69707 }
  source: "appreciate and engage in contemporary debates - for example, around inequality, sustainability, globalisation and cultural diversity."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in archaeology"
  addressee: learner
  verbs: ["appreciate", "engage"]
  about: "engaging in contemporary debates"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Appreciate and take part in current debates, for instance on inequality, sustainability, globalisation and cultural diversity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/archaeology-2022/1.6
  forPractitioner: { text: "A course that is half archaeology or more will build a shared base: the history and present value of the discipline, its legal and policy frame, the social, ethical and political settings of fieldwork and interpretation, and care for a finite resource. Plan for broad regional and period knowledge plus depth in at least one class of material or period, hands-on work with primary data in the field (adjusted where a student is disabled) or with collections and records, scientific dating and analysis, analogy and experiment, and the causes of bias in evidence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your course will give you a broad grounding in how archaeology began, why it matters today and the laws and policies around it. You will be expected to know many regions and periods in outline and at least one kind of material or period in depth, to handle primary data in the field (with adjustments if you need them) or through collections, and to understand scientific methods and why some evidence is less reliable than other evidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation (will, with one should) on any course that is at least half archaeology, at FHEQ level 6 for the honours degree, not as one of the threshold items. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 1.6. Set it beside the threshold knowledge items 4.3.b2, 4.3.b3 and 4.3.b11 and the level 6 descriptor qaa/fheq-2024/4.15.b1; do not claim it binds a course with less archaeology, which para 1.7 treats separately."
  author-agent-dialogue: "Bring this up when a programme team asks what core content an archaeology degree should cover, or when a student wonders why fieldwork, theory and science all appear in the course. Put it to staff as a design checklist and to a student as the broad base the course builds. Ask the team which modules carry depth in one class of material or period, and ask a student which kind of evidence they feel least sure of; avoid reading the long paragraph out or treating every element as a separate pass requirement."
- statement: qaa/archaeology-2022/1.7
  forPractitioner: { text: "In joint, combined or modular routes where archaeology is no more than half the course, design each archaeology module to carry its share of the core base of knowledge; the attainment and teaching environment will match this statement, while the partner subject is judged against its own statement.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a design duty on the course for joint and combined routes; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a course design duty (should) for routes where archaeology is half the course or less; it states no level of its own. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 1.7, and read it with para 1.6 and the scope note at para 4.1. Do not claim that joint honours students must meet every threshold item in 4.3 and 4.4; para 2.23 says they reach a proportion and add others."
  author-agent-dialogue: "Raise this with a programme team designing a joint or combined route, or with a teacher of an archaeology option inside another degree. Frame it for staff as building the core base into each module rather than relying on the full course. Ask which parts of the shared base each module carries and how the partner subject's statement is being met; avoid putting this to a student as something they must achieve."
- statement: qaa/archaeology-2022/1.8
  forPractitioner: { text: "Staff and departments must own the work of widening who takes part in and is heard by archaeology: challenge stereotypes, show that views of the past change, bring the legacy of colonialism into teaching, reflect critically on practice, engage fairly with schools, community groups and the public, and use language that includes rather than excludes.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on archaeologists and departments as practitioners; the student meets its effect through the curriculum", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation (must and should) on archaeologists and departments, not an outcome the student is assessed on. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 1.8, under its equality, diversity and inclusion heading, and set it beside the student-facing items 4.3.b16, 4.3.b17 and 4.4.b18. Do not claim it sets a level or a legal duty; the statement carries no regulatory requirement."
  author-agent-dialogue: "Raise this with a programme team or teacher reviewing curriculum, fieldwork recruitment or outreach for inclusion. Put it in practitioner terms: what the department does to widen who takes part and whose pasts are told. Ask which groups the course still struggles to reach and where colonial legacies are taught; avoid passing this duty to a student or reading the paragraph aloud."
- statement: qaa/archaeology-2022/1.9
  forPractitioner: { text: "Attend to under-represented students at every stage, from outreach and recruitment through teaching to careers, so that they can see role models; put working feedback routes in place so students can report barriers and help solve them, above all for access to practical and extracurricular activity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the department and course; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) on inclusion across the student journey; it carries no level. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 1.9, and set it beside para 1.8, the accessibility paragraphs 2.20 and 2.21 and the student items 4.3.b17 and 4.4.b17. Do not present it as a student outcome or as a statutory equality duty."
  author-agent-dialogue: "Bring this into a programme team's discussion of recruitment, outreach, student voice or access to fieldwork. Frame it for staff as a check across the whole journey and on feedback routes. Ask how students can report a barrier and see it acted on, and which groups the outreach reaches; avoid placing the duty on a student."
- statement: qaa/archaeology-2022/1.10
  forPractitioner: { text: "Treat the degree's core skills as education for sustainable development and make the case for that value outside the university: to local and regional communities and to the bodies that decide what happens to the resource and heritage.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: an expectation on the discipline and its teaching to make a public case; the student meets the related outcomes in 4.3.b11 and 4.4.b19", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on the discipline to convey the value of sustainable approaches, aligned with the ESD guidance std:doc:qaa-advancehe-esd-2021-guidance. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 1.10. Set it beside the student items 4.3.b11, 4.4.b18 and 4.4.b19; do not claim it is a learning outcome or that it applies at a stated level."
  author-agent-dialogue: "Raise this when a programme team maps sustainability across the curriculum or plans public engagement. Frame it for staff as both a curriculum link to the ESD competences and a public-facing task. Ask where students meet the finite nature of the resource and who outside the university hears the case; avoid turning it into a student requirement."
- statement: qaa/archaeology-2022/1.12
  forPractitioner: { text: "If you seek accreditation from the professional body and its university partner, you must show that the degree or pathway covers the core relevant occupational standards through their competency matrix; mapping to this statement already covers many of them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition for the provider seeking accreditation, not a standard for the student", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a condition (must) that the professional body sets for accreditation, reported by the statement, not a QAA requirement on every course. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 1.12, and name the accreditation as the scheme run jointly by CIfA and UAUK (see also paras 1.13, 2.8 and 2.27). Do not claim that accreditation is compulsory or that the occupational standards are reproduced in this document."
  author-agent-dialogue: "Raise this when a programme team considers or prepares for professional accreditation, or when a student asks whether their degree is accredited. Frame it for staff as an optional route with its own matrix of competences. Ask whether the team has mapped modules to the core occupational standards; avoid telling a student it is a standard they must meet."
- statement: qaa/archaeology-2022/2.6
  forPractitioner: { text: "Build the ethics of practice into the curriculum explicitly: dignified and respectful treatment of human and primate remains, illicit trade, personal data, permits and local partners for work abroad, plagiarism, and the uses of archaeology for less privileged groups, using contextualised examples from around the world.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should always treat human remains, and the remains of other primates, with dignity and respect, whatever their age or origin. Your course will help you think through the ethics of fieldwork, research and the way archaeology is used in the world, including its effects on less privileged groups.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on curricula to embed the ethics of practice, and on everyone handling remains to treat them with dignity; it states no level. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 2.6, and set it beside the threshold items 4.3.b18 and 3.3.b17 and the professional conduct row qaa/fheq-2024/annex-d/professional/r2/3rd-1st. Do not reproduce the CIfA or BABAO guidance or claim it is binding law."
  author-agent-dialogue: "Raise this before a student handles human remains or plans a project with living participants, or when a team reviews where ethics is taught. To a student, say plainly that remains are treated with dignity and that ethics runs through the course; to staff, frame it as explicit curriculum content. Ask a student what they would do if material seemed to have been traded illegally; avoid long readings of the guidance."
- statement: qaa/archaeology-2022/2.12
  forPractitioner: { text: "Make sure every student, whatever the course's position in the triangle, learns quantitative methods, how to test hypotheses and what scientific techniques can and cannot show.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should come away able to use numbers and statistics, test a hypothesis and understand the scientific techniques archaeologists rely on, even if your interests lie mainly in the humanities.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) that scientific and quantitative skills are part of every archaeologist's equipment, for the honours degree at FHEQ level 6. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 2.12. Set it beside 3.2.b9, 3.3.b6 and 4.3.b4 and the descriptor qaa/fheq-2024/4.15.b2; do not claim it is itself a threshold item or that it requires laboratory science in every course."
  author-agent-dialogue: "Raise this when a student on a humanities-leaning route doubts they need statistics or science, or when a team reviews methods teaching. To a student, say plainly that numbers and scientific methods are part of every archaeologist's kit; to staff, frame it as a minimum in every pathway. Ask a student which quantitative method they could use unaided today; avoid presenting the list of research themes as content they must master."
- statement: qaa/archaeology-2022/2.19
  forPractitioner: { text: "Wherever your course sits between humanities, science and practice, it will still give weight to the four contexts, to working across disciplines and to the practice of archaeology as a whole.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a design expectation on every course; the student meets its effect", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation (will) on course design, with no level of its own. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 2.19, and read it with paras 2.2 and 2.18 on the four contexts. Do not claim it fixes a course's balance between science and humanities; the statement allows each course its own place."
  author-agent-dialogue: "Raise this with a programme team positioning a new course or reviewing balance between science, humanities and practice. Frame it for staff as a floor shared by all positions in the triangle. Ask how the course shows all four contexts whatever its emphasis; avoid giving it to a student as an outcome."
- statement: qaa/archaeology-2022/2.20
  forPractitioner: { text: "Vary teaching and learning methods as far as you can, from lectures, seminars and tutorials to laboratory, field and placement work, so that no student is held back by one format; build in reasonable adjustments for practical and team work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a design duty on the course; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on teaching design under the accessibility heading; the list that follows is indicative, not required. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 2.20, and set it beside para 2.21 and the student item 3.3.b16. Do not claim every listed method must appear in a course."
  author-agent-dialogue: "Raise this when a programme team plans teaching methods or reviews access for disabled or neurodiverse students. Frame it for staff as variety for fairness, not a checklist. Ask which students a single dominant format would leave behind; avoid reading the list of methods aloud or putting the duty to a student."
- statement: qaa/archaeology-2022/2.21
  forPractitioner: { text: "Offer alternative formats to everyone rather than only to those who ask, and make expectations plain; you must avoid a two-tier system. Agree fieldwork adjustments case by case, work to remove hidden costs from field trips, placements and volunteering, consider religious observance and school holidays in deadlines, and you must publish clear, accessible assessment criteria for each stage.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its assessors; the student meets its effect", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a provider duty (must, with several shoulds) on inclusive teaching, access and assessment criteria; it states no level. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 2.21, and set it beside paras 2.20, 3.10 and 1.9. Do not claim the statement creates a legal duty or that it sets out the adjustments for a given student."
  author-agent-dialogue: "Raise this with a programme team reviewing fieldwork, extracurricular access or assessment information, or with a teacher agreeing an adjustment. Frame it for staff around the two musts: no two-tier system and clear criteria at each stage. Ask whether alternative formats are offered to all and whether field trip costs exclude anyone; avoid presenting it to a student as their obligation."
- statement: qaa/archaeology-2022/2.23
  forPractitioner: { text: "For joint honours, expect students to achieve a share of this statement's specific and generic skills and to add others from the partner subject; decide which, and expect less laboratory and field work unless the partner is a science or social science.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study archaeology jointly with another subject, you will gain some of the archaeological skills and add others from your second subject; you may do less laboratory and field work, unless your other subject is a science.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) for joint honours at FHEQ level 6: a proportion of the skills in 3.2, 3.3, 4.3 and 4.4, not all of them. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 2.23, and read it with para 1.7. Do not claim it names which skills a joint honours student keeps; the course decides that."
  author-agent-dialogue: "Raise this when a joint honours student asks which archaeology outcomes apply to them, or when a team designs a joint route. To a student, say plainly that they will cover part of the archaeology skills and gain others from their second subject; to staff, ask which items the route will evidence. Ask a student which skills they expect from each subject; avoid implying the threshold lists apply in full."
- statement: qaa/archaeology-2022/3.2.b1
  forPractitioner: { text: "Students will weigh, question and apply scholarly, theoretical and scientific concepts to archaeological problems.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to judge, question and use scholarly, theoretical and scientific ideas when you work on archaeological problems.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: critical use of scholarly, theoretical and scientific ideas. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 1). Set it beside 4.3.b6 and 4.4.b6 and the level 6 descriptor qaa/fheq-2024/4.15.b7; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student asks how theory connects to the problems they meet in fieldwork or the laboratory. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask which theory they last applied to a real archaeological problem, and how they tested it? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b2
  forPractitioner: { text: "Students will practise the main field techniques for observing, recording and interpreting primary evidence; plan reasonable adjustments for disabled students.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will practise the main fieldwork techniques for observing, recording and interpreting evidence on site, with adjustments if you need them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: core fieldwork techniques. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 2). Set it beside 4.3.b5 and 4.3.b13 and the level 6 descriptor qaa/fheq-2024/4.15.b2; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student prepares for fieldwork or a team plans field training and its adjustments. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask which field techniques the student could carry out unsupervised, and what adjustment, if any, would help them take part? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b3
  forPractitioner: { text: "Students will practise core post-excavation and post-survey work: stratigraphic analysis of records, phasing and archiving.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will practise the work that follows excavation or survey, such as working out the sequence of layers from records, phasing a site and preparing an archive.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: post-excavation and post-survey techniques. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 3). Set it beside 3.2.b2 and 4.3.b13 and the level 6 descriptor qaa/fheq-2024/4.15.b2; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student asks what happens to finds and records after a dig, or a team reviews post-excavation teaching. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask whether the student has ever phased a site from its records, and what they found hardest? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b4
  forPractitioner: { text: "Students will practise core techniques for recording, measuring, analysing and interpreting archaeological material and data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will practise recording, measuring, analysing and interpreting archaeological material and data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: recording, measuring and analysing material and data. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 4). Set it beside 4.3.b13 and 4.4.b16 and the level 6 descriptor qaa/fheq-2024/4.15.b2; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student works with finds or datasets in a practical class or project. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask which recording or measuring method the student trusts most, and why? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b5
  forPractitioner: { text: "Students will recognise and convey the archaeological importance of material remains, landscapes and environmental evidence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to see why remains, landscapes and environmental evidence matter to archaeology, and explain this to others.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: the significance of remains, landscapes and environmental data. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 5). Set it beside 4.3.b7 and 3.3.b10 and the level 6 descriptor qaa/fheq-2024/4.15.b8; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student must explain to a non-specialist why a site, landscape or sample matters. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask how the student would explain the importance of one find or landscape to a visitor in two sentences? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b7
  forPractitioner: { text: "Students will interpret spatial data, combining theoretical models, surviving landscape traces and excavation results.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to interpret spatial data by bringing together models, what survives in today's landscape and what excavation shows.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: interpreting spatial data. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 7). Set it beside 3.2.b5 and 4.3.b9 and the level 6 descriptor qaa/fheq-2024/4.15.b3.1; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student works with maps, survey or GIS data, or a team plans landscape teaching. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask which kinds of spatial evidence the student has combined so far, and where they disagreed? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b8
  forPractitioner: { text: "Students will observe and describe classes of primary data and record their characteristics by defined methods.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to observe and describe different kinds of primary evidence and record their features using set methods.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: describing and recording classes of primary data. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 8). Set it beside 4.4.b15 and 4.4.b16 and the level 6 descriptor qaa/fheq-2024/4.15.b2; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student starts handling a class of finds or samples for the first time. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask which recording system the student used and how they checked their descriptions were consistent? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b9
  forPractitioner: { text: "Students will select and apply qualitative, quantitative and statistical analyses to data and recognise their potential and limits.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to choose and use the right qualitative, numerical and statistical methods for your data, and know what each method can and cannot tell you.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: choosing qualitative, quantitative and statistical analyses. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 9). Set it beside 2.12, 3.3.b6 and 4.3.b4 and the level 6 descriptor qaa/fheq-2024/4.15.b2; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student plans the analysis for a dissertation or a practical report. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask why the student chose their method, and what it could not show? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b10
  forPractitioner: { text: "Students will understand how social, cultural and environmental factors combine to cause change, and the two-way relation between people and environment over human evolution.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how social, cultural and environmental factors work together to bring about change, and how people have both shaped and been shaped by their surroundings over human history.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: change in coupled socio-ecological systems. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 10). Set it beside 3.2.b14 and 4.4.b20 and the level 6 descriptor qaa/fheq-2024/4.15.b1; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student links archaeology to climate, environment or long-term change. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask what example of human and environmental change the student would use, and which factor they think mattered most? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b11
  forPractitioner: { text: "Students will understand the nature, scope and some causes of human diversity, past and present, from social, cultural, ecological, biological and temporal angles.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how varied people are and have been, and some of the reasons why, looked at from social, cultural, ecological, biological and long-term points of view.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: human diversity, present and past. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 11). Set it beside 4.3.b17 and 4.4.b20 and the level 6 descriptor qaa/fheq-2024/4.15.b1; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a topic on identity, population or difference comes up in teaching or a project. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask which perspective on human diversity the student finds most convincing, and which they have not yet used? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b12
  forPractitioner: { text: "Students will be able to spot and challenge cultural assumptions in different settings, including those shaped by colonial legacies.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to notice and challenge cultural assumptions in many settings, including those still shaped by colonialism.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: questioning cultural assumptions, including colonial legacies. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 12). Set it beside 4.3.b15, 4.3.b16 and 4.4.b18 and the level 6 descriptor qaa/fheq-2024/4.15.b7; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student reads an older interpretation, a museum label or a reading list critically. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask which assumption the student found in a source this term, and where it came from? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b13
  forPractitioner: { text: "Students will be able to interpret and analyse textual, oral, visual and digital forms of evidence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to interpret and analyse written, spoken, visual and digital sources.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: interpreting textual, oral, visual and digital forms. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 13). Set it beside 4.3.b9 and 4.4.b3 and the level 6 descriptor qaa/fheq-2024/4.15.b5; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student combines documents, oral history, images or digital records with material evidence. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask which kind of source the student is least used to, and how they would start to analyse it? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b14
  forPractitioner: { text: "Students will know how biological, environmental and social or cultural factors interact in human ecology.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know how biology, environment and society and culture affect one another in the way people live in their surroundings.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: how biology, environment and culture interact in human ecology. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 14). Set it beside 3.2.b10 and the level 6 descriptor qaa/fheq-2024/4.15.b1; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student meets diet, health or environmental evidence in a module. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask how the student would show one biological and one cultural influence acting together in a case study? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b15
  forPractitioner: { text: "Students will be able to evaluate, compare and synthesise varied forms of evidence to interpret human behaviour past and present.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to judge, compare and combine different kinds of evidence to reach interpretations about how people behaved and behave.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: weighing and combining different evidence about behaviour. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 15). Set it beside 4.3.b8, 4.4.b3 and 4.4.b7 and the level 6 descriptor qaa/fheq-2024/4.15.b3.1; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student writes an interpretation that draws on more than one kind of evidence. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask where two lines of the student's evidence pointed different ways, and how they decided? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b16
  forPractitioner: { text: "Students will be aware of ethical issues in the legacy and uses of archaeology and will critically evaluate and use suitable modes of communication and engagement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know the ethical questions raised by archaeology's past and its uses today, and be able to judge and use good ways of communicating and engaging with people.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: ethics of the discipline and modes of communication. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 16). Set it beside 2.6, 4.3.b18 and 3.3.b10 and the level 6 descriptor qaa/fheq-2024/4.15.b8; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student plans public engagement or writes about a contested site. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask who could be affected by the student's account, and how they would involve them? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.2.b17
  forPractitioner: { text: "Students will understand the legislative and planning context of archaeological work, present and historical.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand the laws and planning rules that shape where and how archaeological work happens, now and in the past.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of the course: legislative and planning context. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.2 (bullet 17). Set it beside 1.6 and 4.3.b18 and the level 6 descriptor qaa/fheq-2024/4.15.b1; do not report it as a threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7)."
  author-agent-dialogue: "Raise this when a student asks how development-led or commercial archaeology works, or a team plans professional practice teaching. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame it as a subject-specific outcome to evidence across modules. Ask which law or planning rule the student would need to check before work on a site? Avoid reading the issuer's bullet aloud or presenting it as a pass requirement, since the threshold lists sit in section 4."
- statement: qaa/archaeology-2022/3.3.b1
  forPractitioner: { text: "Graduates will solve problems creatively and laterally in practical and theoretical work, using techniques from both humanities and sciences.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to solve problems creatively, thinking sideways and using methods from both the humanities and the sciences, in practical and theoretical work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: creative problem solving across humanities and sciences; it refines the level 6 descriptor qaa/fheq-2024/4.15.b9.2. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 1). Set it beside 4.4.b4; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student is stuck on a project problem or a team designs problem-based tasks. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask which method from outside their usual area the student could try? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b2
  forPractitioner: { text: "Graduates will produce logical, structured arguments supported by analytical and critical reference to evidence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to build clear, logical arguments that rest on careful, critical use of evidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: structured, evidenced argument; it refines the level 6 descriptor qaa/fheq-2024/4.15.b3.1. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 2). Set it beside 4.4.b11 and 4.3.b8; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student plans an essay or receives feedback on argument. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask what the strongest objection to the student's argument is, and where their evidence answers it? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b3
  forPractitioner: { text: "Graduates will plan, design, carry out and document primary research, independently and collaboratively as appropriate.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to plan, design, carry out and write up your own primary research, working alone or with others as the task needs.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: designing and carrying out primary research; it refines the level 6 descriptor qaa/fheq-2024/4.15.b6. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 3). Set it beside 4.3.b12 and 3.3.b4; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student starts a dissertation or independent project. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask what the student's research question is and how their design will answer it? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b4
  forPractitioner: { text: "Graduates will assemble coherent research and project designs.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to put together a clear, workable design for a research project.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: coherent research or project designs; it refines the level 6 descriptor qaa/fheq-2024/4.15.b6. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 4). Set it beside 3.3.b3 and 3.3.b15; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student drafts a project proposal. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask whether each part of the student's design serves the question, and what they would cut? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b5
  forPractitioner: { text: "Graduates will evaluate their own and others' opinions critically in the light of the discipline's changing contexts.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to judge your own and other people's views critically, aware of how archaeology's theory, methods, ethics and social setting keep changing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: critical evaluation of own and others' views; it refines the level 6 descriptor qaa/fheq-2024/4.15.b7. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 5). Set it beside 4.4.b6; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student reviews literature or peer work, or reflects on a debate. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask which of the student's own views has changed during the course, and why? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b6
  forPractitioner: { text: "Graduates will apply quantitative analysis and digital literacy in practical contexts.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to use numerical analysis and digital skills in practical work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: quantitative analysis and digital literacy in practice; it refines the level 6 descriptor qaa/fheq-2024/annex-d/transferable/r1/3rd. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 6). Set it beside 2.12, 3.2.b9 and 4.4.b12; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student handles data in a practical or project. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask which software or numerical method the student used last and how confident they felt? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b7
  forPractitioner: { text: "Graduates will show a positive, confident approach to practical problems.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will meet practical problems with confidence and a positive attitude.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: a positive approach to practical problems; it refines the level 6 descriptor qaa/fheq-2024/4.15.b9.1. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 7). Set it beside 3.3.b1; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student faces a setback in fieldwork or a practical task. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask how the student responded to the last practical problem that did not go to plan? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b8
  forPractitioner: { text: "Graduates will show innovation, creativity, collaboration and readiness to take risks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will show that you can be inventive and creative, work with others and take sensible risks.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: innovation, creativity, collaboration and risk-taking; it refines the level 6 descriptor qaa/fheq-2024/4.15.b9.1. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 8). Set it beside 3.3.b1 and 3.3.b16; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when enterprise, placements or creative assessment come up. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask where in the course the student has tried something new, and what they learned from it? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b9
  forPractitioner: { text: "Graduates will present effectively to different kinds of audience.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to give effective presentations to different kinds of audience.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: presenting to different audiences; it refines the level 6 descriptor qaa/fheq-2024/4.15.b8. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 9). Set it beside 4.4.b13 and 3.3.b10; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student prepares a talk, poster or public event. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask who the student's audience is and what they would change for a different one? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b10
  forPractitioner: { text: "Graduates will communicate effectively with wide audiences through written, oral and other media and create suitable visual presentations.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to communicate well with many kinds of audience in writing, in speech and in other media, and make effective visual material.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: communicating in many media, including visual; it refines the level 6 descriptor qaa/fheq-2024/4.15.b8. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 10). Set it beside 4.4.b10 and 3.2.b5; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student plans how to present findings in more than one format. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask which medium suits the student's findings best, and which they find hardest? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b11
  forPractitioner: { text: "Graduates will make effective and appropriate use of relevant digital technology and software to manipulate digital data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to use the right digital tools and software to work with digital data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: digital technology and software for digital data; it refines the level 6 descriptor qaa/fheq-2024/annex-d/transferable/r1/3rd. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 11). Set it beside 3.3.b6 and 4.4.b12; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student works with GIS, databases, imaging or modelling. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask which digital tool the student would choose for their data and why? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b12
  forPractitioner: { text: "Graduates will make critical and effective use of information retrieval skills across analogue and digital resources.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to find information well and critically, in print and archives as well as online.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: information retrieval from analogue and digital resources; it refines the level 6 descriptor qaa/fheq-2024/4.15.b5. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 12). Set it beside 4.4.b3; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student starts a literature search or archival work. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask how the student judged the reliability of the last source they found? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b13
  forPractitioner: { text: "Graduates will work methodically and accurately with attention to detail.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to work carefully, accurately and with attention to detail.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: method, accuracy and attention to detail; it refines the level 6 descriptor qaa/fheq-2024/annex-d/practical/r2/3rd. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 13). Set it beside 4.4.b16 and 3.2.b8; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student records finds, data or references. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask how the student checks their own records for errors? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b14
  forPractitioner: { text: "Graduates will reflect on and take initiative in seeking continuing professional and personal development.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reflect on your own development and take the lead in finding ways to keep learning, personally and professionally.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: continuing professional and personal development; it refines the level 6 descriptor qaa/fheq-2024/4.15.b9.3. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 14). Set it beside 4.4.b9; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when careers, placements or personal tutoring come up. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask what the student wants to learn next and where they will find it? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b15
  forPractitioner: { text: "Graduates will manage time, organise and plan, which includes putting together coherent project designs.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to manage your time, organise yourself and plan work, including designing a research project.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: time management, organisation and planning; it refines the level 6 descriptor qaa/fheq-2024/annex-d/transferable/r3/3rd. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 15). Set it beside 3.3.b4 and 4.4.b8; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student juggles deadlines or plans a long project. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask how the student has planned the stages of their project against the deadline? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b16
  forPractitioner: { text: "Graduates will collaborate effectively in teams through group work in laboratory, field or project settings, with reasonable adjustments if required.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to work well as part of a team, in the laboratory, in the field or on a project, with adjustments if you need them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: teamwork in laboratory, field or project; it refines the level 6 descriptor qaa/fheq-2024/annex-d/transferable/r2/3rd. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 16). Set it beside 4.4.b2 and 2.20; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student meets a group task or a team dispute. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask what role the student took in their last group task and what they would do differently? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b17
  forPractitioner: { text: "Graduates will appreciate ethical and health and safety procedures and responsibilities, personal and towards others, and broader professional frameworks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand why ethics and health and safety rules matter, for you and for others, and how wider professional frameworks apply to your work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: ethics, health and safety and professional frameworks; it refines the level 6 descriptor qaa/fheq-2024/annex-d/professional/r2/3rd-1st. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 17). Set it beside 2.6, 4.3.b18 and 4.4.b17; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a student prepares for fieldwork, laboratory work or a placement. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask which risk the student would check for first on a site, and who else it affects? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b18
  forPractitioner: { text: "Graduates will appreciate the need for inclusiveness and take personal responsibility for respecting diverse people and cultures.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will value inclusion and take personal responsibility for making sure that people from different backgrounds and cultures are respected.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: inclusiveness and respect for others and cultures; it refines the level 6 descriptor qaa/fheq-2024/4.15.b9.1. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 18). Set it beside 1.8, 4.3.b17 and 4.4.b17; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when a group, fieldwork or outreach setting raises questions of respect or exclusion. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask what the student does when someone in a group is left out? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.3.b19
  forPractitioner: { text: "Graduates will engage with the broader cultural context of professional practice, for example EDI, sustainability, global perspectives, inequality, public engagement, employability, enterprise and creativity.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to engage with the wider issues that shape professional life in any field, such as inclusion, sustainability, global views, inequality, public engagement, employability and enterprise.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: the wider cultural context of professional practice; it refines the level 6 descriptor qaa/fheq-2024/4.15.b9.1. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.3 (bullet 19). Set it beside 4.4.b18 and 4.4.b20; do not claim it is a threshold item, a skill only archaeology teaches or a standard at another level."
  author-agent-dialogue: "Raise this when careers, employability or the cross-cutting themes come up. To a student, say in plain words and the second person that the degree will build this skill and where it shows; to staff, frame it as a transferable outcome to make visible in modules and placements. Ask which of these wider issues the student could speak about in a job interview? Avoid reading the issuer's wording aloud or turning it into a separate assessed hurdle."
- statement: qaa/archaeology-2022/3.9
  forPractitioner: { text: "Write an explicit assessment strategy into the curriculum: it will map to each component's outcomes, support learning, show progression in attainment and match the skills developed and the teaching methods chosen.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a design duty on the course; the student meets its effect", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a course design expectation (will) for assessment; it sets no level. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 3.9, and set it beside para 3.10, the indicative list in 3.11 and the classification descriptions in Annex D (std:doc:qaa-fheq-2024-framework, SL6). Do not claim it prescribes particular methods."
  author-agent-dialogue: "Raise this when a programme team reviews its assessment strategy or a validation panel asks how outcomes are assessed. Frame it for staff as alignment, progression and fit with teaching. Ask where in the course a student's growing attainment becomes visible; avoid giving it to a student as their task."
- statement: qaa/archaeology-2022/4.2
  forPractitioner: { text: "Above the threshold, judge performance with your own method and refer to Annex D's outcome classification descriptions for the four honours classes; this statement gives no typical or excellent lists of its own.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the awarding body for judging classes above the threshold", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) to use Annex D for performance above the threshold at FHEQ level 6 and FQHEIS level 10. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.2, and point to std:doc:qaa-fheq-2024-framework, Annex D (SL6), for example qaa/fheq-2024/annex-d/summary/r1/3rd. Do not claim the statement sets subject-specific typical or excellent standards; it states the threshold only."
  author-agent-dialogue: "Raise this when a team or student asks what separates a first from a third in archaeology. To staff, say the statement stops at the threshold and points to Annex D for the classes; to a student, explain that most people do much better than the minimum. Ask which Annex D descriptions the team's marking criteria follow; avoid presenting the threshold as the expected result."
- statement: qaa/archaeology-2022/4.3.b1
  forPractitioner: { text: "At threshold, graduates appreciate the chronological and conceptual reach of archaeological work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you grasp how far archaeology reaches across time and across ideas.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers the time span and conceptual range of the discipline. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 1). Set it beside 4.3.b14 and 3.2.b10, the descriptor qaa/fheq-2024/4.15.b1 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r2/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student asks what the degree expects them to know overall. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask which period or idea the student feels furthest from, and how they would place it in the whole? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b2
  forPractitioner: { text: "At threshold, graduates show knowledge of the archaeology of several regions of the world.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you know the archaeology of several parts of the world.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers regional breadth. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 2). Set it beside 4.3.b3 and para 1.6, the descriptor qaa/fheq-2024/4.15.b1 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r1/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student chooses modules or asks if their regional coverage is wide enough. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask which regions the student could discuss with confidence, and which they have barely met? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b3
  forPractitioner: { text: "At threshold, graduates show knowledge of the archaeology of several periods.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you know the archaeology of several periods of the past.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers period breadth. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 3). Set it beside 4.3.b2 and para 1.6, the descriptor qaa/fheq-2024/4.15.b1 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r1/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student chooses modules or asks if their period coverage is wide enough. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask which periods the student could compare, and on what point? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b4
  forPractitioner: { text: "At threshold, graduates understand the principles and methods by which archaeological data are obtained and analysed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you understand how archaeologists collect and analyse their data, and why.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers how data are gathered and analysed. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 4). Set it beside 3.2.b9 and 2.12, the descriptor qaa/fheq-2024/4.15.b2 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r2/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student plans data collection or a team checks methods teaching. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask how the student would explain one method of collecting data and its weaknesses? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b5
  forPractitioner: { text: "At threshold, graduates show practical experience of recovering primary data, in the field or (with adjustments, per 1.6) through collections or records.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show hands-on experience of recovering primary archaeological evidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers practical experience of recovering primary data. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 5). Set it beside 3.2.b2 and 4.3.b13, the descriptor qaa/fheq-2024/4.15.b2 and the third-class column of Annex D (qaa/fheq-2024/annex-d/practical/r1/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student cannot take part in standard fieldwork or asks how practical experience is evidenced. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask what primary data the student has recovered themselves, and in what setting? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b6
  forPractitioner: { text: "At threshold, graduates describe the variety of theoretical and practical approaches to understanding and interpreting the past.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to describe the different theoretical and practical ways archaeologists understand and build accounts of the past.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers theoretical and practical approaches to the past. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 6). Set it beside 3.2.b1 and 4.3.b14, the descriptor qaa/fheq-2024/4.15.b3.1 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r2/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student studies archaeological theory or compares interpretations. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask which two approaches the student could contrast, and what each would make of the same site? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b7
  forPractitioner: { text: "At threshold, graduates recognise the full range of archaeological evidence and useful data from other disciplines.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to recognise the many kinds of archaeological evidence, and useful evidence from other subjects.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers the range of data, including other disciplines. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 7). Set it beside 4.3.b10 and 3.2.b13, the descriptor qaa/fheq-2024/4.15.b1 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r1/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student plans which evidence a project will draw on. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask which non-archaeological evidence could help the student's question? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b8
  forPractitioner: { text: "At threshold, graduates describe the varied and problematic nature of evidence and understand its possibilities and limits.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to explain why archaeological evidence is varied and often difficult, and what it can and cannot tell you.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers the problems, possibilities and limits of evidence. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 8). Set it beside 3.2.b9 and para 1.6 on bias, the descriptor qaa/fheq-2024/4.15.b4 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r2/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student over-reads a find or a dataset. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask what the student's evidence cannot show, and how that limits their conclusion? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b9
  forPractitioner: { text: "At threshold, graduates gather, analyse and present evidence from primary and secondary sources.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to collect, analyse and present archaeological evidence from both original and published sources.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers working with primary and secondary evidence. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 9). Set it beside 4.3.b12 and 3.3.b3, the descriptor qaa/fheq-2024/4.15.b5 and the third-class column of Annex D (qaa/fheq-2024/annex-d/practical/r4/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student starts a project or report. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask which primary and which secondary sources the student is using, and how they will present them? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b10
  forPractitioner: { text: "At threshold, graduates recognise the range of archaeological data (the issuer repeats this within bullet 7).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to recognise the many kinds of archaeological evidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers the range of archaeological data (repeat of b7). Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 10). Set it beside 4.3.b7, which it repeats, the descriptor qaa/fheq-2024/4.15.b1 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r1/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student lists the kinds of evidence a site might give. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask which kinds of evidence the student would expect from a site they know? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b11
  forPractitioner: { text: "At threshold, graduates recognise that the resource is finite and that it needs sustainable conservation.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to recognise that archaeological remains cannot be replaced and must be conserved in a sustainable way.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers a finite resource needing sustainable conservation. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 11). Set it beside para 1.10, 4.4.b19 and 3.3.b19, the descriptor qaa/fheq-2024/4.15.b1 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r2/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when sustainability, conservation or excavation ethics come up. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask why excavation itself uses up the resource, and what that means for the student's choices? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b12
  forPractitioner: { text: "At threshold, graduates research and present an extended piece of archaeological work, often a dissertation or project (2.26).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to carry out and present an extended piece of archaeological research of your own.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers an extended piece of research. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 12). Set it beside 3.3.b3, 3.3.b4 and para 2.26, the descriptor qaa/fheq-2024/4.15.b6 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r3/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student plans a dissertation or independent project. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask what the student's question is and how far along their research is? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b13
  forPractitioner: { text: "At threshold, graduates show knowledge of archaeological and practical skills, especially observing, recording and interpreting primary data.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show your practical archaeological skills, especially in observing, recording and interpreting original evidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers observing, recording and interpreting primary data. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 13). Set it beside 4.3.b5, 3.2.b2 and 3.2.b8, the descriptor qaa/fheq-2024/4.15.b2 and the third-class column of Annex D (qaa/fheq-2024/annex-d/practical/r1/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student prepares a field or laboratory notebook for assessment. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask how the student would show an assessor that their recording is accurate? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b14
  forPractitioner: { text: "At threshold, graduates describe how archaeology developed as a subject and understand what that means for it today and for its cultural setting.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to describe how archaeology grew as a subject and what that history means for it today.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers the development of the discipline. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 14). Set it beside 4.3.b6 and para 2.11 (fourth element), the descriptor qaa/fheq-2024/4.15.b1 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r2/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student studies the history of the discipline or its colonial origins. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask which part of the subject's history still shapes practice the student has seen? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b15
  forPractitioner: { text: "At threshold, graduates show awareness of the social, cultural and political context of interpretation and practice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you know how society, culture and politics shape archaeological interpretation and practice.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers the social, cultural and political context. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 15). Set it beside 3.2.b12 and 4.3.b16, the descriptor qaa/fheq-2024/4.15.b4 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r2/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student writes about a contested site or a political use of the past. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask who gains from a given interpretation of the past the student has studied? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b16
  forPractitioner: { text: "At threshold, graduates show awareness of the effect of practice and representation on other communities, including marginalised groups, and appreciate the need for equitable engagement with them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you understand how archaeology can affect other communities, including groups pushed to the margins in the past, and why you need to work with them fairly.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers impact on communities and fair engagement. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 16). Set it beside para 1.8, 4.3.b15 and 4.3.b17, the descriptor qaa/fheq-2024/4.15.b9.2 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r2/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student plans community work, writes on contested heritage or handles material from another culture. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask which community the student's work might affect, and how they would involve them? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b17
  forPractitioner: { text: "At threshold, graduates understand why the discipline must be inclusive and show respect to diverse others.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you understand why archaeology needs to include everyone, and that you treat people from different backgrounds with respect.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers an inclusive discipline and respect for others. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 17). Set it beside 3.3.b18 and 4.4.b17, the descriptor qaa/fheq-2024/4.15.b9.1 and the third-class column of Annex D (qaa/fheq-2024/annex-d/professional/r2/3rd-1st); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a group, fieldwork or outreach setting raises questions of inclusion. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask what the student has seen that made a team or site more or less inclusive? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.3.b18
  forPractitioner: { text: "At threshold, graduates show awareness of the law and ethics that bear on archaeology.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you know the legal and ethical issues archaeology raises.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers legal and ethical dimensions. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.3 (bullet 18). Set it beside para 2.6, 3.2.b17 and 3.3.b17, the descriptor qaa/fheq-2024/4.15.b9.2 and the third-class column of Annex D (qaa/fheq-2024/annex-d/professional/r2/3rd-1st); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student meets human remains, illicit material or planning law. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame it as a threshold their assessments must let every student show. Ask which legal or ethical question the student would ask before starting a piece of work? Avoid reading the list aloud or treating this minimum as the class of degree most students reach."
- statement: qaa/archaeology-2022/4.4.b1
  forPractitioner: { text: "At threshold, graduates show they can see where archaeological concepts and methods apply beyond the discipline.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you can see where archaeological ideas and methods are useful outside archaeology.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers using archaeological ideas outside archaeology and refines the descriptor qaa/fheq-2024/4.15.b6. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 1). Set it beside 3.3.b19 and para 1.14 and the third-class column of Annex D (qaa/fheq-2024/annex-d/transferable/r4/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student considers careers outside archaeology. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask where the student could use an archaeological method in a job outside the field? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b2
  forPractitioner: { text: "At threshold, graduates perform assigned tasks in a team and take part in discussion.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to do your share of a team task and take part in the discussion.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers teamwork and discussion and refines the descriptor qaa/fheq-2024/4.15.b9.1. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 2). Set it beside 3.3.b16 and the third-class column of Annex D (qaa/fheq-2024/annex-d/transferable/r2/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a group task begins or a team member is not contributing. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask what the student's part in the last team task was? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b3
  forPractitioner: { text: "At threshold, graduates combine information and materials from different sources.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to combine information and material from different sources.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers bringing together information from different sources and refines the descriptor qaa/fheq-2024/4.15.b5. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 3). Set it beside 3.2.b15 and 3.3.b12 and the third-class column of Annex D (qaa/fheq-2024/annex-d/cognitive/r1/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student starts a literature review or synthesis. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask which sources the student has combined and how they reconciled them? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b4
  forPractitioner: { text: "At threshold, graduates identify problems and questions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to spot problems and turn them into questions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers identifying problems and questions and refines the descriptor qaa/fheq-2024/4.15.b7. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 4). Set it beside 3.3.b1 and the third-class column of Annex D (qaa/fheq-2024/annex-d/cognitive/r3/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student struggles to find a project question. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask what problem the student has noticed in their reading that no one has answered? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b5
  forPractitioner: { text: "At threshold, graduates undertake analysis of factual information.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to analyse factual information.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers analysing factual information and refines the descriptor qaa/fheq-2024/4.15.b7. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 5). Set it beside 4.3.b9 and the third-class column of Annex D (qaa/fheq-2024/annex-d/cognitive/r1/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student handles data or factual sources. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask what the student's analysis of a dataset showed that a summary would miss? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b6
  forPractitioner: { text: "At threshold, graduates recognise the strengths and weaknesses of others' arguments.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to see the strong and weak points in other people's arguments.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers judging others' arguments and refines the descriptor qaa/fheq-2024/4.15.b7. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 6). Set it beside 3.3.b5 and 3.2.b1 and the third-class column of Annex D (qaa/fheq-2024/annex-d/cognitive/r2/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student reviews literature or responds in a seminar. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask what the weakest point is in an argument the student admires? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b7
  forPractitioner: { text: "At threshold, graduates produce a synthesis of current knowledge on a topic.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to pull together what is currently known about a topic.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers synthesising the state of knowledge and refines the descriptor qaa/fheq-2024/4.15.b3.2. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 7). Set it beside 3.2.b15 and 4.3.b9 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r3/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student writes a review essay or dissertation chapter. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask what the student would say is the current consensus on their topic, and where it is weakest? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b8
  forPractitioner: { text: "At threshold, graduates undertake tasks independently, with guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to carry out tasks on your own, with some guidance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers independent work with guidance and refines the descriptor qaa/fheq-2024/4.15.b5. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 8). Set it beside 3.3.b15 and 3.3.b3 and the third-class column of Annex D (qaa/fheq-2024/annex-d/transferable/r3/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student moves from taught work to independent study. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask what guidance the student still needs, and what they now do alone? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b9
  forPractitioner: { text: "At threshold, graduates reflect on their progress and use feedback provided.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to reflect on your own progress and act on feedback you receive.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers reflecting on progress and using feedback and refines the descriptor qaa/fheq-2024/4.15.b5. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 9). Set it beside 3.3.b14 and the third-class column of Annex D (qaa/fheq-2024/annex-d/transferable/r5/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when feedback is returned or a student meets their personal tutor. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask what the student changed after their last piece of feedback? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b10
  forPractitioner: { text: "At threshold, graduates express themselves effectively orally and in writing.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to express yourself clearly in speech and in writing.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers speaking and writing effectively and refines the descriptor qaa/fheq-2024/4.15.b8. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 10). Set it beside 3.3.b10 and 4.4.b11 and the third-class column of Annex D (qaa/fheq-2024/annex-d/transferable/r1/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student receives feedback on writing or speaking. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask which form, spoken or written, the student finds harder and why? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b11
  forPractitioner: { text: "At threshold, graduates present knowledge or argument in a way others can understand.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to present what you know, or an argument, so that others can follow it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers making knowledge or argument understood and refines the descriptor qaa/fheq-2024/4.15.b8. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 11). Set it beside 3.3.b2 and 3.3.b9 and the third-class column of Annex D (qaa/fheq-2024/annex-d/transferable/r1/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student prepares a presentation or essay for a non-specialist reader. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask how the student would check that someone outside the subject followed them? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b12
  forPractitioner: { text: "At threshold, graduates use suitable IT to gather, analyse, choose and present information.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to use the right digital tools to gather, analyse, choose and present information.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers digital literacy with relevant IT and refines the descriptor qaa/fheq-2024/4.15.b8. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 12). Set it beside 3.3.b6 and 3.3.b11 and the third-class column of Annex D (qaa/fheq-2024/annex-d/transferable/r1/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student chooses software for a project or presentation. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask which digital tools the student relies on and which they avoid? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b13
  forPractitioner: { text: "At threshold, graduates make oral presentations using visual aids.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to give a spoken presentation with visual aids.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers oral presentation with visual aids and refines the descriptor qaa/fheq-2024/4.15.b8. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 13). Set it beside 3.3.b9 and 3.3.b10 and the third-class column of Annex D (qaa/fheq-2024/annex-d/transferable/r1/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student prepares for an assessed presentation. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask what the student's visual aids add that their words do not? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b14
  forPractitioner: { text: "At threshold, graduates show they can understand new ideas or information presented to them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you can understand new ideas or information when you meet them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers taking in new ideas and information and refines the descriptor qaa/fheq-2024/4.15.b5. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 14). Set it beside 4.3.b6 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r2/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student meets an unfamiliar method or theory. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask how the student would check their understanding of a new idea? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b15
  forPractitioner: { text: "At threshold, graduates show skill in recognising and describing archaeological material.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you can recognise and describe archaeological material.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers recognising and describing material and refines the descriptor qaa/fheq-2024/4.15.b2. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 15). Set it beside 3.2.b8 and 4.3.b13 and the third-class column of Annex D (qaa/fheq-2024/annex-d/practical/r1/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student handles finds in a practical or identification test. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask which features the student uses first to identify an object? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b16
  forPractitioner: { text: "At threshold, graduates show classification skills in describing, categorising and collating data.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you can describe, sort and organise data into categories.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers classifying and collating data and refines the descriptor qaa/fheq-2024/4.15.b2. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 16). Set it beside 3.2.b8 and 3.3.b13 and the third-class column of Annex D (qaa/fheq-2024/annex-d/practical/r4/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student builds a catalogue, database or typology. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask how the student decided where one category ends and the next begins? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b17
  forPractitioner: { text: "At threshold, graduates understand why health and safety, and equality, diversity and inclusion, matter at work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you understand why health and safety, and equality, diversity and inclusion, matter at work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers health and safety and EDI at work and refines the descriptor qaa/fheq-2024/4.15.b9.1. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 17). Set it beside 3.3.b17 and 3.3.b18 and the third-class column of Annex D (qaa/fheq-2024/annex-d/professional/r2/3rd-1st); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a student prepares for fieldwork, a placement or a laboratory session. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask what the student would do if they saw an unsafe or excluding practice on site? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b18
  forPractitioner: { text: "At threshold, graduates appreciate contemporary debates on global sustainability, employability and global perspectives including decolonisation and anti-racism.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you understand current debates on sustainability, employability and global perspectives, including decolonisation and anti-racism.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers current debates on sustainability, employability, decolonisation and anti-racism and refines the descriptor qaa/fheq-2024/4.15.b4. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 18). Set it beside 3.2.b12, 3.3.b19 and 4.4.b20 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r2/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when decolonisation, anti-racism or sustainability come up in teaching or careers. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask which current debate the student feels archaeology adds most to? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b19
  forPractitioner: { text: "At threshold, graduates appreciate the need to act in a sustainable way.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to show that you understand the need to act sustainably.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers acting sustainably and refines the descriptor qaa/fheq-2024/4.15.b9.1. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 19). Set it beside 4.3.b11 and para 1.10 and the third-class column of Annex D (qaa/fheq-2024/annex-d/transferable/r4/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when fieldwork travel, resource use or conservation choices come up. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask what one sustainable choice the student could make in their own practice? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
- statement: qaa/archaeology-2022/4.4.b20
  forPractitioner: { text: "At threshold, graduates appreciate and engage in contemporary debates such as inequality, sustainability, globalisation and cultural diversity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By graduation you should be able to take part in current debates, for example on inequality, sustainability, globalisation and cultural diversity.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); it covers engaging in contemporary debates and refines the descriptor qaa/fheq-2024/4.15.b3.2. Cite QAA, 2022, Archaeology Subject Benchmark Statement, para 4.4 (bullet 20). Set it beside 4.4.b18 and 3.2.b11 and the third-class column of Annex D (qaa/fheq-2024/annex-d/knowledge/r2/3rd); do not claim it is a regulatory rule, the typical result or a standard at another level."
  author-agent-dialogue: "Raise this when a seminar or public event turns to current affairs. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask what evidence from the past the student would bring to a current debate? Avoid reading the list aloud or presenting the minimum as what a good degree looks like."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.22; 4.2" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.22; 4.2" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.24 (integrated master's, MArc; no standards stated)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.24 (integrated master's, MArc; no standards stated)" }
  - { id: "spine:6", role: "refers", locator: "std:ref:uk-framework R2 and R8 (inferred: Part E)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.22: \"FHEQ Level 6; FQHEIS Level 10\"; 4.2, the title of Annex D)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.24)" }
  - { from: "fheq:6", to: "spine:6", relation: "sameStep", basis: "inferred from std:ref:uk-framework R2 (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.8", "1.9", "2.4", "3.3", "4.3", "4.4"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.6", "1.9", "2.20", "2.21", "3.2", "3.3", "3.8", "3.10"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.1", "1.6", "1.10", "2.7", "2.14", "3.3", "4.3", "4.4"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.11", "1.12", "1.13", "1.14", "3.3", "4.4"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-archaeology-2014-benchmarks (not yet ingested)", note: "the third edition (2014), named in section 6; the front matter lists key changes" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees, for performance above the threshold (4.2); SL6" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "levels 6 and 7 (2.22, 2.24)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "levels 10 and 11 (2.22, 2.24)" }
- { rel: "cites", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "the core skills align with its learning outcomes (1.10)" }
- { rel: "refersTo", target: "CIfA and UAUK degree accreditation and its competency matrix (not yet ingested: Part E)", note: "1.12, 1.13, 2.8, 2.27" }
- { rel: "refersTo", target: "National Occupational Standards for Archaeological Practice (not yet ingested: Part E)", note: "1.12" }
- { rel: "readWith", target: "the Subject Benchmark Statements of partner subjects in joint honours (collection)", note: "1.7, 2.23" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance; QAA Glossary", note: "front matter" }
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
- The one subject that covers the whole human past in every period and place, giving the time depth needed for present concerns such as ecosystems, globalisation and sustainability (D1, 1.1, 2.10).
- It works with tangible and intangible remains, joins discovery to storytelling and debate, and welcomes many voices and narratives (D1, 1.2, 1.3).
- It sits in a triangle of science, arts and professional practice, so teaching and research are often interdisciplinary; it differs from Classics, History and Heritage Management (D1, 1.4, 2.19).
- Degrees rest on four contexts: social, ethical and professional, theoretical and scientific (D1, 2.2 to 2.18).
- It is self-critical about its colonial origins and contested uses, and works to decolonise its teaching and practice (D1, 1.3, 1.8, 2.4, 2.11).
- It is research-led, with undergraduates handling primary material and able to make discoveries of their own (D1, 2.1, 2.25).
- Practical work, in the field or with collections, is the main way evidence is made and is part of every course, with adjustments for access (D1, 1.6, 3.8).
- Archaeological science, conservation science, biological and environmental science, experimental and digital work run through it (D1, 2.12 to 2.17).
- Careers are wide, from commercial archaeology and museums to general graduate work, and a professional accreditation route exists (D1, 1.5, 1.12, 1.14, 2.8).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "the discipline names barriers of ethnicity, disability, gender and class rooted in its origins; it asks for many voices, decolonised teaching, fair engagement with communities and attention to under-represented students at every stage (D1, 1.8, 1.9, 2.4)"
  statements: ["qaa/archaeology-2022/1.8", "qaa/archaeology-2022/1.9", "qaa/archaeology-2022/3.3.b18", "qaa/archaeology-2022/3.3.b19", "qaa/archaeology-2022/4.3.b16", "qaa/archaeology-2022/4.3.b17", "qaa/archaeology-2022/4.4.b17", "qaa/archaeology-2022/4.4.b18", "qaa/archaeology-2022/4.4.b20"]
- theme: theme:accessibility
  inThisSubject: "headed Accessibility in the text: varied teaching methods, adjustments for fieldwork and practical work, no two-tier system, equal access to field trips and placements, clear assessment criteria and accessible assessment (D1, 1.6, 2.20, 2.21, 3.8, 3.10)"
  statements: ["qaa/archaeology-2022/2.20", "qaa/archaeology-2022/2.21", "qaa/archaeology-2022/3.2.b2", "qaa/archaeology-2022/3.3.b16"]
- theme: theme:esd
  inThisSubject: "headed Sustainability in the text: core skills align with the ESD guidance; the archaeological resource is finite and needs sustainable conservation; heritage and tourism can be sustainable (D1, 1.1, 1.6, 1.10, 2.7, 2.14)"
  statements: ["qaa/archaeology-2022/1.6", "qaa/archaeology-2022/1.10", "qaa/archaeology-2022/3.3.b19", "qaa/archaeology-2022/4.3.b11", "qaa/archaeology-2022/4.4.b18", "qaa/archaeology-2022/4.4.b19", "qaa/archaeology-2022/4.4.b20"]
- theme: theme:enterprise
  inThisSubject: "enterprise education for careers, set beside the professional accreditation scheme and a wide range of employment beyond the profession (D1, 1.11 to 1.14)"
  statements: ["qaa/archaeology-2022/1.12", "qaa/archaeology-2022/3.3.b8", "qaa/archaeology-2022/3.3.b19", "qaa/archaeology-2022/4.4.b18"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "1.6", gloss: "the platform of knowledge: origins and value, legal and policy frames, contexts, evidence, theory, regions and periods, primary data, science and bias" }
  - { component: "2.3", gloss: "the social context: past societies through present questions (2.3, 2.4)" }
  - { component: "2.5", gloss: "the ethical and professional context (2.5 to 2.8)" }
  - { component: "2.9", gloss: "the theoretical context and its four elements (2.9 to 2.11)" }
  - { component: "2.12", gloss: "archaeological science and ten research themes, from formation processes to climate change" }
  - { component: "2.13", gloss: "artefact characterisation and dating" }
  - { component: "2.14", gloss: "conservation science" }
  - { component: "2.15", gloss: "biological and environmental science, biomolecular methods" }
  - { component: "2.16", gloss: "experimental archaeology" }
  - { component: "2.17", gloss: "digital data and visualisation" }
practices:
  - { component: "2.20", kind: "teaching", gloss: "a varied mix: reading, lectures, seminars, tutorials, laboratory and field practicals, site visits, placements, outreach, self-guided and team work" }
  - { component: "2.25", kind: "learning", gloss: "research-led, experiential and team learning; flipped classroom, problem-based learning, students in curriculum design" }
  - { component: "2.26", kind: "learning", gloss: "independent research, project or dissertation" }
  - { component: "2.28", kind: "learning", gloss: "placements, community archaeology, shared fieldwork training and online courses with partners" }
  - { component: "3.6", kind: "teaching", gloss: "the resources: literature, digital tools, collections, field equipment and laboratories" }
  - { component: "3.8", kind: "learning", gloss: "practical participation in projects as part of every course" }
  - { component: "3.9", kind: "assessment", gloss: "an explicit strategy tied to outcomes and progression" }
  - { component: "3.10", kind: "assessment", gloss: "accessible mixed methods, adjustments, formative and peer feedback" }
  - { component: "3.11", kind: "assessment", gloss: "indicative methods: research project, essays, exams, notebooks, presentations, practical exams, portfolios, placement reports" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.3 and 4.4 (under the heading Threshold level)", award: "bachelor's with honours", items: 38 }
  - { rung: "typical", leadIn: "none", award: "bachelor's with honours", items: 0 }
  - { rung: "excellent", leadIn: "none", award: "bachelor's with honours", items: 0 }
rungBases: "4.1: the statement sets the minimum threshold only; 4.2: most students perform significantly better, judged by each provider with reference to Annex D (the four honours classes)"
outcomeLists:
  - { leadIn: "3.2", gloss: "subject-specific content students will be equipped with, as the course allows", items: 16, award: ["honours"] }
  - { leadIn: "3.3", gloss: "generic, transferable and employability skills graduates will be equipped with", items: 19, award: ["honours"] }
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
- { body: "Chartered Institute for Archaeologists (CIfA)", says: "the leading professional body; sets standards and, with University Archaeology UK, accredits degrees against a competency matrix aligned with the occupational standards (since 2019); publishes guidance on human remains (D1, 1.12, 1.13, 2.6, 2.7, 2.8, 2.27)", requirements: "not yet ingested (Part E)" }
- { body: "University Archaeology UK (UAUK)", says: "partner in the joint accreditation scheme and its governance (D1, 1.12, 1.13, 2.8, 2.27)", requirements: "not yet ingested (Part E)" }
- { body: "British Association for Biological Anthropology and Osteoarchaeology (BABAO)", says: "publishes guidance on the ethics of human remains (D1, 2.6; section 5)", requirements: "not yet ingested (Part E)" }
- { body: "Institute of Archaeologists of Ireland", says: "professional body for archaeologists; links with institutions in Northern Ireland (D1, 2.7, 2.27)", requirements: "not yet ingested (Part E)" }
- { body: "Institute for Historic Building Conservation; Institute for Conservation; Society for Museum Archaeology", says: "set standards for the built historic environment and the conservation of cultural heritage (D1, 2.7)", requirements: "not yet ingested (Part E)" }
- { body: "European Association of Archaeologists", says: "a continental membership body with its own code of practice and principles of conduct (D1, 2.7)", requirements: "not yet ingested (Part E)" }
- { body: "Historic England; Cadw; Historic Scotland; Department for Communities, Northern Ireland", says: "national heritage bodies with long-standing links to departments (D1, 2.27)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.8", "1.9", "2.4", "3.3", "4.3", "4.4"], statements: ["1.8", "1.9", "3.3.b18", "3.3.b19", "4.3.b16", "4.3.b17", "4.4.b17", "4.4.b18", "4.4.b20"] }
  - { id: "theme:accessibility", named: "Accessibility", carriedIn: ["1.6", "1.9", "2.20", "2.21", "3.2", "3.3", "3.8", "3.10"], statements: ["2.20", "2.21", "3.2.b2", "3.3.b16"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.1", "1.6", "1.10", "2.7", "2.14", "3.3", "4.3", "4.4"], statements: ["1.6", "1.10", "3.3.b19", "4.3.b11", "4.4.b18", "4.4.b19", "4.4.b20"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.11", "1.12", "1.13", "1.14", "3.3", "4.4"], statements: ["1.12", "3.3.b8", "3.3.b19", "4.4.b18"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.22", "2.24", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.22", "2.24", "4.2"] }
bodies:
  - { body: "Chartered Institute for Archaeologists", citedIn: ["1.12", "1.13", "2.6", "2.7", "2.8", "2.27"] }
  - { body: "University Archaeology UK", citedIn: ["1.12", "1.13", "2.8", "2.27"] }
  - { body: "British Association for Biological Anthropology and Osteoarchaeology", citedIn: ["2.6"] }
  - { body: "Institute of Archaeologists of Ireland", citedIn: ["2.7", "2.27"] }
  - { body: "Institute for Historic Building Conservation", citedIn: ["2.7"] }
  - { body: "Institute for Conservation", citedIn: ["2.7"] }
  - { body: "Society for Museum Archaeology", citedIn: ["2.7"] }
  - { body: "European Association of Archaeologists", citedIn: ["2.7"] }
  - { body: "Historic England, Cadw, Historic Scotland, Department for Communities (Northern Ireland)", citedIn: ["2.27"] }
  - { body: "professional, statutory and regulatory bodies (unnamed)", citedIn: ["2.32", "3.8"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "the four honours classes, for performance above the threshold" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Education for Sustainable Development Guidance produced by Advance HE and QAA (March 2021)", citedIn: ["1.10"], role: "the learning outcomes the core skills align with" }
  - { document: "National Occupational Standards for Archaeological Practice (not yet ingested: Part E)", named: "National Occupational Standards for Archaeological Practice (NOS)", citedIn: ["1.12"], role: "the basis of the accreditation competency matrix" }
  - { document: "European Association of Archaeologists, Code of Practice and Principles of Conduct (not yet ingested)", named: "Code of Practice and Principles of Conduct", citedIn: ["2.7"], role: "a professional code" }
  - { document: "Valletta, Faro and World Heritage Conventions (international treaties)", named: "the Valletta and Faro Conventions, and the World Heritage Convention", citedIn: ["2.7"], role: "protection of the archaeological heritage" }
  - { document: "Profiling the Profession (labour market intelligence; external)", named: "Profiling the Profession", citedIn: ["2.8"], role: "evidence of employment growth" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code", citedIn: ["front matter"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "archaeological-science", definition: "using scientific methods on archaeological questions, with methods shared across many sciences (D1, 2.12)", beneficiaryDefinition: "applying science, such as chemistry, biology or physics, to questions about the past", scopeNote: "includes dating, materials, biomolecular and environmental work (2.13 to 2.15)", category: "unknown", practices: ["archaeology"] }
- { slug: "conservation-science", definition: "the science of what makes sites, monuments and artefacts decay and of how to restore and keep them (D1, 2.14)", beneficiaryDefinition: "finding out why remains decay and how to preserve them", scopeNote: "", category: "unknown", practices: ["archaeology"] }
- { slug: "experimental-archaeology", definition: "reproducing past actions and processes to see how the archaeological record forms (D1, 2.16)", beneficiaryDefinition: "recreating past activities to understand what they leave behind", scopeNote: "", category: "unknown", practices: ["archaeology"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "archaeological-science", form: "Archaeological science", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "conservation-science", form: "Conservation science", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "experimental-archaeology", form: "Experimental archaeology", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Archaeology"
  edition: "March 2022 (fourth edition)"
  year: 2022
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/archaeology-2022/archaeology-2022.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: c37a850bc9efdf101db0c38344fb46b3e70ccf63a72cd766af73b273b8d38c18
  heldFiles: ["wkspc2601-library/txt/qaa-2022-archaeology-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2022-archaeology-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2022-archaeology-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2022-archaeology-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0027", source: "CIfA and UAUK degree accreditation scheme and competency matrix", why: "the accreditation route named in 1.12, 1.13, 2.8 and 2.27 (SB5)", status: "wanted" }
- { w: "W-std-0028", source: "National Occupational Standards for Archaeological Practice", why: "the occupational standards the accreditation matrix aligns with (1.12)", status: "wanted" }
```

## Part E Gaps and questions
- Rungs: one only. Section 4 states the threshold (4.3, 18 subject items; 4.4, 20 generic items) and leaves higher performance to Annex D (4.2); no typical or excellent lists, so SB4 `outcomes` is empty and no gradeOf link is drawn. Differs from Psychology (three rungs).
- Lead-in wording: "On graduating with an honours degree in Archaeology, students should be able to" (4.3, 4.4) under the heading "Threshold level"; the modal is should, so force is recorded as should, statementType and rung threshold. 4.1 calls these the minimum threshold standards a student "will have demonstrated". P3 to confirm should against threshold as the force.
- Outcome lists in section 3 use "will be equipped to" (3.2) and "will be equipped with" (3.3), recorded as type outcome, rung none, force will; 3.2 is qualified "as appropriate to the breadth and depth of the course" and 3.1 says combined honours graduates normally have most of the skills. New lead-in wordings against Psychology.
- Skeleton corrections: 3.2.b5 and 3.2.b6 are one item split by a stray bullet ("material remains, / landscapes and environmental data"); recorded as 3.2.b5 with the merged text and 3.2.b6 dropped, so 3.2 has 16 items. 4.3.b16 ran across a page break and lost "and appreciate the need to engage ... equitable basis"; recut with `find`. 3.2.b17 and 4.3.b18 carried the next sub-heading; recut. Paragraph spans for 1.7, 1.9, 1.10, 2.19, 2.21 and 4.2 carried a following heading; recut to the paragraph text. 2.12 and 2.20 are recorded as their stems only; their list items (research themes; teaching methods) are S3 content, not statements.
- Duplicate in the issuer's text: 4.3.b10 ("recognise the range of archaeological data") repeats the start of 4.3.b7; both kept as issued. Also repeated: two identical tutorial bullets in 2.20 (b4, b11), and "assembling coherent research/project designs" in 3.3.b4 and 3.3.b15.
- Broken words in the held text (extraction spacing, such as "perf orm", "bri ng", "identi fy", "undert ake", "re flect", "colla borating", "appreciati ng") mean some verbs cannot be listed as they appear: 4.4.b2, b3, b4, b8, b9, b13 and 3.2.b8, b14, 3.3.b16, b17 list only the intact verbs or none.
- Not cut as statements, with reasons: 1.14 ("should not be seen exclusively as a vocational choice") is a view, not a standard; 2.5 and 2.29 to 2.31 use will to describe institutional practice; 2.22 uses "it is expected" and "would" (an obliging word outside the five, for Abbott); 2.26 ("there is a requirement" in most courses) describes practice; 4.1 frames the threshold and is the rung's introduction.
- Plain-present provider norms not cut (open point 5 of the benchmark template, for P3): 2.25 ("courses in all higher education providers include"), 3.5, 3.6 (providers "facilitate access"), 3.7 (students "are provided with full documentation"; documentation "will refer to" accreditation where appropriate), 3.8 ("participatory experience ... is therefore part of any course") and 3.10 ("aspires to include").
- 2.21 holds both must (no two-tier system; clear assessment criteria must be provided) and several shoulds; recorded at must, with the should parts paraphrased as should. 1.8 likewise holds must and should; recorded at must. 1.6 holds will and should; recorded at will.
- 1.12 reports a condition the professional body sets for accreditation (must demonstrate core NOS coverage); recorded as a requirement with addressee provider, but it is the accreditor's rule, not the issuer's. P3 to confirm it belongs in S4.
- 1.8, 1.9 and 1.10 address the discipline and its practitioners rather than the student; recorded with addressee provider and the student version not applicable.
- Integrated master's (MArc) at FHEQ 7 / FQHEIS 11 is described in 2.24 but no standards are given for it; levelsCovered holds fheq:6 and fqheis:10 only.
- Inferred: HECoS 100384 (archaeological sciences) from 2.12 to 2.17; the text names the subject area but no code. The crosswalk fheq:6 to spine:6 is read from std:ref:uk-framework R2.
- SB5: no body's requirements are ingested; CIfA and UAUK accreditation and the NOS are wanted (D3). The national heritage bodies (2.27) are partners, not regulators of courses; recorded for completeness.
- SB6: the front matter also names the Quality Assessment Framework for Wales, the Quality Enhancement Framework (Scotland) and the OfS regulatory framework for England; these are excluded matter and not quality-level frameworks, so they are not in SB6 frameworks.
- CQFW: not cited by the statement; not used.
- Section order and headings: section 2 is "Distinctive features" with four contexts and design sub-sections (Accessibility, Progression, Flexibility, Partnership, Monitoring and review) where Psychology has its own order; filled by function.
- Supersedes: the 2014 third edition is named only in the advisory group list (section 6); its date of withdrawal is not stated.
- Licence: QAA copyright notice only; re-use terms not stated in the text.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:14: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0085 (P1); built by tools/bm_build.py.
