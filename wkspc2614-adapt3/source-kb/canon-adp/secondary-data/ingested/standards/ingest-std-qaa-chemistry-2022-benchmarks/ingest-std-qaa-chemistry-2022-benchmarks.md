---
id: std:doc:qaa-chemistry-2022-benchmarks
title: "Subject Benchmark Statement Chemistry"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100417", label: "chemistry", basis: "stated" }
  - { scheme: "cah", code: "CAH07-02-01", label: "chemistry", basis: "stated" }
  - { scheme: "cah", code: "CAH07-02", label: "chemistry", basis: "stated" }
  - { scheme: "hecos", code: "101045", label: "environmental chemistry", basis: "inferred" }
  - { scheme: "hecos", code: "100420", label: "medicinal chemistry", basis: "inferred" }
edition: "March 2022 (fifth edition)"
published: 2022-03
status: current
supersedes: "the fourth edition (2019), named in the advisory group list (D1, section 6); this is the fifth edition (D1, back cover)"
heldText: { method: sha256-bytes, raw: 8719210f376e1569cb66c1c4fed4edcd96c6e9c403f62740bc017f9e94cfff23, normalised: 58f271dd83c5c393763b0bef097f4cd646ff5e995e329096093296aeb1f89855 }
heldTextStan: { method: sha256-stan, raw: 8719210f376e1569cb66c1c4fed4edcd96c6e9c403f62740bc017f9e94cfff23, normalised: 3082cffb8018905b3ef3c71fc49be5cb20a247311394fcf65e4b315ce3f5ecd5 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2022 revision with cross-cutting themes (Chemistry fifth edition, March 2022)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0092 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:36"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Chemistry (QAA, March 2022)

> Run 0092, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2022-chemistry-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
This document records what QAA's 2022 Chemistry statement expects of a graduate in chemistry and of the courses that lead there, for the bachelor's degree with honours and for master's degrees, integrated and standalone. Read S4 for the standards: two tables in section 4 grade each outcome at two rungs, threshold and excellent, and section 3 adds four outcome lists (core chemistry content, optional specialist content, enabling skills for honours and further skills for integrated master's). Every standard has a practitioner version, a student version and two instructions for AI agents that write about it or use it in conversation. Classes between the two rungs are left to Annex D of the 2024 Frameworks, which this document points to and never copies.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Chemistry, bachelor's degree with honours (FHEQ level 6; FQHEIS level 10) and master's degrees (FHEQ level 7; FQHEIS level 11), fifth edition, March 2022. Two rungs are stated, threshold and excellent, with no typical rung: Table 1 grades 14 honours outcomes at both rungs and Table 2 adds five master's outcomes, graded by support at threshold and independence at excellent. Section 3 holds four outcome lists: 14 core content outcomes for all undergraduates, three optional specialist outcomes, nine enabling skills for honours and six further skills for integrated master's. Some 30 obliging paragraphs set expectations on courses: breadth, laboratory competence, inclusion, accessibility, progression, placements, monitoring, the project and assessment. Themes: equality, diversity and inclusion; accessibility; education for sustainable development; employability, enterprise and entrepreneurship. Body: the Royal Society of Chemistry, which accredits courses towards Chartered Chemist. Shared documents: Annex D, the ESD guidance, the enterprise guidance and the apprenticeships characteristics statement.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Chemistry"
edition: "March 2022 (fifth edition)"
dates:
  published: 2022-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement; not a sector-recognised standard in England, a key reference point in Wales and Scotland and part of the quality requirements in Northern Ireland (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2022", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate in chemistry is expected to know, understand and be able to do at the end of a bachelor's degree with honours or a master's degree, at threshold and excellent rungs, with the context for course design, teaching and assessment"
appliesTo:
  awards: ["bachelor's with honours", "master's"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This document is a QAA Subject Benchmark Statement for Chemistry that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies.\" (D1, front matter)"
statedSubjects:
  - { name: "Chemistry", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100417", label: "chemistry" }, { scheme: "cah", code: "CAH07-02-01", label: "chemistry" }] }
  - { name: "integrated master's degrees with honours (MChem, MSci) and standalone master's (MSc, MRes)", locator: "(D1, 2.3; 4.7)", kind: "programme title", codes: [{ scheme: "hecos", code: "100417", label: "chemistry" }] }
  - { name: "applications such as biological, computational, environmental, materials or medicinal chemistry", locator: "(D1, 2.1)", kind: "specialism", codes: [{ scheme: "hecos", code: "101045", label: "environmental chemistry" }, { scheme: "hecos", code: "100420", label: "medicinal chemistry" }] }
  - { name: "sub-branches such as green and sustainable chemistry, cheminformatics or chemistry education", locator: "(D1, 3.4)", kind: "specialism", codes: [{ scheme: "hecos", code: "100417", label: "chemistry" }] }
  - { name: "interdisciplinary single honours, joint and combined honours courses with chemistry", locator: "(D1, 1.7; 1.14)", kind: "programme title", codes: [{ scheme: "hecos", code: "100417", label: "chemistry" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "chemistry as the central science; its part in global challenges" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Purposes of a Chemistry degree", gloss: "the aims read within an inclusive, representative curriculum" }
  - { number: "1.3", order: 5, componentType: stem, parent: "section 1", heading: "Purposes of a Chemistry degree", gloss: "general aims of chemistry courses" }
  - { number: "1.4", order: 6, componentType: stem, parent: "section 1", heading: "Purposes of a Chemistry degree", gloss: "aims of honours courses" }
  - { number: "1.5", order: 7, componentType: stem, parent: "section 1", heading: "Purposes of a Chemistry degree", gloss: "aims of master's courses" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Chemistry degree", gloss: "each provider sets its own content and organisation" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Chemistry degree", gloss: "a broad discipline; specialist, joint and combined routes" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Chemistry degree", gloss: "practical work as essential; a spiral towards independent lab work" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Chemistry degree", gloss: "theory underpinned by enabling skills" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI built in; a shared duty to promote equality" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "an inclusive view of the history and uses of chemistry" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainable development as part of studying chemistry; the SDGs" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship", gloss: "employability: subject and wider attributes" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship", gloss: "enterprise and entrepreneurship defined" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship", gloss: "topics in enterprise education; the QAA guidance" }
  - { number: "2.1", order: 19, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "many course designs; theory and application combined" }
  - { number: "2.2", order: 20, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "routes in, foundation years and prior qualifications" }
  - { number: "2.3", order: 21, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "honours and integrated master's degrees and their levels; standalone master's" }
  - { number: "2.4", order: 22, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "placements and study abroad; integrating credit-bearing placements" }
  - { number: "2.5", order: 23, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "a common core with later options" }
  - { number: "2.6", order: 24, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "degree apprenticeships follow this statement" }
  - { number: "2.7", order: 25, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "accessible learning and assessment by inclusive design and adjustment" }
  - { number: "2.8", order: 26, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "fully accessible curricula, pedagogy, assessment and practicals" }
  - { number: "2.9", order: 27, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression from defined to open-ended problems" }
  - { number: "2.10", order: 28, componentType: stem, parent: "section 2", heading: "Progression", gloss: "methods that build independence; strategies that support progression" }
  - { number: "2.11", order: 29, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression rules and the threshold for each level" }
  - { number: "2.12", order: 30, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "resits and exit awards; Scottish four-year honours" }
  - { number: "2.13", order: 31, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes of delivery, credit transfer and flexibility to change" }
  - { number: "2.14", order: 32, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnerships with colleges, overseas providers and industry" }
  - { number: "2.15", order: 33, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review against external reference points" }
  - { number: "2.16", order: 34, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.17", order: 35, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "2.18", order: 36, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "several external examiners for the breadth of the subject" }
  - { number: "2.19", order: 37, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "continuous evaluation with students, graduates and employers" }
  - { number: "2.20", order: 38, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation by the Royal Society of Chemistry towards CChem" }
  - { number: "3.1", order: 40, componentType: paragraph, parent: "section 3", heading: "Content, structure and delivery", gloss: "each provider defines its own content" }
  - { number: "3.2", order: 41, componentType: paragraph, parent: "section 3", heading: "Content, structure and delivery", gloss: "the content as a foundation, developed later" }
  - { number: "3.3", order: 42, componentType: area, parent: "section 3", heading: "Subject knowledge and understanding", gloss: "core chemistry content and what it lets graduates do" }
  - { number: "3.4", order: 43, componentType: area, parent: "section 3", heading: "Subject knowledge and understanding", gloss: "optional specialist and supplementary content" }
  - { number: "3.5", order: 44, componentType: paragraph, parent: "section 3", heading: "Underpinning and enabling knowledge and skills", gloss: "the wider characteristics of chemistry graduates" }
  - { number: "3.6", order: 45, componentType: paragraph, parent: "section 3", heading: "Underpinning and enabling knowledge and skills", gloss: "making development opportunities explicit; support into work or study" }
  - { number: "3.7", order: 46, componentType: paragraph, parent: "section 3", heading: "Underpinning and enabling knowledge and skills", gloss: "skills embedded in content; resilience through practical work" }
  - { number: "3.8", order: 47, componentType: stem, parent: "section 3", heading: "Underpinning and enabling knowledge and skills", gloss: "enabling content for honours graduates" }
  - { number: "3.9", order: 48, componentType: stem, parent: "section 3", heading: "Underpinning and enabling knowledge and skills", gloss: "further skills for integrated master's graduates" }
  - { number: "3.10", order: 49, componentType: practice, parent: "section 3", heading: "Project and dissertation", gloss: "the independent investigative project; originality at master's" }
  - { number: "3.11", order: 50, componentType: paragraph, parent: "section 3", heading: "Project and dissertation", gloss: "supervision and greater ownership at master's" }
  - { number: "3.12", order: 51, componentType: paragraph, parent: "section 3", heading: "Project and dissertation", gloss: "industry and team projects; individual master's projects" }
  - { number: "3.13", order: 52, componentType: area, parent: "section 3", heading: "Project and dissertation", gloss: "training that underpins the project" }
  - { number: "3.14", order: 53, componentType: stem, parent: "section 3", heading: "Project and dissertation", gloss: "typical share of credit for the project" }
  - { number: "3.15", order: 54, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching methods left open but explicit, inclusive and reviewed" }
  - { number: "3.16", order: 55, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "student-centred, visual and practical teaching in many formats" }
  - { number: "3.17", order: 56, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "synchronous learning activities" }
  - { number: "3.18", order: 57, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "asynchronous materials and activities" }
  - { number: "3.19", order: 58, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "blended and multimodal activities" }
  - { number: "3.20", order: 59, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "responsive strategies; development for all teaching staff" }
  - { number: "3.21", order: 60, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment aligned with outcomes and varied" }
  - { number: "3.22", order: 61, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "digital literacy, coding and varied assessment formats" }
  - { number: "3.23", order: 62, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "the kinds of evidence assessed" }
  - { number: "3.24", order: 63, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment for subject and employability skills; the skills map" }
  - { number: "3.25", order: 64, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "master's assessment: unfamiliar problems and research skills" }
  - { number: "4.1", order: 66, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the standards as what an honours graduate has shown" }
  - { number: "4.2", order: 67, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed threshold; Annex D for the classes" }
  - { number: "4.3", order: 68, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "the two rungs defined: threshold and excellent" }
  - { number: "4.4", order: 69, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the tables cover the main content; no checklist or weighting" }
  - { number: "4.5", order: 70, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "achievement across outcomes; compensation by algorithm" }
  - { number: "4.6", order: 71, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "reading the tables with sections 1 and 3; Table 1 for honours" }
  - { number: "4.7", order: 72, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "master's build on Table 1; Table 2" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Chemistry degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Chemistry degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional reference points", kind: "other: front matter, read for S1 and S2" }
  - { number: "section headings 1 to 4", heading: "the four section heading lines", kind: "other: heading lines" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for S7 and SB6" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for Chemistry", kind: "other: back matter, read for S8 (editions)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 103 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/chemistry-2022/1.2
  locator: { number: "1.2", headingPath: ["Context and purposes of a Chemistry degree", "Purposes of a Chemistry degree"] }
  span: { start: 8887, end: 9185 }
  source: "1.2 The points below should be seen within the context of providing relevant and representative material for all students undertaking Chemistry degrees, and creating an inclusive environment where all feel welcome, valued and provided with the opportunity to develop an enthusiasm for the subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "chemistry courses"
  addressee: provider
  verbs: ["providing", "creating"]
  about: "representative material and an inclusive setting"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The aims that follow should be read as part of giving every chemistry student relevant, representative material and a welcoming, inclusive setting where all feel valued and can come to enjoy the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/1.7
  locator: { number: "1.7", headingPath: ["Context and purposes of a Chemistry degree", "Characteristics of a Chemistry degree"] }
  span: { start: 12182, end: 12820 }
  source: "1.7 Chemistry is a very broad discipline and Chemistry courses should reflect this, both through the material covered and the learning, teaching and assessment methods used. Some Chemistry courses will provide students with a wide-ranging coverage of the full breadth of the discipline; others may allow students to specialise in a particular aspect of the subject that is reflected in the title of their award. Institutions may also offer courses that allow students to combine their study of chemistry with that in other disciplines through either interdisciplinary single honours courses, or through joint or combined honours courses.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "chemistry courses"
  addressee: provider
  verbs: ["reflect"]
  about: "breadth in content and methods"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Because chemistry is very broad, courses should show that breadth in what they cover and in how they teach, learn and assess; some courses cover the whole field, others let students specialise or combine chemistry with other subjects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/1.8
  locator: { number: "1.8", headingPath: ["Context and purposes of a Chemistry degree", "Characteristics of a Chemistry degree"] }
  span: { start: 12820, end: 13929 }
  source: "1.8 Hands-on practical work forms an essential part of all Chemistry courses. It allows students to develop the necessary practical skills for a career in science. Indeed, there is an expectation that all Chemistry graduates will be competent and capable of safe and accurate working in a laboratory environment. Experimentation enables students to develop the tacit knowledge and transferable skills that are required for careers in all sectors. The abilities of Chemistry students are often developed most effectively through creative problem-solving in relation to experiments that have not generated the expected results. Consequently, a spiral approach to developing experimental capabilities, and independence in practical work is common in Chemistry courses. Practical sessions at the start of a course typically include detailed instructions, and experiments that generate results reliably over a wide range of conditions, allowing for mistakes to be made and learnt from. In contrast, final-year students are expected to work with precision under minimal supervision, solving problems as they arise.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "chemistry graduates; final-year students"
  addressee: learner
  verbs: ["work", "solving"]
  about: "safe, accurate laboratory work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Practical work is essential to every chemistry course: all graduates will be competent and able to work safely and accurately in a laboratory, and by the final year students work precisely with little supervision, sorting out problems as they come; courses build this in a spiral, from detailed instructions to independence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/1.11
  locator: { number: "1.11", headingPath: ["Context and purposes of a Chemistry degree", "Equality, diversity and inclusion"] }
  span: { start: 15053, end: 15897 }
  source: "1.11 Chemistry, as a subject whose underpinnings rely upon objective observation, should be culturally and ethically neutral. However, its historical identity and application in wider society must be viewed and taught in an inclusive manner. Curricula should recognise the discoveries and contributions of chemical scientists with diverse backgrounds and identities, and acknowledge that different cultural backgrounds may provide different insights and lead to new discoveries. Furthermore, learners should have the opportunity to explore chemistry-related topics that inspire them and that allow them to situate their knowledge in the light of their aspirations, lived experiences or cultural backgrounds. They should also be encouraged to evaluate both the positive and negative impacts of the potential applications of chemical discoveries."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "chemistry curricula and teaching"
  addressee: provider
  verbs: ["viewed", "taught", "recognise", "acknowledge", "evaluate"]
  about: "an inclusive account of chemistry and its uses"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Though chemistry rests on objective observation, its history and its uses in society must be presented and taught inclusively; curricula should credit chemists of diverse backgrounds, accept that other cultures bring other insights, let learners explore topics that matter to them and encourage them to weigh both the good and harm that chemical discoveries can do."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of a Chemistry degree", "Education for sustainable development"] }
  span: { start: 15936, end: 16725 }
  source: "1.12 Chemistry is central to developing solutions to problems, and courses in Chemistry should inspire chemists to engage with the ongoing process of addressing personal, human and global challenges to create a better future. Chemistry courses may include topics drawn from the UN Sustainable Development Goals , particularly those associated with health, energy, clean water and the environment. Education for sustainable development is thus an integral part of the study of chemistry, ensuring that graduates are equipped with the knowledge, skills and competencies that can enable them to generate innovative solutions to complex challenges. More information on education for sustainable development can be found in the QAA and Advance HE guidance Education for Sustainable Development."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "chemistry courses"
  addressee: provider
  verbs: ["inspire", "engage"]
  about: "sustainable development in chemistry courses"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Chemistry is central to solving problems, so courses should inspire chemists to take part in tackling personal, human and global challenges; topics may come from the UN Sustainable Development Goals, and ESD is part of studying chemistry, equipping graduates to devise new answers to complex challenges."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of a Chemistry degree", "Employability, enterprise and entrepreneurship"] }
  span: { start: 16773, end: 17447 }
  source: "1.13 All Chemistry degree courses should equip students with the knowledge, skills, behaviours, characteristics and attributes that prepare them for life after graduation in an increasingly complex and ever-changing social, cultural and economic environment and enable them to make a meaningful and effective contribution to society. Chemistry graduates should be equipped not only with the discipline-specific knowledge and professional skills necessary for careers in the chemical sciences, but also the wider attributes to prepare them for careers in other sectors. Paragraph 3.8 provides details of the range of wider skills that may be expected in Chemistry graduates.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "chemistry courses and their graduates"
  addressee: both
  verbs: ["equip", "prepare", "enable"]
  about: "employability: subject skills and wider attributes"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "All chemistry courses should prepare students for life after graduation in a complex, changing world and for a useful contribution to society; graduates should have both the subject knowledge and professional skills for chemical careers and the wider attributes for careers elsewhere."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of a Chemistry degree", "Design"] }
  span: { start: 18882, end: 19578 }
  source: "2.1 There are a variety of types of Chemistry courses across the UK. That diversity is a strength, in that it allows students to choose a course that aligns with their interests and is suited to their individual needs and aspirations. Some courses follow the traditional sub- divisions of inorganic, organic and physical and analytical chemistry. Others are arranged as synthesis, measurement and application. Alternatively, material may be organised around applications, such as biological, computational, environmental, materials or medicinal chemistry. Some may lead with fundamental theory, and others with application, although all courses should include an appropriate combination of both.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "chemistry courses"
  addressee: provider
  verbs: ["include"]
  about: "theory and application combined"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Chemistry courses across the UK are designed in many ways, by traditional branches, by synthesis, measurement and application, or around applied fields; whichever lead they take, all courses should include a suitable mix of fundamental theory and application."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of a Chemistry degree", "Design"] }
  span: { start: 20447, end: 21773 }
  source: "2.3 Undergraduates in Chemistry may choose to study a standard bachelor's degree with honours (FHEQ Level 6; FQHEIS Level 10) or an integrated master's degree with honours (FHEQ Level 7; FQHEIS Level 11). These each have distinct learning outcomes to reflect the level of the award. Bachelor's degrees should provide students with the subject- specific knowledge, understanding and skills, as well as the wider transferable skills and attributes that prepare graduates for a wide range of careers in many sectors. Integrated master's degree with honours courses (such as MChem, MSci) encompass both bachelor's degrees with honours and master's degree outcomes. An integrated master's degree is awarded after an extended course of study which allows students to study chemistry to a greater depth than is possible on a bachelor's course and to extend the opportunities to develop specialist knowledge, advanced skills and undertake project work. These master's degrees thus provide a coherent, integrated opportunity to develop a deeper level of understanding and experience, sufficient to prepare them for a professional career in the chemical sciences. Standalone master's (MSc and MRes) degree courses in Chemistry, are self-contained courses, normally involving one or two years of postgraduate study in a specialist area.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "bachelor's degrees with honours in chemistry"
  addressee: provider
  verbs: ["provide", "prepare"]
  about: "what honours degrees provide; the integrated master's"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduates may take a bachelor's degree with honours (FHEQ 6; FQHEIS 10) or an integrated master's with honours (FHEQ 7; FQHEIS 11), each with its own outcomes; bachelor's degrees should give subject knowledge, understanding and skills plus wider transferable skills for many careers, while integrated master's degrees cover both sets of outcomes and go deeper."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of a Chemistry degree", "Design"] }
  span: { start: 21773, end: 22847 }
  source: "2.4 Some Chemistry courses will enable students to learn outside the formal academic environment through placement at an organisation in the chemical science sector, or to study at an international university. Such placements may last for a term, semester or an entire year. They typically take place in either the third or fourth year of a student's undergraduate programme. Both bachelor's and integrated master's degrees may include such periods of study, and this may or may not extend the period of the degree, depending on the expected learning undertaken during the year. Credit awarded during such study also varies according to the learning and assessment workload during the experience. Credit- bearing placements should, however, be integrated within the course of study, so that students can relate their experience to, and use the skills that they have developed in, their academic study. Many providers also offer or facilitate non-credit bearing industrial and research placement experiences during vacations to enhance student experience and development.\n\n7\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "credit-bearing placements"
  addressee: provider
  verbs: ["integrated", "relate", "use"]
  about: "integrating placements into the course"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses may include placements or study abroad, often in the third or fourth year and of varied length and credit; credit-bearing placements should be built into the course so students can link their experience and skills to their academic study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of a Chemistry degree", "Design"] }
  span: { start: 23290, end: 23659 }
  source: "2.6 The academic component of degree apprenticeships in Chemistry should follow the guidelines in this Subject Benchmark Statement. Degree apprenticeships in higher education are covered explicitly in the Characteristics Statement for Higher Education in Apprenticeships which describes the general characteristics and distinctive features of apprenticeships in the UK."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "degree apprenticeships in chemistry"
  addressee: provider
  verbs: ["follow"]
  about: "degree apprenticeships follow this statement"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The academic part of chemistry degree apprenticeships should follow this statement; apprenticeships in general are described in QAA's characteristics statement on higher education in apprenticeships."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of a Chemistry degree", "Accessibility"] }
  span: { start: 23674, end: 24533 }
  source: "2.7 Equality of opportunity involves enabling access for people who have differing individual requirements as well as eliminating arbitrary and unnecessary barriers to successful learning. In accordance with this, Chemistry courses must ensure that all students are offered learning and assessment opportunities that are equally accessible to them, by means of inclusive design wherever possible and by means of reasonable individual adjustments where necessary. Learning and assessment experiences should be diverse to both reflect the variety of the subject and to increase accessibility for all. Indeed, to face the challenges of the twenty-f irst century, the subject needs as diverse a body as possible to contribute new ideas and innovations, drawn from the different insights and perspectives from all learners, regardless of disability or background.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "chemistry courses"
  addressee: provider
  verbs: ["ensure", "offered"]
  about: "equally accessible learning and assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Equal opportunity means access for people with differing needs and removing needless barriers; chemistry courses must make learning and assessment equally accessible to all, by inclusive design where possible and reasonable adjustment where needed, and learning and assessment should be varied to reflect the subject and widen access."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of a Chemistry degree", "Accessibility"] }
  span: { start: 24533, end: 24870 }
  source: "2.8 Chemistry course teams must pay attention to ensuring that curricula, pedagogy, assessments and practical elements of courses are designed to be fully accessible, and that all learners are supported in the development of skills in the full range of verbal, spatial, numerical and other approaches required to solve chemical problems."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "chemistry course teams"
  addressee: provider
  verbs: ["pay", "ensuring", "designed", "supported"]
  about: "fully accessible curricula and practicals"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Course teams must take care that curricula, teaching, assessments and practical work are built for full accessibility, and that every learner gets support to develop the verbal, spatial, numerical and other skills chemical problems call for."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of a Chemistry degree", "Progression"] }
  span: { start: 24883, end: 25515 }
  source: "2.9 Chemistry degree courses should be designed to promote academic and personal development. Initially, students will be expected to use their knowledge and understanding of simple concepts to solve well-defined problems. As the course advances, they will become confident in applying their knowledge and understanding, making connections between more challenging and complex concepts to enable them to solve ill-defined and open-ended problems. On graduation, students will be competent in a range of knowledge, understanding, experience and skills to equip them for a career in the chemical sciences, or indeed in other sectors.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "chemistry courses and their students"
  addressee: both
  verbs: ["designed", "promote", "solve", "applying"]
  about: "progression from defined to open problems"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses should be designed to foster academic and personal growth: students first use simple concepts on well-defined problems, then link harder concepts to tackle ill-defined, open problems, and on graduating will have the range of knowledge, experience and skills for a career in chemistry or elsewhere."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/2.10.b1
  locator: { number: "2.10.b1", headingPath: ["Distinctive features of a Chemistry degree", "Progression"] }
  span: { start: 25847, end: 25923 }
  source: "recognise the diversity of prior experience and the challenges of transition"
  stem: "2.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "progression strategies"
  addressee: provider
  verbs: ["recognise"]
  about: "diverse prior experience and transition"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Strategies for progression should take account of how varied students' prior experience is and how hard transition can be."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/2.10.b2
  locator: { number: "2.10.b2", headingPath: ["Distinctive features of a Chemistry degree", "Progression"] }
  span: { start: 25926, end: 26071 }
  source: "allow all students to achieve their potential and realise their ambitions, irrespective of their background or motivations for studying chemistry"
  stem: "2.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "progression strategies"
  addressee: provider
  verbs: ["allow", "achieve", "realise"]
  about: "every student reaching their potential"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Strategies for progression should let every student reach their potential and ambitions, whatever their background or reasons for studying chemistry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/2.10.b3
  locator: { number: "2.10.b3", headingPath: ["Distinctive features of a Chemistry degree", "Progression"] }
  span: { start: 26074, end: 26135 }
  source: "support academic and personal development as well as learning"
  stem: "2.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "progression strategies"
  addressee: provider
  verbs: ["support"]
  about: "academic and personal development"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Strategies for progression should support personal and academic growth as well as learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/2.10.b4
  locator: { number: "2.10.b4", headingPath: ["Distinctive features of a Chemistry degree", "Progression"] }
  span: { start: 26138, end: 26217 }
  source: "are matched to the documented learning outcomes or competencies for each level."
  stem: "2.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "progression strategies"
  addressee: provider
  verbs: ["matched"]
  about: "strategies tied to each level's outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Strategies for progression should fit the stated learning outcomes or competencies for each level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of a Chemistry degree", "Progression"] }
  span: { start: 26218, end: 26978 }
  source: "2.11 Students on a Chemistry degree course progress from one year or academic stage to the next by satisfying the regulations and processes for each institution. These must require the students to demonstrate that they have met the overall threshold standard for the\n\n8\nlevel of study. This will usually include successful completion and the award of credit for the full range of learning and assessment, including practical courses. Students may also be required to meet additional criteria, such as where the title of the programme and ultimate award refers to a particular specialism, or to be eligible to undertake a placement. The standard required to progress on an integrated master's degree course may also be higher than that for a bachelor's course.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "institutions' progression regulations"
  addressee: provider
  verbs: ["require", "demonstrate"]
  about: "the threshold for each level as the condition of progression"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students progress between years by meeting their institution's rules, which must require them to show they have met the overall threshold for the level; this will usually mean completing and gaining credit for all learning and assessment, practicals included, and more may be asked for specialist titles, placements or an integrated master's."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/2.13
  locator: { number: "2.13", headingPath: ["Distinctive features of a Chemistry degree", "Flexibility"] }
  span: { start: 27847, end: 28893 }
  source: "2.13 The diversity in the type of courses offered in chemistry is also reflected in a diversity of mode of delivery. While the majority are delivered full-time, some courses offer part-time and/or distance learning study. Courses may also offer students the opportunity to study abroad or industrial placements. The range of delivery methods (both face-to-face and digital) utilised are similarly diverse and appropriate for the needs of the learner, the material and their assessment. The progressive acquisition of knowledge and skills within the subject area also enables flexibility between courses, both within and between institutions, with mechanisms available for the transfer of credit between institutions. Courses also need to be sufficiently flexible to be able to respond to and anticipate change, both in the advancement of the subject and its interface with other disciplines and in the needs of its graduates and their employers, and should take account of learners' needs and make appropriate reasonable adjustments, as required."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "chemistry courses"
  addressee: provider
  verbs: ["respond", "anticipate", "take", "make"]
  about: "flexibility to change and reasonable adjustments"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses differ in mode, from full-time to part-time and distance study, abroad and in industry; they need to be flexible enough to meet and foresee changes in the subject and in graduates' and employers' needs, and should take account of learners' needs, making reasonable adjustments as required."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/2.16
  locator: { number: "2.16", headingPath: ["Distinctive features of a Chemistry degree", "Monitoring and review"] }
  span: { start: 30362, end: 30674 }
  source: "2.16 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "higher education providers in periodic review"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Externality is essential to UK quality assurance; providers will use external reviewers in periodic review to get an outside view of planned changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of a Chemistry degree", "Monitoring and review"] }
  span: { start: 31597, end: 32338 }
  source: "2.19 Programme and course teams should also conduct regular monitoring and evaluation, with the support of independent evaluators, to ensure continuous quality enhancement. Evaluation of student performance data as well as student feedback and student voice alongside other measures of the student experience should be integrated with expert review (including that provided by external examiners) to ensure the curricula remain current, engaging and accessible. Historic data may also enable trend analysis to measure progress and identify emerging issues. Students and graduates, as well as employers and relevant professional bodies, should be actively involved in designing and delivering actions to develop and enhance courses of study.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "programme and course teams"
  addressee: provider
  verbs: ["conduct", "integrated", "involved"]
  about: "continuous evaluation with stakeholders"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Programme and course teams should evaluate regularly with independent evaluators; student data, feedback and voice should be combined with expert review, external examiners' included, to keep curricula current, engaging and accessible, and students, graduates, employers and professional bodies should help design and deliver improvements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/3.2
  locator: { number: "3.2", headingPath: ["Content, structure and delivery", "Content, structure and delivery"] }
  span: { start: 33291, end: 33658 }
  source: "3.2 Chemistry is a diverse subject, and in an undergraduate curriculum it is impossible to cover all aspects in equal breadth and depth. The content indicated below should be regarded as foundational to a quality chemistry curriculum and elements should be further developed in later parts of the course, reflecting the research and teaching specialisms of the staff."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "undergraduate chemistry curricula"
  addressee: provider
  verbs: ["regarded", "developed"]
  about: "the content as a foundation to build on"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "No undergraduate course can cover every part of chemistry equally; the content that follows should be treated as the foundation of a good curriculum, with parts developed further later on in line with staff research and teaching interests."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b1
  locator: { number: "3.3.b1", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 33810, end: 33941 }
  source: "describe and discuss the full breadth of key chemical concepts confidently, accurately and in detail, using appropriate terminology"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["describe", "discuss"]
  about: "key chemical concepts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates describe and discuss the key concepts across the whole of chemistry with confidence, accuracy and detail, in the right terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b2
  locator: { number: "3.3.b2", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 33944, end: 34147 }
  source: "describe, document and enact safe working practices, in terms of managing chemical toxicity, chemical stability and chemical reactivity, through knowledge- based risk assessments and practical activities"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["describe", "document", "enact"]
  about: "safe working practices"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates describe, record and follow safe practice, managing toxicity, stability and reactivity through knowledge-led risk assessment and practical work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b3
  locator: { number: "3.3.b3", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 34150, end: 34304 }
  source: "consider and apply methods for waste reduction in practical activities, and deploy disposal techniques that protect laboratory workers and the environment"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["consider", "apply", "deploy"]
  about: "waste reduction and safe disposal"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates cut waste in practical work and use disposal methods that protect people in the laboratory and the environment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b4
  locator: { number: "3.3.b4", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 34307, end: 34538 }
  source: "explain and rationalise their understanding of classical and statistical thermodynamics, kinetics, quantum mechanics and spectroscopy and apply this to the solution of theoretical and practical problems to wider topics in chemistry"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["explain", "rationalise", "apply"]
  about: "thermodynamics, kinetics, quantum mechanics and spectroscopy"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates explain and justify how thermodynamics (classical and statistical), kinetics, quantum mechanics and spectroscopy work, and use them on problems in theory and in the laboratory."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b5
  locator: { number: "3.3.b5", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 34541, end: 34803 }
  source: "predict likely and potential synthetic products, bond-forming reactions, mechanistic pathways, stereochemistry and reactivity, and use this knowledge to suggest synthetic pathways to target compounds and design experimental activities that test their predictions"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["predict", "use", "suggest", "design"]
  about: "predicting reactions and planning synthesis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates predict likely products, bond-forming reactions, mechanisms, stereochemistry and reactivity, and use those predictions to propose routes to target compounds and to design experiments that test them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b6
  locator: { number: "3.3.b6", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 34806, end: 34969 }
  source: "explain, design and deploy purification, isolation and characterisation strategies, in the light of physicochemical properties and trends of elements and compounds"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["explain", "design", "deploy"]
  about: "purification, isolation and characterisation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates explain, plan and use ways to purify, isolate and characterise substances, guided by the physical and chemical properties and periodic trends of the elements and their compounds."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b7
  locator: { number: "3.3.b7", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 34972, end: 35178 }
  source: "discuss periodic trends in chemistry, explain the consequences of these trends on reactivity, behaviour and physical properties and apply this knowledge to the solution of theoretical and practical problems"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["discuss", "explain", "apply"]
  about: "periodic trends"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates discuss trends across the periodic table, explain what they mean for how elements react and behave and for their physical properties, and use this on problems in theory and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b8
  locator: { number: "3.3.b8", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 35181, end: 35297 }
  source: "describe atomic and molecular orbitals and their conceptual applications to structure, bonding and reaction pathways"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["describe"]
  about: "atomic and molecular orbitals"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates describe atomic and molecular orbitals and how they help explain structure, bonding and the paths reactions take."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b9
  locator: { number: "3.3.b9", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 35300, end: 35546 }
  source: "design, develop and carry out qualitative and quantitative sample preparation and purification, chemical measurement, metrology and analysis, with due regard to accuracy, precision, traceability and the effects of complex matrices and sample size"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["design", "develop", "carry"]
  about: "sample preparation, measurement and analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates plan, develop and carry out qualitative and quantitative preparation and purification of samples, measurement, metrology and analysis, attending to accuracy, precision, traceability, complex matrices and sample size."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b10
  locator: { number: "3.3.b10", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 35549, end: 35801 }
  source: "explain the theoretical basis and limitations of a range of classical and instrumental analytical techniques, undertake practical analyses and measurement and communicate the outcomes using appropriate terminology and mathematical or graphical notation"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["explain", "undertake", "communicate"]
  about: "analytical techniques and their limits"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates explain the theory behind classical and instrumental analytical techniques and their limits, carry out analyses and measurements and report them in the right terms and notation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b11
  locator: { number: "3.3.b11", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 35804, end: 35930 }
  source: "use computational techniques and tools, to aid further understanding and insight of chemical structure, bonding and reactivity"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["use"]
  about: "computational methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates use computational methods and software to understand chemical structure, bonding and reactivity better."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b12
  locator: { number: "3.3.b12", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 35937, end: 36038 }
  source: "gain knowledge of a range of inorganic and organic substances, compounds and materials and their uses"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["gain"]
  about: "inorganic and organic substances and their uses"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates know many organic and inorganic compounds, substances and materials and what each is for."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b13
  locator: { number: "3.3.b13", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 36041, end: 36220 }
  source: "appreciate the contribution of chemistry to the innovations that characterise the modern world, and the potential of chemists to develop solutions to current and future challenges"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["appreciate"]
  about: "chemistry's part in innovation and future challenges"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates recognise how chemistry has fed the innovations of the modern world and how chemists can help meet present and future challenges."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.3.b14
  locator: { number: "3.3.b14", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 36223, end: 36386 }
  source: "recognise the relationships and interfaces between chemistry and other subjects, such that they are able to operate effectively in a multidisciplinary environment."
  stem: "3.3"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "undergraduates in chemistry (honours and integrated master's)"
  addressee: learner
  verbs: ["recognise", "operate"]
  about: "chemistry and other subjects"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses should include chemistry content that lets graduates see how chemistry relates to and meets other subjects, so as to work well in multidisciplinary settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.4.b1
  locator: { number: "3.4.b1", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 36495, end: 36594 }
  source: "consider and discuss the geographical and historical culture of chemistry and its impact on society"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "undergraduates on courses with specialist or supplementary content"
  addressee: learner
  verbs: ["consider", "discuss"]
  about: "the culture and history of chemistry and its social impact"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses may add specialist or supplementary content that lets graduates think about and discuss where and how chemistry grew as a culture and what it has done to society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.4.b2
  locator: { number: "3.4.b2", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 36597, end: 36729 }
  source: "specialise in one or more sub-branches of chemistry, such as green and sustainable chemistry, cheminformatics or chemistry education"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "undergraduates on courses with specialist or supplementary content"
  addressee: learner
  verbs: ["specialise"]
  about: "specialising in a branch of chemistry"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses may add specialist or supplementary content that lets graduates focus on one or more specialist branches, for example sustainable (green) chemistry, cheminformatics or the teaching of chemistry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.4.b3
  locator: { number: "3.4.b3", headingPath: ["Content, structure and delivery", "Subject knowledge and understanding"] }
  span: { start: 36732, end: 37002 }
  source: "integrate and situate their understanding of chemistry within the context of other honour's subjects, such as biology, physics, geology, biomedical, environmental or pharmaceutical sciences or relate their knowledge to chemistry using vocations such as business and law."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "undergraduates on courses with specialist or supplementary content"
  addressee: learner
  verbs: ["integrate", "situate", "relate"]
  about: "chemistry within other subjects and vocations"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses may add specialist or supplementary content that lets graduates place their chemistry within another honours subject, such as biology, physics or the environmental and pharmaceutical sciences, or link it to vocational fields such as business and law."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.5
  locator: { number: "3.5", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 37050, end: 38255 }
  source: "3.5 Chemistry is an inherently creative discipline. Chemistry graduates are therefore innovative and enterprising in their outlook and excited by the challenge of finding solutions to problems. They are confident and resilient, and are capable of adapting to uncertainty, assessing risk and actively embracing change. They are self-motivated and independent, but also able to work effectively as part of a team. Chemistry graduates should be logical and analytical and be confident in the use of evidence to develop, support or refute arguments. They are constructive and objective in challenging the ideas of others and resilient and reflective when their own ideas are challenged. They are responsible and act with integrity, considering the impacts of their actions and decisions on both individuals and wider society. They value diversity in all of its forms, and respect and recognise the contributions of others. Chemistry degree courses, both through the nature of the discipline and the way that it is taught and assessed, allow students to develop these wider characteristics. Chemistry graduates are therefore highly sought after by employers in both the scientific and non- scientific sectors.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "chemistry graduates"
  addressee: learner
  verbs: ["develop", "support", "refute"]
  about: "logical, analytical use of evidence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Chemistry is a creative discipline and its graduates tend to be innovative, resilient, self-motivated team players; they should be logical and analytical and confident in using evidence to build, back or rebut arguments, and courses let them develop these wider traits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.6
  locator: { number: "3.6", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 38255, end: 38774 }
  source: "3.6 Students should be made explicitly aware of the opportunities for academic and personal development that the course provides, allowing them to reflect on their strengths and the opportunities for further development, and so enhance their employability. Students should also be given support, whether through the formal curriculum or through extracurricular activities, in applying for and making the transition to further study or employment through, for example, advice on applications and practice in interviews.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "chemistry courses"
  addressee: provider
  verbs: ["made", "reflect", "given"]
  about: "making development explicit; support into work or study"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should be shown clearly the chances for academic and personal growth the course offers, so they can reflect on strengths and next steps and improve their employability, and should get support, in or beyond the curriculum, in applying for and moving on to further study or work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/3.8.b1
  locator: { number: "3.8.b1", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 39477, end: 39563 }
  source: "navigate, utilise and collate digital information tools to source information and data"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["navigate", "utilise", "collate"]
  about: "digital information tools"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours courses should include enabling content so graduates can use digital tools to find, gather and organise information and data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.8.b2
  locator: { number: "3.8.b2", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 39566, end: 39765 }
  source: "select, examine and critique the research literature and other sources of information to maintain currency of knowledge, extend learning and support the development of solutions to specified problems"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["select", "examine", "critique"]
  about: "critical use of the literature"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours courses should include enabling content so graduates can choose, examine and criticise research papers and other sources so as to keep their knowledge current, learn further and help solve set problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.8.b3
  locator: { number: "3.8.b3", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 39768, end: 39961 }
  source: "deploy mathematical concepts, processes and tools, such as the manipulation of equations, calculus, and graphical and statistical analysis, to solve chemical problems and evaluate chemical data"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["deploy", "solve", "evaluate"]
  about: "mathematics for chemistry"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours courses should include enabling content so graduates can apply mathematical ideas and tools, such as rearranging equations, calculus and graphical and statistical methods, to chemical problems and data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.8.b4
  locator: { number: "3.8.b4", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 39964, end: 40131 }
  source: "choose and deploy methods for data analysis and manipulation, potentially including coding and scripting, for presentation, communication and problem- solving purposes"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["choose", "deploy"]
  about: "data analysis, coding and scripting"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours courses should include enabling content so graduates can pick and apply methods for analysing and handling data, which may include coding or scripting, to present, communicate and solve problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.8.b5
  locator: { number: "3.8.b5", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 40134, end: 40244 }
  source: "collaborate and work successfully in a group environment, contributing positively and flexibly to team outputs"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["collaborate", "work"]
  about: "teamwork"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours courses should include enabling content so graduates can work well with others in a group, contributing constructively and adaptably to shared outputs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.8.b6
  locator: { number: "3.8.b6", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 40247, end: 40358 }
  source: "communicate effectively, selecting appropriate content, media and methods for the audience, purpose and subject"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["communicate", "selecting"]
  about: "communication for audience and purpose"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours courses should include enabling content so graduates can communicate well, choosing content, medium and method to suit the audience, purpose and topic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.8.b7
  locator: { number: "3.8.b7", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 40361, end: 40533 }
  source: "comprehend the nature of and discriminate between different forms of published information, recognising the contribution of peer review to shaping the scientific literature"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["comprehend", "discriminate", "recognising"]
  about: "kinds of published information and peer review"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours courses should include enabling content so graduates can tell apart different kinds of published information and understand how peer review shapes the scientific literature."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.8.b8
  locator: { number: "3.8.b8", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 40536, end: 40664 }
  source: "realise the nature and value of their own and other's intellectual property and the importance of acting with academic integrity"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["realise"]
  about: "intellectual property and academic integrity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours courses should include enabling content so graduates can understand what their own and others' intellectual property is and is worth, and why academic integrity matters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.8.b9
  locator: { number: "3.8.b9", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 40667, end: 40838 }
  source: "act professionally, with due regard for legal, ethical and societal responsibilities, modelling good practice that promotes positive perceptions of chemistry and chemists."
  stem: "3.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["act", "modelling", "promotes"]
  about: "professional, ethical conduct"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours courses should include enabling content so graduates can behave professionally, mindful of legal, ethical and social duties, setting an example that reflects well on chemistry and chemists."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.9.b1
  locator: { number: "3.9.b1", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 40991, end: 41099 }
  source: "develop innovative approaches to solving advanced problems, sometimes in the absence of complete information"
  stem: "3.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "integrated master's graduates in chemistry"
  addressee: learner
  verbs: ["develop", "solving"]
  about: "new approaches to advanced problems"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Integrated master's courses should build on the honours skills so graduates can devise new ways to tackle advanced problems, at times without full information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.9.b2
  locator: { number: "3.9.b2", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 41102, end: 41253 }
  source: "develop persuasive arguments, and articulate their positions, synthesising their knowledge and skills to provide a convincing narrative for their ideas"
  stem: "3.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "integrated master's graduates in chemistry"
  addressee: learner
  verbs: ["develop", "articulate", "synthesising", "provide"]
  about: "persuasive argument"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Integrated master's courses should build on the honours skills so graduates can build persuasive arguments and state their position, drawing knowledge and skills together into a convincing case for their ideas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.9.b3
  locator: { number: "3.9.b3", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 41256, end: 41492 }
  source: "interrogate and integrate diverse sources of scientific literature alongside other information sources, in order to design and develop methods for investigation and analysis, including in areas outside their current specialist knowledge"
  stem: "3.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "integrated master's graduates in chemistry"
  addressee: learner
  verbs: ["interrogate", "integrate", "design", "develop"]
  about: "literature to design methods"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Integrated master's courses should build on the honours skills so graduates can question and combine varied scientific literature and other information to design methods of investigation and analysis, also beyond their specialism."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.9.b4
  locator: { number: "3.9.b4", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 41495, end: 41663 }
  source: "develop generalisable strategies for solving problems where there is not a unique solution, including the identification and sourcing of additional information required"
  stem: "3.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "integrated master's graduates in chemistry"
  addressee: learner
  verbs: ["develop", "solving"]
  about: "strategies for problems without a single answer"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Integrated master's courses should build on the honours skills so graduates can build general strategies for problems with more than one answer, including finding the extra information needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.9.b5
  locator: { number: "3.9.b5", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 41666, end: 41718 }
  source: "plan and manage their own and group work effectively"
  stem: "3.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "integrated master's graduates in chemistry"
  addressee: learner
  verbs: ["plan", "manage"]
  about: "planning own and group work"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Integrated master's courses should build on the honours skills so graduates can plan and manage their own work and a group's work well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.9.b6
  locator: { number: "3.9.b6", headingPath: ["Content, structure and delivery", "Underpinning and enabling knowledge and skills"] }
  span: { start: 41721, end: 41800 }
  source: "demonstrate preparedness for research, doctoral study or equivalent employment."
  stem: "3.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "integrated master's graduates in chemistry"
  addressee: learner
  verbs: ["demonstrate"]
  about: "readiness for research or doctoral study"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Integrated master's courses should build on the honours skills so graduates can show readiness for research, a doctorate or employment at a similar level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.10
  locator: { number: "3.10", headingPath: ["Content, structure and delivery", "Project and dissertation"] }
  span: { start: 41826, end: 42870 }
  source: "3.10 All honours degree students are expected to engage in an element of independent open-ended investigative work through a project/research-based assignment relevant to chemistry. This is likely to be in the student's final year of study and to involve data collection and analysis from laboratory or literature work. It may cover areas outside of laboratory research such as chemistry education, theoretical and computer modelling, citizen science projects or in the public understanding of science. Interpretation of the information is within the context of current knowledge. At master's level, the project is expected to include an element of originality. Outputs may take the form of dissertations or review and research articles. Typically, some form of oral defence by viva, poster presentation or talk will also be included. At master's level, the quality (but not necessarily the format) of the presentation\n\n13\nand critical evaluation in the written report/dissertation should be equivalent to that of a peer- reviewed publication.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours and master's students in chemistry"
  addressee: learner
  verbs: ["engage", "include"]
  about: "the independent investigative project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Every honours student is expected to carry out some independent, open-ended investigation through a project or research assignment, usually in the final year; at master's level the project is expected to show some originality, and the presentation and critical evaluation in its written report should match the quality of a peer-reviewed publication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 44681, end: 45482 }
  source: "3.15 Teaching and learning strategies are designed to provide students with appropriate subject knowledge, understanding, abilities and academic and professional skills for chemistry-based professions. This Subject Benchmark Statement does not aim to be prescriptive about which teaching or learning methods are used by a particular course. Higher education providers use appropriate teaching methods to ensure that students are engaged, motivated and challenged to learn as well as delivering the course learning outcomes. Such methods must be made explicit to students and be subject to regular internal and external review. Attention should be paid in the design process to ensure that teaching methods support achievement of the learning outcomes and are inclusive and accessible to all students.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "teaching and learning in chemistry courses"
  addressee: provider
  verbs: ["made", "paid", "support"]
  about: "explicit, reviewed, inclusive teaching methods"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The statement does not prescribe teaching methods; whatever methods are used must be explained to students and reviewed regularly inside and outside the institution, and the design should make sure they support the outcomes and are inclusive and accessible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/3.20
  locator: { number: "3.20", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 47534, end: 47997 }
  source: "3.20 Such teaching and learning strategies are not fixed but should be responsive to changes in technology and current research around teaching pedagogy. There is therefore an expectation that all staf f who contribute to student learning and assessment, including technical demonstrators, temporary and visiting lecturers as well as academic staff, should have access to both subject-specific and educational professional development resources and opportunities."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "teaching strategies and teaching staff"
  addressee: provider
  verbs: ["contribute", "have"]
  about: "responsive strategies; development for all teaching staff"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Teaching strategies should change with technology and with research on pedagogy, so everyone who teaches or assesses, technical demonstrators and visiting lecturers as well as academics, should have access to subject and educational development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/3.21
  locator: { number: "3.21", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 48009, end: 48294 }
  source: "3.21 The assessment of students' achievement in chemistry aligns with learning outcomes and is appropriate to the knowledge, abilities, academic and professional skills that the course aims to develop. The diversity of assessment deployed across chemistry courses should reflect this.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment in chemistry courses"
  addressee: provider
  verbs: ["aligns", "reflect"]
  about: "assessment aligned and varied"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Assessment is tied to the learning outcomes and to the knowledge and skills the course builds, and the range of assessment used should reflect that."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/3.22
  locator: { number: "3.22", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 48294, end: 49228 }
  source: "3.22 The increasingly digital world we live in requires students to be future-ready through the development of general IT literacy and coding skills. The latter is becoming an increasingly common expectation of graduates in scientific fields and students should be provided opportunities to engage with these concepts in their studies. The digital world presents unique opportunities to diversify the methods by which we assess students. It is strongly encouraged that assessments make full use of a range of formats that enables\n\n15\nstudents of all backgrounds and characteristics to demonstrate their learning and develop to their fullest potential. Many assessments may be completed using a word processor, as well as spreadsheets and specialist graphical, drawing, modelling and information management software. However, others will require paper-based responses where formulae, diagrams and reaction schemes are drafted by hand.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "chemistry courses and their assessment"
  addressee: provider
  verbs: ["provided", "engage", "demonstrate"]
  about: "digital literacy, coding and varied formats"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A digital world asks students to be ready for the future through IT literacy and coding, and students should be given chances to engage with them; assessments are strongly encouraged to use a range of formats so all students can show their learning, though some tasks still call for hand-drawn formulae and schemes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/3.24
  locator: { number: "3.24", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 50313, end: 51022 }
  source: "3.24 Assessment drives learning and, wherever possible, it should support the development of skills and concepts required specifically for a career in chemistry but also of more general skills that enhance the wider employability of Chemistry graduates. Some examples of relevant skills and the assessment types that require them are shown in the mapping table below. Skills Assessment type a b c d e f g h i j k l m n o p Oral and written communication × × × × × × x × × × Team and group working × × × × × × Numeracy × × × × × × × × × Project planning and management × x × × × Practical × × × × × Problem-solving (unseen/ heterogeneous data) × × × × Enquiry × × × × × × × × × IT literacy × × × × × × × × × ×\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment in chemistry courses"
  addressee: provider
  verbs: ["support", "enhance"]
  about: "assessment that builds subject and employability skills"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Assessment drives learning and, where it can, should build both the skills and concepts a chemistry career needs and wider skills for employability; a map links skills such as communication, teamwork, numeracy and IT literacy to the assessment types that call on them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51678, end: 52156 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees which sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours degree-awarding providers"
  addressee: provider
  verbs: ["perform", "refer"]
  about: "Annex D for achievement above threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do much better than the minimum threshold; each provider decides what evidence shows this and should refer to Annex D, the common descriptions of the four honours classes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/4.6
  locator: { number: "4.6", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53410, end: 53523 }
  source: "4.6 The standards in these tables should be read in conjunction with Sections 1 and 3, and paragraphs 4.1 to 4.5."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "readers of the tables: course teams and examiners"
  addressee: provider
  verbs: ["read"]
  about: "reading the tables with their context"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The standards in the two tables should be read together with sections 1 and 3 and with the introductory paragraphs of section 4."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53847, end: 54022 }
  source: "Recall basic knowledge and theories in chemistry based on the course contents and use these in the discussion or explanation of familiar concepts with appropriate terminology."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Recall", "use"]
  about: "core chemical concepts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can remember the basic knowledge and theory taught on the course and draw on it, with the right terms, to discuss or explain familiar ideas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b1.excellent
  locator: { number: "4.6.b1.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 54023, end: 54213 }
  source: "Use and apply in-depth knowledge of concepts and theories in chemistry to discuss and predict outcomes covering most essential aspects of the course and show evidence of enquiry beyond this."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Use", "apply", "discuss", "predict", "show"]
  about: "core chemical concepts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b1, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can apply deep knowledge of chemical concepts and theory to discuss and predict outcomes across most core parts of the course, and show enquiry that goes further."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 54353, end: 54465 }
  source: "Adequately define and solve routine problems, applying a range of methods and concepts taught within the course."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["define", "solve", "applying"]
  about: "solving chemical problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can set out and work through routine problems adequately, using a variety of the methods and ideas taught."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b2.excellent
  locator: { number: "4.6.b2.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 54466, end: 54567 }
  source: "Devise and evaluate solutions to solve both routine and unfamiliar problems using a range of methods."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Devise", "evaluate", "solve", "using"]
  about: "solving chemical problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b2, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can devise and judge solutions to problems, familiar or new, drawing on several methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 54805, end: 54940 }
  source: "Produce and follow risk assessments f or completing practical work in a safe and reliable manner with significant reliance on guidance."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Produce", "follow"]
  about: "safe practice and risk assessment"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can write and work to risk assessments so practical work is done safely and reliably, leaning heavily on guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b3.excellent
  locator: { number: "4.6.b3.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 54941, end: 55072 }
  source: "Produce and follow risk assessments f or completing practical work in a safe and reliable manner with limited reliance on guidance."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Produce", "follow"]
  about: "safe practice and risk assessment"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b3, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can write and work to risk assessments so practical work is done safely and reliably, with little need for guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55249, end: 55413 }
  source: "Suggest and attempt synthesis, purification, isolation and characterisation strategies accurately with a degree of independence and justify choice/use of technique."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Suggest", "attempt", "justify"]
  about: "synthesis, purification and characterisation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can propose and try out accurate approaches to making, purifying, isolating and characterising compounds with some independence, and give reasons for the techniques chosen."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b4.excellent
  locator: { number: "4.6.b4.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55414, end: 55568 }
  source: "Design, evaluate and complete synthesis, purification, isolation and characterisation strategies accurately with a high degree of autonomy and efficiency."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Design", "evaluate", "complete"]
  about: "synthesis, purification and characterisation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b4, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can design, assess and carry through accurate approaches to making, purifying, isolating and characterising compounds, working efficiently and largely on their own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55997, end: 56191 }
  source: "Suggest, carry out and report qualitative and quantitative sample preparation and purification, chemical measurement, metrology and appropriate analysis accurately with a degree of independence."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Suggest", "carry", "report"]
  about: "chemical measurement and analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can propose, perform and write up accurate sample preparation, measurement and analysis, qualitative and quantitative, with some independence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b5.excellent
  locator: { number: "4.6.b5.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56192, end: 56411 }
  source: "Design, optimise, carry out and report qualitative and quantitative sample preparation and purification, chemical measurement, metrology and appropriate analysis accurately with a high degree of autonomy and efficiency."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Design", "optimise", "carry", "report"]
  about: "chemical measurement and analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b5, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can design, refine, perform and write up accurate sample preparation, measurement and analysis, efficiently and with a high level of autonomy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56540, end: 56646 }
  source: "Use computational techniques and tools to investigate familiar chemical concepts covered in course content"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Use", "investigate"]
  about: "computational chemistry"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can use computational methods and software to explore familiar chemical ideas from the course, reporting what is found in the right terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b6.excellent
  locator: { number: "4.6.b6.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56647, end: 56766 }
  source: "Select and use appropriate computational techniques and tools to investigate complex chemical concepts and evaluate and"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Select", "use", "investigate", "evaluate"]
  about: "computational chemistry"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b6, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can choose and use suitable computational methods and software to explore complex chemical ideas, judging and reporting the results in the right terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b7
  locator: { number: "4.6.b7", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56906, end: 56984 }
  source: "Identify and select appropriate resources and sources of chemical information."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Identify", "select"]
  about: "using the chemical literature"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can track down and choose fitting sources of chemical information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b7.excellent
  locator: { number: "4.6.b7.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56985, end: 57098 }
  source: "Identify and select appropriate resources and sources of chemical information with a high degree of independence."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Identify", "select"]
  about: "using the chemical literature"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b7, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can track down and choose fitting sources of chemical information, largely unaided."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b8
  locator: { number: "4.6.b8", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57218, end: 57290 }
  source: "Complete an open-ended investigative project/ research-based assignment."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Complete"]
  about: "the independent project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can carry an open-ended investigation or research-based assignment through to completion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b8.excellent
  locator: { number: "4.6.b8.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57291, end: 57397 }
  source: "Complete an open-ended investigative project/ research-based assignment with a high level of independence."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Complete"]
  about: "the independent project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b8, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can carry an open-ended investigation or research-based assignment through to completion, working very independently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b9
  locator: { number: "4.6.b9", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57579, end: 57679 }
  source: "Identify and discuss application of chemistry in solving current and future challenges in the world."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Identify", "discuss"]
  about: "chemistry and global challenges"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can name and discuss how chemistry is applied to present and future problems facing the world."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b9.excellent
  locator: { number: "4.6.b9.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57680, end: 57793 }
  source: "Explain and suggest ways in which chemistry can contribute to solving current and future challenges in the world."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Explain", "suggest"]
  about: "chemistry and global challenges"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b9, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can explain how chemistry can help with present and future world problems and propose ways it might do so."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b10
  locator: { number: "4.6.b10", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57958, end: 58060 }
  source: "Identify and explain relationships between chemistry and other subjects as relevant to course content."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Identify", "explain"]
  about: "chemistry and other subjects"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can point out and explain links between chemistry and other subjects met on the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b10.excellent
  locator: { number: "4.6.b10.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58061, end: 58136 }
  source: "Evaluate and explain contribution of chemistry to multidisciplinary issues."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Evaluate", "explain"]
  about: "chemistry and other subjects"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b10, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can assess and explain what chemistry brings to issues that cross several disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b11
  locator: { number: "4.6.b11", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58328, end: 58469 }
  source: "Select and use mathematical concepts, processes and tools to solve familiar chemical problems and evaluate chemical data, usually accurately."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Select", "use", "solve", "evaluate"]
  about: "mathematics in chemistry"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can pick and apply mathematical ideas and tools to familiar chemistry problems and to judging data, accurately most of the time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b11.excellent
  locator: { number: "4.6.b11.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58470, end: 58619 }
  source: "Consistently and accurately select and use mathematical concepts, processes and tools to solve familiar chemical problems and evaluate chemical data."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["select", "use", "solve", "evaluate"]
  about: "mathematics in chemistry"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b11, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can pick and apply mathematical ideas and tools to familiar chemistry problems and to judging data, with consistent accuracy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b12
  locator: { number: "4.6.b12", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58789, end: 58876 }
  source: "Select and correctly use methods for data analysis and manipulation with some guidance."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Select", "use"]
  about: "data analysis methods"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can choose and apply data-handling and analysis methods correctly, with some guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b12.excellent
  locator: { number: "4.6.b12.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58877, end: 58995 }
  source: "Select, evaluate and correctly use methods for data analysis and manipulation in complex and unpredictable situations."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Select", "evaluate", "use"]
  about: "data analysis methods"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b12, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can choose, assess and apply data-handling and analysis methods correctly in complex, unpredictable situations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b13
  locator: { number: "4.6.b13", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 59108, end: 59153 }
  source: "Provide useful contributions to team outputs."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Provide"]
  about: "teamwork"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can make useful contributions to what a team produces."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b13.excellent
  locator: { number: "4.6.b13.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 59154, end: 59256 }
  source: "Provide clear and valuable contributions to team outputs exhibiting teamwork and/or leadership skills."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Provide", "exhibiting"]
  about: "teamwork"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b13, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can make clear, valuable contributions to what a team produces, showing teamwork, leadership or both."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b14
  locator: { number: "4.6.b14", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 59370, end: 59498 }
  source: "Communicate information, ideas, problems and solutions verbally, electronically and in writing, with clear expression and style."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Communicate"]
  about: "communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for the honours degree, the graduate can get information, ideas, problems and solutions across clearly in speech, in writing and electronically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.6.b14.excellent
  locator: { number: "4.6.b14.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 59499, end: 59717 }
  source: "Communicate information, ideas, problems and solutions to an accomplished level verbally, electronically and in writing, in an accurate, fluent and sophisticated style, at a level consistently appropriate for audience."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates in chemistry"
  addressee: learner
  verbs: ["Communicate"]
  about: "communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/chemistry-2022/4.6.b14, basis: stated }
  paraphrase: "At the excellent standard, the level of a first-class degree, the graduate can get information, ideas, problems and solutions across to a high standard in speech, writing and electronic forms, accurately, fluently and with sophistication, always pitched to the audience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.7
  locator: { number: "4.7", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 59894, end: 60230 }
  source: "4.7 There are a range of master's courses (integrated and standalone), but all students should have attained the thresholds in Table 1. Master's courses further develop transferable skills and depth of knowledge, in particular, mastery of one or more specialist areas or applications of chemistry and independence in project-based work."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students in chemistry, integrated and standalone"
  addressee: learner
  verbs: ["attained", "develop"]
  about: "Table 1 thresholds as the base for master's"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Whatever kind of master's course, integrated or standalone, all students should have reached the Table 1 thresholds; master's courses then deepen knowledge and transferable skills, above all mastery of a specialism and independence in project work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60395, end: 60557 }
  source: "Develop, integrate, synthesise and apply the systematic and broad understanding of relevant and state-of-the-art chemical concepts to solve more complex problems."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in chemistry, integrated and standalone"
  addressee: learner
  verbs: ["Develop", "integrate", "synthesise", "apply", "solve"]
  about: "applying advanced understanding to complex problems"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the threshold for a master's degree, beyond Table 1, the graduate can build up, combine and apply a broad, systematic grasp of current chemical concepts to harder problems, with substantial support and guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.7.b1.excellent
  locator: { number: "4.7.b1.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60395, end: 60557 }
  source: "Develop, integrate, synthesise and apply the systematic and broad understanding of relevant and state-of-the-art chemical concepts to solve more complex problems."
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:7
  appliesTo: "master's graduates in chemistry, integrated and standalone"
  addressee: learner
  verbs: ["Develop", "integrate", "synthesise", "apply", "solve"]
  about: "applying advanced understanding to complex problems"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: { statement: qaa/chemistry-2022/4.7.b1, basis: stated }
  paraphrase: "At the excellent standard for a master's degree, the graduate can build up, combine and apply a broad, systematic grasp of current chemical concepts to harder problems largely independently and autonomously."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60646, end: 60917 }
  source: "Interrogate and integrate diverse sources of scientific literature alongside other information sources, in order to design and develop methods for investigation and analysis, including in areas at the forefront of knowledge and outside their current specialist knowledge."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in chemistry, integrated and standalone"
  addressee: learner
  verbs: ["Interrogate", "integrate", "design", "develop"]
  about: "using the literature to design methods"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the threshold for a master's degree, beyond Table 1, the graduate can question and combine varied scientific literature and other information to design methods of investigation, at the forefront and beyond their specialism, with substantial support and guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.7.b2.excellent
  locator: { number: "4.7.b2.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60646, end: 60917 }
  source: "Interrogate and integrate diverse sources of scientific literature alongside other information sources, in order to design and develop methods for investigation and analysis, including in areas at the forefront of knowledge and outside their current specialist knowledge."
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:7
  appliesTo: "master's graduates in chemistry, integrated and standalone"
  addressee: learner
  verbs: ["Interrogate", "integrate", "design", "develop"]
  about: "using the literature to design methods"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: { statement: qaa/chemistry-2022/4.7.b2, basis: inferred }
  paraphrase: "At the excellent standard for a master's degree, the graduate can question and combine varied scientific literature and other information to design methods of investigation, at the forefront and beyond their specialism largely independently and autonomously."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60918, end: 61045 }
  source: "Project planning, including, as appropriate, evaluation of ethics, hazards and environmental effects and appreciation of costs."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in chemistry, integrated and standalone"
  addressee: learner
  verbs: []
  about: "project planning"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the threshold for a master's degree, beyond Table 1, the graduate can plan a project, weighing ethics, hazards, environmental effects and costs where relevant, with substantial support and guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.7.b3.excellent
  locator: { number: "4.7.b3.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60918, end: 61045 }
  source: "Project planning, including, as appropriate, evaluation of ethics, hazards and environmental effects and appreciation of costs."
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:7
  appliesTo: "master's graduates in chemistry, integrated and standalone"
  addressee: learner
  verbs: []
  about: "project planning"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: { statement: qaa/chemistry-2022/4.7.b3, basis: inferred }
  paraphrase: "At the excellent standard for a master's degree, the graduate can plan a project, weighing ethics, hazards, environmental effects and costs where relevant largely independently and autonomously."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 61046, end: 61135 }
  source: "Development of advanced experimental and investigative skills as appropriate for project."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in chemistry, integrated and standalone"
  addressee: learner
  verbs: []
  about: "advanced experimental skills"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the threshold for a master's degree, beyond Table 1, the graduate can develop the advanced practical and investigative skills a project calls for, with substantial support and guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.7.b4.excellent
  locator: { number: "4.7.b4.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 61046, end: 61135 }
  source: "Development of advanced experimental and investigative skills as appropriate for project."
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:7
  appliesTo: "master's graduates in chemistry, integrated and standalone"
  addressee: learner
  verbs: []
  about: "advanced experimental skills"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: { statement: qaa/chemistry-2022/4.7.b4, basis: inferred }
  paraphrase: "At the excellent standard for a master's degree, the graduate can develop the advanced practical and investigative skills a project calls for largely independently and autonomously."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 61136, end: 61247 }
  source: "Discussion of the background, context, methods, results and potential impact of a significant research project."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in chemistry, integrated and standalone"
  addressee: learner
  verbs: []
  about: "discussing a research project"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the threshold for a master's degree, beyond Table 1, the graduate can discuss the background, context, methods, results and likely impact of a substantial research project, with substantial support and guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/chemistry-2022/4.7.b5.excellent
  locator: { number: "4.7.b5.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 61136, end: 61247 }
  source: "Discussion of the background, context, methods, results and potential impact of a significant research project."
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:7
  appliesTo: "master's graduates in chemistry, integrated and standalone"
  addressee: learner
  verbs: []
  about: "discussing a research project"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: { statement: qaa/chemistry-2022/4.7.b5, basis: inferred }
  paraphrase: "At the excellent standard for a master's degree, the graduate can discuss the background, context, methods, results and likely impact of a substantial research project largely independently and autonomously."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/chemistry-2022/1.2
  forPractitioner: { text: "Read the course aims through an inclusion lens: choose material that is relevant and representative for every student, and build a setting where all feel welcome and valued.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level framing of the course aims: relevant, representative material and an inclusive environment for every student, for honours and master's courses. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 1.2. Do not present it as a student outcome or a legal duty; set it beside 1.10, 1.11 and 2.7 in this document."
  author-agent-dialogue: "Raise this when a team reviews its curriculum or induction and asks whether the material speaks to all its students. Frame it for staff as a test applied to every aim, not a separate module. Ask: 'Whose work and examples appear in your first-year material, and who might not see themselves there?' Avoid presenting it to a student as their task."
- statement: qaa/chemistry-2022/1.7
  forPractitioner: { text: "Let the breadth of chemistry show in both the topics covered and the variety of teaching, learning and assessment methods, whether the course is broad, specialist, joint or combined.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that courses reflect the breadth of chemistry in content and in methods. It applies to all chemistry courses, broad or specialist. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 1.7. Do not claim it requires every course to cover the whole field; set it beside 2.1, 3.2 and 3.21 in this document."
  author-agent-dialogue: "Raise this when a team designs a specialist, joint or combined chemistry course and asks how broad it must be. Put it to staff as breadth in methods as well as topics. Ask: 'Which parts of chemistry, and which kinds of assessment, does your course leave out, and is that a choice you can defend?' Avoid presenting it to a student as their duty."
- statement: qaa/chemistry-2022/1.8
  forPractitioner: { text: "Plan practical work as a spiral: detailed instructions and forgiving experiments early, then less support, so that final-year students work precisely with little supervision and every graduate is safe and accurate in the laboratory.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your course you will be able to work safely and accurately in a laboratory, and in your final year you will work precisely with little supervision, solving problems as they come up.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level expectation that every chemistry graduate is competent at safe, accurate laboratory work, with final-year students working precisely under minimal supervision, for honours (FHEQ level 6) and integrated master's courses. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 1.8. Do not claim it sets a professional licence or a fixed number of laboratory hours; set it beside 3.3.b2, 4.6.b3 and 4.6.b4 in this document and the FHEQ honours descriptor qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise this when a student asks how much practical work matters or why early labs are so tightly scripted, or when a team plans its laboratory programme. To a student, explain that support is reduced step by step until you can work alone; to staff, frame it as the spiral the course should build. Ask: 'Which experiment could you now run with no script, and where do you still need one?' Avoid suggesting that early mistakes in the laboratory count against them."
- statement: qaa/chemistry-2022/1.11
  forPractitioner: { text: "Teach the history and applications of chemistry inclusively as a must; as shoulds, credit chemists from diverse backgrounds, give learners room to follow topics tied to their own experience, and ask them to weigh benefits and harms of discoveries.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must-level duty to view and teach the history and applications of chemistry inclusively, with should-level expectations on curricula and learner choice. It applies to all chemistry courses. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 1.11. Do not weaken the must or strengthen the shoulds, and do not present it as a student outcome; set it beside 1.2, 1.10 and 3.4.b1 in this document."
  author-agent-dialogue: "Raise this when a team reviews whose discoveries its teaching names or plans a module on the history or impact of chemistry. Frame it for staff as a firm duty with shoulds attached. Ask: 'Which chemists from under-represented backgrounds appear in your course, and where do students judge the harms as well as the benefits of chemistry?' Avoid presenting it to students as their responsibility."
- statement: qaa/chemistry-2022/1.12
  forPractitioner: { text: "Inspire students to engage with global challenges through chemistry; draw topics where useful from the SDGs, such as health, energy, clean water and the environment, and use the QAA and Advance HE ESD guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that chemistry courses inspire engagement with personal, human and global challenges, with the SDGs as an optional source of topics. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 1.12. Do not present the SDGs as a mandatory checklist; set it beside 3.3.b3, 3.3.b13 and 4.6.b9 in this document and the ESD guidance std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise this when a team maps sustainability content or asks how to make it more than one module. Frame it for staff as inspiration through chemistry's own problems, such as clean energy or water. Ask: 'Where in the course do students use chemistry on a real sustainability problem?' Avoid reading the issuer's text on the SDGs aloud at length."
- statement: qaa/chemistry-2022/1.13
  forPractitioner: { text: "Build both subject-specific professional skills and wider attributes into the course, so graduates can work in the chemical sciences or in other sectors; 3.8 lists the wider skills.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should prepare you for work in chemistry and beyond it, giving you both subject expertise and the wider skills employers in other sectors value.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation with two sides: courses equip students for life after graduation, and graduates hold both subject and wider attributes (honours, FHEQ level 6). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 1.13. Do not claim it guarantees employment; set it beside 3.5, 3.6 and the enabling skills 3.8.b1 to 3.8.b9 in this document and the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3."
  author-agent-dialogue: "Raise this when a student asks what the degree prepares them for beyond the laboratory, or when a team reviews employability. To a student, put it as subject skills plus wider attributes that travel to other careers; to staff, as a course duty. Ask: 'Which of your skills would an employer outside chemistry value, and where did you build them?' Avoid promising particular jobs."
- statement: qaa/chemistry-2022/2.1
  forPractitioner: { text: "Whatever structure the course takes, branches or applications, make sure it combines fundamental theory and application in suitable proportion.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that every chemistry course combines theory and application, whatever its structure. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.1. Do not claim it prescribes the traditional branches or any one structure; set it beside 1.7 and 3.2 in this document."
  author-agent-dialogue: "Raise this when a team chooses how to organise its course. Frame it for staff as freedom of structure with a fixed need for both theory and application. Ask: 'If your course leads with applications, where do students meet the underlying theory?' Avoid presenting it to students."
- statement: qaa/chemistry-2022/2.3
  forPractitioner: { text: "Give honours students subject knowledge, understanding and skills together with wider transferable skills; in an integrated master's, meet the honours outcomes and add the depth, specialist knowledge and project work of master's level.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation of what the honours degree provides, with a statement of the two undergraduate awards and their levels (FHEQ 6 and FQHEIS 10; FHEQ 7 and FQHEIS 11). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.3. Do not claim standalone MSc or MRes courses carry the honours outcomes; set it beside 3.8, 3.9 and 4.7 in this document and std:doc:qaa-fheq-2024-framework, Table 1."
  author-agent-dialogue: "Raise this when a student weighs a bachelor's against an integrated master's, or a team designs both. For staff, frame it as two awards with distinct outcomes at two levels. Ask: 'What does your integrated master's add beyond the honours outcomes, and where?' Avoid treating it as a student standard."
- statement: qaa/chemistry-2022/2.4
  forPractitioner: { text: "Where a placement carries credit, integrate it with the rest of the course so students connect what they do on placement with their academic work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that credit-bearing placements are integrated with academic study. It applies to bachelor's and integrated master's courses that offer placements. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.4. Do not claim every course must offer a placement; set it beside 2.13 and 3.19 in this document."
  author-agent-dialogue: "Raise this when a team designs or reviews a placement year. Frame it for staff as a link students should be able to draw between placement and study. Ask: 'How do students bring what they learn on placement back into their final-year work?' Avoid presenting it to a student as a requirement."
- statement: qaa/chemistry-2022/2.6
  forPractitioner: { text: "Design the academic component of a chemistry degree apprenticeship to the same outcomes as other chemistry degrees, reading the apprenticeships characteristics statement alongside.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that the academic component of chemistry degree apprenticeships follows this statement. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.6. Do not claim it covers the work-based or end-point parts of an apprenticeship; set it beside the Characteristics Statement for Higher Education in Apprenticeships (not yet ingested) and 2.14 in this document."
  author-agent-dialogue: "Raise this when a team builds a degree apprenticeship in chemistry. Frame it for staff as the same academic standards in a different delivery model. Ask: 'Where does your apprenticeship meet the outcomes of Table 1?' Avoid presenting it to apprentices as an extra duty."
- statement: qaa/chemistry-2022/2.7
  forPractitioner: { text: "As a must, design learning and assessment inclusively so they are equally accessible, adding reasonable individual adjustments where needed; as a should, vary the experiences to reflect the subject and widen access.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must-level duty on chemistry courses: learning and assessment equally accessible to all, by inclusive design and reasonable adjustment, with a should on varied experiences. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.7. Do not weaken the must or present it as a student outcome; set it beside 2.8, 2.13 and 3.15 in this document."
  author-agent-dialogue: "Raise this when a team plans assessment or laboratory work, or a disabled student asks what to expect. Frame it for staff as a duty met first by design, then by adjustment; to a student, only as what they can expect. Ask: 'Which assessment in your course would a student with a visual impairment find hardest, and what would you redesign?' Avoid placing the duty on the student."
- statement: qaa/chemistry-2022/2.8
  forPractitioner: { text: "Check every element, curriculum, pedagogy, assessment and practicals, for full accessibility, and support all learners in the verbal, spatial and numerical skills chemistry needs.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must-level duty on course teams: fully accessible design of curricula, pedagogy, assessment and practicals, and support for all learners in the skills chemical problems need. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.8. Do not present it as a student outcome; set it beside 2.7 and 3.15 in this document."
  author-agent-dialogue: "Raise this with a team reviewing its practical classes or spatial-reasoning tasks. Frame it for staff as a design duty covering practicals as well as lectures. Ask: 'How would a student who cannot stand at a bench complete your laboratory course?' Avoid presenting it to students as theirs to solve."
- statement: qaa/chemistry-2022/2.9
  forPractitioner: { text: "Sequence the course so students move from simple concepts and well-defined problems to complex concepts and open-ended ones, ending with the competence a chemistry career needs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should take you from using simple ideas on clear-cut problems to connecting harder ideas on open-ended ones, so that you finish ready for a career in chemistry or another field.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on course design, with a will-level account of where students arrive, for honours (FHEQ level 6) and integrated master's courses. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.9. Do not claim it sets the outcomes for each year; set it beside 2.10, 2.11 and 4.6.b2 in this document and the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1."
  author-agent-dialogue: "Raise this when a student finds later problems much less defined than earlier ones, or a team plans the sequence of problem types. To a student, explain that the shift to open problems is intended; to staff, frame it as a progression to design. Ask: 'Can you name a problem you solved this year that had no single right answer?' Avoid suggesting struggle with open problems means failure."
- statement: qaa/chemistry-2022/2.10.b1
  forPractitioner: { text: "Plan induction and early teaching around the range of prior experience in the cohort and the difficulty of moving into higher education.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as one of four should-level strategies that support progression from guided study to independence. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.10, first item. Do not present it as a student outcome; set it beside 2.10.b2 to 2.10.b4 and 2.2 in this document."
  author-agent-dialogue: "Raise this when a team plans induction or first-year support. Frame it for staff as planning for varied starting points. Ask: 'What do you know about the routes your students took into the course, and how does first year allow for them?' Avoid presenting it to students."
- statement: qaa/chemistry-2022/2.10.b2
  forPractitioner: { text: "Check that progression arrangements let students of any background or motivation reach their potential.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level strategy for progression with an inclusion aim. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.10, second item. Do not present it as a student outcome; set it beside 2.10.b1, 1.2 and 2.7 in this document."
  author-agent-dialogue: "Raise this when a team studies who progresses and who does not. Frame it for staff as a question of equal chances. Ask: 'Do progression rates in your course differ by background, and what would explain it?' Avoid presenting it to students."
- statement: qaa/chemistry-2022/2.10.b3
  forPractitioner: { text: "Give personal development a place beside academic learning in the support that moves students through the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level strategy for progression. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.10, third item. Do not present it as a student outcome; set it beside 2.9 and 3.6 in this document."
  author-agent-dialogue: "Raise this when a team reviews personal tutoring or skills support. Frame it for staff as development beyond content. Ask: 'Where does your course support personal development, not only knowledge?' Avoid presenting it to students."
- statement: qaa/chemistry-2022/2.10.b4
  forPractitioner: { text: "Align progression strategies with the documented outcomes or competencies at each level of the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level strategy for progression. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.10, fourth item. Do not claim it sets level outcomes itself; set it beside 2.11 in this document and the FHEQ level descriptors qaa/fheq-2024/4.10, 4.12 and 4.15."
  author-agent-dialogue: "Raise this when a team writes level outcomes. Frame it for staff as alignment between support and outcomes. Ask: 'Does your second-year support match what level 5 asks of students?' Avoid presenting it to students."
- statement: qaa/chemistry-2022/2.11
  forPractitioner: { text: "Write progression rules that require students to show the overall threshold for each level, usually with credit for every element including practical courses; set any extra criteria for specialist titles, placements or the integrated master's.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must-level duty on institutions: progression rules require evidence that the overall threshold for the level has been met. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.11. Do not claim it sets the threshold for each year's content; set it beside 2.10.b4 and 4.6.b1 in this document and the FHEQ level descriptors."
  author-agent-dialogue: "Raise this when a team writes or reviews progression regulations, or a student asks why a failed practical blocks progression. To staff, frame it as a firm duty; to a student, explain only that each level has a threshold. Ask: 'Does your regulation let a student progress without passing the practical course?' Avoid presenting the duty as the student's."
- statement: qaa/chemistry-2022/2.13
  forPractitioner: { text: "Keep the course flexible to change in the subject and in employers' needs, and make reasonable adjustments for learners as required.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that courses take account of learners' needs with reasonable adjustments, alongside an unmodalled call for flexibility. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.13. Do not claim it requires part-time or distance routes; set it beside 2.7 and 2.8 in this document."
  author-agent-dialogue: "Raise this when a team reviews modes of study or responds to a change in the field. Frame it for staff as responsiveness to the subject and to learners. Ask: 'When did your course last change because of a shift in chemistry or in employers' needs?' Avoid presenting it to students."
- statement: qaa/chemistry-2022/2.16
  forPractitioner: { text: "Bring external reviewers into periodic review to test changes, confirm the threshold standards and check that content fits chemistry.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level statement of provider practice: external reviewers in periodic review, partly to confirm threshold standards. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.16. Do not confuse it with external examining (2.17); set it beside 2.15, 2.17 and 2.19 in this document."
  author-agent-dialogue: "Raise this with a team preparing for periodic review. Frame it for staff as the outside check on the threshold column of Table 1. Ask: 'Which external reviewer will see your threshold evidence, and what will they compare it with?' Avoid presenting it to students."
- statement: qaa/chemistry-2022/2.19
  forPractitioner: { text: "Run regular evaluation that combines performance data, student feedback and expert review, and involve students, graduates, employers and professional bodies in improving the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on teams to monitor and evaluate continuously and to involve stakeholders in enhancement. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 2.19. Do not present it as a student outcome; set it beside 2.15 to 2.17 in this document."
  author-agent-dialogue: "Raise this when a team plans an annual review or a curriculum change. Frame it for staff as evaluation with students and employers at the table. Ask: 'Which change to your course in the past year came from student or employer input?' Avoid presenting it to students as a duty."
- statement: qaa/chemistry-2022/3.2
  forPractitioner: { text: "Treat the 3.3 content as the foundation, then develop parts of it further in later years according to your staff's specialisms.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on how to read the core content of 3.3: as foundational, to be developed further. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.2. Do not claim the 3.3 list is a complete syllabus; set it beside 3.3.b1 to 3.3.b14 and 4.4 in this document."
  author-agent-dialogue: "Raise this when a team asks whether 3.3 is a syllabus to cover in full. Frame it for staff as a foundation they build on in their own direction. Ask: 'Which parts of the core does your course take furthest, and why?' Avoid presenting it to students."
- statement: qaa/chemistry-2022/3.3.b1
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can describe and discuss the key concepts across the whole of chemistry with confidence, accuracy and detail, in the right terms; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to describe and discuss the key concepts across the whole of chemistry with confidence, accuracy and detail, in the right terms.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with key chemical concepts, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 1. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b1 and 4.6.b1.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on key chemical concepts, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'Which key concept could you explain in detail without notes, and which would you struggle with?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.3.b2
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can describe, record and follow safe practice, managing toxicity, stability and reactivity through knowledge-led risk assessment and practical work; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to describe, record and follow safe practice, managing toxicity, stability and reactivity through knowledge-led risk assessment and practical work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with safe working practices, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 2. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b3 and 4.6.b3.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on safe working practices, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'How did you decide the controls in your last risk assessment?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.3.b3
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can cut waste in practical work and use disposal methods that protect people in the laboratory and the environment; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to cut waste in practical work and use disposal methods that protect people in the laboratory and the environment.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with waste reduction and safe disposal, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 3. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b3 and 4.6.b3.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on waste reduction and safe disposal, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'What did you do to reduce or safely dispose of waste in your last experiment?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.3.b4
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can explain and justify how thermodynamics (classical and statistical), kinetics, quantum mechanics and spectroscopy work, and use them on problems in theory and in the laboratory; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to explain and justify how thermodynamics (classical and statistical), kinetics, quantum mechanics and spectroscopy work, and use them on problems in theory and in the laboratory.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with thermodynamics, kinetics, quantum mechanics and spectroscopy, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 4. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b2 and 4.6.b2.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on thermodynamics, kinetics, quantum mechanics and spectroscopy, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'Can you use thermodynamics or kinetics to explain why a reaction you ran behaved as it did?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.3.b5
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can predict likely products, bond-forming reactions, mechanisms, stereochemistry and reactivity, and use those predictions to propose routes to target compounds and to design experiments that test them; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to predict likely products, bond-forming reactions, mechanisms, stereochemistry and reactivity, and use those predictions to propose routes to target compounds and to design experiments that test them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with predicting reactions and planning synthesis, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 5. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b4 and 4.6.b4.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on predicting reactions and planning synthesis, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'For a target compound, could you propose a route and say which step is most likely to fail?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.3.b6
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can explain, plan and use ways to purify, isolate and characterise substances, guided by the physical and chemical properties and periodic trends of the elements and their compounds; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to explain, plan and use ways to purify, isolate and characterise substances, guided by the physical and chemical properties and periodic trends of the elements and their compounds.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with purification, isolation and characterisation, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 6. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b4 and 4.6.b4.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on purification, isolation and characterisation, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'Why would you choose one purification method over another for a given product?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.3.b7
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can discuss trends across the periodic table, explain what they mean for how elements react and behave and for their physical properties, and use this on problems in theory and practice; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to discuss trends across the periodic table, explain what they mean for how elements react and behave and for their physical properties, and use this on problems in theory and practice.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with periodic trends, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 7. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b2 and 4.6.b2.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on periodic trends, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'Which periodic trend best explains a reaction you have studied, and how?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.3.b8
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can describe atomic and molecular orbitals and how they help explain structure, bonding and the paths reactions take; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to describe atomic and molecular orbitals and how they help explain structure, bonding and the paths reactions take.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with atomic and molecular orbitals, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 8. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b1 and 4.6.b1.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on atomic and molecular orbitals, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'Could you sketch the orbitals involved in a bond you know well and explain what they show?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.3.b9
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can plan, develop and carry out qualitative and quantitative preparation and purification of samples, measurement, metrology and analysis, attending to accuracy, precision, traceability, complex matrices and sample size; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to plan, develop and carry out qualitative and quantitative preparation and purification of samples, measurement, metrology and analysis, attending to accuracy, precision, traceability, complex matrices and sample size.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with sample preparation, measurement and analysis, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 9. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b5 and 4.6.b5.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on sample preparation, measurement and analysis, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'How did you check the accuracy and precision of your last quantitative analysis?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.3.b10
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can explain the theory behind classical and instrumental analytical techniques and their limits, carry out analyses and measurements and report them in the right terms and notation; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to explain the theory behind classical and instrumental analytical techniques and their limits, carry out analyses and measurements and report them in the right terms and notation.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with analytical techniques and their limits, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 10. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b5 and 4.6.b5.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on analytical techniques and their limits, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'What are the limits of an instrumental technique you have used, and how did they affect your result?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.3.b11
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can use computational methods and software to understand chemical structure, bonding and reactivity better; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to use computational methods and software to understand chemical structure, bonding and reactivity better.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with computational methods, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 11. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b6 and 4.6.b6.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on computational methods, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'What has a computational model shown you about a molecule that you could not easily see otherwise?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.3.b12
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can know many organic and inorganic compounds, substances and materials and what each is for; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to know many organic and inorganic compounds, substances and materials and what each is for.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with inorganic and organic substances and their uses, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 12. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b1 and 4.6.b1.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on inorganic and organic substances and their uses, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'Can you name a material you have studied and explain what makes it fit for its use?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.3.b13
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can recognise how chemistry has fed the innovations of the modern world and how chemists can help meet present and future challenges; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to recognise how chemistry has fed the innovations of the modern world and how chemists can help meet present and future challenges.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with chemistry's part in innovation and future challenges, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 13. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b9 and 4.6.b9.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on chemistry's part in innovation and future challenges, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'Which modern innovation depends on chemistry, and which challenge could chemists help with next?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.3.b14
  forPractitioner: { text: "Cover this in the core chemistry content so every undergraduate can see how chemistry relates to and meets other subjects, so as to work well in multidisciplinary settings; it is foundational content to build on later (3.2).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course you should be able to see how chemistry relates to and meets other subjects, so as to work well in multidisciplinary settings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome of the core chemistry content: graduates able to work with chemistry and other subjects, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.3, item 14. Do not present it as a regulatory requirement or a complete syllabus. Set it beside the graded row 4.6.b10 and 4.6.b10.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what core chemistry they need on chemistry and other subjects, or when a team maps modules against the core content. To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. Ask: 'When have you used chemistry alongside another subject, and what did each bring?' Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."
- statement: qaa/chemistry-2022/3.4.b1
  forPractitioner: { text: "Optionally, add specialist or supplementary content so graduates can think about and discuss where and how chemistry grew as a culture and what it has done to society; it is a choice for the course, not a requirement.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "Your course may also give you the chance to think about and discuss where and how chemistry grew as a culture and what it has done to society.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an optional outcome (may) of specialist or supplementary content on the culture and history of chemistry and its social impact, for undergraduate courses at FHEQ level 6. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.4, item 1. Do not present it as a requirement of every chemistry course. Set it beside the core outcomes 3.3.b1 to 3.3.b14 in this document and spine:6."
  author-agent-dialogue: "Raise this when a student asks about options, specialisms or joint study, or a team considers adding specialist content. To a student, describe it as a possible opportunity, not a must; to staff, as an option the statement allows. Ask: 'How has chemistry changed the society you live in, for better and worse?' Avoid implying that a course lacking it falls short."
- statement: qaa/chemistry-2022/3.4.b2
  forPractitioner: { text: "Optionally, add specialist or supplementary content so graduates can focus on one or more specialist branches, for example sustainable (green) chemistry, cheminformatics or the teaching of chemistry; it is a choice for the course, not a requirement.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "Your course may also give you the chance to focus on one or more specialist branches, for example sustainable (green) chemistry, cheminformatics or the teaching of chemistry.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an optional outcome (may) of specialist or supplementary content on specialising in a branch of chemistry, for undergraduate courses at FHEQ level 6. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.4, item 2. Do not present it as a requirement of every chemistry course. Set it beside the core outcomes 3.3.b1 to 3.3.b14 in this document and spine:6."
  author-agent-dialogue: "Raise this when a student asks about options, specialisms or joint study, or a team considers adding specialist content. To a student, describe it as a possible opportunity, not a must; to staff, as an option the statement allows. Ask: 'Which branch of chemistry would you most like to specialise in, and why?' Avoid implying that a course lacking it falls short."
- statement: qaa/chemistry-2022/3.4.b3
  forPractitioner: { text: "Optionally, add specialist or supplementary content so graduates can place their chemistry within another honours subject, such as biology, physics or the environmental and pharmaceutical sciences, or link it to vocational fields such as business and law; it is a choice for the course, not a requirement.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "Your course may also give you the chance to place your chemistry within another honours subject, such as biology, physics or the environmental and pharmaceutical sciences, or link it to vocational fields such as business and law.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an optional outcome (may) of specialist or supplementary content on chemistry within other subjects and vocations, for undergraduate courses at FHEQ level 6. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.4, item 3. Do not present it as a requirement of every chemistry course. Set it beside the core outcomes 3.3.b1 to 3.3.b14 in this document and spine:6."
  author-agent-dialogue: "Raise this when a student asks about options, specialisms or joint study, or a team considers adding specialist content. To a student, describe it as a possible opportunity, not a must; to staff, as an option the statement allows. Ask: 'How does your chemistry connect with the other subject or field you are studying?' Avoid implying that a course lacking it falls short."
- statement: qaa/chemistry-2022/3.5
  forPractitioner: { text: "Give students repeated practice in building and testing arguments from evidence, alongside the creativity, resilience and teamwork the course develops.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should become logical and analytical, and confident in using evidence to build, support or knock down an argument.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation of chemistry graduates' reasoning, set within a plain-present account of their wider character, for honours (FHEQ level 6) and integrated master's courses. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.5. Do not turn the plain-present traits into requirements; set it beside 3.8.b2, 3.9.b2 in this document and the FHEQ honours descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise this when a student asks what makes a good chemistry argument or how to handle criticism of their ideas. To a student, put it as using evidence to support or challenge a claim; to staff, as a habit to build across modules. Ask: 'What evidence would make you change your mind about your last conclusion?' Avoid presenting the other traits in the paragraph as tests a student must pass."
- statement: qaa/chemistry-2022/3.6
  forPractitioner: { text: "Make development opportunities visible and give structured support for applications and interviews, in the curriculum or through extracurricular activity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on courses: make development explicit and support transition to further study or employment. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.6. Do not present it as a student outcome; set it beside 1.13 and 3.24 in this document."
  author-agent-dialogue: "Raise this when a team reviews careers support or personal tutoring. Frame it for staff as making the hidden development visible. Ask: 'Where does a student in your course learn to describe their skills to an employer?' Avoid presenting it to students as their obligation."
- statement: qaa/chemistry-2022/3.8.b1
  forPractitioner: { text: "Build enabling content into the honours course so every graduate can use digital tools to find, gather and organise information and data; it may sit inside the chemistry content (3.7).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you should be able to use digital tools to find, gather and organise information and data.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for honours graduates in chemistry, on digital information tools, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.8, item 1. Do not present it as a regulatory requirement or as a master's outcome. Set it beside the graded row 4.6.b7 and 4.6.b7.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5, the Annex D third-class description qaa/fheq-2024/annex-d/cognitive/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks which wider skills the degree builds on digital information tools, or when a team checks where those skills are taught and assessed. To a student, put it plainly in the second person; to staff, as enabling content the course should include. Ask: 'Which database or search tool do you use to find chemical information, and how do you organise what you find?' Avoid reading the issuer's list aloud or treating every item as a separate module."
- statement: qaa/chemistry-2022/3.8.b2
  forPractitioner: { text: "Build enabling content into the honours course so every graduate can choose, examine and criticise research papers and other sources so as to keep their knowledge current, learn further and help solve set problems; it may sit inside the chemistry content (3.7).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you should be able to choose, examine and criticise research papers and other sources so as to keep your knowledge current, learn further and help solve set problems.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for honours graduates in chemistry, on critical use of the literature, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.8, item 2. Do not present it as a regulatory requirement or as a master's outcome. Set it beside the graded row 4.6.b7 and 4.6.b7.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5, the Annex D third-class description qaa/fheq-2024/annex-d/cognitive/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks which wider skills the degree builds on critical use of the literature, or when a team checks where those skills are taught and assessed. To a student, put it plainly in the second person; to staff, as enabling content the course should include. Ask: 'How do you judge whether a paper you found is reliable enough to use?' Avoid reading the issuer's list aloud or treating every item as a separate module."
- statement: qaa/chemistry-2022/3.8.b3
  forPractitioner: { text: "Build enabling content into the honours course so every graduate can apply mathematical ideas and tools, such as rearranging equations, calculus and graphical and statistical methods, to chemical problems and data; it may sit inside the chemistry content (3.7).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you should be able to apply mathematical ideas and tools, such as rearranging equations, calculus and graphical and statistical methods, to chemical problems and data.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for honours graduates in chemistry, on mathematics for chemistry, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.8, item 3. Do not present it as a regulatory requirement or as a master's outcome. Set it beside the graded row 4.6.b11 and 4.6.b11.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1, the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks which wider skills the degree builds on mathematics for chemistry, or when a team checks where those skills are taught and assessed. To a student, put it plainly in the second person; to staff, as enabling content the course should include. Ask: 'Which mathematical tool do you rely on most in chemistry, and where does it still trip you up?' Avoid reading the issuer's list aloud or treating every item as a separate module."
- statement: qaa/chemistry-2022/3.8.b4
  forPractitioner: { text: "Build enabling content into the honours course so every graduate can pick and apply methods for analysing and handling data, which may include coding or scripting, to present, communicate and solve problems; it may sit inside the chemistry content (3.7).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you should be able to pick and apply methods for analysing and handling data, which may include coding or scripting, to present, communicate and solve problems.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for honours graduates in chemistry, on data analysis, coding and scripting, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.8, item 4. Do not present it as a regulatory requirement or as a master's outcome. Set it beside the graded row 4.6.b12 and 4.6.b12.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1, the Annex D third-class description qaa/fheq-2024/annex-d/practical/r4/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks which wider skills the degree builds on data analysis, coding and scripting, or when a team checks where those skills are taught and assessed. To a student, put it plainly in the second person; to staff, as enabling content the course should include. Ask: 'Have you written code or a script to handle data, and what did it let you do?' Avoid reading the issuer's list aloud or treating every item as a separate module."
- statement: qaa/chemistry-2022/3.8.b5
  forPractitioner: { text: "Build enabling content into the honours course so every graduate can work well with others in a group, contributing constructively and adaptably to shared outputs; it may sit inside the chemistry content (3.7).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you should be able to work well with others in a group, contributing constructively and adaptably to shared outputs.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for honours graduates in chemistry, on teamwork, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.8, item 5. Do not present it as a regulatory requirement or as a master's outcome. Set it beside the graded row 4.6.b13 and 4.6.b13.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1, the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r2/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks which wider skills the degree builds on teamwork, or when a team checks where those skills are taught and assessed. To a student, put it plainly in the second person; to staff, as enabling content the course should include. Ask: 'What did you bring to the last team task, and how did you adapt when plans changed?' Avoid reading the issuer's list aloud or treating every item as a separate module."
- statement: qaa/chemistry-2022/3.8.b6
  forPractitioner: { text: "Build enabling content into the honours course so every graduate can communicate well, choosing content, medium and method to suit the audience, purpose and topic; it may sit inside the chemistry content (3.7).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you should be able to communicate well, choosing content, medium and method to suit the audience, purpose and topic.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for honours graduates in chemistry, on communication for audience and purpose, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.8, item 6. Do not present it as a regulatory requirement or as a master's outcome. Set it beside the graded row 4.6.b14 and 4.6.b14.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8, the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks which wider skills the degree builds on communication for audience and purpose, or when a team checks where those skills are taught and assessed. To a student, put it plainly in the second person; to staff, as enabling content the course should include. Ask: 'How would you present the same result to a lab group and to a school class?' Avoid reading the issuer's list aloud or treating every item as a separate module."
- statement: qaa/chemistry-2022/3.8.b7
  forPractitioner: { text: "Build enabling content into the honours course so every graduate can tell apart different kinds of published information and understand how peer review shapes the scientific literature; it may sit inside the chemistry content (3.7).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you should be able to tell apart different kinds of published information and understand how peer review shapes the scientific literature.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for honours graduates in chemistry, on kinds of published information and peer review, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.8, item 7. Do not present it as a regulatory requirement or as a master's outcome. Set it beside the graded row 4.6.b7 and 4.6.b7.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5, the Annex D third-class description qaa/fheq-2024/annex-d/cognitive/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks which wider skills the degree builds on kinds of published information and peer review, or when a team checks where those skills are taught and assessed. To a student, put it plainly in the second person; to staff, as enabling content the course should include. Ask: 'What is the difference between a peer-reviewed article, a preprint and a press release?' Avoid reading the issuer's list aloud or treating every item as a separate module."
- statement: qaa/chemistry-2022/3.8.b8
  forPractitioner: { text: "Build enabling content into the honours course so every graduate can understand what their own and others' intellectual property is and is worth, and why academic integrity matters; it may sit inside the chemistry content (3.7).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you should be able to understand what your own and others' intellectual property is and is worth, and why academic integrity matters.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for honours graduates in chemistry, on intellectual property and academic integrity, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.8, item 8. Do not present it as a regulatory requirement or as a master's outcome. Set it beside the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1, the Annex D third-class description qaa/fheq-2024/annex-d/professional/r2/3rd-1st and spine:6."
  author-agent-dialogue: "Raise this when a student asks which wider skills the degree builds on intellectual property and academic integrity, or when a team checks where those skills are taught and assessed. To a student, put it plainly in the second person; to staff, as enabling content the course should include. Ask: 'When would you need to credit someone else's idea in your own work?' Avoid reading the issuer's list aloud or treating every item as a separate module."
- statement: qaa/chemistry-2022/3.8.b9
  forPractitioner: { text: "Build enabling content into the honours course so every graduate can behave professionally, mindful of legal, ethical and social duties, setting an example that reflects well on chemistry and chemists; it may sit inside the chemistry content (3.7).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you should be able to behave professionally, mindful of legal, ethical and social duties, setting an example that reflects well on chemistry and chemists.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for honours graduates in chemistry, on professional, ethical conduct, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.8, item 9. Do not present it as a regulatory requirement or as a master's outcome. Set it beside Table 1's last row, which repeats it without rung cells (Part E), the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.2, the Annex D third-class description qaa/fheq-2024/annex-d/professional/r2/3rd-1st and spine:6."
  author-agent-dialogue: "Raise this when a student asks which wider skills the degree builds on professional, ethical conduct, or when a team checks where those skills are taught and assessed. To a student, put it plainly in the second person; to staff, as enabling content the course should include. Ask: 'Which ethical or legal question have you met in chemistry, and how did you handle it?' Avoid reading the issuer's list aloud or treating every item as a separate module."
- statement: qaa/chemistry-2022/3.9.b1
  forPractitioner: { text: "Building on the honours enabling skills, make sure integrated master's graduates can devise new ways to tackle advanced problems, at times without full information.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your integrated master's you should be able to devise new ways to tackle advanced problems, at times without full information.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for integrated master's graduates in chemistry, on new approaches to advanced problems, at FHEQ level 7 (FQHEIS level 11). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.9, item 1. Do not apply it to the bachelor's degree with honours or present it as regulation. Set it beside the Table 2 outcome 4.7.b1 and 4.7.b1.excellent, the honours skills 3.8.b1 to 3.8.b9, the FHEQ master's descriptor qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise this when an integrated master's student asks how the final year differs from honours, or a team plans master's-level teaching on new approaches to advanced problems. To a student, put it as the extra step beyond honours, in plain words; to staff, as an outcome the master's year should secure. Ask: 'Describe a problem you tackled without all the information: how did you proceed?' Avoid holding a bachelor's student to it."
- statement: qaa/chemistry-2022/3.9.b2
  forPractitioner: { text: "Building on the honours enabling skills, make sure integrated master's graduates can build persuasive arguments and state their position, drawing knowledge and skills together into a convincing case for their ideas.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your integrated master's you should be able to build persuasive arguments and state your position, drawing knowledge and skills together into a convincing case for your ideas.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for integrated master's graduates in chemistry, on persuasive argument, at FHEQ level 7 (FQHEIS level 11). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.9, item 2. Do not apply it to the bachelor's degree with honours or present it as regulation. Set it beside the honours skills 3.8.b1 to 3.8.b9, the FHEQ master's descriptor qaa/fheq-2024/4.17.b4.2 and spine:7."
  author-agent-dialogue: "Raise this when an integrated master's student asks how the final year differs from honours, or a team plans master's-level teaching on persuasive argument. To a student, put it as the extra step beyond honours, in plain words; to staff, as an outcome the master's year should secure. Ask: 'What is the strongest objection to your current research idea, and how would you answer it?' Avoid holding a bachelor's student to it."
- statement: qaa/chemistry-2022/3.9.b3
  forPractitioner: { text: "Building on the honours enabling skills, make sure integrated master's graduates can question and combine varied scientific literature and other information to design methods of investigation and analysis, also beyond their specialism.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your integrated master's you should be able to question and combine varied scientific literature and other information to design methods of investigation and analysis, also beyond your specialism.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for integrated master's graduates in chemistry, on literature to design methods, at FHEQ level 7 (FQHEIS level 11). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.9, item 3. Do not apply it to the bachelor's degree with honours or present it as regulation. Set it beside the Table 2 outcome 4.7.b2 and 4.7.b2.excellent, the honours skills 3.8.b1 to 3.8.b9, the FHEQ master's descriptor qaa/fheq-2024/4.17.b4.1 and spine:7."
  author-agent-dialogue: "Raise this when an integrated master's student asks how the final year differs from honours, or a team plans master's-level teaching on literature to design methods. To a student, put it as the extra step beyond honours, in plain words; to staff, as an outcome the master's year should secure. Ask: 'Which sources outside your specialism shaped the method you are using?' Avoid holding a bachelor's student to it."
- statement: qaa/chemistry-2022/3.9.b4
  forPractitioner: { text: "Building on the honours enabling skills, make sure integrated master's graduates can build general strategies for problems with more than one answer, including finding the extra information needed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your integrated master's you should be able to build general strategies for problems with more than one answer, including finding the extra information needed.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for integrated master's graduates in chemistry, on strategies for problems without a single answer, at FHEQ level 7 (FQHEIS level 11). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.9, item 4. Do not apply it to the bachelor's degree with honours or present it as regulation. Set it beside the honours skills 3.8.b1 to 3.8.b9, the FHEQ master's descriptor qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise this when an integrated master's student asks how the final year differs from honours, or a team plans master's-level teaching on strategies for problems without a single answer. To a student, put it as the extra step beyond honours, in plain words; to staff, as an outcome the master's year should secure. Ask: 'When a problem has several possible answers, how do you decide what information you still need?' Avoid holding a bachelor's student to it."
- statement: qaa/chemistry-2022/3.9.b5
  forPractitioner: { text: "Building on the honours enabling skills, make sure integrated master's graduates can plan and manage their own work and a group's work well.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your integrated master's you should be able to plan and manage your own work and a group's work well.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for integrated master's graduates in chemistry, on planning own and group work, at FHEQ level 7 (FQHEIS level 11). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.9, item 5. Do not apply it to the bachelor's degree with honours or present it as regulation. Set it beside the Table 2 outcome 4.7.b3 and 4.7.b3.excellent, the honours skills 3.8.b1 to 3.8.b9, the FHEQ master's descriptor qaa/fheq-2024/4.17.b8.1 and spine:7."
  author-agent-dialogue: "Raise this when an integrated master's student asks how the final year differs from honours, or a team plans master's-level teaching on planning own and group work. To a student, put it as the extra step beyond honours, in plain words; to staff, as an outcome the master's year should secure. Ask: 'How do you plan your project week by week, and how do you share work in a group?' Avoid holding a bachelor's student to it."
- statement: qaa/chemistry-2022/3.9.b6
  forPractitioner: { text: "Building on the honours enabling skills, make sure integrated master's graduates can show readiness for research, a doctorate or employment at a similar level.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your integrated master's you should be able to show readiness for research, a doctorate or employment at a similar level.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level generic skill for integrated master's graduates in chemistry, on readiness for research or doctoral study, at FHEQ level 7 (FQHEIS level 11). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.9, item 6. Do not apply it to the bachelor's degree with honours or present it as regulation. Set it beside the honours skills 3.8.b1 to 3.8.b9, the FHEQ master's descriptor qaa/fheq-2024/4.17.b7 and spine:7."
  author-agent-dialogue: "Raise this when an integrated master's student asks how the final year differs from honours, or a team plans master's-level teaching on readiness for research or doctoral study. To a student, put it as the extra step beyond honours, in plain words; to staff, as an outcome the master's year should secure. Ask: 'What would you need to show a doctoral supervisor or research employer that you are ready?' Avoid holding a bachelor's student to it."
- statement: qaa/chemistry-2022/3.10
  forPractitioner: { text: "Give every honours student an open-ended investigative project, usually in the final year; at master's level expect originality, and judge the report's quality against that of a peer-reviewed paper.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You will undertake an open-ended investigation of your own, usually in your final year. At master's level, your project should show some original thinking, and your written report should be as good as a published, peer-reviewed paper in quality, though not in format.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation that every honours student undertakes independent investigative work, with a should-level standard for the master's report equal in quality to a peer-reviewed publication. It holds for honours (FHEQ level 6) and master's (FHEQ level 7). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.10. Do not claim the format of a paper is required, and record the obliging words outside the five ('expected to') as written; set it beside 4.6.b8, 4.7.b5 and 3.13 in this document and the FHEQ descriptors qaa/fheq-2024/4.15.b6 and 4.17.b3."
  author-agent-dialogue: "Raise this when a student plans a final-year or master's project, or a team sets project assessment. To a student, explain that the project is the place to investigate on your own, and that at master's level the report is judged as if for publication. Ask: 'What open question will your project try to answer, and what would make the answer new?' Avoid suggesting that an honours project needs originality."
- statement: qaa/chemistry-2022/3.15
  forPractitioner: { text: "Tell students how and why you teach as you do, review methods internally and externally, and design them to support the outcomes and to be inclusive and accessible.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must-level duty to make teaching methods explicit to students and subject them to regular review, with a should on alignment and inclusion. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.15. Do not claim it prescribes any method; set it beside 2.7, 3.16 and 3.20 in this document."
  author-agent-dialogue: "Raise this when a team writes a module handbook or plans a review of teaching. Frame it for staff as a duty to explain and review methods. Ask: 'Could a student in your module say why it is taught the way it is?' Avoid presenting it to students as their task."
- statement: qaa/chemistry-2022/3.20
  forPractitioner: { text: "Keep teaching responsive to new technology and pedagogic research, and give every member of teaching staff, demonstrators and visiting lecturers included, access to subject and educational development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on providers: responsive strategies and professional development for all who teach or assess. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.20. Do not present it as a student outcome; where staff development is the subject, set it beside std:doc:advancehe-psf-dimensions-2023-framework and 3.15 in this document."
  author-agent-dialogue: "Raise this when a team plans staff development or reviews how demonstrators are trained. Frame it for staff as access for everyone who teaches, not only academics. Ask: 'What development have your technical demonstrators had in the past year?' Avoid presenting it to students."
- statement: qaa/chemistry-2022/3.21
  forPractitioner: { text: "Align assessment with the outcomes and vary it enough to cover the knowledge, abilities and professional skills the course develops.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that the diversity of assessment reflects the outcomes and skills a course develops. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.21. Do not present it as a student outcome; set it beside 3.22 to 3.24 in this document."
  author-agent-dialogue: "Raise this when a team reviews its assessment pattern. Frame it for staff as a check that variety matches the range of outcomes. Ask: 'Which of your outcomes is assessed only by examination, and would another format test it better?' Avoid presenting it to students."
- statement: qaa/chemistry-2022/3.22
  forPractitioner: { text: "Give students opportunities to build IT literacy and coding, and use a wide range of assessment formats, digital and handwritten, so every student can show what they have learned.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that students get opportunities to develop IT literacy and coding, with a strong encouragement towards varied assessment formats. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.22. Do not claim coding is a required outcome; set it beside 3.8.b4, 4.6.b12 and 3.21 in this document."
  author-agent-dialogue: "Raise this when a team plans where coding sits in the course or reviews assessment formats. Frame it for staff as opportunity and variety. Ask: 'Where in your course does a student first write code, and is it assessed?' Avoid presenting it to students as a duty."
- statement: qaa/chemistry-2022/3.24
  forPractitioner: { text: "Use assessment to build both chemistry-specific and wider employability skills; the skills map shows which assessment types exercise which skills.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that assessment supports both career-specific and wider skills, with an illustrative skills map. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 3.24. Do not present the map as a required pattern; set it beside 3.23, 1.13 and 3.6 in this document."
  author-agent-dialogue: "Raise this when a team audits which skills its assessments exercise. Frame it for staff as using the map as a prompt. Ask: 'Which of the mapped skills, such as teamwork, does none of your assessments require?' Avoid presenting it to students."
- statement: qaa/chemistry-2022/4.2
  forPractitioner: { text: "When deciding what evidence shows achievement above threshold, use Annex D's descriptions of first, upper second, lower second and third.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level pointer for providers to Annex D when judging achievement above threshold in the honours degree (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 4.2. Do not claim the statement sets its own class bands; set it beside 4.3, the rungs 4.6.b1 to 4.6.b14 and their excellent forms, and qaa/fheq-2024/annex-d (SL6 of std:doc:qaa-fheq-2024-framework)."
  author-agent-dialogue: "Raise this when a team aligns its marking with degree classes. Frame it for staff as Annex D filling the space between the two rungs. Ask: 'How do your criteria for a 2:1 differ from those for a first, and do they draw on Annex D?' Avoid presenting it to a student as their duty."
- statement: qaa/chemistry-2022/4.6
  forPractitioner: { text: "Read Tables 1 and 2 with the context, content and enabling skills of sections 1 and 3 and the framing of 4.1 to 4.5, not as standalone lists.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider or course team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level instruction on how to read Tables 1 and 2. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 4.6. Do not quote a table row without its context; set it beside 4.4 (no checklist, no weighting) and the outcome lists 3.3 and 3.8 in this document."
  author-agent-dialogue: "Raise this when a team or examiner lifts a table row out of context. Frame it for staff as reading the tables with sections 1 and 3. Ask: 'Which paragraph of section 3 explains the row you are using?' Avoid presenting it to students."
- statement: qaa/chemistry-2022/4.6.b1
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least remember the basic knowledge and theory taught on the course and draw on it, with the right terms, to discuss or explain familiar ideas; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can remember the basic knowledge and theory taught on the course and draw on it, with the right terms, to discuss or explain familiar ideas.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on core chemical concepts (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 1, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b1.excellent, the related outcome 3.3.b1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the Annex D third-class description qaa/fheq-2024/annex-d/knowledge/r1/3rd (strand:knowledge, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on core chemical concepts, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'Could you explain a familiar idea from your course, such as a reaction type, using the correct terms?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b1.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can apply deep knowledge of chemical concepts and theory to discuss and predict outcomes across most core parts of the course, and show enquiry that goes further; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would apply deep knowledge of chemical concepts and theory to discuss and predict outcomes across most core parts of the course, and show enquiry that goes further.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on core chemical concepts: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 1, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the Annex D first-class description qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on core chemical concepts and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'Can you predict what would happen in a case the course did not cover, and justify it?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.6.b2
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least set out and work through routine problems adequately, using a variety of the methods and ideas taught; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can set out and work through routine problems adequately, using a variety of the methods and ideas taught.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on solving chemical problems (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 2, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b2.excellent, the related outcome 3.3.b4, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D third-class description qaa/fheq-2024/annex-d/cognitive/r3/3rd (strand:thinking, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on solving chemical problems, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'Take a routine problem from your course: can you state it clearly and solve it without a worked example?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b2.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can devise and judge solutions to problems, familiar or new, drawing on several methods; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would devise and judge solutions to problems, familiar or new, drawing on several methods.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on solving chemical problems: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 2, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D first-class description qaa/fheq-2024/annex-d/cognitive/r3/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on solving chemical problems and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'Faced with a problem unlike any you have practised, how would you choose and test an approach?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.6.b3
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least write and work to risk assessments so practical work is done safely and reliably, leaning heavily on guidance; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can write and work to risk assessments so practical work is done safely and reliably, leaning heavily on guidance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on safe practice and risk assessment (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 3, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b3.excellent, the related outcome 3.3.b2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the Annex D third-class description qaa/fheq-2024/annex-d/practical/r2/3rd (strand:application, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on safe practice and risk assessment, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'When did you last write a risk assessment, and what guidance did you need?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b3.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can write and work to risk assessments so practical work is done safely and reliably, with little need for guidance; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would write and work to risk assessments so practical work is done safely and reliably, with little need for guidance.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on safe practice and risk assessment: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 3, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b3, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the Annex D first-class description qaa/fheq-2024/annex-d/practical/r2/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on safe practice and risk assessment and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'Could you assess the hazards of a new procedure on your own and justify your controls?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.6.b4
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least propose and try out accurate approaches to making, purifying, isolating and characterising compounds with some independence, and give reasons for the techniques chosen; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can propose and try out accurate approaches to making, purifying, isolating and characterising compounds with some independence, and give reasons for the techniques chosen.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on synthesis, purification and characterisation (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 4, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b4.excellent, the related outcome 3.3.b6, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the Annex D third-class description qaa/fheq-2024/annex-d/practical/r1/3rd (strand:application, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on synthesis, purification and characterisation, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'For a compound you made recently, why did you choose that purification method?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b4.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can design, assess and carry through accurate approaches to making, purifying, isolating and characterising compounds, working efficiently and largely on their own; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would design, assess and carry through accurate approaches to making, purifying, isolating and characterising compounds, working efficiently and largely on your own.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on synthesis, purification and characterisation: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 4, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b4, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the Annex D first-class description qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on synthesis, purification and characterisation and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'Could you plan a full route from synthesis to characterisation for a new target and defend each step?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.6.b5
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least propose, perform and write up accurate sample preparation, measurement and analysis, qualitative and quantitative, with some independence; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can propose, perform and write up accurate sample preparation, measurement and analysis, qualitative and quantitative, with some independence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on chemical measurement and analysis (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 5, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b5.excellent, the related outcome 3.3.b9, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the Annex D third-class description qaa/fheq-2024/annex-d/practical/r4/3rd (strand:application, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on chemical measurement and analysis, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'Which analytical method have you run from preparation to report, and how confident are you in its accuracy?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b5.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can design, refine, perform and write up accurate sample preparation, measurement and analysis, efficiently and with a high level of autonomy; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would design, refine, perform and write up accurate sample preparation, measurement and analysis, efficiently and with a high level of autonomy.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on chemical measurement and analysis: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 5, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the Annex D first-class description qaa/fheq-2024/annex-d/practical/r4/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on chemical measurement and analysis and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'How would you improve the precision of a measurement you have made, and how would you show it?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.6.b6
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least use computational methods and software to explore familiar chemical ideas from the course, reporting what is found in the right terms; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can use computational methods and software to explore familiar chemical ideas from the course, reporting what is found in the right terms.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on computational chemistry (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 6, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b6.excellent, the related outcome 3.3.b11, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the Annex D third-class description qaa/fheq-2024/annex-d/practical/r1/3rd (strand:application, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on computational chemistry, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'Which computational tool have you used to look at a structure or reaction, and what did it show you?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b6.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can choose and use suitable computational methods and software to explore complex chemical ideas, judging and reporting the results in the right terms; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would choose and use suitable computational methods and software to explore complex chemical ideas, judging and reporting the results in the right terms.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on computational chemistry: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 6, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b6, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the Annex D first-class description qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on computational chemistry and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'How would you decide which computational method suits a complex system, and how would you check the result?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.6.b7
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least track down and choose fitting sources of chemical information; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can track down and choose fitting sources of chemical information.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on using the chemical literature (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 7, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b7.excellent, the related outcome 3.8.b2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and the Annex D third-class description qaa/fheq-2024/annex-d/cognitive/r1/3rd (strand:application, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on using the chemical literature, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'Where would you look first for reliable data on a compound, and why there?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b7.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can track down and choose fitting sources of chemical information, largely unaided; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would track down and choose fitting sources of chemical information, largely unaided.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on using the chemical literature: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 7, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b7, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and the Annex D first-class description qaa/fheq-2024/annex-d/cognitive/r1/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on using the chemical literature and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'How do you find what has been published on a topic you have not studied before?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.6.b8
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least carry an open-ended investigation or research-based assignment through to completion; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can carry an open-ended investigation or research-based assignment through to completion.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on the independent project (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 8, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b8.excellent, the related outcome 3.10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r3/3rd (strand:autonomy, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on the independent project, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'What stage of your project needs the most help from your supervisor?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b8.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can carry an open-ended investigation or research-based assignment through to completion, working very independently; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would carry an open-ended investigation or research-based assignment through to completion, working very independently.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on the independent project: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 8, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b8, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and the Annex D first-class description qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on the independent project and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'Which decisions in your project did you take on your own, and how did you justify them?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.6.b9
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least name and discuss how chemistry is applied to present and future problems facing the world; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can name and discuss how chemistry is applied to present and future problems facing the world.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on chemistry and global challenges (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 9, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b9.excellent, the related outcome 3.3.b13, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and the Annex D third-class description qaa/fheq-2024/annex-d/cognitive/r2/3rd (strand:thinking, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on chemistry and global challenges, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'Which global problem do you know chemistry is helping with, and how?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b9.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can explain how chemistry can help with present and future world problems and propose ways it might do so; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would explain how chemistry can help with present and future world problems and propose ways it might do so.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on chemistry and global challenges: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 9, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b9, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and the Annex D first-class description qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on chemistry and global challenges and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'Could you propose a way chemistry might help with a challenge such as clean energy, and weigh its limits?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.6.b10
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least point out and explain links between chemistry and other subjects met on the course; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can point out and explain links between chemistry and other subjects met on the course.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on chemistry and other subjects (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 10, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b10.excellent, the related outcome 3.3.b14, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the Annex D third-class description qaa/fheq-2024/annex-d/knowledge/r2/3rd (strand:knowledge, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on chemistry and other subjects, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'Where has your chemistry met another subject, such as biology or physics, on your course?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b10.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can assess and explain what chemistry brings to issues that cross several disciplines; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would assess and explain what chemistry brings to issues that cross several disciplines.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on chemistry and other subjects: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 10, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the Annex D first-class description qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on chemistry and other subjects and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'For a problem that crosses disciplines, what does chemistry add that the others cannot?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.6.b11
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least pick and apply mathematical ideas and tools to familiar chemistry problems and to judging data, accurately most of the time; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can pick and apply mathematical ideas and tools to familiar chemistry problems and to judging data, accurately most of the time.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on mathematics in chemistry (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 11, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b11.excellent, the related outcome 3.8.b3, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r1/3rd (strand:application, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on mathematics in chemistry, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'Which calculation in your course do you still find hardest to get right?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b11.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can pick and apply mathematical ideas and tools to familiar chemistry problems and to judging data, with consistent accuracy; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would pick and apply mathematical ideas and tools to familiar chemistry problems and to judging data, with consistent accuracy.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on mathematics in chemistry: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 11, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b11, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D first-class description qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on mathematics in chemistry and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'How do you check that your data analysis is correct before you rely on it?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.6.b12
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least choose and apply data-handling and analysis methods correctly, with some guidance; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can choose and apply data-handling and analysis methods correctly, with some guidance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on data analysis methods (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 12, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b12.excellent, the related outcome 3.8.b4, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D third-class description qaa/fheq-2024/annex-d/practical/r4/3rd (strand:thinking, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on data analysis methods, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'Which data analysis method do you use most, and when do you still need help with it?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b12.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can choose, assess and apply data-handling and analysis methods correctly in complex, unpredictable situations; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would choose, assess and apply data-handling and analysis methods correctly in complex, unpredictable situations.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on data analysis methods: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 12, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b12, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D first-class description qaa/fheq-2024/annex-d/practical/r4/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on data analysis methods and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'When data are messy or incomplete, how do you decide which method to trust?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.6.b13
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least make useful contributions to what a team produces; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can make useful contributions to what a team produces.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on teamwork (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 13, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b13.excellent, the related outcome 3.8.b5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r2/3rd (strand:autonomy, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on teamwork, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'What did you contribute to the last group task, and how did the team use it?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b13.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can make clear, valuable contributions to what a team produces, showing teamwork, leadership or both; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would make clear, valuable contributions to what a team produces, showing teamwork, leadership or both.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on teamwork: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 13, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b13, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D first-class description qaa/fheq-2024/annex-d/transferable/r2/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on teamwork and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'When have you helped a team work better, or led part of it?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.6.b14
  forPractitioner: { text: "Threshold: make sure every honours graduate can at least get information, ideas, problems and solutions across clearly in speech, in writing and electronically; teaching and assessment need to evidence this floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, by the end of your honours degree you can get information, ideas, problems and solutions across clearly in speech, in writing and electronically.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard, the least every honours graduate in chemistry shows on communication (FHEQ level 6; FQHEIS level 10). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 14, threshold column. Do not present it as regulation, a mark scheme or the master's standard. Set it beside its excellent form 4.6.b14.excellent, the related outcome 3.8.b6, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r1/3rd (strand:communication, spine:6)."
  author-agent-dialogue: "Raise this when a student asks what they must at least manage on communication, or when a team checks a module against the floor. To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. Ask: 'Who was the audience for your last presentation, and how did you adapt it for them?' Do not read the table aloud, and never offer the excellent column as the pass standard."
- statement: qaa/chemistry-2022/4.6.b14.excellent
  forPractitioner: { text: "Excellent: for first-class work, look for evidence that the student can get information, ideas, problems and solutions across to a high standard in speech, writing and electronic forms, accurately, fluently and with sophistication, always pitched to the audience; set tasks that leave room to show it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent, first-class work, you would get information, ideas, problems and solutions across to a high standard in speech, writing and electronic forms, accurately, fluently and with sophistication, always pitched to the audience.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard on communication: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 1, row 14, excellent column. Do not present it as the minimum or as a master's standard. Set it beside its threshold form 4.6.b14, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and the Annex D first-class description qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise this with a student who meets the minimum on communication and asks how to reach the top band, or with a team designing stretch tasks. Present it as a step above the threshold, in plain words to a student and as a design aim to staff. Ask: 'Could you explain the same result to a specialist and to a member of the public?' Avoid implying that every student has to reach it."
- statement: qaa/chemistry-2022/4.7
  forPractitioner: { text: "Check that master's students hold the Table 1 thresholds, then build specialist mastery, transferable skills and independence in projects on top.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "On a master's course you should already meet the minimum honours outcomes; the course then deepens your knowledge in a specialism and makes you more independent in project work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that every master's student in chemistry, integrated or standalone, has attained the Table 1 thresholds, with Table 2 adding master's outcomes (FHEQ level 7; FQHEIS level 11). Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, para 4.7. Do not claim it makes Table 1's excellent column the master's standard; set it beside 4.6.b1 to 4.6.b14, 4.7.b1 to 4.7.b5 in this document, the FHEQ master's descriptor qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise this when a master's applicant or student asks what they are expected to know already, or a team admits students to a standalone MSc. To a student, explain that the honours minimum is the starting point; to staff, frame it as an entry check. Ask: 'Which Table 1 outcome do you feel least secure in, and how will you close that gap?' Avoid treating the excellent column as an entry requirement."
- statement: qaa/chemistry-2022/4.7.b1
  forPractitioner: { text: "Threshold: every master's graduate can build up, combine and apply a broad, systematic grasp of current chemical concepts to harder problems, though with a good deal of support and guidance from staff.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum on a master's course you can build up, combine and apply a broad, systematic grasp of current chemical concepts to harder problems, with plenty of support and guidance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a master's threshold standard on applying advanced understanding to complex problems: reached with considerable support (FHEQ level 7; FQHEIS level 11), in addition to the honours thresholds. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 2, row 1, threshold column. Do not apply it to the honours degree or use Annex D for it, since Annex D covers honours classes only. Set it beside its excellent form 4.7.b1.excellent, the related outcome 3.9.b1, the FHEQ master's descriptor qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise this when a master's student asks what the minimum is on applying advanced understanding to complex problems, or a team sets master's assessment. To a student, say that support and guidance are expected at the minimum; to staff, frame it as the floor for the award. Ask: 'Which complex problem have you tackled by combining ideas from different areas of chemistry?' Do not present the excellent column's independence as the minimum."
- statement: qaa/chemistry-2022/4.7.b1.excellent
  forPractitioner: { text: "Excellent: look for master's students who can build up, combine and apply a broad, systematic grasp of current chemical concepts to harder problems on their own initiative, needing little direction.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent work on a master's course, you would build up, combine and apply a broad, systematic grasp of current chemical concepts to harder problems largely on your own initiative.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard for master's graduates on applying advanced understanding to complex problems: the same outcome reached with a high degree of independence (FHEQ level 7), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 2, row 1, excellent column. Do not present it as the minimum or as a doctoral standard. Set it beside its threshold form 4.7.b1, the FHEQ master's descriptor qaa/fheq-2024/4.17.b6 on self-direction and spine:7."
  author-agent-dialogue: "Raise this with a master's student aiming high on applying advanced understanding to complex problems, or a team designing work that rewards independence. Put it as doing the same work with little direction, in plain words to a student and as a design aim to staff. Ask: 'Which parts of this could you now do without asking your supervisor?' Avoid implying that needing guidance means failing."
- statement: qaa/chemistry-2022/4.7.b2
  forPractitioner: { text: "Threshold: every master's graduate can question and combine varied scientific literature and other information to design methods of investigation, at the forefront and beyond their specialism, though with a good deal of support and guidance from staff.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum on a master's course you can question and combine varied scientific literature and other information to design methods of investigation, at the forefront and beyond your specialism, with plenty of support and guidance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a master's threshold standard on using the literature to design methods: reached with considerable support (FHEQ level 7; FQHEIS level 11), in addition to the honours thresholds. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 2, row 2, threshold column. Do not apply it to the honours degree or use Annex D for it, since Annex D covers honours classes only. Set it beside its excellent form 4.7.b2.excellent, the related outcome 3.9.b3, the FHEQ master's descriptor qaa/fheq-2024/4.17.b4.1 and spine:7."
  author-agent-dialogue: "Raise this when a master's student asks what the minimum is on using the literature to design methods, or a team sets master's assessment. To a student, say that support and guidance are expected at the minimum; to staff, frame it as the floor for the award. Ask: 'Which recent papers shaped the method you are using, and what did you take from each?' Do not present the excellent column's independence as the minimum."
- statement: qaa/chemistry-2022/4.7.b2.excellent
  forPractitioner: { text: "Excellent: look for master's students who can question and combine varied scientific literature and other information to design methods of investigation, at the forefront and beyond their specialism on their own initiative, needing little direction.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent work on a master's course, you would question and combine varied scientific literature and other information to design methods of investigation, at the forefront and beyond your specialism largely on your own initiative.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard for master's graduates on using the literature to design methods: the same outcome reached with a high degree of independence (FHEQ level 7), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 2, row 2, excellent column. Do not present it as the minimum or as a doctoral standard. Set it beside its threshold form 4.7.b2, the FHEQ master's descriptor qaa/fheq-2024/4.17.b6 on self-direction and spine:7."
  author-agent-dialogue: "Raise this with a master's student aiming high on using the literature to design methods, or a team designing work that rewards independence. Put it as doing the same work with little direction, in plain words to a student and as a design aim to staff. Ask: 'Which parts of this could you now do without asking your supervisor?' Avoid implying that needing guidance means failing."
- statement: qaa/chemistry-2022/4.7.b3
  forPractitioner: { text: "Threshold: every master's graduate can plan a project, weighing ethics, hazards, environmental effects and costs where relevant, though with a good deal of support and guidance from staff.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum on a master's course you can plan a project, weighing ethics, hazards, environmental effects and costs where relevant, with plenty of support and guidance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a master's threshold standard on project planning: reached with considerable support (FHEQ level 7; FQHEIS level 11), in addition to the honours thresholds. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 2, row 3, threshold column. Do not apply it to the honours degree or use Annex D for it, since Annex D covers honours classes only. Set it beside its excellent form 4.7.b3.excellent, the related outcome 3.9.b5, the FHEQ master's descriptor qaa/fheq-2024/4.17.b6 and spine:7."
  author-agent-dialogue: "Raise this when a master's student asks what the minimum is on project planning, or a team sets master's assessment. To a student, say that support and guidance are expected at the minimum; to staff, frame it as the floor for the award. Ask: 'What ethical, safety, environmental and cost questions did you weigh in planning your project?' Do not present the excellent column's independence as the minimum."
- statement: qaa/chemistry-2022/4.7.b3.excellent
  forPractitioner: { text: "Excellent: look for master's students who can plan a project, weighing ethics, hazards, environmental effects and costs where relevant on their own initiative, needing little direction.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent work on a master's course, you would plan a project, weighing ethics, hazards, environmental effects and costs where relevant largely on your own initiative.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard for master's graduates on project planning: the same outcome reached with a high degree of independence (FHEQ level 7), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 2, row 3, excellent column. Do not present it as the minimum or as a doctoral standard. Set it beside its threshold form 4.7.b3, the FHEQ master's descriptor qaa/fheq-2024/4.17.b6 on self-direction and spine:7."
  author-agent-dialogue: "Raise this with a master's student aiming high on project planning, or a team designing work that rewards independence. Put it as doing the same work with little direction, in plain words to a student and as a design aim to staff. Ask: 'Which parts of this could you now do without asking your supervisor?' Avoid implying that needing guidance means failing."
- statement: qaa/chemistry-2022/4.7.b4
  forPractitioner: { text: "Threshold: every master's graduate can develop the advanced practical and investigative skills a project calls for, though with a good deal of support and guidance from staff.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum on a master's course you can develop the advanced practical and investigative skills a project calls for, with plenty of support and guidance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a master's threshold standard on advanced experimental skills: reached with considerable support (FHEQ level 7; FQHEIS level 11), in addition to the honours thresholds. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 2, row 4, threshold column. Do not apply it to the honours degree or use Annex D for it, since Annex D covers honours classes only. Set it beside its excellent form 4.7.b4.excellent, the related outcome 3.13, the FHEQ master's descriptor qaa/fheq-2024/4.17.b2 and spine:7."
  author-agent-dialogue: "Raise this when a master's student asks what the minimum is on advanced experimental skills, or a team sets master's assessment. To a student, say that support and guidance are expected at the minimum; to staff, frame it as the floor for the award. Ask: 'Which advanced technique did your project need, and how did you learn it?' Do not present the excellent column's independence as the minimum."
- statement: qaa/chemistry-2022/4.7.b4.excellent
  forPractitioner: { text: "Excellent: look for master's students who can develop the advanced practical and investigative skills a project calls for on their own initiative, needing little direction.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent work on a master's course, you would develop the advanced practical and investigative skills a project calls for largely on your own initiative.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard for master's graduates on advanced experimental skills: the same outcome reached with a high degree of independence (FHEQ level 7), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 2, row 4, excellent column. Do not present it as the minimum or as a doctoral standard. Set it beside its threshold form 4.7.b4, the FHEQ master's descriptor qaa/fheq-2024/4.17.b6 on self-direction and spine:7."
  author-agent-dialogue: "Raise this with a master's student aiming high on advanced experimental skills, or a team designing work that rewards independence. Put it as doing the same work with little direction, in plain words to a student and as a design aim to staff. Ask: 'Which parts of this could you now do without asking your supervisor?' Avoid implying that needing guidance means failing."
- statement: qaa/chemistry-2022/4.7.b5
  forPractitioner: { text: "Threshold: every master's graduate can discuss the background, context, methods, results and likely impact of a substantial research project, though with a good deal of support and guidance from staff.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum on a master's course you can discuss the background, context, methods, results and likely impact of a substantial research project, with plenty of support and guidance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a master's threshold standard on discussing a research project: reached with considerable support (FHEQ level 7; FQHEIS level 11), in addition to the honours thresholds. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 2, row 5, threshold column. Do not apply it to the honours degree or use Annex D for it, since Annex D covers honours classes only. Set it beside its excellent form 4.7.b5.excellent, the related outcome 3.10, the FHEQ master's descriptor qaa/fheq-2024/4.17.b3 and spine:7."
  author-agent-dialogue: "Raise this when a master's student asks what the minimum is on discussing a research project, or a team sets master's assessment. To a student, say that support and guidance are expected at the minimum; to staff, frame it as the floor for the award. Ask: 'How would you explain why your project's results matter, and to whom?' Do not present the excellent column's independence as the minimum."
- statement: qaa/chemistry-2022/4.7.b5.excellent
  forPractitioner: { text: "Excellent: look for master's students who can discuss the background, context, methods, results and likely impact of a substantial research project on their own initiative, needing little direction.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For excellent work on a master's course, you would discuss the background, context, methods, results and likely impact of a substantial research project largely on your own initiative.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent standard for master's graduates on discussing a research project: the same outcome reached with a high degree of independence (FHEQ level 7), not a requirement for the award. Cite it as QAA, 2022, Chemistry Subject Benchmark Statement, Table 2, row 5, excellent column. Do not present it as the minimum or as a doctoral standard. Set it beside its threshold form 4.7.b5, the FHEQ master's descriptor qaa/fheq-2024/4.17.b6 on self-direction and spine:7."
  author-agent-dialogue: "Raise this with a master's student aiming high on discussing a research project, or a team designing work that rewards independence. Put it as doing the same work with little direction, in plain words to a student and as a design aim to staff. Ask: 'Which parts of this could you now do without asking your supervisor?' Avoid implying that needing guidance means failing."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.3; 4.2" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.3; 4.2" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.3 (integrated master's); Table 2 and 4.7 (level inferred for standalone master's)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.3 (integrated master's)" }
  - { id: "spine:6", role: "refers", locator: "std:ref:uk-framework R2 and R8 (inferred: Part E)" }
  - { id: "spine:7", role: "refers", locator: "std:ref:uk-framework R2 and R8 (inferred: Part E)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.3: \"FHEQ Level 6; FQHEIS Level 10\"; 4.2, the title of Annex D)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.3: integrated master's, \"FHEQ Level 7; FQHEIS Level 11\")" }
  - { from: "fheq:6", to: "spine:6", relation: "sameStep", basis: "inferred from std:ref:uk-framework R2 (Part E)" }
  - { from: "fheq:7", to: "spine:7", relation: "sameStep", basis: "inferred from std:ref:uk-framework R2 (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.2", "1.10", "1.11", "2.7", "2.10", "3.5", "3.15", "3.22"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["2.7", "2.8", "2.13", "2.19", "3.15", "3.16"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.1", "1.3", "1.12", "1.15", "3.3", "3.4", "3.13", "4.7"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.13", "1.14", "1.15", "3.5", "3.6", "3.24"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-chemistry-2019-benchmarks (not yet ingested)", note: "the fourth edition (2019), named in the advisory group list; key changes listed in the front matter" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree classification descriptions for honours (4.2); cited as the 2019 Annex D in the reference list, now in the 2024 Frameworks" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "Education for Sustainable Development guidance (1.12)" }
- { rel: "refersTo", target: "std:doc:qaa-enterprise-2018-guidance", note: "Enterprise and Entrepreneurship Education guidance (1.15)" }
- { rel: "refersTo", target: "QAA (2019) Characteristics Statement: Higher Education in Apprenticeships (not yet ingested)", note: "2.6" }
- { rel: "refersTo", target: "United Nations, Sustainable Development Goals", note: "1.12" }
- { rel: "refersTo", target: "Royal Society of Chemistry accreditation criteria for Chartered Chemist (not yet ingested)", note: "2.20" }
- { rel: "refersTo", target: "HEA (2016) Framework for embedding employability in higher education (not yet ingested)", note: "reference list only" }
- { rel: "refersTo", target: "QAA Quality Code Advice and Guidance; QAA Glossary (not ingested)", note: "front matter" }
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
- Chemistry is the central science, describing, explaining and changing the material world, with large effects on society and a key part in sustainable development and global challenges (D1, 1.1).
- A very broad discipline, organised in many ways: the traditional inorganic, organic, physical and analytical branches; synthesis, measurement and application; or applied fields such as biological, computational, environmental, materials or medicinal chemistry (D1, 1.7; 2.1).
- Hands-on practical work is essential, built up in a spiral from scripted experiments to independent, precise work by the final year (D1, 1.8).
- Theory is underpinned by mathematical, spatial, information, planning, communication and problem-solving skills; the subject has a strong visual and practical side (D1, 1.9; 3.16).
- An inherently creative, multidisciplinary subject whose graduates combine subject expertise with wider attributes valued by employers in and beyond science (D1, 1.3; 3.5).
- Two undergraduate routes, the bachelor's with honours and the integrated master's (MChem, MSci), plus standalone MSc and MRes courses; accreditation by the Royal Society of Chemistry towards Chartered Chemist (D1, 2.3; 2.20).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "relevant, representative material; an inclusive account of the history and uses of chemistry crediting diverse chemists; learner choice of topics tied to their lives; progression that lets all reach their potential (D1, 1.2; 1.10; 1.11; 2.10; 3.5)"
  statements: ["qaa/chemistry-2022/1.2", "qaa/chemistry-2022/1.11", "qaa/chemistry-2022/2.10.b2"]
- theme: theme:accessibility
  inThisSubject: "inclusive design and reasonable adjustment for learning, assessment and practical work, support for verbal, spatial and numerical skills, recorded and simulcast sessions (D1, 2.7; 2.8; 2.13; 3.15; 3.16)"
  statements: ["qaa/chemistry-2022/2.7", "qaa/chemistry-2022/2.8", "qaa/chemistry-2022/2.13", "qaa/chemistry-2022/3.15"]
- theme: theme:esd
  inThisSubject: "chemistry as a toolkit for the SDGs, from health to clean energy and water; waste reduction and safe disposal; green and sustainable chemistry as a specialism; environmental effects weighed in project planning (D1, 1.1; 1.12; 3.3; 3.4; 3.13; Table 2)"
  statements: ["qaa/chemistry-2022/1.12", "qaa/chemistry-2022/3.3.b3", "qaa/chemistry-2022/3.4.b2", "qaa/chemistry-2022/4.7.b3", "qaa/chemistry-2022/4.7.b3.excellent"]
- theme: theme:enterprise
  inThisSubject: "employability through subject and wider skills, enterprise as creativity and problem-solving central to chemistry, enterprise education topics such as business plans and intellectual property, assessment that builds employability (D1, 1.13 to 1.15; 3.5; 3.6; 3.24)"
  statements: ["qaa/chemistry-2022/1.13", "qaa/chemistry-2022/3.6", "qaa/chemistry-2022/3.24", "qaa/chemistry-2022/3.8.b8"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.3", gloss: "core content: concepts, safe practice and waste, physical chemistry, synthesis and reactivity, purification, periodic trends, orbitals, measurement and analysis, computation, substances and materials, chemistry in innovation and with other subjects" }
  - { component: "3.4", gloss: "optional content: culture and history of chemistry, specialist branches, chemistry within other subjects and vocations" }
  - { component: "3.13", gloss: "project training: advanced experimental skills, literature, planning, communication, the research community, impact" }
practices:
  - { component: "3.10", kind: "learning", gloss: "an independent open-ended project, usually in the final year; originality at master's" }
  - { component: "3.15", kind: "teaching", gloss: "methods left open, explained to students, reviewed, inclusive and accessible" }
  - { component: "3.16", kind: "teaching", gloss: "student-centred, visual and practical; remote, face-to-face and recorded sessions; pre-sessional work" }
  - { component: "3.17", kind: "teaching", gloss: "synchronous: lectures, problem classes, labs, computer workshops, case studies, peer learning, presentations, fieldwork" }
  - { component: "3.18", kind: "learning", gloss: "asynchronous: texts, digital media, recordings, simulations, virtual experiments, practice tests, pre-lab exercises" }
  - { component: "3.19", kind: "learning", gloss: "blended: team projects, placements, reflective portfolios, research projects" }
  - { component: "3.20", kind: "teaching", gloss: "responsive strategies and development for all teaching staff" }
  - { component: "3.21", kind: "assessment", gloss: "assessment aligned with outcomes and varied" }
  - { component: "3.22", kind: "assessment", gloss: "IT literacy and coding; digital and handwritten formats" }
  - { component: "3.23", kind: "assessment", gloss: "sixteen kinds of evidence, from invigilated exams to practical skills assessed on yield and precision" }
  - { component: "3.24", kind: "assessment", gloss: "assessment building subject and employability skills, with a skills-by-assessment map" }
  - { component: "3.25", kind: "assessment", gloss: "master's: unfamiliar problems and the full range of research skills" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.6", award: "bachelor's with honours", items: 14 }
  - { rung: "excellent", leadIn: "4.6", award: "bachelor's with honours", items: 14 }
  - { rung: "threshold", leadIn: "4.7", award: "master's", items: 5 }
  - { rung: "excellent", leadIn: "4.7", award: "master's", items: 5 }
rungBases: "4.3 defines two rungs, threshold (the minimum for an honours degree) and excellent (the level for a first); no typical rung, Annex D covering the classes between (4.2). Table 1, after 4.6 (caption: on graduating with honours, graduates should be able to), gives 15 benchmark standards, 14 with a threshold cell and an excellent cell of their own text, recorded on their own spans; the first column names the outcome. Table 2, in 4.7, adds five master's outcomes with one threshold cell (significant support and guidance) and one excellent cell (high independence and autonomy), read as applying to all five; each outcome is recorded at both rungs on its span."
outcomeLists:
  - { leadIn: "3.3", gloss: "core chemistry content for all undergraduates", items: 14, award: ["bachelor's with honours", "master's"] }
  - { leadIn: "3.4", gloss: "optional specialist and supplementary content (may)", items: 3, award: ["bachelor's with honours", "master's"] }
  - { leadIn: "3.8", gloss: "enabling content for honours graduates", items: 9, award: ["bachelor's with honours"] }
  - { leadIn: "3.9", gloss: "further skills for integrated master's graduates", items: 6, award: ["master's"] }
outcomes:
  - { outcome: "core chemical concepts", threshold: "qaa/chemistry-2022/4.6.b1", typical: "none", excellent: "qaa/chemistry-2022/4.6.b1.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "solving chemical problems", threshold: "qaa/chemistry-2022/4.6.b2", typical: "none", excellent: "qaa/chemistry-2022/4.6.b2.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "safe practice and risk assessment", threshold: "qaa/chemistry-2022/4.6.b3", typical: "none", excellent: "qaa/chemistry-2022/4.6.b3.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "synthesis, purification and characterisation", threshold: "qaa/chemistry-2022/4.6.b4", typical: "none", excellent: "qaa/chemistry-2022/4.6.b4.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "chemical measurement and analysis", threshold: "qaa/chemistry-2022/4.6.b5", typical: "none", excellent: "qaa/chemistry-2022/4.6.b5.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "computational chemistry", threshold: "qaa/chemistry-2022/4.6.b6", typical: "none", excellent: "qaa/chemistry-2022/4.6.b6.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "using the chemical literature", threshold: "qaa/chemistry-2022/4.6.b7", typical: "none", excellent: "qaa/chemistry-2022/4.6.b7.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "the independent project", threshold: "qaa/chemistry-2022/4.6.b8", typical: "none", excellent: "qaa/chemistry-2022/4.6.b8.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "chemistry and global challenges", threshold: "qaa/chemistry-2022/4.6.b9", typical: "none", excellent: "qaa/chemistry-2022/4.6.b9.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "chemistry and other subjects", threshold: "qaa/chemistry-2022/4.6.b10", typical: "none", excellent: "qaa/chemistry-2022/4.6.b10.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "mathematics in chemistry", threshold: "qaa/chemistry-2022/4.6.b11", typical: "none", excellent: "qaa/chemistry-2022/4.6.b11.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "data analysis methods", threshold: "qaa/chemistry-2022/4.6.b12", typical: "none", excellent: "qaa/chemistry-2022/4.6.b12.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "teamwork", threshold: "qaa/chemistry-2022/4.6.b13", typical: "none", excellent: "qaa/chemistry-2022/4.6.b13.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "communication", threshold: "qaa/chemistry-2022/4.6.b14", typical: "none", excellent: "qaa/chemistry-2022/4.6.b14.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "applying advanced understanding to complex problems", threshold: "qaa/chemistry-2022/4.7.b1", typical: "none", excellent: "qaa/chemistry-2022/4.7.b1.excellent", basis: "stated", domain: "understanding", award: "master's" }
  - { outcome: "using the literature to design methods", threshold: "qaa/chemistry-2022/4.7.b2", typical: "none", excellent: "qaa/chemistry-2022/4.7.b2.excellent", basis: "inferred", domain: "generic-skill", award: "master's" }
  - { outcome: "project planning", threshold: "qaa/chemistry-2022/4.7.b3", typical: "none", excellent: "qaa/chemistry-2022/4.7.b3.excellent", basis: "inferred", domain: "subject-skill", award: "master's" }
  - { outcome: "advanced experimental skills", threshold: "qaa/chemistry-2022/4.7.b4", typical: "none", excellent: "qaa/chemistry-2022/4.7.b4.excellent", basis: "inferred", domain: "subject-skill", award: "master's" }
  - { outcome: "discussing a research project", threshold: "qaa/chemistry-2022/4.7.b5", typical: "none", excellent: "qaa/chemistry-2022/4.7.b5.excellent", basis: "inferred", domain: "generic-skill", award: "master's" }
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
- { body: "Royal Society of Chemistry", says: "may accredit chemistry courses; bachelor's and multidisciplinary courses are usually accredited as partly meeting the academic criteria for Chartered Chemist (CChem) and integrated master's as fully meeting them, through site visits and desk review (D1, 2.20)", requirements: "not yet ingested: listed in Part E" }
- { body: "professional bodies, unnamed", says: "should be involved with students, graduates and employers in enhancing courses; multidisciplinary courses may be accredited by more than one (D1, 2.19; 2.20)", requirements: "not yet ingested: no body named (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.2", "1.10", "1.11", "2.7", "2.10", "3.5", "3.15", "3.22"], statements: ["1.2", "1.11", "2.10.b2"] }
  - { id: "theme:accessibility", named: "Accessibility", carriedIn: ["2.7", "2.8", "2.13", "2.19", "3.15", "3.16"], statements: ["2.7", "2.8", "2.13", "3.15"] }
  - { id: "theme:esd", named: "Education for sustainable development", carriedIn: ["1.1", "1.3", "1.12", "1.15", "3.3", "3.4", "3.13", "4.7"], statements: ["1.12", "3.3.b3", "3.4.b2", "4.7.b3", "4.7.b3.excellent"] }
  - { id: "theme:enterprise", named: "Employability, enterprise and entrepreneurship (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.13", "1.14", "1.15", "3.5", "3.6", "3.24"], statements: ["1.13", "3.6", "3.24", "3.8.b8"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.3", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.3", "4.2"] }
bodies:
  - { body: "Royal Society of Chemistry", citedIn: ["2.20"] }
  - { body: "professional bodies, unnamed", citedIn: ["2.19", "2.20"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "common descriptions of the four honours classes, for evidence of achievement above threshold" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "the QAA and Advance HE guidance Education for Sustainable Development", citedIn: ["1.12"], role: "further information on ESD" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers", citedIn: ["1.15"], role: "further information on enterprise education" }
  - { document: "not yet ingested: listed in Part E", named: "the Characteristics Statement for Higher Education in Apprenticeships", citedIn: ["2.6"], role: "general characteristics of apprenticeships" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "threshold-standard", definition: "the least needed to gain an honours degree in the subject, shown by an acceptable level of ability and skill (D1, 4.3)", beneficiaryDefinition: "the minimum you need to reach to be awarded an honours degree", scopeNote: "one of the two rungs of Tables 1 and 2", category: "unknown", practices: ["education"] }
- { slug: "excellent-standard", definition: "the level needed for a first-class degree, shown by consistently advanced knowledge, understanding and skill (D1, 4.3)", beneficiaryDefinition: "the level of work that earns a first-class degree", scopeNote: "the upper rung of Tables 1 and 2", category: "unknown", practices: ["education"] }
- { slug: "enterprise", definition: "generating and developing ideas, drawing on creativity, innovation, adaptability, reflection, problem-solving and communication (D1, 1.14)", beneficiaryDefinition: "coming up with ideas and turning them into something", scopeNote: "with entrepreneurship, a cross-cutting theme", category: "unknown", practices: ["education"] }
- { slug: "entrepreneurship", definition: "applying enterprise to create social, cultural or economic value, in private, public or third sectors and not only for profit (D1, 1.14)", beneficiaryDefinition: "using your ideas to create value for people, culture or the economy", scopeNote: "not limited to commercial activity", category: "unknown", practices: ["education"] }
- { slug: "integrated-masters-degree", definition: "an extended undergraduate award with honours, such as MChem or MSci, covering both honours and master's outcomes at greater depth (D1, 2.3)", beneficiaryDefinition: "a longer first degree that takes you to master's level", scopeNote: "FHEQ level 7; FQHEIS level 11", category: "unknown", practices: ["education", "chemistry"] }
- { slug: "monitoring-and-evaluation", definition: "periodic internal or external assessment of a course, using current and past data to understand achievement and plan ahead (D1, 2.15)", beneficiaryDefinition: "how your course is checked and improved over time", scopeNote: "with periodic review and external examining", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "threshold-standard", form: "threshold standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "excellent-standard", form: "excellent standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "enterprise", form: "Enterprise", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "entrepreneurship", form: "Entrepreneurship", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "integrated-masters-degree", form: "integrated master's degree", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "monitoring-and-evaluation", form: "Monitoring and evaluation", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Chemistry"
  edition: "March 2022 (fifth edition)"
  year: 2022
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/chemistry-2022/chemistry-2022.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 8719210f376e1569cb66c1c4fed4edcd96c6e9c403f62740bc017f9e94cfff23
  heldFiles: ["wkspc2601-library/txt/qaa-2022-chemistry-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2022-chemistry-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2022-chemistry-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2022-chemistry-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0041", citation: "QAA (2022) Subject Benchmark Statement: Chemistry, the PDF as published", settles: ["S4", "SB4"], asked: "2026-10-03", state: "wanted: to check Table 1's last row (no rung cells in the extraction), the page-break split of row 6 and the layout of Table 2's two cells" }
- { w: "W-std-0042", citation: "Royal Society of Chemistry, accreditation criteria for degree programmes (Chartered Chemist)", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0036", citation: "QAA (2019) Characteristics Statement: Higher Education in Apprenticeships", settles: ["SB6", "S7"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- Rung shape (new against Psychology): two rungs only, threshold and excellent, defined in 4.3; no typical rung, Annex D covering the classes between (4.2). The rungs sit in two tables, not separate lists.
- Table 1 (honours, caption after 4.6: 'graduates should be able to') has three columns: benchmark standard, threshold, excellent. Each of 14 rows has its own threshold and excellent text; recorded as 4.6.b<n> (threshold) and 4.6.b<n>.excellent, each on its own span, our ids under 4.6 where the table sits (rule 3: for P3). The first column is read as the row's outcome name, not a separate statement: rows 1, 3 to 6 and 9 to 14 restate 3.3 and 3.8 items, which are recorded there; rows 2, 7 and 8 reword them (3.3.b4, 3.8.b2, 3.10).
- Table 1's last row ('Act professionally ...') has no threshold or excellent cell in the held text; it repeats 3.8.b9 word for word and is not recorded again. Whether the PDF has cells there is for P2 (D3).
- Table 1 row 6 runs across a page break: the threshold cell ends '... covered in course content' and the excellent cell '... evaluate and'; each continues after the page number with 'and report outcomes using appropriate terminology.' The spans stop at the break; the paraphrases include the reporting. Extraction fault, for P2.
- Table 1 row 3 holds 'f or' (an extraction split of 'for') in both cells; kept as held.
- Table 2 (master's, in 4.7) has five outcomes but only row 1 carries threshold ('With significant support and guidance.') and excellent ('With a high degree of independence and autonomy.') cells. Read as merged cells qualifying all five outcomes, so each outcome is recorded at both rungs on its own span (4.7.b<n>, 4.7.b<n>.excellent). The reading is ours: gradeOf is stated for row 1 and inferred for rows 2 to 5. For P2 against the PDF.
- Force: threshold cells take force threshold (the column heading and 4.3); excellent cells take describes (4.3 defines excellent as the level for a first, not a requirement), as in run 0084's tables. The caption's 'should be able to' governs the outcome column. P3 to rule whether excellent cells take should.
- gradeOf: 19 links, each excellent cell to the threshold cell in its row; 15 stated (paired cells in one row: Table 1's 14 and Table 2 row 1) and four inferred (Table 2 rows 2 to 5).
- Outcome lists: 3.3 (14, should, all undergraduates), 3.4 (3, may, optional content: recorded as outcomes with force may; P3 to rule whether a may list is a standard), 3.8 (9, should, honours), 3.9 (6, should, integrated master's). The aims lists 1.3, 1.4 and 1.5 ('the aims ... are to') state course aims, not outcomes or obligations: not cut; S3 components.
- Levels: honours stated at FHEQ 6 and FQHEIS 10, integrated master's at FHEQ 7 and FQHEIS 11 (2.3). Standalone master's (MSc, MRes) are given no level; Table 2 records take fheq:7 by std:doc:qaa-fheq-2024-framework Table 1 (inferred). spine:6 and spine:7 are inferred from std:ref:uk-framework R2. No CQFW reference.
- Awards: 3.3 and 3.4 say 'undergraduate courses', recorded for both honours and integrated master's; 3.9 says master's degrees with honours (integrated master's); Table 2 and 4.7 cover integrated and standalone master's.
- Subject codes: HECoS 100417 and CAH07-02-01 and CAH07-02 marked stated, as the statement names Chemistry, though it gives no code (as run 0085); 101045 environmental chemistry and 100420 medicinal chemistry are inferred from 2.1. For P3.
- Obliging words outside the five, not cut as statements: 1.10 ('responsibility for, promoting equality'); 2.14 ('Providers are expected to develop processes for oversight'); 3.11 and 3.12 ('expected to take more ownership'; master's projects 'expected to be individual'). In 3.10 'expected to' sits beside a should, which is recorded; 2.13 'need to' sits beside a should. 3.22 'strongly encouraged'; 3.25 'considered crucial'.
- Not cut, with reasons: 2.12, 2.15, 2.17, 3.13 and 3.16 use will for routine practice (resits, review, examining, project training, session formats); 4.1 frames the tables (as run 0085); 4.3 defines the rungs (the skeleton's 4.3.b1 and 4.3.b2 rung candidates are definitions, recorded in B1); 4.5 and 2.20 describe.
- Plain-present provider norms not cut (template open point 5): 1.6, 2.5, 3.1, 3.15 first sentences ('Teaching and learning strategies are designed'), 3.21 first sentence, 4.4 ('Courses include the full range of content and skills'), 4.5.
- Skeleton corrections: 1.11, 1.12, 2.6, 2.8, 2.13, 3.2, 3.4.b3, 3.9.b6 and 3.20 carried a following sub-heading and are recut; 4.6 and 4.7 spans covered the tables and are recut to their own sentences; skeleton rung counts (threshold 2) replaced by the table counts.
- Paragraphs with two forces: 1.11 (must and should), 2.7 (must and should), 3.15 (must and should): one record each at must, the shoulds in paraphrase and versions. 2.9 (should and will) and 3.10 (expected to, should) recorded at should.
- Themes: the four in the front matter, with section 1 headings for three (EDI; ESD; employability, enterprise and entrepreneurship) and section 2 for accessibility. Employability recorded under theme:enterprise.
- Bodies: the Royal Society of Chemistry is the only body named in the body text (2.20); PSRBs and the Office for Students appear only in the front matter, the Disabled Students' Commission only in the back matter. The RSC accreditation criteria are not yet ingested (D3).
- Shared documents: Annex D is cited as the 2019 standalone annex (reference list) and is now in the 2024 Frameworks (std:doc:qaa-fheq-2024-framework); the apprenticeships characteristics statement is not yet ingested. The HEA (2016) employability framework is in the reference list only.
- Agent instructions pair the excellent cells with the Annex D first-class descriptions because 4.3 defines excellent as the level of a first; the choice of Annex D row for each outcome and the FHEQ descriptor ids are ours and inferred.
- Text faults noted, not acted on: 'under standing' in the contents; 'f irst' in 4.3; 'tacking unfamiliar problems' in 3.7; 'other's intellectual property' in 3.8.b8; 'honour's subjects' in 3.4.b3.
- S9 commentary not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:36: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0092 (P1); built by tools/bm_build.py.
