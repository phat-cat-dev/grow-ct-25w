---
id: std:doc:qaa-computing-2022-benchmarks
title: "Subject Benchmark Statement Computing"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "cah", code: "CAH11-01", label: "computing", basis: "inferred" }
  - { scheme: "hecos", code: "100366", label: "computer science", basis: "inferred" }
  - { scheme: "hecos", code: "100162", label: "computer systems engineering", basis: "inferred" }
  - { scheme: "hecos", code: "100374", label: "software engineering", basis: "inferred" }
  - { scheme: "hecos", code: "100367", label: "computing and information technology", basis: "inferred" }
  - { scheme: "hecos", code: "100371", label: "information systems", basis: "inferred" }
  - { scheme: "hecos", code: "100376", label: "computer and information security", basis: "inferred" }
edition: "March 2022 (fifth edition)"
published: 2022-03
status: current
supersedes: "the fourth edition, Computing (2019), and the separate Computing (Master's) statement (2019), which this edition brings together in one statement (D1, front matter; 1.2; back matter)"
heldText: { method: sha256-bytes, raw: 5985a0eb13fe5b3911daa6fdf70721dc5fb0701ce88aef32b42d09be009ce518, normalised: 3ca70f64d0984e655598dfabf1b04bbefc53867a3b165e556a0ee71c5a8d8cc3 }
heldTextStan: { method: sha256-stan, raw: 5985a0eb13fe5b3911daa6fdf70721dc5fb0701ce88aef32b42d09be009ce518, normalised: 3e90d965f44c59e357022c3485bb223522a49e996b505ef50a6e112035bdc277 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, the 2022 revision with cross-cutting themes; this statement's fifth edition (D1, back cover)"
awardsCovered: ["bachelor's with honours", "integrated master's", "master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0095 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:57"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Computing (QAA, March 2022)

> Run 0095, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2022-computing-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what graduates in computing should know, understand and be able to do, in one statement for three awards: bachelor's degrees with honours, integrated undergraduate master's degrees and taught postgraduate master's degrees, degree apprenticeships included. Reach for it when designing, approving, reviewing or describing a computing course or its outcomes, when placing a student's work against the threshold, typical and excellent rungs or when building employability, inclusion, accessibility or sustainability into a computing curriculum. It is a sector reference point, not a syllabus, a regulation or a professional body's accreditation standard.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2022 as the fifth edition, the statement joins the earlier bachelor's and master's computing statements. It sets out the context and purposes of a computing degree with the cross-cutting themes of equality, diversity and inclusion, sustainability (education for sustainable development) and entrepreneurship and enterprise education, read as employability, with a long list of employability skills; the distinctive features of course design (seven discipline areas built on computer science and seven fundamental requirements), accessibility, progression, flexibility, partnership and review; and content, teaching and assessment. The benchmark standards are two tables: an undergraduate table of six outcome categories at threshold, typical and excellent, mapped to third, second and first-class honours; and a master's table of six categories at typical and excellent only, mapped to Pass/Merit and Distinction, with the master's threshold required by reference. Integrated master's graduates meet the threshold at both levels. It cites the FHEQ and FQHEIS levels 6 and 7 (10 and 11), Annex D, the ESD and enterprise guidance, and names the British Computer Society, the Institute for Apprenticeships and Technical Education, the Engineering Council and the ACM and IEEE.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Computing"
edition: "March 2022 (fifth edition)"
dates:
  published: 2022-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector-owned reference point, not a regulatory requirement; a key reference point in Wales and Scotland and part of the quality requirements in Northern Ireland, not a sector-recognised standard in England (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2022", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what graduates in computing can be expected to know, understand and do on bachelor's honours, integrated master's and taught master's courses, at threshold, typical and excellent rungs, with employability skills and the context for course design, teaching and assessment"
appliesTo:
  awards: ["bachelor's with honours", "integrated master's", "master's"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This Subject Benchmark Statement refers to courses of study in Computing, including: bachelor's degrees with honours; integrated undergraduate master's degrees; postgraduate degrees that are generalist in nature; postgraduate degrees that are specialist in nature; courses designed to be studied in part-time mode at both undergraduate and postgraduate levels; undergraduate and postgraduate degree apprenticeships.\" (D1, 1.1)"
statedSubjects:
  - { name: "Computing", locator: "(D1, 1.1; 1.5; 3.1)", kind: "subject", codes: [{ scheme: "cah", code: "CAH11-01", label: "computing" }] }
  - { name: "computer science", locator: "(D1, 2.1; Appendix 3)", kind: "discipline area", codes: [{ scheme: "hecos", code: "100366", label: "computer science" }] }
  - { name: "computer engineering", locator: "(D1, 2.1; Appendix 3)", kind: "discipline area", codes: [{ scheme: "hecos", code: "100162", label: "computer systems engineering" }] }
  - { name: "software engineering", locator: "(D1, 2.1; Appendix 3)", kind: "discipline area", codes: [{ scheme: "hecos", code: "100374", label: "software engineering" }] }
  - { name: "information technology", locator: "(D1, 2.1; Appendix 3)", kind: "discipline area", codes: [{ scheme: "hecos", code: "100367", label: "computing and information technology" }] }
  - { name: "information systems", locator: "(D1, 2.1; Appendix 3)", kind: "discipline area", codes: [{ scheme: "hecos", code: "100371", label: "information systems" }] }
  - { name: "cybersecurity", locator: "(D1, 2.1; Appendix 3)", kind: "discipline area", codes: [{ scheme: "hecos", code: "100376", label: "computer and information security" }] }
  - { name: "data science", locator: "(D1, 2.1; Appendix 3)", kind: "discipline area", codes: [] }
  - { name: "computer networking; games; multimedia; artificial intelligence; health informatics", locator: "(D1, 2.3)", kind: "specialism", codes: [{ scheme: "hecos", code: "100365", label: "computer networks" }, { scheme: "hecos", code: "101267", label: "computer games" }, { scheme: "hecos", code: "100737", label: "multimedia computing science" }, { scheme: "hecos", code: "100359", label: "artificial intelligence" }, { scheme: "hecos", code: "100994", label: "health informatics" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: stem, parent: "section 1", heading: "Context", gloss: "the courses covered, from honours to degree apprenticeships" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "a merged review of earlier statements; ACM and IEEE curricula for detail" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "a reference point for joint courses with a large computing core" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes of a Computing degree", gloss: "why people study computing; equity and the SDGs" }
  - { number: "1.5", order: 7, componentType: stem, parent: "section 1", heading: "Characteristics of a Computing degree", gloss: "what the discipline is concerned with and does" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Computing degree", gloss: "innovation, disciplined problem-solving and abstraction" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Computing degree", gloss: "innovation from theory as well as technology" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Computing degree", gloss: "varied course titles; other sources a provider may need" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Computing degree", gloss: "graduate outcomes rather than a core curriculum" }
  - { number: "1.10", order: 12, componentType: practice, parent: "section 1", heading: "Characteristics of a Computing degree", gloss: "placements and early professional competence" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "a culturally responsive curriculum and unbiased technology" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "representing all students; the gender imbalance" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "how course structure affects students; reasonable adjustments" }
  - { number: "1.14", order: 16, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "an auditable list of EDI practices for courses to consider" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainable development in computing courses; the ESD guidance" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "the broad sense of sustainability in the curriculum" }
  - { number: "1.17", order: 19, componentType: stem, parent: "section 1", heading: "Sustainability", gloss: "the SDGs and four common ways of teaching sustainability" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "graduates appreciate sustainability issues in their field" }
  - { number: "1.19", order: 21, componentType: stem, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "employability and enterprise skills for computing courses" }
  - { number: "2.1", order: 23, componentType: area, parent: "section 2", heading: "Design", gloss: "computing degrees and their seven discipline areas" }
  - { number: "2.2", order: 24, componentType: area, parent: "section 2", heading: "Design", gloss: "no syllabus; the ACM and IEEE curricula inform design" }
  - { number: "2.3", order: 25, componentType: area, parent: "section 2", heading: "Design", gloss: "specialist degrees count when a discipline area informs them" }
  - { number: "2.4", order: 26, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "joint and interdisciplinary courses" }
  - { number: "2.5", order: 27, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "course titles and the dominant discipline area" }
  - { number: "2.6", order: 28, componentType: stem, parent: "section 2", heading: "Design", gloss: "the fundamental requirements of every computing degree" }
  - { number: "2.7", order: 29, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "computing's responsibility to disabled people" }
  - { number: "2.8", order: 30, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "universal access in teaching and practice" }
  - { number: "2.9", order: 31, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "accessible curriculum design; the statutory minimum" }
  - { number: "2.10", order: 32, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through honours; readiness for postgraduate study" }
  - { number: "2.11", order: 33, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "skills for joint honours students" }
  - { number: "2.12", order: 34, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's structure, exit awards, Scottish honours" }
  - { number: "2.13", order: 35, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible education and wider access" }
  - { number: "2.14", order: 36, componentType: stem, parent: "section 2", heading: "Flexibility", gloss: "kinds of flexibility in delivery, study, assessment and entry" }
  - { number: "2.15", order: 37, componentType: practice, parent: "section 2", heading: "Partnership", gloss: "work-based learning and study abroad through partnership" }
  - { number: "2.16", order: 38, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "a pointer to further guidance on partnerships" }
  - { number: "2.17", order: 39, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "collaboration with outside organisations; advisory boards" }
  - { number: "2.18", order: 40, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.19", order: 41, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.20", order: 42, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "2.21", order: 43, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation by professional bodies" }
  - { number: "2.22", order: 44, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "learners in monitoring and review" }
  - { number: "3.1", order: 46, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "computing defined; talent-based recruitment" }
  - { number: "3.2", order: 47, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "degrees and micro-credentials for learner-earners" }
  - { number: "3.3", order: 48, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "stakeholders, international bodies and future skills" }
  - { number: "3.4", order: 49, componentType: practice, parent: "section 3", heading: "Content", gloss: "balance of skills; capstone and teamwork encouraged" }
  - { number: "3.5", order: 50, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "evidencing competence in applied contexts" }
  - { number: "3.6", order: 51, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "learner agency, reflection and personalised assessment" }
  - { number: "3.7", order: 52, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching for capability and competence" }
  - { number: "3.8", order: 53, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "competence through practical work at scale" }
  - { number: "3.9", order: 54, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching that builds reflective, adaptable learners" }
  - { number: "3.10", order: 55, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "research-informed, inclusive curriculum design" }
  - { number: "3.11", order: 56, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "from breadth to focus; generalist and specialist master's" }
  - { number: "3.12", order: 57, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "curriculum, outcomes and individual competence" }
  - { number: "3.13", order: 58, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "resources and staff development" }
  - { number: "3.14", order: 59, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "legitimacy for integrated specialist master's" }
  - { number: "3.15", order: 60, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "grounding knowledge and applying it for lifelong learning" }
  - { number: "3.16", order: 61, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "applied learning, team projects and industry partners" }
  - { number: "3.17", order: 62, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "varied, authentic assessment" }
  - { number: "3.18", order: 63, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "academic integrity and assessment design" }
  - { number: "3.19", order: 64, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "the capstone activity" }
  - { number: "3.20", order: 65, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "capstone formats; research literature at master's level" }
  - { number: "4.1", order: 67, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the minimum threshold standards and the awards they cover" }
  - { number: "4.2", order: 68, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "standards set against FHEQ and FQHEIS levels; accreditors" }
  - { number: "4.3", order: 69, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed threshold; Annex D for degree classes" }
  - { number: "4.4", order: 70, componentType: paragraph, parent: "section 4", heading: "Undergraduate standards: threshold, typical and excellent descriptors", gloss: "three levels of attainment" }
  - { number: "4.5", order: 71, componentType: paragraph, parent: "section 4", heading: "Undergraduate standards: threshold, typical and excellent descriptors", gloss: "honours: threshold required; rungs linked to classes" }
  - { number: "4.6", order: 72, componentType: paragraph, parent: "section 4", heading: "Undergraduate standards: threshold, typical and excellent descriptors", gloss: "a pointer to the master's paragraphs; the undergraduate rung table" }
  - { number: "4.7", order: 73, componentType: paragraph, parent: "section 4", heading: "Postgraduate degrees", gloss: "kinds of postgraduate computing degree" }
  - { number: "4.8", order: 74, componentType: paragraph, parent: "section 4", heading: "Postgraduate degrees", gloss: "what all master's graduates have" }
  - { number: "4.9", order: 75, componentType: paragraph, parent: "section 4", heading: "Postgraduate degrees", gloss: "research, specialist and professional master's graduates" }
  - { number: "4.10", order: 76, componentType: paragraph, parent: "section 4", heading: "Postgraduate degrees", gloss: "where master's graduates go next" }
  - { number: "4.11", order: 77, componentType: paragraph, parent: "section 4", heading: "Postgraduate degrees", gloss: "not every category fits every postgraduate course" }
  - { number: "4.12", order: 78, componentType: paragraph, parent: "section 4", heading: "Postgraduate degrees", gloss: "postgraduate content aligned to level 7 or 11" }
  - { number: "4.13", order: 79, componentType: paragraph, parent: "section 4", heading: "Postgraduate degrees", gloss: "postgraduate threshold required; Pass" }
  - { number: "4.14", order: 80, componentType: paragraph, parent: "section 4", heading: "Postgraduate degrees", gloss: "typical and excellent for master's; the postgraduate rung table" }
  - { number: "4.15", order: 81, componentType: paragraph, parent: "section 4", heading: "Integrated undergraduate master's degrees", gloss: "integrated master's build on honours; their length" }
  - { number: "4.16", order: 82, componentType: paragraph, parent: "section 4", heading: "Integrated undergraduate master's degrees", gloss: "the master's characteristics apply" }
  - { number: "4.17", order: 83, componentType: paragraph, parent: "section 4", heading: "Integrated undergraduate master's degrees", gloss: "integrated master's: threshold at both levels" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Computing degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Computing degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points", kind: "other: front matter, read for S1 and S2" }
  - { number: "section headings 1 to 4", heading: "the four section heading lines", kind: "other: heading lines" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for S7 and SB6" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for Computing", kind: "other: back matter, read for S8 (editions)" }
  - { number: "Appendix 1", heading: "Mapping and audit templates", kind: "other: blank EDI mapping and audit templates, read for SB2" }
  - { number: "Appendix 2", heading: "Examples of ESD approaches", kind: "other: illustrative examples, read for SB2 and SB6" }
  - { number: "Appendix 3", heading: "Foundations of computer science courses", kind: "other: the discipline areas and ACM curricula, read for SB1 and SB3" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 110 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/computing-2022/1.11
  locator: { number: "1.11", headingPath: ["Context and purposes of a Computing degree", "Equality, diversity and inclusion"] }
  span: { start: 13928, end: 14793 }
  source: "1.11 The pervasiveness of the computing discipline can enable a curriculum which is relevant and authentic, relates to real and current challenges, and able to promote greater social justice and equity. The curriculum should also speak to and be valued by every student, while addressing issues that are important to them. Culturally responsive computing approaches that recognise and value students' cultures can bring about ways for students to reflect and engage with issues of representation, exclusion, disadvantage and structurally embedded advantage. The curriculum should engage students in meaningful, culturally- contexed practical tasks in a welcoming and collaborative environment, as well as ensuring that technological solutions do not emerge with unintentional bias and limited insight into the diversity of the people who will develop and use them.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "computing curricula"
  addressee: provider
  verbs: ["speak", "engage", "ensuring"]
  about: "a culturally responsive curriculum"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Because computing reaches everywhere, a curriculum can be authentic, tied to real problems and a force for social justice; it should matter to every student and be valued by them, and should give students culturally grounded practical work in a welcoming, collaborative setting, so that the technology they build carries no unintended bias."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of a Computing degree", "Equality, diversity and inclusion"] }
  span: { start: 14793, end: 15202 }
  source: "1.12 Curricula should therefore actively represent all students, acknowledging and removing existing biases, and enabling and supporting all students equally. For example, traditionally, the computer science field has suffered from gender imbalance, in part as a result of structurally genderised terminology, approaches to teaching and learning and the historical context in which the subject has developed.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "computing curricula"
  addressee: provider
  verbs: ["represent"]
  about: "a curriculum that represents all students"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Curricula should therefore represent every student, recognising and removing the biases already present and supporting all students equally; the gender imbalance in computer science, partly the product of gendered terms, teaching habits and history, is the example given."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/1.15
  locator: { number: "1.15", headingPath: ["Context and purposes of a Computing degree", "Sustainability"] }
  span: { start: 19763, end: 20362 }
  source: "1.15 Computing courses should address the sustainable development agenda through highlighting key economic, social and environmental issues that the discipline influences, whether positively or negatively. Courses should enable students to develop core personal and professional competencies to address the key societal challenges highlighted by the United Nations Sustainable Development Goals for 2030 in their future working lives. The Education for Sustainable Development Guidance (QAA and Advance HE, 2021) outlines pedagogic approaches for implementation in UK higher education institutions.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "computing courses"
  addressee: provider
  verbs: ["address", "enable"]
  about: "sustainable development in computing courses"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Computing courses should take up the sustainable development agenda by pointing to the economic, social and environmental issues the discipline affects for good or ill, and should help students build the personal and professional competencies to meet the challenges named in the UN Sustainable Development Goals in their later careers; the QAA and Advance HE ESD guidance sets out teaching approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/1.16
  locator: { number: "1.16", headingPath: ["Context and purposes of a Computing degree", "Sustainability"] }
  span: { start: 20362, end: 21265 }
  source: "1.16 Across the Computing curriculum, we should be considering the broad definition of sustainable development, which encompasses economic and social sustainable development as well as environmental, and thinking about how the material that we teach links to these goals. There will be places where environmental sustainability can be discussed, for example, the resource consumption of massive data centres used for cloud computing, and more generally, the environmental costs of both building hardware to support computing and disposing of electronic waste. Sustainable development also links with equality, diversity and inclusion; therefore, issues around social justice and economic prosperity can also be brought into the discussion in many areas of computing, alongside developing curricula that are global in outlook and that support inclusive lifelong learning and economic prosperity for all.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the computing subject community and its teachers"
  addressee: provider
  verbs: ["considering"]
  about: "the broad sense of sustainable development"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "The subject community should take sustainable development in its broad sense, economic and social as well as environmental, and think how its teaching links to it: data centre energy use, the cost of making hardware and e-waste are environmental examples, and the link with EDI brings in social justice, prosperity and a global, inclusive approach to lifelong learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of a Computing degree", "Sustainability"] }
  span: { start: 22728, end: 22967 }
  source: "1.18 Irrespective of the approach adopted, the intention is that Computing graduates should have an appreciation of domain-relevant issues related to sustainable development and the emergent manner by which these issues might be addressed."
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["have"]
  about: "appreciating sustainability issues in computing"
  themes: [theme:esd]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Whatever approach a course takes, computing graduates should appreciate the sustainable development issues that bear on their field and the ways those issues are starting to be tackled."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b1
  locator: { number: "1.19.b1", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 24071, end: 24131 }
  source: "Ability to work with professional and behavioural integrity."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["work"]
  about: "professional integrity"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Generic skills for computing courses to build in as part of employability: acting with integrity in professional conduct and behaviour."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b2
  locator: { number: "1.19.b2", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 24134, end: 24237 }
  source: "Awareness of the legal and ethical factors and principles in the professional environment of computing."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: []
  about: "legal and ethical awareness"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Generic skills for computing courses to build in as part of employability: awareness of the legal and ethical principles that govern professional computing work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b3
  locator: { number: "1.19.b3", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 24240, end: 24322 }
  source: "Awareness of sustainability issues related to the computing discipline/profession."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: []
  about: "sustainability awareness"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Generic skills for computing courses to build in as part of employability: awareness of the sustainability issues that computing raises as a discipline and a profession."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b4
  locator: { number: "1.19.b4", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 24325, end: 24388 }
  source: "Demonstrable understanding of computing as a global profession."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: []
  about: "computing as a global profession"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Generic skills for computing courses to build in as part of employability: an evident understanding that computing is practised as a global profession."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b5
  locator: { number: "1.19.b5", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 24391, end: 24579 }
  source: "Responsible use and application of social media in a professional environment. This to include professional online communication, email etiquette and the development of an online presence."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["include"]
  about: "professional use of social media"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Generic skills for computing courses to build in as part of employability: using social media responsibly at work, including professional online communication, email conduct and building an online presence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b6
  locator: { number: "1.19.b6", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 24582, end: 24692 }
  source: "Critical reflection skills and the ability to communicate effectively in writing, verbally and electronically."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["communicate"]
  about: "critical reflection and communication"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Generic skills for computing courses to build in as part of employability: critical reflection and clear communication in writing, in speech and online."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b7
  locator: { number: "1.19.b7", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 24695, end: 24742 }
  source: "Apply a high standard of numeracy and literacy."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["apply"]
  about: "numeracy and literacy"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Generic skills for computing courses to build in as part of employability: a high standard of numeracy and literacy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b8
  locator: { number: "1.19.b8", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 24745, end: 24814 }
  source: "Ability to interact with others in a professional and respectful way."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["interact"]
  about: "respectful professional interaction"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Generic skills for computing courses to build in as part of employability: dealing with others professionally and with respect."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b9
  locator: { number: "1.19.b9", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 24817, end: 25053 }
  source: "Understand and demonstrate respect for the values of equality and diversity across a range of different industries and business sectors within the broad computing professional workplace (see Equality, diversity and inclusion on page 4)."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["understand", "demonstrate"]
  about: "respect for equality and diversity"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Generic skills for computing courses to build in as part of employability: understanding and showing respect for equality and diversity across the many sectors where computing professionals work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b10
  locator: { number: "1.19.b10", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25056, end: 25162 }
  source: "Understand the role of a leader in setting directions and taking responsibility for actions and decisions."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["understand"]
  about: "the role of a leader"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Generic skills for computing courses to build in as part of employability: understanding what a leader does in setting direction and owning actions and decisions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b11
  locator: { number: "1.19.b11", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25165, end: 25230 }
  source: "Communicate with confidence at face-to-face and virtual meetings."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["communicate"]
  about: "confident communication in meetings"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Generic skills for computing courses to build in as part of employability: communicating confidently in meetings held in person or online."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b12
  locator: { number: "1.19.b12", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25248, end: 25343 }
  source: "Ability to work with agility and flexibility in response to changing situations and priorities."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["work"]
  about: "agility and flexibility"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Agile working for computing courses to build in as part of employability: working with agility and flexibility as situations and priorities change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b13
  locator: { number: "1.19.b13", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25349, end: 25454 }
  source: "Ability to interpret data and information within both academic and professional contexts in a timely way."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["interpret"]
  about: "timely interpretation of data"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Agile working for computing courses to build in as part of employability: interpreting data and information promptly in academic and professional settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b14
  locator: { number: "1.19.b14", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25457, end: 25554 }
  source: "Ability to recognise and make best use of the skills and knowledge of individuals to collaborate."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["recognise", "make", "collaborate"]
  about: "drawing on others' strengths to collaborate"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Agile working for computing courses to build in as part of employability: recognising and drawing on other people's skills and knowledge in order to collaborate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b15
  locator: { number: "1.19.b15", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25557, end: 25678 }
  source: "Ability to identify problems and desired outcomes and negotiate with colleagues to achieve mutually acceptable solutions."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["identify", "negotiate", "achieve"]
  about: "negotiating solutions"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Agile working for computing courses to build in as part of employability: identifying problems and wanted outcomes and negotiating with colleagues towards solutions all can accept."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b16
  locator: { number: "1.19.b16", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25697, end: 25763 }
  source: "Ability to work unsupervised, plan effectively and meet deadlines."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["work", "plan", "meet"]
  about: "working unsupervised to deadlines"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Remote working for computing courses to build in as part of employability: working without supervision, planning well and meeting deadlines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b17
  locator: { number: "1.19.b17", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25766, end: 25817 }
  source: "Ability to act confidently on one's own initiative."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["act"]
  about: "acting on own initiative"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Remote working for computing courses to build in as part of employability: acting with confidence on their own initiative."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b18
  locator: { number: "1.19.b18", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25832, end: 25894 }
  source: "Build social capital and apply professional networking skills."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["build", "apply"]
  about: "networking and social capital"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Resilience for computing courses to build in as part of employability: building social capital and using professional networking skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b19
  locator: { number: "1.19.b19", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 25897, end: 26055 }
  source: "Maintain an up-to-date critical understanding of the developments, challenges and opportunities of the professional environment, both nationally and globally."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["maintain"]
  about: "keeping up with the profession"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Resilience for computing courses to build in as part of employability: keeping a current, critical understanding of developments, challenges and opportunities in the profession, at home and worldwide."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b20
  locator: { number: "1.19.b20", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 26058, end: 26232 }
  source: "The ability to succinctly present rational and reasoned arguments that address a given problem or opportunity, to a range of audiences (orally, electronically or in writing)."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["present", "address"]
  about: "presenting reasoned arguments"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Resilience for computing courses to build in as part of employability: presenting rational, reasoned arguments concisely on a given problem or opportunity to varied audiences, orally, online or in writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b21
  locator: { number: "1.19.b21", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 26278, end: 26335 }
  source: "Active engagement in continuous professional development."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: []
  about: "continuing professional development"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Entrepreneurship and enterprise education for computing courses to build in as part of employability: active engagement in continuing professional development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b22
  locator: { number: "1.19.b22", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 26338, end: 26448 }
  source: "Contribute to the development of the profession and ability to apply an enterprising and challenging approach."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["contribute", "apply"]
  about: "enterprise and contribution to the profession"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Entrepreneurship and enterprise education for computing courses to build in as part of employability: contributing to the development of the profession and bringing an enterprising, challenging approach."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b23
  locator: { number: "1.19.b23", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 26451, end: 26605 }
  source: "The ability to locate and retrieve relevant ideas and ensure that these can be effectively communicated in a variety of formats to a variety of audiences."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["locate", "retrieve", "ensure"]
  about: "finding and communicating ideas"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Entrepreneurship and enterprise education for computing courses to build in as part of employability: finding and retrieving relevant ideas and making sure they can be communicated well in varied formats to varied audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b24
  locator: { number: "1.19.b24", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 26608, end: 26765 }
  source: "Recognise factors in environmental and societal contexts which present opportunities and challenges for computing systems across a range of human activities."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["recognise", "present"]
  about: "opportunities and challenges in context"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Entrepreneurship and enterprise education for computing courses to build in as part of employability: recognising environmental and social factors that open opportunities or pose challenges for computing systems across human activity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b25
  locator: { number: "1.19.b25", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 26819, end: 27062 }
  source: "The subject-specific computing knowledge and skills specified elsewhere in this Subject Benchmark Statement will form the basis of the body of knowledge that an employer could reasonably expect a Computing graduate to be able to use and apply."
  stem: "1.19"
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["form", "use", "apply"]
  about: "subject knowledge employers can rely on"
  themes: [theme:enterprise]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "The computing knowledge and skills set out across the statement will make up the body of knowledge an employer can fairly expect a computing graduate to use and apply."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b26
  locator: { number: "1.19.b26", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 27065, end: 27255 }
  source: "Graduates should be able to link subject knowledge to business and industry by discussing examples and cases studies of how their subject knowledge of computing can be used by organisations."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["link", "discussing"]
  about: "linking computing to business and industry"
  themes: [theme:enterprise]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Graduates should be able to connect their computing knowledge to business and industry, discussing examples and case studies of how organisations put it to use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b27
  locator: { number: "1.19.b27", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 27258, end: 27448 }
  source: "Application of computing knowledge and computational thinking to solve complex problems to the benefit and enhancement of the organisation or enterprise that the graduate will be working in."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["solve"]
  about: "applying computational thinking to complex problems"
  themes: [theme:enterprise]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Subject-specific skills in computing (common core) for computing courses to build in as part of employability: using what they know of computing, with computational thinking, to crack complex problems for the benefit of the organisation the graduate works in."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b28
  locator: { number: "1.19.b28", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 27451, end: 27657 }
  source: "Ability to continuously plan and record self-learning and development in core computing skills and applications of technology as the foundation for lifelong learning and continuous professional development."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["plan", "record"]
  about: "planning and recording self-learning"
  themes: [theme:enterprise]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A skill listed under Subject-specific skills in computing (common core) for computing courses to build in as part of employability: planning and recording their own learning in core computing skills and technologies throughout, as a basis for lifelong learning and CPD."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b30
  locator: { number: "1.19.b30", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 28004, end: 28371 }
  source: "Interdisciplinary teamwork and creative thinking are important employability skills for computing students. Interdisciplinary thinking promotes innovation, open- mindedness and creativity. Due to the interdisciplinary nature of computing, graduates should be able to apply computer science, data science and digital technology to problem-solving in other disciplines."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["apply"]
  about: "applying computing in other disciplines"
  themes: [theme:enterprise]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Interdisciplinary teamwork and creative thinking are valued employability skills that foster innovation and open minds; since computing is interdisciplinary, graduates should be able to bring computer science, data science and digital technology to bear on problems in other fields."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b32
  locator: { number: "1.19.b32", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 28787, end: 29358 }
  source: "There is a huge range of different employment pathways open to graduates of computing across organisation types: public and private sector, start-ups, scale- ups, small to large enterprises; and role discipline: software engineer, cybersecurity, data ethics; the list continues to grow. Graduates of computing should build an understanding of potential employment pathways, their differing skills requirements together with a self-awareness of personal skillsets, covering both technical and more generic employability skills and how to match these to career aspirations."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["build", "match"]
  about: "understanding career pathways"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Computing graduates can follow many routes across organisation types and roles; they should build an understanding of those routes and their differing skill demands, know their own technical and wider employability skills and see how to match these to their career aims."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b33
  locator: { number: "1.19.b33", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 29361, end: 29657 }
  source: "Graduates should have the ability to communicate effectively how study and experience provides evidence of personal strengths and skills and how these can be effectively articulated to prospective employers, including the use of social media platforms to support professional profile development."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["communicate"]
  about: "articulating strengths to employers"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Graduates should be able to show employers how their study and experience evidence their strengths and skills, using social media to build a professional profile among other means."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b34
  locator: { number: "1.19.b34", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 29660, end: 29872 }
  source: "Careers within computing have a high requirement for continuing professional development (CPD) and courses should encourage students to explore how to access CPD and how to build this into future career planning."
  stem: "1.19"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "computing courses"
  addressee: provider
  verbs: ["encourage", "explore"]
  about: "continuing professional development in career planning"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Computing careers depend heavily on continuing professional development, so courses should encourage students to find out how to access CPD and to plan it into their careers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/1.19.b35
  locator: { number: "1.19.b35", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 29875, end: 30105 }
  source: "Course planning and development should include working with employers wherever possible, to identify co-curricular activities such as bootcamps, hackathons, master classes and the development of authentic assessment opportunities."
  stem: "1.19"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course planning and development"
  addressee: provider
  verbs: ["include", "identify"]
  about: "working with employers on course planning"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Course planning and development should involve employers wherever it can, to find co-curricular activities such as bootcamps, hackathons and master classes and to develop authentic assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/1.19.b36
  locator: { number: "1.19.b36", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 30132, end: 30350 }
  source: "Courses should encourage students to explore the potential role of digital technologies within the workplace and how to apply appropriate digital technologies, techniques and principles to advance digital capabilities."
  stem: "1.19"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "computing courses"
  addressee: provider
  verbs: ["encourage", "explore", "apply"]
  about: "digital technologies in the workplace"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Courses should encourage students to explore what digital technologies can do in the workplace and how to apply suitable technologies, techniques and principles to raise digital capability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/1.19.b37
  locator: { number: "1.19.b37", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 30353, end: 30565 }
  source: "Employers will expect graduates to be able to demonstrate core skills required to apply and advance digital technologies within the workplace and the development of these skills should be included within courses."
  stem: "1.19"
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "computing graduates and courses"
  addressee: both
  verbs: ["expect", "demonstrate", "included"]
  about: "core digital skills employers expect"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Employers will expect graduates to show the core skills needed to apply and advance digital technologies at work, and courses should include the development of those skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b38
  locator: { number: "1.19.b38", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 30568, end: 30756 }
  source: "Collaboration and teamwork: capability to work with other people, from a range of cultures, to achieve common goals, for example through group work, group projects and group presentations."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["work", "achieve"]
  about: "teamwork across cultures"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A core skill employers will expect computing graduates to show: the capability to work with people from a range of cultures towards shared goals, as in group work, group projects and group presentations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b39
  locator: { number: "1.19.b39", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 30759, end: 30924 }
  source: "Self-management: a readiness to accept responsibility and flexibility, to be resilient, self-starting and appropriately assertive, to plan, organise and manage time."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["accept", "plan", "organise", "manage"]
  about: "self-management"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A core skill employers will expect computing graduates to show: the capability to take responsibility, be flexible and resilient, start things themselves, assert themselves fittingly and plan, organise and manage their time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b40
  locator: { number: "1.19.b40", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 30927, end: 31076 }
  source: "Self-reflection: self-analysis and an awareness/sensitivity to diversity in terms of people and cultures, showing emotional intelligence and empathy."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["showing"]
  about: "self-reflection and empathy"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A core skill employers will expect computing graduates to show: the capability to analyse themselves and show awareness of and sensitivity to diversity among people and cultures, with emotional intelligence and empathy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b41
  locator: { number: "1.19.b41", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 31083, end: 31203 }
  source: "Communication and listening: including the ability to produce clear, structured communications using a variety of media."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["produce"]
  about: "communication and listening"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A core skill employers will expect computing graduates to show: the capability to listen and produce clear, well-structured communications in varied media."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/1.19.b42
  locator: { number: "1.19.b42", headingPath: ["Context and purposes of a Computing degree", "Entrepreneurship and enterprise education"] }
  span: { start: 31206, end: 31368 }
  source: "Capability advancement: including networking with peers and horizon scanning to identify opportunities to advance digital capabilities and create a better future."
  stem: "1.19"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["identify", "advance", "create"]
  about: "capability advancement"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A core skill employers will expect computing graduates to show: the capability to network with peers and scan the horizon for chances to advance digital capability and improve the future."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/2.2
  locator: { number: "2.2", headingPath: ["Distinctive features of a Computing degree", "Design"] }
  span: { start: 31878, end: 32183 }
  source: "2.2 This Statement does not specify a syllabus or include a body of knowledge. ACM, in conjunction with IEEE and other professional societies, maintain and regularly update curricula in several discipline areas (Appendix 3). These documents should be used to inform course design and curriculum content.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course design and curriculum content"
  addressee: provider
  verbs: ["used", "inform"]
  about: "ACM and IEEE curricula to inform design"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "The statement gives no syllabus or body of knowledge; the ACM, with the IEEE and other societies, keeps curricula for several discipline areas up to date, and these should be used to inform course design and content."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/2.6.b1
  locator: { number: "2.6.b1", headingPath: ["Distinctive features of a Computing degree", "Design"] }
  span: { start: 33617, end: 33804 }
  source: "the topic and learning outcomes are identified and defined clearly, and their relationship to the subject of computing and its applications is carefully captured in the title of the award"
  stem: "2.6"
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "requirements" read as must
  level: none
  appliesTo: "all computing degree courses"
  addressee: provider
  verbs: ["identified", "defined", "captured"]
  about: "clear outcomes reflected in the award title"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "The topic and learning outcomes are clearly set out, and the award title captures how they relate to computing and its applications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/2.6.b2
  locator: { number: "2.6.b2", headingPath: ["Distinctive features of a Computing degree", "Design"] }
  span: { start: 33807, end: 33925 }
  source: "courses are carefully designed to accommodate students who enter with a wide range of accepted entrance qualifications"
  stem: "2.6"
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "requirements" read as must
  level: none
  appliesTo: "all computing degree courses"
  addressee: provider
  verbs: ["designed", "accommodate"]
  about: "design for varied entry qualifications"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Courses are designed with care to suit students entering with a wide range of accepted qualifications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/2.6.b3
  locator: { number: "2.6.b3", headingPath: ["Distinctive features of a Computing degree", "Design"] }
  span: { start: 33928, end: 34172 }
  source: "the relevant theoretical underpinnings, which may or may not be mathematical in nature, are identified and should result in emphasis on those fundamental aspects of a subject which do not change in the context of rapid technological development"
  stem: "2.6"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "all computing degree courses"
  addressee: provider
  verbs: ["identified", "result"]
  about: "theory that lasts despite rapid change"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "The relevant theory, mathematical or not, is identified and should lead to emphasis on the fundamentals of the subject that stay stable while technology changes fast."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/2.6.b4
  locator: { number: "2.6.b4", headingPath: ["Distinctive features of a Computing degree", "Design"] }
  span: { start: 34175, end: 34375 }
  source: "the curriculum demonstrates an integration between theory and practice as well as the planned development of a set of attitudes and an appreciation of a range of applications and their impact on users"
  stem: "2.6"
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "requirements" read as must
  level: none
  appliesTo: "all computing degree courses"
  addressee: provider
  verbs: ["demonstrates"]
  about: "integrating theory and practice"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "The curriculum joins theory and practice and plans how students' attitudes develop and how they come to appreciate a range of applications and their effect on users."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/2.6.b5
  locator: { number: "2.6.b5", headingPath: ["Distinctive features of a Computing degree", "Design"] }
  span: { start: 34378, end: 34526 }
  source: "there is an appropriate integration between a set of classes that demonstrates cohesion in content and a planned approach to the topic of the course"
  stem: "2.6"
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "requirements" read as must
  level: none
  appliesTo: "all computing degree courses"
  addressee: provider
  verbs: ["demonstrates"]
  about: "a cohesive set of classes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "The classes fit together, cohesive in content and planned as an approach to the topic of the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/2.6.b6
  locator: { number: "2.6.b6", headingPath: ["Distinctive features of a Computing degree", "Design"] }
  span: { start: 34533, end: 34831 }
  source: "a major component is a substantial individual activity, or team activity that provides substantial individual responsibility, that requires an awareness of material from across the individual modules and which provides opportunities for students to demonstrate a range of abilities and achievements"
  stem: "2.6"
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "requires" read as must
  level: none
  appliesTo: "all computing degree courses"
  addressee: provider
  verbs: ["requires", "provides", "demonstrate"]
  about: "a substantial individual or team activity"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A major part of the course is a substantial individual activity, or a team activity carrying substantial individual responsibility, that draws on material from across the modules and lets students show a range of abilities and achievements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/2.6.b7
  locator: { number: "2.6.b7", headingPath: ["Distinctive features of a Computing degree", "Design"] }
  span: { start: 34834, end: 35030 }
  source: "all undergraduate and master's degree courses will meet the outcomes of the qualification descriptors identified in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies."
  stem: "2.6"
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "all undergraduate and master's computing courses"
  addressee: provider
  verbs: ["meet"]
  about: "meeting the FHEQ qualification descriptors"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Every undergraduate and master's computing course will meet the outcomes of the qualification descriptors in the UK qualifications frameworks."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of a Computing degree", "Accessibility"] }
  span: { start: 35045, end: 35525 }
  source: "2.7 In any discussion of accessibility in computing education, it is important to recognise the unique responsibility that computing as a subject has to people with disabilities. Technology can be transformational: tasks that previously were difficult or impossible for some people can be made routine with the use of technology. However, technology can also cause barriers to access, and care should be taken to ensure technology acts to enable people rather than disable them.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "computing education"
  addressee: provider
  verbs: ["recognise", "taken", "ensure"]
  about: "computing's responsibility to disabled people"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Computing has a particular responsibility to disabled people: technology can make once hard or impossible tasks routine, but it can also raise barriers, so care should be taken that it enables rather than disables."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of a Computing degree", "Accessibility"] }
  span: { start: 35525, end: 36014 }
  source: "2.8 As such, when we discuss accessibility in respect of computing education it must encompass both the teaching and practice of universal access, following standards and ensuring compatibility with assistive technologies. In terms of curricula, accessibility should be treated as a standard part of computing. For example, where software development lifecycles are taught, accessibility should be embedded as a concern along with other concerns, such as the testing of software quality.\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "computing education and curricula"
  addressee: provider
  verbs: ["encompass", "treated", "embedded"]
  about: "universal access in teaching and practice"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Accessibility in computing education must cover both teaching and practising universal access, following standards and working with assistive technologies; in curricula it should be a standard part of computing, embedded, for example, beside quality testing wherever software lifecycles are taught."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of a Computing degree", "Accessibility"] }
  span: { start: 36014, end: 36465 }
  source: "2.9 In terms of practice, curricula should be designed with accessibility in mind, meeting statutory requirements as a minimum. Creating educational environments with accessibility as a primary concern can enable students to study computing when without such consideration, they would be unable to do so. For example, if a course requires students to regularly attend a physical location on campus, this may place barriers in the way of some students."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "curriculum design"
  addressee: provider
  verbs: ["designed", "meeting"]
  about: "accessible curriculum design"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Curricula should be designed with accessibility in mind and meet statutory requirements at the least; putting access first lets students study who otherwise could not, and a requirement to attend campus regularly is an example of a barrier."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of a Computing degree", "Progression"] }
  span: { start: 36479, end: 37200 }
  source: "2.10 Over the course of a degree with honours (FHEQ Level 6; FQHEIS Level 10) a Computing student will progress from one year of study to the next, in line with the regulations and processes for each institution. However, it is expected that each year would see the attainment of certain levels of knowledge, expertise and experience which builds towards the final achievement of meeting all of the threshold-level subject-specific and generic skills listed in this Statement. Upon graduation from an undergraduate degree, it would be expected that a student who had achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in computing or an associated discipline.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours students in computing"
  addressee: learner
  verbs: ["progress"]
  about: "progression towards the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An honours student will move from year to year under their institution's rules; each year is expected to add knowledge, expertise and experience towards meeting all the threshold subject and generic skills, and a graduate with a second-class degree or better is expected to be ready for postgraduate study in computing or a related subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of a Computing degree", "Progression"] }
  span: { start: 37200, end: 37384 }
  source: "2.11 Joint honours undergraduates will achieve elements of the specific and generic skills for the subject but will add others according to the subjects covered in a joint programme.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint honours students"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "joint honours skills"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Joint honours students will gain part of the subject and generic skills of computing and add others from their other subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of a Computing degree", "Monitoring and review"] }
  span: { start: 41489, end: 41802 }
  source: "2.19 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "providers in periodic review"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Externality is essential to UK quality assurance; providers will bring external reviewers into periodic review for an outside view of proposed changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/2.22
  locator: { number: "2.22", headingPath: ["Distinctive features of a Computing degree", "Monitoring and review"] }
  span: { start: 42825, end: 42993 }
  source: "2.22 Additionally, courses should also consider the inclusion of learners in their monitoring and review processes as part of their student-staff partnership work.\n\n15\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "computing courses"
  addressee: provider
  verbs: ["consider"]
  about: "learners in monitoring and review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Courses should also consider involving learners in monitoring and review as part of their partnership with students."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 45441, end: 46313 }
  source: "3.4 Pedagogically, educators should consider the balance between subject-specific and transferable skills development in both curriculum and assessment, opportunities for personalised learning and evidencing of individual capability and competency development within courses and the balance between educational and workforce requirements as courses are developed and maintained. The value of learning, in providing both learner-earner agency and value to society and the economy, should be both clear and wherever possible differentiated between learners. Problem-solving and artefact creation form core parts of the computing discipline and enabling learners to evidence these within a curriculum in ways they understand and can communicate with others are encouraged. The use of capstone activity as well as teamwork is encouraged within courses.\n\nTeaching and learning\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who teach and design computing courses"
  addressee: provider
  verbs: ["consider", "encouraged"]
  about: "balancing skills; capstone and teamwork"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Teachers should weigh subject-specific against transferable skills in curriculum and assessment, personalised learning and evidence of individual capability, as well as education against workforce needs; the value of learning should be clear, problem-solving and building artefacts are core, and capstone work and teamwork are encouraged."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/3.7
  locator: { number: "3.7", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 48073, end: 48518 }
  source: "3.7 Computing courses deploy a diverse range of teaching approaches, which is a strength of the subject. The teaching methods employed should have the potential to firstly deliver a range of learning that can be demonstrated through the achievement of learning outcomes, indicating capability. They should also ensure that learners have competence in specific areas of computing, which requires an ability to work independently in these areas.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "teaching methods in computing courses"
  addressee: provider
  verbs: ["employed", "deliver", "ensure"]
  about: "teaching for capability and competence"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Computing teaching is varied, which is a strength; the methods used should deliver learning shown through the learning outcomes, as evidence of capability, and should make sure learners gain competence in particular areas, which needs the ability to work independently in them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 48879, end: 49615 }
  source: "3.9 Teaching should encourage students to reflect, evaluate, select, justify, communicate and be innovative in their problem-solving; and prepare them to become adaptable independent learners throughout their lifelong learner-earner journey. Students should be exposed to a range of tools and techniques relevant to their course, including bespoke, open source and commercially available approaches. The diverse prior learning, capabilities, competencies and experiences should be understood and accommodated. Learning barriers should be minimised wherever possible to enable all learners to be as successful as possible. Equality, diversity and inclusion within the curriculum should be carefully considered as outlined in section 1.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "teaching in computing courses"
  addressee: provider
  verbs: ["encourage", "prepare", "exposed", "minimised", "considered"]
  about: "teaching for reflective, adaptable learners"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Teaching should get students to reflect, evaluate, select, justify, communicate and innovate in solving problems, and prepare them to be adaptable, independent learners for life; students should meet a range of bespoke, open source and commercial tools; varied prior learning should be understood and accommodated, barriers minimised and EDI carefully considered."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/3.10
  locator: { number: "3.10", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 49615, end: 50372 }
  source: "3.10 Curriculum design should reflect appropriate research, scholarship and the ability to make an informed choice as to which is the most appropriate approach to use in a specific context, alongside current industrial and business practices. Teaching needs to be placed within the context of the legal, social, ethical, professional, environmental and economic factors that are relevant to computing. In addition to technical subjects such as security, the curriculum should use an inclusive design approach and also include relevant aspects of sustainability as well as equality, diversity and inclusion. The attitudes and values of graduates should also be developed to enable them to thrive in a diverse and rapidly changing subject such as computing.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "curriculum design"
  addressee: provider
  verbs: ["reflect", "use", "include", "developed"]
  about: "research-informed, inclusive curriculum design"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Curriculum design should reflect research, scholarship and current industry practice and the ability to choose the right approach for a context; teaching sits within computing's legal, ethical, social, professional, economic and environmental setting; the curriculum should use inclusive design and cover sustainability and EDI, and graduates' attitudes and values should be developed for a diverse, fast-changing subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/3.11
  locator: { number: "3.11", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 50372, end: 51425 }
  source: "3.11 To ensure students have sufficient underpinning, the early stages of undergraduate courses will typically expose students to a broad range of computing topics, becoming more focused in the final year. Generalist master's, where no prior subject knowledge may have been studied, will typically focus on meeting the minimum subject knowledge required of a Computing graduate. Generalist master's may be designed to offer a broad underpinning or to focus on particular niche areas such as software testing. Specialist master's (and the final\n\n17\nyear of integrated undergraduate master's) will typically be more focused on specific aspects of the subject. In addition to increasing focus, progression through Levels should also reflect a move from general underpinning to current research and state of the art. Further, it is important that progression reflects increasing levels of independent learning, so students learn how to learn for themselves, supporting their future development and enabling them to retain currency throughout their career.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "undergraduate and master's computing courses"
  addressee: provider
  verbs: ["expose", "reflect"]
  about: "from breadth to focus across levels"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Undergraduate courses typically start broad and narrow in the final year; generalist master's usually aim at the minimum subject knowledge of a computing graduate, broadly or in a niche, and specialist master's and integrated master's final years focus more closely; progression through levels should also move from general foundations towards current research and the state of the art, with growing independence in learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/3.12
  locator: { number: "3.12", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 51425, end: 52129 }
  source: "3.12 The curriculum will define the knowledge students will gain and the course learning outcomes indicate the areas in which graduates will have knowledge competence or capability. However, individual students are expected to have the opportunity to develop a greater level of competence in some aspects of computing. These areas could also be linked to specific applied learning contexts, the particular focus of their major capstone activity, or a student's chosen pathway through optional modules on the course. Individual students could highlight their competencies, for example, in a learning portfolio, through the achievement of badges linked to micro-credentials, or in their curriculum vitae.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "computing curricula and students"
  addressee: both
  verbs: ["define", "gain", "indicate"]
  about: "curriculum, outcomes and individual competence"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "The curriculum will define what students learn and the outcomes show where graduates will have knowledge, competence or capability; each student is expected to have the chance to build deeper competence in some areas, through applied contexts, the capstone or optional modules, and may show it in a portfolio, through badges or in a CV."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/3.13
  locator: { number: "3.13", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 52129, end: 52631 }
  source: "3.13 The hardware and software resources available should facilitate a practical approach to the delivery of the course. Staff delivering Computing courses should be able to demonstrate ongoing personal development in the subject and appropriate pedagogy. Such activity should be supported at institutional level. Normally, staff would be qualified to a level beyond the level they are teaching and would also have undertaken, or be undertaking, a teaching qualification relevant to higher education.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "institutions and staff delivering computing courses"
  addressee: provider
  verbs: ["facilitate", "demonstrate", "supported"]
  about: "resources and staff development"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Hardware and software resources should support practical delivery; staff should show ongoing development in the subject and in pedagogy, supported by their institution, and would normally hold qualifications above the level they teach and a teaching qualification for higher education, held or in progress."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/3.14
  locator: { number: "3.14", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 52631, end: 53009 }
  source: "3.14 Institutions offering integrated undergraduate specialist master's courses must be able to articulate the legitimacy of providing education in the course topic. Although there are other possibilities, this will often mean that the institution possesses staff who are at the forefront of developments in the topic of the course and engaged in related advanced scholarship.\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "institutions offering integrated specialist master's courses"
  addressee: provider
  verbs: ["articulate"]
  about: "legitimacy for integrated specialist master's"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "An institution that offers an integrated specialist master's must be able to show why it is well placed to teach the topic, which often means staff at its forefront and engaged in advanced scholarship."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 53009, end: 53429 }
  source: "3.15 Computing graduates need to have acquired a strong grounding in underpinning knowledge alongside an ability to apply that knowledge to support future lifelong learning and the development of competence in new technologies as they are developed. Typically, students would demonstrate their ability to learn and apply a new approach or as part of the major activity that takes place towards the end of their course.\n\n"
  stem: none
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "computing graduates at every award covered"
  addressee: learner
  verbs: ["acquired", "apply", "demonstrate"]
  about: "grounding knowledge and applying it to new technology"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Computing graduates need a firm grounding in core knowledge and the ability to apply it to keep learning and to become competent in new technologies as they appear; students would usually show they can learn and apply a new approach, often in the major activity near the end of the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/3.16
  locator: { number: "3.16", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 53429, end: 54037 }
  source: "3.16 Course delivery should incorporate opportunities for applied learning in an authentic or simulated work context, such as industrial placements or apprenticeships. Working in teams of several people on sizable projects can simulate the real-world environment as well as exposing students to complexity. Projects defined in collaboration with industrial partners or research groups can enhance student learning and stimulate and promote interest in self- regulated learning as well as exposing students to aspects such as legal or ethical issues, demonstrating their relevance and importance.\n\nAssessment\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course delivery"
  addressee: provider
  verbs: ["incorporate"]
  about: "applied learning and team projects"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Course delivery should offer learning applied in real or simulated workplaces, such as placements or apprenticeships; sizeable team projects simulate real-world complexity, and projects set with industry or research partners can strengthen learning, self-regulation and awareness of legal and ethical issues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/3.17
  locator: { number: "3.17", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54037, end: 54311 }
  source: "3.17 Assessment f or Computing courses should be varied, appropriate and engaging. Perhaps most importantly, assessments should be authentic and tied to real-world contexts and constraints, and also allow students to practically demonstrate the skills they have developed.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment in computing courses"
  addressee: provider
  verbs: ["tied", "demonstrate"]
  about: "varied, authentic assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Assessment in computing should be varied, fitting and engaging and, above all, authentic, tied to real contexts and constraints and letting students show their skills in practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/3.18
  locator: { number: "3.18", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54311, end: 54811 }
  source: "3.18 Academic integrity is a key concept here and assessment design plays a critical role in enabling all students to succeed to the best of their abilities. Assessment techniques should afford students the opportunities to showcase what they can do, not just what they can write about, while also ensuring that checkpoints are in place to ensure that only work\n\n18\nproduced by students themselves is being assessed, for example by following the principles in the QAA's contract cheating guidance .\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["afford", "showcase", "ensure"]
  about: "academic integrity in assessment design"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Academic integrity matters and assessment design is central to every student succeeding: assessment should let students show what they can do, not only write about it, with checkpoints so that only students' own work is assessed, for example by following QAA's contract cheating guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/3.20
  locator: { number: "3.20", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 55141, end: 55489 }
  source: "3.20 A traditional written dissertation may not be suitable for all Computing courses, so a capstone activity may also include the production of academic papers, the development of a professional portfolio or work on entrepreneurial activities. Such activities at master's level should have a greater focus on drawing upon research literature.\n\n19\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "capstone activities at master's level"
  addressee: provider
  verbs: ["drawing"]
  about: "capstone formats; research literature at master's level"
  themes: [none]
  domain: none
  award: ["integrated master's", "master's"]
  gradeOf: none
  paraphrase: "A written dissertation may not suit every computing course, so a capstone may include academic papers, a professional portfolio or entrepreneurial work; at master's level such activities should focus more on research literature."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56592, end: 57400 }
  source: "4.3 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd. While it is expected these benchmarks will provide the foundation for awards, it is understood that variances may arise for reasons of institutional autonomy or subject evolution, and that any deviation from these standards be identified and justified.\n\nUndergraduate standards: threshold, typical and excellent descriptors\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "providers judging achievement"
  addressee: provider
  verbs: ["perform", "refer"]
  about: "evidence of achievement and Annex D"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will perform well above the minimum threshold; each provider sets what counts as evidence of this and should refer to Annex D, which describes the four honours classes; the standards are expected to underpin awards, and any departure from them is to be identified and justified."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/4.5
  locator: { number: "4.5", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 57489, end: 58087 }
  source: "4.5 With regard to undergraduate courses, those graduating with a bachelor's honours degree in Computing must demonstrate at least a threshold level of attainment across all outcome categories. Threshold level attainment typically maps onto that associated with a 3rd class honours. The typical level descriptor defines outcomes usually associated with 2:1. or 2:2. class honours performance. The excellent descriptor defines outcomes usually associated with a 1st class honours. It is not expected that a 1st class honours student must demonstrate excellent attainment in all outcome categories.\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "honours graduates in computing"
  addressee: learner
  verbs: ["demonstrate"]
  about: "threshold in every category; rungs and classes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours graduates in computing must show at least threshold attainment in every outcome category; threshold usually corresponds to a third, typical to a 2:1 or 2:2 and excellent to a first, and a first does not need excellence in every category."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 58356, end: 58441 }
  source: "Demonstrate a requisite understanding of the main body of knowledge for their subject"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in computing, at the threshold rung"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the main body of subject knowledge"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will show the understanding of the core body of computing knowledge that their subject needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b1.excellent
  locator: { number: "4.6.b1.excellent", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 58596, end: 58920 }
  source: "Demonstrate an exceptional understanding of the main body of knowledge for their subject and be able to exercise insightful and critical judgement in the use of that knowledge. Be creative and innovative in the application of the principles covered in the curriculum, and be able to go beyond what has been taught in classes"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates in computing, at the excellent rung"
  addressee: learner
  verbs: ["demonstrate", "exercise", "go"]
  about: "the main body of subject knowledge"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/computing-2022/4.6.b1.typical, basis: stated }
  paraphrase: "At the excellent rung, honours graduates will show an exceptional grasp of the core body of knowledge with insightful critical judgement in using it, apply what the curriculum covers creatively and with innovation and reach past what was taught."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b1.typical
  locator: { number: "4.6.b1.typical", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 58442, end: 58595 }
  source: "Demonstrate a sound understanding of the main body of knowledge for their subject and be able to exercise critical judgement in the use of that knowledge"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in computing, at the typical rung"
  addressee: learner
  verbs: ["demonstrate", "exercise"]
  about: "the main body of subject knowledge"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/computing-2022/4.6.b1, basis: stated }
  paraphrase: "At the typical rung, honours graduates will show a sound grasp of the core body of knowledge in their subject and use critical judgement in applying it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 58941, end: 59139 }
  source: "Understand and apply essential concepts, principles and practices of the subject in the context of well- defined scenarios, showing judgement in the selection and application of tools and techniques"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in computing, at the threshold rung"
  addressee: learner
  verbs: ["understand", "apply", "showing"]
  about: "applying concepts, principles and practices"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will understand and use the subject's essential concepts, principles and practices in clearly defined scenarios, choosing and applying tools and techniques with judgement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b2.excellent
  locator: { number: "4.6.b2.excellent", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 59358, end: 59578 }
  source: "Critically analyse and apply a wide range of concepts, principles and practices of the subject in the context of open scenarios, showing refined judgement and adaptability in the selection and use of tools and techniques"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates in computing, at the excellent rung"
  addressee: learner
  verbs: ["analyse", "apply", "showing"]
  about: "applying concepts, principles and practices"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/computing-2022/4.6.b2.typical, basis: stated }
  paraphrase: "At the excellent rung, honours graduates will analyse critically and apply a wide range of the subject's ideas, principles and practices in open scenarios, choosing and using tools and techniques with refined judgement and adaptability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b2.typical
  locator: { number: "4.6.b2.typical", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 59140, end: 59357 }
  source: "Critically analyse and apply concepts, principles and practices of the subject in the context of loosely defined scenarios, showing effective judgement and adaptability in the selection and use of tools and techniques"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in computing, at the typical rung"
  addressee: learner
  verbs: ["analyse", "apply", "showing"]
  about: "applying concepts, principles and practices"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/computing-2022/4.6.b2, basis: stated }
  paraphrase: "At the typical rung, honours graduates will analyse critically and apply the subject's ideas, principles and practices where scenarios are only loosely defined, choosing and using tools and techniques with effective judgement and adaptability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 59609, end: 59786 }
  source: "Be able to demonstrate judgement, critical thinking and problem-solving skills to solve well- specified problems, to create computational artefacts with a degree of independence"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in computing, at the threshold rung"
  addressee: learner
  verbs: ["demonstrate", "solve", "create"]
  about: "computational problem-solving"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will use judgement, critical thinking and problem-solving to solve clearly specified problems and build computational artefacts with some independence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b3.excellent
  locator: { number: "4.6.b3.excellent", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 59981, end: 60242 }
  source: "Be able to demonstrate sophisticated judgement, critical thinking, research design, and well- developed problem- solving skills with a high degree of autonomy, and to create highly effective computational artefacts across complex and unpredictable circumstances"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates in computing, at the excellent rung"
  addressee: learner
  verbs: ["demonstrate", "create"]
  about: "computational problem-solving"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/computing-2022/4.6.b3.typical, basis: stated }
  paraphrase: "At the excellent rung, honours graduates will bring sophisticated judgement and critical thinking, research design and strong problem-solving to bear with considerable autonomy, building highly effective computational artefacts where circumstances are complex and unpredictable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b3.typical
  locator: { number: "4.6.b3.typical", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 59787, end: 59980 }
  source: "Be able to demonstrate detailed judgement, critical thinking and problem- solving skills to solve both well-specified and loosely defined problems, to create appropriate computational artefacts"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in computing, at the typical rung"
  addressee: learner
  verbs: ["demonstrate", "solve", "create"]
  about: "computational problem-solving"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/computing-2022/4.6.b3, basis: stated }
  paraphrase: "At the typical rung, honours graduates will use detailed judgement, critical thinking and problem-solving to solve both clearly specified and loosely defined problems and build suitable computational artefacts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 60291, end: 61223 }
  source: "Demonstrate the ability to undertake problem identification and analysis to appropriately design, develop, test, integrate or Demonstrate the ability to undertake problem identification and analysis to appropriately design, develop, test, integrate or deploy a complex computing Demonstrate the ability to undertake problem identification and analysis to appropriately design, develop, test, integrate or deploy a highly complex\n\n21\nThreshold Typical Excellent deploy a computing system and any associated artefacts; understand the relationship between stages system and any associated artefacts; understand the relationship between stages and be able to demonstrate related problem-solving and evidence-informed evaluative skills computing system and any associated artefacts; deeply understand the relationship between stages and be able to demonstrate related sophisticated problem-solving and evidence-informed evaluative skills"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in computing, at the threshold rung"
  addressee: learner
  verbs: ["undertake", "design", "develop", "test", "integrate", "deploy", "understand"]
  about: "practical skills across the lifecycle"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will identify and analyse a problem, then suitably design, build, test, integrate or deploy a computing system with its related artefacts, understanding how the stages connect."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b4.excellent
  locator: { number: "4.6.b4.excellent", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 60291, end: 61223 }
  source: "Demonstrate the ability to undertake problem identification and analysis to appropriately design, develop, test, integrate or Demonstrate the ability to undertake problem identification and analysis to appropriately design, develop, test, integrate or deploy a complex computing Demonstrate the ability to undertake problem identification and analysis to appropriately design, develop, test, integrate or deploy a highly complex\n\n21\nThreshold Typical Excellent deploy a computing system and any associated artefacts; understand the relationship between stages system and any associated artefacts; understand the relationship between stages and be able to demonstrate related problem-solving and evidence-informed evaluative skills computing system and any associated artefacts; deeply understand the relationship between stages and be able to demonstrate related sophisticated problem-solving and evidence-informed evaluative skills"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates in computing, at the excellent rung"
  addressee: learner
  verbs: ["undertake", "design", "deploy", "understand", "demonstrate"]
  about: "practical skills across the lifecycle"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/computing-2022/4.6.b4.typical, basis: stated }
  paraphrase: "At the excellent rung, honours graduates will identify and analyse a problem, then suitably design, build, test, integrate or deploy a highly complex computing system with its related artefacts, understanding in depth how the stages connect and applying sophisticated problem-solving and evidence-informed evaluation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b4.typical
  locator: { number: "4.6.b4.typical", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 60291, end: 61223 }
  source: "Demonstrate the ability to undertake problem identification and analysis to appropriately design, develop, test, integrate or Demonstrate the ability to undertake problem identification and analysis to appropriately design, develop, test, integrate or deploy a complex computing Demonstrate the ability to undertake problem identification and analysis to appropriately design, develop, test, integrate or deploy a highly complex\n\n21\nThreshold Typical Excellent deploy a computing system and any associated artefacts; understand the relationship between stages system and any associated artefacts; understand the relationship between stages and be able to demonstrate related problem-solving and evidence-informed evaluative skills computing system and any associated artefacts; deeply understand the relationship between stages and be able to demonstrate related sophisticated problem-solving and evidence-informed evaluative skills"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in computing, at the typical rung"
  addressee: learner
  verbs: ["undertake", "design", "deploy", "understand", "demonstrate"]
  about: "practical skills across the lifecycle"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/computing-2022/4.6.b4, basis: stated }
  paraphrase: "At the typical rung, honours graduates will identify and analyse a problem, then suitably design, build, test, integrate or deploy a complex computing system with its related artefacts, understanding how the stages connect and applying problem-solving and evidence-informed evaluation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 61315, end: 61514 }
  source: "Demonstrate the ability to work in an effective manner, including as a member of a team, making use of tools and techniques to appropriately communicate, manage tasks and plan projects under guidance"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in computing, at the threshold rung"
  addressee: learner
  verbs: ["work", "communicate", "manage", "plan"]
  about: "teamwork and project working"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will work effectively, including in a team, using tools and techniques suitably to communicate, organise tasks and plan projects with guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b5.excellent
  locator: { number: "4.6.b5.excellent", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 61739, end: 61985 }
  source: "Demonstrate the ability to work in a highly proactive and accomplished manner, including as a leading member of a team, making excellent use of tools and techniques to proficiently communicate, manage tasks and plan projects with minimum guidance"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates in computing, at the excellent rung"
  addressee: learner
  verbs: ["work", "communicate", "manage", "plan"]
  about: "teamwork and project working"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/computing-2022/4.6.b5.typical, basis: stated }
  paraphrase: "At the excellent rung, honours graduates will work in a highly proactive, accomplished way, including leading within a team, using tools and techniques excellently to communicate, organise tasks and plan projects proficiently with little guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b5.typical
  locator: { number: "4.6.b5.typical", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 61515, end: 61738 }
  source: "Demonstrate the ability to work in a proactive and effective manner, including as a member of a team, making good use of tools and techniques to successfully communicate, manage tasks and plan projects with minimum guidance"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in computing, at the typical rung"
  addressee: learner
  verbs: ["work", "communicate", "manage", "plan"]
  about: "teamwork and project working"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/computing-2022/4.6.b5, basis: stated }
  paraphrase: "At the typical rung, honours graduates will work proactively and effectively, including in a team, using tools and techniques well to communicate clearly, organise tasks and plan projects with little guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 62115, end: 62353 }
  source: "Identify appropriate practices and perform work within a professional, legal and ethical framework – including data management and use, security, equality, diversity and inclusion (EDI) and sustainability – in the work that they undertake"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in computing, at the threshold rung"
  addressee: learner
  verbs: ["identify", "perform"]
  about: "professional, legal and ethical practice"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, honours graduates will identify suitable practices and carry out their own work inside a professional, legal and ethical framework that covers data management and use, security, EDI and sustainability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b6.excellent
  locator: { number: "4.6.b6.excellent", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 62639, end: 62966 }
  source: "Identify best-of-kind practices and effect highly principled solutions within a professional, legal and ethical framework to consistently address a wide breadth of relevant considerations – including data management and use, security, equality, diversity and inclusion (EDI) and sustainability – in the work that they undertake"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates in computing, at the excellent rung"
  addressee: learner
  verbs: ["identify", "effect", "address"]
  about: "professional, legal and ethical practice"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/computing-2022/4.6.b6.typical, basis: stated }
  paraphrase: "At the excellent rung, honours graduates will identify the best practices of their kind and reach highly principled solutions inside a professional, legal and ethical framework that deal consistently with a wide range of relevant considerations, such as data management and use, security, EDI and sustainability, in their own work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.6.b6.typical
  locator: { number: "4.6.b6.typical", headingPath: ["Benchmark standards", "Undergraduate standards: threshold, typical and excellent descriptors"] }
  span: { start: 62354, end: 62638 }
  source: "Identify appropriate practices and effect principled solutions within a professional, legal and ethical framework to address core considerations – including data management and use, security, equality, diversity and inclusion (EDI) and sustainability – in the work that they undertake"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in computing, at the typical rung"
  addressee: learner
  verbs: ["identify", "effect", "address"]
  about: "professional, legal and ethical practice"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/computing-2022/4.6.b6, basis: stated }
  paraphrase: "At the typical rung, honours graduates will identify suitable practices and reach principled solutions inside a professional, legal and ethical framework that deal with the core considerations, such as data management and use, security, EDI and sustainability, in their own work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.8
  locator: { number: "4.8", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 63448, end: 63895 }
  source: "4.8 Nonetheless, all master's degree graduates have in-depth and advanced knowledge and understanding of their subject and/or profession, informed by current practice, scholarship and research. This will include a critical awareness of current issues and developments in the subject and/or profession; critical skills; knowledge of professional responsibility, integrity and ethics; and the ability to reflect on their own progress as a learner.\n\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "all master's graduates in computing"
  addressee: learner
  verbs: ["include", "reflect"]
  about: "what all master's graduates have"
  themes: [none]
  domain: knowledge
  award: ["integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Every master's graduate has deep, advanced knowledge and understanding of their subject or profession, shaped by practice, scholarship and research; this will include critical awareness of current issues and developments, critical skills, an understanding of professional ethics, integrity and responsibility and the capacity to reflect on how they are progressing as learners."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.9
  locator: { number: "4.9", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 63895, end: 64662 }
  source: "4.9 Graduates of research master's are likely to be further characterised by their ability to study independently in the subject, and to use a range of techniques and research methods applicable to advanced scholarship in the subject. Graduates of specialist or advanced study master's are likely to be characterised in particular by their ability to complete a research project in the subject, which in some subjects includes a critical review of existing literature or other scholarly outputs. Meanwhile, graduates of professional or practice master's are able to apply research and critical perspectives to professional situations, both practical and theoretical, and to use a range of techniques and research methods applicable to their professional activities.\n\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of research, specialist and professional master's"
  addressee: learner
  verbs: ["study", "use", "complete", "apply"]
  about: "what each kind of master's graduate can do"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Research master's graduates are likely also to study independently and use advanced research methods; specialist or advanced study master's graduates are likely to complete a research project, sometimes with a critical literature review; and professional or practice master's graduates are able to bring research and critical perspectives to professional situations and use methods suited to their practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.12
  locator: { number: "4.12", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 65324, end: 65432 }
  source: "4.12 In all cases, the content of the course should align to the FHEQ Level 7/SCQF Level 11 specification.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "postgraduate computing courses"
  addressee: provider
  verbs: ["align"]
  about: "postgraduate content aligned to level 7 or 11"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "In every case, a postgraduate course's content should align with the specification for FHEQ level 7 or SCQF level 11."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/computing-2022/4.13
  locator: { number: "4.13", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 65432, end: 65805 }
  source: "4.13 With reference to the descriptors outlined in Undergraduate standards: threshold, typical and excellent descriptors, students graduating with a postgraduate degree in Computing must demonstrate at least a threshold level of attainment across all relevant course outcome categories. Attainment at a threshold level usually maps onto that associated with a Pass award.\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "postgraduate master's graduates in computing"
  addressee: learner
  verbs: ["demonstrate"]
  about: "threshold for postgraduate master's; Pass"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "With reference to the undergraduate descriptors, postgraduate computing graduates must show at least threshold attainment in every relevant outcome category; threshold usually corresponds to a Pass."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.14.b1.excellent
  locator: { number: "4.14.b1.excellent", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 66908, end: 67545 }
  source: "Demonstrate a deep and systematic understanding of knowledge, as appropriate to the area of study, much of which is at, or informed by, the forefront of their academic discipline, field of study or area of professional practice. Alongside this, demonstrate a critical awareness and advanced understanding of current problems and/or recent development within the discipline.\n\nDemonstrate originality in the application of knowledge, together with a practical and reflective understanding of how established and state-of-the-art investigative techniques of research and enquiry are used to create and interpret knowledge in the discipline."
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:7
  appliesTo: "postgraduate master's graduates in computing, at the excellent rung"
  addressee: learner
  verbs: ["demonstrate", "create", "interpret"]
  about: "systematic knowledge at the forefront"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: { statement: qaa/computing-2022/4.14.b1.typical, basis: stated }
  paraphrase: "At the excellent rung, master's graduates will show deep, systematic understanding of knowledge in their area, much of it at or shaped by the forefront, with critical awareness and advanced understanding of current problems or recent developments, originality in applying knowledge and a practical and reflective grasp of how research and enquiry techniques, both established and state-of-the-art, create and interpret knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.14.b1.typical
  locator: { number: "4.14.b1.typical", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 66330, end: 66907 }
  source: "Demonstrate a systematic understanding of knowledge, as appropriate to the area of study, much of which is at, or informed by, the forefront of their academic discipline, field of study or area of professional practice. Alongside this, demonstrate a critical awareness of current problems and/or recent development within the discipline.\n\nDemonstrate a degree of originality in the application of knowledge, together with a practical understanding of how established investigative techniques of research and enquiry are used to create and interpret knowledge in the discipline."
  stem: "4.14"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "postgraduate master's graduates in computing, at the typical rung"
  addressee: learner
  verbs: ["demonstrate", "create", "interpret"]
  about: "systematic knowledge at the forefront"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the typical rung, master's graduates will show systematic understanding of knowledge in their area of study, much of it at or shaped by the forefront of the discipline or of professional practice, critical awareness of current problems or recent developments, some originality in applying knowledge and a practical understanding of how established research and enquiry techniques create and interpret knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.14.b2.excellent
  locator: { number: "4.14.b2.excellent", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 67691, end: 67907 }
  source: "Be able to deeply analyse, apply and critically evaluate concepts, principles and practices at the forefront of the area of study, demonstrating insight and innovation, and application of these skills as appropriate."
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:7
  appliesTo: "postgraduate master's graduates in computing, at the excellent rung"
  addressee: learner
  verbs: ["analyse", "apply", "evaluate", "demonstrating"]
  about: "critical evaluation at the forefront"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: { statement: qaa/computing-2022/4.14.b2.typical, basis: stated }
  paraphrase: "At the excellent rung, master's graduates will analyse in depth, apply and critically evaluate leading-edge concepts, principles and practices, showing insight and innovation and applying these skills where they fit."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.14.b2.typical
  locator: { number: "4.14.b2.typical", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 67566, end: 67689 }
  source: "Be able to analyse, apply and critically evaluate concepts, principles and practices at the forefront of the area of study."
  stem: "4.14"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "postgraduate master's graduates in computing, at the typical rung"
  addressee: learner
  verbs: ["analyse", "apply", "evaluate"]
  about: "critical evaluation at the forefront"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the typical rung, master's graduates will critically evaluate, analyse and apply the concepts, principles and practices found at the leading edge of their area of study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.14.b3.excellent
  locator: { number: "4.14.b3.excellent", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 68167, end: 68462 }
  source: "Be able to demonstrate innovation and/or originality, sophisticated judgement, critical thinking, research design and well-developed problem-solving skills with a high degree of autonomy, and to create comprehensive and highly effective computational artefacts given complex or open constraints."
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:7
  appliesTo: "postgraduate master's graduates in computing, at the excellent rung"
  addressee: learner
  verbs: ["demonstrate", "create"]
  about: "computational problem-solving with autonomy"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: { statement: qaa/computing-2022/4.14.b3.typical, basis: stated }
  paraphrase: "At the excellent rung, master's graduates will show innovation or originality with sophisticated judgement, critical thinking, research design and strong problem-solving, working with considerable autonomy to build comprehensive, highly effective computational artefacts under complex or open constraints."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.14.b3.typical
  locator: { number: "4.14.b3.typical", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 67938, end: 68165 }
  source: "Be able to demonstrate judgement, critical thinking, research design, and well- developed problem-solving skills with a high degree of autonomy, and to create effective computational artefacts given complex or open constraints."
  stem: "4.14"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "postgraduate master's graduates in computing, at the typical rung"
  addressee: learner
  verbs: ["demonstrate", "create"]
  about: "computational problem-solving with autonomy"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the typical rung, master's graduates will bring judgement, critical thinking, research design and strong problem-solving to bear with considerable autonomy, building effective computational artefacts under complex or open constraints."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.14.b4.excellent
  locator: { number: "4.14.b4.excellent", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 68712, end: 68969 }
  source: "Demonstrate the ability to apply state-of-the-art computing techniques, as appropriate to the area of study, within highly complex or unpredictable scenarios, in a systematic and creative manner, making insightful decisions given incomplete or missing data."
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:7
  appliesTo: "postgraduate master's graduates in computing, at the excellent rung"
  addressee: learner
  verbs: ["apply", "making"]
  about: "applying computing techniques in complex scenarios"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: { statement: qaa/computing-2022/4.14.b4.typical, basis: stated }
  paraphrase: "At the excellent rung, master's graduates will apply state-of-the-art computing techniques suited to their area systematically and creatively in highly complex or unpredictable scenarios, making insightful decisions when data are incomplete or missing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.14.b4.typical
  locator: { number: "4.14.b4.typical", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 68490, end: 68711 }
  source: "Demonstrate the ability to apply computing techniques, as appropriate to the area of study, within complex or unpredictable scenarios, in a systematic manner, making appropriate decisions given incomplete or missing data."
  stem: "4.14"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "postgraduate master's graduates in computing, at the typical rung"
  addressee: learner
  verbs: ["apply", "making"]
  about: "applying computing techniques in complex scenarios"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the typical rung, master's graduates will apply computing techniques suited to their area systematically in complex or unpredictable scenarios, making sound decisions when data are incomplete or missing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.14.b5.excellent
  locator: { number: "4.14.b5.excellent", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 69008, end: 69373 }
  source: "Demonstrate elements of self- direction in tackling and solving problems, alongside approaching Demonstrate self-direction in tackling and solving complex problems, alongside approaching\n\n24\nTypical Excellent and implementing tasks and activities in a proactive and effective manner. and implementing tasks and activities in a highly proactive and effective manner."
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:7
  appliesTo: "postgraduate master's graduates in computing, at the excellent rung"
  addressee: learner
  verbs: ["tackling", "solving", "approaching", "implementing"]
  about: "self-direction"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: { statement: qaa/computing-2022/4.14.b5.typical, basis: stated }
  paraphrase: "At the excellent rung, master's graduates will show self-direction in tackling and solving complex problems and approach and carry out tasks in a highly proactive, effective way."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.14.b5.typical
  locator: { number: "4.14.b5.typical", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 69008, end: 69373 }
  source: "Demonstrate elements of self- direction in tackling and solving problems, alongside approaching Demonstrate self-direction in tackling and solving complex problems, alongside approaching\n\n24\nTypical Excellent and implementing tasks and activities in a proactive and effective manner. and implementing tasks and activities in a highly proactive and effective manner."
  stem: "4.14"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "postgraduate master's graduates in computing, at the typical rung"
  addressee: learner
  verbs: ["tackling", "solving", "approaching", "implementing"]
  about: "self-direction"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the typical rung, master's graduates will show some self-direction in tackling and solving problems and approach and carry out tasks proactively and effectively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.14.b6.excellent
  locator: { number: "4.14.b6.excellent", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 69791, end: 70278 }
  source: "Ability to communicate their work to specialist and non-specialist audiences in an accessible and impactful way.\n\nIdentify and effect best-of-kind and highly principled solutions in complex and unpredictable professional environments, within a professional, legal and ethical framework to consistently address a wide breadth of relevant considerations – including data management and use, security, equality, diversity and inclusion (EDI) and sustainability – in the work they undertake."
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:7
  appliesTo: "postgraduate master's graduates in computing, at the excellent rung"
  addressee: learner
  verbs: ["communicate", "identify", "effect", "address"]
  about: "communication and professional practice"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: { statement: qaa/computing-2022/4.14.b6.typical, basis: stated }
  paraphrase: "At the excellent rung, master's graduates will communicate their work accessibly and with impact to specialist and non-specialist audiences, and identify and reach the best, highly principled solutions inside a professional, legal and ethical framework, dealing consistently with a wide range of considerations such as data management and use, security, EDI and sustainability, in complex, unpredictable professional settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.14.b6.typical
  locator: { number: "4.14.b6.typical", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 69396, end: 69789 }
  source: "Ability to communicate their work to specialist and a diverse range of non-specialist audiences.\n\nIdentify appropriate practices in complex and unpredictable professional environments, and perform work within a professional, legal and ethical framework – including data management and use, security, equality, diversity and inclusion (EDI) and sustainability – in the work that they undertake."
  stem: "4.14"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "postgraduate master's graduates in computing, at the typical rung"
  addressee: learner
  verbs: ["communicate", "identify", "perform"]
  about: "communication and professional practice"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the typical rung, master's graduates will communicate their work to specialists and to a wide range of non-specialist audiences, and identify suitable practices and work inside a professional, legal and ethical framework, covering data management and use, security, EDI and sustainability, in complex, unpredictable professional settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/computing-2022/4.17
  locator: { number: "4.17", headingPath: ["Benchmark standards", "Integrated undergraduate master's degrees"] }
  span: { start: 70987, end: 71242 }
  source: "4.17 Students graduating with an integrated undergraduate master's degrees in computing must demonstrate at least a threshold level of attainment across all descriptors in both FHEQ Levels 6 and 7, or FQHEIS Level 10 and 11 in paragraphs 4.2 and 4.3.\n\n25\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "integrated master's graduates in computing"
  addressee: learner
  verbs: ["demonstrate"]
  about: "integrated master's: threshold at both levels"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Integrated master's graduates in computing must show at least threshold attainment against every descriptor at both FHEQ levels 6 and 7 (FQHEIS 10 and 11)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/computing-2022/1.11
  forPractitioner: { text: "Build a curriculum every student can see themselves in: draw practical tasks from varied cultures, keep the setting welcoming and collaborative and teach students to check what they build for bias.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the curriculum and the course team, not a student outcome: a culturally responsive curriculum that every student values and that guards against biased technology. It holds for all three awards the statement covers. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.11. Do not present it as a legal duty; set it beside 1.12, 3.9 and 3.10 here and the professional practice rungs 4.6.b6, 4.6.b6.typical and 4.6.b6.excellent."
  author-agent-dialogue: "Raise this when a programme team reviews its curriculum, case studies or practical tasks for inclusion. Frame it for staff as a test of whether every student finds the work relevant and the setting welcoming. Ask: 'Whose experiences do your practical tasks draw on, and whose are missing?' Do not hand it to a student as a standard they must meet."
- statement: qaa/computing-2022/1.12
  forPractitioner: { text: "Look through terminology, teaching approaches and examples for bias, gendered language included, remove what you find and support every student on equal terms.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on curricula: represent all students and remove existing bias, with gender imbalance as the worked example. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.12. Do not claim it sets quotas or a legal test; set it beside 1.11 and 3.9 here and the EDI practices listed in 1.14."
  author-agent-dialogue: "Raise this when a team looks at recruitment or attainment by gender, or reviews the language of its modules. Frame it for staff as removing barriers that are already built in. Ask: 'Which terms, examples or teaching habits in your modules might tell some students that computing is not for them?' Avoid presenting it to a student as their task."
- statement: qaa/computing-2022/1.15
  forPractitioner: { text: "Show students where computing helps or harms economically, socially and environmentally, and build the competencies they will need to act on the SDGs at work; use the ESD guidance for methods.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on computing courses to address sustainable development and build students' competencies for the SDGs. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.15. Do not claim it prescribes particular goals (1.17 says it does not); set it beside 1.16 to 1.18 here, std:doc:qaa-advancehe-esd-2021-guidance and the professional practice rungs from 4.6.b6."
  author-agent-dialogue: "Raise this when a team maps sustainability content or writes outcomes about it. Frame it for staff as showing both the good and the harm computing does, and building students' capacity to act. Ask: 'Where in your course do students weigh the environmental or social cost of a system they build?' Avoid presenting a list of SDGs as compulsory."
- statement: qaa/computing-2022/1.16
  forPractitioner: { text: "Use the broad meaning of sustainability when planning the curriculum: alongside environmental topics such as data centre energy and e-waste, bring in social justice and economic prosperity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation addressed to the subject community and its teachers: sustainability in its economic, social and environmental senses, linked to EDI. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.16. Do not narrow it to green IT or present it as a student outcome; set it beside 1.15, 1.17, 1.18 and 3.10 in this document."
  author-agent-dialogue: "Raise this when a lecturer treats sustainability as only an environmental topic. Frame it for staff as a wider lens on material they already teach. Ask: 'Which topic in your module could carry a social or economic sustainability question as well as an environmental one?' Avoid lecturing on the SDGs at length."
- statement: qaa/computing-2022/1.18
  forPractitioner: { text: "Whichever ESD approach the course takes, check that every graduate can recognise the sustainability issues in their area of computing and how they are starting to be addressed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your course, you should appreciate the sustainability issues that matter in your area of computing and how people are beginning to tackle them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome for computing graduates at all three awards (FHEQ levels 6 and 7; FQHEIS 10 and 11). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.18. Do not claim it requires specialist sustainability science or a set list of SDGs; set it beside 1.15, 1.19.b3 and the professional practice rungs from 4.6.b6, the FHEQ descriptors qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/4.17.b1 and the reference step spine:6."
  author-agent-dialogue: "Raise this when a student plans a project or asks why sustainability belongs in a computing degree. To a student, say plainly that you should be able to name the sustainability issues in your own area; to staff, frame it as a graduate outcome their modules must give evidence of. Ask: 'What sustainability issue does your project raise, and how is your field starting to respond to it?' Avoid treating it as a test of specialist environmental knowledge."
- statement: qaa/computing-2022/1.19.b1
  forPractitioner: { text: "Give students chances to develop and evidence acting with integrity in professional conduct and behaviour (generic skills), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop acting with integrity in your professional conduct and behaviour.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Generic skills); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.17.b8.1, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r4/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about professional integrity, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'Think of a time on a project when cutting a corner was tempting: what did you do, and why?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b2
  forPractitioner: { text: "Give students chances to develop and evidence awareness of the legal and ethical principles that govern professional computing work (generic skills), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop an awareness of the legal and ethical principles that govern computing work.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Generic skills); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.2 and qaa/fheq-2024/4.17.b8.2, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r4/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about legal and ethical awareness, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'Which law or ethical principle shaped a design decision in your last project?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b3
  forPractitioner: { text: "Give students chances to develop and evidence awareness of the sustainability issues that computing raises as a discipline and a profession (generic skills), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop an awareness of the sustainability issues computing raises.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Generic skills); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/4.17.b1, the Annex D descriptions qaa/fheq-2024/annex-d/knowledge/r2/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about sustainability awareness, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'What sustainability issue would you raise about the system you are building now?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b4
  forPractitioner: { text: "Give students chances to develop and evidence an evident understanding that computing is practised as a global profession (generic skills), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop an understanding that computing is a global profession.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Generic skills); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1, the Annex D descriptions qaa/fheq-2024/annex-d/knowledge/r2/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about computing as a global profession, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'How would your work change if your team or your users were in another country?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b5
  forPractitioner: { text: "Give students chances to develop and evidence using social media responsibly at work, including professional online communication, email conduct and building an online presence (generic skills), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the habit of using social media responsibly at work, including how you write online and by email and how you present yourself.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Generic skills); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/4.17.b5, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r1/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about professional use of social media, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'What would an employer learn about you from your public online profile today?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b6
  forPractitioner: { text: "Give students chances to develop and evidence critical reflection and clear communication in writing, in speech and online (generic skills), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop critical reflection and clear communication in writing, in speech and online.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Generic skills); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/4.17.b5, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r5/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about critical reflection and communication, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'What did your last piece of feedback tell you, and how did you explain your response to it?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b7
  forPractitioner: { text: "Give students chances to develop and evidence a high standard of numeracy and literacy (generic skills), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop a high standard of numeracy and literacy.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Generic skills); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/4.17.b5, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r1/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about numeracy and literacy, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'Where did your last report depend on getting the numbers and the wording exactly right?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b8
  forPractitioner: { text: "Give students chances to develop and evidence dealing with others professionally and with respect (generic skills), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the ability to deal with others professionally and with respect.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Generic skills); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.17.b8.1, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r2/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about respectful professional interaction, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'How did you handle a disagreement in your last team project?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b9
  forPractitioner: { text: "Give students chances to develop and evidence understanding and showing respect for equality and diversity across the many sectors where computing professionals work (generic skills), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop respect for equality and diversity, understood and shown, across the many sectors where computing is practised.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Generic skills); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.2 and qaa/fheq-2024/4.17.b8.2, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r2/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about respect for equality and diversity, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'Where have you seen a team or a product leave some people out, and what would you change?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b10
  forPractitioner: { text: "Give students chances to develop and evidence understanding what a leader does in setting direction and owning actions and decisions (generic skills), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop an understanding of what a leader does in setting direction and owning decisions.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Generic skills); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.17.b8.1, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r4/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about the role of a leader, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'When have you set the direction for a group, and what did you take responsibility for?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b11
  forPractitioner: { text: "Give students chances to develop and evidence communicating confidently in meetings held in person or online (generic skills), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the confidence to speak up in meetings, in person or online.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Generic skills); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/4.17.b5, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r1/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about confident communication in meetings, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'In your last online or face-to-face meeting, what did you contribute and how was it received?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b12
  forPractitioner: { text: "Give students chances to develop and evidence working with agility and flexibility as situations and priorities change (agile working), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the ability to adapt quickly as situations and priorities change.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Agile working); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.2 and qaa/fheq-2024/4.17.b8.2, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r3/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about agility and flexibility, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'When a project's priorities changed suddenly, how did you adjust your plan?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b13
  forPractitioner: { text: "Give students chances to develop and evidence interpreting data and information promptly in academic and professional settings (agile working), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the ability to make sense of data and information promptly, in study and at work.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Agile working); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/4.17.b4.1, the Annex D descriptions qaa/fheq-2024/annex-d/cognitive/r1/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about timely interpretation of data, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'How quickly could you tell what the data in your last project showed, and how sure were you?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b14
  forPractitioner: { text: "Give students chances to develop and evidence recognising and drawing on other people's skills and knowledge in order to collaborate (agile working), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the ability to spot and use other people's skills and knowledge when you work together.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Agile working); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.17.b8.1, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r2/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about drawing on others' strengths to collaborate, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'In your last group task, whose strengths did you rely on, and how did you find them?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b15
  forPractitioner: { text: "Give students chances to develop and evidence identifying problems and wanted outcomes and negotiating with colleagues towards solutions all can accept (agile working), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the ability to pin down a problem and the outcome wanted and to negotiate a solution your colleagues accept.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Agile working); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/4.17.b4.1, the Annex D descriptions qaa/fheq-2024/annex-d/cognitive/r3/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about negotiating solutions, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'Describe a solution you reached with others that was not your first choice: how did you agree on it?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b16
  forPractitioner: { text: "Give students chances to develop and evidence working without supervision, planning well and meeting deadlines (remote working), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the ability to work without supervision, plan well and meet deadlines.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Remote working); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.17.b8.1, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r3/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about working unsupervised to deadlines, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'How did you plan your last piece of independent work, and did you meet the deadline?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b17
  forPractitioner: { text: "Give students chances to develop and evidence acting with confidence on their own initiative (remote working), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the confidence to act on your own initiative.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Remote working); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.17.b8.1, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r4/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about acting on own initiative, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'When did you last act without being asked, and what happened?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b18
  forPractitioner: { text: "Give students chances to develop and evidence building social capital and using professional networking skills (resilience), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop a professional network and the skills to grow it.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Resilience); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.3 and qaa/fheq-2024/4.17.b8.3, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r2/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about networking and social capital, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'Who in the profession could you ask for advice today, and how did you meet them?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b19
  forPractitioner: { text: "Give students chances to develop and evidence keeping a current, critical understanding of developments, challenges and opportunities in the profession, at home and worldwide (resilience), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop a current, critical view of what is changing in the profession, at home and worldwide.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Resilience); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b3.2 and qaa/fheq-2024/4.17.b4.1, the Annex D descriptions qaa/fheq-2024/annex-d/cognitive/r1/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about keeping up with the profession, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'What development in computing this year matters most for your area, and why?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b20
  forPractitioner: { text: "Give students chances to develop and evidence presenting rational, reasoned arguments concisely on a given problem or opportunity to varied audiences, orally, online or in writing (resilience), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the ability to make a short, reasoned case on a problem or opportunity to different audiences, in speech, online or in writing.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Resilience); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/4.17.b5, the Annex D descriptions qaa/fheq-2024/annex-d/cognitive/r2/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about presenting reasoned arguments, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'Could you make the case for your project's approach in two minutes to a non-specialist?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b21
  forPractitioner: { text: "Give students chances to develop and evidence active engagement in continuing professional development (entrepreneurship and enterprise education), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop an active habit of continuing professional development.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Entrepreneurship and enterprise education); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.3 and qaa/fheq-2024/4.17.b8.3, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r3/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about continuing professional development, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'What have you learned outside your modules this term, and how did you choose it?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b22
  forPractitioner: { text: "Give students chances to develop and evidence contributing to the development of the profession and bringing an enterprising, challenging approach (entrepreneurship and enterprise education), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop an enterprising, questioning approach and a part in developing your profession.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Entrepreneurship and enterprise education); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.17.b8.1, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r4/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about enterprise and contribution to the profession, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'Where have you challenged an accepted way of doing something, and what did you propose instead?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b23
  forPractitioner: { text: "Give students chances to develop and evidence finding and retrieving relevant ideas and making sure they can be communicated well in varied formats to varied audiences (entrepreneurship and enterprise education), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the ability to find relevant ideas and share them well in different formats with different audiences.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Entrepreneurship and enterprise education); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/4.17.b5, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r1/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about finding and communicating ideas, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'How did you find the key sources for your last assignment, and how did you present them?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b24
  forPractitioner: { text: "Give students chances to develop and evidence recognising environmental and social factors that open opportunities or pose challenges for computing systems across human activity (entrepreneurship and enterprise education), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the ability to see how environmental and social factors create openings or problems for computing systems.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Entrepreneurship and enterprise education); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/4.17.b4.1, the Annex D descriptions qaa/fheq-2024/annex-d/cognitive/r3/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about opportunities and challenges in context, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'What social or environmental factor could make or break the system you are working on?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b25
  forPractitioner: { text: "Treat the subject knowledge and skills of the whole statement, above all section 4, as the base an employer will expect graduates to put to use.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "The computing knowledge and skills you build on your course will be what an employer expects you to be able to use and apply at work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level statement linking the subject standards to employers' expectations: the statement's subject knowledge and skills will form the base employers expect graduates to apply. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not claim it adds new outcomes or guarantees employment; set it beside the rungs 4.6.b1 to 4.6.b4 and 4.14.b1.typical to 4.14.b4.typical and the FHEQ descriptors qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.17.b2."
  author-agent-dialogue: "Raise this when a student asks whether what they learn will matter to employers. To a student, say that the subject knowledge in the course is what an employer will expect you to use; to staff, frame it as the link between the rungs and employability. Ask: 'Which part of your course would you expect to use in your first month at work?' Avoid promising particular jobs."
- statement: qaa/computing-2022/1.19.b26
  forPractitioner: { text: "Use examples and case studies of organisations using computing so that graduates can explain how their subject knowledge serves business and industry.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show how your computing knowledge is used by organisations, talking through examples and case studies.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome for computing graduates at every award covered (FHEQ levels 6 and 7): relating subject knowledge to business and industry through examples. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not claim it requires business management knowledge; set it beside 1.19.b25 and 1.19.b27 here, the FHEQ descriptor qaa/fheq-2024/4.15.b3.1 and the reference step spine:6."
  author-agent-dialogue: "Raise this when a student prepares for placements or interviews, or a team plans case-study teaching. To a student, put it as being able to explain how a real organisation uses what you know; to staff, as an outcome case studies should build. Ask: 'Name an organisation that uses something you have learned, and explain how.' Avoid making it a test of business jargon."
- statement: qaa/computing-2022/1.19.b27
  forPractitioner: { text: "Give students chances to develop and evidence using what they know of computing, with computational thinking, to crack complex problems for the benefit of the organisation the graduate works in (subject-specific skills in computing (common core)), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the ability to use what you know of computing, with computational thinking, to crack complex problems for the organisation you work in.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Subject-specific skills in computing (common core)); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/4.17.b5, the Annex D descriptions qaa/fheq-2024/annex-d/cognitive/r3/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about applying computational thinking to complex problems, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'What complex problem have you broken down with computational thinking, and who gained from the result?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b28
  forPractitioner: { text: "Give students chances to develop and evidence planning and recording their own learning in core computing skills and technologies throughout, as a basis for lifelong learning and CPD (subject-specific skills in computing (common core)), as one of the employability skills the course builds in.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is meant to help you develop the habit of planning and recording your own learning in core computing skills, as a basis for lifelong learning.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the employability skills the statement lists for computing courses to build in (Subject-specific skills in computing (common core)); the list is offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/4.17.b8.3, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r3/3rd to 1st and the reference steps spine:6 and spine:7."
  author-agent-dialogue: "Bring this up when a student or team talks about planning and recording self-learning, in study, placements or careers planning. To a student, put it in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to design in and give evidence of. Ask: 'How do you keep track of what you are learning in computing, and what is next on your list?' Avoid reading the issuer's list aloud or treating it as one of the rungs in section 4."
- statement: qaa/computing-2022/1.19.b30
  forPractitioner: { text: "Give students interdisciplinary problems so that, by graduation, they can bring computer science, data science and digital technology to bear on questions from other fields.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to use computer science, data science and digital technology to help solve problems in other subjects, working with people from those fields.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome for computing graduates (FHEQ levels 6 and 7): applying computing to problem-solving in other disciplines, set in a paragraph on interdisciplinary teamwork. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not claim it requires expertise in a second subject; set it beside 2.4 here, the FHEQ descriptor qaa/fheq-2024/4.15.b6 and the reference strand strand:application."
  author-agent-dialogue: "Raise this when a student joins an interdisciplinary project or a joint course. To a student, put it as using your computing to help with someone else's problem; to staff, as an outcome interdisciplinary projects can show. Ask: 'What problem from another subject could your computing skills help with?' Avoid suggesting the student must master the other subject."
- statement: qaa/computing-2022/1.19.b32
  forPractitioner: { text: "Help students map the range of computing careers, the skills each asks for and their own skills, so they can plan towards the roles they want.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should get to know the many careers open to you in computing, what each asks for and what your own skills are, so you can match them to what you want to do.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome for computing graduates (FHEQ levels 6 and 7): understanding employment pathways and matching personal skills to them. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not claim it guarantees a role or sets out a careers service duty; set it beside 1.19.b33 and 1.19.b34 here, the FHEQ descriptor qaa/fheq-2024/4.15.b9.3 and the Annex D description qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise this when a student is unsure what to do after the course. To a student, put it plainly: look at the routes open to you and at what you already offer; to staff, frame it as career awareness the course should build. Ask: 'Which two roles interest you, and which skills do you still need for them?' Avoid steering the student towards one career."
- statement: qaa/computing-2022/1.19.b33
  forPractitioner: { text: "Have students practise turning their study and experience into evidence of strengths for employers, including through a professional online profile.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to explain to an employer how your study and experience show your strengths and skills, including through a professional online profile.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level outcome for computing graduates (FHEQ levels 6 and 7): communicating to employers how study and experience evidence their strengths. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not claim it requires a social media presence; set it beside 1.19.b5 and 1.19.b32 here and the FHEQ descriptor qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise this when a student writes a CV, a portfolio or an online profile. To a student, put it as being able to tell an employer what your work shows about you; to staff, as an outcome placements and portfolios can build. Ask: 'Which piece of your work best shows a strength an employer wants, and how would you describe it?' Avoid writing the student's profile for them."
- statement: qaa/computing-2022/1.19.b34
  forPractitioner: { text: "Show students where CPD comes from in computing and help them build it into their career plans.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on computing courses to encourage students to explore CPD and plan for it. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a student outcome on its own; set it beside 1.19.b21 and 1.19.b28 here and the FHEQ descriptor qaa/fheq-2024/4.15.b9.3."
  author-agent-dialogue: "Raise this when a team plans careers or professional development content. Frame it for staff as making CPD visible and part of career planning. Ask: 'Where in your course do students learn how professionals in computing keep their skills current?' Avoid presenting it to a student as their duty alone."
- statement: qaa/computing-2022/1.19.b35
  forPractitioner: { text: "Involve employers when planning courses, to set up co-curricular activities and to design authentic assessments.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on course teams to work with employers where possible. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not claim it requires an employer on every course or module; set it beside 2.17 and 3.17 in this document."
  author-agent-dialogue: "Raise this when a team plans a revalidation or new assessments. Frame it for staff as using employers to make activities and assessment authentic. Ask: 'Which employer has shaped an assessment on your course, and how?' Avoid presenting it to students as their task."
- statement: qaa/computing-2022/1.19.b36
  forPractitioner: { text: "Give students room to explore workplace uses of digital technology and to practise applying it to improve digital capability.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on computing courses: encouraging students to explore and apply digital technologies at work. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not present it as a student outcome; set it beside 1.19.b37 and 1.19.b42 here and the FHEQ descriptor qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise this when a team plans placements, projects or work-related modules. Frame it for staff as giving students real workplace problems for digital technology. Ask: 'Where do students try out digital technology on a workplace problem in your course?' Avoid presenting it to students as an obligation."
- statement: qaa/computing-2022/1.19.b37
  forPractitioner: { text: "Build the core skills for applying and advancing digital technology at work into the course; employers will expect graduates to show them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Employers will expect you to show the core skills needed to use and improve digital technology at work, and your course should help you build them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level statement of employers' expectations of graduates, with a should-level duty on courses to develop the skills; the core skills follow as 1.19.b38 to 1.19.b42. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19. Do not weaken the will or turn the should into a must; set it beside 1.19.b36 here, the FHEQ descriptors qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.17.b8.1 and the reference step spine:6."
  author-agent-dialogue: "Raise this when a student asks what employers look for, or a team reviews its employability outcomes. To a student, put it as the core skills employers will expect you to show; to staff, as skills the course should develop. Ask: 'Which of the five core skills that follow could you show an employer today, and with what evidence?' Avoid reading the list aloud."
- statement: qaa/computing-2022/1.19.b38
  forPractitioner: { text: "Develop, and give students ways to evidence, the capability to work with people from a range of cultures towards shared goals, as in group work, group projects and group presentations; employers will expect it of graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Employers will expect you to be able to work with people from many cultures towards shared goals, as you do in group projects and presentations.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as one of the core skills that employers will expect computing graduates to show (the will comes from its lead-in, 1.19.b37), at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19, under Employers' perspective. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.17.b8.1, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r2/3rd to 1st and the reference step spine:6."
  author-agent-dialogue: "Bring this up when a student prepares for placements or interviews, or a team reviews employability outcomes on teamwork across cultures. To a student, say plainly that employers will expect this of you; to staff, frame it as a skill to build and assess. Ask: 'In your last group project, what did you do to help a mixed team reach a shared goal?' Avoid reading the issuer's list aloud or presenting it as one of the section 4 rungs."
- statement: qaa/computing-2022/1.19.b39
  forPractitioner: { text: "Develop, and give students ways to evidence, the capability to take responsibility, be flexible and resilient, start things themselves, assert themselves fittingly and plan, organise and manage their time; employers will expect it of graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Employers will expect you to be able to take responsibility, stay flexible and resilient, get started without being asked, speak up when it is right to and plan and manage your time.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as one of the core skills that employers will expect computing graduates to show (the will comes from its lead-in, 1.19.b37), at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19, under Employers' perspective. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.17.b8.1, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r3/3rd to 1st and the reference step spine:6."
  author-agent-dialogue: "Bring this up when a student prepares for placements or interviews, or a team reviews employability outcomes on self-management. To a student, say plainly that employers will expect this of you; to staff, frame it as a skill to build and assess. Ask: 'How do you plan your week when several deadlines fall together?' Avoid reading the issuer's list aloud or presenting it as one of the section 4 rungs."
- statement: qaa/computing-2022/1.19.b40
  forPractitioner: { text: "Develop, and give students ways to evidence, the capability to analyse themselves and show awareness of and sensitivity to diversity among people and cultures, with emotional intelligence and empathy; employers will expect it of graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Employers will expect you to be able to look honestly at yourself and show awareness of different people and cultures, with emotional intelligence and empathy.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as one of the core skills that employers will expect computing graduates to show (the will comes from its lead-in, 1.19.b37), at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19, under Employers' perspective. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.2 and qaa/fheq-2024/4.17.b8.2, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r5/3rd to 1st and the reference step spine:6."
  author-agent-dialogue: "Bring this up when a student prepares for placements or interviews, or a team reviews employability outcomes on self-reflection and empathy. To a student, say plainly that employers will expect this of you; to staff, frame it as a skill to build and assess. Ask: 'When did you last change how you worked because you understood a colleague's point of view?' Avoid reading the issuer's list aloud or presenting it as one of the section 4 rungs."
- statement: qaa/computing-2022/1.19.b41
  forPractitioner: { text: "Develop, and give students ways to evidence, the capability to listen and produce clear, well-structured communications in varied media; employers will expect it of graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Employers will expect you to be able to listen well and produce clear, well-organised communications in different media.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as one of the core skills that employers will expect computing graduates to show (the will comes from its lead-in, 1.19.b37), at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19, under Employers' perspective. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/4.17.b5, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r1/3rd to 1st and the reference step spine:6."
  author-agent-dialogue: "Bring this up when a student prepares for placements or interviews, or a team reviews employability outcomes on communication and listening. To a student, say plainly that employers will expect this of you; to staff, frame it as a skill to build and assess. Ask: 'Which medium did you choose for your last piece of communication, and why?' Avoid reading the issuer's list aloud or presenting it as one of the section 4 rungs."
- statement: qaa/computing-2022/1.19.b42
  forPractitioner: { text: "Develop, and give students ways to evidence, the capability to network with peers and scan the horizon for chances to advance digital capability and improve the future; employers will expect it of graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Employers will expect you to be able to network with peers and watch for chances to push digital capability forward and improve the future.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as one of the core skills that employers will expect computing graduates to show (the will comes from its lead-in, 1.19.b37), at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 1.19, under Employers' perspective. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/4.15.b9.3 and qaa/fheq-2024/4.17.b8.3, the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r4/3rd to 1st and the reference step spine:6."
  author-agent-dialogue: "Bring this up when a student prepares for placements or interviews, or a team reviews employability outcomes on capability advancement. To a student, say plainly that employers will expect this of you; to staff, frame it as a skill to build and assess. Ask: 'What new technology have you spotted that could change your field, and how did you hear about it?' Avoid reading the issuer's list aloud or presenting it as one of the section 4 rungs."
- statement: qaa/computing-2022/2.2
  forPractitioner: { text: "Use the current ACM and IEEE curriculum guidelines for your discipline area when designing the course and its content.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on course design: draw on the ACM and IEEE curricula, since the statement sets no syllabus. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.2. Do not claim the ACM or IEEE curricula are UK requirements; set it beside 1.2 and 2.1 here and the curricula listed in Appendix 3 (relatedTo in S7)."
  author-agent-dialogue: "Raise this when a team designs a new computing course or asks what content it must cover. Frame it for staff as the statement deferring content to the professional curricula. Ask: 'Which ACM or IEEE guideline matches your course, and where does your content depart from it?' Avoid presenting the guidelines as a checklist for students."
- statement: qaa/computing-2022/2.6.b1
  forPractitioner: { text: "Make the topic and learning outcomes explicit and choose an award title that shows how they relate to computing.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the fundamental requirements the statement sets for every computing degree course (2.6): a duty on course design, not a student outcome; the lead-in calls it a requirement but uses none of must, should or will. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.6. Do not present it as a regulatory condition; set it beside the other items 2.6.b1 to 2.6.b7 and the FHEQ statement on meeting the descriptor in full, qaa/fheq-2024/4.15.i1."
  author-agent-dialogue: "Raise this when a programme team designs, approves or reviews a computing course and checks it against the fundamental requirements. Frame it for staff as a design test on clear outcomes reflected in the award title. Ask: 'Where in your course documents could a reviewer see this, and what would they find?' Avoid presenting it to a student as their responsibility."
- statement: qaa/computing-2022/2.6.b2
  forPractitioner: { text: "Design the course so that students arriving with any of the accepted entry qualifications can succeed.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the fundamental requirements the statement sets for every computing degree course (2.6): a duty on course design, not a student outcome; the lead-in calls it a requirement but uses none of must, should or will. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.6. Do not present it as a regulatory condition; set it beside the other items 2.6.b1 to 2.6.b7 and the FHEQ statement on meeting the descriptor in full, qaa/fheq-2024/4.15.i1."
  author-agent-dialogue: "Raise this when a programme team designs, approves or reviews a computing course and checks it against the fundamental requirements. Frame it for staff as a design test on design for varied entry qualifications. Ask: 'Where in your course documents could a reviewer see this, and what would they find?' Avoid presenting it to a student as their responsibility."
- statement: qaa/computing-2022/2.6.b3
  forPractitioner: { text: "Identify the theoretical foundations of the course and give most weight to the fundamentals that outlast changes in technology.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as one of the fundamental requirements the statement sets for every computing degree course (2.6): a duty on course design, not a student outcome; the lead-in calls it a requirement but uses none of must, should or will, and the item itself says should. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.6. Do not present it as a regulatory condition; set it beside the other items 2.6.b1 to 2.6.b7 and the FHEQ statement on meeting the descriptor in full, qaa/fheq-2024/4.15.i1."
  author-agent-dialogue: "Raise this when a programme team designs, approves or reviews a computing course and checks it against the fundamental requirements. Frame it for staff as a design test on theory that lasts despite rapid change. Ask: 'Where in your course documents could a reviewer see this, and what would they find?' Avoid presenting it to a student as their responsibility."
- statement: qaa/computing-2022/2.6.b4
  forPractitioner: { text: "Plan the curriculum so theory and practice meet, and so students build attitudes and an appreciation of applications and their effect on users.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the fundamental requirements the statement sets for every computing degree course (2.6): a duty on course design, not a student outcome; the lead-in calls it a requirement but uses none of must, should or will. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.6. Do not present it as a regulatory condition; set it beside the other items 2.6.b1 to 2.6.b7 and the FHEQ statement on meeting the descriptor in full, qaa/fheq-2024/4.15.i1."
  author-agent-dialogue: "Raise this when a programme team designs, approves or reviews a computing course and checks it against the fundamental requirements. Frame it for staff as a design test on integrating theory and practice. Ask: 'Where in your course documents could a reviewer see this, and what would they find?' Avoid presenting it to a student as their responsibility."
- statement: qaa/computing-2022/2.6.b5
  forPractitioner: { text: "Make sure the modules form a cohesive, planned whole rather than a loose collection.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the fundamental requirements the statement sets for every computing degree course (2.6): a duty on course design, not a student outcome; the lead-in calls it a requirement but uses none of must, should or will. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.6. Do not present it as a regulatory condition; set it beside the other items 2.6.b1 to 2.6.b7 and the FHEQ statement on meeting the descriptor in full, qaa/fheq-2024/4.15.i1."
  author-agent-dialogue: "Raise this when a programme team designs, approves or reviews a computing course and checks it against the fundamental requirements. Frame it for staff as a design test on a cohesive set of classes. Ask: 'Where in your course documents could a reviewer see this, and what would they find?' Avoid presenting it to a student as their responsibility."
- statement: qaa/computing-2022/2.6.b6
  forPractitioner: { text: "Include a major individual activity, or a team one with real individual responsibility, that draws on the whole course and lets students show a range of abilities.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as one of the fundamental requirements the statement sets for every computing degree course (2.6): a duty on course design, not a student outcome; the lead-in calls it a requirement but uses none of must, should or will. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.6. Do not present it as a regulatory condition; set it beside the other items 2.6.b1 to 2.6.b7 and the FHEQ statement on meeting the descriptor in full, qaa/fheq-2024/4.15.i1."
  author-agent-dialogue: "Raise this when a programme team designs, approves or reviews a computing course and checks it against the fundamental requirements. Frame it for staff as a design test on a substantial individual or team activity. Ask: 'Where in your course documents could a reviewer see this, and what would they find?' Avoid presenting it to a student as their responsibility."
- statement: qaa/computing-2022/2.6.b7
  forPractitioner: { text: "Check each award against its level's qualification descriptor in the UK frameworks; the course will meet those outcomes.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level requirement on courses: every award meets the outcomes of its qualification descriptor in the Frameworks (std:doc:qaa-fheq-2024-framework), at FHEQ level 6 for honours and 7 for master's. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.6. Do not claim the statement replaces the descriptors; set it beside qaa/fheq-2024/4.15.i1 and qaa/fheq-2024/4.17.i1 and 4.2 here."
  author-agent-dialogue: "Raise this when a team maps outcomes for approval or review. Frame it for staff as a check against the national descriptor before the subject rungs. Ask: 'Which of your programme outcomes meets each part of the level descriptor?' Avoid presenting it to students."
- statement: qaa/computing-2022/2.7
  forPractitioner: { text: "Teach and practise computing so that technology removes barriers for disabled people and does not create new ones.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on computing education: care that technology enables disabled people. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.7. Do not present it as a full statement of legal duties; set it beside 2.8 and 2.9 here and the professional practice rungs from 4.6.b6."
  author-agent-dialogue: "Raise this when a team discusses accessibility in the curriculum or in student projects. Frame it for staff as the subject's own responsibility, not only a support service matter. Ask: 'Which of your students' projects would a screen reader user struggle with, and does the course teach them why?' Avoid presenting it to a student as their sole duty."
- statement: qaa/computing-2022/2.8
  forPractitioner: { text: "Teach universal access and practise it, with standards and assistive technologies; make accessibility a normal concern in the curriculum, for example wherever software lifecycles are taught.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must-level requirement that accessibility in computing education covers teaching and practice, with should-level expectations to embed it in curricula. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.8. Do not weaken the must or strengthen the should; set it beside 2.7 and 2.9 here and the practical skills rungs from 4.6.b4."
  author-agent-dialogue: "Raise this when a team reviews where accessibility appears in the curriculum. Frame it for staff as both content to teach and practice to model. Ask: 'In which module do students first test their software for accessibility, and is it assessed?' Avoid presenting it to students as their obligation."
- statement: qaa/computing-2022/2.9
  forPractitioner: { text: "Design the course with access as a primary concern, treating legal requirements as the floor; question anything, such as compulsory regular attendance, that shuts some students out.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on curriculum design, with statutory requirements as the minimum. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.9. Do not claim it sets out the law; set it beside 1.13, 2.8 and 2.14 in this document."
  author-agent-dialogue: "Raise this when a team designs delivery patterns or attendance rules. Frame it for staff as design for access first. Ask: 'Which part of your course would a student who cannot come to campus every week be unable to complete?' Avoid placing the duty on the student."
- statement: qaa/computing-2022/2.10
  forPractitioner: { text: "Plan each year so that it builds towards all the threshold subject and generic skills; a 2:2 or better is expected to fit a graduate for postgraduate study.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Each year of your course builds towards the minimum subject and general skills you need at the end, and with a second-class result or better you can expect to be ready for postgraduate study.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level description of progression through an honours degree (FHEQ level 6; FQHEIS level 10, as the paragraph states): each year builds towards the threshold rungs. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.10. Do not claim it sets entry rules for postgraduate courses; set it beside 4.5 and the threshold rungs 4.6.b1 to 4.6.b6, the FHEQ descriptor qaa/fheq-2024/4.15.b9.3 and the reference step spine:6."
  author-agent-dialogue: "Raise this when a student asks whether every year counts or whether their result will let them go on to a master's. To a student, say that each year builds towards the final minimum and that a second-class result usually opens postgraduate study; to staff, frame it as year-by-year design. Ask: 'Which threshold skills has this year moved you towards?' Avoid promising entry to a particular course."
- statement: qaa/computing-2022/2.11
  forPractitioner: { text: "On joint honours, secure the core computing skills and let the other subject add its own.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study computing with another subject, you will gain part of the computing skills and add others from your second subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level expectation for joint honours: elements of the computing skills plus those of the other subject. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.11. Do not claim joint students must meet every rung in full; set it beside 2.4 and the rungs 4.6.b1 to 4.6.b6 here and the FHEQ statement qaa/fheq-2024/4.15.i1."
  author-agent-dialogue: "Raise this when a joint honours student or their team asks which computing standards apply. To a student, say you will cover part of the computing skills and add your other subject's; to staff, frame it as a core set rather than the whole table. Ask: 'Which computing outcomes does your joint pathway cover, and where?' Avoid implying they must meet everything."
- statement: qaa/computing-2022/2.19
  forPractitioner: { text: "Include external reviewers in periodic review to test proposed changes, confirm the threshold standards and check the content.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level statement of provider practice: external reviewers in periodic review, partly to confirm threshold standards. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.19. Do not confuse it with external examining (2.20) or present it as a student outcome; set it beside 2.18 and 2.20 here and 4.5."
  author-agent-dialogue: "Raise this with a team preparing a periodic review. Frame it for staff as the outside check that the threshold rungs are met. Ask: 'Which external reviewer will see your threshold evidence, and what will they compare it with?' Avoid presenting it to students."
- statement: qaa/computing-2022/2.22
  forPractitioner: { text: "Bring students into course monitoring and review as partners.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation that courses consider including learners in monitoring and review. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 2.22. Do not claim it requires student members on every panel; set it beside 2.18 and 2.19 in this document."
  author-agent-dialogue: "Raise this when a team plans an annual monitoring or periodic review. Frame it for staff as partnership, not consultation after the event. Ask: 'Where did students shape your last course review?' Avoid presenting it to a student as an obligation."
- statement: qaa/computing-2022/3.4
  forPractitioner: { text: "Balance subject and transferable skills, individual evidence and employer needs as you develop the course; make the value of learning clear and use capstone work and teamwork.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on those who design and teach courses, with capstone activity and teamwork encouraged rather than required. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 3.4. Do not turn the encouragement into a requirement; set it beside 3.19 and 3.20 here and the team working rungs from 4.6.b5."
  author-agent-dialogue: "Raise this when a team designs assessment or the shape of the final year. Frame it for staff as balancing kinds of skill and making learning visible to students. Ask: 'How can a student evidence their own contribution in your team projects?' Avoid presenting it to students as a rule."
- statement: qaa/computing-2022/3.7
  forPractitioner: { text: "Choose teaching methods that let students show capability through the outcomes and also build competence, with independent work, in specific areas.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on teaching methods: capability shown through outcomes and competence in specific areas. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 3.7. Do not claim it prescribes particular methods; set it beside 3.8 and 3.12 here and the FHEQ descriptor qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise this when a team aligns teaching methods with outcomes. Frame it for staff as the difference between showing capability and building competence. Ask: 'In which area does your course give students enough independent practice to become competent?' Avoid presenting it to students."
- statement: qaa/computing-2022/3.9
  forPractitioner: { text: "Teach so that students reflect, justify and innovate in problem-solving; use bespoke, open source and commercial tools; accommodate varied backgrounds and remove barriers to learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on teaching, with several parts: reflective problem-solving, a range of tools, accommodating prior learning, removing barriers and attending to EDI. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 3.9. Do not present it as a student outcome; set it beside 1.11 to 1.14 and 3.10 here and the FHEQ descriptor qaa/fheq-2024/4.15.b5."
  author-agent-dialogue: "Raise this when a team reviews its teaching approaches or support for students with varied backgrounds. Frame it for staff as a checklist of teaching aims. Ask: 'Which barrier to learning in your module could you remove this year?' Avoid placing the duty on students."
- statement: qaa/computing-2022/3.10
  forPractitioner: { text: "Ground the curriculum in research and industry practice, set teaching in its legal, ethical and wider context, design it inclusively and cover sustainability and EDI.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on curriculum design: research-informed, set in its professional context, inclusively designed and covering sustainability and EDI. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 3.10. Do not present it as a student outcome; set it beside 1.11, 1.15 and 3.9 here and the professional practice rungs from 4.6.b6."
  author-agent-dialogue: "Raise this when a team revalidates a course or adds new content. Frame it for staff as checking the curriculum's context and inclusiveness as well as its technical content. Ask: 'Where does your curriculum place security, ethics and sustainability side by side with technical topics?' Avoid presenting it to students."
- statement: qaa/computing-2022/3.11
  forPractitioner: { text: "Plan progression from broad foundations to focus, and from general knowledge towards current research, with students taking more charge of their own learning at each level.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on how courses progress through levels (FHEQ 6 to 7), with typical patterns for undergraduate, generalist and specialist master's courses. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 3.11. Do not present the typical patterns as rules; set it beside 2.10, 4.12 and the FHEQ descriptors qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Raise this when a team plans the shape of a course across years or designs a generalist master's. Frame it for staff as progression in focus, currency and independence. Ask: 'How does your final year bring students closer to current research than your first?' Avoid presenting it to students as a rule."
- statement: qaa/computing-2022/3.12
  forPractitioner: { text: "Use the curriculum and outcomes to define what all graduates know and can do, and give each student room to build deeper competence in chosen areas and to evidence it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your course sets out what you will learn, and you will also have the chance to build deeper competence in some areas you choose, which you can show in a portfolio, through badges or in your CV.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level statement of what the curriculum and outcomes do, with an expectation that each student can deepen competence in some areas. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 3.12. Do not claim every student must specialise or hold micro-credentials; set it beside 3.5, 3.7 and 3.19 here and the FHEQ descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a student chooses options or a capstone topic, or asks how to show what they are best at. To a student, say you will have room to go deeper in some areas and show it; to staff, frame it as designing for individual depth. Ask: 'Which area of computing do you want to be strongest in, and how will you show it?' Avoid presenting badges as required."
- statement: qaa/computing-2022/3.13
  forPractitioner: { text: "Provide hardware and software for practical work, support staff development in computing and in teaching and expect staff to be qualified beyond the level they teach.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on institutions and staff: practical resources, continuing development and, normally, qualifications above the level taught. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 3.13. Do not present 'normally' as a must; set it beside 3.14 here and, for staff development, std:doc:advancehe-psf-dimensions-2023-framework."
  author-agent-dialogue: "Raise this when a team plans staffing, resources or staff development. Frame it for staff as institutional support for practical teaching and for their own development. Ask: 'What development in computing or pedagogy have you done this year, and who supported it?' Avoid presenting it to students."
- statement: qaa/computing-2022/3.14
  forPractitioner: { text: "If you offer an integrated specialist master's, be ready to justify your standing in the topic, usually through staff active at its forefront.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must-level requirement on institutions offering integrated specialist master's courses (FHEQ level 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 3.14. Do not extend it to other awards or present it as a student outcome; set it beside 3.13 and 4.15 to 4.17 here and the FHEQ master's descriptor qaa/fheq-2024/4.17.i1."
  author-agent-dialogue: "Raise this when a team proposes an integrated specialist master's. Frame it for staff as a firm duty to justify the course's topic. Ask: 'Which staff work at the forefront of this topic, and what is their recent scholarship?' Avoid presenting it to students."
- statement: qaa/computing-2022/3.15
  forPractitioner: { text: "Secure a strong base of core knowledge and test students' ability to learn and apply something new, often in the final major activity.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You need a firm base of core computing knowledge and the ability to use it to learn new technologies as they appear, which you would usually show in your final major project.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a graduate outcome stated with 'need to', a word outside must, should and will, so describe it as an expectation without strengthening it; it holds at every award covered (FHEQ levels 6 and 7). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 3.15. Do not present it as a must; set it beside 3.19, 1.19.b28 and the FHEQ descriptors qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/4.17.b7."
  author-agent-dialogue: "Raise this when a student plans a final project or asks how to keep up with new technology. To a student, put it as having a firm base and showing you can learn something new on your own; to staff, as an outcome the capstone can test. Ask: 'What new technique or tool have you taught yourself, and how did you apply it?' Avoid presenting it as a hard rule."
- statement: qaa/computing-2022/3.16
  forPractitioner: { text: "Build in placements or simulated work, sizeable team projects and projects set with industry or research partners.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on course delivery: applied learning in authentic or simulated work contexts. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 3.16. Do not claim placements are compulsory; set it beside 1.10, 2.15 and 3.17 here and the team working rungs from 4.6.b5."
  author-agent-dialogue: "Raise this when a team plans placements, live projects or group work. Frame it for staff as giving students authentic work contexts. Ask: 'Where do students meet a real client or an industry-set problem in your course?' Avoid presenting it to students as their obligation."
- statement: qaa/computing-2022/3.17
  forPractitioner: { text: "Design varied, engaging assessment that mirrors real contexts and lets students show their skills practically.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on assessment design: varied and authentic, with practical demonstration of skills. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 3.17. Do not claim it bans examinations; set it beside 3.18 to 3.20 and 1.19.b35 here."
  author-agent-dialogue: "Raise this when a team reviews its assessment strategy. Frame it for staff as authenticity and practical demonstration. Ask: 'Which of your assessments would a working developer recognise as real work?' Avoid presenting it to students as a rule for them."
- statement: qaa/computing-2022/3.18
  forPractitioner: { text: "Design assessments where students show what they can do, with checkpoints that confirm the work is their own; use the contract cheating guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on assessment design: chances to show practical ability, with checkpoints for authorship. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 3.18. Do not present it as an academic misconduct regulation; set it beside 3.17 here and QAA's contract cheating guidance (not yet ingested)."
  author-agent-dialogue: "Raise this when a team redesigns assessments for integrity. Frame it for staff as design that makes authorship visible. Ask: 'At which checkpoint in your project would you see that the work is the student's own?' Avoid accusing students or presenting it as their obligation."
- statement: qaa/computing-2022/3.20
  forPractitioner: { text: "Offer capstone formats beyond the dissertation where they fit; at master's level, make research literature central to them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on capstone design at master's level (FHEQ level 7), with permission for varied formats at any level. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 3.20. Do not apply the master's should to honours capstones; set it beside 3.19 here, the master's rungs from 4.14.b1.typical and the FHEQ descriptor qaa/fheq-2024/4.17.b4.1."
  author-agent-dialogue: "Raise this when a master's team designs its capstone or a student asks about formats. Frame it for staff as room for varied formats with a stronger research base at master's level. Ask: 'How does your capstone brief require students to engage with research literature?' Avoid presenting it to a student as their duty."
- statement: qaa/computing-2022/4.3
  forPractitioner: { text: "Use Annex D's descriptions of the 1st, 2:1, 2:2 and 3rd as the common reference when deciding how to evidence achievement above threshold, and record and justify any departure from the standards.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on providers to refer to Annex D (std:doc:qaa-fheq-2024-framework, Annex D) when judging achievement, with the statement that most students exceed threshold. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.3. Do not claim the statement sets the classification algorithm; set it beside 4.5 here and the Annex D summary descriptions from qaa/fheq-2024/annex-d/summary/r1/3rd to qaa/fheq-2024/annex-d/summary/r1/1st."
  author-agent-dialogue: "Raise this when a team sets marking criteria or links the rungs to classes. Frame it for staff as a pointer to Annex D and a duty to justify departures. Ask: 'How do your marking bands relate to the Annex D descriptions?' Avoid telling a student their class follows mechanically from the rungs."
- statement: qaa/computing-2022/4.5
  forPractitioner: { text: "Make sure every honours graduate reaches at least the threshold in all six categories; use the typical and excellent rungs to describe second and first-class work.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To gain an honours degree in computing, you must reach at least the minimum level in every outcome area; a first does not mean being excellent in all of them.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must-level requirement: every honours graduate meets the threshold in all outcome categories, with the issuer's own mapping of rungs to classes (threshold to third, typical to 2:1 or 2:2, excellent to first). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.5. Do not claim the mapping is fixed for every provider; set it beside the rungs 4.6.b1 to 4.6.b6, their typical and excellent records and the Annex D summary descriptions qaa/fheq-2024/annex-d/summary/r1/3rd to 1st."
  author-agent-dialogue: "Raise this when a student asks what they must do to pass, or whether a first means excellence everywhere. To a student, say plainly that you must reach the minimum in every area and that a first does not need excellence in all of them; to staff, frame it as the rule assessment must secure. Ask: 'In which outcome area are you least sure you have reached the minimum?' Avoid presenting the typical rung as the pass mark."
- statement: qaa/computing-2022/4.6.b1
  forPractitioner: { text: "Every honours graduate must reach this in subject knowledge, understanding and skills: they show the understanding of the core body of computing knowledge that their subject needs. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for an honours degree, you will show that you understand the core knowledge of your area of computing well enough for what it needs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold rung for honours graduates in computing: the minimum the award requires in Subject knowledge, understanding and skills (the main body of subject knowledge), at FHEQ level 6 (FQHEIS level 10 in Scotland). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Subject knowledge, understanding and skills row, threshold column. Do not present it as a regulatory requirement or as a master's standard, which has its own table after 4.14. Set it beside 4.6.b1.typical and 4.6.b1.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the Annex D third-class description qaa/fheq-2024/annex-d/knowledge/r1/3rd, which 4.5 says the threshold usually maps onto."
  author-agent-dialogue: "Raise this when a student asks what they must show in the main body of subject knowledge to pass, or when a team checks the minimum every graduate reaches. To a student, say plainly that this is the floor for an honours degree; to staff, frame it as what the course must secure for everyone. Ask: 'Which core topics of your subject could you explain without your notes?' Do not read the table aloud, and do not present the typical or excellent columns as the minimum."
- statement: qaa/computing-2022/4.6.b1.excellent
  forPractitioner: { text: "First-class work in subject knowledge, understanding and skills usually shows this: graduates show an exceptional grasp of the core body of knowledge with insightful critical judgement in using it, apply what the curriculum covers creatively and with innovation and reach past what was taught. Leave room in tasks for the strongest students to show it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will show an exceptional grasp of the core knowledge of your area, judge insightfully how to use it, apply it creatively and go beyond what you were taught.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung, an aspiration rather than a requirement: what first-class work in Subject knowledge, understanding and skills (the main body of subject knowledge) usually shows, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Subject knowledge, understanding and skills row, excellent column. Do not claim every first-class student must reach it in every category (4.5 says not) or that it is master's work. Set it beside 4.6.b1 and 4.6.b1.typical, the FHEQ descriptor qaa/fheq-2024/4.15.b1 and the Annex D first-class description qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this with a student aiming for a first, or a team designing stretch tasks in the main body of subject knowledge. To a student, describe it as what the strongest work shows; to staff, as the room assessment must leave at the top. Ask: 'What have you learned beyond the taught material, and how did you use it?' Avoid implying that everyone must reach it or that a first needs it in every category."
- statement: qaa/computing-2022/4.6.b1.typical
  forPractitioner: { text: "Most honours graduates reach this in subject knowledge, understanding and skills: they show a sound grasp of the core body of knowledge in their subject and use critical judgement in applying it. Design teaching and assessment so it is the usual result.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level, you will show a sound grasp of the core knowledge of your area and use critical judgement in applying it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung: what most honours graduates in computing show in Subject knowledge, understanding and skills (the main body of subject knowledge), above the threshold, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Subject knowledge, understanding and skills row, typical column. Do not present it as the pass standard; 4.5 links it to 2:1 or 2:2 performance, so set it beside 4.6.b1 and 4.6.b1.excellent, the FHEQ descriptor qaa/fheq-2024/4.15.b1 and the Annex D descriptions qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise this when a student who meets the basics in the main body of subject knowledge asks what a solid result looks like, or a team calibrates marking. To a student, describe it as the level most people reach, linked to an upper or lower second; to staff, as the expected standard above the floor. Ask: 'Where did you have to judge which part of your knowledge fitted a problem, and why?' Avoid presenting it as the pass mark."
- statement: qaa/computing-2022/4.6.b2
  forPractitioner: { text: "Every honours graduate must reach this in intellectual skills: they understand and use the subject's essential concepts, principles and practices in clearly defined scenarios, choosing and applying tools and techniques with judgement. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for an honours degree, you will understand and use the essential ideas and methods of your subject on clearly set problems, choosing suitable tools with care.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold rung for honours graduates in computing: the minimum the award requires in Intellectual skills (applying concepts, principles and practices), at FHEQ level 6 (FQHEIS level 10 in Scotland). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Intellectual skills row, threshold column. Do not present it as a regulatory requirement or as a master's standard, which has its own table after 4.14. Set it beside 4.6.b2.typical and 4.6.b2.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and the Annex D third-class description qaa/fheq-2024/annex-d/cognitive/r2/3rd, which 4.5 says the threshold usually maps onto."
  author-agent-dialogue: "Raise this when a student asks what they must show in applying concepts, principles and practices to pass, or when a team checks the minimum every graduate reaches. To a student, say plainly that this is the floor for an honours degree; to staff, frame it as what the course must secure for everyone. Ask: 'For your last assignment, why did you choose the tools you used?' Do not read the table aloud, and do not present the typical or excellent columns as the minimum."
- statement: qaa/computing-2022/4.6.b2.excellent
  forPractitioner: { text: "First-class work in intellectual skills usually shows this: graduates analyse critically and apply a wide range of the subject's ideas, principles and practices in open scenarios, choosing and using tools and techniques with refined judgement and adaptability. Leave room in tasks for the strongest students to show it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will analyse critically and apply a wide range of ideas and methods to open problems, choosing tools with refined judgement and adapting readily.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung, an aspiration rather than a requirement: what first-class work in Intellectual skills (applying concepts, principles and practices) usually shows, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Intellectual skills row, excellent column. Do not claim every first-class student must reach it in every category (4.5 says not) or that it is master's work. Set it beside 4.6.b2 and 4.6.b2.typical, the FHEQ descriptor qaa/fheq-2024/4.15.b7 and the Annex D first-class description qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise this with a student aiming for a first, or a team designing stretch tasks in applying concepts, principles and practices. To a student, describe it as what the strongest work shows; to staff, as the room assessment must leave at the top. Ask: 'Faced with an open problem, how did you weigh several approaches before choosing one?' Avoid implying that everyone must reach it or that a first needs it in every category."
- statement: qaa/computing-2022/4.6.b2.typical
  forPractitioner: { text: "Most honours graduates reach this in intellectual skills: they analyse critically and apply the subject's ideas, principles and practices where scenarios are only loosely defined, choosing and using tools and techniques with effective judgement and adaptability. Design teaching and assessment so it is the usual result.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level, you will analyse critically and apply your subject's ideas and methods to loosely defined problems, choosing tools well and adapting as you go.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung: what most honours graduates in computing show in Intellectual skills (applying concepts, principles and practices), above the threshold, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Intellectual skills row, typical column. Do not present it as the pass standard; 4.5 links it to 2:1 or 2:2 performance, so set it beside 4.6.b2 and 4.6.b2.excellent, the FHEQ descriptor qaa/fheq-2024/4.15.b7 and the Annex D descriptions qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise this when a student who meets the basics in applying concepts, principles and practices asks what a solid result looks like, or a team calibrates marking. To a student, describe it as the level most people reach, linked to an upper or lower second; to staff, as the expected standard above the floor. Ask: 'When a brief was vague, how did you decide which approach and tools to use?' Avoid presenting it as the pass mark."
- statement: qaa/computing-2022/4.6.b3
  forPractitioner: { text: "Every honours graduate must reach this in computational problem-solving: they use judgement, critical thinking and problem-solving to solve clearly specified problems and build computational artefacts with some independence. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for an honours degree, you will use judgement and critical thinking to solve clearly set problems and build working software or other artefacts with some independence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold rung for honours graduates in computing: the minimum the award requires in Computational problem-solving (computational problem-solving), at FHEQ level 6 (FQHEIS level 10 in Scotland). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Computational problem-solving row, threshold column. Do not present it as a regulatory requirement or as a master's standard, which has its own table after 4.14. Set it beside 4.6.b3.typical and 4.6.b3.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D third-class description qaa/fheq-2024/annex-d/cognitive/r3/3rd, which 4.5 says the threshold usually maps onto."
  author-agent-dialogue: "Raise this when a student asks what they must show in computational problem-solving to pass, or when a team checks the minimum every graduate reaches. To a student, say plainly that this is the floor for an honours degree; to staff, frame it as what the course must secure for everyone. Ask: 'What part of your last program or system did you work out on your own?' Do not read the table aloud, and do not present the typical or excellent columns as the minimum."
- statement: qaa/computing-2022/4.6.b3.excellent
  forPractitioner: { text: "First-class work in computational problem-solving usually shows this: graduates bring sophisticated judgement and critical thinking, research design and strong problem-solving to bear with considerable autonomy, building highly effective computational artefacts where circumstances are complex and unpredictable. Leave room in tasks for the strongest students to show it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will bring sophisticated judgement, research design and strong problem-solving to complex, unpredictable problems with real independence, building highly effective artefacts.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung, an aspiration rather than a requirement: what first-class work in Computational problem-solving (computational problem-solving) usually shows, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Computational problem-solving row, excellent column. Do not claim every first-class student must reach it in every category (4.5 says not) or that it is master's work. Set it beside 4.6.b3 and 4.6.b3.typical, the FHEQ descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D first-class description qaa/fheq-2024/annex-d/cognitive/r3/1st."
  author-agent-dialogue: "Raise this with a student aiming for a first, or a team designing stretch tasks in computational problem-solving. To a student, describe it as what the strongest work shows; to staff, as the room assessment must leave at the top. Ask: 'Which complex problem have you tackled with little guidance, and how did you design your approach?' Avoid implying that everyone must reach it or that a first needs it in every category."
- statement: qaa/computing-2022/4.6.b3.typical
  forPractitioner: { text: "Most honours graduates reach this in computational problem-solving: they use detailed judgement, critical thinking and problem-solving to solve both clearly specified and loosely defined problems and build suitable computational artefacts. Design teaching and assessment so it is the usual result.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level, you will use detailed judgement and critical thinking to solve both clearly set and loosely defined problems and build suitable artefacts.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung: what most honours graduates in computing show in Computational problem-solving (computational problem-solving), above the threshold, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Computational problem-solving row, typical column. Do not present it as the pass standard; 4.5 links it to 2:1 or 2:2 performance, so set it beside 4.6.b3 and 4.6.b3.excellent, the FHEQ descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D descriptions qaa/fheq-2024/annex-d/cognitive/r3/2.2 and qaa/fheq-2024/annex-d/cognitive/r3/2.1."
  author-agent-dialogue: "Raise this when a student who meets the basics in computational problem-solving asks what a solid result looks like, or a team calibrates marking. To a student, describe it as the level most people reach, linked to an upper or lower second; to staff, as the expected standard above the floor. Ask: 'How did you turn a loosely defined problem into something you could build?' Avoid presenting it as the pass mark."
- statement: qaa/computing-2022/4.6.b4
  forPractitioner: { text: "Every honours graduate must reach this in practical skills across the computing lifecycle: they identify and analyse a problem, then suitably design, build, test, integrate or deploy a computing system with its related artefacts, understanding how the stages connect. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for an honours degree, you will identify and analyse a problem and then design, build, test, integrate or deploy a system to solve it, knowing how the stages fit together.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold rung for honours graduates in computing: the minimum the award requires in Practical skills across the computing lifecycle (practical skills across the lifecycle), at FHEQ level 6 (FQHEIS level 10 in Scotland). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Practical skills across the computing lifecycle row, threshold column. Do not present it as a regulatory requirement or as a master's standard, which has its own table after 4.14. Set it beside 4.6.b4.typical and 4.6.b4.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and the Annex D third-class description qaa/fheq-2024/annex-d/practical/r1/3rd, which 4.5 says the threshold usually maps onto."
  author-agent-dialogue: "Raise this when a student asks what they must show in practical skills across the lifecycle to pass, or when a team checks the minimum every graduate reaches. To a student, say plainly that this is the floor for an honours degree; to staff, frame it as what the course must secure for everyone. Ask: 'Walk me through the stages of your last project, from the problem to the working system.' Do not read the table aloud, and do not present the typical or excellent columns as the minimum."
- statement: qaa/computing-2022/4.6.b4.excellent
  forPractitioner: { text: "First-class work in practical skills across the computing lifecycle usually shows this: graduates identify and analyse a problem, then suitably design, build, test, integrate or deploy a highly complex computing system with its related artefacts, understanding in depth how the stages connect and applying sophisticated problem-solving and evidence-informed evaluation. Leave room in tasks for the strongest students to show it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will do the same for a highly complex system, with a deep grasp of how the stages fit together and sophisticated, evidence-based evaluation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung, an aspiration rather than a requirement: what first-class work in Practical skills across the computing lifecycle (practical skills across the lifecycle) usually shows, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Practical skills across the computing lifecycle row, excellent column. Do not claim every first-class student must reach it in every category (4.5 says not) or that it is master's work. Set it beside 4.6.b4 and 4.6.b4.typical, the FHEQ descriptor qaa/fheq-2024/4.15.b6 and the Annex D first-class description qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this with a student aiming for a first, or a team designing stretch tasks in practical skills across the lifecycle. To a student, describe it as what the strongest work shows; to staff, as the room assessment must leave at the top. Ask: 'On your most complex system, how did a decision at one stage affect the others, and how did you evaluate it?' Avoid implying that everyone must reach it or that a first needs it in every category."
- statement: qaa/computing-2022/4.6.b4.typical
  forPractitioner: { text: "Most honours graduates reach this in practical skills across the computing lifecycle: they identify and analyse a problem, then suitably design, build, test, integrate or deploy a complex computing system with its related artefacts, understanding how the stages connect and applying problem-solving and evidence-informed evaluation. Design teaching and assessment so it is the usual result.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level, you will do the same for a complex system, knowing how the stages fit together and judging your work on evidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung: what most honours graduates in computing show in Practical skills across the computing lifecycle (practical skills across the lifecycle), above the threshold, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Practical skills across the computing lifecycle row, typical column. Do not present it as the pass standard; 4.5 links it to 2:1 or 2:2 performance, so set it beside 4.6.b4 and 4.6.b4.excellent, the FHEQ descriptor qaa/fheq-2024/4.15.b6 and the Annex D descriptions qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when a student who meets the basics in practical skills across the lifecycle asks what a solid result looks like, or a team calibrates marking. To a student, describe it as the level most people reach, linked to an upper or lower second; to staff, as the expected standard above the floor. Ask: 'How did evidence from testing change your design on a complex system?' Avoid presenting it as the pass mark."
- statement: qaa/computing-2022/4.6.b5
  forPractitioner: { text: "Every honours graduate must reach this in interpersonal and team working skills: they work effectively, including in a team, using tools and techniques suitably to communicate, organise tasks and plan projects with guidance. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for an honours degree, you will work well, including in a team, using suitable tools to communicate, organise tasks and plan projects with some guidance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold rung for honours graduates in computing: the minimum the award requires in Interpersonal and team working skills (teamwork and project working), at FHEQ level 6 (FQHEIS level 10 in Scotland). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Interpersonal and team working skills row, threshold column. Do not present it as a regulatory requirement or as a master's standard, which has its own table after 4.14. Set it beside 4.6.b5.typical and 4.6.b5.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r2/3rd, which 4.5 says the threshold usually maps onto."
  author-agent-dialogue: "Raise this when a student asks what they must show in teamwork and project working to pass, or when a team checks the minimum every graduate reaches. To a student, say plainly that this is the floor for an honours degree; to staff, frame it as what the course must secure for everyone. Ask: 'Which tools did your team use to share tasks, and what was your part?' Do not read the table aloud, and do not present the typical or excellent columns as the minimum."
- statement: qaa/computing-2022/4.6.b5.excellent
  forPractitioner: { text: "First-class work in interpersonal and team working skills usually shows this: graduates work in a highly proactive, accomplished way, including leading within a team, using tools and techniques excellently to communicate, organise tasks and plan projects proficiently with little guidance. Leave room in tasks for the strongest students to show it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will work in a highly proactive, accomplished way, taking a lead in your team and using tools excellently to plan and run projects with little guidance.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung, an aspiration rather than a requirement: what first-class work in Interpersonal and team working skills (teamwork and project working) usually shows, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Interpersonal and team working skills row, excellent column. Do not claim every first-class student must reach it in every category (4.5 says not) or that it is master's work. Set it beside 4.6.b5 and 4.6.b5.typical, the FHEQ descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D first-class description qaa/fheq-2024/annex-d/transferable/r2/1st."
  author-agent-dialogue: "Raise this with a student aiming for a first, or a team designing stretch tasks in teamwork and project working. To a student, describe it as what the strongest work shows; to staff, as the room assessment must leave at the top. Ask: 'When have you led a team, and how did you plan and run the work?' Avoid implying that everyone must reach it or that a first needs it in every category."
- statement: qaa/computing-2022/4.6.b5.typical
  forPractitioner: { text: "Most honours graduates reach this in interpersonal and team working skills: they work proactively and effectively, including in a team, using tools and techniques well to communicate clearly, organise tasks and plan projects with little guidance. Design teaching and assessment so it is the usual result.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level, you will work proactively and well in a team, using tools to communicate, organise tasks and plan projects with little guidance.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung: what most honours graduates in computing show in Interpersonal and team working skills (teamwork and project working), above the threshold, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Interpersonal and team working skills row, typical column. Do not present it as the pass standard; 4.5 links it to 2:1 or 2:2 performance, so set it beside 4.6.b5 and 4.6.b5.excellent, the FHEQ descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r2/2.2 and qaa/fheq-2024/annex-d/transferable/r2/2.1."
  author-agent-dialogue: "Raise this when a student who meets the basics in teamwork and project working asks what a solid result looks like, or a team calibrates marking. To a student, describe it as the level most people reach, linked to an upper or lower second; to staff, as the expected standard above the floor. Ask: 'Where did you step in without being asked to keep a team project on track?' Avoid presenting it as the pass mark."
- statement: qaa/computing-2022/4.6.b6
  forPractitioner: { text: "Every honours graduate must reach this in professional practice: they identify suitable practices and carry out their own work inside a professional, legal and ethical framework that covers data management and use, security, EDI and sustainability. Teaching and assessment need to secure it for all.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for an honours degree, you will choose suitable practices and work within professional, legal and ethical limits, including on data, security, equality and sustainability.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold rung for honours graduates in computing: the minimum the award requires in Professional practice (professional, legal and ethical practice), at FHEQ level 6 (FQHEIS level 10 in Scotland). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Professional practice row, threshold column. Do not present it as a regulatory requirement or as a master's standard, which has its own table after 4.14. Set it beside 4.6.b6.typical and 4.6.b6.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.2 and the Annex D third-class description qaa/fheq-2024/annex-d/transferable/r4/3rd, which 4.5 says the threshold usually maps onto."
  author-agent-dialogue: "Raise this when a student asks what they must show in professional, legal and ethical practice to pass, or when a team checks the minimum every graduate reaches. To a student, say plainly that this is the floor for an honours degree; to staff, frame it as what the course must secure for everyone. Ask: 'What legal or ethical rule applied to the data in your last project, and how did you follow it?' Do not read the table aloud, and do not present the typical or excellent columns as the minimum."
- statement: qaa/computing-2022/4.6.b6.excellent
  forPractitioner: { text: "First-class work in professional practice usually shows this: graduates identify the best practices of their kind and reach highly principled solutions inside a professional, legal and ethical framework that deal consistently with a wide range of relevant considerations, such as data management and use, security, EDI and sustainability, in their own work. Leave room in tasks for the strongest students to show it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will choose the best practices available and reach highly principled solutions that deal consistently with a wide range of professional, legal and ethical issues in your work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung, an aspiration rather than a requirement: what first-class work in Professional practice (professional, legal and ethical practice) usually shows, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Professional practice row, excellent column. Do not claim every first-class student must reach it in every category (4.5 says not) or that it is master's work. Set it beside 4.6.b6 and 4.6.b6.typical, the FHEQ descriptor qaa/fheq-2024/4.15.b9.2 and the Annex D first-class description qaa/fheq-2024/annex-d/transferable/r4/1st."
  author-agent-dialogue: "Raise this with a student aiming for a first, or a team designing stretch tasks in professional, legal and ethical practice. To a student, describe it as what the strongest work shows; to staff, as the room assessment must leave at the top. Ask: 'Where have you weighed several ethical, legal and sustainability issues at once and reached a sound solution?' Avoid implying that everyone must reach it or that a first needs it in every category."
- statement: qaa/computing-2022/4.6.b6.typical
  forPractitioner: { text: "Most honours graduates reach this in professional practice: they identify suitable practices and reach principled solutions inside a professional, legal and ethical framework that deal with the core considerations, such as data management and use, security, EDI and sustainability, in their own work. Design teaching and assessment so it is the usual result.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level, you will choose suitable practices and reach principled solutions that deal with the main professional, legal and ethical issues in your work, from data and security to equality and sustainability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung: what most honours graduates in computing show in Professional practice (professional, legal and ethical practice), above the threshold, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.6, undergraduate table, Professional practice row, typical column. Do not present it as the pass standard; 4.5 links it to 2:1 or 2:2 performance, so set it beside 4.6.b6 and 4.6.b6.excellent, the FHEQ descriptor qaa/fheq-2024/4.15.b9.2 and the Annex D descriptions qaa/fheq-2024/annex-d/transferable/r4/2.2 and qaa/fheq-2024/annex-d/transferable/r4/2.1."
  author-agent-dialogue: "Raise this when a student who meets the basics in professional, legal and ethical practice asks what a solid result looks like, or a team calibrates marking. To a student, describe it as the level most people reach, linked to an upper or lower second; to staff, as the expected standard above the floor. Ask: 'Which principled choice did you make about security, data or inclusion in a recent project?' Avoid presenting it as the pass mark."
- statement: qaa/computing-2022/4.8
  forPractitioner: { text: "Make sure master's graduates leave with advanced, current knowledge, critical skills, a grasp of professional ethics and the habit of reflecting on their own learning.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At master's level, you will have advanced, up-to-date knowledge of your subject or profession, critical skills, an understanding of professional responsibility and ethics and the habit of reflecting on how you are progressing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-level outcome for all master's graduates (FHEQ level 7; FQHEIS level 11), drawn from QAA's master's characteristics. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.8. Do not apply it to honours graduates; set it beside 4.9, the master's rungs 4.14.b1.typical and 4.14.b6.typical, the FHEQ descriptor qaa/fheq-2024/4.17.b1 and the reference step spine:7."
  author-agent-dialogue: "Raise this when a master's student or team asks what sets master's work apart. To a student, say you will have advanced, current knowledge, critical skills, a grasp of ethics and the habit of reflection; to staff, frame it as the shared core of every master's. Ask: 'Which recent development in your field could you critique, and how has your view of your own learning changed?' Avoid presenting it as the honours standard."
- statement: qaa/computing-2022/4.9
  forPractitioner: { text: "Match outcomes to the kind of master's: independent study and research methods for research master's, a research project for specialist ones and research applied to practice for professional ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on your master's, you are likely to study independently with advanced research methods, complete a research project, or, on a professional master's, bring research and critical thinking to real work situations.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome statement for three kinds of master's (FHEQ level 7): 'likely' for research and specialist master's, 'are able to' for professional or practice master's. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.9. Do not turn 'likely' into a requirement; set it beside 4.8 and 4.10 here, the FHEQ descriptors qaa/fheq-2024/4.17.b2 and qaa/fheq-2024/4.17.b4.2 and the reference step spine:7."
  author-agent-dialogue: "Raise this when a student chooses between master's types or a team designs one. To a student, explain what each type usually leads you to do; to staff, frame it as matching outcomes to the course's kind. Ask: 'Is your master's mainly research, specialist or professional, and do your outcomes show it?' Avoid presenting the likely outcomes as fixed rules."
- statement: qaa/computing-2022/4.12
  forPractitioner: { text: "Check that the content of each postgraduate course matches the FHEQ level 7 (SCQF level 11) descriptor.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on postgraduate courses to align with FHEQ level 7 or SCQF level 11 (fqheis:11). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.12. Do not claim it requires every undergraduate category to apply (4.11 says not); set it beside 4.13 and the FHEQ master's descriptor qaa/fheq-2024/4.17.i1."
  author-agent-dialogue: "Raise this when a team designs or reviews a taught master's. Frame it for staff as a level check before the subject rungs. Ask: 'Which modules carry the level 7 demands for originality and judgement without complete data?' Avoid presenting it to students."
- statement: qaa/computing-2022/4.13
  forPractitioner: { text: "Make sure every master's graduate reaches at least the threshold in each category that applies to the course; a Pass usually marks it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To gain a postgraduate degree in computing, you must reach at least the minimum level in every outcome area that applies to your course, which usually means a Pass.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must-level requirement for postgraduate computing graduates (FHEQ level 7; SCQF level 11): threshold in all relevant categories, usually a Pass. The postgraduate table gives no threshold column, so the threshold is read by reference to the undergraduate descriptors. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.13. Do not invent a master's threshold text; set it beside 4.11, 4.14, the master's rungs from 4.14.b1.typical and the FHEQ descriptor qaa/fheq-2024/4.17.i1."
  author-agent-dialogue: "Raise this when a master's student asks what they need to pass. To a student, say plainly that you must reach the minimum in every area your course covers, which usually means a Pass; to staff, frame it as the floor and note that the table only describes typical and excellent. Ask: 'Which outcome area applies to your course, and where are you least sure of the minimum?' Avoid presenting the typical column as the pass standard."
- statement: qaa/computing-2022/4.14.b1.excellent
  forPractitioner: { text: "Distinction-level work in subject knowledge, understanding and skills usually shows this: graduates show deep, systematic understanding of knowledge in their area, much of it at or shaped by the forefront, with critical awareness and advanced understanding of current problems or recent developments, originality in applying knowledge and a practical and reflective grasp of how research and enquiry techniques, both established and state-of-the-art, create and interpret knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level on a master's, you will show a deep, systematic understanding of your area, much of it close to the leading edge, an advanced and critical view of its current problems, originality in using what you know and a reflective grasp of how established and the newest research methods build knowledge.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung for taught master's graduates in Subject knowledge, understanding and skills (systematic knowledge at the forefront), usually linked to a Distinction (4.14), at FHEQ level 7 (FQHEIS and SCQF level 11). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.14, postgraduate table, Subject knowledge, understanding and skills row, excellent column. Do not claim every Distinction must show it in every category; 4.14 says not. Set it beside 4.14.b1.typical, the FHEQ master's descriptor qaa/fheq-2024/4.17.b1 and the reference step spine:7."
  author-agent-dialogue: "Raise this with a master's student aiming for a Distinction, or a team designing stretch tasks in systematic knowledge at the forefront. To a student, describe it as what the strongest master's work shows; to staff, as room assessment must leave at the top. Ask: 'Where have you applied knowledge in a way that was genuinely your own?' Avoid implying that everyone must reach it."
- statement: qaa/computing-2022/4.14.b1.typical
  forPractitioner: { text: "Most master's graduates reach this in subject knowledge, understanding and skills: they show systematic understanding of knowledge in their area of study, much of it at or shaped by the forefront of the discipline or of professional practice, critical awareness of current problems or recent developments, some originality in applying knowledge and a practical understanding of how established research and enquiry techniques create and interpret knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level on a master's, you will show a systematic understanding of your area, much of it close to the leading edge, a critical awareness of its current problems, some originality in using what you know and a practical grasp of how research builds knowledge.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung for taught master's graduates in computing in Subject knowledge, understanding and skills (systematic knowledge at the forefront), at FHEQ level 7 (FQHEIS and SCQF level 11); 4.14 links it to a Pass/Merit or Commendation. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.14, postgraduate table, Subject knowledge, understanding and skills row, typical column. The table has no threshold column, so do not invent one and do not apply this rung to honours awards. Set it beside 4.14.b1.excellent, the threshold requirement 4.13, the FHEQ master's descriptor qaa/fheq-2024/4.17.b1 and the reference step spine:7."
  author-agent-dialogue: "Raise this when a master's student asks what a solid result looks like in systematic knowledge at the forefront, or a team calibrates master's marking. To a student, describe it as the level most master's students reach; to staff, as the expected standard, with the floor set by 4.13. Ask: 'Which current problem in your field could you explain and critique?' Avoid presenting it as the bare pass standard or reading the table aloud."
- statement: qaa/computing-2022/4.14.b2.excellent
  forPractitioner: { text: "Distinction-level work in intellectual skills usually shows this: graduates analyse in depth, apply and critically evaluate leading-edge concepts, principles and practices, showing insight and innovation and applying these skills where they fit.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level on a master's, you will analyse in depth, apply and critically judge leading-edge ideas and practices, with insight and innovation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung for taught master's graduates in Intellectual skills (critical evaluation at the forefront), usually linked to a Distinction (4.14), at FHEQ level 7 (FQHEIS and SCQF level 11). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.14, postgraduate table, Intellectual skills row, excellent column. Do not claim every Distinction must show it in every category; 4.14 says not. Set it beside 4.14.b2.typical, the FHEQ master's descriptor qaa/fheq-2024/4.17.b4.1 and the reference step spine:7."
  author-agent-dialogue: "Raise this with a master's student aiming for a Distinction, or a team designing stretch tasks in critical evaluation at the forefront. To a student, describe it as what the strongest master's work shows; to staff, as room assessment must leave at the top. Ask: 'Where did your analysis of a new idea lead you to something innovative?' Avoid implying that everyone must reach it."
- statement: qaa/computing-2022/4.14.b2.typical
  forPractitioner: { text: "Most master's graduates reach this in intellectual skills: they critically evaluate, analyse and apply the concepts, principles and practices found at the leading edge of their area of study.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level on a master's, you will analyse, apply and critically judge the ideas and practices at the leading edge of your area.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung for taught master's graduates in computing in Intellectual skills (critical evaluation at the forefront), at FHEQ level 7 (FQHEIS and SCQF level 11); 4.14 links it to a Pass/Merit or Commendation. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.14, postgraduate table, Intellectual skills row, typical column. The table has no threshold column, so do not invent one and do not apply this rung to honours awards. Set it beside 4.14.b2.excellent, the threshold requirement 4.13, the FHEQ master's descriptor qaa/fheq-2024/4.17.b4.1 and the reference step spine:7."
  author-agent-dialogue: "Raise this when a master's student asks what a solid result looks like in critical evaluation at the forefront, or a team calibrates master's marking. To a student, describe it as the level most master's students reach; to staff, as the expected standard, with the floor set by 4.13. Ask: 'Which leading-edge idea in your area have you evaluated critically, and what did you conclude?' Avoid presenting it as the bare pass standard or reading the table aloud."
- statement: qaa/computing-2022/4.14.b3.excellent
  forPractitioner: { text: "Distinction-level work in computational problem-solving usually shows this: graduates show innovation or originality with sophisticated judgement, critical thinking, research design and strong problem-solving, working with considerable autonomy to build comprehensive, highly effective computational artefacts under complex or open constraints.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level on a master's, you will bring innovation or originality and sophisticated judgement to problems you tackle largely on your own, building comprehensive, highly effective artefacts under complex or open constraints.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung for taught master's graduates in Computational problem-solving (computational problem-solving with autonomy), usually linked to a Distinction (4.14), at FHEQ level 7 (FQHEIS and SCQF level 11). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.14, postgraduate table, Computational problem-solving row, excellent column. Do not claim every Distinction must show it in every category; 4.14 says not. Set it beside 4.14.b3.typical, the FHEQ master's descriptor qaa/fheq-2024/4.17.b5 and the reference step spine:7."
  author-agent-dialogue: "Raise this with a master's student aiming for a Distinction, or a team designing stretch tasks in computational problem-solving with autonomy. To a student, describe it as what the strongest master's work shows; to staff, as room assessment must leave at the top. Ask: 'What was original in the way you solved your hardest problem this year?' Avoid implying that everyone must reach it."
- statement: qaa/computing-2022/4.14.b3.typical
  forPractitioner: { text: "Most master's graduates reach this in computational problem-solving: they bring judgement, critical thinking, research design and strong problem-solving to bear with considerable autonomy, building effective computational artefacts under complex or open constraints.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level on a master's, you will use judgement, critical thinking and research design to solve problems largely on your own, building effective artefacts when the constraints are complex or open.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung for taught master's graduates in computing in Computational problem-solving (computational problem-solving with autonomy), at FHEQ level 7 (FQHEIS and SCQF level 11); 4.14 links it to a Pass/Merit or Commendation. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.14, postgraduate table, Computational problem-solving row, typical column. The table has no threshold column, so do not invent one and do not apply this rung to honours awards. Set it beside 4.14.b3.excellent, the threshold requirement 4.13, the FHEQ master's descriptor qaa/fheq-2024/4.17.b5 and the reference step spine:7."
  author-agent-dialogue: "Raise this when a master's student asks what a solid result looks like in computational problem-solving with autonomy, or a team calibrates master's marking. To a student, describe it as the level most master's students reach; to staff, as the expected standard, with the floor set by 4.13. Ask: 'How did you design your approach to a problem whose constraints were open?' Avoid presenting it as the bare pass standard or reading the table aloud."
- statement: qaa/computing-2022/4.14.b4.excellent
  forPractitioner: { text: "Distinction-level work in practical computing skills usually shows this: graduates apply state-of-the-art computing techniques suited to their area systematically and creatively in highly complex or unpredictable scenarios, making insightful decisions when data are incomplete or missing.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level on a master's, you will apply the newest computing techniques systematically and creatively in highly complex situations and make insightful decisions when data are missing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung for taught master's graduates in Practical computing skills (applying computing techniques in complex scenarios), usually linked to a Distinction (4.14), at FHEQ level 7 (FQHEIS and SCQF level 11). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.14, postgraduate table, Practical computing skills row, excellent column. Do not claim every Distinction must show it in every category; 4.14 says not. Set it beside 4.14.b4.typical, the FHEQ master's descriptor qaa/fheq-2024/4.17.b2 and the reference step spine:7."
  author-agent-dialogue: "Raise this with a master's student aiming for a Distinction, or a team designing stretch tasks in applying computing techniques in complex scenarios. To a student, describe it as what the strongest master's work shows; to staff, as room assessment must leave at the top. Ask: 'Which state-of-the-art technique have you used, and why did it fit?' Avoid implying that everyone must reach it."
- statement: qaa/computing-2022/4.14.b4.typical
  forPractitioner: { text: "Most master's graduates reach this in practical computing skills: they apply computing techniques suited to their area systematically in complex or unpredictable scenarios, making sound decisions when data are incomplete or missing.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level on a master's, you will apply suitable computing techniques systematically in complex, unpredictable situations and make sound decisions when data are missing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung for taught master's graduates in computing in Practical computing skills (applying computing techniques in complex scenarios), at FHEQ level 7 (FQHEIS and SCQF level 11); 4.14 links it to a Pass/Merit or Commendation. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.14, postgraduate table, Practical computing skills row, typical column. The table has no threshold column, so do not invent one and do not apply this rung to honours awards. Set it beside 4.14.b4.excellent, the threshold requirement 4.13, the FHEQ master's descriptor qaa/fheq-2024/4.17.b2 and the reference step spine:7."
  author-agent-dialogue: "Raise this when a master's student asks what a solid result looks like in applying computing techniques in complex scenarios, or a team calibrates master's marking. To a student, describe it as the level most master's students reach; to staff, as the expected standard, with the floor set by 4.13. Ask: 'When data were missing, how did you decide what to do next?' Avoid presenting it as the bare pass standard or reading the table aloud."
- statement: qaa/computing-2022/4.14.b5.excellent
  forPractitioner: { text: "Distinction-level work in self-directed learning and attainment usually shows this: graduates show self-direction in tackling and solving complex problems and approach and carry out tasks in a highly proactive, effective way.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level on a master's, you will direct yourself in tackling complex problems and carry out tasks in a highly proactive, effective way.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung for taught master's graduates in Self-directed learning and attainment (self-direction), usually linked to a Distinction (4.14), at FHEQ level 7 (FQHEIS and SCQF level 11). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.14, postgraduate table, Self-directed learning and attainment row, excellent column. Do not claim every Distinction must show it in every category; 4.14 says not. Set it beside 4.14.b5.typical, the FHEQ master's descriptor qaa/fheq-2024/4.17.b6 and the reference step spine:7."
  author-agent-dialogue: "Raise this with a master's student aiming for a Distinction, or a team designing stretch tasks in self-direction. To a student, describe it as what the strongest master's work shows; to staff, as room assessment must leave at the top. Ask: 'What complex task did you plan and complete on your own initiative?' Avoid implying that everyone must reach it."
- statement: qaa/computing-2022/4.14.b5.typical
  forPractitioner: { text: "Most master's graduates reach this in self-directed learning and attainment: they show some self-direction in tackling and solving problems and approach and carry out tasks proactively and effectively.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level on a master's, you will direct yourself to some extent in tackling problems and carry out tasks proactively and well.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung for taught master's graduates in computing in Self-directed learning and attainment (self-direction), at FHEQ level 7 (FQHEIS and SCQF level 11); 4.14 links it to a Pass/Merit or Commendation. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.14, postgraduate table, Self-directed learning and attainment row, typical column. The table has no threshold column, so do not invent one and do not apply this rung to honours awards. Set it beside 4.14.b5.excellent, the threshold requirement 4.13, the FHEQ master's descriptor qaa/fheq-2024/4.17.b6 and the reference step spine:7."
  author-agent-dialogue: "Raise this when a master's student asks what a solid result looks like in self-direction, or a team calibrates master's marking. To a student, describe it as the level most master's students reach; to staff, as the expected standard, with the floor set by 4.13. Ask: 'Which problem did you take on without being directed, and how did you see it through?' Avoid presenting it as the bare pass standard or reading the table aloud."
- statement: qaa/computing-2022/4.14.b6.excellent
  forPractitioner: { text: "Distinction-level work in professional practice usually shows this: graduates communicate their work accessibly and with impact to specialist and non-specialist audiences, and identify and reach the best, highly principled solutions inside a professional, legal and ethical framework, dealing consistently with a wide range of considerations such as data management and use, security, EDI and sustainability, in complex, unpredictable professional settings.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level on a master's, you will explain your work clearly and with impact to any audience, and reach the best, highly principled solutions to a wide range of professional, legal and ethical issues in complex settings.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung for taught master's graduates in Professional practice (communication and professional practice), usually linked to a Distinction (4.14), at FHEQ level 7 (FQHEIS and SCQF level 11). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.14, postgraduate table, Professional practice row, excellent column. Do not claim every Distinction must show it in every category; 4.14 says not. Set it beside 4.14.b6.typical, the FHEQ master's descriptor qaa/fheq-2024/4.17.b8.2 and the reference step spine:7."
  author-agent-dialogue: "Raise this with a master's student aiming for a Distinction, or a team designing stretch tasks in communication and professional practice. To a student, describe it as what the strongest master's work shows; to staff, as room assessment must leave at the top. Ask: 'Where have you balanced several legal, ethical and sustainability issues in a complex professional setting?' Avoid implying that everyone must reach it."
- statement: qaa/computing-2022/4.14.b6.typical
  forPractitioner: { text: "Most master's graduates reach this in professional practice: they communicate their work to specialists and to a wide range of non-specialist audiences, and identify suitable practices and work inside a professional, legal and ethical framework, covering data management and use, security, EDI and sustainability, in complex, unpredictable professional settings.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level on a master's, you will explain your work to specialists and to many kinds of non-specialist, and work within professional, legal and ethical limits, including on data, security, equality and sustainability, in complex settings.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung for taught master's graduates in computing in Professional practice (communication and professional practice), at FHEQ level 7 (FQHEIS and SCQF level 11); 4.14 links it to a Pass/Merit or Commendation. Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.14, postgraduate table, Professional practice row, typical column. The table has no threshold column, so do not invent one and do not apply this rung to honours awards. Set it beside 4.14.b6.excellent, the threshold requirement 4.13, the FHEQ master's descriptor qaa/fheq-2024/4.17.b8.2 and the reference step spine:7."
  author-agent-dialogue: "Raise this when a master's student asks what a solid result looks like in communication and professional practice, or a team calibrates master's marking. To a student, describe it as the level most master's students reach; to staff, as the expected standard, with the floor set by 4.13. Ask: 'How would you explain your project to a non-specialist manager, and what professional issues would you raise?' Avoid presenting it as the bare pass standard or reading the table aloud."
- statement: qaa/computing-2022/4.17
  forPractitioner: { text: "Make sure integrated master's graduates reach the threshold at both the honours and the master's level across all descriptors.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "On an integrated master's in computing, you must reach at least the minimum at both the honours and the master's level in every outcome area.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must-level requirement for integrated master's graduates: threshold across all descriptors at FHEQ levels 6 and 7 (FQHEIS 10 and 11). Cite it as QAA (2022), Computing Subject Benchmark Statement, para 4.17. Do not read its pointer to 'paragraphs 4.2 and 4.3' as statements; set it beside 4.5, 4.13, the rungs 4.6.b1 to 4.6.b6, the master's rungs from 4.14.b1.typical and the FHEQ descriptors qaa/fheq-2024/4.15.i1 and qaa/fheq-2024/4.17.i1."
  author-agent-dialogue: "Raise this when an integrated master's student asks what they must reach, or a team plans its final year. To a student, say you must reach the minimum at both levels; to staff, frame it as two thresholds, honours then master's. Ask: 'Which master's-level outcome is your final year built to secure?' Avoid presenting either typical column as the minimum."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.10; 4.2 (honours)" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.12; 4.2; 4.12; 4.17 (integrated and taught master's)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.10; 4.2; 4.3 (Annex D title); 4.17" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.12; 4.2; 4.17; 4.12 (as SCQF Level 11)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.10: 'FHEQ Level 6; FQHEIS Level 10'; 4.2; 4.17); agrees with std:doc:qaa-fheq-2024-framework, Table 1" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.12; 4.2; 4.12: 'FHEQ Level 7/SCQF Level 11'; 4.17); agrees with std:doc:qaa-fheq-2024-framework, S5 (shared descriptor)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.4", "1.11", "1.12", "1.13", "1.14", "1.16", "1.19", "3.9", "3.10", "4.6", "4.14"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.13", "1.14", "2.7", "2.8", "2.9"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.4", "1.15", "1.16", "1.17", "1.18", "1.19", "3.10", "4.6", "4.14"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.19", "2.17", "3.20", "4.6"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-computing-2019-benchmarks (not yet ingested)", note: "the fourth edition (2019), named in the back matter" }
- { rel: "supersedes", target: "std:doc:qaa-computing-masters-2019-benchmarks (not yet ingested)", note: "the separate Computing (Master's) statement, merged here (front matter; 1.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree outcome classification descriptions for honours (4.3)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "the Frameworks and their qualification descriptors (2.6; 4.15, cited as the 2014 edition; references)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS levels 10 and 11 (2.10; 2.12; 4.2; 4.17)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "Education for Sustainable Development Guidance (1.15)" }
- { rel: "refersTo", target: "std:doc:qaa-enterprise-2018-guidance", note: "Enterprise and Entrepreneurship Education guidance, to be read with 1.19" }
- { rel: "refersTo", target: "QAA Master's Degree Characteristics Statement (not yet ingested)", note: "4.7; 4.16" }
- { rel: "refersTo", target: "QAA contract cheating guidance, Contracting to Cheat in Higher Education (not yet ingested)", note: "3.18" }
- { rel: "refersTo", target: "QAA Advice and Guidance: Partnerships and Work-based Learning (not yet ingested)", note: "2.16" }
- { rel: "relatedTo", target: "ACM and IEEE Computing Curricula 2020 and the discipline curriculum guidelines", note: "1.2; 2.2; Appendix 3" }
- { rel: "refersTo", target: "British Computer Society accreditation requirements (not yet ingested)", note: "4.2" }
- { rel: "refersTo", target: "United Nations, Sustainable Development Goals", note: "1.4; 1.15; 1.17" }
- { rel: "refersTo", target: "OECD, Future of Education and Skills 2030", note: "3.3" }
- { rel: "refersTo", target: "York University, Decolonising the Curriculum", note: "1.14" }
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
- Computing studies how computation and computer technologies are understood, designed and exploited, joining elegant theory drawn from mathematics, engineering, psychology and design with the solving of practical problems (D1, 1.5).
- It underpins secure, reliable and usable systems of every size, is pervasive and often invisible and serves people's daily lives and careers (D1, 1.5).
- Its ways of working: disciplined problem-solving, design by choosing among alternatives with argued justification and control of complexity by abstraction and simplification and then integration (D1, 1.6).
- Innovation comes as much from foundational areas such as algorithmics and cryptography as from new technology (D1, 1.7).
- Seven discipline areas rest on computer science: computer science, computer engineering, software engineering, information technology, information systems, cybersecurity and data science; one degree may draw on several (D1, 2.1; Appendix 3).
- Specialist degrees such as networking, games, multimedia, AI or health informatics count as computing when a discipline area informs their content; merely using computers in a field does not (D1, 2.3).
- The statement sets graduate outcomes, not a syllabus; the ACM and IEEE curricula give detailed content (D1, 1.2; 1.9; 2.2).
- Problem-solving and the making of artefacts are core, learned through practical, team and capstone work and through placements (D1, 1.10; 3.4; 3.8; 3.19).
- Computing carries a particular responsibility to disabled people, since technology can remove barriers or raise them (D1, 2.7).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "a culturally responsive curriculum that represents all students, tackles the gender imbalance and guards against biased systems; an auditable list of EDI practices for courses to consider; EDI written into professional practice at every rung (D1, 1.11 to 1.14; 3.9; 3.10; 4.6; 4.14)"
  statements: ["qaa/computing-2022/1.11", "qaa/computing-2022/1.12", "qaa/computing-2022/1.19.b9", "qaa/computing-2022/1.19.b40", "qaa/computing-2022/3.9", "qaa/computing-2022/3.10", "qaa/computing-2022/4.6.b6", "qaa/computing-2022/4.6.b6.typical", "qaa/computing-2022/4.6.b6.excellent", "qaa/computing-2022/4.14.b6.typical", "qaa/computing-2022/4.14.b6.excellent"]
- theme: theme:accessibility
  inThisSubject: "computing's own responsibility to disabled people: universal access taught and practised, accessibility built into the software lifecycle and curricula designed for access beyond the statutory minimum (D1, 1.13; 1.14; 2.7 to 2.9)"
  statements: ["qaa/computing-2022/2.7", "qaa/computing-2022/2.8", "qaa/computing-2022/2.9"]
- theme: theme:esd
  inThisSubject: "the SDGs (4, 5 and 8 above all), the environmental cost of data centres, hardware and e-waste, social and economic sustainability, four ways of embedding ESD and sustainability written into professional practice at every rung (D1, 1.4; 1.15 to 1.18; 3.10; 4.6; 4.14; Appendix 2)"
  statements: ["qaa/computing-2022/1.15", "qaa/computing-2022/1.16", "qaa/computing-2022/1.18", "qaa/computing-2022/1.19.b3", "qaa/computing-2022/1.19.b24", "qaa/computing-2022/3.10", "qaa/computing-2022/4.6.b6", "qaa/computing-2022/4.6.b6.typical", "qaa/computing-2022/4.6.b6.excellent", "qaa/computing-2022/4.14.b6.typical", "qaa/computing-2022/4.14.b6.excellent"]
- theme: theme:enterprise
  inThisSubject: "read as employability in its widest sense: generic, agile, remote working, resilience and enterprise skills, a common core of subject skills, interdisciplinary thinking, career planning and employers' expected core skills; entrepreneurial capstones; teamwork at every rung (D1, 1.19; 2.17; 3.20; 4.6)"
  statements: ["qaa/computing-2022/1.19.b1", "qaa/computing-2022/1.19.b2", "qaa/computing-2022/1.19.b3", "qaa/computing-2022/1.19.b4", "qaa/computing-2022/1.19.b5", "qaa/computing-2022/1.19.b6", "qaa/computing-2022/1.19.b7", "qaa/computing-2022/1.19.b8", "qaa/computing-2022/1.19.b9", "qaa/computing-2022/1.19.b10", "qaa/computing-2022/1.19.b11", "qaa/computing-2022/1.19.b12", "qaa/computing-2022/1.19.b13", "qaa/computing-2022/1.19.b14", "qaa/computing-2022/1.19.b15", "qaa/computing-2022/1.19.b16", "qaa/computing-2022/1.19.b17", "qaa/computing-2022/1.19.b18", "qaa/computing-2022/1.19.b19", "qaa/computing-2022/1.19.b20", "qaa/computing-2022/1.19.b21", "qaa/computing-2022/1.19.b22", "qaa/computing-2022/1.19.b23", "qaa/computing-2022/1.19.b24", "qaa/computing-2022/1.19.b27", "qaa/computing-2022/1.19.b28", "qaa/computing-2022/1.19.b25", "qaa/computing-2022/1.19.b26", "qaa/computing-2022/1.19.b30", "qaa/computing-2022/1.19.b32", "qaa/computing-2022/1.19.b33", "qaa/computing-2022/1.19.b34", "qaa/computing-2022/1.19.b35", "qaa/computing-2022/1.19.b36", "qaa/computing-2022/1.19.b37", "qaa/computing-2022/1.19.b38", "qaa/computing-2022/1.19.b39", "qaa/computing-2022/1.19.b40", "qaa/computing-2022/1.19.b41", "qaa/computing-2022/1.19.b42", "qaa/computing-2022/3.20", "qaa/computing-2022/4.6.b5", "qaa/computing-2022/4.6.b5.typical", "qaa/computing-2022/4.6.b5.excellent"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "2.1", gloss: "the seven discipline areas, outlined in Appendix 3, from computer science to data science" }
  - { component: "2.2", gloss: "content informed by the ACM and IEEE curricula rather than a syllabus here" }
  - { component: "2.3", gloss: "specialist foci such as networking, games, multimedia, AI and health informatics" }
practices:
  - { component: "1.10", kind: "learning", gloss: "placements and internships" }
  - { component: "2.15", kind: "learning", gloss: "apprenticeships, placements, live projects and study abroad through partnership" }
  - { component: "3.4", kind: "teaching", gloss: "balanced skills, personalised learning, capstone activity and teamwork" }
  - { component: "3.5", kind: "learning", gloss: "evidencing competence in applied, often work-based, contexts" }
  - { component: "3.6", kind: "learning", gloss: "reflection, portfolios and personalised assessment for learner agency" }
  - { component: "3.7", kind: "teaching", gloss: "varied approaches building capability and competence" }
  - { component: "3.8", kind: "learning", gloss: "repeated practical coursework of real scale" }
  - { component: "3.9", kind: "teaching", gloss: "reflective, innovative problem-solving with varied tools" }
  - { component: "3.16", kind: "learning", gloss: "applied learning, team projects and industry or research partners" }
  - { component: "3.17", kind: "assessment", gloss: "varied, authentic, practical assessment" }
  - { component: "3.18", kind: "assessment", gloss: "academic integrity by design, with authorship checkpoints" }
  - { component: "3.19", kind: "assessment", gloss: "a capstone bringing the course together" }
  - { component: "3.20", kind: "assessment", gloss: "capstone formats beyond the dissertation; research literature at master's level" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.5", award: "bachelor's with honours", items: 6 }
  - { rung: "typical", leadIn: "4.5", award: "bachelor's with honours", items: 6 }
  - { rung: "excellent", leadIn: "4.5", award: "bachelor's with honours", items: 6 }
  - { rung: "threshold", leadIn: "4.13", award: "master's", items: 0 }
  - { rung: "typical", leadIn: "4.14", award: "master's", items: 6 }
  - { rung: "excellent", leadIn: "4.14", award: "master's", items: 6 }
  - { rung: "threshold", leadIn: "4.17", award: "integrated master's", items: 0 }
rungBases: "Two unnumbered tables. Undergraduate (after 4.6): six outcome categories, each a row with a threshold, typical and excellent cell; 4.5 requires threshold in every category and maps threshold to a third, typical to a 2:1 or 2:2 and excellent to a first. Postgraduate (after 4.14): six categories with typical and excellent cells only; 4.13 requires threshold in every relevant category by reference to the undergraduate descriptors (no master's threshold text), mapped to a Pass; typical maps to Pass/Merit or Commendation, excellent to a Distinction. Integrated master's (4.17): threshold at both levels, no table of its own. Threshold items: 6 in all; typical 12; excellent 12."
outcomeLists:
  - { leadIn: "1.19", gloss: "employability skills: generic, agile working, remote working, resilience, enterprise, a common core of subject skills, interdisciplinary thinking, careers and employers' expected core skills", items: 40, award: ["bachelor's with honours", "integrated master's", "master's"] }
outcomes:
  - { outcome: "the main body of subject knowledge", threshold: "qaa/computing-2022/4.6.b1", typical: "qaa/computing-2022/4.6.b1.typical", excellent: "qaa/computing-2022/4.6.b1.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "applying concepts, principles and practices", threshold: "qaa/computing-2022/4.6.b2", typical: "qaa/computing-2022/4.6.b2.typical", excellent: "qaa/computing-2022/4.6.b2.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "computational problem-solving", threshold: "qaa/computing-2022/4.6.b3", typical: "qaa/computing-2022/4.6.b3.typical", excellent: "qaa/computing-2022/4.6.b3.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "practical skills across the lifecycle", threshold: "qaa/computing-2022/4.6.b4", typical: "qaa/computing-2022/4.6.b4.typical", excellent: "qaa/computing-2022/4.6.b4.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "teamwork and project working", threshold: "qaa/computing-2022/4.6.b5", typical: "qaa/computing-2022/4.6.b5.typical", excellent: "qaa/computing-2022/4.6.b5.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "professional, legal and ethical practice", threshold: "qaa/computing-2022/4.6.b6", typical: "qaa/computing-2022/4.6.b6.typical", excellent: "qaa/computing-2022/4.6.b6.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "systematic knowledge at the forefront (master's)", threshold: "none", typical: "qaa/computing-2022/4.14.b1.typical", excellent: "qaa/computing-2022/4.14.b1.excellent", basis: "stated", domain: "knowledge", award: "master's" }
  - { outcome: "critical evaluation at the forefront (master's)", threshold: "none", typical: "qaa/computing-2022/4.14.b2.typical", excellent: "qaa/computing-2022/4.14.b2.excellent", basis: "stated", domain: "understanding", award: "master's" }
  - { outcome: "computational problem-solving with autonomy (master's)", threshold: "none", typical: "qaa/computing-2022/4.14.b3.typical", excellent: "qaa/computing-2022/4.14.b3.excellent", basis: "stated", domain: "subject-skill", award: "master's" }
  - { outcome: "applying computing techniques in complex scenarios (master's)", threshold: "none", typical: "qaa/computing-2022/4.14.b4.typical", excellent: "qaa/computing-2022/4.14.b4.excellent", basis: "stated", domain: "subject-skill", award: "master's" }
  - { outcome: "self-direction (master's)", threshold: "none", typical: "qaa/computing-2022/4.14.b5.typical", excellent: "qaa/computing-2022/4.14.b5.excellent", basis: "stated", domain: "generic-skill", award: "master's" }
  - { outcome: "communication and professional practice (master's)", threshold: "none", typical: "qaa/computing-2022/4.14.b6.typical", excellent: "qaa/computing-2022/4.14.b6.excellent", basis: "stated", domain: "generic-skill", award: "master's" }
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
- { body: "British Computer Society (BCS, The Chartered Institute for IT)", says: "accredits many computing degrees, so its professional competency standards will often apply (D1, 4.2)", requirements: "not yet ingested: listed in Part E" }
- { body: "Institute for Apprenticeships and Technical Education", says: "named among the bodies whose competency standards apply to accredited courses and apprenticeships (D1, 4.2)", requirements: "not yet ingested: listed in Part E" }
- { body: "Engineering Council and its recognised accreditors", says: "other accreditors recognised by the Engineering Council may accredit computing degrees, with their standards applying (D1, 4.2)", requirements: "not yet ingested: listed in Part E" }
- { body: "sector skills bodies (unnamed)", says: "named in general terms among accrediting bodies (D1, 4.2)", requirements: "not yet ingested: no body named (Part E)" }
- { body: "Association for Computing Machinery (ACM) and Institute of Electrical and Electronics Engineers (IEEE)", says: "maintain the curricula (Computing Curricula 2020 and discipline guidelines) to be used for detailed content and course design (D1, 1.2; 2.2; Appendix 3)", requirements: "not yet ingested: listed in Part E" }
- { body: "professional, statutory and regulatory bodies (PSRBs), unnamed", says: "may evaluate and accredit courses with professional or vocational outcomes, by site visits and desk review (D1, 2.21; front matter)", requirements: "not yet ingested: no body named (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.4", "1.11", "1.12", "1.13", "1.14", "1.16", "1.19", "3.9", "3.10", "4.6", "4.14"], statements: ["1.11", "1.12", "1.19.b9", "1.19.b40", "3.9", "3.10", "4.6.b6", "4.6.b6.typical", "4.6.b6.excellent", "4.14.b6.typical", "4.14.b6.excellent"] }
  - { id: "theme:accessibility", named: "Accessibility (a section 2 heading; not among the front matter themes)", carriedIn: ["1.13", "1.14", "2.7", "2.8", "2.9"], statements: ["2.7", "2.8", "2.9"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.4", "1.15", "1.16", "1.17", "1.18", "1.19", "3.10", "4.6", "4.14"], statements: ["1.15", "1.16", "1.18", "1.19.b3", "1.19.b24", "3.10", "4.6.b6", "4.6.b6.typical", "4.6.b6.excellent", "4.14.b6.typical", "4.14.b6.excellent"] }
  - { id: "theme:enterprise", named: "Entrepreneurship and enterprise education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.19", "2.17", "3.20", "4.6"], statements: ["1.19.b1", "1.19.b2", "1.19.b3", "1.19.b4", "1.19.b5", "1.19.b6", "1.19.b7", "1.19.b8", "1.19.b9", "1.19.b10", "1.19.b11", "1.19.b12", "1.19.b13", "1.19.b14", "1.19.b15", "1.19.b16", "1.19.b17", "1.19.b18", "1.19.b19", "1.19.b20", "1.19.b21", "1.19.b22", "1.19.b23", "1.19.b24", "1.19.b27", "1.19.b28", "1.19.b25", "1.19.b26", "1.19.b30", "1.19.b32", "1.19.b33", "1.19.b34", "1.19.b35", "1.19.b36", "1.19.b37", "1.19.b38", "1.19.b39", "1.19.b40", "1.19.b41", "1.19.b42", "3.20", "4.6.b5", "4.6.b5.typical", "4.6.b5.excellent"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.6", "2.10", "2.12", "4.2", "4.3", "4.12", "4.15", "4.17"] }
  - { framework: "other: FQHEIS", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.10", "2.12", "4.2", "4.3", "4.17"] }
  - { framework: "scqf", levels: ["fqheis:11"], citedIn: ["4.12"] }
bodies:
  - { body: "British Computer Society", citedIn: ["4.2"] }
  - { body: "Institute for Apprenticeships and Technical Education", citedIn: ["4.2"] }
  - { body: "Engineering Council", citedIn: ["4.2"] }
  - { body: "sector skills bodies", citedIn: ["4.2"] }
  - { body: "ACM", citedIn: ["1.2", "2.2"] }
  - { body: "IEEE", citedIn: ["1.2", "2.2"] }
  - { body: "professional and regulatory bodies, unnamed", citedIn: ["2.21"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.3"], role: "common descriptions of the four honours classes (1st, 2:1, 2:2, 3rd), for judging achievement above threshold" }
  - { document: "std:doc:qaa-fheq-2024-framework", named: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies (cited in its 2014 edition)", citedIn: ["2.6", "4.15"], role: "qualification descriptors every course meets; the length of integrated master's" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "The Education for Sustainable Development Guidance (QAA and Advance HE, 2021)", citedIn: ["1.15"], role: "teaching approaches for sustainable development" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (QAA, 2018)", citedIn: ["1.19"], role: "to be read with the employability skills" }
  - { document: "not yet ingested: listed in Part E", named: "QAA characteristics statement on master's degrees", citedIn: ["4.7", "4.16"], role: "kinds of master's and the integrated master's characteristics" }
  - { document: "not yet ingested: listed in Part E", named: "QAA's contract cheating guidance", citedIn: ["3.18"], role: "assessment integrity" }
  - { document: "not yet ingested: listed in Part E", named: "Partnerships and Work-based Learning (QAA Advice and Guidance)", citedIn: ["2.16"], role: "further advice on partnerships" }
  - { document: "not yet ingested: listed in Part E", named: "other Subject Benchmark Statements (unnamed)", citedIn: ["1.8", "2.4"], role: "joint and interdisciplinary courses" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "computing", definition: "any purposeful activity that uses, exploits or creates computing equipment and services (D1, 3.1)", beneficiaryDefinition: "anything you do on purpose that uses, makes or exploits computers and computing services", scopeNote: "the statement's working definition of its subject", category: "unknown", practices: ["computing"] }
- { slug: "computing-competence", definition: "the application of computing capabilities in applied contexts, often work-based, as distinct from capability shown through learning outcomes (D1, 3.5; 3.7)", beneficiaryDefinition: "being able to use your computing skills in real settings, such as at work", scopeNote: "competency; capability is the related term", category: "unknown", practices: ["computing", "education"] }
- { slug: "capstone-activity", definition: "a culminating activity that brings together the knowledge and practical and analytical skills of the course, as a project, end-point assessment, paper, portfolio or entrepreneurial work (D1, 3.19; 3.20)", beneficiaryDefinition: "a final major piece of work that pulls together what you have learned", scopeNote: "often near the end of the course", category: "unknown", practices: ["education"] }
- { slug: "learner-earner", definition: "a person moving between study and work through life, building on achievements without repeating study (D1, 3.1; 3.2; 3.6)", beneficiaryDefinition: "someone who keeps learning and working at the same time or in turns through life", scopeNote: "used with micro-credentials and lifelong learning", category: "unknown", practices: ["education"] }
- { slug: "entrepreneurship-and-enterprise-education", definition: "in this statement, read as employability in its widest sense (D1, 1.18 to 1.19)", beneficiaryDefinition: "learning that prepares you for work and for making things happen", scopeNote: "a cross-cutting theme", category: "unknown", practices: ["education"] }
- { slug: "externality", definition: "the use of people from outside the provider, such as external reviewers and examiners, to check standards and content (D1, 2.19; 2.20)", beneficiaryDefinition: "outside experts checking that your course meets the standards", scopeNote: "quality assurance", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "computing", form: "Computing", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "computing-competence", form: "computing competencies", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "capstone-activity", form: "capstone activity", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "learner-earner", form: "learner-earners", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "entrepreneurship-and-enterprise-education", form: "entrepreneurship and enterprise education", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "externality", form: "Externality", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Computing"
  edition: "March 2022 (fifth edition)"
  year: 2022
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/computing-2022/computing-2022.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 5985a0eb13fe5b3911daa6fdf70721dc5fb0701ce88aef32b42d09be009ce518
  heldFiles: ["wkspc2601-library/txt/qaa-2022-computing-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2022-computing-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2022-computing-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2022-computing-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
[]
```

## Part E Gaps and questions
- Rung shape (new against Psychology): the rungs are two unnumbered tables, each listing six outcome categories in rows with one cell per rung. The undergraduate table follows 4.6 and has threshold, typical and excellent columns; its cells take the ids 4.6.b<n> (threshold), 4.6.b<n>.typical and 4.6.b<n>.excellent, our ids hung on the nearest issuer paragraph (4.6 is only a cross-reference). The postgraduate table follows 4.14 and has typical and excellent columns only; its cells take 4.14.b<n>.typical and 4.14.b<n>.excellent, with no bare id because there is no threshold cell. For P3.
- The postgraduate table has no threshold column: 4.13 requires threshold attainment 'with reference to the descriptors outlined in Undergraduate standards', so the master's threshold is read against the honours table; and 4.14 says the typical descriptor goes with 'the typical threshold performance', an unclear phrase. SB4 records the master's threshold rung with items 0. For Abbott.
- Integrated master's (4.17): threshold required at both FHEQ 6 and 7 (FQHEIS 10 and 11) across "all descriptors ... in paragraphs 4.2 and 4.3"; 4.2 and 4.3 hold no descriptors, so the pointer looks like a slip carried from an earlier edition (perhaps the old sections 4.2 and 4.3 or the two tables). Not a statement (rule 3); SB4 records the rung with items 0.
- gradeOf: 18 links (each typical to its threshold, each excellent to its typical, in both tables), recorded as stated because the issuer pairs the cells in one row by category (batch 1 convention, paired cells). No link runs across the two tables.
- Rungs mapped to classes by the issuer (4.5; 4.13; 4.14): threshold to a third, typical to a 2:1 or 2:2, excellent to a first; for master's, threshold to a Pass, typical to Pass/Merit or Commendation, excellent to a Distinction. The agent instructions use these as stated; the Annex D pairings by strand (knowledge, cognitive, practical, transferable) are ours, inferred.
- Force: threshold cells take force threshold, since 4.5 defines the threshold as the minimum for honours (forceFrom 4.5). Typical and excellent cells in both tables take will from 4.1 ("will have demonstrated"; benchmark standards defined for all awards), as in Psychology and Agriculture; the issuer's own lead-ins for these rungs are descriptive ("defines outcomes usually associated with"). For P3.
- Split cells: a page break splits the practical skills row of the undergraduate table (4.6.b4) and the self-directed learning row of the postgraduate table (4.14.b5); each rung record in those rows takes one span covering the whole row, so its source holds its own words with its neighbours' interleaved.
- 1.19 employability skills: the lead-in says it is "imperative" that employability skills are embedded, with the list "acting as a guide"; the 26 skill items under Generic skills, Agile working, Remote working, Resilience, Entrepreneurship and enterprise education and the last two of the common core (1.19.b1 to b24, b27, b28) have no modal of their own and are recorded with force describes. "Imperative" is an obliging word outside the five: for Abbott whether it makes these must.
- 1.19 under Employers' perspective: the five core skills 1.19.b38 to b42 take will from their lead-in 1.19.b37 ("Employers will expect graduates to be able to demonstrate core skills"), given as forceFrom.
- 2.6: the lead-in calls its items "fundamental requirements associated with all degree courses"; "requirements" reads as must, but it is none of the five and the builder's force check matches only must and required, so items b1, b2, b4, b5 and b6 (plain present) are recorded as describes with forceFrom 2.6; b3 has its own should and b7 its own will. For Abbott: whether "requirements" counts as must; if so the check needs widening before the force can be raised.
- 3.15: "Computing graduates need to have acquired ..." ("need to", outside the five) recorded as describes. 3.3 ("it is important ... to consider"), 1.13 ("is key"), 2.17 and 3.11's "it is important that progression reflects" are obliging words outside the five, not recorded as force.
- Not recorded as statements: the 14 items of 1.14 (the issuer calls them "EDI statements" for audit against Appendix 1, but their lead-in is "could consider", which obliges nothing); the 8 items of 2.14 ("there may need to be"); 1.17's list of common ESD approaches; 1.19.b29 and 1.19.b31 (descriptive, "may", "could"). 1.14 especially is for Abbott's P3.
- Plain-present provider norms and descriptive will, not recorded (template open point 5): 1.9 and 3.2 (predictions with "will continue"), 2.18 ("will draw on" external reference points, routine practice), 2.20 ("typically, external examiners will be asked"), 4.2 ("all professional competency standards will apply in many instances", context), 4.10 (master's graduates "are equipped"), 4.15 and 4.16 (descriptive).
- Levels: fheq:6, fheq:7, fqheis:10 and fqheis:11 are all stated (2.10, 2.12, 4.2, 4.17); 4.12 names "SCQF Level 11", recorded as fqheis:11 under a separate scqf entry in SB6. CQFW is not cited. Statements in sections 1 to 3 that apply to all three awards take level fheq:6 (the lowest award's level) with award listing all three; their agent instructions name FHEQ 6 and 7.
- Awards: the statement covers bachelor's with honours, integrated master's and taught postgraduate master's; degree apprenticeships and part-time courses (1.1; 4.1) are modes of those awards, not separate awards. Research master's are mentioned only in 4.9.
- Subject codes: the statement states none; all seven in front matter (CAH11-01; HECoS 100366, 100162, 100374, 100367, 100371, 100376) are basis inferred, as are the specialism codes in S2 (100365, 101267, 100737, 100359, 100994). Computer engineering maps to computer systems engineering (100162, CAH10-01-08, an engineering code); data science has no HECoS term found. For P3.
- Themes: accessibility is a section 2 heading, not one of the front matter themes. Employability is named with enterprise in the front matter and in 1.18/1.19 and recorded under theme:enterprise. The heading and first sentence of the enterprise section fall at the end of component 1.18 in the skeleton; 1.18's record is cut by find to its own sentence. No generative AI section.
- Skeleton theme hits not kept: theme:edi in 1.10 and 2.22 and theme:accessibility in 2.6, 1.14 and theme:esd in 1.14 come only from the next sub-heading caught at the end of those components; theme:accessibility in 4.14 is "communicate ... in an accessible and impactful way", not the theme.
- Bodies: BCS, the Institute for Apprenticeships and Technical Education, the Engineering Council (and its recognised accreditors) and sector skills bodies (4.2); ACM and IEEE (1.2; 2.2); PSRBs in general (2.21; front matter). Not bodies of this kind, and not recorded in SB5: the United Nations (1.4; 1.15; 1.17), the OECD, UNESCO, the World Bank and the International Labour Organization (3.3), the Office for Students (front matter) and the Disabled Students' Commission (back matter). None of the bodies' requirements is ingested.
- Shared documents not yet ingested: QAA's Master's Degree Characteristics Statement (4.7; 4.16), the contract cheating guidance (3.18), the Partnerships and Work-based Learning advice (2.16), the Characteristics Statement: Higher Education in Apprenticeships (references list only), the two 2019 statements superseded and the ACM and IEEE curricula. The Frameworks are cited in their 2014 edition; we point to std:doc:qaa-fheq-2024-framework (inferred as the current edition).
- Appendices 1 to 3 fall inside the skeleton's back-matter component (membership of the advisory groups); they are read for SB1, SB2 and SB3 and cited as (D1, Appendix n). Appendix 1's templates are blank in the held text.
- Text faults noted, not acted on: 4.6 cites "paragraphs 4.7-4.17", though 4.15 to 4.17 are on integrated master's; 4.14 "the typical threshold performance"; 1.14.b12 "Decolonising of curriculum" (the reference list says "Decolonising the Curriculum"); 3.3 "twenty-f irst" and 3.17 "Assessment f or" (extraction spacing).
- Patterns that differ from Psychology: one statement for three awards; a master's table with no threshold column; rung tables rather than lists; a long employability skills list in section 1 with no modal; "fundamental requirements" (2.6) and "imperative" (1.19) as obliging words outside the five; a must on accessibility (2.8) and on integrated specialist master's (3.14).
- S9 commentary not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:57: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0095 (P1); built by tools/bm_build.py.
