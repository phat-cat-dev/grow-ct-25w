---
id: std:doc:qaa-criminology-2022-benchmarks
title: "Subject Benchmark Statement: Criminology"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100484", label: "criminology", basis: "stated" }
  - { scheme: "cah", code: "CAH15-01-02", label: "sociology", basis: "inferred" }
  - { scheme: "hecos", code: "100483", label: "criminal justice", basis: "stated" }
edition: "March 2022 (fourth edition)"
published: 2022-03
status: current
supersedes: "the third edition (2019), revised from the 2014 and 2007 editions (D1, back matter)"
heldText: { method: sha256-bytes, raw: 93178fffca2a57964faea7e7fb4fc0cb6676f0782672c87651bb4fdc5fee5056, normalised: d29b5293c9bd2bc3cbf0e49097f070d8e7a01baccc4be75a5d69d47a533f1fcf }
heldTextStan: { method: sha256-stan, raw: 93178fffca2a57964faea7e7fb4fc0cb6676f0782672c87651bb4fdc5fee5056, normalised: 1b7eb5818dc50a7d384965c8cf7f61e04aa51c972b5042bffd93bd743dd09317 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2022 revision with cross-cutting themes (fourth edition of this Statement)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0098 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:55"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Criminology (QAA, March 2022)

> Run 0098, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2022-criminology-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
This document holds the academic standards QAA sets for criminology degrees in the UK: what an honours graduate should be able to do at three rungs (threshold, typical and excellent), shown as an eleven-row table, plus threshold outcomes for a master's degree, research-methods and ethics expectations by stage and the duties it places on course teams for inclusion, sustainability, employability and accessibility. Use it to describe, design or review a criminology course or to help a student see where their work stands; cite paragraph numbers and never treat it as regulation.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Criminology (QAA, March 2022) covers the bachelor's degree with honours (FHEQ level 6, FQHEIS level 10, stated) and sets threshold outcomes for postgraduate (master's) degrees. Section 4 states three rungs in one table: threshold (third class), typical (2:2 and 2:1) and excellent (first class), eleven outcomes each, worded with rising criticality and 'exceptional'; section 2 adds research-philosophy expectations at threshold and typical, excellent and postgraduate levels. Its cross-cutting themes are equality, diversity and inclusion; education for sustainable development (with green criminology); employability, entrepreneurship and enterprise; and accessibility. It names the British Society of Criminology, the British Sociological Association, the ESRC, the College of Policing and the National Probation Service, and points to Annex D of the FHEQ for the classification descriptions.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement: Criminology"
edition: "March 2022 (fourth edition)"
dates:
  published: 2022-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point published by QAA as a membership body; in England not a sector-recognised standard, in Wales and Scotland a key reference point, in Northern Ireland part of quality requirements (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2022", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "the academic standards of criminology degrees, chiefly the bachelor's degree with honours, with threshold standards for postgraduate degrees"
appliesTo:
  awards: ["bachelor's with honours", "master's"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This document relates mainly to bachelor's degrees with honours, although Criminology is also studied at levels above and below this\" (D1, 1.3)"
statedSubjects:
  - { name: "Criminology", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100484", label: "criminology" }, { scheme: "cah", code: "CAH15-01-02", label: "sociology" }] }
  - { name: "single honours ... joint honours", locator: "(D1, 1.1; 1.8; 2.21)", kind: "programme title", codes: [{ scheme: "hecos", code: "100484", label: "criminology" }] }
  - { name: "police studies, security, criminal justice policy, international criminology, forensic psychology and criminal justice", locator: "(D1, 1.4)", kind: "specialism", codes: [{ scheme: "hecos", code: "100483", label: "criminal justice" }, { scheme: "hecos", code: "100486", label: "policing" }, { scheme: "hecos", code: "100387", label: "forensic psychology" }] }
  - { name: "green criminology", locator: "(D1, 1.15; 1.16)", kind: "specialism", codes: [{ scheme: "hecos", code: "100484", label: "criminology" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "single and joint honours; core curriculum" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "academic, not occupational, standards; areas not content" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "honours focus; foundation and master's around it" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "origins at postgraduate level; specialisms" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes of a Criminology degree", gloss: "a changing field with a stable core" }
  - { number: "1.6", order: 8, componentType: area, parent: "section 1", heading: "Purposes of a Criminology degree", gloss: "what criminology is concerned with" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes of a Criminology degree", gloss: "the list is open" }
  - { number: "1.8", order: 10, componentType: area, parent: "section 1", heading: "Characteristics of a Criminology degree", gloss: "core areas for single and joint honours" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusion debates at the heart of the field" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "duty to embed inclusion in curricula" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusion built into course design" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "belonging and safe dialogue" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusion in review; removing barriers" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "diverse intake; under-represented groups" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainability as current curriculum" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "green criminology" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "theory with practice; proactive discipline" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "ethics tied to sustainability" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "ESD principles quoted" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "multidisciplinary teaching for ESD" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "content for global citizenship" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "skills; volunteering and placements" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "where to find ESD guidance" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "methodological skills at honours level" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "research ethics and employability" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "wide career routes; workforce links" }
  - { number: "1.27", order: 29, componentType: practice, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "employability opportunities and safeguards" }
  - { number: "2.1", order: 31, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "research and enquiry underpin the subject" }
  - { number: "2.2", order: 32, componentType: paragraph, parent: "section 2", heading: "Threshold and typical level", gloss: "research philosophy at threshold and typical" }
  - { number: "2.3", order: 33, componentType: paragraph, parent: "section 2", heading: "Excellent level", gloss: "research philosophy at excellent" }
  - { number: "2.4", order: 34, componentType: paragraph, parent: "section 2", heading: "Postgraduate level", gloss: "research competence at postgraduate level" }
  - { number: "2.5", order: 35, componentType: paragraph, parent: "section 2", heading: "Skills and competencies", gloss: "basic research design and reflexivity" }
  - { number: "2.6", order: 36, componentType: area, parent: "section 2", heading: "Skills and competencies", gloss: "basic qualitative approaches" }
  - { number: "2.7", order: 37, componentType: stem, parent: "section 2", heading: "Skills and competencies", gloss: "advanced qualitative analysis" }
  - { number: "2.8", order: 38, componentType: area, parent: "section 2", heading: "Skills and competencies", gloss: "basic quantitative techniques" }
  - { number: "2.9", order: 39, componentType: stem, parent: "section 2", heading: "Skills and competencies", gloss: "advanced quantitative techniques" }
  - { number: "2.10", order: 40, componentType: stem, parent: "section 2", heading: "Skills and competencies", gloss: "methods in practice, higher or postgraduate" }
  - { number: "2.11", order: 41, componentType: paragraph, parent: "section 2", heading: "Skills and competencies", gloss: "mixing data; stages of analysis" }
  - { number: "2.12", order: 42, componentType: paragraph, parent: "section 2", heading: "Skills and competencies", gloss: "knowing research ethics and codes" }
  - { number: "2.13", order: 43, componentType: stem, parent: "section 2", heading: "Skills and competencies", gloss: "ethical problems and strategies" }
  - { number: "2.14", order: 44, componentType: paragraph, parent: "section 2", heading: "Skills and competencies", gloss: "limits of ethical strategies" }
  - { number: "2.15", order: 45, componentType: paragraph, parent: "section 2", heading: "Skills and competencies", gloss: "ethics debates and data law" }
  - { number: "2.16", order: 46, componentType: paragraph, parent: "section 2", heading: "Skills and competencies", gloss: "ethical literacy for all" }
  - { number: "2.17", order: 47, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "varied entry routes" }
  - { number: "2.18", order: 48, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "accessible, single-tier teaching and assessment" }
  - { number: "2.19", order: 49, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression from foundations to graduate skills" }
  - { number: "2.20", order: 50, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "yearly progress; readiness for further study" }
  - { number: "2.21", order: 51, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint honours outcomes" }
  - { number: "2.22", order: 52, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards; Scottish four-year degree" }
  - { number: "2.23", order: 53, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "specialising; independent work late on" }
  - { number: "2.24", order: 54, componentType: practice, parent: "section 2", heading: "Flexibility", gloss: "varied teaching styles" }
  - { number: "2.25", order: 55, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "independent research and its risks" }
  - { number: "2.26", order: 56, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "influence on crime policy" }
  - { number: "2.27", order: 57, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "research partnerships and their aims" }
  - { number: "2.28", order: 58, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partners in justice and government" }
  - { number: "2.29", order: 59, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partner charities and NGOs" }
  - { number: "2.30", order: 60, componentType: practice, parent: "section 2", heading: "Partnership", gloss: "educational partnerships; placements" }
  - { number: "2.31", order: 61, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.32", order: 62, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers" }
  - { number: "2.33", order: 63, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examining" }
  - { number: "2.34", order: 64, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation by professional bodies" }
  - { number: "3.1", order: 66, componentType: area, parent: "section 3", heading: "Content", gloss: "debates that characterise the field" }
  - { number: "3.2", order: 67, componentType: area, parent: "section 3", heading: "Content", gloss: "theory, evidence and open dialogue" }
  - { number: "3.3", order: 68, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "empirical work driving theory" }
  - { number: "3.4", order: 69, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "contested core concepts" }
  - { number: "3.5", order: 70, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "modes of study; accessible materials" }
  - { number: "3.6", order: 71, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "principles for teaching, learning and assessment" }
  - { number: "3.7", order: 72, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "settings for teaching and learning" }
  - { number: "3.8", order: 73, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "purposes of assessment; monitoring outcomes" }
  - { number: "3.9", order: 74, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "what assessment covers" }
  - { number: "3.10", order: 75, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "scaffolded modules" }
  - { number: "4.1", order: 77, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "threshold standards for the honours award" }
  - { number: "4.2", order: 78, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "classes rest on level 6 or level 10" }
  - { number: "4.3", order: 79, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "most exceed the threshold; kinds of evidence" }
  - { number: "4.4", order: 80, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "three rungs named" }
  - { number: "4.5", order: 81, componentType: stem, parent: "section 4", heading: "Criminology subject-specific expectations", gloss: "the rung table: eleven outcomes at three rungs" }
  - { number: "4.6", order: 82, componentType: stem, parent: "section 4", heading: "Benchmark standard for postgraduate degrees", gloss: "threshold outcomes for master's degrees" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Criminology degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Criminology degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional reference points", kind: "other: front matter, read for S1 and S2" }
  - { number: "none", heading: "Contents", kind: "other: table of contents" }
  - { number: "1; 2; 3; 4", heading: "section headings", kind: "other: headings, recorded as sections in S3" }
  - { number: "5", heading: "Membership of the Advisory Group for the Subject Benchmark Statement for Criminology", kind: "other: back matter (review group members, 2022, 2019, 2014 and 2007)" }
  - { number: "none", heading: "publication details and copyright notice", kind: "other: back matter, read for S1 and S8" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 85 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/criminology-2022/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of a Criminology degree", "Equality, diversity and inclusion"] }
  span: { start: 16860, end: 17676 }
  source: "1.10 Criminologists have a responsibility to engage with students to ensure inclusivity in practice as well as theoretically and conceptually. In addition, equality issues relate to the fair and lawful treatment of students and staff. Not only is there a responsibility to meet public sector equality duties as set down in legislation, but there is an expectation that the discipline will ensure that equality-related matters are embedded within the curriculum. The study of equality, diversity and inclusion must be embedded within and across curricula, ensuring that our learning communities can prepare our graduates to make positive contributions to increasingly diverse workplaces and societies. To achieve this, criminology must endeavour to create inclusivity in the learning experience, design and delivery.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["engage", "embedded", "create"]
  about: "embedding equality, diversity and inclusion in the curriculum"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Criminology staff carry a responsibility to make inclusion real in practice as well as in theory; the study of equality, diversity and inclusion must run through and across curricula, and the discipline must work to make learning, design and delivery inclusive."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/1.11
  locator: { number: "1.11", headingPath: ["Context and purposes of a Criminology degree", "Equality, diversity and inclusion"] }
  span: { start: 17676, end: 18467 }
  source: "1.11 Equality and diversity practice must be embedded in the planning and design stage of courses and curricula, through learning design. This could include ensuring principles of equity and equality are embedded in the design, planning and evaluation of the course; creating saf e learning environments for students to express their ideas and beliefs; student involvement in assessment and delivery design; and ensuring the curriculum is flexible, accessible and responsive to an evolving and variated student population. Students will be respected as individual learners and may be engaged with as co-creators and co-producers of knowledge. Building flexibility into course design can ensure students are able to access a range of study materials, across a variety of delivery methods.\n\n6\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["embedded", "respected"]
  about: "inclusive learning design"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Equality and diversity must be built in when courses and curricula are planned and designed, for instance through equity in design and evaluation, safe spaces for students to voice views, student input to assessment and delivery and a curriculum that is flexible and accessible; students will be treated with respect as individual learners and may share in creating knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of a Criminology degree", "Equality, diversity and inclusion"] }
  span: { start: 18467, end: 19716 }
  source: "1.12 Equality and diversity should be further addressed at each stage of the student learning journey to achieve an inclusive learning experience. Criminology must ensure that students feel a sense of belonging, and a recognition that their experiences will enrich their learning rather than be a barrier to their success. Opportunities for meaningful and respectful dialogue and engagement within and across diverse student groups will contribute to an inclusive learning experience, such as ensuring that a lack of experience does not exclude them from fulfilling their potential, as well as considering the type of learning environment best suited to meeting student needs. Students should be supported to express their ideas and beliefs across a range of sensitive and controversial subject areas within the discipline, in a collaborative, saf e and collegiate environment, as well as being supported to reflect on how their own experiences may be shaping their views. Further, criminology should reflect critically on enabling increased participation with external communities, groups and public spaces to promote opportunities for embedding diverse cultural, social and institutional engagements at both undergraduate and postgraduate levels.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["addressed", "ensure", "supported"]
  about: "belonging and safe dialogue across the learning journey"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Equality and diversity should be revisited at every stage of study, and the discipline must make sure students feel they belong and that their experience adds to their learning; students should be helped to voice views on sensitive and contested topics in a safe, collegial setting and to reflect on how their experience shapes them, and criminology should look critically at widening links with outside communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of a Criminology degree", "Equality, diversity and inclusion"] }
  span: { start: 19716, end: 20921 }
  source: "1.13 Finally, equality and diversity should form the basis for disciplinary practice and delivery. Inclusivity must be seen as an ongoing process of quality review and enhancement, to promote equality of opportunity for students, while proactively addressing and removing barriers to learning and participation. At all stages of curriculum and course review, criminology should ensure that inclusivity is reflected upon and embedded as a catalyst for change. Course teams must consider whether there are hidden or overt barriers to success for certain groups of students and identify what changes could be undertaken to welcome under-represented groups. Existing students should likewise be exposed to saf e and collaborative methods of learning and expression, with a sense of being part of a shared community. Additionally, course teams should establish an environment that reflects appropriate role models among staff, active student support, and considered and thoughtful language to facilitate inclusion and diversity. The flexible manner in which the discipline can be studied (part-time, full-time, online, face-to-face, blended/hybrid) has also broadened the inclusive nature of the subject area.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["form", "consider", "identify", "establish"]
  about: "inclusive review and removing barriers"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Equality and diversity should underpin how the discipline is practised and delivered; inclusion must be treated as continuing quality review and enhancement, course teams must look for hidden or open barriers to success for some groups and for changes that would welcome under-represented groups; teams should build an environment with role models, active support and careful language."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/1.14
  locator: { number: "1.14", headingPath: ["Context and purposes of a Criminology degree", "Equality, diversity and inclusion"] }
  span: { start: 20921, end: 21672 }
  source: "1.14 Criminology degrees have traditionally attracted learners from a wide range of backgrounds, including, for example: mature students, students from non-traditional academic backgrounds, students from disadvantaged or less affluent backgrounds and students with caring responsibilities, disabilities and/or mental health considerations. As such, greater attention should be directed at under-represented groups at all stages, from recruitment, marketing, education and career progression to after graduation, in order to make certain that inclusive practice is both internally and externally visible. This will ensure criminology is recognised as a diverse global discipline that supports all students to reach their full potential. Sustainability\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["directed", "ensure", "supports"]
  about: "attention to under-represented groups"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Criminology draws students from many backgrounds, including mature students, those from non-traditional or less affluent backgrounds, carers and disabled students; more attention should go to under-represented groups at every stage from recruitment to after graduation, so that inclusive practice is seen inside and outside the institution."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/1.15
  locator: { number: "1.15", headingPath: ["Context and purposes of a Criminology degree", "Sustainability"] }
  span: { start: 21672, end: 22346 }
  source: "1.15 In order to ensure the sustainability of the discipline, criminology has to be fit for purpose and the purpose has to be clearly defined. Sustainability of criminology can be considered on two levels: within the University, as internal programme sustainability, and also as a discipline in the contemporary world (external). Internal sustainability of Criminology courses should not only be based on the recruitment numbers, but on ensuring that the curriculum is contemporary and encompassing of new and emerging theoretical and methodological developments, for example: green criminology, queer criminology, southern criminology, indigenous knowledge, and zemiology.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["based", "ensuring"]
  about: "keeping the curriculum current"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "For the discipline to last, its purpose needs to be clear; a course's internal sustainability should rest not only on recruitment but on a current curriculum that takes in new theoretical and methodological work such as green, queer and southern criminology, indigenous knowledge and zemiology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/1.16
  locator: { number: "1.16", headingPath: ["Context and purposes of a Criminology degree", "Sustainability"] }
  span: { start: 22346, end: 22811 }
  source: "1.16 Specifically, within the discipline, green criminology has grown in influence within recent years. green criminology addresses forms of crime that cause harm to the environment, explores ecological justice and studies environmental law and criminality. This focus encompasses individual crime, state failure in environmental protection and corporate\n\n7\ncrime. The design of Criminology curricula should include consideration of green criminology perspectives.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["include"]
  about: "green criminology in the curriculum"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Green criminology, which studies crime that harms the environment, ecological justice and environmental law, has grown in influence; curriculum design should consider its perspectives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of a Criminology degree", "Sustainability"] }
  span: { start: 22811, end: 23934 }
  source: "1.17 At its core, criminology is a merger between academia and practice. Theoretical approaches both inform and support practical applications and implementations to prepare students for professional life outside academia. The sustainability of Criminology degrees is directly linked with accessibility, employability and partnerships (please see the relevant sections below). Therefore, sustainable education includes working with criminal justice system agencies, practitioners, cross-sectors and cross-cultures to reflect ever-developing security and global challenges. Criminology, together with criminal and social justice agencies of a domestic and international nature, should aim to be proactive and pre-emptive, rather than just reactive. This will ensure sustainability of the discipline, which is of crucial importance when it comes to educating future practitioners, leaders, and research and development of modern remits in the quest for social justice. Innovation and standardisation of concepts and practices (including pedagogy) should also be considered when developing and managing sustainable education.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["aim", "considered"]
  about: "proactive, partnership-based sustainable education"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Criminology joins scholarship and practice, and sustainable education means working with justice agencies, practitioners and other sectors and cultures; together with justice agencies at home and abroad, the discipline should aim to act ahead of problems rather than only react, and should consider innovation and shared concepts and practice, pedagogy included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of a Criminology degree", "Sustainability"] }
  span: { start: 23934, end: 24666 }
  source: "1.18 Due to the nature of the discipline, ethics form an important part of teaching, research, theoretical, and methodological approaches respectively. Ethics cannot exist without sustainability, and sustainability cannot exist without ethics. Understanding and consideration of ethics is crucial for the development of criminology as a discipline, and it also should be considered at the development, updating and reviewing stages of the courses. Closely linked with ethics is studying emotive topics, which require a delicate balance of ethical considerations such as equality, diversity, open-mindedness, impartiality and accessibility. The success of this forms part of the sustainability of the programme and discipline alike.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["considered"]
  about: "ethics in course development"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Ethics runs through teaching, research and the discipline's theory and methods, and is tied to sustainability; it should be considered when courses are developed, updated and reviewed, not least because emotive topics call for a careful balance of equality, diversity, open-mindedness, impartiality and accessibility."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/1.20
  locator: { number: "1.20", headingPath: ["Context and purposes of a Criminology degree", "Sustainability"] }
  span: { start: 25410, end: 25911 }
  source: "1.20 Therefore, understanding the multi-disciplinary nature of criminology should guide the practices of curricular development and teaching methodologies, which empowers learners to critically understand the interconnectedness between culture, economy, environment and globalisation. Ultimately, university education, and criminology in particular, has a significant role to play in achieving the aims of the ESD - transforming society and providing the foundation for a safer and sustainable world.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["guide", "empowers"]
  about: "multidisciplinarity guiding curriculum and teaching"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding that criminology draws on many disciplines should guide curriculum development and teaching methods, helping learners grasp critically how culture, economy, environment and globalisation connect."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/1.21
  locator: { number: "1.21", headingPath: ["Context and purposes of a Criminology degree", "Sustainability"] }
  span: { start: 25911, end: 26323 }
  source: "1.21 Criminology should also offer students knowledge across several subject areas, such as poverty, social justice, environmental and social harms, which enables learners to gain greater awareness of sustainable development and global citizenship and equip them with the skills and knowledge necessary to address 'social, environmental and economic concerns to create a better world' (ESD Guidance, 2021, p.8).\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["offer", "enables"]
  about: "knowledge for sustainable development and global citizenship"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Criminology should also give students knowledge across topics such as poverty, social justice and environmental and social harm, building awareness of sustainable development and global citizenship and the skills to act on social, environmental and economic concerns."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of a Criminology degree", "Sustainability"] }
  span: { start: 26323, end: 26971 }
  source: "1.22 Criminology students develop a range of skills, such as critical thinking, presenting effective arguments and the ability to listen to others; all crucial skills for global citizenship and criminal justice and security settings. When possible, students should be encouraged to pursue volunteering or work placements opportunities, which relate to sustainability of both\n\n8\neducational development and the discipline within and beyond the academic realm. Such service and work learning can be embedded within modules. It is therefore implied to consider creating opportunities for applied learning in relation to sustainability where possible.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["encouraged", "embedded"]
  about: "volunteering and placements for sustainability"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Criminology students build skills such as critical thinking, argument and listening that matter for global citizenship and for justice and security work; where possible they should be encouraged to take up volunteering or placements linked to sustainability, and such learning can sit inside modules."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of a Criminology degree", "Entrepreneurship and enterprise education"] }
  span: { start: 27153, end: 27523 }
  source: "1.24 Students of Criminology at honours degree level are expected to develop a range of skills that will enable them to comprehend methodological concepts and principles. This includes understanding the relationship between theory and methods in criminological research and more specialist knowledge about the role, functions and practices of criminal justice agencies.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop", "comprehend"]
  about: "methodological skills at honours level"
  themes: [theme:enterprise]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours students in criminology are expected to build skills for grasping methodological concepts and principles, including how theory relates to method in research and specialist knowledge of what criminal justice agencies do."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/1.27
  locator: { number: "1.27", headingPath: ["Context and purposes of a Criminology degree", "Entrepreneurship and enterprise education"] }
  span: { start: 29128, end: 30178 }
  source: "1.27 Opportunities for students to develop their employability skills should be offered at an appropriate point in the course. This may be in traditional placement opportunities, or volunteering, or through in-module developments, such as assessments linked to employability-based skills, or the use of guest speakers on courses to link theory to practice. Such opportunities provide students with the chance to engage with the applied nature of criminology, as well as enhancing transferable skills. They can operate both within and outside of the formal curriculum and, when integrated, students may be invited to reflect on their experiences within the broader context of their criminological knowledge as part of their assessment. Safeguards are put in place for the protection of students' rights from work- based exploitation and/or harassment. It is also important that employers who offer placement and volunteering opportunities consider accessibility and reasonable adjustments where needed, and that any additional support is in place.\n\n9\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["offered", "consider"]
  about: "employability opportunities"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Chances for students to build employability skills should be offered at a suitable point, through placements, volunteering, employability-linked assessment or guest speakers; safeguards protect students from exploitation or harassment at work, and it matters that placement employers consider accessibility and reasonable adjustments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of a Criminology degree", "Design"] }
  span: { start: 30232, end: 30564 }
  source: "2.1 Research and critical enquiry underpin criminology; therefore, students are expected to develop a range of skills that will enable them to comprehend methodological concepts and principles. This includes understanding the relationship between theory, evidence and methods in criminological research. Threshold and typical level\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop", "comprehend"]
  about: "methodological concepts and principles"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Because research and critical enquiry underpin criminology, students are expected to build skills for grasping methodological concepts and principles, including how theory, evidence and method relate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.2
  locator: { number: "2.2", headingPath: ["Distinctive features of a Criminology degree", "Threshold and typical level"] }
  span: { start: 30564, end: 31438 }
  source: "2.2 At threshold and typical level, students are expected to understand arguments in the philosophy of explanation in contemporary criminological research. Thus, an understanding of the concepts of ontology and epistemology for the design, analysis, interpretation and dissemination of criminological research will be important. Students will also be expected to understand the fundamental distinction which can be made between qualitative and quantitative research strategies, as well as the debates surrounding mixing the two (mixed methods research), and from this develop an understanding of inductive and deductive relationships between theory and research. They should also be able to discern which data collection and analysis methods are suitable for different kinds of research questions, bearing in mind that research may use multiple methods and/or mixed methods."
  stem: none
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours students at the threshold level"
  addressee: learner
  verbs: ["understand", "discern"]
  about: "philosophy of explanation and research strategies (threshold)"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold level (set jointly with typical) students are expected to understand arguments about explanation in criminological research; ontology and epistemology; the split between qualitative and quantitative research, with mixed methods; inductive and deductive reasoning; they should also be able to tell which data collection and analysis methods suit which research questions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.2.typical
  locator: { number: "2.2.typical", headingPath: ["Distinctive features of a Criminology degree", "Threshold and typical level"] }
  span: { start: 30564, end: 31438 }
  source: "2.2 At threshold and typical level, students are expected to understand arguments in the philosophy of explanation in contemporary criminological research. Thus, an understanding of the concepts of ontology and epistemology for the design, analysis, interpretation and dissemination of criminological research will be important. Students will also be expected to understand the fundamental distinction which can be made between qualitative and quantitative research strategies, as well as the debates surrounding mixing the two (mixed methods research), and from this develop an understanding of inductive and deductive relationships between theory and research. They should also be able to discern which data collection and analysis methods are suitable for different kinds of research questions, bearing in mind that research may use multiple methods and/or mixed methods."
  stem: none
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours students at the typical level"
  addressee: learner
  verbs: ["understand", "discern"]
  about: "philosophy of explanation and research strategies (typical)"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/2.2, basis: stated }
  paraphrase: "The issuer sets the same research-philosophy expectation for the typical level as for threshold: understanding debates on explanation, ontology and epistemology, research strategies, mixed methods and induction and deduction; and being able to match methods to questions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of a Criminology degree", "Excellent level"] }
  span: { start: 31455, end: 32109 }
  source: "2.3 At excellent level of achievement (first class level) students are not only expected to be able to discuss the relationship between theory and method in criminological research, but to develop the ability to criticise and apply concepts in criminological thought to the design of research projects. At this level students should be able to demonstrate an ability to criticise the philosophy of explanation adopted by criminological studies. In other words, they should be able to appreciate the ethical implications of the chosen research methods and the political value of different interpretations of research data and findings. Postgraduate level\n"
  stem: none
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours students at the excellent level"
  addressee: learner
  verbs: ["discuss", "criticise", "apply", "demonstrate", "appreciate"]
  about: "critique of research philosophy (excellent)"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/2.2.typical, basis: inferred }
  paraphrase: "At the excellent (first-class) level students are expected not only to discuss how theory and method relate but to critique and apply criminological concepts in designing research; they should be able to criticise the explanatory philosophy of criminological studies and see the ethical stakes of methods and the political weight of different readings of data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of a Criminology degree", "Postgraduate level"] }
  span: { start: 32109, end: 32738 }
  source: "2.4 At a postgraduate level, students are not only expected to be able to comprehend key methodological concepts and principles, and develop an ability to criticise and apply concepts in criminological thought to the design of research projects, but also recognise nuanced debates. At postgraduate level there is an expectation of the development of a wider range of skills and competencies than at undergraduate level and demonstration of ability to design and implement criminological research projects in real world situations, while making use of a wide repertoire of research methods and strategies. Skills and competencies\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:7
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["comprehend", "develop", "criticise", "apply", "recognise"]
  about: "research competence at postgraduate level"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At postgraduate level students are expected to grasp key methodological concepts, critique and apply criminological thought in research design and recognise subtle debates, with a wider range of skills than undergraduates and the ability to design and carry out research in real-world settings using many methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of a Criminology degree", "Skills and competencies"] }
  span: { start: 32738, end: 33058 }
  source: "2.5 At a basic level, students are expected to have foundational knowledge of the following in relation to both qualitative and quantitative methods: how to develop a research question and design research; how to reflect on research designs and practice, thinking in particular about positionality and power imbalances.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop", "design", "reflect"]
  about: "foundations of research design and reflexivity"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Early in the degree students are expected to have grounding, for both qualitative and quantitative methods, in forming research questions, designing research and reflecting on design and practice, with attention to positionality and power."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of a Criminology degree", "Skills and competencies"] }
  span: { start: 33058, end: 33881 }
  source: "2.6 In relation to qualitative methods at a basic level, students are expected to have a foundational knowledge of different approaches available, which may include:\n• case study design\n• interviewing (including knowledge of the difference between structured, semi-structured and unstructured interview schedules)\n\n10\n• focus groups\n• observation\n• documentary and discourse analysis\n• ethnography\n• virtual ethnography\n• participatory action research\n• decolonising research methods with indigenous communities\n• internet research (including social media research techniques)\n• evaluation methods\n• visual methods\n• sampling strategies\n• the differences between description, analysis and interpretation in regard to analysis\n• how to index and retrieve qualitative data\n• the limits to interpretation\n• internet research.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["have"]
  about: "basic knowledge of qualitative approaches"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At a basic level students are expected to know the range of qualitative approaches available; the issuer's list is illustrative, running from case studies, interviews, focus groups, observation and ethnography to participatory, decolonising, internet, visual and evaluation methods, sampling, indexing and interpreting qualitative data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of a Criminology degree", "Skills and competencies"] }
  span: { start: 33881, end: 34233 }
  source: "2.7 At a higher or more advanced level, students would be expected to demonstrate knowledge and possible use of some of the following qualitative techniques and software:\n• coding qualitative data\n• analysis qualitative data\n• interpretation of qualitative findings\n• using qualitative software to facilitate analysis (for example, ATLAS.ti or NVivo )\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "be expected to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "advanced qualitative analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "In the later, more advanced stages, students would be expected to show knowledge, and perhaps use, of some qualitative techniques and software, such as coding, analysis and interpretation, using packages like ATLAS.ti or NVivo."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of a Criminology degree", "Skills and competencies"] }
  span: { start: 34233, end: 34923 }
  source: "2.8 Focusing on quantitative methods, at a basic level, students are expected to have foundational knowledge of some of the quantitative techniques available, which may include:\n• how to develop a questionnaire\n• survey sampling\n• experimental design (including randomised control trials)\n• evaluation methods\n• understanding the use of statistical analysis software packages and basic analysis, for example, SPSS or 'R'\n• comparing means in statistical analysis\n• the distinction between correlation and causation\n• how to approach use of secondary data sets\n• use and understanding of descriptive and inferential statistics, basic statistical tests (for example, cross-tabs, chi-square).\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["have"]
  about: "basic knowledge of quantitative techniques"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "For quantitative methods, early in the degree students are expected to know some of the techniques available, illustratively questionnaire design, survey sampling, experimental design, evaluation, statistical software, comparing means, correlation and causation, secondary data and descriptive and inferential statistics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of a Criminology degree", "Skills and competencies"] }
  span: { start: 34923, end: 35347 }
  source: "2.9 At a higher or more advanced level, students would be expected to demonstrate knowledge and possible use of some of the following quantitative techniques:\n• T-tests\n• ANOVA\n• other forms of multi-variate analysis\n• systematic reviews\n• secondary data and big data\n• data mapping\n• graphical presentation of statistics data\n• online data analysis, for example via social media platforms such as Twitter and Facebook.\n\n11\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "be expected to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "advanced quantitative techniques"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "In the later, more advanced stages, students would be expected to show knowledge, and perhaps use, of some quantitative techniques such as t-tests, ANOVA and other multivariate analysis, systematic reviews, secondary and big data, data mapping, graphical presentation and online data analysis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of a Criminology degree", "Skills and competencies"] }
  span: { start: 35347, end: 35661 }
  source: "2.10 At a higher or postgraduate level there is also an expectation of knowledge and understanding of both qualitative and quantitative methods, and possible utilisation, of the following in practice:\n• computer-assisted personal interviewing\n• use of ATLAS.ti or NVivo\n• systematic reviews\n• virtual ethnography.\n"
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["use"]
  about: "methods in practice at higher or postgraduate level"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "At higher or postgraduate level there is a further expectation of knowing and understanding, and perhaps using in practice, computer-assisted personal interviewing, qualitative software, systematic reviews and virtual ethnography."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of a Criminology degree", "Skills and competencies"] }
  span: { start: 35661, end: 36187 }
  source: "2.11 Data analysis: All students should also gain a basic understanding of how qualitative and quantitative data can be mixed. This entails consideration of intra method and inter methods triangulation and data integration, as well as data analysis principles: induction, deduction and abduction. All students should also gain a basic understanding of the different stages of data analysis, such as data reduction, data display, data transformation, data correlation, data consolidation, data comparison and data integration.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["gain"]
  about: "mixing data and the stages of analysis"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "All students should also acquire a basic grasp of two things: how qualitative and quantitative data can be combined, including triangulation, data integration and inductive, deductive and abductive reasoning; and the stages of analysis from reduction and display to comparison and integration."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of a Criminology degree", "Skills and competencies"] }
  span: { start: 36187, end: 36926 }
  source: "2.12 Ethical considerations are fundamental to any research. At all levels, students are expected to have knowledge of what is meant by 'ethics', policy frameworks, the difference between individual, legal and professional ethics, and key codes or statements of ethics utilised by criminologists (for example, the British Society of Criminology's Statement of Ethics, the British Sociological Association's Code of Ethics). Consideration should also be given to issues of power, positionality and reflexivity. Students should show that they can engage in discussion about the value and limitations of codes of ethics. They are also expected to know about the practicalities of applying for ethics approval in their particular institution.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["show", "engage", "know"]
  about: "knowledge of research ethics and codes"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Ethics is basic to all research; at every level students are expected to know what ethics means, the policy frameworks, the difference between personal, legal and professional ethics and the main codes criminologists use, and should show they can discuss the value and limits of codes; they are also expected to know how to get ethical approval locally."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.13
  locator: { number: "2.13", headingPath: ["Distinctive features of a Criminology degree", "Skills and competencies"] }
  span: { start: 36926, end: 37556 }
  source: "2.13 Some common examples of ethical problems are: interviews which trigger painful experiences; using material without consent; and unconsciously manipulating the direction and content of material so as to produce results/findings which conform to a particular research theory. Students are also expected to be able to consider strategies such as:\n• choosing an appropriate research design\n• holding f ast to the concept of 'informed consent' or 'valid consent'\n• maintaining confidentiality\n• engaging 'hard to reach' and 'vulnerable' populations and the appropriate research designs and ethical protocols that may be required.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["consider", "choosing", "maintaining", "engaging"]
  about: "strategies for ethical problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Ethical problems include interviews that revive painful experiences, using material without consent and steering data towards a favoured theory; students are expected to be able to weigh up approaches such as a fitting research design, informed or valid consent, confidentiality and ethical approaches to hard-to-reach and vulnerable groups."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of a Criminology degree", "Skills and competencies"] }
  span: { start: 37556, end: 38050 }
  source: "2.14 At the higher and postgraduate levels there is an expectation that students would have increased awareness that these strategies are not straightforward (for example, what is meant by 'appropriate research design', 'autonomy' and 'confidentiality'? Are there situations where confidentiality cannot be guaranteed or where the situation demands the breaking of confidentiality?). There should also be awareness of ways of minimising harm and different ways of safeguarding confidentiality.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["have"]
  about: "the limits of ethical strategies"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "At higher and postgraduate levels students are expected to see that these strategies are not simple, for instance when confidentiality cannot be guaranteed or has to be broken; there should also be awareness of ways to minimise harm and protect confidentiality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.15
  locator: { number: "2.15", headingPath: ["Distinctive features of a Criminology degree", "Skills and competencies"] }
  span: { start: 38050, end: 38470 }
  source: "2.15 At the higher and postgraduate levels, students are expected to be aware of contextual debates about ethics (for example, are disciplinary codes needed or would a general code suffice?) and to be familiar with details of what the law requires as well as what personal ethics require (including principles within relevant legislation and exemptions for researchers) in line with current data protection legislation.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["be"]
  about: "ethics debates and data protection law"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "At higher and postgraduate levels students are expected to know the wider debates on ethics, such as whether discipline codes are needed, and to know what the law and personal ethics require, including current data protection law and its research exemptions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.16
  locator: { number: "2.16", headingPath: ["Distinctive features of a Criminology degree", "Skills and competencies"] }
  span: { start: 38470, end: 38665 }
  source: "2.16 In summation, there is an expectation that all students gain an appropriate level of 'ethical literacy' so as to ensure the safety and well-being of research participants.\n\n12\nAccessibility\n"
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["gain", "ensure"]
  about: "ethical literacy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Overall, all students are expected to reach a suitable level of ethical literacy so that research participants stay safe and well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.18
  locator: { number: "2.18", headingPath: ["Distinctive features of a Criminology degree", "Accessibility"] }
  span: { start: 38878, end: 40176 }
  source: "2.18 The principal learning and teaching methods that a Criminology student may experience will depend on the aims and objectives of the course, given the wide range of subject-specific and transferable skills being developed. The creation of a two-tier system that singles out students with additional needs must be avoided, therefore, teaching and assessments may need to be adjusted or tailored to the requirements of individuals to ensure inclusiveness and well-being, different formats should be offered to all students and expectations should be transparent. Reasonable adjustments should be considered for fieldwork to enable all students, where possible, to participate. In addition, all practical efforts should be made to ensure equal access to extracurricular activities such as field trips, placements and volunteering opportunities, given the often hidden costs (including opportunity costs) involved. The timing of religious observances and school holidays may be considered when setting deadlines. It should be remembered that perceptions of assessment may differ according to the cultural and experiential backgrounds of both assessors and their students. Clear and accessible guidance outlining assessment criteria at different stages of the degree should be expected. Progression\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["avoided", "adjusted", "offered", "considered"]
  about: "accessible, single-tier teaching and assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Teaching methods depend on course aims; a two-tier system singling out students with extra needs must be avoided, so teaching and assessment may be tailored, varied formats should be offered to all and expectations should be clear; reasonable adjustments should be considered for fieldwork, equal access to trips, placements and volunteering pursued and assessment criteria should be clear and accessible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of a Criminology degree", "Progression"] }
  span: { start: 40176, end: 40664 }
  source: "2.19 At the beginning of a degree in Criminology, students are expected to develop and appreciate an understanding of core theoretical knowledge and develop fundamental study skills. This enables students at subsequent points of the course to strengthen their analytic, interpretative and communication skills and, by graduation, to demonstrate the problem- solving, evaluative and reflective skills intrinsic to the subject and the attributes needed for self-managed, lifelong learning.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop", "appreciate", "strengthen", "demonstrate"]
  about: "progression from foundations to graduate skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Early in the degree students are expected to build core theoretical knowledge and basic study skills, then strengthen analysis, interpretation and communication and by graduation show problem-solving, evaluation and reflection and the attributes for self-managed, lifelong learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.20
  locator: { number: "2.20", headingPath: ["Distinctive features of a Criminology degree", "Progression"] }
  span: { start: 40664, end: 41379 }
  source: "2.20 Over the course of a degree with honours (FHEQ level 6; FQHEIS level 10) a Criminology student will progress from one year of study to the next, in line with the regulations and processes for each institution. However, it is expected that each year would see the attainment of certain levels of knowledge, expertise and experience that build towards the final achievement of meeting the threshold-level subject-specific and generic skills listed in this Statement. Upon graduation from an undergraduate degree, it would be expected that a student who had achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in Criminology or an associated discipline.\n"
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["progress", "meeting", "undertaking"]
  about: "progress towards the threshold and readiness for postgraduate study"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Across an honours degree, which the issuer places at FHEQ level 6 and FQHEIS level 10, students move through the years under each institution's rules, each year expected to build towards the threshold subject-specific and generic skills; a graduate with a second-class degree or better would be expected to be ready for postgraduate study in criminology or a related field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.21
  locator: { number: "2.21", headingPath: ["Distinctive features of a Criminology degree", "Progression"] }
  span: { start: 41379, end: 41699 }
  source: "2.21 Joint honours undergraduates will achieve core elements of the specific and generic skills for the subject and will add others according to the subjects covered in joint courses. Additionally, they may explore the overlap between their two subject areas, creating further opportunities for interdisciplinary study.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "joint honours outcomes"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Joint honours students will attain the core subject-specific and generic skills of criminology, add others from their second subject and may explore where the two meet."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.23
  locator: { number: "2.23", headingPath: ["Distinctive features of a Criminology degree", "Progression"] }
  span: { start: 42143, end: 42836 }
  source: "2.23 As students progress through their course, it is anticipated there will be greater opportunity for specialisation, and higher levels of study should enable students to develop deeper analytical and critical skills. Both core and optional modules will enable students to\n\n13\ndevelop expertise and focus their learning on particular fields of interest. Opportunities for the formal assessment of students' independent and more specialised study, for example the presentation of a dissertation or research project, will normally occur towards the end of the course and enable students to produce an independent piece of work, which may be empirical, policy-based or theoretical. Flexibility\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["enable", "develop", "occur", "produce"]
  about: "specialising and independent work later in the course"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As students progress, chances to specialise are expected to grow; higher levels should help them deepen analytical and critical skills, core and optional modules will let them build expertise and assessed independent study such as a dissertation will normally come near the end."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/2.25
  locator: { number: "2.25", headingPath: ["Distinctive features of a Criminology degree", "Flexibility"] }
  span: { start: 43104, end: 43576 }
  source: "2.25 As noted above, within most Criminology degree courses there is a requirement that students undertake some form of independent research work, often in the form of project work and/or a dissertation presented in the later stages of the course. This represents an area of the student's learning in which mature and intelligent critical reflection is needed with regard to the potential risks and moral and ethical issues associated with a proposed project. Partnership\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "requirement" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["undertake"]
  about: "independent research and reflection on its risks"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most criminology degrees ask students to do some independent research, usually a project or dissertation late in the course, which calls for mature, intelligent reflection on its risks and its moral and ethical issues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/2.32
  locator: { number: "2.32", headingPath: ["Distinctive features of a Criminology degree", "Monitoring and review"] }
  span: { start: 46134, end: 46446 }
  source: "2.32 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Externality is key to UK quality assurance; providers will use external reviewers in periodic review to gain an outside view of proposed changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/3.5
  locator: { number: "3.5", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 50488, end: 50979 }
  source: "3.5 Students of Criminology engage with course materials in a variety of ways which may include classroom, online or blended/hybrid learning, independent study, or a mixture of options, full or part-time. Students may have access to a range of resources, both traditional, such as core texts and journals, and complementary, such as online tutorials, streaming services and additional online content provided by publishers. It is important to ensure that these materials are accessible.\n\n16\n"
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["ensure"]
  about: "accessible learning materials"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students meet course materials in many ways and modes, full or part-time, with core texts, journals and online resources; it matters that these materials are accessible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/3.6.b1
  locator: { number: "3.6.b1", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 51068, end: 51528 }
  source: "a) Criminology is neither purely deductive nor purely descriptive; theorisation needs both to guide the collection of data and to be grounded in evidence. Similarly, interpretation of data has to be guided by theorisation. Students are, therefore, given opportunities to acquire capacities of thinking in both abstract and concrete terms and to relate the two. It is expected that criminological theory is a core, foundational aspect of any Criminology degree."
  stem: "3.6"
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["guide", "relate"]
  about: "theory as a core of the degree"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Criminology is neither purely deductive nor descriptive: theory guides data collection and interpretation and has to rest on evidence, so students get chances to think abstractly and concretely and link the two; theory is expected to be a core, foundational part of any criminology degree."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/3.6.b2
  locator: { number: "3.6.b2", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 51529, end: 52014 }
  source: "b) Bodies of evidence in criminology are often consistent with alternative interpretations embodied in rival theoretical perspectives. Students are required to weigh alternative interpretations in terms of consistency with evidence, logic, fit with other findings and breadth of explanatory power. Therefore, students are provided with opportunities to rehearse and revise their own ideas and where these fit into their own understanding of criminology and the criminal justice system."
  stem: "3.6"
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["weigh", "rehearse", "revise"]
  about: "weighing rival interpretations of evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Evidence in criminology often fits rival theories, so students are required to weigh alternative readings by how well they match the evidence, their logic, how they sit with other findings and how much they explain, and are given chances to test and revise their own ideas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/3.6.b3
  locator: { number: "3.6.b3", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 52015, end: 52623 }
  source: "c) Criminology is an ever-evolving discipline and reflects current social, political and public disputes. Therefore, students are provided with opportunities to develop awareness of, and reflect on, their own values and those of their cultural, global and political environment, and an appreciation of how alternative values impact upon rival interpretations of evidence. Learning, teaching and assessment approaches within criminology should enable students to engage with these social, political and public disputes, and offer opportunities to apply criminological knowledge to contemporary crime problems."
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["enable", "engage", "apply"]
  about: "engaging with public disputes and with values"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Criminology mirrors current social, political and public disputes, so students get chances to reflect on their own values and those around them and on how values shape rival readings of evidence; learning, teaching and assessment should let students engage with these disputes and apply criminological knowledge to current crime problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/3.6.b4
  locator: { number: "3.6.b4", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 52624, end: 53434 }
  source: "d) Criminology attracts students from diverse academic and social backgrounds; their learning and skills development needs vary accordingly. To reflect this, degree courses need to provide flexible and varied teaching, learning and assessment strategies to ensure that all students have as equal an opportunity as possible to acquire the necessary knowledge and skills to graduate in Criminology. Where possible, criminological learning, teaching and assessment approaches should be designed to be as inclusive as possible to remove the need for alternative assessment. Alongside this, all involved in the delivery of learning, teaching and assessment within criminology should recognise the emotive nature of much of criminology, and the challenges and impact of engaging with potentially distressing content."
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["provide", "designed", "recognise"]
  about: "inclusive strategies and distressing content"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students come from diverse backgrounds with varying needs, so courses need flexible, varied strategies giving all as equal a chance as possible; approaches should be designed to be inclusive enough to make alternative assessment unnecessary, and everyone teaching should recognise the emotive nature of the subject and the impact of distressing content."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/3.8
  locator: { number: "3.8", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 53801, end: 54348 }
  source: "3.8 Assessment is a crucial component for student learning, progression and personal development. It is necessary to monitor student progress, motivate learning, provide 'feed forward' feedback, and to grade students in line with the appropriate assessment criteria. As noted earlier, reasonable adjustments may need to be made to assessment to ensure inclusivity. Course teams should monitor student outcomes and reflect on assessment strategies - for example, monitor by protected characteristics to ensure there are no unintended outcomes.\n\n17\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["monitor", "reflect"]
  about: "monitoring assessment outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessment drives learning, progress and development, and serves to monitor progress, motivate, give feed-forward and grade against criteria; reasonable adjustments may be needed for inclusion, and course teams should monitor student outcomes, for example by protected characteristics, and reflect on assessment strategies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/3.10
  locator: { number: "3.10", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54779, end: 54933 }
  source: "3.10 Modules within a Criminology course should be scaffolded to enable students to build on previous learning as they progress through their course.\n\n18\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["scaffolded", "build"]
  about: "scaffolded modules"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Modules in a criminology course should be scaffolded so that students can build on earlier learning as they progress."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55297, end: 55777 }
  source: "4.2 Students are assessed against their curricula of study, which should allow them to achieve the required learning outcomes and to develop and demonstrate characteristics associated with the higher level of learning of a bachelor's degree with honours. At the most fundamental level, each classification means that students have achieved the characteristics of Level 6 in England, Wales and Northern Ireland, and Level 10 in Scotland of the respective qualification frameworks.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "criminology courses and course teams"
  addressee: provider
  verbs: ["assessed", "allow", "achieve"]
  about: "curricula enabling the honours outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students are assessed against their curricula, which should let them reach the required outcomes and show the higher learning of an honours degree; at base every class shows the student has reached level 6 (England, Wales and Northern Ireland) or level 10 (Scotland)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/criminology-2022/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 57140, end: 57265 }
  source: "describe and examine a range of key concepts and theoretical approaches within criminology, and to evaluate their application"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["describe", "examine", "evaluate"]
  about: "describing and examining key concepts and theories"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold (third-class) level, a graduate should be able to set out and look closely at the main concepts and theories of criminology, and judge how well they work when applied."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 57268, end: 57404 }
  source: "describe and critically examine a range of key concepts and theoretical approaches within criminology, and to evaluate their application"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["describe", "examine", "evaluate"]
  about: "critically examining key concepts and theories"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b1, basis: stated }
  paraphrase: "At the typical (2:2 and 2:1) level, a graduate should be able to set out and critically interrogate the main concepts and theories of criminology, and judge how well they work when applied."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 57407, end: 57567 }
  source: "describe and critically examine to an exceptional level a range of key concepts and theoretical approaches within criminology, and to evaluate their application"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["describe", "examine", "evaluate"]
  about: "exceptional critical examination of key concepts and theories"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b2, basis: stated }
  paraphrase: "At the excellent (first-class) level, a graduate should be able to set out and critically interrogate, to an exceptional standard, the main concepts and theories of criminology, and judge how well they work when applied."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 57658, end: 57768 }
  source: "assess political and social processes of victimisation and criminalisation in light of criminological theories"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["assess"]
  about: "assessing processes of victimisation and criminalisation"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold (third-class) level, a graduate should be able to weigh up, using criminological theory, the political and social processes by which people are victimised and criminalised."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 57771, end: 57892 }
  source: "critically assess political and social processes of victimisation and criminalisation in light of criminological theories"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["assess"]
  about: "critically assessing processes of victimisation and criminalisation"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b4, basis: stated }
  paraphrase: "At the typical (2:2 and 2:1) level, a graduate should be able to weigh up critically, using criminological theory, the political and social processes by which people are victimised and criminalised."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 57895, end: 58041 }
  source: "provide exceptional critical assessment of political and social processes of victimisation and criminalisation in light of criminological theories"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["provide"]
  about: "exceptional critical assessment of victimisation and criminalisation"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b5, basis: stated }
  paraphrase: "At the excellent (first-class) level, a graduate should be able to give an exceptionally critical appraisal, using criminological theory, of the political and social processes by which people are victimised and criminalised."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 58044, end: 58227 }
  source: "provide an account of social diversity and inequality and their effects in relation to crime, harm, deviance and victimisation and responses to crime, harm, deviance and victimisation"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["provide"]
  about: "an account of diversity and inequality in crime and its responses"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold (third-class) level, a graduate should be able to give an account of how social diversity and inequality shape crime, harm, deviance and victimisation and the ways societies respond to them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 58230, end: 58427 }
  source: "provide a critical understanding of social diversity and inequality and their effects in relation to crime, harm, deviance and victimisation and responses to crime, harm, deviance and victimisation"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["provide"]
  about: "critical understanding of diversity and inequality in crime and its responses"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b7, basis: stated }
  paraphrase: "At the typical (2:2 and 2:1) level, a graduate should be able to show a critical understanding of how social diversity and inequality shape crime, harm, deviance and victimisation and the ways societies respond to them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 58430, end: 58644 }
  source: "demonstrate an exceptional critical understanding of social diversity and inequality and their effects in relation to crime, harm, deviance and victimisation and responses to crime, harm, deviance and victimisation"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "exceptional critical understanding of diversity and inequality"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b8, basis: stated }
  paraphrase: "At the excellent (first-class) level, a graduate should be able to show an exceptionally critical understanding of how social diversity and inequality shape crime, harm, deviance and victimisation and the ways societies respond to them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 58647, end: 58836 }
  source: "evaluate criminal justice agency practices and developments in terms of changing values and relationships between individuals, groups, and public and private agencies in different locations"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["evaluate"]
  about: "evaluating criminal justice agency practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold (third-class) level, a graduate should be able to judge how criminal justice agencies work and change, against shifting values and relationships among people, groups and public and private bodies in different places."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b11
  locator: { number: "4.5.b11", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 58839, end: 59039 }
  source: "critically evaluate criminal justice agency practices and developments in terms of changing values and relationships between individuals, groups, and public and private agencies in different locations"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["evaluate"]
  about: "critically evaluating criminal justice agency practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b10, basis: stated }
  paraphrase: "At the typical (2:2 and 2:1) level, a graduate should be able to judge critically how criminal justice agencies work and change, against shifting values and relationships among people, groups and public and private bodies in different places."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b12
  locator: { number: "4.5.b12", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 59042, end: 59266 }
  source: "critically evaluate to an exceptional level criminal justice agency practices and developments in terms of changing values and relationships between individuals, groups, and public and private agencies in different locations"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["evaluate"]
  about: "exceptional critical evaluation of criminal justice agency practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b11, basis: stated }
  paraphrase: "At the excellent (first-class) level, a graduate should be able to judge critically, to an exceptional standard, how criminal justice agencies work and change, against shifting values and relationships among people, groups and public and private bodies in different places."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b13
  locator: { number: "4.5.b13", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 59269, end: 59503 }
  source: "examine the values, practices and processes of governance, risk management and human rights that underpin the treatment of lawbreakers within UK criminal justice systems and allied agencies which administer sentencing and alternatives"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["examine"]
  about: "examining governance, risk and rights in dealing with lawbreakers"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold (third-class) level, a graduate should be able to look into the governance, risk management and human rights values and processes that shape how UK criminal justice systems, and the agencies that run sentences and their alternatives, treat people who break the law."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b14
  locator: { number: "4.5.b14", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 59506, end: 59750 }
  source: "critically assess the values, practices and processes of governance, risk management and human rights that underpin the treatment of lawbreakers within UK criminal justice systems and allied agencies which administer sentencing and alternatives"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["assess"]
  about: "critically assessing governance, risk and rights in dealing with lawbreakers"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b13, basis: stated }
  paraphrase: "At the typical (2:2 and 2:1) level, a graduate should be able to appraise critically the governance, risk management and human rights values and processes that shape how UK criminal justice systems, and the agencies that run sentences and their alternatives, treat people who break the law."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b15
  locator: { number: "4.5.b15", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 59753, end: 60026 }
  source: "demonstrate exceptional critical assessment of the values, practices and processes of governance, risk management and human rights that underpin the treatment of lawbreakers within UK criminal justice systems and allied agencies which administer sentencing and alternatives"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "exceptional critical assessment of governance, risk and rights"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b14, basis: stated }
  paraphrase: "At the excellent (first-class) level, a graduate should be able to give an exceptionally critical appraisal of the governance, risk management and human rights values and processes that shape how UK criminal justice systems, and the agencies that run sentences and their alternatives, treat people who break the law."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b16
  locator: { number: "4.5.b16", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 60117, end: 60222 }
  source: "apply conceptions of human rights in order to evaluate efforts to prevent harm and ensure personal safety"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["apply", "evaluate"]
  about: "applying human rights to judge harm prevention"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold (third-class) level, a graduate should be able to use ideas of human rights to judge efforts to prevent harm and keep people safe."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b17
  locator: { number: "4.5.b17", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 60225, end: 60381 }
  source: "provide a critical understanding of and apply conceptions of human rights in order to critically evaluate efforts to prevent harm and ensure personal safety"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["provide", "apply", "evaluate"]
  about: "critical use of human rights to judge harm prevention"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b16, basis: stated }
  paraphrase: "At the typical (2:2 and 2:1) level, a graduate should be able to understand ideas of human rights critically and use them to judge, critically, efforts to prevent harm and keep people safe."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b18
  locator: { number: "4.5.b18", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 60384, end: 60562 }
  source: "provide an exceptional critical understanding of and application of conceptions of human rights in order to critically evaluate efforts to prevent harm and ensure personal safety"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["provide", "evaluate"]
  about: "exceptional critical use of human rights to judge harm prevention"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b17, basis: stated }
  paraphrase: "At the excellent (first-class) level, a graduate should be able to show an exceptionally critical understanding and use of ideas of human rights, judging critically efforts to prevent harm and keep people safe."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b19
  locator: { number: "4.5.b19", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 60565, end: 60721 }
  source: "use a range of research strategies and methods, assess the appropriateness of their use, and identify an appropriate strategy for specific research problems"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["use", "assess", "identify"]
  about: "using and choosing research strategies and methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold (third-class) level, a graduate should be able to use a variety of research strategies and methods, judge when each fits and choose a suitable strategy for a given research problem."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b20
  locator: { number: "4.5.b20", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 60724, end: 60891 }
  source: "use a range of research strategies and methods, critically assess the appropriateness of their use, and identify an appropriate strategy for specific research problems"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["use", "assess", "identify"]
  about: "critically choosing research strategies and methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b19, basis: stated }
  paraphrase: "At the typical (2:2 and 2:1) level, a graduate should be able to use a variety of research strategies and methods, judge critically when each fits and choose a suitable strategy for a given research problem."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b21
  locator: { number: "4.5.b21", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 60894, end: 61110 }
  source: "accurately use a range of research strategies and methods, provide exceptional critical assessment of the appropriateness of their use, and consistently identify an appropriate strategy for specific research problems"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["use", "provide", "identify"]
  about: "accurate, exceptional choice of research strategies and methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b20, basis: stated }
  paraphrase: "At the excellent (first-class) level, a graduate should be able to use a variety of research strategies and methods accurately, appraise to an exceptional standard when each fits and choose a suitable strategy for a given research problem every time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b22
  locator: { number: "4.5.b22", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 61113, end: 61283 }
  source: "evaluate strengths and weaknesses in the use of comparison in relation to crime, harm, deviance and victimisation and responses to crime, harm, deviance and victimisation"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["evaluate"]
  about: "evaluating the use of comparison"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold (third-class) level, a graduate should be able to judge the strengths and weaknesses of comparative approaches to crime, harm, deviance and victimisation and to how societies deal with them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b23
  locator: { number: "4.5.b23", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 61286, end: 61467 }
  source: "critically evaluate strengths and weaknesses in the use of comparison in relation to crime, harm, deviance and victimisation and responses to crime, harm, deviance and victimisation"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["evaluate"]
  about: "critically evaluating the use of comparison"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b22, basis: stated }
  paraphrase: "At the typical (2:2 and 2:1) level, a graduate should be able to judge critically the strengths and weaknesses of comparative approaches to crime, harm, deviance and victimisation and to how societies deal with them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b24
  locator: { number: "4.5.b24", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 61470, end: 61675 }
  source: "critically evaluate to an exceptional level strengths and weaknesses in the use of comparison in relation to crime, harm, deviance and victimisation and responses to crime, harm, deviance and victimisation"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["evaluate"]
  about: "exceptional critical evaluation of comparison"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b23, basis: stated }
  paraphrase: "At the excellent (first-class) level, a graduate should be able to judge critically, to an exceptional standard, the strengths and weaknesses of comparative approaches to crime, harm, deviance and victimisation and to how societies deal with them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b25
  locator: { number: "4.5.b25", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 61678, end: 61902 }
  source: "summarise and analyse quantitative and qualitative empirical data about crime, harm, deviance and victimisation and responses to crime, harm, deviance and victimisation, in order to evaluate competing criminological theories"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["summarise", "analyse", "evaluate"]
  about: "summarising and analysing data to weigh theories"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold (third-class) level, a graduate should be able to summarise and analyse quantitative and qualitative evidence on crime, harm, deviance, victimisation and how societies respond, so as to weigh rival criminological theories."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b26
  locator: { number: "4.5.b26", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 61905, end: 62151 }
  source: "summarise and critically analyse quantitative and qualitative empirical data about crime, harm, deviance and victimisation and responses to crime, harm, deviance and victimisation, in order to critically evaluate competing criminological theories"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["summarise", "analyse", "evaluate"]
  about: "critical analysis of data to weigh theories"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b25, basis: stated }
  paraphrase: "At the typical (2:2 and 2:1) level, a graduate should be able to summarise and critically analyse quantitative and qualitative evidence on crime, harm, deviance, victimisation and how societies respond, so as to weigh rival criminological theories critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b27
  locator: { number: "4.5.b27", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 62154, end: 62420 }
  source: "provide exceptional summary and critical analysis of quantitative and qualitative empirical data about crime, harm, deviance and victimisation and responses to crime, harm, deviance and victimisation, in order to critically evaluate competing criminological theories"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["provide", "evaluate"]
  about: "exceptional summary and critical analysis of data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b26, basis: stated }
  paraphrase: "At the excellent (first-class) level, a graduate should be able to summarise and critically analyse, to an exceptional standard, quantitative and qualitative evidence on crime, harm, deviance, victimisation and how societies respond, weighing rival theories critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b28
  locator: { number: "4.5.b28", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 62511, end: 62658 }
  source: "explain and evaluate complex social problems in terms of criminological theories of crime, class, victimisation and responses to crime and deviance"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["explain", "evaluate"]
  about: "explaining and evaluating complex social problems"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold (third-class) level, a graduate should be able to explain and judge complex social problems using criminological theories about crime, social class, victimisation and how societies respond to crime and deviance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b29
  locator: { number: "4.5.b29", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 62661, end: 62819 }
  source: "explain and critically evaluate complex social problems in terms of criminological theories of crime, class, victimisation and responses to crime and deviance"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["explain", "evaluate"]
  about: "explaining and critically evaluating complex social problems"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b28, basis: stated }
  paraphrase: "At the typical (2:2 and 2:1) level, a graduate should be able to explain and judge critically complex social problems using criminological theories about crime, social class, victimisation and how societies respond to crime and deviance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b30
  locator: { number: "4.5.b30", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 62822, end: 63007 }
  source: "provide exceptional critical explanation and evaluation of complex social problems in terms of criminological theories of crime, class, victimisation and responses to crime and deviance"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["provide"]
  about: "exceptional critical explanation of complex social problems"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b29, basis: stated }
  paraphrase: "At the excellent (first-class) level, a graduate should be able to explain and judge critically, to an exceptional standard, complex social problems using criminological theories about crime, social class, victimisation and how societies respond to crime and deviance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b31
  locator: { number: "4.5.b31", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 63010, end: 63114 }
  source: "analyse ways in which the subject of criminology can be distinguished from other forms of understanding."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["analyse"]
  about: "analysing how criminology differs from other understandings"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold (third-class) level, a graduate should be able to analyse how criminology differs from other ways of understanding crime and society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b32
  locator: { number: "4.5.b32", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 63117, end: 63232 }
  source: "critically analyse ways in which the subject of criminology can be distinguished from other forms of understanding."
  stem: "4.5"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["analyse"]
  about: "critically analysing how criminology differs from other understandings"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b31, basis: stated }
  paraphrase: "At the typical (2:2 and 2:1) level, a graduate should be able to analyse critically how criminology differs from other ways of understanding crime and society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.5.b33
  locator: { number: "4.5.b33", headingPath: ["Benchmark standards", "Criminology subject-specific expectations"] }
  span: { start: 63235, end: 63376 }
  source: "demonstrate exceptional critical analysis of ways in which the subject of criminology can be distinguished from other forms of understanding."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "exceptional critical analysis of what sets criminology apart"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/criminology-2022/4.5.b32, basis: stated }
  paraphrase: "At the excellent (first-class) level, a graduate should be able to show an exceptionally critical analysis of how criminology differs from other ways of understanding crime and society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Benchmark standard for postgraduate degrees"] }
  span: { start: 63665, end: 63773 }
  source: "a systematic understanding and critical awareness of topics which are informed by the subject of criminology"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in criminology"
  addressee: learner
  verbs: ["informed"]
  about: "systematic understanding of criminological topics"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Beyond the honours outcomes, a master's graduate should be able to show systematic understanding of, and critical awareness about, topics shaped by criminology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Benchmark standard for postgraduate degrees"] }
  span: { start: 63776, end: 63935 }
  source: "a critical awareness of the history of ideas, the cultural context, and the social and political theories that inform and influence the practice of criminology"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in criminology"
  addressee: learner
  verbs: ["inform", "influence"]
  about: "history of ideas and social and political theory"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Beyond the honours outcomes, a master's graduate should be able to show critical awareness of how ideas developed over time, their cultural setting and the social and political theories that shape criminological practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Benchmark standard for postgraduate degrees"] }
  span: { start: 63938, end: 64090 }
  source: "a critical awareness of the intersectionality of power in relation to criminal justice agencies and responses to crime, harm, deviance and victimisation"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in criminology"
  addressee: learner
  verbs: []
  about: "the intersectionality of power"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Beyond the honours outcomes, a master's graduate should be able to show critical awareness of how intersecting forms of power bear on criminal justice agencies and on responses to crime, harm, deviance and victimisation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Benchmark standard for postgraduate degrees"] }
  span: { start: 64093, end: 64216 }
  source: "an ability to identify appropriate methodologies for dealing with complex problems and to design their own research project"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in criminology"
  addressee: learner
  verbs: ["identify", "dealing", "design"]
  about: "methodologies and an own research design"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Beyond the honours outcomes, a master's graduate should be able to pick suitable methodologies for complex problems and design an original research project."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Benchmark standard for postgraduate degrees"] }
  span: { start: 64219, end: 64343 }
  source: "an ability to develop critical discussion and analysis of complex concepts, and work independently and with some originality"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in criminology"
  addressee: learner
  verbs: ["develop", "work"]
  about: "critical discussion, independence and originality"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Beyond the honours outcomes, a master's graduate should be able to carry critical discussion and analysis of complex ideas forward and work independently with some originality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/criminology-2022/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Benchmark standard for postgraduate degrees"] }
  span: { start: 64346, end: 64524 }
  source: "an ability to successf ully complete a substantial empirical research project, systematic review or systematic case study, informed by wide current understandings in the subject."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "holders of a master's degree in criminology"
  addressee: learner
  verbs: ["complete"]
  about: "a substantial research project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Beyond the honours outcomes, a master's graduate should be able to complete a substantial empirical project, systematic review or systematic case study grounded in broad current understanding of the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/criminology-2022/1.10
  forPractitioner: { text: "Embed the study of equality, diversity and inclusion in every part of the curriculum, not one module, and make design and delivery inclusive; staff share a duty to practise inclusion, and equality law applies to students and staff alike.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty (the issuer's 'must') on the course provider, not a standard students are assessed against: equality, diversity and inclusion must be studied throughout the curriculum and built into how courses are designed and taught. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.10, and do not call it a regulatory requirement. Set it beside paras 1.11 to 1.13 (the other inclusion duties), para 3.6 item d and spine:6."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team reviews where equality, diversity and inclusion sit in the curriculum. Frame it as a duty of the course and ask: 'Where in each year do students study equality, diversity and inclusion, and how is delivery itself made inclusive?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/1.11
  forPractitioner: { text: "Build equality and diversity into the planning and design stage through learning design: equity in course evaluation, safe settings for discussion, student input to assessment and delivery and a curriculum that is flexible, accessible and offered in several modes.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty (the issuer's 'must') on the course provider, not a standard students are assessed against: equality and diversity must be designed into courses from the planning stage. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.11, and do not call it a regulatory requirement. Set it beside paras 1.10 and 1.12, para 2.18 (accessibility) and spine:6."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team plans or redesigns a course or module. Frame it as a duty of the course and ask: 'At what point in your design process do you test the course for equity, and which students have a say in it?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/1.12
  forPractitioner: { text: "Plan for belonging at each stage: students must feel their experience is an asset, not a barrier. Support open discussion of sensitive and controversial topics safely, help students see how their experience shapes their views and widen engagement with outside communities at undergraduate and postgraduate levels.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty (the issuer's 'must') on the course provider, not a standard students are assessed against: students must be helped to feel they belong, with safe, respectful dialogue on sensitive topics at every stage. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.12, and do not call it a regulatory requirement. Set it beside paras 1.11 and 1.13 and para 3.6 item d (distressing content)."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team discusses belonging, retention or how sensitive topics are taught. Frame it as a duty of the course and ask: 'How do students on your course learn that their own experience counts, and how do you prepare them to discuss distressing material?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/1.13
  forPractitioner: { text: "Treat inclusion as part of every review: course teams must check for hidden or overt barriers that hold back particular groups and plan changes to welcome under-represented students, and should provide visible staff role models, active support and considered language.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty (the issuer's 'must') on the course provider, not a standard students are assessed against: course teams must review courses for barriers that hold back some groups and act on them. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.13, and do not call it a regulatory requirement. Set it beside paras 1.12 and 1.14, para 2.31 (monitoring and review) and para 3.8 (monitoring outcomes by protected characteristics)."
  author-agent-dialogue: "Raise this with a programme team or teacher when a course team prepares a periodic or annual review. Frame it as a duty of the course and ask: 'Which groups of your students do less well, and what in the course might explain it?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/1.14
  forPractitioner: { text: "Pay deliberate attention to under-represented groups across recruitment, marketing, teaching and career support through to after graduation, so that inclusive practice is visible to students and to the outside world.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: under-represented groups should receive more attention at every stage, from recruitment to after graduation. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.14, and do not call it a regulatory requirement. Set it beside para 1.13 and para 2.17 (entry routes)."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team looks at recruitment, widening participation or graduate outcomes. Frame it as a duty of the course and ask: 'Which under-represented groups do you reach at recruitment, and do you follow them through to graduate outcomes?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/1.15
  forPractitioner: { text: "Judge a course's sustainability by more than recruitment: keep the curriculum current, bringing in emerging approaches such as green, queer and southern criminology, indigenous knowledge and zemiology.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: course sustainability should be judged by a current curriculum, not only by recruitment. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.15, and do not call it a regulatory requirement. Set it beside para 1.16 (green criminology) and para 1.17."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team reviews curriculum currency or a course's viability. Frame it as a duty of the course and ask: 'Which emerging approaches in criminology does your curriculum cover, and when was that last reviewed?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/1.16
  forPractitioner: { text: "Consider green criminology when designing the curriculum: crimes against the environment, ecological justice and environmental law, including individual, corporate and state failings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: curriculum design should take account of green criminology. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.16, and do not call it a regulatory requirement. Set it beside para 1.15 and paras 1.19 to 1.21 (education for sustainable development)."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team decides what the curriculum covers on environmental harm. Frame it as a duty of the course and ask: 'Where, if anywhere, do students meet green criminology on your course?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/1.17
  forPractitioner: { text: "Link theory to practice through work with criminal justice agencies, practitioners and other sectors; aim for a curriculum that anticipates problems rather than reacting, and consider innovation in concepts, practice and pedagogy when developing courses.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: the discipline should aim to be proactive and work with justice agencies and practitioners. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.17, and do not call it a regulatory requirement. Set it beside paras 1.22 and 1.27 and paras 2.26 to 2.30 (partnership)."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team plans partnerships or practice links. Frame it as a duty of the course and ask: 'Which agencies or practitioners shape your curriculum now, and how?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/1.18
  forPractitioner: { text: "Consider ethics at each stage of developing, updating and reviewing a course, and plan how emotive topics will be taught with care for equality, openness, impartiality and accessibility.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: ethics should be considered whenever courses are developed, updated or reviewed. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.18, and do not call it a regulatory requirement. Set it beside paras 2.12 to 2.16 (research ethics) and para 3.6 item d."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team reviews how ethics and emotive topics are handled. Frame it as a duty of the course and ask: 'How does your course review check the treatment of ethics and of emotive topics?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/1.20
  forPractitioner: { text: "Let criminology's multidisciplinary nature guide curriculum and teaching methods, so that students learn to see critically how culture, the economy, the environment and globalisation interlock.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: the subject's multidisciplinary nature should guide curriculum and teaching. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.20, and do not call it a regulatory requirement. Set it beside paras 1.19 and 1.21 and the ESD guidance std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team discusses how sustainability enters teaching. Frame it as a duty of the course and ask: 'Where does your course ask students to connect culture, economy, environment and globalisation?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/1.21
  forPractitioner: { text: "Offer content on poverty, social justice and environmental and social harms, so that students gain awareness of sustainable development and global citizenship and the skills to address such concerns.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: courses should offer content that builds awareness of sustainable development and global citizenship. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.21, and do not call it a regulatory requirement. Set it beside paras 1.19 and 1.20 and the ESD guidance std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team maps sustainable development in the curriculum. Frame it as a duty of the course and ask: 'Which modules address poverty, social justice or environmental harm, and how is that assessed?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/1.22
  forPractitioner: { text: "Where possible, encourage volunteering and work placements connected with sustainability, and consider building service and work-based learning into modules.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: students should be encouraged, where possible, to volunteer or take placements linked to sustainability. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.22, and do not call it a regulatory requirement. Set it beside para 1.27 (employability opportunities) and para 2.30 (educational partnerships)."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team plans placements, volunteering or applied learning. Frame it as a duty of the course and ask: 'What volunteering or placement routes can your students take, and are any linked to sustainability?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/1.24
  forPractitioner: { text: "Plan for honours students to develop methodological understanding, including the link between theory and methods and specialist knowledge of the roles and practices of criminal justice agencies.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to build the skills to understand research methods and their principles, including how theory and methods connect, and to learn in some depth what criminal justice agencies do and how.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a stated expectation worded with 'expected' or 'important', which is not one of the five force words for honours students: skills for understanding methodological concepts and principles. It holds for the honours award, at FHEQ level 6 and FQHEIS level 10. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.24; do not claim it is a rung or a regulatory standard. Set it beside para 2.1 (the same expectation), the rung cells 4.5.b19 to 4.5.b21 (research strategies), qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Bring this up when a student asks why methods matter in a criminology degree. Put it in plain words, in the second person for a student and as a question of course design for staff. Ask: 'How would you explain the link between a theory you know and the method you would use to test it?' Avoid reading the paragraph aloud at length."
- statement: qaa/criminology-2022/1.27
  forPractitioner: { text: "Offer employability opportunities at a fitting point in the course, inside or outside the formal curriculum, with safeguards against exploitation and harassment and attention to accessibility and reasonable adjustments on placements.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: courses should offer chances to build employability skills at a fitting point. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 1.27, and do not call it a regulatory requirement. Set it beside para 1.22, para 2.18 (reasonable adjustments) and para 2.30."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team plans employability, placements or guest teaching. Frame it as a duty of the course and ask: 'At what point in the course do students meet employability activity, and how are they protected on placement?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/2.1
  forPractitioner: { text: "Design the research methods strand so that students build an understanding of methodological concepts and of the relationship between theory, evidence and methods.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Research and critical enquiry are at the heart of criminology, so you are expected to build the skills to understand research methods, including how theory, evidence and methods fit together.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a stated expectation worded with 'expected' or 'important', which is not one of the five force words for students across the honours degree (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.1. Do not claim it is a rung on its own; the rungs for research philosophy follow in paras 2.2 and 2.3. Set it beside para 1.24, paras 2.2 to 2.4, qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Bring this up when a student or team asks what the methods strand is for. Put it in plain words, in the second person for a student and as a question of course design for staff. Ask: 'How do theory, evidence and method fit together in a study you have read?' Avoid reading the paragraph aloud at length."
- statement: qaa/criminology-2022/2.2
  forPractitioner: { text: "By threshold, students should grasp the philosophy of explanation; ontology and epistemology; the qualitative-quantitative distinction, with mixed methods; inductive and deductive reasoning. They should also be able to match methods of data collection and analysis to research questions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should understand the debates about how criminological research explains things, the difference between qualitative and quantitative research, including ways of mixing them; you should also be able to pick methods that suit a research question.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the research-philosophy expectation the issuer sets jointly for the threshold and typical rungs of the honours degree (FHEQ level 6, FQHEIS level 10), worded as 'expected to' with a 'should' for choosing methods. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.2. Do not claim it applies to master's study or that it is regulatory. Set it beside the excellent paragraph 2.3, the table row 4.5.b19 to 4.5.b21, qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student struggles to justify a research design or asks what ontology and epistemology have to do with them. Put it plainly as knowing why you chose your methods; with staff, frame it as the floor the methods teaching must secure. Ask: 'Is your question better answered with numbers, with accounts or with both, and why?' Do not read the paragraph aloud or present the excellent expectations in 2.3 as the minimum."
- statement: qaa/criminology-2022/2.2.typical
  forPractitioner: { text: "At the typical level, expect the same grasp of research philosophy and strategy as at threshold, shown more securely; most students should be able to justify their choice of methods for a question.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you should understand the debates about explanation in criminological research and the main research strategies; you should also be able to explain clearly why a method suits your question.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical-rung reading of a paragraph the issuer sets jointly for threshold and typical in the honours degree (FHEQ level 6, FQHEIS level 10); the wording does not change between the two rungs. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.2. Do not invent a separate typical standard or present it as the minimum. Set it beside the threshold record 2.2, the excellent paragraph 2.3 and Annex D's cognitive cells qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise this when a student working at second-class level asks how to strengthen a methods section. Put it in plain words as justifying your design securely; with staff, use it to check the middle bands. Ask: 'Could you defend your choice of method against someone who prefers the other approach?' Do not present it as the pass threshold, and do not read the paragraph out."
- statement: qaa/criminology-2022/2.3
  forPractitioner: { text: "At first-class level, students should go beyond discussing theory and method: they critique and apply criminological concepts in research design, critique the philosophy of explanation in studies and weigh the ethics of methods and the politics of interpreting findings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you should be able to critique how criminological studies explain things, use criminological ideas to design research and see the ethical side of your methods and the political side of how findings are read.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent-rung expectation for research philosophy in the honours degree (FHEQ level 6, FQHEIS level 10): an aspiration that marks first-class work, worded with 'should'. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.3. Do not present it as required for the award or as a master's standard (para 2.4 covers postgraduate study). Set it beside para 2.2, the excellent cell 4.5.b21 and Annex D's first-class cell qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise this when a student aiming for a first asks how to make a methods discussion stand out. Put it as an aspiration in plain words; with staff, use it to describe the top band. Ask: 'What does your design assume about how crime can be known, and what is at stake politically in how your data are read?' Never present it as what every student must reach."
- statement: qaa/criminology-2022/2.4
  forPractitioner: { text: "At postgraduate level, expect students to critique and apply concepts in research design, engage with nuanced methodological debates and design and run criminological research in real settings with a wide repertoire of methods.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At postgraduate level, you are expected to critique and apply criminological ideas when designing research, follow subtle debates about method and design and carry out real-world research using a wide range of methods.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a stated expectation worded with 'expected' or 'important', which is not one of the five force words for postgraduate study in criminology, read as the master's degree (FHEQ level 7, FQHEIS level 11, inferred). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.4. Do not apply it to the honours degree or call it regulatory. Set it beside the master's outcomes 4.6.b4 and 4.6.b6, qaa/fheq-2024/4.17.b2 and spine:7."
  author-agent-dialogue: "Raise this with master's students or a postgraduate team when research design or a dissertation plan is discussed. Put it plainly as designing and running real-world research with a wide choice of methods. Ask: 'Which debates about method bear on your project, and how will you answer them?' Do not apply it to undergraduates or read the paragraph aloud."
- statement: qaa/criminology-2022/2.5
  forPractitioner: { text: "In early methods teaching, cover forming a research question, designing a study and reflecting on design and practice, with explicit attention to positionality and power, across qualitative and quantitative traditions.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Early on, you are expected to learn how to form a research question, design a study and reflect on your research, thinking about your own position and the power differences involved.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a stated expectation worded with 'expected' or 'important', which is not one of the five force words for the early, basic stage of the honours degree, on the route to FHEQ level 6. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.5. Do not present 'basic level' as a framework level or claim it is regulatory. Set it beside paras 2.6 and 2.8 (basic qualitative and quantitative methods), the cell 4.5.b19 and spine:6."
  author-agent-dialogue: "Raise this when a student starts planning a first project or asks what positionality means. Put it plainly as learning to ask a good question and to think about your own place in the research. Ask: 'How might who you are affect what participants tell you?' Avoid reading the paragraph aloud at length."
- statement: qaa/criminology-2022/2.6
  forPractitioner: { text: "Introduce the main qualitative approaches early, choosing from a broad menu that includes interviewing, focus groups, observation, ethnography (virtual too), participatory and decolonising methods, documentary, visual and internet research, sampling and the limits of interpretation.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Early on, you are expected to know the main qualitative approaches, such as interviews, focus groups, observation and ethnography, and how qualitative data are sampled, organised and interpreted.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a stated expectation worded with 'expected' or 'important', which is not one of the five force words: basic knowledge of qualitative approaches in the honours degree, with an illustrative list, not a required syllabus. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.6. Do not claim each listed method must be taught or assessed. Set it beside para 2.7 (more advanced qualitative techniques), para 2.8 (basic quantitative methods) and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise this when a team plans the qualitative methods strand or a student asks which methods they should know. Put it plainly as knowing the main options and when each is used. Ask: 'Which two qualitative approaches could answer your question, and what would each miss?' Do not present the list as a checklist every student must master."
- statement: qaa/criminology-2022/2.7
  forPractitioner: { text: "In later years, give students the chance to know and possibly use techniques for coding, analysing and interpreting qualitative data, with software such as ATLAS.ti or NVivo.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Later in your studies, you would be expected to know, and perhaps use, some techniques for coding, analysing and interpreting qualitative data, possibly with software such as NVivo.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a hedged expectation ('would be expected to', 'some of', 'possible use') for the later stages of the honours degree, not a requirement to use every technique. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.7. Do not claim that software use is required. Set it beside para 2.6, para 2.9 (advanced quantitative techniques) and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise this when a student is choosing how to analyse interview or text data. Put it plainly as knowing how qualitative data are coded and interpreted. Ask: 'How will you move from your transcripts to findings you can defend?' Do not suggest that particular software is compulsory."
- statement: qaa/criminology-2022/2.8
  forPractitioner: { text: "Introduce basic quantitative techniques early, drawing on a menu such as questionnaire design, survey sampling, experimental design and trials, statistical software (for example SPSS or R), comparing means, correlation versus causation, secondary data and basic statistical tests.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Early on, you are expected to know some basic quantitative techniques, such as designing a questionnaire, sampling, using statistics software, telling correlation from causation and running simple statistical tests.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a stated expectation worded with 'expected' or 'important', which is not one of the five force words: basic quantitative knowledge in the honours degree, with an illustrative list of techniques. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.8. Do not claim every technique listed must be taught. Set it beside para 2.9 (advanced quantitative techniques), the cells 4.5.b25 to 4.5.b27 (analysing empirical data) and Annex D's qaa/fheq-2024/annex-d/transferable/r1/3rd (numeracy)."
  author-agent-dialogue: "Raise this when a student is anxious about statistics or a team plans the quantitative strand. Put it plainly as the basic tools for working with numbers about crime. Ask: 'Can you explain why a link between two figures does not show that one causes the other?' Do not present the list as a test everyone must pass item by item."
- statement: qaa/criminology-2022/2.9
  forPractitioner: { text: "In later years, offer some advanced quantitative techniques, such as t-tests, ANOVA, multivariate analysis, systematic reviewing, big and secondary data, mapping, data visualisation and analysis of social media data.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Later in your studies, you would be expected to know, and perhaps use, some advanced quantitative techniques, such as t-tests, ANOVA, systematic reviews, mapping data or analysing online data.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a hedged expectation ('would be expected to', 'some of') for the later stages of the honours degree. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.9. Do not claim each technique is required. Set it beside para 2.8, para 2.10 (higher or postgraduate methods) and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise this when a student plans a quantitative dissertation or asks which tests to learn. Put it plainly as a choice of advanced tools. Ask: 'Which test suits your data and question, and what would it not tell you?' Do not treat the list as compulsory."
- statement: qaa/criminology-2022/2.10
  forPractitioner: { text: "At higher or postgraduate level, give students knowledge and understanding, and where possible practice, of computer-assisted interviewing, qualitative analysis software, systematic reviewing and virtual ethnography.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At a higher or postgraduate stage, you are expected to know and understand, and may use, methods such as computer-assisted interviewing, qualitative analysis software, systematic reviews and online ethnography.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a stated expectation worded with 'expected' or 'important', which is not one of the five force words for the higher stages of the honours degree or for postgraduate study; the issuer does not say which, so give no single framework level. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.10. Do not claim the methods must be used, only known and understood. Set it beside paras 2.7 and 2.9 and the master's outcome 4.6.b4."
  author-agent-dialogue: "Raise this when an advanced student or postgraduate asks which specialist methods to learn. Put it plainly as knowing these methods well enough to choose among them. Ask: 'Would any of these methods strengthen your project?' Do not present them as compulsory."
- statement: qaa/criminology-2022/2.11
  forPractitioner: { text: "Teach every student the basics of mixing qualitative and quantitative data (triangulation and integration), of induction, deduction and abduction and of the stages of data analysis.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should gain a basic understanding of how numerical and qualitative data can be combined, of reasoning by induction, deduction and abduction and of the stages of analysing data.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation (the issuer's 'should') for all students in criminology, at every stage; it names no framework level. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.11. Do not present it as an advanced or optional topic. Set it beside para 2.2 (mixed methods), the cells 4.5.b25 to 4.5.b27 and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise this when a student plans to use more than one kind of data. Put it plainly as knowing how different data can be brought together. Ask: 'How will you bring your survey results and interviews together, and what happens if they disagree?' Avoid reading the list of analysis stages aloud."
- statement: qaa/criminology-2022/2.12
  forPractitioner: { text: "Teach ethics at every level: what ethics means, policy frameworks, the split between individual, legal and professional ethics and the main codes (such as the British Society of Criminology's); students should show they can discuss what codes achieve and where they fall short, and know your institution's approval process.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At every stage, you are expected to know what research ethics means and the main codes criminologists use; you should be able to discuss what those codes do well and badly, and know how to get ethical approval for your own research.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation for students at all levels ('expected to', with a 'should' for discussing codes). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.12, and name the British Society of Criminology's Statement of Ethics only as the issuer's example. Do not claim a particular code is mandatory. Set it beside paras 2.13 to 2.16 and the professional cell qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Raise this when a student is preparing an ethics application or asks why codes of ethics matter. Put it plainly as knowing the rules and being able to question them. Ask: 'Which code applies to your project, and where might it not fit your situation?' Do not read the codes aloud at length."
- statement: qaa/criminology-2022/2.13
  forPractitioner: { text: "Use common ethical problems, such as distress in interviews, lack of consent and biased handling of data, to teach strategies: suitable design, informed consent, confidentiality and protocols for hard-to-reach and vulnerable groups.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to be able to think through ways of handling ethical problems in research, such as choosing a suitable design, getting informed consent, keeping things confidential and working carefully with vulnerable people.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a stated expectation worded with 'expected' or 'important', which is not one of the five force words: students can consider strategies for common ethical problems; the list is illustrative. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.13. Do not present the strategies as settled answers; para 2.14 says they are not straightforward. Set it beside paras 2.12 and 2.14."
  author-agent-dialogue: "Raise this when a student designs research with people who may be distressed or vulnerable. Put it plainly as planning how to protect participants. Ask: 'What could go wrong ethically in your study, and what will you do if it does?' Avoid reading the examples aloud."
- statement: qaa/criminology-2022/2.14
  forPractitioner: { text: "At higher and postgraduate levels, push students to see the limits of ethical strategies, such as when confidentiality has to be broken, and to know ways of minimising harm and safeguarding confidentiality.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At a higher or postgraduate stage, you are expected to see that ethical strategies are rarely simple, for example when confidentiality cannot be kept, and you should know ways to reduce harm and protect confidentiality.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation (the issuer's 'should') for the higher stages of the honours degree or for postgraduate study; the issuer does not separate the two, so give no single level. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.14. Do not claim it applies from the start of the degree. Set it beside paras 2.13 and 2.15 and qaa/fheq-2024/4.15.b4 (uncertainty and the limits of knowledge)."
  author-agent-dialogue: "Raise this when an advanced student's project touches on disclosure of harm or illegal acts. Put it plainly as knowing where your promises to participants end. Ask: 'Is there anything a participant might tell you that you could not keep confidential, and how will you tell them that in advance?' Do not read the paragraph aloud."
- statement: qaa/criminology-2022/2.15
  forPractitioner: { text: "At higher and postgraduate levels, cover debates about codes of ethics and what data protection law requires of researchers, including relevant principles and exemptions.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At a higher or postgraduate stage, you are expected to know the debates about research ethics codes and what data protection law asks of you as a researcher.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a stated expectation worded with 'expected' or 'important', which is not one of the five force words for the higher stages of the honours degree or for postgraduate study. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.15. Do not give legal advice or claim it sets out what the law requires. Set it beside paras 2.14 and 2.16."
  author-agent-dialogue: "Raise this when an advanced student handles personal data in research. Put it plainly as knowing your legal duties as a researcher. Ask: 'What personal data will you hold, and what does data protection law expect you to do with it?' Do not offer legal rulings."
- statement: qaa/criminology-2022/2.16
  forPractitioner: { text: "Make sure every student reaches a level of ethical literacy fit for keeping research participants safe and well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are expected to become ethically literate enough to keep the people in your research safe and well.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the summary expectation on research ethics for all students, a stated expectation worded with 'expected' or 'important', which is not one of the five force words. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.16. Do not define ethical literacy more tightly than the issuer does. Set it beside paras 2.12 to 2.15 and the professional cell qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Raise this when a student or team reviews readiness for fieldwork. Put it plainly as being able to keep participants safe. Ask: 'How would you know if your research was harming someone, and what would you do?' Avoid lecturing from the paragraph."
- statement: qaa/criminology-2022/2.18
  forPractitioner: { text: "Avoid a two-tier system: offer varied formats to all students, keep expectations transparent, tailor teaching and assessment where needed, consider reasonable adjustments for fieldwork, reduce hidden costs of trips and placements and give clear, accessible assessment criteria at each stage.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty (the issuer's 'must') on the course provider, not a standard students are assessed against: teaching and assessment must not split students into two tiers by need; adjustments and accessible formats are for all. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.18, and do not call it a regulatory requirement. Set it beside paras 1.11 and 1.27 and para 3.8 (adjustments to assessment)."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team reviews assessment formats, fieldwork or placement access. Frame it as a duty of the course and ask: 'Are your alternative formats open to every student, or only to those with a formal adjustment?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/2.19
  forPractitioner: { text: "Sequence the course so that core theory and study skills come first, analysis, interpretation and communication grow next and problem-solving, evaluation, reflection and self-managed learning are shown by graduation.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to start with core theory and study skills, build your analysis, interpretation and communication as you go and by the end show that you can solve problems, evaluate, reflect and manage your own learning.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a stated expectation worded with 'expected' or 'important', which is not one of the five force words about progression across the honours degree, ending in generic skills at FHEQ level 6 and FQHEIS level 10. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.19. Do not claim it sets year-by-year standards. Set it beside paras 2.20 and 2.23, qaa/fheq-2024/4.15.b5 (managing own learning), qaa/fheq-2024/4.15.b9.3 and spine:6."
  author-agent-dialogue: "Raise this when a student asks how the years of the degree build on each other. Put it plainly as a path from foundations to independent learning. Ask: 'Which of these skills feel secure now, and which do you need to build next year?' Do not read the paragraph aloud."
- statement: qaa/criminology-2022/2.20
  forPractitioner: { text: "Plan each year to move students towards the threshold subject-specific and generic skills; those finishing with a second-class degree or higher would be expected to be ready for postgraduate study.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Each year of your degree is meant to build towards the minimum skills for the award, and if you finish with a second-class degree or better you would be expected to be ready for postgraduate study.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a stated expectation worded with 'expected' or 'important', which is not one of the five force words about progress through the honours degree at FHEQ level 6 and FQHEIS level 10, which the issuer names here. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.20. Do not claim it guarantees entry to postgraduate study. Set it beside para 2.19, the threshold cells of para 4.5 (4.5.b1 onward), qaa/fheq-2024/4.15.b9.3 and spine:6."
  author-agent-dialogue: "Raise this when a student asks whether their degree prepares them for a master's. Put it plainly as what a good result opens up. Ask: 'What result are you on track for, and what would you need for the course you have in mind?' Do not promise admission or treat a second-class degree as the pass mark."
- statement: qaa/criminology-2022/2.21
  forPractitioner: { text: "In joint honours courses, students will reach the core specific and generic criminology skills; plan for the skills the other subject adds and for interdisciplinary work where the two overlap.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study criminology with another subject, you will gain the core criminology skills, add skills from your other subject and may explore where the two overlap.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a stated expectation (the issuer's 'will') for joint honours students at FHEQ level 6 and FQHEIS level 10: the core of the subject, not all of it. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.21. Do not claim joint honours students meet every single honours expectation in full. Set it beside para 1.8 (core areas for single and joint honours) and the threshold cells of para 4.5."
  author-agent-dialogue: "Raise this when a joint honours student asks how their degree compares with single honours. Put it plainly as the core of criminology plus your other subject. Ask: 'Where do your two subjects meet, and could your project sit there?' Avoid reading the paragraph aloud."
- statement: qaa/criminology-2022/2.23
  forPractitioner: { text: "Increase specialisation as students progress: higher levels should deepen analysis and critique, core and optional modules will let students focus and an assessed independent project, empirical, policy-based or theoretical, normally comes near the end.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: higher levels of study should deepen students' analytical and critical skills, with independent work near the end. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.23, and do not call it a regulatory requirement. Set it beside paras 2.19 and 2.25 (independent research) and qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team designs later-year modules or the dissertation. Frame it as a duty of the course and ask: 'How does your final year let students specialise and produce an independent piece of work?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/2.25
  forPractitioner: { text: "Where the course includes a project or dissertation, prepare students to reflect critically on its risks and its moral and ethical issues before they start.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Most courses ask you to carry out independent research, such as a dissertation, near the end; you need to reflect maturely and critically on its risks and its ethical issues.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the issuer's description of a common requirement in most courses, not a rule for every course; its 'requirement' and 'needed' are recorded as describes. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.25. Do not claim every criminology degree must include a dissertation. Set it beside paras 2.16 and 2.23, the master's outcome 4.6.b6 and qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise this when a student plans a dissertation or project. Put it plainly as thinking through the risks before you begin. Ask: 'What are the moral and ethical risks of your project, to others and to you?' Do not tell a student that every course must include a dissertation."
- statement: qaa/criminology-2022/2.32
  forPractitioner: { text: "Include external reviewers in periodic review so that proposed changes get an outside view and threshold standards and subject content are checked.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a stated expectation (the issuer's 'will') on the course provider, not a standard students are assessed against: providers will use external reviewers in periodic review to check threshold standards and content. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 2.32, and do not call it a regulatory requirement. Set it beside para 2.31, para 2.33 (external examiners) and para 4.1."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team prepares for periodic review. Frame it as a duty of the course and ask: 'Who will act as your external reviewer, and which threshold standards will they check against?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/3.5
  forPractitioner: { text: "Check that every learning resource, printed, online or streamed, is accessible to all students in every mode of study.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a stated expectation worded with 'expected' or 'important', which is not one of the five force words on the course provider, not a standard students are assessed against: learning materials need to be accessible (the issuer calls this important, not one of the five force words). It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 3.5, and do not call it a regulatory requirement. Set it beside paras 1.11 and 2.18."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team selects or reviews learning resources. Frame it as a duty of the course and ask: 'How do you check that online and streamed materials are accessible to every student?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/3.6.b1
  forPractitioner: { text: "Make criminological theory a foundational, core strand of the degree, and give students repeated practice moving between abstract theory and concrete evidence.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a stated expectation worded with 'expected' or 'important', which is not one of the five force words on the course provider, not a standard students are assessed against: criminological theory is expected to be a core, foundational part of every criminology degree. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 3.6, item a, and do not call it a regulatory requirement. Set it beside the rung row 4.5.b1 to 4.5.b3 (concepts and theories), para 3.2 and spine:6."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team decides how much theory the course carries. Frame it as a duty of the course and ask: 'Where in each year do students move between theory and evidence?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/3.6.b2
  forPractitioner: { text: "Students must weigh competing interpretations against evidence, logic, fit with other findings and explanatory power; give them repeated chances to rehearse and revise their own positions.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are required to weigh rival explanations of the same evidence, judging them by how well they fit the evidence and other findings, how logical they are and how much they explain, and to test and revise your own ideas.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a requirement on students ('required', recorded as must) in the honours degree at FHEQ level 6 and FQHEIS level 10. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 3.6, item b. Do not claim it sets a mark or a rung. Set it beside the rung row 4.5.b25 to 4.5.b27 (weighing competing theories), qaa/fheq-2024/4.15.b7 and Annex D's qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise this when a student presents one theory as the obvious answer. Put it plainly as weighing explanations against each other. Ask: 'What would a rival theory make of the same evidence, and which explanation fits better and why?' Avoid reading the paragraph aloud."
- statement: qaa/criminology-2022/3.6.b3
  forPractitioner: { text: "Design learning, teaching and assessment so that students engage with live social and political disputes, reflect on their own values and apply criminological knowledge to current crime problems.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: learning, teaching and assessment should let students engage with live disputes and apply criminological knowledge to current problems. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 3.6, item c, and do not call it a regulatory requirement. Set it beside para 1.8 (a reflective approach and own values), the rung row 4.5.b10 to 4.5.b12 and qaa/fheq-2024/4.15.b3.1."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team plans assessment on contemporary crime problems. Frame it as a duty of the course and ask: 'Which assessments ask students to apply criminology to a live public dispute?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/3.6.b4
  forPractitioner: { text: "Use flexible, varied teaching and assessment so all students have as equal a chance as possible, design for inclusion so alternative assessment is rarely needed and plan for the emotional impact of distressing material.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: teaching and assessment should be inclusive by design, and staff should recognise the impact of distressing content. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 3.6, item d, and do not call it a regulatory requirement. Set it beside paras 1.12, 2.18 and 3.8."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team designs assessment or plans teaching of distressing topics. Frame it as a duty of the course and ask: 'How do you prepare and support students before they study distressing material?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/3.8
  forPractitioner: { text: "Monitor student outcomes, including by protected characteristics, to find unintended differences, reflect on assessment strategies and make reasonable adjustments to assessment where needed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: course teams should monitor outcomes, including by protected characteristics, and reflect on assessment. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 3.8, and do not call it a regulatory requirement. Set it beside paras 1.13, 2.18 and 3.9."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team reviews assessment results or an awarding gap. Frame it as a duty of the course and ask: 'Do you break down your assessment outcomes by protected characteristics, and what have you changed as a result?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/3.10
  forPractitioner: { text: "Scaffold modules so each builds on what students learned before, year on year.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: modules should be scaffolded so students build on earlier learning. It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 3.10, and do not call it a regulatory requirement. Set it beside paras 2.19 and 3.9 and spine:6."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team maps modules across the years. Frame it as a duty of the course and ask: 'Which earlier module does each final-year module build on?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/4.2
  forPractitioner: { text: "Design curricula so that students can reach the required outcomes and show honours-level learning; every class of degree, a third included, means level 6 (FHEQ) or level 10 (FQHEIS) has been met.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (the issuer's 'should') on the course provider, not a standard students are assessed against: curricula should let students achieve the required outcomes and show the characteristics of FHEQ level 6 (FQHEIS level 10). It applies to criminology courses at honours degree level and above where the issuer says so. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.2, and do not call it a regulatory requirement. Set it beside paras 4.1, 4.4 and 4.5, the honours descriptor qaa/fheq-2024/4.15 and spine:6."
  author-agent-dialogue: "Raise this with a programme team or teacher when a team checks that module outcomes add up to the honours level. Frame it as a duty of the course and ask: 'Can you show where each honours-level outcome is assessed?' Do not put it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/criminology-2022/4.5.b1
  forPractitioner: { text: "At threshold, set teaching and assessment so that every honours graduate can set out and look closely at the main concepts and theories of criminology, and judge how well they work when applied; this is the minimum for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should be able to set out and look closely at the main concepts and theories of criminology, and judge how well they work when applied.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold outcome on key concepts and theories: the minimum every honours graduate in criminology is expected to show, at third-class level (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, threshold column, row 1. Do not call it a regulatory requirement or apply it to master's study. Set it beside the typical cell 4.5.b2, the excellent cell 4.5.b3, the honours descriptor qaa/fheq-2024/4.15.b1, Annex D's cell qaa/fheq-2024/annex-d/knowledge/r2/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks what passing with honours means for key concepts and theories, or when a team checks that a module secures the minimum. Tell a student in plain words what you need to be able to do; with staff, frame it as the floor every assessment route must reach. Ask: 'Which criminological theory can you explain well, and where does it work less well in practice?' Do not read the cell out at length or treat the typical or excellent cell as the pass mark."
- statement: qaa/criminology-2022/4.5.b2
  forPractitioner: { text: "At the typical level (2:2 and 2:1), most graduates should be able to set out and critically interrogate the main concepts and theories of criminology, and judge how well they work when applied; design assessment so they can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you should be able to set out and critically interrogate the main concepts and theories of criminology, and judge how well they work when applied.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical outcome on key concepts and theories: what most honours graduates in criminology should reach at lower or upper second-class level (FHEQ level 6, FQHEIS level 10), not the minimum. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, typical column, row 1. Do not present it as a pass requirement or as a regulatory standard. Set it beside the threshold cell 4.5.b1, the excellent cell 4.5.b3, the honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise this when a student wants to know what a good second-class answer on key concepts and theories looks like, or when staff calibrate marking. Explain it in plain words as the usual standard, above the minimum; with staff, use it to describe the middle bands. Ask: 'Which criminological theory can you explain well, and where does it work less well in practice?' and 'Where is your work more descriptive than critical?' Do not present it as the minimum needed to pass."
- statement: qaa/criminology-2022/4.5.b3
  forPractitioner: { text: "At the excellent level (first class), graduates should be able to set out and critically interrogate, to an exceptional standard, the main concepts and theories of criminology, and judge how well they work when applied; design assessment with room to show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you should be able to set out and critically interrogate, to an exceptional standard, the main concepts and theories of criminology, and judge how well they work when applied.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent outcome on key concepts and theories: an aspiration that marks first-class work in an honours degree in criminology (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, excellent column, row 1. Do not present it as required for the award or as a master's standard. Set it beside the typical cell 4.5.b2, the threshold cell 4.5.b1, the honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's first-class cell qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise this when a student aims for a first or asks how to stretch their work on key concepts and theories. Put it as an aspiration in plain words; with staff, use it to describe what lifts work into the top band. Ask: 'Which criminological theory can you explain well, and where does it work less well in practice?' and 'What would make your analysis exceptional rather than sound?' Never present it as what everyone must reach."
- statement: qaa/criminology-2022/4.5.b4
  forPractitioner: { text: "At threshold, set teaching and assessment so that every honours graduate can weigh up, using criminological theory, the political and social processes by which people are victimised and criminalised; this is the minimum for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should be able to weigh up, using criminological theory, the political and social processes by which people are victimised and criminalised.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold outcome on victimisation and criminalisation: the minimum every honours graduate in criminology is expected to show, at third-class level (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, threshold column, row 2. Do not call it a regulatory requirement or apply it to master's study. Set it beside the typical cell 4.5.b5, the excellent cell 4.5.b6, the honours descriptor qaa/fheq-2024/4.15.b3.1, Annex D's cell qaa/fheq-2024/annex-d/cognitive/r2/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks what passing with honours means for victimisation and criminalisation, or when a team checks that a module secures the minimum. Tell a student in plain words what you need to be able to do; with staff, frame it as the floor every assessment route must reach. Ask: 'How would a theory you know explain why some people or acts come to be treated as criminal?' Do not read the cell out at length or treat the typical or excellent cell as the pass mark."
- statement: qaa/criminology-2022/4.5.b5
  forPractitioner: { text: "At the typical level (2:2 and 2:1), most graduates should be able to weigh up critically, using criminological theory, the political and social processes by which people are victimised and criminalised; design assessment so they can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you should be able to weigh up critically, using criminological theory, the political and social processes by which people are victimised and criminalised.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical outcome on victimisation and criminalisation: what most honours graduates in criminology should reach at lower or upper second-class level (FHEQ level 6, FQHEIS level 10), not the minimum. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, typical column, row 2. Do not present it as a pass requirement or as a regulatory standard. Set it beside the threshold cell 4.5.b4, the excellent cell 4.5.b6, the honours descriptor qaa/fheq-2024/4.15.b3.1 and Annex D's cells qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise this when a student wants to know what a good second-class answer on victimisation and criminalisation looks like, or when staff calibrate marking. Explain it in plain words as the usual standard, above the minimum; with staff, use it to describe the middle bands. Ask: 'How would a theory you know explain why some people or acts come to be treated as criminal?' and 'Where is your work more descriptive than critical?' Do not present it as the minimum needed to pass."
- statement: qaa/criminology-2022/4.5.b6
  forPractitioner: { text: "At the excellent level (first class), graduates should be able to give an exceptionally critical appraisal, using criminological theory, of the political and social processes by which people are victimised and criminalised; design assessment with room to show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you should be able to give an exceptionally critical appraisal, using criminological theory, of the political and social processes by which people are victimised and criminalised.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent outcome on victimisation and criminalisation: an aspiration that marks first-class work in an honours degree in criminology (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, excellent column, row 2. Do not present it as required for the award or as a master's standard. Set it beside the typical cell 4.5.b5, the threshold cell 4.5.b4, the honours descriptor qaa/fheq-2024/4.15.b3.1 and Annex D's first-class cell qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise this when a student aims for a first or asks how to stretch their work on victimisation and criminalisation. Put it as an aspiration in plain words; with staff, use it to describe what lifts work into the top band. Ask: 'How would a theory you know explain why some people or acts come to be treated as criminal?' and 'What would make your analysis exceptional rather than sound?' Never present it as what everyone must reach."
- statement: qaa/criminology-2022/4.5.b7
  forPractitioner: { text: "At threshold, set teaching and assessment so that every honours graduate can give an account of how social diversity and inequality shape crime, harm, deviance and victimisation and the ways societies respond to them; this is the minimum for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should be able to give an account of how social diversity and inequality shape crime, harm, deviance and victimisation and the ways societies respond to them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold outcome on social diversity and inequality: the minimum every honours graduate in criminology is expected to show, at third-class level (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, threshold column, row 3. Do not call it a regulatory requirement or apply it to master's study. Set it beside the typical cell 4.5.b8, the excellent cell 4.5.b9, the honours descriptor qaa/fheq-2024/4.15.b1, Annex D's cell qaa/fheq-2024/annex-d/knowledge/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks what passing with honours means for social diversity and inequality, or when a team checks that a module secures the minimum. Tell a student in plain words what you need to be able to do; with staff, frame it as the floor every assessment route must reach. Ask: 'How do class, gender, race or other social divisions shape the cases you have studied?' Do not read the cell out at length or treat the typical or excellent cell as the pass mark."
- statement: qaa/criminology-2022/4.5.b8
  forPractitioner: { text: "At the typical level (2:2 and 2:1), most graduates should be able to show a critical understanding of how social diversity and inequality shape crime, harm, deviance and victimisation and the ways societies respond to them; design assessment so they can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you should be able to show a critical understanding of how social diversity and inequality shape crime, harm, deviance and victimisation and the ways societies respond to them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical outcome on social diversity and inequality: what most honours graduates in criminology should reach at lower or upper second-class level (FHEQ level 6, FQHEIS level 10), not the minimum. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, typical column, row 3. Do not present it as a pass requirement or as a regulatory standard. Set it beside the threshold cell 4.5.b7, the excellent cell 4.5.b9, the honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's cells qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise this when a student wants to know what a good second-class answer on social diversity and inequality looks like, or when staff calibrate marking. Explain it in plain words as the usual standard, above the minimum; with staff, use it to describe the middle bands. Ask: 'How do class, gender, race or other social divisions shape the cases you have studied?' and 'Where is your work more descriptive than critical?' Do not present it as the minimum needed to pass."
- statement: qaa/criminology-2022/4.5.b9
  forPractitioner: { text: "At the excellent level (first class), graduates should be able to show an exceptionally critical understanding of how social diversity and inequality shape crime, harm, deviance and victimisation and the ways societies respond to them; design assessment with room to show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you should be able to show an exceptionally critical understanding of how social diversity and inequality shape crime, harm, deviance and victimisation and the ways societies respond to them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent outcome on social diversity and inequality: an aspiration that marks first-class work in an honours degree in criminology (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, excellent column, row 3. Do not present it as required for the award or as a master's standard. Set it beside the typical cell 4.5.b8, the threshold cell 4.5.b7, the honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's first-class cell qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this when a student aims for a first or asks how to stretch their work on social diversity and inequality. Put it as an aspiration in plain words; with staff, use it to describe what lifts work into the top band. Ask: 'How do class, gender, race or other social divisions shape the cases you have studied?' and 'What would make your analysis exceptional rather than sound?' Never present it as what everyone must reach."
- statement: qaa/criminology-2022/4.5.b10
  forPractitioner: { text: "At threshold, set teaching and assessment so that every honours graduate can judge how criminal justice agencies work and change, against shifting values and relationships among people, groups and public and private bodies in different places; this is the minimum for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should be able to judge how criminal justice agencies work and change, against shifting values and relationships among people, groups and public and private bodies in different places.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold outcome on criminal justice agency practice: the minimum every honours graduate in criminology is expected to show, at third-class level (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, threshold column, row 4. Do not call it a regulatory requirement or apply it to master's study. Set it beside the typical cell 4.5.b11, the excellent cell 4.5.b12, the honours descriptor qaa/fheq-2024/4.15.b7, Annex D's cell qaa/fheq-2024/annex-d/cognitive/r2/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks what passing with honours means for criminal justice agency practice, or when a team checks that a module secures the minimum. Tell a student in plain words what you need to be able to do; with staff, frame it as the floor every assessment route must reach. Ask: 'Pick a criminal justice agency: how have its practices changed, and how would you judge them?' Do not read the cell out at length or treat the typical or excellent cell as the pass mark."
- statement: qaa/criminology-2022/4.5.b11
  forPractitioner: { text: "At the typical level (2:2 and 2:1), most graduates should be able to judge critically how criminal justice agencies work and change, against shifting values and relationships among people, groups and public and private bodies in different places; design assessment so they can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you should be able to judge critically how criminal justice agencies work and change, against shifting values and relationships among people, groups and public and private bodies in different places.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical outcome on criminal justice agency practice: what most honours graduates in criminology should reach at lower or upper second-class level (FHEQ level 6, FQHEIS level 10), not the minimum. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, typical column, row 4. Do not present it as a pass requirement or as a regulatory standard. Set it beside the threshold cell 4.5.b10, the excellent cell 4.5.b12, the honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's cells qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise this when a student wants to know what a good second-class answer on criminal justice agency practice looks like, or when staff calibrate marking. Explain it in plain words as the usual standard, above the minimum; with staff, use it to describe the middle bands. Ask: 'Pick a criminal justice agency: how have its practices changed, and how would you judge them?' and 'Where is your work more descriptive than critical?' Do not present it as the minimum needed to pass."
- statement: qaa/criminology-2022/4.5.b12
  forPractitioner: { text: "At the excellent level (first class), graduates should be able to judge critically, to an exceptional standard, how criminal justice agencies work and change, against shifting values and relationships among people, groups and public and private bodies in different places; design assessment with room to show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you should be able to judge critically, to an exceptional standard, how criminal justice agencies work and change, against shifting values and relationships among people, groups and public and private bodies in different places.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent outcome on criminal justice agency practice: an aspiration that marks first-class work in an honours degree in criminology (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, excellent column, row 4. Do not present it as required for the award or as a master's standard. Set it beside the typical cell 4.5.b11, the threshold cell 4.5.b10, the honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's first-class cell qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise this when a student aims for a first or asks how to stretch their work on criminal justice agency practice. Put it as an aspiration in plain words; with staff, use it to describe what lifts work into the top band. Ask: 'Pick a criminal justice agency: how have its practices changed, and how would you judge them?' and 'What would make your analysis exceptional rather than sound?' Never present it as what everyone must reach."
- statement: qaa/criminology-2022/4.5.b13
  forPractitioner: { text: "At threshold, set teaching and assessment so that every honours graduate can look into the governance, risk management and human rights values and processes that shape how UK criminal justice systems, and the agencies that run sentences and their alternatives, treat people who break the law; this is the minimum for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should be able to look into the governance, risk management and human rights values and processes that shape how UK criminal justice systems, and the agencies that run sentences and their alternatives, treat people who break the law.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold outcome on governance, risk and rights in the treatment of lawbreakers: the minimum every honours graduate in criminology is expected to show, at third-class level (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, threshold column, row 5. Do not call it a regulatory requirement or apply it to master's study. Set it beside the typical cell 4.5.b14, the excellent cell 4.5.b15, the honours descriptor qaa/fheq-2024/4.15.b7, Annex D's cell qaa/fheq-2024/annex-d/knowledge/r2/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks what passing with honours means for governance, risk and rights in the treatment of lawbreakers, or when a team checks that a module secures the minimum. Tell a student in plain words what you need to be able to do; with staff, frame it as the floor every assessment route must reach. Ask: 'What values and risks shape how people who break the law are dealt with in the UK systems you know?' Do not read the cell out at length or treat the typical or excellent cell as the pass mark."
- statement: qaa/criminology-2022/4.5.b14
  forPractitioner: { text: "At the typical level (2:2 and 2:1), most graduates should be able to appraise critically the governance, risk management and human rights values and processes that shape how UK criminal justice systems, and the agencies that run sentences and their alternatives, treat people who break the law; design assessment so they can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you should be able to appraise critically the governance, risk management and human rights values and processes that shape how UK criminal justice systems, and the agencies that run sentences and their alternatives, treat people who break the law.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical outcome on governance, risk and rights in the treatment of lawbreakers: what most honours graduates in criminology should reach at lower or upper second-class level (FHEQ level 6, FQHEIS level 10), not the minimum. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, typical column, row 5. Do not present it as a pass requirement or as a regulatory standard. Set it beside the threshold cell 4.5.b13, the excellent cell 4.5.b15, the honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise this when a student wants to know what a good second-class answer on governance, risk and rights in the treatment of lawbreakers looks like, or when staff calibrate marking. Explain it in plain words as the usual standard, above the minimum; with staff, use it to describe the middle bands. Ask: 'What values and risks shape how people who break the law are dealt with in the UK systems you know?' and 'Where is your work more descriptive than critical?' Do not present it as the minimum needed to pass."
- statement: qaa/criminology-2022/4.5.b15
  forPractitioner: { text: "At the excellent level (first class), graduates should be able to give an exceptionally critical appraisal of the governance, risk management and human rights values and processes that shape how UK criminal justice systems, and the agencies that run sentences and their alternatives, treat people who break the law; design assessment with room to show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you should be able to give an exceptionally critical appraisal of the governance, risk management and human rights values and processes that shape how UK criminal justice systems, and the agencies that run sentences and their alternatives, treat people who break the law.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent outcome on governance, risk and rights in the treatment of lawbreakers: an aspiration that marks first-class work in an honours degree in criminology (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, excellent column, row 5. Do not present it as required for the award or as a master's standard. Set it beside the typical cell 4.5.b14, the threshold cell 4.5.b13, the honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's first-class cell qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise this when a student aims for a first or asks how to stretch their work on governance, risk and rights in the treatment of lawbreakers. Put it as an aspiration in plain words; with staff, use it to describe what lifts work into the top band. Ask: 'What values and risks shape how people who break the law are dealt with in the UK systems you know?' and 'What would make your analysis exceptional rather than sound?' Never present it as what everyone must reach."
- statement: qaa/criminology-2022/4.5.b16
  forPractitioner: { text: "At threshold, set teaching and assessment so that every honours graduate can use ideas of human rights to judge efforts to prevent harm and keep people safe; this is the minimum for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should be able to use ideas of human rights to judge efforts to prevent harm and keep people safe.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold outcome on human rights and harm prevention: the minimum every honours graduate in criminology is expected to show, at third-class level (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, threshold column, row 6. Do not call it a regulatory requirement or apply it to master's study. Set it beside the typical cell 4.5.b17, the excellent cell 4.5.b18, the honours descriptor qaa/fheq-2024/4.15.b3.1, Annex D's cell qaa/fheq-2024/annex-d/cognitive/r3/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks what passing with honours means for human rights and harm prevention, or when a team checks that a module secures the minimum. Tell a student in plain words what you need to be able to do; with staff, frame it as the floor every assessment route must reach. Ask: 'How would you use a human rights argument to judge a measure meant to keep people safe?' Do not read the cell out at length or treat the typical or excellent cell as the pass mark."
- statement: qaa/criminology-2022/4.5.b17
  forPractitioner: { text: "At the typical level (2:2 and 2:1), most graduates should be able to understand ideas of human rights critically and use them to judge, critically, efforts to prevent harm and keep people safe; design assessment so they can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you should be able to understand ideas of human rights critically and use them to judge, critically, efforts to prevent harm and keep people safe.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical outcome on human rights and harm prevention: what most honours graduates in criminology should reach at lower or upper second-class level (FHEQ level 6, FQHEIS level 10), not the minimum. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, typical column, row 6. Do not present it as a pass requirement or as a regulatory standard. Set it beside the threshold cell 4.5.b16, the excellent cell 4.5.b18, the honours descriptor qaa/fheq-2024/4.15.b3.1 and Annex D's cells qaa/fheq-2024/annex-d/cognitive/r3/2.2 and qaa/fheq-2024/annex-d/cognitive/r3/2.1."
  author-agent-dialogue: "Raise this when a student wants to know what a good second-class answer on human rights and harm prevention looks like, or when staff calibrate marking. Explain it in plain words as the usual standard, above the minimum; with staff, use it to describe the middle bands. Ask: 'How would you use a human rights argument to judge a measure meant to keep people safe?' and 'Where is your work more descriptive than critical?' Do not present it as the minimum needed to pass."
- statement: qaa/criminology-2022/4.5.b18
  forPractitioner: { text: "At the excellent level (first class), graduates should be able to show an exceptionally critical understanding and use of ideas of human rights, judging critically efforts to prevent harm and keep people safe; design assessment with room to show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you should be able to show an exceptionally critical understanding and use of ideas of human rights, judging critically efforts to prevent harm and keep people safe.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent outcome on human rights and harm prevention: an aspiration that marks first-class work in an honours degree in criminology (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, excellent column, row 6. Do not present it as required for the award or as a master's standard. Set it beside the typical cell 4.5.b17, the threshold cell 4.5.b16, the honours descriptor qaa/fheq-2024/4.15.b3.1 and Annex D's first-class cell qaa/fheq-2024/annex-d/cognitive/r3/1st."
  author-agent-dialogue: "Raise this when a student aims for a first or asks how to stretch their work on human rights and harm prevention. Put it as an aspiration in plain words; with staff, use it to describe what lifts work into the top band. Ask: 'How would you use a human rights argument to judge a measure meant to keep people safe?' and 'What would make your analysis exceptional rather than sound?' Never present it as what everyone must reach."
- statement: qaa/criminology-2022/4.5.b19
  forPractitioner: { text: "At threshold, set teaching and assessment so that every honours graduate can use a variety of research strategies and methods, judge when each fits and choose a suitable strategy for a given research problem; this is the minimum for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should be able to use a variety of research strategies and methods, judge when each fits and choose a suitable strategy for a given research problem.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold outcome on research strategies and methods: the minimum every honours graduate in criminology is expected to show, at third-class level (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, threshold column, row 7. Do not call it a regulatory requirement or apply it to master's study. Set it beside the typical cell 4.5.b20, the excellent cell 4.5.b21, the honours descriptor qaa/fheq-2024/4.15.b2, Annex D's cell qaa/fheq-2024/annex-d/practical/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks what passing with honours means for research strategies and methods, or when a team checks that a module secures the minimum. Tell a student in plain words what you need to be able to do; with staff, frame it as the floor every assessment route must reach. Ask: 'For your research question, which method fits best, and why not the others?' Do not read the cell out at length or treat the typical or excellent cell as the pass mark."
- statement: qaa/criminology-2022/4.5.b20
  forPractitioner: { text: "At the typical level (2:2 and 2:1), most graduates should be able to use a variety of research strategies and methods, judge critically when each fits and choose a suitable strategy for a given research problem; design assessment so they can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you should be able to use a variety of research strategies and methods, judge critically when each fits and choose a suitable strategy for a given research problem.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical outcome on research strategies and methods: what most honours graduates in criminology should reach at lower or upper second-class level (FHEQ level 6, FQHEIS level 10), not the minimum. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, typical column, row 7. Do not present it as a pass requirement or as a regulatory standard. Set it beside the threshold cell 4.5.b19, the excellent cell 4.5.b21, the honours descriptor qaa/fheq-2024/4.15.b2 and Annex D's cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when a student wants to know what a good second-class answer on research strategies and methods looks like, or when staff calibrate marking. Explain it in plain words as the usual standard, above the minimum; with staff, use it to describe the middle bands. Ask: 'For your research question, which method fits best, and why not the others?' and 'Where is your work more descriptive than critical?' Do not present it as the minimum needed to pass."
- statement: qaa/criminology-2022/4.5.b21
  forPractitioner: { text: "At the excellent level (first class), graduates should be able to use a variety of research strategies and methods accurately, appraise to an exceptional standard when each fits and choose a suitable strategy for a given research problem every time; design assessment with room to show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you should be able to use a variety of research strategies and methods accurately, appraise to an exceptional standard when each fits and choose a suitable strategy for a given research problem every time.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent outcome on research strategies and methods: an aspiration that marks first-class work in an honours degree in criminology (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, excellent column, row 7. Do not present it as required for the award or as a master's standard. Set it beside the typical cell 4.5.b20, the threshold cell 4.5.b19, the honours descriptor qaa/fheq-2024/4.15.b2 and Annex D's first-class cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when a student aims for a first or asks how to stretch their work on research strategies and methods. Put it as an aspiration in plain words; with staff, use it to describe what lifts work into the top band. Ask: 'For your research question, which method fits best, and why not the others?' and 'What would make your analysis exceptional rather than sound?' Never present it as what everyone must reach."
- statement: qaa/criminology-2022/4.5.b22
  forPractitioner: { text: "At threshold, set teaching and assessment so that every honours graduate can judge the strengths and weaknesses of comparative approaches to crime, harm, deviance and victimisation and to how societies deal with them; this is the minimum for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should be able to judge the strengths and weaknesses of comparative approaches to crime, harm, deviance and victimisation and to how societies deal with them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold outcome on comparative analysis: the minimum every honours graduate in criminology is expected to show, at third-class level (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, threshold column, row 8. Do not call it a regulatory requirement or apply it to master's study. Set it beside the typical cell 4.5.b23, the excellent cell 4.5.b24, the honours descriptor qaa/fheq-2024/4.15.b7, Annex D's cell qaa/fheq-2024/annex-d/cognitive/r2/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks what passing with honours means for comparative analysis, or when a team checks that a module secures the minimum. Tell a student in plain words what you need to be able to do; with staff, frame it as the floor every assessment route must reach. Ask: 'What does comparing two places or systems show you, and what can it hide?' Do not read the cell out at length or treat the typical or excellent cell as the pass mark."
- statement: qaa/criminology-2022/4.5.b23
  forPractitioner: { text: "At the typical level (2:2 and 2:1), most graduates should be able to judge critically the strengths and weaknesses of comparative approaches to crime, harm, deviance and victimisation and to how societies deal with them; design assessment so they can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you should be able to judge critically the strengths and weaknesses of comparative approaches to crime, harm, deviance and victimisation and to how societies deal with them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical outcome on comparative analysis: what most honours graduates in criminology should reach at lower or upper second-class level (FHEQ level 6, FQHEIS level 10), not the minimum. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, typical column, row 8. Do not present it as a pass requirement or as a regulatory standard. Set it beside the threshold cell 4.5.b22, the excellent cell 4.5.b24, the honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's cells qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise this when a student wants to know what a good second-class answer on comparative analysis looks like, or when staff calibrate marking. Explain it in plain words as the usual standard, above the minimum; with staff, use it to describe the middle bands. Ask: 'What does comparing two places or systems show you, and what can it hide?' and 'Where is your work more descriptive than critical?' Do not present it as the minimum needed to pass."
- statement: qaa/criminology-2022/4.5.b24
  forPractitioner: { text: "At the excellent level (first class), graduates should be able to judge critically, to an exceptional standard, the strengths and weaknesses of comparative approaches to crime, harm, deviance and victimisation and to how societies deal with them; design assessment with room to show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you should be able to judge critically, to an exceptional standard, the strengths and weaknesses of comparative approaches to crime, harm, deviance and victimisation and to how societies deal with them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent outcome on comparative analysis: an aspiration that marks first-class work in an honours degree in criminology (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, excellent column, row 8. Do not present it as required for the award or as a master's standard. Set it beside the typical cell 4.5.b23, the threshold cell 4.5.b22, the honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's first-class cell qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise this when a student aims for a first or asks how to stretch their work on comparative analysis. Put it as an aspiration in plain words; with staff, use it to describe what lifts work into the top band. Ask: 'What does comparing two places or systems show you, and what can it hide?' and 'What would make your analysis exceptional rather than sound?' Never present it as what everyone must reach."
- statement: qaa/criminology-2022/4.5.b25
  forPractitioner: { text: "At threshold, set teaching and assessment so that every honours graduate can summarise and analyse quantitative and qualitative evidence on crime, harm, deviance, victimisation and how societies respond, so as to weigh rival criminological theories; this is the minimum for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should be able to summarise and analyse quantitative and qualitative evidence on crime, harm, deviance, victimisation and how societies respond, so as to weigh rival criminological theories.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold outcome on analysing empirical data: the minimum every honours graduate in criminology is expected to show, at third-class level (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, threshold column, row 9. Do not call it a regulatory requirement or apply it to master's study. Set it beside the typical cell 4.5.b26, the excellent cell 4.5.b27, the honours descriptor qaa/fheq-2024/4.15.b6, Annex D's cell qaa/fheq-2024/annex-d/practical/r4/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks what passing with honours means for analysing empirical data, or when a team checks that a module secures the minimum. Tell a student in plain words what you need to be able to do; with staff, frame it as the floor every assessment route must reach. Ask: 'What do the figures and accounts you have gathered say about the theories you are testing?' Do not read the cell out at length or treat the typical or excellent cell as the pass mark."
- statement: qaa/criminology-2022/4.5.b26
  forPractitioner: { text: "At the typical level (2:2 and 2:1), most graduates should be able to summarise and critically analyse quantitative and qualitative evidence on crime, harm, deviance, victimisation and how societies respond, so as to weigh rival criminological theories critically; design assessment so they can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you should be able to summarise and critically analyse quantitative and qualitative evidence on crime, harm, deviance, victimisation and how societies respond, so as to weigh rival criminological theories critically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical outcome on analysing empirical data: what most honours graduates in criminology should reach at lower or upper second-class level (FHEQ level 6, FQHEIS level 10), not the minimum. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, typical column, row 9. Do not present it as a pass requirement or as a regulatory standard. Set it beside the threshold cell 4.5.b25, the excellent cell 4.5.b27, the honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's cells qaa/fheq-2024/annex-d/practical/r4/2.2 and qaa/fheq-2024/annex-d/practical/r4/2.1."
  author-agent-dialogue: "Raise this when a student wants to know what a good second-class answer on analysing empirical data looks like, or when staff calibrate marking. Explain it in plain words as the usual standard, above the minimum; with staff, use it to describe the middle bands. Ask: 'What do the figures and accounts you have gathered say about the theories you are testing?' and 'Where is your work more descriptive than critical?' Do not present it as the minimum needed to pass."
- statement: qaa/criminology-2022/4.5.b27
  forPractitioner: { text: "At the excellent level (first class), graduates should be able to summarise and critically analyse, to an exceptional standard, quantitative and qualitative evidence on crime, harm, deviance, victimisation and how societies respond, weighing rival theories critically; design assessment with room to show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you should be able to summarise and critically analyse, to an exceptional standard, quantitative and qualitative evidence on crime, harm, deviance, victimisation and how societies respond, weighing rival theories critically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent outcome on analysing empirical data: an aspiration that marks first-class work in an honours degree in criminology (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, excellent column, row 9. Do not present it as required for the award or as a master's standard. Set it beside the typical cell 4.5.b26, the threshold cell 4.5.b25, the honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's first-class cell qaa/fheq-2024/annex-d/practical/r4/1st."
  author-agent-dialogue: "Raise this when a student aims for a first or asks how to stretch their work on analysing empirical data. Put it as an aspiration in plain words; with staff, use it to describe what lifts work into the top band. Ask: 'What do the figures and accounts you have gathered say about the theories you are testing?' and 'What would make your analysis exceptional rather than sound?' Never present it as what everyone must reach."
- statement: qaa/criminology-2022/4.5.b28
  forPractitioner: { text: "At threshold, set teaching and assessment so that every honours graduate can explain and judge complex social problems using criminological theories about crime, social class, victimisation and how societies respond to crime and deviance; this is the minimum for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should be able to explain and judge complex social problems using criminological theories about crime, social class, victimisation and how societies respond to crime and deviance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold outcome on explaining complex social problems: the minimum every honours graduate in criminology is expected to show, at third-class level (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, threshold column, row 10. Do not call it a regulatory requirement or apply it to master's study. Set it beside the typical cell 4.5.b29, the excellent cell 4.5.b30, the honours descriptor qaa/fheq-2024/4.15.b3.1, Annex D's cell qaa/fheq-2024/annex-d/cognitive/r3/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks what passing with honours means for explaining complex social problems, or when a team checks that a module secures the minimum. Tell a student in plain words what you need to be able to do; with staff, frame it as the floor every assessment route must reach. Ask: 'Choose a social problem: how would two theories explain it differently?' Do not read the cell out at length or treat the typical or excellent cell as the pass mark."
- statement: qaa/criminology-2022/4.5.b29
  forPractitioner: { text: "At the typical level (2:2 and 2:1), most graduates should be able to explain and judge critically complex social problems using criminological theories about crime, social class, victimisation and how societies respond to crime and deviance; design assessment so they can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you should be able to explain and judge critically complex social problems using criminological theories about crime, social class, victimisation and how societies respond to crime and deviance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical outcome on explaining complex social problems: what most honours graduates in criminology should reach at lower or upper second-class level (FHEQ level 6, FQHEIS level 10), not the minimum. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, typical column, row 10. Do not present it as a pass requirement or as a regulatory standard. Set it beside the threshold cell 4.5.b28, the excellent cell 4.5.b30, the honours descriptor qaa/fheq-2024/4.15.b3.1 and Annex D's cells qaa/fheq-2024/annex-d/cognitive/r3/2.2 and qaa/fheq-2024/annex-d/cognitive/r3/2.1."
  author-agent-dialogue: "Raise this when a student wants to know what a good second-class answer on explaining complex social problems looks like, or when staff calibrate marking. Explain it in plain words as the usual standard, above the minimum; with staff, use it to describe the middle bands. Ask: 'Choose a social problem: how would two theories explain it differently?' and 'Where is your work more descriptive than critical?' Do not present it as the minimum needed to pass."
- statement: qaa/criminology-2022/4.5.b30
  forPractitioner: { text: "At the excellent level (first class), graduates should be able to explain and judge critically, to an exceptional standard, complex social problems using criminological theories about crime, social class, victimisation and how societies respond to crime and deviance; design assessment with room to show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you should be able to explain and judge critically, to an exceptional standard, complex social problems using criminological theories about crime, social class, victimisation and how societies respond to crime and deviance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent outcome on explaining complex social problems: an aspiration that marks first-class work in an honours degree in criminology (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, excellent column, row 10. Do not present it as required for the award or as a master's standard. Set it beside the typical cell 4.5.b29, the threshold cell 4.5.b28, the honours descriptor qaa/fheq-2024/4.15.b3.1 and Annex D's first-class cell qaa/fheq-2024/annex-d/cognitive/r3/1st."
  author-agent-dialogue: "Raise this when a student aims for a first or asks how to stretch their work on explaining complex social problems. Put it as an aspiration in plain words; with staff, use it to describe what lifts work into the top band. Ask: 'Choose a social problem: how would two theories explain it differently?' and 'What would make your analysis exceptional rather than sound?' Never present it as what everyone must reach."
- statement: qaa/criminology-2022/4.5.b31
  forPractitioner: { text: "At threshold, set teaching and assessment so that every honours graduate can analyse how criminology differs from other ways of understanding crime and society; this is the minimum for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should be able to analyse how criminology differs from other ways of understanding crime and society.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold outcome on what sets criminology apart: the minimum every honours graduate in criminology is expected to show, at third-class level (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, threshold column, row 11. Do not call it a regulatory requirement or apply it to master's study. Set it beside the typical cell 4.5.b32, the excellent cell 4.5.b33, the honours descriptor qaa/fheq-2024/4.15.b4, Annex D's cell qaa/fheq-2024/annex-d/knowledge/r2/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks what passing with honours means for what sets criminology apart, or when a team checks that a module secures the minimum. Tell a student in plain words what you need to be able to do; with staff, frame it as the floor every assessment route must reach. Ask: 'What makes a criminological explanation different from a journalistic or a legal one?' Do not read the cell out at length or treat the typical or excellent cell as the pass mark."
- statement: qaa/criminology-2022/4.5.b32
  forPractitioner: { text: "At the typical level (2:2 and 2:1), most graduates should be able to analyse critically how criminology differs from other ways of understanding crime and society; design assessment so they can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you should be able to analyse critically how criminology differs from other ways of understanding crime and society.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical outcome on what sets criminology apart: what most honours graduates in criminology should reach at lower or upper second-class level (FHEQ level 6, FQHEIS level 10), not the minimum. Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, typical column, row 11. Do not present it as a pass requirement or as a regulatory standard. Set it beside the threshold cell 4.5.b31, the excellent cell 4.5.b33, the honours descriptor qaa/fheq-2024/4.15.b4 and Annex D's cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise this when a student wants to know what a good second-class answer on what sets criminology apart looks like, or when staff calibrate marking. Explain it in plain words as the usual standard, above the minimum; with staff, use it to describe the middle bands. Ask: 'What makes a criminological explanation different from a journalistic or a legal one?' and 'Where is your work more descriptive than critical?' Do not present it as the minimum needed to pass."
- statement: qaa/criminology-2022/4.5.b33
  forPractitioner: { text: "At the excellent level (first class), graduates should be able to show an exceptionally critical analysis of how criminology differs from other ways of understanding crime and society; design assessment with room to show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you should be able to show an exceptionally critical analysis of how criminology differs from other ways of understanding crime and society.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent outcome on what sets criminology apart: an aspiration that marks first-class work in an honours degree in criminology (FHEQ level 6, FQHEIS level 10). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.5, excellent column, row 11. Do not present it as required for the award or as a master's standard. Set it beside the typical cell 4.5.b32, the threshold cell 4.5.b31, the honours descriptor qaa/fheq-2024/4.15.b4 and Annex D's first-class cell qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise this when a student aims for a first or asks how to stretch their work on what sets criminology apart. Put it as an aspiration in plain words; with staff, use it to describe what lifts work into the top band. Ask: 'What makes a criminological explanation different from a journalistic or a legal one?' and 'What would make your analysis exceptional rather than sound?' Never present it as what everyone must reach."
- statement: qaa/criminology-2022/4.6.b1
  forPractitioner: { text: "At master's level, make sure graduates can show systematic understanding of, and critical awareness about, topics shaped by criminology; this adds to the honours outcomes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a master's course in criminology, you should be able to show systematic understanding of, and critical awareness about, topics shaped by criminology.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold outcome for a master's degree in criminology, added to the honours outcomes, at FHEQ level 7 and FQHEIS level 11 (levels inferred from the award). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.6. Do not claim it applies to the honours degree or that it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b1, spine:7, para 2.4 and the honours outcomes in para 4.5."
  author-agent-dialogue: "Raise this with master's students or a postgraduate course team when a master's student asks how much depth is expected across the field. Put it plainly as what a master's graduate should be able to show. Ask: 'Which topics in your field do you know systematically, and where are the gaps?' Do not read the list aloud or apply it to undergraduates."
- statement: qaa/criminology-2022/4.6.b2
  forPractitioner: { text: "At master's level, make sure graduates can show critical awareness of how ideas developed over time, their cultural setting and the social and political theories that shape criminological practice; this adds to the honours outcomes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a master's course in criminology, you should be able to show critical awareness of how ideas developed over time, their cultural setting and the social and political theories that shape criminological practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold outcome for a master's degree in criminology, added to the honours outcomes, at FHEQ level 7 and FQHEIS level 11 (levels inferred from the award). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.6. Do not claim it applies to the honours degree or that it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b1, spine:7, para 2.4 and the honours outcomes in para 4.5."
  author-agent-dialogue: "Raise this with master's students or a postgraduate course team when a student treats theory as fixed rather than shaped by history and politics. Put it plainly as what a master's graduate should be able to show. Ask: 'Where did the ideas behind your topic come from, and whose politics do they carry?' Do not read the list aloud or apply it to undergraduates."
- statement: qaa/criminology-2022/4.6.b3
  forPractitioner: { text: "At master's level, make sure graduates can show critical awareness of how intersecting forms of power bear on criminal justice agencies and on responses to crime, harm, deviance and victimisation; this adds to the honours outcomes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a master's course in criminology, you should be able to show critical awareness of how intersecting forms of power bear on criminal justice agencies and on responses to crime, harm, deviance and victimisation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold outcome for a master's degree in criminology, added to the honours outcomes, at FHEQ level 7 and FQHEIS level 11 (levels inferred from the award). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.6. Do not claim it applies to the honours degree or that it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b1, spine:7, para 2.4 and the honours outcomes in para 4.5."
  author-agent-dialogue: "Raise this with master's students or a postgraduate course team when a student analyses inequality one dimension at a time. Put it plainly as what a master's graduate should be able to show. Ask: 'How do class, race, gender and other forms of power combine in the case you are studying?' Do not read the list aloud or apply it to undergraduates."
- statement: qaa/criminology-2022/4.6.b4
  forPractitioner: { text: "At master's level, make sure graduates can pick suitable methodologies for complex problems and design an original research project; this adds to the honours outcomes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a master's course in criminology, you should be able to pick suitable methodologies for complex problems and design an original research project.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold outcome for a master's degree in criminology, added to the honours outcomes, at FHEQ level 7 and FQHEIS level 11 (levels inferred from the award). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.6. Do not claim it applies to the honours degree or that it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b4.2, spine:7, para 2.4 and the honours outcomes in para 4.5."
  author-agent-dialogue: "Raise this with master's students or a postgraduate course team when a master's student plans a dissertation. Put it plainly as what a master's graduate should be able to show. Ask: 'Why is this methodology the right one for your problem, and what would make you change it?' Do not read the list aloud or apply it to undergraduates."
- statement: qaa/criminology-2022/4.6.b5
  forPractitioner: { text: "At master's level, make sure graduates can carry critical discussion and analysis of complex ideas forward and work independently with some originality; this adds to the honours outcomes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a master's course in criminology, you should be able to carry critical discussion and analysis of complex ideas forward and work independently with some originality.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold outcome for a master's degree in criminology, added to the honours outcomes, at FHEQ level 7 and FQHEIS level 11 (levels inferred from the award). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.6. Do not claim it applies to the honours degree or that it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b6, spine:7, para 2.4 and the honours outcomes in para 4.5."
  author-agent-dialogue: "Raise this with master's students or a postgraduate course team when a student relies heavily on supervision or on summary. Put it plainly as what a master's graduate should be able to show. Ask: 'What in your argument is your own, and how did you reach it without being told?' Do not read the list aloud or apply it to undergraduates."
- statement: qaa/criminology-2022/4.6.b6
  forPractitioner: { text: "At master's level, make sure graduates can complete a substantial empirical project, systematic review or systematic case study grounded in broad current understanding of the subject; this adds to the honours outcomes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a master's course in criminology, you should be able to complete a substantial empirical project, systematic review or systematic case study grounded in broad current understanding of the subject.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold outcome for a master's degree in criminology, added to the honours outcomes, at FHEQ level 7 and FQHEIS level 11 (levels inferred from the award). Cite it as QAA (2022), Criminology Subject Benchmark Statement, para 4.6. Do not claim it applies to the honours degree or that it is a regulatory requirement. Set it beside the master's descriptor qaa/fheq-2024/4.17.b3, spine:7, para 2.4 and the honours outcomes in para 4.5."
  author-agent-dialogue: "Raise this with master's students or a postgraduate course team when a student scopes a final project. Put it plainly as what a master's graduate should be able to show. Ask: 'Is your project substantial enough, and which current work in the field does it build on?' Do not read the list aloud or apply it to undergraduates."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.20; 4.2; 4.5" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.20; 4.2; 4.5" }
  - { id: "fheq:7", role: "inferred", locator: "D1, 2.4; 4.6 (master's degree; level from std:doc:qaa-fheq-2024-framework S5, Table 1)" }
  - { id: "fqheis:11", role: "inferred", locator: "D1, 4.6 (master's degree; shares the FHEQ level 7 descriptor, std:doc:qaa-fheq-2024-framework S5)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.20; 4.2; 4.5)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "shared-descriptor", basis: "inferred (std:doc:qaa-fheq-2024-framework S5; Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.9", "1.10", "1.11", "1.12", "1.13", "1.14"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.15", "1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.24", "1.25", "1.26", "1.27"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["2.17", "2.18"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "4.5: the outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees" }
- { rel: "thresholdAt", target: "std:doc:qaa-fheq-2024-framework, 4.15 (fheq:6)", note: "2.20; 4.2: each class means level 6 has been achieved" }
- { rel: "readWith", target: "std:doc:qaa-fqheis-2024-framework, 4.16 (fqheis:10)", note: "2.20; 4.2" }
- { rel: "themeReference", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "1.19 and 1.21 quote it; 1.23 points to QAA's ESD pages" }
- { rel: "refersTo", target: "British Society of Criminology, Statement of Ethics", note: "2.12; not yet ingested (Part E)" }
- { rel: "refersTo", target: "British Sociological Association, Code of Ethics", note: "2.12; not yet ingested (Part E)" }
- { rel: "refersTo", target: "Economic and Social Research Council, guidelines for research training", note: "1.4; not yet ingested (Part E)" }
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
- Criminology studies how people and acts are criminalised and victimised, what crime, harm and deviance mean and what causes them, how they are prevented and managed and how they are represented (D1, 1.6)
- A multidisciplinary field first taught in the UK at postgraduate level from the late 1950s; undergraduate degrees came later (D1, 1.4)
- Its theories and areas of enquiry keep changing, fed by staff research and by neighbouring subjects such as sociology, law and philosophy, while its core stays steady (D1, 1.5)
- Theoretical and empirical at once, with practical application; many of its theoretical advances have come from empirical studies (D1, 3.2; 3.3)
- Marked by debate over how to explain its subject, put theory into research, inform policy and human rights, handle data and manage research ethics (D1, 3.1)
- Contested values in what counts as crime, harm, criminalisation and victimisation lie at its centre (D1, 3.4)
- Joins scholarship and practice, working with justice agencies, government and charities in research and teaching partnerships (D1, 1.17; 2.26 to 2.30)
- Its material is often emotive and distressing, so ethics and care run through its teaching and research (D1, 1.18; 3.6)
- Taught as single or joint honours, with foundation degrees leading towards the honours standard and master's degrees going beyond it (D1, 1.1; 1.3)

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "Inclusion is part of the subject matter (discrimination, colonialism, bias in justice) and a duty on course teams: embedded curricula, belonging, safe dialogue on sensitive topics, review for barriers and attention to a diverse intake (D1, 1.9 to 1.14)"
  statements: ["qaa/criminology-2022/1.10", "qaa/criminology-2022/1.11", "qaa/criminology-2022/1.12", "qaa/criminology-2022/1.13", "qaa/criminology-2022/1.14", "qaa/criminology-2022/3.6.b4", "qaa/criminology-2022/3.8"]
- theme: theme:esd
  inThisSubject: "Sustainability means both a current curriculum (green, queer and southern criminology, zemiology) and education for sustainable development: green criminology, ethics, global citizenship and placements linked to sustainability (D1, 1.15 to 1.23)"
  statements: ["qaa/criminology-2022/1.15", "qaa/criminology-2022/1.16", "qaa/criminology-2022/1.17", "qaa/criminology-2022/1.18", "qaa/criminology-2022/1.20", "qaa/criminology-2022/1.21", "qaa/criminology-2022/1.22"]
- theme: theme:enterprise
  inThisSubject: "Named with employability: methodological and research-ethics skills, wide career routes including policing and probation and employability opportunities with safeguards (D1, 1.24 to 1.27)"
  statements: ["qaa/criminology-2022/1.24", "qaa/criminology-2022/1.27"]
- theme: theme:accessibility
  inThisSubject: "Varied entry routes and a single-tier approach: adjustments, varied formats for all, fair access to fieldwork and placements, accessible materials and criteria (D1, 2.17; 2.18; 3.5)"
  statements: ["qaa/criminology-2022/2.18", "qaa/criminology-2022/3.5"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "1.6", gloss: "the concerns of criminology: criminalisation, victimisation, causes, prevention, responses and representation" }
  - { component: "1.8", gloss: "core areas for single and joint honours, from the history of the discipline to ethics in research" }
  - { component: "2.6", gloss: "qualitative approaches at a basic level (illustrative list)" }
  - { component: "2.8", gloss: "quantitative techniques at a basic level (illustrative list)" }
  - { component: "3.1", gloss: "the debates that characterise modern criminology" }
  - { component: "3.2", gloss: "theory and evidence across state crime, crimes of the powerful, security and digital crime" }
practices:
  - { component: "1.27", kind: "learning", gloss: "employability through placements, volunteering and guest speakers" }
  - { component: "2.24", kind: "teaching", gloss: "a wide and flexible range of teaching styles" }
  - { component: "2.30", kind: "learning", gloss: "placements, field trips and work-based modules through partnerships" }
  - { component: "3.5", kind: "learning", gloss: "modes of study and resources, which need to be accessible" }
  - { component: "3.6", kind: "teaching", gloss: "four principles: theory and evidence, rival readings, values, inclusion" }
  - { component: "3.7", kind: "teaching", gloss: "lectures, seminars, tutorials, placements, online and fieldwork" }
  - { component: "3.8", kind: "assessment", gloss: "purposes of assessment; monitoring outcomes" }
  - { component: "3.9", kind: "assessment", gloss: "what assessment methods take into account" }
  - { component: "3.10", kind: "teaching", gloss: "scaffolding modules across the years" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.5", award: "bachelor's with honours", items: 11 }
  - { rung: "threshold", leadIn: "2.2", award: "bachelor's with honours", items: 1 }
  - { rung: "threshold", leadIn: "4.6", award: "master's", items: 6 }
  - { rung: "typical", leadIn: "4.5", award: "bachelor's with honours", items: 11 }
  - { rung: "typical", leadIn: "2.2", award: "bachelor's with honours", items: 1 }
  - { rung: "excellent", leadIn: "4.5", award: "bachelor's with honours", items: 11 }
  - { rung: "excellent", leadIn: "2.3", award: "bachelor's with honours", items: 1 }
rungBases: "4.4 names three rungs for the honours graduate: threshold (3rd class), typical (2:2 or 2:1) and excellent (1st class); 4.5 is one table with three columns, each row stating one outcome three times in rising wording, so gradeOf is stated by row; 2.2 (threshold and typical jointly) and 2.3 (excellent) set research-philosophy rungs; 4.6 gives threshold standards for postgraduate (master's) degrees"
outcomeLists: []
outcomes:
  - { outcome: "key concepts and theories", threshold: "qaa/criminology-2022/4.5.b1", typical: "qaa/criminology-2022/4.5.b2", excellent: "qaa/criminology-2022/4.5.b3", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "victimisation and criminalisation", threshold: "qaa/criminology-2022/4.5.b4", typical: "qaa/criminology-2022/4.5.b5", excellent: "qaa/criminology-2022/4.5.b6", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "social diversity and inequality", threshold: "qaa/criminology-2022/4.5.b7", typical: "qaa/criminology-2022/4.5.b8", excellent: "qaa/criminology-2022/4.5.b9", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "criminal justice agency practice", threshold: "qaa/criminology-2022/4.5.b10", typical: "qaa/criminology-2022/4.5.b11", excellent: "qaa/criminology-2022/4.5.b12", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "governance, risk and rights in the treatment of lawbreakers", threshold: "qaa/criminology-2022/4.5.b13", typical: "qaa/criminology-2022/4.5.b14", excellent: "qaa/criminology-2022/4.5.b15", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "human rights and harm prevention", threshold: "qaa/criminology-2022/4.5.b16", typical: "qaa/criminology-2022/4.5.b17", excellent: "qaa/criminology-2022/4.5.b18", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "research strategies and methods", threshold: "qaa/criminology-2022/4.5.b19", typical: "qaa/criminology-2022/4.5.b20", excellent: "qaa/criminology-2022/4.5.b21", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "comparative analysis", threshold: "qaa/criminology-2022/4.5.b22", typical: "qaa/criminology-2022/4.5.b23", excellent: "qaa/criminology-2022/4.5.b24", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "analysing empirical data", threshold: "qaa/criminology-2022/4.5.b25", typical: "qaa/criminology-2022/4.5.b26", excellent: "qaa/criminology-2022/4.5.b27", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "explaining complex social problems", threshold: "qaa/criminology-2022/4.5.b28", typical: "qaa/criminology-2022/4.5.b29", excellent: "qaa/criminology-2022/4.5.b30", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "what sets criminology apart", threshold: "qaa/criminology-2022/4.5.b31", typical: "qaa/criminology-2022/4.5.b32", excellent: "qaa/criminology-2022/4.5.b33", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "philosophy of explanation and research strategy", threshold: "qaa/criminology-2022/2.2", typical: "qaa/criminology-2022/2.2.typical", excellent: "qaa/criminology-2022/2.3", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
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
- { body: "British Society of Criminology", says: "the UK professional body for criminology; it contributed to the thinking behind the statement, and its Statement of Ethics is an example of the codes students should know (D1, 1.2; 2.12)", requirements: "not yet ingested (Part E)" }
- { body: "British Sociological Association", says: "its Code of Ethics is a second example of the codes criminologists use (D1, 2.12)", requirements: "not yet ingested (Part E)" }
- { body: "Economic and Social Research Council", says: "its research training guidelines often guide postgraduate courses (D1, 1.4)", requirements: "not yet ingested (Part E)" }
- { body: "College of Policing", says: "with the National Probation Service, its workforce development positions criminology as an applied and theoretical qualification (D1, 1.26)", requirements: "not yet ingested (Part E)" }
- { body: "National Probation Service", says: "named with the College of Policing for developing the criminal justice workforce (D1, 1.26)", requirements: "not yet ingested (Part E)" }
- { body: "Advance HE", says: "publishes the ESD guidance jointly with QAA and supports its principles (D1, 1.19)", requirements: "std:doc:qaa-advancehe-esd-2021-guidance" }
- { body: "professional and regulatory bodies (unnamed)", says: "may evaluate and accredit courses with professional and vocational outcomes, through visits and desk review (D1, 2.34)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.8", "1.9", "1.10", "1.11", "1.12", "1.13", "1.14", "1.18", "2.18", "3.6", "3.8"], statements: ["1.10", "1.11", "1.12", "1.13", "1.14", "3.6.b4", "3.8"] }
  - { id: "theme:esd", named: "Sustainability; Education for Sustainable Development (ESD)", carriedIn: ["1.15", "1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23"], statements: ["1.15", "1.16", "1.17", "1.18", "1.20", "1.21", "1.22"] }
  - { id: "theme:enterprise", named: "Entrepreneurship and enterprise education; employability", carriedIn: ["1.24", "1.25", "1.26", "1.27"], statements: ["1.24", "1.27"] }
  - { id: "theme:accessibility", named: "Accessibility", carriedIn: ["1.11", "1.17", "1.18", "1.27", "2.17", "2.18", "3.5"], statements: ["2.18", "3.5"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6"], citedIn: ["2.20", "4.2", "4.5"] }
  - { framework: "scqf", levels: ["fqheis:10"], citedIn: ["2.20", "4.2", "4.5"] }
bodies:
  - { body: "British Society of Criminology", citedIn: ["1.2", "2.12"] }
  - { body: "British Sociological Association", citedIn: ["2.12"] }
  - { body: "Economic and Social Research Council", citedIn: ["1.4"] }
  - { body: "College of Policing", citedIn: ["1.26"] }
  - { body: "National Probation Service", citedIn: ["1.26"] }
  - { body: "Advance HE", citedIn: ["1.19"] }
  - { body: "professional and regulatory bodies (unnamed)", citedIn: ["2.34"] }
  - { body: "partners named as examples: police forces, Ministry of Justice, prisons, probation, youth justice, local government, Europol, UNODC, UK and international NGOs", citedIn: ["2.27", "2.28", "2.29"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.5"], role: "further detail on typical expectations at each classification" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Advance HE and QAA (2021); ESD Guidance, 2021", citedIn: ["1.19", "1.21"], role: "definition and aims of education for sustainable development" }
  - { document: "not yet ingested: QAA web pages on ESD (Quality Code advice), listed in Part E", named: "www.qaa.ac.uk/quality-code/education-for-sustainable-development", citedIn: ["1.23"], role: "further guidance on developing ESD" }
  - { document: "not yet ingested: listed in Part E", named: "British Society of Criminology's Statement of Ethics; British Sociological Association's Code of Ethics", citedIn: ["2.12"], role: "examples of ethics codes students should know" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "green-criminology", definition: "the study of crimes that harm the environment, of ecological justice and of environmental law and criminality, from individual and corporate crime to state failure (D1, 1.16)", beneficiaryDefinition: "the part of criminology that looks at harm to the environment and at justice for the natural world", scopeNote: "named with queer and southern criminology, indigenous knowledge and zemiology as emerging approaches (D1, 1.15)", category: "unknown", practices: ["education"] }
- { slug: "ethical-literacy", definition: "a level of ethical understanding enough to keep research participants safe and well (D1, 2.16)", beneficiaryDefinition: "knowing research ethics well enough to protect the people you study", scopeNote: "the summary of paras 2.12 to 2.15", category: "unknown", practices: ["education"] }
- { slug: "mixed-methods-research", definition: "research that combines qualitative and quantitative strategies (D1, 2.2; 2.11)", beneficiaryDefinition: "research that uses both numbers and accounts", scopeNote: "with triangulation and data integration (2.11)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "green-criminology", form: "green criminology", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "ethical-literacy", form: "'ethical literacy'", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "mixed-methods-research", form: "mixed methods research", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement: Criminology"
  edition: "March 2022 (fourth edition)"
  year: 2022
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/criminology-2022/criminology-2022.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 93178fffca2a57964faea7e7fb4fc0cb6676f0782672c87651bb4fdc5fee5056
  heldFiles: ["wkspc2601-library/txt/qaa-2022-criminology-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2022-criminology-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2022-criminology-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2022-criminology-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0048", source: "British Society of Criminology, Statement of Ethics", why: "named as an example code in 2.12; a body document to ingest as its own standards document" }
- { w: "W-std-0049", source: "British Sociological Association, Code of Ethics", why: "named as an example code in 2.12" }
- { w: "W-std-0050", source: "Economic and Social Research Council, guidelines for research training", why: "named in 1.4 as guiding postgraduate courses" }
```

## Part E Gaps and questions
- Rung shape (new against Psychology): 4.5 is one three-column table (threshold 3rd class; typical 2:2 and 2:1; excellent 1st class) whose eleven rows each state one outcome three times in rising wording ('critically', 'to an exceptional level'). Each cell has its own span, so each keeps its skeleton id (4.5.b1 to 4.5.b33, read row by row: threshold, typical, excellent) rather than the `.typical` and `.excellent` suffixes the batch-1 convention uses for one shared span; gradeOf is stated by row.
- Skeleton corrections: the skeleton marked all 33 table cells typical and 4.3.b1 to 4.3.b4 and 4.6.b1 to 4.6.b6 threshold. Rungs judged by column; 4.3's four items are kinds of evidence (knowledge and understanding, cognitive, practical and transferable skills), not statements; 4.6's items are threshold standards for the master's degree.
- Rung lead-ins also in section 2 (new against Psychology): 2.2 sets one research-philosophy expectation for threshold and typical jointly (recorded twice on one span, 2.2 and 2.2.typical, gradeOf stated as the same text); 2.3 sets the excellent rung (gradeOf 2.2.typical, inferred: the issuer pairs the paragraphs by heading, not by item); 2.4 the postgraduate level.
- Typical rung spans two classes (2:2 and 2:1) as one rung; Annex D splits them. Recorded as one rung.
- Master's (4.6): 'threshold standards for a postgraduate degree', in addition to the honours ones; award master's; level fheq:7 and fqheis:11 inferred from the FHEQ Table 1 (std:doc:qaa-fheq-2024-framework S5), not stated. 2.4, 2.10, 2.14 and 2.15 say 'postgraduate' or 'higher or postgraduate' without naming the award.
- Force: the 4.5 and 4.6 lead-ins say 'should be able to'. Threshold cells and 4.6 items take force threshold (4.1 and 4.3 define the threshold as the minimum for the award); typical and excellent cells take should.
- Obliging words outside the five, recorded as describes, for Abbott: 'expected to' or 'there is an expectation' (1.24, 2.1, 2.4 to 2.10, 2.13, 2.15, 2.16, 2.19, 2.20, 2.25); 'requirement' and 'is needed' in 2.25 (said of most courses only, so not must); 'important to ensure' (3.5); 'need to' (3.6 item d, recorded with its should); 'responsibility' (1.10, recorded with its must); 'has to' (1.15); 'necessity' (1.25, not recorded). 'Required' in 3.6 item b is recorded as must.
- Mixed modals in one paragraph: 1.12 and 1.13 carry both should and must; recorded must, with the should parts kept as should in the paraphrase. 2.2, 2.12 and 2.14 mix 'expected to' with should; recorded should.
- Illustrative method lists (2.6 to 2.10, 2.13: 'may include', 'some of the following', 'such as'): each paragraph is one statement; the list items (2.6.b1 to 2.13.b4 in the skeleton) are not cut as statements because the issuer offers them as a menu. For P3.
- Plain-present provider norms and content lists, not statements (template open point 5): 1.6 and 1.8 (what criminology is concerned with; core areas courses 'include'), 2.24 ('courses ... include'), 2.30 ('Most Criminology courses ... will include'), 3.1 (debates that characterise the field), 3.9 (assessment 'take[s] account of, as a minimum'), 4.3 ('this will include'), and the 'students are given opportunities' sentences in 3.6 items a to c. 1.6, 1.8 and 3.1 are recorded as SB3 areas.
- Not recorded though worded with will or should: 1.2 and 4.1 (what the statement sets out), 1.7 (a reading instruction), 2.33 ('Typically, external examiners will be asked': descriptive), 1.25 and 1.26 (descriptive).
- 3.6 has lettered items a) to d) inside one numbered paragraph; cut as 3.6.b1 to 3.6.b4 by find, in the issuer's order.
- Stage words in section 2 ('basic', 'higher or more advanced', 'higher or postgraduate', 'all levels') are stages of study, not framework levels; honours-only records carry the award's level fheq:6, mixed honours and postgraduate records carry level none.
- Provider duties carry domain none, as in Psychology run 0043; SB-4 asks for one of the four values on every benchmark standard. For Abbott.
- Subject codes: HECoS 100484 criminology (stated, by name); HECoS 100483 criminal justice (stated as a postgraduate specialism, 1.4); CAH15-01-02 is inferred, being HECoS 100484's CAH3 mapping, labelled sociology, which the text does not name as this subject. Policing (100486) and forensic psychology (100387) appear only in S2 statedSubjects as specialisms (1.4), not in the lookup subjects.
- Inferred gradeOf link: 2.3 to 2.2.typical. All 22 table links are stated by row.
- Inferred crosswalk: fheq:7 to fqheis:11 (from the FHEQ document, not this one).
- No CQFW citation in the text; Wales appears only through the Quality Assessment Framework for Wales in the front matter.
- Front matter (excluded) names the Office for Students' regulatory framework, the Quality Assessment Framework for Wales, the Quality Enhancement Framework (Scotland), the Quality Code's Advice and Guidance and QAA's Glossary; back matter names the Disabled Students' Commission. Not in SB6, being in excluded matter.
- The issuer's sub-headings run into the end of the preceding paragraph in the held text (for example 'Purposes of a Criminology degree' ends 1.4), so some `source` spans end with the next heading.
- Extraction artefacts in the held text: 'saf e' (1.11, 1.12, 1.13), 'successf ul' (1.25, 4.6.b6), 'f ast' (2.13). Sources carry them as held.
- Employability is named with entrepreneurship and enterprise in the key changes and in 1.25 to 1.27; recorded under theme:enterprise, no separate theme id.
- Partners named in 2.27 to 2.29 (police forces, Ministry of Justice, Europol, UNODC, charities and NGOs) are research partners, not PSRBs; grouped as one SB6 body entry, not in SB5.
- Section order differs from Psychology: the cross-cutting themes sit inside section 1, and research-methods expectations by level sit in section 2 before the section 4 table.
- ESD pages on QAA's website (1.23) not ingested; the ESD guidance itself is std:doc:qaa-advancehe-esd-2021-guidance.
- SB-10: 4.2 cites level 6 and level 10 'of the respective qualification frameworks' without naming the FHEQ or FQHEIS; recorded in SB6 for both frameworks.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:55: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0098 (P1); built by tools/bm_build.py.
