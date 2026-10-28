---
id: std:doc:qaa-engineering-2023-benchmarks
title: "Subject Benchmark Statement Engineering"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "cah", code: "CAH10-01", label: "engineering", basis: "stated" }
  - { scheme: "cah", code: "CAH10-01-01", label: "engineering (non-specific)", basis: "inferred" }
  - { scheme: "hecos", code: "100184", label: "general or integrated engineering", basis: "inferred" }
edition: "March 2023 (fifth edition)"
published: 2023-03
status: current
supersedes: "the fourth edition (2019), named in the back matter; the front matter lists key changes from the previous statement"
heldText: { method: sha256-bytes, raw: a8bb20ba437fd6f55c1873358eb5740f59a77dc8e43c8678e16678a80096aa0e, normalised: 0597885729cfb060eb7cb81fb61bfe8455552d483583cc8faa6bd153d5cf4ce2 }
heldTextStan: { method: sha256-stan, raw: a8bb20ba437fd6f55c1873358eb5740f59a77dc8e43c8678e16678a80096aa0e, normalised: 3643699e4b88b998b00fc623b3b3787cdc42a8869115b72d7d81e3c2cf78d26a }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2022 onward series with cross-cutting themes (fifth edition of this statement)"
awardsCovered: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to the QAA Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0104 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:16"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Engineering (QAA, March 2023)

> Run 0104, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2023-engineering-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in Engineering is expected to know, understand and be able to do at the end of a BEng with honours, an MEng or a taught MSc, with the features of courses that lead there. Its subject standards are threshold lists in five outcome categories for each award; the typical and excellent levels are left to each provider's marking scheme and, for honours, to Annex D of the qualifications frameworks. Use it when designing, reviewing or describing an engineering course. It is not the profession's accreditation standard: for accredited courses the Engineering Council's AHEP outcomes are the threshold.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2023 as the fifth edition, the statement covers bachelor's degrees with honours, integrated master's and postgraduate taught master's degrees in engineering. It sets out the subject's context and purpose, its distinctive features (curriculum design, progression, partnership with industry and society, monitoring), content, teaching and assessment, and benchmark standards. Each award has a threshold list of five categories (knowledge and understanding; problem solving; analysis; delivery, skills and practice; values and principles); typical (2:1 and 2:2, or merit) and excellent (first, or distinction) defer to provider marking schemes and, for honours, Annex D. It treats equality, diversity and inclusion; accessibility; sustainability; and industry and entrepreneurship as cross-cutting themes, with ethics, safety and security as further subject sections. The Engineering Council and the professional engineering institutions shape it throughout: for accredited courses, AHEP's outcomes are the minimum threshold.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Engineering"
edition: "March 2023 (fifth edition)"
dates:
  published: 2023-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of quality requirements in Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2023", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate in Engineering is expected to know, understand and be able to do at the end of a bachelor's degree with honours, an integrated master's or a postgraduate taught master's, and the features of courses leading to them"
appliesTo:
  awards: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This Statement refers to courses of study in Engineering delivered by universities and other higher education providers.\" (D1, 1.3)"
statedSubjects:
  - { name: "Engineering", locator: "(D1, title; 1.3)", kind: "subject", codes: [{ scheme: "cah", code: "CAH10-01", label: "engineering" }] }
  - { name: "general and multidisciplinary BEng and MEng degree courses", locator: "(D1, 1.7)", kind: "programme title", codes: [{ scheme: "hecos", code: "100184", label: "general or integrated engineering" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "What is Engineering?", gloss: "engineers make technology and systems that improve and protect lives; designing things that work" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "What is Engineering?", gloss: "fair, sustainable solutions to global problems; adaptable future engineers" }
  - { number: "1.3", order: 5, componentType: stem, parent: "section 1", heading: "Engineering degree courses", gloss: "a broad subject; the three awards in scope" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Engineering degree courses", gloss: "other routes: apprenticeships and foundation degrees at Level 5" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Engineering degree courses", gloss: "the honours bachelor's: first cycle, credit, honours and ordinary titles" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Engineering degree courses", gloss: "the MEng: one designed whole, first and second cycle, credit and transfer" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Engineering degree courses", gloss: "single-specialism and general or multidisciplinary courses" }
  - { number: "1.8", order: 10, componentType: stem, parent: "section 1", heading: "Engineering degree courses", gloss: "other master's degrees: research, specialised, professional" }
  - { number: "1.9", order: 11, componentType: area, parent: "section 1", heading: "Characteristics of an Engineering degree", gloss: "the five areas students typically study" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Engineering degree", gloss: "problem types: broadly defined and complex; early exposure" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Engineering degree", gloss: "structured design tools and practical activity" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Engineering degree", gloss: "graduate engineers are in demand" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "diverse engineers and equitable solutions" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI as a professional expectation and accredited outcome; where inclusion appears" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI embedded in practice; global perspectives in curricula" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "accessibility in access to and within the curriculum" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "accessibility as standard in curricula and design" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "accessible environments for disabled students, including hidden disabilities" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "courses inspire sustainable engineers; the SDGs encouraged" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "education for sustainable development in engineering" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Ethics", gloss: "the profession's ethical principles; ethics toolkit" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Ethics", gloss: "protecting life; health and safety judgement" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Safety", gloss: "a holistic approach to safety; automation and autonomy" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Safety", gloss: "complex systems, human behaviour and safety as system qualities" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Security", gloss: "what security means" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Security", gloss: "security awareness and secure design" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Security", gloss: "security in legacy systems" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Security", gloss: "safeguarding sensitive data and secure communication" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Industry and entrepreneurship", gloss: "read with the 2018 enterprise guidance" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Industry and entrepreneurship", gloss: "industrial involvement; industry advisory boards" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Industry and entrepreneurship", gloss: "placements and support for placement students" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Professional accreditation of Engineering degrees", gloss: "professional registration and course accreditation" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Professional accreditation of Engineering degrees", gloss: "how accreditation works; progression rules" }
  - { number: "1.34", order: 36, componentType: stem, parent: "section 1", heading: "Professional accreditation of Engineering degrees", gloss: "accreditation is optional; reasons a course is not accredited" }
  - { number: "2.1", order: 38, componentType: paragraph, parent: "section 2", heading: "Curriculum design", gloss: "degrees prepare graduates to start professional careers" }
  - { number: "2.2", order: 39, componentType: paragraph, parent: "section 2", heading: "Curriculum design", gloss: "systems thinking and risk; the curriculum supports risk analysis" }
  - { number: "2.3", order: 40, componentType: practice, parent: "section 2", heading: "Curriculum design", gloss: "course design features for future challenges" }
  - { number: "2.4", order: 41, componentType: stem, parent: "section 2", heading: "Curriculum design", gloss: "inclusive course culture and its measures" }
  - { number: "2.5", order: 42, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through the bachelor's; postgraduate readiness" }
  - { number: "2.6", order: 43, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards and Scottish four-year honours" }
  - { number: "2.7", order: 44, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through the MEng; transfer to the bachelor's" }
  - { number: "2.8", order: 45, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "MEng exit awards and Scottish five-year courses" }
  - { number: "2.9", order: 46, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "general and multidisciplinary honours degrees" }
  - { number: "2.10", order: 47, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "award rules; AHEP overlay for accredited degrees" }
  - { number: "2.11", order: 48, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "keeping current through industry partnership" }
  - { number: "2.12", order: 49, componentType: stem, parent: "section 2", heading: "Partnership", gloss: "what strong industry links bring" }
  - { number: "2.13", order: 50, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "industry norms and net zero; a two-way partnership" }
  - { number: "2.14", order: 51, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership with society; community-centred design" }
  - { number: "2.15", order: 52, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "students as partners and co-creators" }
  - { number: "2.16", order: 53, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "the Engineering Council and licensed institutions" }
  - { number: "2.17", order: 54, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "international recognition: IEA, ENAEE, Washington Accord" }
  - { number: "2.18", order: 55, componentType: stem, parent: "section 2", heading: "Partnership", gloss: "organisations supporting engineering education" }
  - { number: "2.19", order: 56, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.20", order: 57, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers and industrial partners in review" }
  - { number: "2.21", order: 58, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners" }
  - { number: "2.22", order: 59, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation as assurance of professional standards" }
  - { number: "3.1", order: 61, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "content is broad and hard to prescribe" }
  - { number: "3.2", order: 62, componentType: area, parent: "section 3", heading: "Content", gloss: "the aim: tools, skills, mindset and ethics of a practising engineer" }
  - { number: "3.3", order: 63, componentType: area, parent: "section 3", heading: "Content", gloss: "practical work sets engineering apart" }
  - { number: "3.4", order: 64, componentType: area, parent: "section 3", heading: "Content", gloss: "specialist and non-specialist content; accreditation fit" }
  - { number: "3.5", order: 65, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching aligned with outcomes" }
  - { number: "3.6", order: 66, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "diverse teaching methods kept current" }
  - { number: "3.7", order: 67, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "curriculum informed by current practice; AHEP for accredited courses" }
  - { number: "3.8", order: 68, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "the bachelor's: lab work and projects in context" }
  - { number: "3.9", order: 69, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "the MEng: deeper technical work, teams and industry" }
  - { number: "3.10", order: 70, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "other master's: focus-led teaching, growing self-direction" }
  - { number: "3.11", order: 71, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "master's students with varied prior learning" }
  - { number: "3.12", order: 72, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "employability embedded in and beyond the curriculum" }
  - { number: "3.13", order: 73, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "flexible delivery for accessibility" }
  - { number: "3.14", order: 74, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment principles and methods" }
  - { number: "3.15", order: 75, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "strict failure limits on accredited degrees" }
  - { number: "4.1", order: 77, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "minimum threshold standards for the three awards" }
  - { number: "4.2", order: 78, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "meeting the standards shows the expected range" }
  - { number: "4.3", order: 79, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most students exceed the threshold" }
  - { number: "4.4", order: 80, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "standards defined against framework levels; accredited outcomes apply" }
  - { number: "4.5", order: 81, componentType: paragraph, parent: "section 4", heading: "Minimum threshold standards", gloss: "AHEP outcomes as threshold for accredited courses" }
  - { number: "4.6", order: 82, componentType: paragraph, parent: "section 4", heading: "Undergraduate benchmark standards", gloss: "honours classes in Annex D" }
  - { number: "4.7", order: 83, componentType: paragraph, parent: "section 4", heading: "Undergraduate benchmark standards", gloss: "the MEng includes and goes beyond honours outcomes" }
  - { number: "4.8", order: 84, componentType: stem, parent: "section 4", heading: "Bachelor's degree with honours", gloss: "BEng honours threshold: five outcome categories" }
  - { number: "4.9", order: 85, componentType: paragraph, parent: "section 4", heading: "Bachelor's degree with honours", gloss: "BEng typical level (2:1, 2:2) by marking scheme" }
  - { number: "4.10", order: 86, componentType: paragraph, parent: "section 4", heading: "Bachelor's degree with honours", gloss: "BEng excellent level (first) by marking scheme" }
  - { number: "4.11", order: 87, componentType: stem, parent: "section 4", heading: "Integrated master's degree", gloss: "MEng threshold: five outcome categories" }
  - { number: "4.12", order: 88, componentType: paragraph, parent: "section 4", heading: "Integrated master's degree", gloss: "MEng typical level by marking scheme" }
  - { number: "4.13", order: 89, componentType: paragraph, parent: "section 4", heading: "Integrated master's degree", gloss: "MEng excellent level by marking scheme" }
  - { number: "4.14", order: 90, componentType: paragraph, parent: "section 4", heading: "Postgraduate master's degrees benchmark standards", gloss: "MSc: at least threshold in every category" }
  - { number: "4.15", order: 91, componentType: stem, parent: "section 4", heading: "Postgraduate master's degrees benchmark standards", gloss: "MSc threshold: five outcome categories" }
  - { number: "4.16", order: 92, componentType: paragraph, parent: "section 4", heading: "Postgraduate master's degrees benchmark standards", gloss: "MSc merit by marking scheme" }
  - { number: "4.17", order: 93, componentType: paragraph, parent: "section 4", heading: "Postgraduate master's degrees benchmark standards", gloss: "MSc distinction by marking scheme" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purpose of an Engineering degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of an Engineering degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content design and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1 and S2" }
  - { number: "none", heading: "section headings 1 to 4", kind: "other: headings, recorded as sections" }
  - { number: "none", heading: "5 List of references and further resources", kind: "other: back matter, read for SB6, S7 and D3" }
  - { number: "none", heading: "6 Membership of the Advisory Groups for the Subject Benchmark Statement for Engineering", kind: "other: back matter, read for S8 (edition history)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 74 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/engineering-2023/1.2
  locator: { number: "1.2", headingPath: ["Context and purpose of an Engineering degree", "What is Engineering?"] }
  span: { start: 9750, end: 10492 }
  source: "1.2 Engineering innovation is central to delivering equitable and sustainable solutions to the most pressing global challenges. Sustainable solutions are not merely about the environment, but also addressing social and economic concerns at all levels in order to create a more robust and resilient world. Particular emphasis has been placed within this Statement on the ways in which engineers can meet the challenges defined in the United Nations Sustainable Development Goals together with the global challenges of cybersecurity, infrastructure, manufacturing, mobility and energy. Engineers of the future must be adaptable to new and emerging challenges as these arise and, as a consequence, the engineering curriculum continues to evolve."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "engineers in training and in practice"
  addressee: learner
  verbs: ["be"]
  about: "adaptable engineers and a changing curriculum"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Engineering innovation is key to fair and sustainable answers to the world's hardest problems, read through the UN Sustainable Development Goals and challenges such as cybersecurity, energy and mobility; future engineers must be able to adapt as new challenges appear, so the curriculum keeps changing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/1.5
  locator: { number: "1.5", headingPath: ["Context and purpose of an Engineering degree", "Engineering degree courses"] }
  span: { start: 11968, end: 13001 }
  source: "1.5 A bachelor’s degree with honours is a f irst cycle qualification in the overarching Qualifications Frameworks in the European Higher Education Area . It usually includes study equivalent to at least three full-time academic years (four in Scotland), of which study is equivalent to at least 90 credits at FHEQ Level 6 or SCQF Level 10. A bachelor’s degree that does not have honours also exists but is not as common as a bachelor’s degree with honours. A bachelor’s degree that does not have honours includes an ordinary degree or a pass degree; these degrees consist of a smaller volume of credit and so meet the qualification descriptor in part at Level 6 or SCQF Level 10 but not in full. In everyday usage,\n\n4\nthe ‘honours’ or ‘ordinary’ part of the degree title is often omitted and both are simply referred to as bachelor’s or BEng. This can lead to confusion, and providers should resolve such confusion through stipulating what is meant by various titles in their course information to prospective students and employers."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers awarding bachelor's degrees"
  addressee: provider
  verbs: ["resolve", "stipulating"]
  about: "making honours and non-honours bachelor's titles clear"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An honours bachelor's degree is a first-cycle award, usually three years full time (four in Scotland), with 90 or more credits at FHEQ Level 6 (SCQF Level 10); a non-honours bachelor's carries less credit and meets the level only in part. Because everyday usage drops 'honours' or 'ordinary', providers should remove the confusion by saying what each title means in their course information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/1.10
  locator: { number: "1.10", headingPath: ["Context and purpose of an Engineering degree", "Characteristics of an Engineering degree"] }
  span: { start: 16052, end: 17030 }
  source: "1.10 As students progress through an Engineering degree, depending on the nature of their course, they will either develop skills to solve broadly defined, single-domain problems, or develop skills to solve progressively more complex, integrated, socioeconomical and technological systems. Typically, broadly defined problems involve making appropriate assumptions and balancing needs of different requirements to achieve a goal. Such problems can be solved by the application of engineering science and learned analysis techniques. Complex problems, on the other hand, have no obvious, known or optimum solutions and may involve wide-ranging or conflicting technical issues and/or user needs that must be addressed through creativity and innovative application of engineering science and skills. Learners will need to be exposed to problems at an early stage in their course of study so that they have sufficient opportunities to develop their knowledge, confidence and skills."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop", "solve", "exposed"]
  about: "solving broadly defined and complex problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Depending on the course, students will build skill either in solving broadly defined problems within one domain or in tackling increasingly complex, integrated sociotechnical systems; broadly defined problems call for sensible assumptions and balanced requirements, while complex problems lack an obvious or optimal answer and demand creativity. Learners will need early exposure to problems so they get enough practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/1.15
  locator: { number: "1.15", headingPath: ["Context and purpose of an Engineering degree", "Equality, diversity and inclusion"] }
  span: { start: 18767, end: 19591 }
  source: "1.15 Equality, diversity and inclusion principles and practices are essential ingredients in engineering practice and should be embedded in all activities, from the composition of the team, the engineering process, to the solutions created for society. It is particularly valuable to consider how different cultural traditions can shape engineering design approaches. Especially for courses that include projects focused on design of solutions for developing or international contexts, it is vital that students thoroughly understand the technical and non- technical environment in which the solution will operate and ensure that cultural and user perspectives are included. Therefore, the development of Engineering curricula should foster global perspectives and facilitate the recognition of historic western assumptions."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "engineering practice and curricula"
  addressee: both
  verbs: ["embedded", "consider", "understand", "foster", "facilitate"]
  about: "EDI embedded in engineering practice and curricula"
  themes: [theme:edi]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Equality, diversity and inclusion belong in every part of engineering, from the make-up of the team through the process to the solutions society receives, and should be built into all activity; where projects design for developing or international settings, it matters greatly that students grasp the technical and wider context and include cultural and user views, so curricula should build global perspectives and help students recognise inherited western assumptions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/1.16
  locator: { number: "1.16", headingPath: ["Context and purpose of an Engineering degree", "Accessibility"] }
  span: { start: 19606, end: 20015 }
  source: "1.16 Accessibility supports the promotion and implementation of EDI. Engineering solutions can transform lives and directly facilitate accessibility and remove barriers in society. Therefore, accessibility should be considered in terms of both access to Engineering\n\n6\neducation and within curricula. As noted in paragraph 3.13, this entails the use of flexible approaches to learning teaching and assessment."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "engineering education and curricula"
  addressee: provider
  verbs: ["considered"]
  about: "accessibility in access to and within the curriculum"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Accessibility advances EDI, and engineering can itself remove barriers in society, so accessibility should be weighed both in access to engineering education and inside the curriculum, which calls for flexible learning, teaching and assessment (see 3.13)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/1.17
  locator: { number: "1.17", headingPath: ["Context and purpose of an Engineering degree", "Accessibility"] }
  span: { start: 20016, end: 20307 }
  source: "1.17 Accessibility should be treated as a standard part of Engineering curricula, particularly in design, ensuring solutions remove barriers to access and facilitate inclusion. In addition, curricula should be designed with accessibility in mind, meeting statutory requirements as a minimum."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "engineering curricula"
  addressee: provider
  verbs: ["treated", "designed"]
  about: "accessibility as standard in curricula and design"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Accessibility should be a normal part of engineering curricula, above all in design, so that solutions remove barriers and support inclusion; curricula should also be designed with accessibility in mind, at least meeting statutory requirements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/1.18
  locator: { number: "1.18", headingPath: ["Context and purpose of an Engineering degree", "Accessibility"] }
  span: { start: 20308, end: 20876 }
  source: "1.18 Furthermore, creating educational environments with accessibility as a primary concern can enable disabled students to study Engineering when without such consideration, they would be unable to do so. Accessibility considerations should remove barriers to engagement and should extend beyond practical initiatives (such as access to laboratory and workshop environments) to all areas of the curriculum, including group work and placements. Accessibility considerations should also address hidden disabilities to ensure individuals or groups are not disadvantaged."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the learning environment"
  addressee: provider
  verbs: ["remove", "extend", "address"]
  about: "removing barriers for disabled students"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Learning environments built with accessibility first can let disabled students study engineering who otherwise could not; accessibility measures should remove barriers to taking part, should reach past laboratories and workshops to every part of the curriculum including group work and placements, and should cover hidden disabilities so that no one is disadvantaged."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/1.19
  locator: { number: "1.19", headingPath: ["Context and purpose of an Engineering degree", "Sustainability"] }
  span: { start: 20892, end: 21489 }
  source: "1.19 Engineering courses should inspire students in their journey to become more sustainable engineers by equipping them with the knowledge and skills to evaluate the environmental and societal impact of solutions. Reference to the United Nations Sustainable Development Goals to inform curriculum design, pedagogy and assessment is encouraged. This includes the importance of digital accessibility and the promotion of resilience, adaptability and problem-solving. Engineering and sustainable development are closely linked, and the role of engineers is critical in building a sustainable future."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "engineering courses and their students"
  addressee: both
  verbs: ["inspire", "equipping", "evaluate"]
  about: "equipping sustainable engineers"
  themes: [theme:esd]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Courses should motivate students to become more sustainable engineers, giving them the knowledge and skills to judge the environmental and social effects of solutions; using the UN Sustainable Development Goals in curriculum design, teaching and assessment is encouraged, including digital accessibility, resilience, adaptability and problem-solving."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/1.21
  locator: { number: "1.21", headingPath: ["Context and purpose of an Engineering degree", "Ethics"] }
  span: { start: 22045, end: 22962 }
  source: "1.21 Engineers should carry out their work in accordance with the ethical principles of the profession. A revised statement on these principles was jointly produced in 2017 by the Engineering Council and Royal Academy of Engineering and covers the principles of honesty and integrity, respect for life, law, the environment and public good, accuracy and rigour, and leadership and communication. Engineers should develop a comprehension of the ethical issues inherent in engineering through their course of study together with the ability to make judgements and justify ethical choices. To support the teaching of ethics within Engineering curricula, an Engineering Ethics Toolkit has been produced by the Engineering Professors Council and can be consulted for advice and guidance on how to embed and assess ethics within the curriculum. The toolkit includes a suite of case studies for use in Engineering education."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "engineers in training"
  addressee: learner
  verbs: ["carry", "develop", "make", "justify"]
  about: "professional ethics and ethical judgement"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Engineers should work to the profession's ethical principles (the 2017 statement of the Engineering Council and Royal Academy of Engineering: honesty and integrity, respect for life, law, environment and public good, accuracy and rigour, leadership and communication) and should, through their studies, come to understand engineering's ethical issues and be able to judge and defend ethical choices; the Engineering Professors Council's toolkit supports teaching and assessing ethics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/1.22
  locator: { number: "1.22", headingPath: ["Context and purpose of an Engineering degree", "Ethics"] }
  span: { start: 22963, end: 23435 }
  source: "1.22 A key ethical consideration in engineering is the protection of life, which includes exercising professional judgement on the health and safety of engineering solutions. These engineering solutions may be legacy or may be newly created. Engineers typically have a day-to-day responsibility to protect the well-being of others and themselves and need a detailed understanding of both the legal frameworks that exist and have the skills to analyse and mitigate hazards."
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "engineers in training and in practice"
  addressee: learner
  verbs: ["protect", "analyse", "mitigate"]
  about: "protecting life: health and safety"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Protecting life is a central ethical concern, so engineers judge the health and safety of new and legacy solutions; they usually carry a daily responsibility for others' and their own well-being and need a detailed grasp of the legal frameworks and the skill to analyse and reduce hazards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/1.23
  locator: { number: "1.23", headingPath: ["Context and purpose of an Engineering degree", "Safety"] }
  span: { start: 23446, end: 23895 }
  source: "1.23 Engineering degree courses should support students in developing a holistic approach to safety throughout their course of study. This requires an understanding of human behaviour, experience of risk monitoring and management approaches and the knowledge and skills to carry out specification and testing of these system qualities. They should understand the specific threats created in the light of increased automation and autonomy of systems."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "engineering courses and their students"
  addressee: both
  verbs: ["support", "developing", "understand"]
  about: "a holistic approach to safety"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Courses should help students build an all-round approach to safety across their studies, drawing on human behaviour, risk monitoring and management and the ability to specify and test such system qualities; students should understand the particular threats raised by growing automation and autonomy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/1.24
  locator: { number: "1.24", headingPath: ["Context and purpose of an Engineering degree", "Safety"] }
  span: { start: 23896, end: 24902 }
  source: "1.24 The development of complex systems is made more challenging due to the unpredictability of behaviour and interactions, and the rapidly evolving risk climate posed by political, socio-economic and environmental change. The impact of failure on systems and the influence of human behaviour are challenging to model, yet it is essential to consider how people may act and interact with systems to ensure success. There are specific risks associated with safety which must be explicitly included in engineering design approaches - these are typically labelled as non-functional system attributes (or system qualities) and include reliability, resilience, performance and useability. Non-compliance with such requirements can result in system failure and there are often legal obligations to meet regulatory requirements. The Engineering X initiative from the Royal Academy of Engineering presents case-studies and reports for the development of safer complex systems which can be used to support teaching."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "engineering design approaches"
  addressee: both
  verbs: ["included"]
  about: "safety as a non-functional system quality in design"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Complex systems are hard to develop because behaviour and interactions are unpredictable and political, socio-economic and environmental change shifts the risks; designers must still account for how people act with systems, and safety risks must be built explicitly into design approaches as non-functional attributes such as reliability, resilience, performance and usability, since failing them can breach legal duties; Engineering X offers teaching material."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/1.26
  locator: { number: "1.26", headingPath: ["Context and purpose of an Engineering degree", "Security"] }
  span: { start: 25383, end: 25872 }
  source: "1.26 Engineers know what security is and have an awareness of how deliberate, unwanted, hostile or malicious acts could affect engineering solutions. They are able to critically analyse the security implications of their own design choices and are able to work collaboratively with others to realise systems and solutions that are robust against security threats. In doing so they appreciate the need for a holistic approach addressing the physical, people, process and technology aspects."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "engineers of the subject"
  addressee: learner
  verbs: ["know", "analyse", "work", "appreciate"]
  about: "security awareness and secure design"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Engineers know what security means and how deliberate hostile acts could affect their solutions; they can critically analyse the security consequences of their own design choices and work with others to build systems robust to threats, seeing the need to cover physical, people, process and technology aspects together."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/1.27
  locator: { number: "1.27", headingPath: ["Context and purpose of an Engineering degree", "Security"] }
  span: { start: 25873, end: 26289 }
  source: "1.27 Learners develop contextual knowledge of their subdiscipline within Engineering with an appropriate focus. As well as mitigating security issues in new engineering solutions, engineers are also able to resolve security problems that exist in legacy systems. This involves applying engineering thinking to problems that may have incomplete data and making design changes or developments to affect an improvement."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "engineers of the subject"
  addressee: learner
  verbs: ["develop", "resolve", "applying", "making"]
  about: "resolving security problems in legacy systems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Learners gain context-specific knowledge of their branch of engineering; besides reducing security risks in new solutions, engineers can fix security weaknesses in existing systems, applying engineering thinking where data may be incomplete and changing designs to improve them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/1.28
  locator: { number: "1.28", headingPath: ["Context and purpose of an Engineering degree", "Security"] }
  span: { start: 26290, end: 26847 }
  source: "1.28 Engineers commonly handle sensitive data and have the skills and knowledge to safeguard it against direct potential security threats. They have an awareness of the importance of managing and protecting data and information and know the legal frameworks that exist. Sensitive data could come in the form of personal data, defence data or designs, or commercially sensitive information. Engineers also have an awareness of the ethical and legal implications of sharing information and can make informed decisions regarding security-minded communications."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "engineers of the subject"
  addressee: learner
  verbs: ["handle", "safeguard", "make"]
  about: "safeguarding sensitive data"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Engineers often hold sensitive data, personal, defence or commercial, and have the knowledge and skill to protect it from security threats; they understand the importance of managing data, know the relevant legal frameworks and the ethical and legal side of sharing information, and can decide well about security-minded communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/1.31
  locator: { number: "1.31", headingPath: ["Context and purpose of an Engineering degree", "Industry and entrepreneurship"] }
  span: { start: 27475, end: 27748 }
  source: "1.31 Some students take part in placements and internships which can be integrated into their degree course. Students who elect to take a formal industrial placement should receive continued support from their institution to ensure educational as well as financial benefit."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "institutions with placement students"
  addressee: provider
  verbs: ["receive", "ensure"]
  about: "support for students on industrial placements"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Some students take placements or internships built into their degree; those who choose a formal industrial placement should get continued support from their institution so that they gain educationally as well as financially."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/1.32
  locator: { number: "1.32", headingPath: ["Context and purpose of an Engineering degree", "Professional accreditation of Engineering degrees"] }
  span: { start: 27799, end: 28382 }
  source: "1.32 Engineers practice in a variety of professions; some of their roles require professional registration with a licensed engineering institution, while for many others registration is desirable. The academic course of study must meet specific requirements and standards if it is to contribute towards the student’s professional registration and the course must undergo periodic accreditation. The accreditation length awarded is usually no more than five years. Readers are referred to the Engineering Council's Accreditation of Higher Education Programmes (AHEP) for more details."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "courses contributing to professional registration"
  addressee: provider
  verbs: ["meet", "undergo"]
  about: "accreditation for professional registration"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Engineers work across many professions, some of which need registration with a licensed institution; for a course to count towards a student's registration it must meet set requirements and standards and be accredited periodically, usually for up to five years, as AHEP explains."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/1.33
  locator: { number: "1.33", headingPath: ["Context and purpose of an Engineering degree", "Professional accreditation of Engineering degrees"] }
  span: { start: 28383, end: 29499 }
  source: "1.33 Engineering accreditation in the UK is a rigorous peer-review process undertaken by one or more professional engineering institutions (PEIs) under license from the Engineering Council. Accreditation is applied to individual courses, not departments. Part of the process of accreditation is to ensure that specific educational courses, delivered at a specific site or sites, provide some, or all, of the underpinning knowledge and understanding for eventual professional registration in a particular category, such as Incorporated Engineer (IEng) or Chartered Engineer (CEng). This requires reviewing degree courses to ensure that all graduates satisf y the prescribed learning outcomes by viewing assessments, facilities for being taught the discipline, staffing and other factors. The standard expected for all learning outcomes is the minimum threshold level. Accredited degree courses also have to meet stringent requirements with regard to progression. The reason for this is to reduce the likelihood that degree graduates have gaps in their education which would make them unfit to practice the profession."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "accredited courses"
  addressee: provider
  verbs: ["meet", "reviewing"]
  about: "the accreditation process and progression rules"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Accreditation in the UK is peer review by professional engineering institutions licensed by the Engineering Council, applied to single courses at named sites, checking that they give the grounding for registration as IEng or CEng; reviewers examine assessments, facilities and staffing so that every graduate meets the prescribed outcomes at the minimum threshold, and accredited courses also have to meet strict progression requirements so graduates have no gaps unfitting them for practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of an Engineering degree", "Curriculum design"] }
  span: { start: 30715, end: 30990 }
  source: "2.1 Engineering degrees are designed to equip graduates with integrated knowledge, skills and judgement which will enable them to begin a professional career in the engineering sector. Engineering degrees usually have some industrial involvement in their design and delivery."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["equip", "enable", "begin"]
  about: "readiness to start a professional career"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Engineering degrees are built to give graduates joined-up knowledge, skills and judgement that will let them start a professional career in engineering, and usually involve industry in their design and teaching."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/2.2
  locator: { number: "2.2", headingPath: ["Distinctive features of an Engineering degree", "Curriculum design"] }
  span: { start: 30991, end: 31767 }
  source: "2.2 Engineering is a sector that works with and across multiple other technical and non- technical disciplines and within a variety of contexts. The design of an Engineering degree prepares graduates to apply systems thinking to engineering products and processes, equipping them to unpick and predict system-level interactions that move beyond technical considerations to encompass economic, political, legal, social, environmental and ethical considerations. The curriculum should support engineers in analysing and mitigating the risks posed to a system (especially those concerned with safety and security). In doing so, Engineering graduates are equipped to optimise designs to prevent failure, reduce bias and be effective advocates for social and environmental justice."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "the curriculum and its graduates"
  addressee: both
  verbs: ["support", "analysing", "mitigating", "apply", "optimise"]
  about: "systems thinking and risk mitigation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Engineering crosses technical and non-technical fields, so the degree readies graduates to think in systems and foresee system-level effects that reach into economic, political, legal, social, environmental and ethical matters; the curriculum should help engineers analyse and reduce risks to systems, above all to safety and security, so they can design against failure, cut bias and argue for social and environmental justice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/2.3.b1
  locator: { number: "2.3.b1", headingPath: ["Distinctive features of an Engineering degree", "Curriculum design"] }
  span: { start: 31879, end: 32235 }
  source: "For students to achieve a rounded competence in Engineering, the expectation is that they have significant exposure to practical work, including hands-on laboratory and project work. Experiential learning can help students to understand concepts, and gain an appreciation of the logistics and health, safety and well-being aspects of practical engineering."
  stem: "2.3"
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "the expectation is" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: both
  verbs: ["achieve", "understand", "gain"]
  about: "substantial practical and laboratory work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "To become rounded engineers, students are expected to have substantial practical experience, including hands-on laboratory and project work; learning by doing helps them grasp concepts and the logistics and health, safety and well-being sides of practical engineering."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/2.3.b2
  locator: { number: "2.3.b2", headingPath: ["Distinctive features of an Engineering degree", "Curriculum design"] }
  span: { start: 32238, end: 32383 }
  source: "Students should be given sufficient opportunities to develop mathematic and scientific literacies relevant to their discipline or specialisation."
  stem: "2.3"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "engineering courses"
  addressee: provider
  verbs: ["given", "develop"]
  about: "mathematical and scientific literacy"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Students should have enough opportunity to build the mathematical and scientific literacy their discipline or specialism needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/2.3.b3
  locator: { number: "2.3.b3", headingPath: ["Distinctive features of an Engineering degree", "Curriculum design"] }
  span: { start: 32386, end: 32552 }
  source: "The curriculum should offer plenty of opportunities for students to acquire and enhance digital skills reflecting the societal needs in an increasingly digital world."
  stem: "2.3"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the curriculum"
  addressee: provider
  verbs: ["offer", "acquire", "enhance"]
  about: "digital skills"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "The curriculum should give students many chances to gain and improve digital skills that match society's needs in a more and more digital world."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/2.3.b4
  locator: { number: "2.3.b4", headingPath: ["Distinctive features of an Engineering degree", "Curriculum design"] }
  span: { start: 32555, end: 32886 }
  source: "A balance of individual and facilitated group project work can help students develop those competencies in self-directed learning, teamwork and leadership that are required for graduate-level work. Students at higher FHEQ/FQHEIS levels are expected to be increasingly autonomous learners and require less facilitation in groupwork."
  stem: "2.3"
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "students at higher levels"
  addressee: learner
  verbs: ["develop"]
  about: "autonomy, teamwork and leadership"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "A mix of individual and supported group projects can build the self-directed learning, teamwork and leadership graduate work needs; students at higher FHEQ and FQHEIS levels are expected to learn more independently and to need less help in group work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/2.3.b6
  locator: { number: "2.3.b6", headingPath: ["Distinctive features of an Engineering degree", "Curriculum design"] }
  span: { start: 33134, end: 33512 }
  source: "The curriculum typically includes both design and research-led projects informed by industrial and societal needs. These should incorporate aspects of inclusive and accessible design and practice and students should develop the ability to meet a combination of economic, social and environmental needs together with knowledge of their professional responsibilities as engineers."
  stem: "2.3"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "projects and their students"
  addressee: both
  verbs: ["incorporate", "develop", "meet"]
  about: "inclusive design and professional responsibility in projects"
  themes: [theme:edi]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Courses usually include design and research projects driven by industry and society; these should build in inclusive and accessible design and practice, and students ought to become able to balance economic, social and environmental needs and know their professional duties as engineers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/2.3.b7
  locator: { number: "2.3.b7", headingPath: ["Distinctive features of an Engineering degree", "Curriculum design"] }
  span: { start: 33515, end: 34117 }
  source: "Uncertainty and competing factors are often an inherent part of engineering problem-definition and solving, and therefore an Engineering degree provides graduates with an ability to manage compromise. Students at higher FHEQ/FQHEIS levels are expected to be able to handle progressively more complex scenarios with an increasing amount of conflicting and/or missing information, and use critical reasoning to make rational, effective and justified\n\n11\ndecisions. This approach can benefit from being applied beyond design modules in order to help students gain familiarity with working with complexity."
  stem: "2.3"
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "students at higher levels"
  addressee: learner
  verbs: ["handle", "use", "make"]
  about: "managing compromise, complexity and missing information"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Uncertainty and competing factors are part of defining and solving engineering problems, so the degree gives graduates the ability to manage compromise; at higher FHEQ and FQHEIS levels students are expected to deal with more complex cases with more conflicting or missing information, and to reason critically to rational, justified decisions; applying this beyond design modules helps."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/2.3.b9
  locator: { number: "2.3.b9", headingPath: ["Distinctive features of an Engineering degree", "Curriculum design"] }
  span: { start: 34444, end: 34750 }
  source: "The ability to evaluate the lifecycle and environmental impact of engineering decisions is necessary in designing within the global context of climate change. Alongside the understanding of low-carbon and clean technologies, students should also be able to evaluate the impact of exploitation of resources."
  stem: "2.3"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["evaluate"]
  about: "lifecycle and resource impact"
  themes: [theme:esd]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Assessing the whole-life and environmental effects of engineering decisions is necessary for design in a world facing climate change; besides understanding low-carbon and clean technology, students should be able to assess the impact of exploiting resources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/2.3.b10
  locator: { number: "2.3.b10", headingPath: ["Distinctive features of an Engineering degree", "Curriculum design"] }
  span: { start: 34753, end: 35045 }
  source: "Engineering courses within the UK attract a significant number of overseas students and students from the UK have the opportunity to work across the world and with international teams. Students should therefore possess cultural competencies to prepare them for working within a global sector."
  stem: "2.3"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["possess", "prepare"]
  about: "cultural competence for a global sector"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "UK engineering courses draw many international students and UK students can work worldwide and in international teams, so students should have the cultural competence to work in a global sector."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of an Engineering degree", "Curriculum design"] }
  span: { start: 35046, end: 36192 }
  source: "2.4 Students can be significantly impacted by the way courses are structured, delivered and assessed. Understanding these potential impacts and how best to address them can be achieved through the use of inclusive education approaches. Such an inclusive culture within Engineering courses requires nurturing, ongoing re-evaluation and an evidence-informed approach. Measures to promote an inclusive engineering community include:\n• student-centred course design that facilitates an inclusive culture in which individual differences are recognised as a strength and incorporated, enabling all individuals to be successf ul\n• course design that promotes belonging and ensure equitable experiences for all students, including accommodations, and do not disadvantage any students\n• embedding opportunities to increase awareness and understanding of all aspects of EDI, including equity, justice and human rights, through knowledge and experience\n• building in key EDI elements for supporting collaboration and facilitating self- reflection and an understanding of others in order to appreciate a wide range of personal characteristics and identities."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "engineering courses"
  addressee: provider
  verbs: ["requires", "promote"]
  about: "an inclusive course culture"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "How courses are structured, delivered and assessed can strongly affect students, and inclusive education approaches help address this; an inclusive culture requires nurturing, constant re-evaluation and evidence, through student-centred design that values difference, design that fosters belonging and fair experience, chances to learn about every side of EDI, equity, justice and human rights among them, and EDI elements that support collaboration and self-reflection."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of an Engineering degree", "Progression"] }
  span: { start: 36205, end: 37080 }
  source: "2.5 Over the course of a bachelor’s degree (FHEQ Level 6; FQHEIS Level 10) an Engineering student will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the attainment of certain levels of knowledge, expertise and experience that build towards the final achievement of meeting the threshold-level subject-specific and generic skills listed in this Statement. Upon graduation from an undergraduate degree, it would be expected that a student who had achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in Engineering or an associated subject. Entry requirements to postgraduate courses are, however, determined by individual providers and may require specified levels of achievement at undergraduate level."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on a bachelor's degree"
  addressee: learner
  verbs: ["progress", "build"]
  about: "progression through an honours degree"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Across a bachelor's degree at FHEQ Level 6 or FQHEIS Level 10, a student will move up level by level under institutional rules, each level adding knowledge, expertise and experience towards the threshold subject and generic skills; a graduate with a second-class degree or better would be expected to be ready for postgraduate study, though entry rules are set by each provider."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of an Engineering degree", "Progression"] }
  span: { start: 37649, end: 38595 }
  source: "2.7 Over the course of an integrated master’s degree (FHEQ Level 7; FQHEIS Level 11) an Engineering student will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each year would see the attainment of certain levels of knowledge, expertise and experience that build towards the final achievement of meeting the threshold-level subject-specific and generic skills listed in this Statement. Integrated master’s courses often have more stringent progression requirements than BEng(hons) degrees, and students who do not meet the progression requirements may be transferred onto a corresponding bachelor’s degree. Upon graduation from an integrated master’s degree, it would be expected that a student who had achieved a third-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in Engineering or an associated subject."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "students on an integrated master's"
  addressee: learner
  verbs: ["progress", "build", "transferred"]
  about: "progression through an integrated master's"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Across an integrated master's degree at FHEQ Level 7 or FQHEIS Level 11, a student will move up level by level under institutional rules, each year adding towards the threshold subject and generic skills; MEng progression rules are often stricter than BEng ones, so those who miss them may move to the matching bachelor's, and a graduate with a third or better would be expected to be ready for postgraduate study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of an Engineering degree", "Progression"] }
  span: { start: 39182, end: 39532 }
  source: "2.9 General and multidisciplinary undergraduate honours degrees will achieve core elements of the specific and generic skills for Engineering, and will add others according to the subjects covered in joint courses. Additionally, they may explore the overlap between their two subject areas, creating further opportunities for interdisciplinary study."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "general and multidisciplinary honours degrees"
  addressee: both
  verbs: ["achieve", "add", "explore"]
  about: "general and multidisciplinary degrees"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "General and multidisciplinary honours degrees will reach the core subject and generic skills of engineering and will add others from the subjects in the joint course, and may explore where their subjects overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of an Engineering degree", "Progression"] }
  span: { start: 39533, end: 40376 }
  source: "2.10 An Engineering degree is awarded as a result of a student demonstrating that they have met the learning outcomes of the course and the higher education provider regulations governing the award of degrees. An accredited degree is awarded when a student has also demonstrated the learning outcomes required by the applicable Accreditation of Higher Education Programmes (AHEP) regulations and any additional requirements for their discipline prescribed by their professional engineering institution. The overlay of these AHEP requirements may mean that students registered on an accredited degree course are required to meet these more challenging requirements until such time as the attainment of an accredited degree is no longer possible for the student. At which time, the standard higher education provider regulations will be applied."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "students on accredited courses"
  addressee: learner
  verbs: ["demonstrating", "met", "required", "applied"]
  about: "accredited degree outcomes under AHEP"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "A degree is awarded when a student shows they have met the course outcomes and the provider's award regulations; an accredited degree also needs the outcomes AHEP sets and any discipline requirements of the institution, so students on accredited courses are required to meet these harder requirements until an accredited award is no longer possible, after which the standard regulations apply."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of an Engineering degree", "Partnership"] }
  span: { start: 40389, end: 40895 }
  source: "2.11 Engineering degree courses exist in a rapidly changing sector. Higher education providers need to therefore stay up to date with contemporary industry needs through active partnerships with industry. Engineering industry advisory boards provide an essential input into the design of Engineering courses. These boards can provide valuable insight into the knowledge, skills and experience that would be valuable in their industry and provide insight into sector innovation and contemporary skill needs."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: none
  appliesTo: "providers of engineering courses"
  addressee: provider
  verbs: ["stay", "provide"]
  about: "keeping current through industry partnership"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Engineering courses sit in a fast-changing sector, so providers need to keep current with industry through active partnerships; industry advisory boards are essential to course design, offering insight into valued knowledge, skills and experience and into sector innovation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of an Engineering degree", "Partnership"] }
  span: { start: 41876, end: 42282 }
  source: "2.14 There is a partnership between Engineering and the broader society that the sector serves. Partnerships with community groups impacted by engineering products and processes may help students to understand the needs of beneficiaries, as can taking human and community-centred approaches to design. Such approaches should explicitly consider EDI and ethical implications in serving the whole of society."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "community-centred design approaches"
  addressee: both
  verbs: ["understand", "consider"]
  about: "community-centred design with EDI and ethics"
  themes: [theme:edi]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Engineering is in partnership with the society it serves; working with communities affected by engineering, and human- and community-centred design, can help students understand beneficiaries' needs, and such approaches should explicitly take EDI and ethical consequences into account."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/2.20
  locator: { number: "2.20", headingPath: ["Distinctive features of an Engineering degree", "Monitoring and review"] }
  span: { start: 46625, end: 47089 }
  source: "2.20 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject. In particular, the periodic review of Engineering degrees should also draw in the expertise of industrial partners to ensure the currency of curriculum."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "periodic review of engineering degrees"
  addressee: provider
  verbs: ["use", "draw", "ensure"]
  about: "external and industrial input to periodic review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "External input is a core part of UK quality assurance: providers will use external reviewers in periodic review to test proposed changes and confirm threshold standards and suitable content, and periodic review of engineering degrees should also bring in industrial partners to keep the curriculum current."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/3.3
  locator: { number: "3.3", headingPath: ["Content design and delivery", "Content"] }
  span: { start: 49407, end: 49933 }
  source: "3.3 The practical component of any Engineering course is of particular significance as this distinguishes it from other applied sciences. It is not enough to be able to theorise how to solve a problem in an engineering context; the degree course needs to include opportunities for the learner to demonstrate their ability to make this work in practice. Thus, the practical components of an Engineering course can range from the build-and-test of a programming solution through to the build-and-test of a physical construction."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "needs to" read as must
  level: fheq:6
  appliesTo: "engineering courses and their students"
  addressee: both
  verbs: ["include", "demonstrate"]
  about: "showing practical engineering ability"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Practical work matters especially because it sets engineering apart from other applied sciences; knowing in theory how to solve a problem is not enough, so the course needs to let learners show they can make a solution work in practice, from building and testing software to physical construction."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/3.4
  locator: { number: "3.4", headingPath: ["Content design and delivery", "Content"] }
  span: { start: 49934, end: 50603 }
  source: "3.4 There is some flexibility within all Engineering degrees for higher education providers to develop specialist content and skills relevant to their local and institutional context. Higher education providers seeking accreditation should ensure that the learning outcomes are consistent with what is required by the relevant professional engineering institution and the Engineering Council. Engineering degrees have the flexibility to offer non- specialist content, from subjects beyond Engineering (language, humanities and so on) which can enhance a course of study, help students to gain interdisciplinary insights and offer more choice for course personalisation."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers seeking accreditation"
  addressee: provider
  verbs: ["ensure", "develop"]
  about: "specialist content and fit with accreditation"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "All engineering degrees leave providers room to add specialist content suited to their local and institutional setting; those seeking accreditation should make sure their outcomes match what the professional engineering institution and the Engineering Council require, and degrees can also include non-engineering subjects for breadth and choice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/3.7
  locator: { number: "3.7", headingPath: ["Content design and delivery", "Teaching and learning"] }
  span: { start: 51580, end: 51911 }
  source: "3.7 Curriculum design is informed by relevant examples of current developments, reflecting appropriate research, scholarship and industrial practice, and an understanding of the potential destination of graduates. Accredited degree courses must also satisf y the requirements of Accreditation of Higher Education Programmes (AHEP)."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "accredited courses"
  addressee: provider
  verbs: ["informed"]
  about: "current curriculum; AHEP for accredited courses"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Curriculum design draws on current developments in research, scholarship and industrial practice and on where graduates may go; accredited courses must also meet AHEP's requirements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/3.8
  locator: { number: "3.8", headingPath: ["Content design and delivery", "Teaching and learning"] }
  span: { start: 51912, end: 52492 }
  source: "3.8 For students on a bachelor’s degree course to achieve a satisfactory understanding of Engineering, the expectation is that they have significant exposure to hands-on laboratory work and substantial individual and group project work. The curriculum includes both design, development and research-led projects, which develop in graduates both independence of thought and the ability to work effectively in a team. Teaching and learning needs to be\n\n17\nplaced within the context of social, ethical, legal, environmentally sustainable and economic factors relevant to engineering."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "the expectation is" read as must
  level: fheq:6
  appliesTo: "bachelor's courses and their students"
  addressee: both
  verbs: ["achieve", "develop", "placed"]
  about: "lab work and projects on the bachelor's"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "For a satisfactory understanding of engineering, bachelor's students are expected to have extensive practical laboratory work and sizeable projects, alone and in groups, including design, development and research projects that build independent thought and teamwork; teaching and learning needs to be set in social, ethical, legal, environmentally sustainable and economic contexts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/3.10
  locator: { number: "3.10", headingPath: ["Content design and delivery", "Teaching and learning"] }
  span: { start: 53302, end: 53666 }
  source: "3.10 Teaching and learning for other master's qualifications (typically MSc degrees) depends to a large extent on the focus of the course, but may include increased specialisation, breadth or depth of material. There are expectations that master's students will be increasingly self-reliant and self-directing, particularly during the later stages of their course."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: ["include"]
  about: "growing self-reliance on the master's"
  themes: [none]
  domain: generic-skill
  award: ["postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Teaching on other master's courses, usually MSc, depends on the course's focus and may add specialism, breadth or depth; master's students are expected to become more self-reliant and self-directing, especially later in the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/3.11
  locator: { number: "3.11", headingPath: ["Content design and delivery", "Teaching and learning"] }
  span: { start: 53667, end: 54001 }
  source: "3.11 Master’s degrees often attract students who have not studied for their f irst degree within the UK higher education system. The learning outcomes they achieve in their f irst degree do not always align with those of students from the UK system and this difference should be taken into account in the design of individual courses."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "master's course design"
  addressee: provider
  verbs: ["taken"]
  about: "designing for varied prior learning"
  themes: [none]
  domain: none
  award: ["postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Many master's students took their first degree outside the UK system, and their earlier outcomes may not match UK graduates'; course design should allow for this."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/3.14
  locator: { number: "3.14", headingPath: ["Content design and delivery", "Assessment"] }
  span: { start: 54538, end: 54741 }
  source: "3.14 As stated in the Frameworks for HE qualifications of UK degree awarding bodies, assessment procedures should not allow for the award of a qualification when learning outcomes have not been achieved."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment procedures"
  addressee: provider
  verbs: ["allow"]
  about: "no award without achieved outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Following the qualifications frameworks, assessment procedures should not permit a qualification to be awarded where learning outcomes have not been met."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/3.14.b1
  locator: { number: "3.14.b1", headingPath: ["Content design and delivery", "Assessment"] }
  span: { start: 54744, end: 55127 }
  source: "All students graduating with Engineering degrees will be able to demonstrate that they have achieved the necessary output standards for the degree that they have been awarded. The higher education provider publishes course objectives and outcomes, and sets robust assessment standards and procedures to assess whether a graduate achieves the expected learning outcomes of the course."
  stem: "3.14"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: both
  verbs: ["demonstrate", "achieved", "publishes", "sets", "assess"]
  about: "showing the output standards of the award"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Every engineering graduate will be able to show they have reached the output standards for the degree they hold; the provider publishes course aims and outcomes and sets sound assessment standards and procedures to check them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/3.14.b2
  locator: { number: "3.14.b2", headingPath: ["Content design and delivery", "Assessment"] }
  span: { start: 55130, end: 55522 }
  source: "Assessment focuses on student learning and enables students to demonstrate their full range of abilities, both theoretical and practical. All assessments directly align to the learning outcomes and emphasise deep learning. The higher education provider offers a range of assessment methods that are accessible to all students and should also make reasonable adjustments for disabled students."
  stem: "3.14"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["offers", "make"]
  about: "accessible assessment and reasonable adjustments"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Assessment centres on learning, lets students show their full theoretical and practical ability, aligns with outcomes and favours deep learning; providers offer accessible assessment methods and should also adjust reasonably for disabled students."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/3.14.b3
  locator: { number: "3.14.b3", headingPath: ["Content design and delivery", "Assessment"] }
  span: { start: 55525, end: 55955 }
  source: "A diversity of innovative assessment methods is encouraged and assessments can be carried out in person or remotely using appropriate digital technology. Flexibility of assessment can improve accessibility to learning for a diverse community. Assessment design beyond traditional exams can allow students to showcase different strengths across the curriculum. Assessment methods in Engineering may include, but are not limited to:"
  stem: "3.14"
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["encouraged", "carried", "showcase"]
  about: "diverse and innovative assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "A variety of innovative assessment is encouraged, in person or remotely through digital technology; flexible assessment can widen access, and going beyond traditional exams lets students show different strengths, through methods such as exams, lab and project reports, case studies, literature reviews, dissertations, presentations, peer and self-assessment and work-integrated tasks."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/3.14.b13
  locator: { number: "3.14.b13", headingPath: ["Content design and delivery", "Assessment"] }
  span: { start: 56330, end: 56861 }
  source: "The aims and requirements for each assessment should be clearly defined through using transparent marking criteria, and relevant feedback should be provided for all students in a timely manner. Assessment should be designed to ensure the highest possible standards while also preventing opportunities for academic misconduct - such as plagiarism and contract cheating. Policies and procedures published by the higher education providers for safeguarding academic integrity should also be actively promoted and applied consistently."
  stem: "3.14"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["defined", "provided", "designed", "promoted", "applied"]
  about: "criteria, feedback and academic integrity"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Each assessment's aims and requirements should be made clear through transparent marking criteria, with timely and useful feedback for every student; assessment should aim at the highest standards while closing off academic misconduct such as plagiarism and contract cheating, and published integrity policies should be actively promoted and consistently applied."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/3.14.b14
  locator: { number: "3.14.b14", headingPath: ["Content design and delivery", "Assessment"] }
  span: { start: 56864, end: 57527 }
  source: "Students should be given opportunities to demonstrate their skills through collaborative group work in addition to individual assessments. The fair assessment of groupwork is fundamental to supporting an inclusive curriculum. Consideration should be given to assessing the ability to work in a group (not just the academic output), including student actions within the group environment that promotes inclusivity while recognising the needs of learners who have different learning abilities and styles. Another priority involves peer assessment, including individual self-reflection about the ability to work effectively in a group when meeting learning outcomes."
  stem: "3.14"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "assessment of group work"
  addressee: both
  verbs: ["given", "demonstrate", "assessing"]
  about: "fair assessment of group work"
  themes: [theme:edi]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Students should have chances to show their skills through group work as well as individual assessment; fair assessment of group work underpins an inclusive curriculum, so the ability to work in a group, including inclusive behaviour and regard for differing abilities and styles, should be assessed, not just the output, alongside peer assessment and individual reflection on teamwork."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/3.14.b15
  locator: { number: "3.14.b15", headingPath: ["Content design and delivery", "Assessment"] }
  span: { start: 57530, end: 57712 }
  source: "Authentic assessment, which will equip students for employment, is encouraged through considering communication methods, the assessment of technical skills, and cultural competences."
  stem: "3.14"
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "assessment design"
  addressee: both
  verbs: ["equip", "encouraged", "considering"]
  about: "authentic assessment for employment"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Authentic assessment, which prepares students for work, is encouraged by attending to how students communicate, how technical skills are assessed and cultural competence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/3.15
  locator: { number: "3.15", headingPath: ["Content design and delivery", "Assessment"] }
  span: { start: 57714, end: 58032 }
  source: "3.15 Accredited Engineering degrees are subject to strictly imposed limits on failure and marginal failure. These are more stringent than the standard credit recognition of most providers. Typically, students will have to pass most, or in some cases all, modules on the course in order to achieve an accredited degree."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "students on accredited degrees"
  addressee: learner
  verbs: ["pass", "achieve"]
  about: "strict limits on failure for accredited degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Accredited degrees impose strict limits on failure and marginal failure, tighter than most providers' usual credit rules; students will usually have to pass most, sometimes all, modules to gain an accredited degree."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.4
  locator: { number: "4.4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58878, end: 59441 }
  source: "4.4 The benchmark standards are defined relative to the appropriate FHEQ Level 6 or 7 (FQHEIS Level 10 or 11) specification and associated descriptors. As such, their application to an individual course is necessarily contextual. Many Engineering degrees are accredited by UK professional engineering institutions acting under license from the Engineering Council (see section 1 for more details). For degrees that are accredited, learning outcomes defined by the profession to support development of competences required for professional registration will apply."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "the standards and accredited degrees"
  addressee: provider
  verbs: ["defined", "apply"]
  about: "standards set against framework levels; accredited outcomes apply"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "The standards are set against the relevant FHEQ Level 6 or 7 (FQHEIS 10 or 11) descriptors, so applying them to a course depends on context; many degrees are accredited by institutions licensed by the Engineering Council, and for accredited degrees the profession's outcomes for registration competences will apply."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/4.5
  locator: { number: "4.5", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 59470, end: 59991 }
  source: "4.5 For the purposes of this Statement, the learning outcomes set out in the relevant edition of Accreditation of Higher Education Programmes (AHEP), published by the Engineering Council, should be interpreted as the minimum threshold standards for accredited courses. These learning outcomes should be read in the context of the generic statements of competence and commitment for Incorporated Engineer (IEng) and Chartered Engineer (CEng) in UK Standard for Professional Engineering Competence and Commitment (UK-SPEC)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "accredited courses"
  addressee: provider
  verbs: ["interpreted", "read"]
  about: "AHEP outcomes as the threshold for accredited courses"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "postgraduate taught master's"]
  gradeOf: none
  paraphrase: "For this text, the learning outcomes in the current edition of AHEP should be taken as the minimum threshold for accredited courses and read with the UK-SPEC statements of competence and commitment for Incorporated and Chartered Engineers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/engineering-2023/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Bachelor's degree with honours"] }
  span: { start: 61458, end: 61588 }
  source: "Knowledge and understanding: a coherent knowledge and understanding of their engineering discipline and its practical application."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "BEng with honours graduates at threshold"
  addressee: learner
  verbs: []
  about: "coherent discipline knowledge and its application"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown joined-up knowledge and understanding of their branch of engineering and how it is put into practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Bachelor's degree with honours"] }
  span: { start: 61591, end: 61781 }
  source: "Problem solving: the ability to identify complex engineering problems, select the appropriate tools and go on to create safe, secure and sustainable solutions designed to meet defined needs."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "BEng with honours graduates at threshold"
  addressee: learner
  verbs: ["identify", "select", "create"]
  about: "complex problems and safe, secure, sustainable solutions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown they can recognise complex engineering problems, choose fitting tools and go on to produce safe, secure and sustainable solutions that meet set needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Bachelor's degree with honours"] }
  span: { start: 61784, end: 61927 }
  source: "Analysis: the skill to select and apply quantitative and computational analysis techniques recognising the limitations of the methods employed."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "BEng with honours graduates at threshold"
  addressee: learner
  verbs: ["select", "apply", "recognising"]
  about: "quantitative and computational analysis and its limits"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the skill to choose and use quantitative and computational methods of analysis while knowing where those methods fall short."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Bachelor's degree with honours"] }
  span: { start: 61930, end: 62010 }
  source: "Delivery/skills/practice: creativity, innovation, teamworking and communication."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "BEng with honours graduates at threshold"
  addressee: learner
  verbs: []
  about: "creativity, innovation, teamwork and communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown creativity, innovation, teamwork and communication in carrying out engineering work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Bachelor's degree with honours"] }
  span: { start: 62013, end: 62145 }
  source: "Values and principles: an appreciation of professional and commercial engineering practice, ethics and global social responsibility."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "BEng with honours graduates at threshold"
  addressee: learner
  verbs: []
  about: "professional and commercial practice, ethics and global responsibility"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown that they value professional and commercial practice in engineering, ethics and social responsibility at a global scale."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.9
  locator: { number: "4.9", headingPath: ["Benchmark standards", "Bachelor's degree with honours"] }
  span: { start: 62173, end: 62437 }
  source: "4.9 Criteria for achievement above threshold level at 2:1 and 2:2 will be in line with the higher education provider's common or generic marking schemes for undergraduate courses and the sector-recognised standards that are in use in each of the nations of the UK."
  stem: none
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "BEng with honours graduates at the typical level"
  addressee: both
  verbs: []
  about: "typical level (2:1 and 2:2) set by marking schemes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Criteria for the typical level, upper and lower second-class, will follow each provider's own undergraduate marking scheme and the sector-recognised standards used in each UK nation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.10
  locator: { number: "4.10", headingPath: ["Benchmark standards", "Bachelor's degree with honours"] }
  span: { start: 62467, end: 62718 }
  source: "4.10 Criteria for excellent (1st class achievement) will be in line with the higher education provider's common or generic marking schemes for undergraduate courses and the sector- recognised standards that are in use in each of the nations of the UK."
  stem: none
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "BEng with honours graduates at the excellent level"
  addressee: both
  verbs: []
  about: "excellent level (first class) set by marking schemes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/engineering-2023/4.9, basis: inferred }
  paraphrase: "Criteria for the excellent level, first-class, will follow each provider's own undergraduate marking scheme and the sector-recognised standards used in each UK nation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.11.b1
  locator: { number: "4.11.b1", headingPath: ["Benchmark standards", "Integrated master's degree"] }
  span: { start: 63466, end: 63606 }
  source: "Knowledge and understanding: a broad and coherent knowledge and understanding of their engineering discipline and its practical application."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "MEng graduates at threshold"
  addressee: learner
  verbs: []
  about: "broad, coherent discipline knowledge and its application"
  themes: [none]
  domain: knowledge
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will have shown broad, joined-up knowledge and understanding of their branch of engineering and how it is put into practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.11.b2
  locator: { number: "4.11.b2", headingPath: ["Benchmark standards", "Integrated master's degree"] }
  span: { start: 63609, end: 63799 }
  source: "Problem solving: the ability to identify complex engineering problems, select the appropriate tools and go on to create safe, secure and sustainable solutions designed to meet defined needs."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "MEng graduates at threshold"
  addressee: learner
  verbs: ["identify", "select", "create"]
  about: "complex problems and safe, secure, sustainable solutions"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will have shown they can recognise complex engineering problems, choose fitting tools and go on to produce safe, secure and sustainable solutions that meet set needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.11.b3
  locator: { number: "4.11.b3", headingPath: ["Benchmark standards", "Integrated master's degree"] }
  span: { start: 63802, end: 63977 }
  source: "Analysis: the skill to select and apply quantitative and computational analysis techniques in the absence of complete data, discussing the limitations of the methods employed."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "MEng graduates at threshold"
  addressee: learner
  verbs: ["select", "apply", "discussing"]
  about: "analysis with incomplete data and its limits"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will have shown the skill to choose and use quantitative and computational methods of analysis when data are incomplete, and to discuss where those methods fall short."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.11.b4
  locator: { number: "4.11.b4", headingPath: ["Benchmark standards", "Integrated master's degree"] }
  span: { start: 63980, end: 64082 }
  source: "Delivery/skills/practice: creativity, innovation, effective teamworking, leadership and communication."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "MEng graduates at threshold"
  addressee: learner
  verbs: []
  about: "creativity, innovation, effective teamwork, leadership and communication"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will have shown creativity, innovation, effective teamwork, leadership and communication in carrying out engineering work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.11.b5
  locator: { number: "4.11.b5", headingPath: ["Benchmark standards", "Integrated master's degree"] }
  span: { start: 64085, end: 64217 }
  source: "Values and principles: an appreciation of professional and commercial engineering practice, ethics and global social responsibility."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "MEng graduates at threshold"
  addressee: learner
  verbs: []
  about: "professional and commercial practice, ethics and global responsibility"
  themes: [none]
  domain: understanding
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will have shown that they value professional and commercial practice in engineering, ethics and social responsibility at a global scale."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.12
  locator: { number: "4.12", headingPath: ["Benchmark standards", "Integrated master's degree"] }
  span: { start: 64246, end: 64432 }
  source: "4.12 Criteria for achievement above threshold level at 2:1 and 2:2 will be in line with the higher education provider's common or generic marking schemes for integrated master’s courses."
  stem: none
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "MEng graduates at the typical level"
  addressee: both
  verbs: []
  about: "typical level (2:1 and 2:2) set by marking schemes"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Criteria for the typical level, upper and lower second-class, will follow each provider's own marking scheme for integrated master's courses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.13
  locator: { number: "4.13", headingPath: ["Benchmark standards", "Integrated master's degree"] }
  span: { start: 64461, end: 64632 }
  source: "4.13 Criteria for excellent (1st class achievement) will be in line with the higher education provider's common or generic marking schemes for integrated master’s courses."
  stem: none
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:7
  appliesTo: "MEng graduates at the excellent level"
  addressee: both
  verbs: []
  about: "excellent level (first class) set by marking schemes"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: { statement: qaa/engineering-2023/4.12, basis: inferred }
  paraphrase: "Criteria for the excellent level, first-class, will follow each provider's own marking scheme for integrated master's courses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.14
  locator: { number: "4.14", headingPath: ["Benchmark standards", "Postgraduate master's degrees benchmark standards"] }
  span: { start: 64683, end: 64948 }
  source: "4.14 Students graduating with a postgraduate master’s degree in Engineering must demonstrate at least a threshold level of attainment across all relevant course outcome categories. Attainment at a threshold level usually maps onto that associated with a pass award."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "postgraduate taught master's graduates"
  addressee: learner
  verbs: ["demonstrate"]
  about: "threshold in every category for the MSc"
  themes: [none]
  domain: none
  award: ["postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Postgraduate master's graduates must show at least threshold attainment in every relevant outcome category, usually equivalent to a pass."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.15.b1
  locator: { number: "4.15.b1", headingPath: ["Benchmark standards", "Postgraduate master's degrees benchmark standards"] }
  span: { start: 65639, end: 65757 }
  source: "Knowledge and understanding: a coherent knowledge and understanding of their engineering discipline or specialisation."
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "taught MSc graduates at threshold"
  addressee: learner
  verbs: []
  about: "coherent knowledge of the discipline or specialism"
  themes: [none]
  domain: knowledge
  award: ["postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Will have shown joined-up knowledge and understanding of their branch of engineering or their specialism."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.15.b2
  locator: { number: "4.15.b2", headingPath: ["Benchmark standards", "Postgraduate master's degrees benchmark standards"] }
  span: { start: 65760, end: 65950 }
  source: "Problem-solving: the ability to identify complex engineering problems, select the appropriate tools and go on to create safe, secure and sustainable solutions designed to meet defined needs."
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "taught MSc graduates at threshold"
  addressee: learner
  verbs: ["identify", "select", "create"]
  about: "complex problems and safe, secure, sustainable solutions"
  themes: [none]
  domain: subject-skill
  award: ["postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Will have shown they can recognise complex engineering problems, choose fitting tools and go on to produce safe, secure and sustainable solutions that meet set needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.15.b3
  locator: { number: "4.15.b3", headingPath: ["Benchmark standards", "Postgraduate master's degrees benchmark standards"] }
  span: { start: 65953, end: 66128 }
  source: "Analysis: the skill to select and apply quantitative and computational analysis techniques in the absence of complete data, discussing the limitations of the methods employed."
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "taught MSc graduates at threshold"
  addressee: learner
  verbs: ["select", "apply", "discussing"]
  about: "analysis with incomplete data and its limits"
  themes: [none]
  domain: subject-skill
  award: ["postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Will have shown the skill to choose and use quantitative and computational methods of analysis when data are incomplete, and to discuss where those methods fall short."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.15.b4
  locator: { number: "4.15.b4", headingPath: ["Benchmark standards", "Postgraduate master's degrees benchmark standards"] }
  span: { start: 66135, end: 66247 }
  source: "Delivery/skills/practice: creativity, innovation, research, effective teamworking, leadership and communication."
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "taught MSc graduates at threshold"
  addressee: learner
  verbs: []
  about: "creativity, innovation, research, effective teamwork, leadership and communication"
  themes: [none]
  domain: generic-skill
  award: ["postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Will have shown creativity, innovation, research, effective teamwork, leadership and communication in carrying out engineering work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.15.b5
  locator: { number: "4.15.b5", headingPath: ["Benchmark standards", "Postgraduate master's degrees benchmark standards"] }
  span: { start: 66250, end: 66382 }
  source: "Values and principles: an appreciation of professional and commercial engineering practice, ethics and global social responsibility."
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "taught MSc graduates at threshold"
  addressee: learner
  verbs: []
  about: "professional and commercial practice, ethics and global responsibility"
  themes: [none]
  domain: understanding
  award: ["postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Will have shown that they value professional and commercial practice in engineering, ethics and social responsibility at a global scale."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.16
  locator: { number: "4.16", headingPath: ["Benchmark standards", "Postgraduate master's degrees benchmark standards"] }
  span: { start: 66405, end: 66571 }
  source: "4.16 Criteria for merit achievement above threshold level will be in line with the higher education provider's common or generic marking schemes for master’s courses."
  stem: none
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "taught MSc graduates at the typical level"
  addressee: both
  verbs: []
  about: "typical level (merit) set by marking schemes"
  themes: [none]
  domain: none
  award: ["postgraduate taught master's"]
  gradeOf: none
  paraphrase: "Criteria for merit, above threshold, will follow each provider's own marking scheme for master's courses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/engineering-2023/4.17
  locator: { number: "4.17", headingPath: ["Benchmark standards", "Postgraduate master's degrees benchmark standards"] }
  span: { start: 66602, end: 66758 }
  source: "4.17 Criteria for excellent level (distinction) will be in line with the higher education provider's common or generic marking schemes for master’s courses."
  stem: none
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:7
  appliesTo: "taught MSc graduates at the excellent level"
  addressee: both
  verbs: []
  about: "excellent level (distinction) set by marking schemes"
  themes: [none]
  domain: none
  award: ["postgraduate taught master's"]
  gradeOf: { statement: qaa/engineering-2023/4.16, basis: inferred }
  paraphrase: "Criteria for distinction will follow each provider's own marking scheme for master's courses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/engineering-2023/1.2
  forPractitioner: { text: "Prepare students to adapt to new and emerging challenges, since future engineers must be adaptable; use the UN Sustainable Development Goals and global challenges such as energy, infrastructure and cybersecurity as reference points, and expect the curriculum to keep changing.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "As a future engineer you must be ready to adapt to new challenges as they arise, from climate and sustainable development to cybersecurity, energy and transport.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a statement of what the profession must be: adaptable engineers, framed by the UN Sustainable Development Goals; it is a general expectation across all three awards, not an assessed outcome with its own threshold. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.2). Do not present it as a regulatory requirement or as a learning outcome in itself. Set it beside the sustainability paragraphs 1.19 and 1.20 and the decision-making descriptor at spine:6 (qaa/fheq-2024/4.15.b9.2)."
  author-agent-dialogue: "Raise it when a student or programme team asks why the curriculum keeps changing or how to prepare for an uncertain future. With a student, say in plain words that engineers need to adapt as problems change, and ask: which recent challenge in your field did your course not cover, and how would you get up to speed on it? Avoid reading the paragraph aloud or turning it into a graded outcome."
- statement: qaa/engineering-2023/1.5
  forPractitioner: { text: "State plainly in course information for applicants and employers what each bachelor's title means, honours or not, since everyday usage blurs the two; this is a should, aimed at the provider.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider to explain award titles; the student meets its effect in course information", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider duty (should) on how bachelor's titles are explained, not an outcome for students; it concerns the bachelor's degree with honours at fheq:6 and fqheis:10 and the non-honours bachelor's that meets that level only in part. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.5). Do not claim it fixes credit rules; set it beside the honours descriptor qaa/fheq-2024/4.15 and the qualification table in std:doc:qaa-fheq-2024-framework, S5."
  author-agent-dialogue: "Raise it with a programme team drafting award titles or applicant information, or with a student unsure whether their BEng carries honours. For staff, frame it as a clarity duty; for a student, explain in plain words what honours adds and ask: does your course page say whether the award is honours or ordinary? Avoid presenting this as something the student must do."
- statement: qaa/engineering-2023/1.10
  forPractitioner: { text: "Plan for students to meet engineering problems from the first stage and to progress, according to the course, either to broadly defined single-domain problems or to complex integrated systems with no obvious best answer; students will develop the knowledge, confidence and skill to handle them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will build your skill at solving engineering problems, starting early in your studies: either well-defined problems in one area, or increasingly complex problems that mix technical and social factors and have no single obvious answer.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) that runs across the BEng, MEng and MSc, with the type of problem depending on the course; it is not a rung on its own. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.10). Do not claim that it sets the level of problem a given course must reach. Set it beside the problem-solving threshold items 4.8.b2, 4.11.b2 and 4.15.b2, the honours descriptor on framing questions with incomplete data (qaa/fheq-2024/4.15.b7) and, for master's, qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Bring it up when a student asks why they meet open-ended problems so early, or when a team reviews where problem-solving is taught. With a student, explain that engineers grow by solving gradually harder problems, and ask: which problem this year had no single right answer, and how did you decide? Avoid implying that every course must reach the most complex kind."
- statement: qaa/engineering-2023/1.15
  forPractitioner: { text: "Embed equality, diversity and inclusion throughout the course, from team composition to the design process and its outcomes; in projects for developing or international contexts, make sure students understand the whole setting and bring in cultural and user perspectives. The curriculum should foster global perspectives and help students see historic western assumptions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should see equality, diversity and inclusion as part of all engineering work, from who is on the team to what you design; when you design for other countries or cultures, it is vital that you understand the setting and include the views of the people who will use the solution.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on the course and on engineering practice across all three awards, carrying the EDI theme; it is a design expectation, not a graded outcome. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.15). Do not claim it is a statutory duty; set it beside 2.4 and 2.14 on inclusive course design and the honours decision-making descriptor qaa/fheq-2024/4.15.b9.2 (spine:6)."
  author-agent-dialogue: "Raise it when a team plans projects for international or community users, or when a student asks why EDI appears in an engineering course. For staff, frame it as an expectation on curriculum and team practice; for a student, ask: whose needs did your last design leave out, and how would you find out? Avoid reading the paragraph aloud or treating it as a box to tick."
- statement: qaa/engineering-2023/1.16
  forPractitioner: { text: "Consider accessibility twice: in who can get into and through the course, and in what the curriculum teaches; flexible approaches to learning, teaching and assessment carry this out (3.13).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) applying to all three awards and carrying the accessibility theme; it is not a student outcome. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.16). Do not claim it states legal duties; set it beside 1.17, 1.18 and 3.13."
  author-agent-dialogue: "Use it with programme teams reviewing admissions, delivery or curriculum for accessibility. Frame it as two questions for staff: who cannot get into or through this course as designed, and where does the curriculum teach accessible design? Avoid putting it to a student as their duty."
- statement: qaa/engineering-2023/1.17
  forPractitioner: { text: "Teach accessibility as a routine part of the curriculum, especially in design work, so students produce solutions that remove barriers; design the curriculum itself to be accessible, meeting legal requirements as the floor.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on the curriculum for all three awards, with statutory requirements named as the minimum; the legal floor comes from law, not from this text. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.17). Do not claim it lists those requirements; set it beside 1.16, 1.18 and the inclusive-design item 2.3.b6."
  author-agent-dialogue: "Bring it up when staff design modules or briefs, especially design projects. Ask the team: where in the course do students design for disabled users, and does the module itself meet legal accessibility duties? Avoid treating it as a student requirement."
- statement: qaa/engineering-2023/1.18
  forPractitioner: { text: "Make accessibility a primary concern so disabled students can study engineering: remove barriers to engagement in labs and workshops and also in group work, placements and every other part of the course, including for hidden disabilities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) across all three awards; it concerns the course environment, not student outcomes. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.18). Do not claim it lists every legal duty; set it beside 1.17, 3.13 and 3.14.b2 on reasonable adjustments."
  author-agent-dialogue: "Raise it in reviews of labs, group work and placements. Ask staff: which parts of this course would a student with a hidden disability find hardest, and what have we changed? With a student who asks, explain plainly that support should reach every setting, but do not give them the duty."
- statement: qaa/engineering-2023/1.19
  forPractitioner: { text: "Equip students to weigh the environmental and social effects of engineering solutions, and draw on the UN Sustainable Development Goals in curriculum design, pedagogy and assessment (encouraged), including digital accessibility and resilience.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you become a more sustainable engineer, able to weigh up the environmental and social effects of what you design.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on courses for all three awards, carrying the sustainability (ESD) theme, with a student capability attached: judging environmental and societal impact. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.19). Do not claim the SDGs are mandated; the issuer encourages them. Set it beside 1.20, 2.3.b9 and the threshold items 4.8.b2 and 4.8.b5, with spine:6 (qaa/fheq-2024/4.15.b7)."
  author-agent-dialogue: "Raise it when a student or team discusses sustainability in design work. For a student, ask: how did you weigh the environmental and social effects of your last design, and what would you trade off? Avoid presenting the SDGs as a required checklist."
- statement: qaa/engineering-2023/1.21
  forPractitioner: { text: "Teach students to work to the profession's ethical principles and assess their grasp of engineering's ethical issues and their ability to make and justify ethical judgements; the Engineering Ethics Toolkit offers case studies for embedding this.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should learn to work by the profession's ethical principles, such as honesty, integrity and respect for life and the environment, and be able to make ethical judgements and explain why you made them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a should on engineers in training at all three awards, naming the joint Engineering Council and Royal Academy of Engineering statement of ethical principles; it is a professional expectation, not this text's own code. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.21). Do not claim the toolkit is required; set it beside the threshold values items 4.8.b5, 4.11.b5 and 4.15.b5 and the honours judgement descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student meets an ethical dilemma in a project or a team plans where ethics is taught and assessed. Ask a student: what was the hardest ethical choice in your project, and how would you justify it to a client? Avoid lecturing from the principles list; let the person reason it out."
- statement: qaa/engineering-2023/1.22
  forPractitioner: { text: "Prepare students for the everyday responsibility of protecting others and themselves: teach the relevant legal frameworks in detail and build skill in hazard analysis and mitigation, for new and legacy solutions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Engineers carry everyday responsibility for keeping people safe, so you need a detailed understanding of the safety laws that apply and the skills to analyse and reduce hazards.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a descriptive expectation: the issuer says engineers need this understanding and skill, using 'need' and 'responsibility' rather than must or should, so its force is recorded as describes. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.22). Do not present it as a regulatory requirement; set it beside the safety paragraphs 1.23 and 1.24 and the threshold problem-solving items (safe solutions) 4.8.b2, 4.11.b2 and 4.15.b2."
  author-agent-dialogue: "Bring it up when a student does hazardous practical work or a design with safety risks. Ask: which hazards did you identify, and which law or standard applies? Avoid overstating it as a rule the student will be marked against on its own."
- statement: qaa/engineering-2023/1.23
  forPractitioner: { text: "Support students throughout the course to take a holistic view of safety: human behaviour, risk monitoring and management, and specifying and testing safety qualities; make sure they understand the new threats that automated and autonomous systems bring.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should develop a rounded approach to safety, understanding how people behave, how risks are monitored and managed, and the new threats that come with automated and autonomous systems.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on courses and students across all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.23). Do not claim it prescribes a safety module; set it beside 1.22, 1.24 and the honours descriptor on decisions in complex and unpredictable contexts (qaa/fheq-2024/4.15.b9.2)."
  author-agent-dialogue: "Raise it when students work on automated or autonomous systems or a team maps safety across the curriculum. Ask a student: how could a person misuse or misread your system, and how would you test for it? Avoid turning it into a list of regulations to memorise."
- statement: qaa/engineering-2023/1.24
  forPractitioner: { text: "Teach design so that safety risks are explicitly included as non-functional system qualities (reliability, resilience, performance, usability), with attention to human behaviour and changing risk; failing to meet them can mean system failure and legal breach.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "When you design a system, you must build in safety qualities such as reliability, resilience, performance and usability, and think about how people will really use it.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a must on engineering design approaches, carried into teaching for all three awards; it concerns what designs must include, not a separate graded rung. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.24). Do not claim the issuer imposes the legal duties it mentions; set it beside 1.23 and the threshold problem-solving items 4.8.b2, 4.11.b2 and 4.15.b2."
  author-agent-dialogue: "Bring it up in design reviews and project supervision. Ask a student: which non-functional qualities did your design specify, and how did you test them? Avoid reciting the paragraph; use the four qualities as prompts."
- statement: qaa/engineering-2023/1.26
  forPractitioner: { text: "Graduates will be able to analyse critically the security consequences of their design decisions and collaborate to build threat-resistant systems, covering physical, human, process and technological aspects.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand what security means in engineering, be able to judge how your own design choices affect it and work with others to make systems hard to attack.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected capability, stated as what engineers are able to do, across all three awards within the security section. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.26). Do not claim it is a threshold item; set it beside 1.27, 1.28, the threshold problem-solving items (secure solutions) 4.8.b2, 4.11.b2 and 4.15.b2, and the honours evaluation descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student's design handles data, networks or physical access. Ask: who might want to attack this, and which of your design choices makes it easier or harder? Avoid presenting security as only a software matter."
- statement: qaa/engineering-2023/1.27
  forPractitioner: { text: "Develop students' contextual knowledge of their own branch so they will be able to resolve security problems in legacy systems as well as new ones, working with incomplete data and making design changes that improve things.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will learn enough about your own branch of engineering to fix security problems in existing systems as well as new ones, even when you do not have all the data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected capability (engineers are able to) for all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.27). Do not claim it sets a level of its own; set it beside 1.26, the MEng and MSc analysis items with incomplete data (4.11.b3, 4.15.b3) and, for master's, qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Bring it up when a student works on an existing system or a refurbishment project. Ask: what do you not know about this system, and how would you still make it safer? Avoid implying they must redesign from scratch."
- statement: qaa/engineering-2023/1.28
  forPractitioner: { text: "Teach students to protect sensitive data (personal, defence, commercial), the legal frameworks that govern it, and the ethics and law of sharing information, so they will be able to make informed choices about secure communication.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know how to protect sensitive data, such as personal or commercial information, understand the laws that apply and make sound choices about sharing information securely.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected capability (engineers have the skills and can decide) for all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.28). Do not claim it names specific legislation; set it beside 1.26, 1.27 and the threshold values items 4.8.b5, 4.11.b5 and 4.15.b5."
  author-agent-dialogue: "Raise it when a project handles personal, defence or commercial data. Ask a student: who could see this data, and what law or agreement governs sharing it? Avoid giving legal advice; point to the course's own guidance."
- statement: qaa/engineering-2023/1.31
  forPractitioner: { text: "Keep supporting students while they are on formal industrial placements, so the placement benefits their learning and not only their finances.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the institution to support placement students; the student receives the support", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider duty (should) for all three awards, carried by the industry and entrepreneurship theme. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.31). Do not claim placements are required; set it beside 1.30 and the partnership paragraphs 2.12 and 2.13."
  author-agent-dialogue: "Raise it with a team planning placement support, or when a student on placement says they feel cut off. Frame it for staff as a continuing support duty and ask: how often does the placement student hear from the course, and about what? Do not hand the duty to the student."
- statement: qaa/engineering-2023/1.32
  forPractitioner: { text: "If the course is to count towards professional registration, it must meet the profession's requirements and be re-accredited periodically (usually at most every five years); consult the Engineering Council's AHEP.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course for accreditation; the student-facing effect is in 2.10 and 3.15", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a must that applies only to courses seeking to contribute to professional registration, at any of the three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.32). Do not claim every engineering course must be accredited (1.34 says otherwise); set it beside 1.33, 3.7 and 4.5, and name AHEP as the Engineering Council's document, not this one."
  author-agent-dialogue: "Use it with programme teams deciding whether to seek or renew accreditation. Ask: which registration category is the course aiming at, and when is the next accreditation visit? If a student asks, explain plainly what accreditation means for registration, but do not give them the course's duty."
- statement: qaa/engineering-2023/1.33
  forPractitioner: { text: "For accredited courses, expect peer review of assessments, facilities and staffing against the prescribed outcomes at minimum threshold, and meet the stricter progression requirements accreditation imposes.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on accredited courses; the student meets its effect in progression rules (2.10, 3.15)", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a description of accreditation that carries a must for accredited courses (they have to meet strict progression requirements), at any of the three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 1.33). Do not claim the issuer accredits; set it beside 1.32, 2.22, 3.15 and 4.5."
  author-agent-dialogue: "Raise it when a team prepares for an accreditation visit or sets progression rules. Ask: where do we evidence that every graduate meets each prescribed outcome? Avoid presenting the accreditation process to students as their responsibility."
- statement: qaa/engineering-2023/2.1
  forPractitioner: { text: "Design the degree so that graduates leave with integrated knowledge, skill and judgement that will let them begin professional engineering careers, involving industry in design and delivery.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your degree is designed so that you will leave with the knowledge, skills and judgement to start a professional career in engineering.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the expected end point of all three awards (will), stated as a design aim. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.1). Do not claim it guarantees employment; set it beside the threshold rungs 4.8, 4.11 and 4.15 and the honours employability descriptor qaa/fheq-2024/4.15.b9.3 (spine:6)."
  author-agent-dialogue: "Raise it when a student asks what the degree is for or a team checks its aims. Ask a student: which parts of your course feel closest to professional work, and which feel furthest? Avoid promising a job."
- statement: qaa/engineering-2023/2.2
  forPractitioner: { text: "Build systems thinking into the course and make sure the curriculum supports students in analysing and mitigating system risks, especially to safety and security, across economic, legal, social, environmental and ethical dimensions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you think about whole systems and analyse and reduce the risks they face, especially to safety and security, so you can design things that do not fail and treat people fairly.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on the curriculum, with systems thinking as the expected graduate capability, for all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.2). Do not claim it fixes content; set it beside 1.23, 1.24, 1.26 and the threshold problem-solving items 4.8.b2, 4.11.b2 and 4.15.b2."
  author-agent-dialogue: "Bring it up when a student's design stops at the technical boundary. Ask: who else is affected if this system fails, and what risk would you reduce first? Avoid listing all the dimensions at once."
- statement: qaa/engineering-2023/2.3.b1
  forPractitioner: { text: "Give students substantial hands-on laboratory and project work so they develop rounded competence, understand concepts through experience and learn the practical logistics and health and safety of engineering.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect a lot of hands-on lab and project work, which helps you understand ideas and learn how to work safely and practically.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a course design expectation phrased as 'the expectation is that', held here as describes, not a must; it applies to all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.3). Do not claim a minimum number of lab hours; set it beside 3.3 and 3.8 and Annex D's practical-skills cell qaa/fheq-2024/annex-d/practical/r2/3rd."
  author-agent-dialogue: "Raise it when a team reviews lab provision or a student asks why practicals matter. Ask a student: what did you learn in the lab that you could not have learned from notes? Avoid presenting it as a fixed requirement."
- statement: qaa/engineering-2023/2.3.b2
  forPractitioner: { text: "Provide enough chances for students to build the maths and science their discipline or specialism calls for.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course to offer opportunities; the student takes them up", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider expectation (should) for all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.3). Do not claim it sets a maths syllabus; set it beside the knowledge threshold items 4.8.b1, 4.11.b1 and 4.15.b1 and the honours knowledge descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a team reviews maths support or where students struggle with analysis. Ask staff: where do students practise the maths their discipline uses, and who falls behind? Avoid telling a student it is their duty."
- statement: qaa/engineering-2023/2.3.b3
  forPractitioner: { text: "Offer plenty of opportunities across the curriculum for students to gain and extend digital skills that meet society's needs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the curriculum to offer opportunities; the student takes them up", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on the curriculum, for all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.3). Do not claim it names particular software; set it beside the analysis threshold items (computational techniques) 4.8.b3, 4.11.b3 and 4.15.b3, and Annex D's digital literacy cell qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a team maps digital skills or a student asks which tools they will learn. Ask staff: which digital skills will graduates use in their first job, and where are they taught? Avoid giving it to the student as a duty."
- statement: qaa/engineering-2023/2.3.b4
  forPractitioner: { text: "Balance individual and facilitated group projects to build self-directed learning, teamwork and leadership; at higher levels, students will be expected to work more autonomously and need less facilitation in groups.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As you move up through the levels of your course, you will be expected to learn more independently and to need less help when working in groups.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation on students at higher levels (the issuer's 'are expected to', held here as will), applying above all at fheq:7 and fqheis:11 for the MEng and MSc. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.3). Do not claim it sets a level-6 requirement; set it beside 3.10 and the master's autonomy descriptor qaa/fheq-2024/4.17.b6 (spine:7)."
  author-agent-dialogue: "Raise it when a student moves into a higher level and finds less guidance in group work. Ask: what did you decide alone this term that a tutor decided for you last year? Avoid treating growing autonomy as the minimum at the first level."
- statement: qaa/engineering-2023/2.3.b6
  forPractitioner: { text: "Build inclusive and accessible design into design and research projects, and develop students' ability to balance economic, social and environmental needs with knowledge of their professional responsibilities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "In your projects you should learn to design inclusively and accessibly, balance economic, social and environmental needs, and understand your professional responsibilities as an engineer.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on projects and on students, for all three awards, carrying the EDI, accessibility and sustainability themes. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.3). Do not claim it prescribes project types; set it beside 1.17, 1.19 and the threshold values items 4.8.b5, 4.11.b5 and 4.15.b5."
  author-agent-dialogue: "Bring it up when a student scopes a design or research project. Ask: who would struggle to use what you are designing, and which economic, social or environmental need did you weigh least? Avoid reading the full list of needs aloud."
- statement: qaa/engineering-2023/2.3.b7
  forPractitioner: { text: "Develop students' ability to manage compromise under uncertainty; at higher levels, students will be expected to handle more complex scenarios with conflicting or missing information and reach reasoned, justified decisions, ideally across modules and not only in design.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will learn to handle trade-offs and uncertainty; as you progress you will be expected to deal with harder problems where information is missing or conflicting, and make decisions you can justify.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (held as will from 'are expected to be able to') that grows with level, strongest at fheq:7 and fqheis:11 for the MEng and MSc. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.3). Do not claim it is a threshold item on its own; set it beside the MEng and MSc analysis items 4.11.b3 and 4.15.b3 and the master's descriptor on judgement without complete data (qaa/fheq-2024/4.17.b5)."
  author-agent-dialogue: "Raise it when a student is stuck because the brief has gaps or conflicts. Ask: what are you assuming to fill the gaps, and how would you defend that decision? Avoid presenting the master's-level expectation as the minimum for a first-year student."
- statement: qaa/engineering-2023/2.3.b9
  forPractitioner: { text: "Teach lifecycle and environmental impact assessment alongside low-carbon and clean technologies, so students can judge the effects of resource exploitation.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to judge the environmental impact of engineering decisions over their whole life, including the effects of using up natural resources.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on students for all three awards, carrying the sustainability (ESD) theme. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.3). Do not claim it requires a named method such as life-cycle assessment; set it beside 1.19, 1.20 and the threshold problem-solving items (sustainable solutions) 4.8.b2, 4.11.b2 and 4.15.b2."
  author-agent-dialogue: "Raise it when a student chooses materials, energy sources or end-of-life options. Ask: where does this material come from, and what happens to it when the product is finished? Avoid moralising; keep it to evidence."
- statement: qaa/engineering-2023/2.3.b10
  forPractitioner: { text: "Develop students' cultural competence for international teams and a global sector, drawing on the mix of UK and overseas students on the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should build the cultural awareness and skills to work well in international teams and anywhere in the world.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on students for all three awards, a generic skill read at spine:6. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.3). Do not claim it is assessed separately; set it beside 1.15, 3.14.b15 and the honours communication descriptor qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise it when a student works in a mixed international team or plans to work abroad. Ask: what surprised you about how your teammates from other countries work, and how did you adapt? Avoid stereotyping any group."
- statement: qaa/engineering-2023/2.4
  forPractitioner: { text: "Nurture an inclusive culture through student-centred course design that treats difference as a strength, design for belonging and equitable experience with accommodations, opportunities to learn about EDI including equity and justice, and EDI elements that support collaboration and reflection; keep re-evaluating it with evidence.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course culture; the student meets its effect", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a provider requirement ('requires') for an inclusive course culture across all three awards, carrying the EDI theme; the four measures are listed as ways to promote it, not as separate rules. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.4). Do not claim it is a statutory duty; set it beside 1.14, 1.15, 3.6 and 3.14.b14."
  author-agent-dialogue: "Raise it in course design or review meetings and after student feedback about belonging. Ask the team: which students feel they do not belong here, and what evidence tells us? Avoid putting the duty on students."
- statement: qaa/engineering-2023/2.5
  forPractitioner: { text: "Plan each level of the bachelor's degree so that it builds knowledge, expertise and experience towards the threshold subject-specific and generic skills; students will progress under institutional rules, and a graduate with a second or better would be expected to be ready for postgraduate study.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As you move through your degree, each year will build your knowledge, skills and experience towards the standard you need to graduate; with a second-class degree or better you would normally be ready for postgraduate study, though each university sets its own entry rules.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected progression pattern (will) for the bachelor's degree with honours at fheq:6 and fqheis:10. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.5). Do not claim it sets postgraduate entry rules; set it beside 2.7, the threshold rung 4.8 and the honours descriptor qaa/fheq-2024/4.15 with spine:6."
  author-agent-dialogue: "Raise it when a student asks how each year builds or whether they can go on to postgraduate study. Ask: what can you do now that you could not do at the start of last year? Avoid promising admission; entry rules belong to each institution."
- statement: qaa/engineering-2023/2.7
  forPractitioner: { text: "Set progression requirements for the MEng (often stricter than for the BEng), plan each year to build towards the threshold-level skills, and provide a transfer route to the matching bachelor's for students who do not meet them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On an integrated master's course you will move up year by year, building towards the standard you need to graduate; the rules for moving on are often stricter than on a bachelor's, and if you do not meet them you may transfer to the matching bachelor's degree.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected progression pattern (will) for the integrated master's at fheq:7 and fqheis:11. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.7). Do not claim a fixed progression mark; set it beside 1.6, 2.5, the threshold rung 4.11 and the master's descriptor qaa/fheq-2024/4.17 with spine:7."
  author-agent-dialogue: "Raise it when an MEng student worries about progression or transfer. Ask: do you know the progression rule for your next year, and what would transfer to the bachelor's mean for you? Avoid stating the rule yourself; send them to their course regulations."
- statement: qaa/engineering-2023/2.9
  forPractitioner: { text: "In a general or multidisciplinary honours degree, make sure students will achieve the core engineering subject and generic skills, then add the skills of the other subjects and use the overlap for interdisciplinary study.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a general or joint engineering degree you will gain the core engineering skills plus skills from your other subject, with chances to work across both.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) for general and multidisciplinary honours degrees at fheq:6. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.9). Do not claim joint degrees cover the full range of single-honours content; set it beside 1.7 and the threshold rung 4.8."
  author-agent-dialogue: "Raise it with joint-honours students or teams designing such courses. Ask a student: which core engineering skills does your course cover, and what does your other subject add? Avoid suggesting a joint degree is a lesser award."
- statement: qaa/engineering-2023/2.10
  forPractitioner: { text: "On an accredited course, apply AHEP's learning outcomes and the institution's extra requirements on top of the standard regulations, and switch to the standard regulations only once an accredited award is no longer possible for the student.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If your course is accredited, you must meet the extra, more demanding requirements set by the professional body as well as the usual ones; if you can no longer achieve an accredited degree, the usual university rules apply instead.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a must on students registered on accredited courses (they are required to meet AHEP's requirements), at any of the three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.10). Do not claim AHEP applies to non-accredited courses; set it beside 1.33, 3.15 and 4.5, naming AHEP as the Engineering Council's document."
  author-agent-dialogue: "Raise it when a student on an accredited course asks why their rules differ from other courses, or fails a module. Ask: do you know which modules must be passed for the accredited degree, and what happens if one is not? Avoid stating the professional body's rules from memory."
- statement: qaa/engineering-2023/2.11
  forPractitioner: { text: "Keep the course current through active industry partnerships, using an industrial advisory board to advise on design, contemporary skill needs and sector innovation.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a provider expectation phrased with 'need to', held here as describes, for all three awards and carried by the industry and entrepreneurship theme. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.11). Do not claim an advisory board is mandatory; set it beside 1.30, 2.12, 2.13 and 2.20."
  author-agent-dialogue: "Raise it when a team reviews currency or plans an advisory board meeting. Ask: when did industry last change something in this course, and what? Avoid presenting it to students as their responsibility."
- statement: qaa/engineering-2023/2.14
  forPractitioner: { text: "Use partnerships with affected community groups and human- and community-centred design to help students understand beneficiaries' needs, and make sure these approaches explicitly address EDI and ethics.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "When you design for a community, you should work with the people affected and think explicitly about fairness, inclusion and ethics.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on community-centred design approaches, for all three awards, carrying the EDI theme. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.14). Do not claim community partnerships are required; set it beside 1.13, 1.15 and 2.4."
  author-agent-dialogue: "Raise it when a student designs for a community or public client. Ask: who in that community have you spoken to, and who might be harmed or left out? Avoid treating consultation as a formality."
- statement: qaa/engineering-2023/2.20
  forPractitioner: { text: "In periodic review, use external reviewers to check threshold standards and content, and also draw on industrial partners so the curriculum stays current.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in course review", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation: external reviewers (will) and industrial partners (should) in periodic review, for all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 2.20). Do not claim it fixes the review cycle; set it beside 2.11, 2.19 and 2.21."
  author-agent-dialogue: "Raise it when a team plans a periodic review. Ask: which industrial partners will join the review, and what will we ask them? Avoid involving students as if the duty were theirs."
- statement: qaa/engineering-2023/3.3
  forPractitioner: { text: "Include opportunities for students to show they can make solutions work in practice, from build-and-test programming to build-and-test of physical constructions; theory alone is not enough.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course needs to give you chances to show that you can make engineering solutions work in practice, not just explain them in theory, whether that is software or a physical build.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a course expectation phrased with 'needs to', held here as describes, for all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.3). Do not claim it requires physical lab work in every discipline (software build-and-test counts); set it beside 2.3.b1, 3.8, the delivery and practice threshold items 4.8.b4, 4.11.b4 and 4.15.b4, and Annex D's practical cell qaa/fheq-2024/annex-d/practical/r2/3rd."
  author-agent-dialogue: "Raise it when a student's work stays theoretical or a team plans assessment of practice. Ask: where in your course did you build and test something, and what failed first? Avoid implying only hardware counts."
- statement: qaa/engineering-2023/3.4
  forPractitioner: { text: "If seeking accreditation, check the learning outcomes against what the accrediting institution and the Engineering Council require; use the remaining flexibility for specialist and non-specialist content.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider seeking accreditation", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on providers seeking accreditation, for all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.4). Do not claim it limits specialist content; set it beside 1.32, 3.7 and 4.5."
  author-agent-dialogue: "Raise it when a team adds specialist or non-engineering modules to an accredited course. Ask: does this change still map to every outcome the accrediting institution requires? Avoid presenting it to students."
- statement: qaa/engineering-2023/3.7
  forPractitioner: { text: "Inform the curriculum with current research, scholarship, industrial practice and graduate destinations; for accredited courses, meet AHEP's requirements as well.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on accredited courses", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a must on accredited courses only (they must satisfy AHEP), for all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.7). Do not claim AHEP binds non-accredited courses; set it beside 1.32, 2.10 and 4.5."
  author-agent-dialogue: "Raise it with teams revising an accredited curriculum. Ask: which AHEP outcomes does this module evidence? Avoid giving the duty to students."
- statement: qaa/engineering-2023/3.8
  forPractitioner: { text: "On the bachelor's degree, give substantial hands-on lab work and individual and group projects (design, development and research) that develop independent thinking and effective teamwork, and set teaching in its social, ethical, legal, sustainable and economic context.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "On a bachelor's course you can expect plenty of hands-on lab work and individual and group projects that build your independent thinking and teamwork, set in their social, ethical, legal, environmental and economic context.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a course expectation for the bachelor's degree with honours ('the expectation is that'; 'needs to'), held here as describes, at fheq:6. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.8). Do not claim minimum hours; set it beside 2.3.b1, 3.3, 3.9 and the delivery and practice threshold item 4.8.b4, with qaa/fheq-2024/4.15.b6 on initiating and carrying out projects."
  author-agent-dialogue: "Raise it when a bachelor's team reviews the balance of lab and project work. Ask a student: which project made you think most independently, and what did teamwork add? Avoid treating it as a fixed rule."
- statement: qaa/engineering-2023/3.10
  forPractitioner: { text: "Shape MSc teaching around the course's focus, and plan for students who will become steadily more self-reliant and self-directed, especially in the later stages.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a taught master's course you will be expected to become more and more self-reliant and to direct your own learning, especially towards the end.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation on master's students (will) for the postgraduate taught master's at fheq:7 and fqheis:11, a generic skill. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.10). Do not claim it applies at fheq:6; set it beside 2.3.b4 and the master's autonomy descriptor qaa/fheq-2024/4.17.b6 (spine:7)."
  author-agent-dialogue: "Raise it when an MSc student expects close direction late in the course. Ask: which decisions about your project are you making alone now? Avoid presenting full self-direction as the starting point."
- statement: qaa/engineering-2023/3.11
  forPractitioner: { text: "Design master's courses with students' varied prior learning in mind, since outcomes from first degrees outside the UK may not match UK ones.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) for master's courses at fheq:7. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.11). Do not claim international students are less prepared; set it beside 3.10 and 2.3.b10."
  author-agent-dialogue: "Raise it with MSc teams planning induction or early modules. Ask: what do we assume students already know, and how do we check it? Avoid singling out students by background."
- statement: qaa/engineering-2023/3.14
  forPractitioner: { text: "Make sure assessment procedures cannot lead to an award when the learning outcomes have not been achieved.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment procedures", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on assessment procedures, restating the qualifications frameworks, for all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.14), and point to std:doc:qaa-fheq-2024-framework as the source it restates. Do not claim it is new regulation; set it beside 3.14.b1 and the threshold rungs 4.8, 4.11 and 4.15."
  author-agent-dialogue: "Raise it when a team designs compensation or condonement rules. Ask: could a student under these rules graduate without meeting an outcome? Avoid presenting it to students as their duty."
- statement: qaa/engineering-2023/3.14.b1
  forPractitioner: { text: "Publish course objectives and outcomes and set robust assessment standards and procedures so that every graduate will be able to show they have met the output standards for their award.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "When you graduate, you will be able to show that you have met the standards for your degree; your course publishes its outcomes and assesses you against them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) for every graduate of the three awards, with a provider duty to publish outcomes and assess robustly. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.14). Do not claim it defines the standards; set it beside 3.14 (the stem) and the threshold rungs 4.8, 4.11 and 4.15."
  author-agent-dialogue: "Raise it when a student asks how they will know they have met the standard. Ask: have you read your course's published outcomes, and which one feels least evidenced so far? Avoid reading outcome lists aloud."
- statement: qaa/engineering-2023/3.14.b2
  forPractitioner: { text: "Offer assessment methods accessible to all students and make reasonable adjustments for disabled students; align every assessment to outcomes and let students show theoretical and practical abilities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student receives the adjustments", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on reasonable adjustments, beside plain-present norms on alignment and accessibility, for all three awards; it carries the accessibility theme. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.14). Do not claim it states the legal duty in full; set it beside 1.18 and 3.13."
  author-agent-dialogue: "Raise it with a team reviewing assessment design, or when a disabled student asks about adjustments. For staff ask: which assessment would a student with a hidden disability find hardest to access? Point a student to the support service; do not make it their duty."
- statement: qaa/engineering-2023/3.14.b3
  forPractitioner: { text: "Use a diverse mix of innovative assessments, on site or remote, going beyond traditional exams so students can show varied strengths; the issuer encourages this rather than requiring it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: guidance to those who design assessment", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as encouragement to assessment designers ('is encouraged'), held here as describes and not a requirement, for all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.14). Do not claim the list of methods is complete or compulsory; set it beside 3.13 and 3.14.b15."
  author-agent-dialogue: "Raise it when a team relies heavily on closed exams. Ask: which strengths can no student currently show in this module's assessment? Avoid presenting the listed methods as a checklist."
- statement: qaa/engineering-2023/3.14.b13
  forPractitioner: { text: "Define each assessment's aims and requirements through transparent criteria, give all students timely feedback, design out plagiarism and contract cheating, and promote and apply integrity policies consistently.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design; the student meets its effect in criteria and feedback", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a set of provider expectations (should) on criteria, feedback and integrity, for all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.14). Do not claim it fixes a feedback turnaround; set it beside 3.14.b2 and the reference assessment criteria std:ref:uk-assesscriteria."
  author-agent-dialogue: "Raise it when a team writes marking criteria or integrity guidance, or a student complains about unclear criteria. Ask staff: could a student predict their mark from these criteria? Avoid giving the duty to students."
- statement: qaa/engineering-2023/3.14.b14
  forPractitioner: { text: "Assess group work fairly: give students opportunities to show their skills in groups, assess how they work in the group (including inclusive behaviour) as well as the output, and use peer assessment and individual reflection.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should get chances to show your skills in group work as well as alone, and expect to be assessed on how you work with others and to reflect on your own part.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on assessment design, with teamwork as the generic skill assessed, for all three awards at spine:6 and above; it carries the EDI theme. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.14). Do not claim group marks must be split in a set way; set it beside 2.4, the delivery and practice threshold items 4.8.b4, 4.11.b4 and 4.15.b4, and Annex D's group-work cell qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student is worried about a group mark or a team designs group assessment. Ask a student: what did you contribute, and how did you help the group include everyone? Avoid making peer assessment sound like blame."
- statement: qaa/engineering-2023/3.14.b15
  forPractitioner: { text: "Use authentic assessment that reflects workplace communication, technical skills and cultural competence; the issuer encourages this.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Some of your assessments may look like real engineering work, testing how you communicate, your technical skills and how you work across cultures.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as encouragement ('is encouraged'), held here as describes, for all three awards, carried by the industry, employability and enterprise theme. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.14). Do not claim authentic assessment is required; set it beside 2.3.b10, 3.12 and the honours employment descriptor qaa/fheq-2024/4.15.b9.3."
  author-agent-dialogue: "Raise it when a team redesigns assessment for employability. Ask: what would a new graduate engineer actually produce at work, and does any assessment look like it? Avoid presenting it as a rule."
- statement: qaa/engineering-2023/3.15
  forPractitioner: { text: "On accredited degrees, apply the stricter limits on failure and marginal failure; students will typically need to pass most or all modules for the accredited award.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On an accredited course you will usually have to pass most, and sometimes all, of your modules to get the accredited degree; the rules are stricter than on many other courses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected condition (will have to) for students on accredited courses at any of the three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 3.15). Do not claim exact limits, which belong to AHEP and each institution; set it beside 1.33 and 2.10."
  author-agent-dialogue: "Raise it at induction on accredited courses or when a student fails a module. Ask: do you know which modules you must pass for the accredited degree? Avoid quoting limits you have not checked in the course regulations."
- statement: qaa/engineering-2023/4.4
  forPractitioner: { text: "Read the standards against the FHEQ Level 6 or 7 descriptor for the award and apply them in context; for accredited degrees, the profession's learning outcomes will apply as well.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a statement for course designers on how the standards apply", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the issuer's statement of how its standards relate to the frameworks: defined against fheq:6 and fheq:7 (fqheis:10 and fqheis:11), with the profession's outcomes applying (will) to accredited degrees. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.4). Do not claim the standards replace the frameworks; set it beside qaa/fheq-2024/4.15, qaa/fheq-2024/4.17, qaa/fqheis-2024/4.16 and 4.5."
  author-agent-dialogue: "Raise it when a team asks how these standards relate to the national frameworks or to accreditation. Ask: which descriptor level does this award sit at, and is the course accredited? Avoid presenting it to students."
- statement: qaa/engineering-2023/4.5
  forPractitioner: { text: "For accredited courses, treat AHEP's learning outcomes as the minimum threshold, reading them with UK-SPEC's competence and commitment statements for IEng and CEng.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a rule for course designers on accredited courses", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on how to read the threshold for accredited courses: AHEP's outcomes, read with UK-SPEC, for all three awards. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.5). Do not quote AHEP or UK-SPEC as if they were in this text (they are the Engineering Council's, not yet ingested); set it beside the threshold rungs 4.8, 4.11 and 4.15."
  author-agent-dialogue: "Raise it when a team maps an accredited course's outcomes. Ask: which AHEP edition applies, and which outcome is weakest in our evidence? Avoid presenting it to students as their rule."
- statement: qaa/engineering-2023/4.8.b1
  forPractitioner: { text: "At threshold, BEng graduates will have shown well-connected knowledge and understanding of their discipline and its use in practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for a BEng with honours, you will have shown a joined-up understanding of your branch of engineering and how it is used in practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the BEng with honours requires at fheq:6 (fqheis:10), which the issuer maps onto a third-class degree, in the category knowledge and understanding. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.8). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.11.b1, 4.15.b1), the framework descriptor qaa/fheq-2024/4.15.b1, qaa/fqheis-2024/4.16.b1, Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/3rd and spine:6."
  author-agent-dialogue: "Raise it when a BEng with honours student asks what they must show to graduate, or a team checks its outcomes for knowledge and understanding. Ask a student: can you explain how the core ideas of your discipline fit together and where they are used? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.8.b2
  forPractitioner: { text: "At threshold, BEng graduates will have shown they can identify complex engineering problems, pick suitable tools and produce safe, secure and sustainable answers to defined needs.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for a BEng with honours, you will have shown that you can spot complex engineering problems, pick the right tools and create solutions that are safe, secure and sustainable and meet the need.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the BEng with honours requires at fheq:6 (fqheis:10), which the issuer maps onto a third-class degree, in the category problem solving. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.8). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.11.b2, 4.15.b2), the framework descriptor qaa/fheq-2024/4.15.b7, Annex D cell qaa/fheq-2024/annex-d/cognitive/r3/3rd and spine:6."
  author-agent-dialogue: "Raise it when a BEng with honours student asks what they must show to graduate, or a team checks its outcomes for problem solving. Ask a student: which tool did you choose for your last problem, and how did you check the solution was safe and sustainable? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.8.b3
  forPractitioner: { text: "At threshold, BEng graduates will have shown they can choose and use quantitative and computational analysis, aware of the limits of the methods.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for a BEng with honours, you will have shown that you can choose and use numerical and computer-based analysis, and know where those methods stop being reliable.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the BEng with honours requires at fheq:6 (fqheis:10), which the issuer maps onto a third-class degree, in the category analysis. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.8). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.11.b3, 4.15.b3), the framework descriptor qaa/fheq-2024/4.15.b2, Annex D cell qaa/fheq-2024/annex-d/knowledge/r3/3rd and spine:6."
  author-agent-dialogue: "Raise it when a BEng with honours student asks what they must show to graduate, or a team checks its outcomes for analysis. Ask a student: what assumption in your analysis would you check first if the result looked wrong? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.8.b4
  forPractitioner: { text: "At threshold, BEng graduates will have shown creativity, innovation, teamwork and communication in delivering engineering work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for a BEng with honours, you will have shown creativity and fresh thinking, worked well in a team and communicated clearly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the BEng with honours requires at fheq:6 (fqheis:10), which the issuer maps onto a third-class degree, in the category delivery, skills and practice. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.8). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.11.b4, 4.15.b4), the framework descriptor qaa/fheq-2024/4.15.b8, Annex D cells qaa/fheq-2024/annex-d/transferable/r1/3rd and qaa/fheq-2024/annex-d/transferable/r2/3rd and spine:6."
  author-agent-dialogue: "Raise it when a BEng with honours student asks what they must show to graduate, or a team checks its outcomes for delivery, skills and practice. Ask a student: what did you contribute to your last team project, and how did you explain it to others? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.8.b5
  forPractitioner: { text: "At threshold, BEng graduates will have shown they appreciate how engineering is practised professionally and commercially, its ethics and its social responsibility worldwide.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for a BEng with honours, you will have shown that you understand how engineering works as a profession and a business, and its ethical and social responsibilities around the world.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the BEng with honours requires at fheq:6 (fqheis:10), which the issuer maps onto a third-class degree, in the category values and principles. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.8). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.11.b5, 4.15.b5), the framework descriptor qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.15.b9.2, Annex D cell qaa/fheq-2024/annex-d/transferable/r4/3rd and spine:6."
  author-agent-dialogue: "Raise it when a BEng with honours student asks what they must show to graduate, or a team checks its outcomes for values and principles. Ask a student: what would you do if a client asked for a cheaper design that cut a safety margin? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.9
  forPractitioner: { text: "Set 2:1 and 2:2 criteria from your institution's common or generic undergraduate marking scheme and your nation's sector-recognised standards; no subject-specific typical outcomes are given.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a 2:1 or 2:2, you will be judged against your university's own marking scheme for undergraduate work and the national standards that apply where you study.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung (2:1 and 2:2) for the BEng with honours at fheq:6: it states no outcomes of its own and says the criteria will follow each provider's undergraduate marking scheme and the sector-recognised standards of each UK nation. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.9). Do not invent subject outcomes for this rung or present it as the minimum; set it beside the threshold items 4.8.b1 to 4.8.b5 and Annex D's 2.2 and 2.1 cells (for example qaa/fheq-2024/annex-d/summary/r1/2.2 and qaa/fheq-2024/annex-d/summary/r1/2.1), with spine:6."
  author-agent-dialogue: "Raise it when a BEng with honours student asks what 2:1 and 2:2 needs, or a team writes criteria for it. Explain that the subject sets the minimum and the institution's marking scheme sets the higher classes, and ask: have you read the marking criteria for your modules, and which band does your recent work sit in? Avoid presenting this level as what everyone must reach."
- statement: qaa/engineering-2023/4.10
  forPractitioner: { text: "Set first-class criteria from your institution's common or generic undergraduate marking scheme and your nation's sector-recognised standards; no subject-specific excellent outcomes are given.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a first, you will be judged against your university's own marking scheme for undergraduate work and the national standards that apply where you study.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung (first class) for the BEng with honours at fheq:6: it states no outcomes of its own and says the criteria will follow each provider's undergraduate marking scheme and the sector-recognised standards of each UK nation. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.10). Do not invent subject outcomes for this rung or present it as the minimum; set it beside the threshold items 4.8.b1 to 4.8.b5 and Annex D's first-class cells (for example qaa/fheq-2024/annex-d/summary/r1/1st), with spine:6."
  author-agent-dialogue: "Raise it when a BEng with honours student asks what first class needs, or a team writes criteria for it. Explain that the subject sets the minimum and the institution's marking scheme sets the higher classes, and ask: have you read the marking criteria for your modules, and which band does your recent work sit in? Avoid presenting this level as what everyone must reach."
- statement: qaa/engineering-2023/4.11.b1
  forPractitioner: { text: "At threshold, MEng graduates will have shown wide and well-connected knowledge and understanding of their discipline and its use in practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an MEng, you will have shown a broad and joined-up understanding of your branch of engineering and how it is used in practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the MEng requires at fheq:7 (fqheis:11), which the issuer maps onto a third-class degree, in the category knowledge and understanding. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.11). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.8.b1, 4.15.b1), the framework descriptor qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it when a MEng student asks what they must show to graduate, or a team checks its outcomes for knowledge and understanding. Ask a student: how far beyond your specialism can you explain the ideas of your discipline? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.11.b2
  forPractitioner: { text: "At threshold, MEng graduates will have shown they can identify complex engineering problems, pick suitable tools and produce safe, secure and sustainable answers to defined needs.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an MEng, you will have shown that you can spot complex engineering problems, pick the right tools and create solutions that are safe, secure and sustainable and meet the need.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the MEng requires at fheq:7 (fqheis:11), which the issuer maps onto a third-class degree, in the category problem solving. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.11). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.8.b2, 4.15.b2), the framework descriptor qaa/fheq-2024/4.17.b6 and spine:7."
  author-agent-dialogue: "Raise it when a MEng student asks what they must show to graduate, or a team checks its outcomes for problem solving. Ask a student: which complex problem in your project had no obvious answer, and how did you choose your approach? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.11.b3
  forPractitioner: { text: "At threshold, MEng graduates will have shown they can choose and use quantitative and computational analysis with incomplete data and discuss the limits of the methods.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an MEng, you will have shown that you can choose and use numerical and computer-based analysis even when some data are missing, and explain the limits of your methods.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the MEng requires at fheq:7 (fqheis:11), which the issuer maps onto a third-class degree, in the category analysis. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.11). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.8.b3, 4.15.b3), the framework descriptor qaa/fheq-2024/4.17.b5 and qaa/fheq-2024/4.17.b2 and spine:7."
  author-agent-dialogue: "Raise it when a MEng student asks what they must show to graduate, or a team checks its outcomes for analysis. Ask a student: which data were missing in your analysis, and how did that limit your conclusions? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.11.b4
  forPractitioner: { text: "At threshold, MEng graduates will have shown creativity, innovation, effective teamwork, leadership and communication in delivering engineering work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an MEng, you will have shown creativity and fresh thinking, worked effectively in a team, taken a lead and communicated clearly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the MEng requires at fheq:7 (fqheis:11), which the issuer maps onto a third-class degree, in the category delivery, skills and practice. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.11). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.8.b4, 4.15.b4), the framework descriptor qaa/fheq-2024/4.17.b5 and qaa/fheq-2024/4.17.b8.1 and spine:7."
  author-agent-dialogue: "Raise it when a MEng student asks what they must show to graduate, or a team checks its outcomes for delivery, skills and practice. Ask a student: when did you lead a team, and what did you do when it stalled? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.11.b5
  forPractitioner: { text: "At threshold, MEng graduates will have shown they appreciate how engineering is practised professionally and commercially, its ethics and its social responsibility worldwide.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an MEng, you will have shown that you understand how engineering works as a profession and a business, and its ethical and social responsibilities around the world.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the MEng requires at fheq:7 (fqheis:11), which the issuer maps onto a third-class degree, in the category values and principles. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.11). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.8.b5, 4.15.b5), the framework descriptor qaa/fheq-2024/4.17.b8.1 and qaa/fheq-2024/4.17.b8.2 and spine:7."
  author-agent-dialogue: "Raise it when a MEng student asks what they must show to graduate, or a team checks its outcomes for values and principles. Ask a student: which professional or ethical judgement in your project would you defend to an outside reviewer? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.12
  forPractitioner: { text: "Set 2:1 and 2:2 criteria for the MEng from your institution's common or generic integrated master's marking scheme; no subject-specific typical outcomes are given.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a 2:1 or 2:2 on an integrated master's, you will be judged against your university's own marking scheme for these courses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung (2:1 and 2:2) for the MEng at fheq:7: it states no outcomes of its own and says the criteria will follow each provider's marking scheme for integrated master's courses. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.12). Do not invent subject outcomes for this rung or present it as the minimum; set it beside the threshold items 4.11.b1 to 4.11.b5 and the master's descriptor qaa/fheq-2024/4.17 and spine:7 (Annex D describes level 6 classes, so check the provider's scheme before reading it across)."
  author-agent-dialogue: "Raise it when a MEng student asks what 2:1 and 2:2 needs, or a team writes criteria for it. Explain that the subject sets the minimum and the institution's marking scheme sets the higher classes, and ask: have you read the marking criteria for your modules, and which band does your recent work sit in? Avoid presenting this level as what everyone must reach."
- statement: qaa/engineering-2023/4.13
  forPractitioner: { text: "Set first-class criteria for the MEng from your institution's common or generic integrated master's marking scheme; no subject-specific excellent outcomes are given.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a first on an integrated master's, you will be judged against your university's own marking scheme for these courses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung (first class) for the MEng at fheq:7: it states no outcomes of its own and says the criteria will follow each provider's marking scheme for integrated master's courses. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.13). Do not invent subject outcomes for this rung or present it as the minimum; set it beside the threshold items 4.11.b1 to 4.11.b5 and the master's descriptor qaa/fheq-2024/4.17 and spine:7."
  author-agent-dialogue: "Raise it when a MEng student asks what first class needs, or a team writes criteria for it. Explain that the subject sets the minimum and the institution's marking scheme sets the higher classes, and ask: have you read the marking criteria for your modules, and which band does your recent work sit in? Avoid presenting this level as what everyone must reach."
- statement: qaa/engineering-2023/4.14
  forPractitioner: { text: "Make sure every MSc graduate shows at least threshold attainment across all relevant outcome categories; threshold usually matches a pass.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To get a taught master's in engineering you must reach at least the minimum standard in every relevant area of the course; that usually means a pass.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a must for the postgraduate taught master's at fheq:7 (fqheis:11): threshold attainment in every relevant outcome category, usually a pass. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.14). Do not claim merit or distinction is required; set it beside the threshold items 4.15.b1 to 4.15.b5 and the master's descriptor qaa/fheq-2024/4.17 (spine:7)."
  author-agent-dialogue: "Raise it when an MSc student asks what they need to pass. Ask: in which outcome area is your evidence thinnest? Avoid presenting merit as the minimum."
- statement: qaa/engineering-2023/4.15.b1
  forPractitioner: { text: "At threshold, MSc graduates will have shown well-connected knowledge and understanding of their discipline or specialism.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for a taught MSc, you will have shown a joined-up understanding of your branch of engineering or your specialist area.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the taught MSc requires at fheq:7 (fqheis:11), which the issuer maps onto a pass, in the category knowledge and understanding. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.15). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.8.b1, 4.11.b1), the framework descriptor qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it when a taught MSc student asks what they must show to graduate, or a team checks its outcomes for knowledge and understanding. Ask a student: how does your specialism connect to the wider discipline it comes from? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.15.b2
  forPractitioner: { text: "At threshold, MSc graduates will have shown they can identify complex engineering problems, pick suitable tools and produce safe, secure and sustainable answers to defined needs.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for a taught MSc, you will have shown that you can spot complex engineering problems, pick the right tools and create solutions that are safe, secure and sustainable and meet the need.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the taught MSc requires at fheq:7 (fqheis:11), which the issuer maps onto a pass, in the category problem solving. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.15). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.8.b2, 4.11.b2), the framework descriptor qaa/fheq-2024/4.17.b6 and spine:7."
  author-agent-dialogue: "Raise it when a taught MSc student asks what they must show to graduate, or a team checks its outcomes for problem solving. Ask a student: which tool or method did you reject for your project problem, and why? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.15.b3
  forPractitioner: { text: "At threshold, MSc graduates will have shown they can choose and use quantitative and computational analysis with incomplete data and discuss the limits of the methods.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for a taught MSc, you will have shown that you can choose and use numerical and computer-based analysis even when some data are missing, and explain the limits of your methods.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the taught MSc requires at fheq:7 (fqheis:11), which the issuer maps onto a pass, in the category analysis. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.15). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.8.b3, 4.11.b3), the framework descriptor qaa/fheq-2024/4.17.b5 and qaa/fheq-2024/4.17.b2 and spine:7."
  author-agent-dialogue: "Raise it when a taught MSc student asks what they must show to graduate, or a team checks its outcomes for analysis. Ask a student: how sure are you of your result, given the data you lacked? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.15.b4
  forPractitioner: { text: "At threshold, MSc graduates will have shown creativity, innovation, research, effective teamwork, leadership and communication in delivering engineering work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for a taught MSc, you will have shown creativity and fresh thinking, carried out research, worked effectively in a team, taken a lead and communicated clearly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the taught MSc requires at fheq:7 (fqheis:11), which the issuer maps onto a pass, in the category delivery, skills and practice. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.15). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.8.b4, 4.11.b4), the framework descriptor qaa/fheq-2024/4.17.b5 and qaa/fheq-2024/4.17.b8.1 and spine:7."
  author-agent-dialogue: "Raise it when a taught MSc student asks what they must show to graduate, or a team checks its outcomes for delivery, skills and practice. Ask a student: what did your research add that a literature search alone would not? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.15.b5
  forPractitioner: { text: "At threshold, MSc graduates will have shown they appreciate how engineering is practised professionally and commercially, its ethics and its social responsibility worldwide.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for a taught MSc, you will have shown that you understand how engineering works as a profession and a business, and its ethical and social responsibilities around the world.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the taught MSc requires at fheq:7 (fqheis:11), which the issuer maps onto a pass, in the category values and principles. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.15). Do not present it as the typical or excellent level, which the issuer leaves to marking schemes; set it beside the same category for the other awards (4.8.b5, 4.11.b5), the framework descriptor qaa/fheq-2024/4.17.b8.1 and qaa/fheq-2024/4.17.b8.2 and spine:7."
  author-agent-dialogue: "Raise it when a taught MSc student asks what they must show to graduate, or a team checks its outcomes for values and principles. Ask a student: which commercial pressure in your field most tests an engineer's ethics? Present it as the minimum, not the target, and avoid reading the issuer's list aloud."
- statement: qaa/engineering-2023/4.16
  forPractitioner: { text: "Set merit criteria from your institution's common or generic master's marking scheme; no subject-specific merit outcomes are given.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a merit, you will be judged against your university's own marking scheme for master's courses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical rung (merit) for the taught MSc at fheq:7: it states no outcomes of its own and says the criteria will follow each provider's marking scheme for master's courses. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.16). Do not invent subject outcomes for this rung or present it as the minimum; set it beside the threshold items 4.15.b1 to 4.15.b5 and the master's descriptor qaa/fheq-2024/4.17 and spine:7."
  author-agent-dialogue: "Raise it when a taught MSc student asks what merit needs, or a team writes criteria for it. Explain that the subject sets the minimum and the institution's marking scheme sets the higher classes, and ask: have you read the marking criteria for your modules, and which band does your recent work sit in? Avoid presenting this level as what everyone must reach."
- statement: qaa/engineering-2023/4.17
  forPractitioner: { text: "Set distinction criteria from your institution's common or generic master's marking scheme; no subject-specific distinction outcomes are given.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a distinction, you will be judged against your university's own marking scheme for master's courses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent rung (distinction) for the taught MSc at fheq:7: it states no outcomes of its own and says the criteria will follow each provider's marking scheme for master's courses. Cite it as (QAA, 2023, Engineering Subject Benchmark Statement, para 4.17). Do not invent subject outcomes for this rung or present it as the minimum; set it beside the threshold items 4.15.b1 to 4.15.b5 and the master's descriptor qaa/fheq-2024/4.17 and spine:7."
  author-agent-dialogue: "Raise it when a taught MSc student asks what distinction needs, or a team writes criteria for it. Explain that the subject sets the minimum and the institution's marking scheme sets the higher classes, and ask: have you read the marking criteria for your modules, and which band does your recent work sit in? Avoid presenting this level as what everyone must reach."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 1.5; 2.5; 4.4; 4.6" }
  - { id: "fheq:7", role: "cites", locator: "D1, 1.6; 2.7; 4.4" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 1.5 (as SCQF Level 10); 2.5; 4.4; 4.6" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 1.6 (as SCQF Level 11); 2.7; 4.4" }
  - { id: "fheq:5", role: "mentions", locator: "D1, 1.4 (foundation degrees, outside scope)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 1.5; 2.5; 4.4; 4.6: honours at FHEQ Level 6 or FQHEIS/SCQF Level 10)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 1.6; 2.7; 4.4); the frameworks share one descriptor (std:doc:qaa-fheq-2024-framework, S5)" }
  - { from: "fheq:6", to: "qfehea:1", relation: "corresponds", basis: "stated (D1, 1.5: first cycle); qfehea ids are held in std:doc:qaa-fheq-2024-framework, S5" }
  - { from: "fheq:7", to: "qfehea:2", relation: "corresponds", basis: "stated (D1, 1.6; 1.8: integrated master's first and second cycle; master's second cycle)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.9", "1.13", "1.14", "1.15", "1.16", "2.3", "2.4", "2.14", "3.6", "3.14"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.16", "1.17", "1.18", "1.19", "2.3", "3.13", "3.14"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.2", "1.9", "1.19", "1.20", "2.3", "2.13", "3.8", "3.9", "4.8", "4.11", "4.15"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.29", "1.30", "1.31", "2.11", "2.12", "2.13", "3.12", "3.14"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-engineering-2019-benchmarks (not held)", note: "the fourth edition, 2019, named in the back matter; this is the fifth edition" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ Levels 6 and 7 (1.5, 1.6, 2.5, 2.7, 4.4); restated in 3.14" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the honours classes (4.6), cited as a separate annex" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS/SCQF Levels 10 and 11 (1.5, 1.6, 2.5, 2.7, 4.4)" }
- { rel: "themeReference", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "Education for Sustainable Development Guidance (1.20)" }
- { rel: "themeReference", target: "std:doc:qaa-enterprise-2018-guidance", note: "Enterprise and Entrepreneurship Education guidance, 2018 (1.29)" }
- { rel: "relatedTo", target: "std:doc:qaa-computing-2022-benchmarks", note: "the front matter names a separate statement for Computing" }
- { rel: "refersTo", target: "Engineering Council, Accreditation of Higher Education Programmes (AHEP) (not yet ingested; Part E)", note: "threshold for accredited courses (4.5); 1.32, 2.10, 2.17, 2.22, 3.7" }
- { rel: "refersTo", target: "Engineering Council, UK-SPEC (not yet ingested; Part E)", note: "read with AHEP (4.5)" }
- { rel: "refersTo", target: "QAA Characteristics Statements: Higher Education in Apprenticeships; Master's Degrees (not yet ingested)", note: "1.4; 1.8" }
- { rel: "refersTo", target: "QAA UK Quality Code and Advice and Guidance (not yet ingested)", note: "front matter; 1.34" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2023-03"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "none-stated (an advisory group of 2023 is listed in the back matter)"
replacedBy: "none"
editions: "fifth edition, published 8 March 2023; earlier editions 2019 (fourth), 2015 (third), 2006 (second), 2000 (original), as the back matter lists them"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- Engineering creates, develops and applies technology, processes and systems that improve lives and protect people, joining ingenuity and creativity to science and mathematics; at its core is putting things together and designing things that work, and then work better (D1, 1.1).
- It aims at fair and sustainable answers to global challenges, read through the UN Sustainable Development Goals and through cybersecurity, infrastructure, manufacturing, mobility and energy (D1, 1.2).
- It is a very broad subject of many disciplines and specialisms, studied as the BEng with honours, the integrated MEng and the taught MSc, with general and multidisciplinary courses beside single-specialism ones (D1, 1.3, 1.7, 1.8).
- Study usually covers five areas: scientific and mathematical principles; analysis with computational tools; design, creativity and innovation; engineering and society; and engineering practice (D1, 1.9).
- Problem-solving runs from broadly defined, single-domain problems to complex problems with no obvious or optimal answer, met early in the course (D1, 1.10).
- Practical work, physical or software build-and-test, sets it apart from other applied sciences (D1, 1.11, 3.3).
- Ethics, safety and security are core professional concerns, each with its own section (D1, 1.21 to 1.28).
- It is shaped by the profession: most degrees are accredited by professional engineering institutions licensed by the Engineering Council against AHEP, and industry is involved in design and delivery (D1, 1.32, 1.33, 2.1, 2.11, 2.22).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "a more diverse profession and equitable designs for users worldwide; EDI embedded from team make-up to solutions; global perspectives and the questioning of historic western assumptions; inclusive course culture and fair assessment of group work (D1, 1.13 to 1.15, 2.4, 2.14, 3.14)"
  statements: ["qaa/engineering-2023/1.15", "qaa/engineering-2023/2.3.b6", "qaa/engineering-2023/2.4", "qaa/engineering-2023/2.14", "qaa/engineering-2023/3.14.b14"]
- theme: theme:accessibility
  inThisSubject: "accessible design as a standard part of the curriculum; accessible labs, workshops, group work and placements, hidden disabilities included; flexible delivery and reasonable adjustments in assessment (D1, 1.16 to 1.18, 3.13, 3.14)"
  statements: ["qaa/engineering-2023/1.16", "qaa/engineering-2023/1.17", "qaa/engineering-2023/1.18", "qaa/engineering-2023/3.14.b2"]
- theme: theme:esd
  inThisSubject: "headed Sustainability: engineers as builders of a sustainable future; the SDGs encouraged in design, teaching and assessment; lifecycle and resource impact; challenging industry norms for net zero (D1, 1.2, 1.19, 1.20, 2.3, 2.13)"
  statements: ["qaa/engineering-2023/1.2", "qaa/engineering-2023/1.19", "qaa/engineering-2023/2.3.b9"]
- theme: theme:enterprise
  inThisSubject: "headed Industry and entrepreneurship: industrial involvement, advisory boards, placements and authentic assessment for employment; to be read with the 2018 enterprise guidance (D1, 1.29 to 1.31, 2.11 to 2.13, 3.12, 3.14)"
  statements: ["qaa/engineering-2023/1.31", "qaa/engineering-2023/2.11", "qaa/engineering-2023/3.14.b15"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "1.9", gloss: "five areas: science, mathematics and principles; analysis and computation; design, creativity and innovation; engineering and society; engineering practice" }
  - { component: "3.2", gloss: "academic tools, digital and practical skills, mindset and ethical framework of a practising engineer" }
  - { component: "3.3", gloss: "practical work, from software build-and-test to physical construction" }
  - { component: "3.4", gloss: "specialist content for local context; non-engineering subjects for breadth" }
practices:
  - { component: "2.3", kind: "teaching", gloss: "design features: practical work, maths and science, digital skills, individual and group projects, managing compromise, cultural competence" }
  - { component: "3.5", kind: "teaching", gloss: "activities aligned with intended outcomes" }
  - { component: "3.6", kind: "teaching", gloss: "diverse methods, regularly updated, recognising varied backgrounds" }
  - { component: "3.8", kind: "learning", gloss: "bachelor's: lab work and individual and group projects in social and ethical context" }
  - { component: "3.9", kind: "learning", gloss: "MEng: deeper technical work, teamwork, industrial applications, case studies and visits" }
  - { component: "3.10", kind: "learning", gloss: "other master's: focus-led, growing self-direction" }
  - { component: "3.12", kind: "learning", gloss: "employability in and beyond the curriculum" }
  - { component: "3.13", kind: "learning", gloss: "flexible, synchronous and asynchronous delivery" }
  - { component: "3.14", kind: "assessment", gloss: "alignment, accessibility, diverse methods, criteria and feedback, integrity, group work, authentic assessment" }
  - { component: "3.15", kind: "assessment", gloss: "strict failure limits on accredited degrees" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.8", award: "bachelor's with honours", items: 5 }
  - { rung: "typical", leadIn: "4.9", award: "bachelor's with honours", items: 1 }
  - { rung: "excellent", leadIn: "4.10", award: "bachelor's with honours", items: 1 }
  - { rung: "threshold", leadIn: "4.11", award: "integrated master's", items: 5 }
  - { rung: "typical", leadIn: "4.12", award: "integrated master's", items: 1 }
  - { rung: "excellent", leadIn: "4.13", award: "integrated master's", items: 1 }
  - { rung: "threshold", leadIn: "4.15", award: "postgraduate taught master's", items: 5 }
  - { rung: "typical", leadIn: "4.16", award: "postgraduate taught master's", items: 1 }
  - { rung: "excellent", leadIn: "4.17", award: "postgraduate taught master's", items: 1 }
rungBases: "Three awards, each with the same three rungs under its own headings. Threshold: a list of five outcome categories, mapped onto a third (honours and MEng) or a pass (MSc), with the threshold also set by the accrediting institution where the course is accredited (4.8, 4.11, 4.15); for accredited courses AHEP's outcomes are the threshold (4.5). Typical (2:1 and 2:2; merit) and excellent (first; distinction) state no outcomes: their criteria follow each provider's marking scheme (4.9, 4.10, 4.12, 4.13, 4.16, 4.17); for honours, 4.6 points to Annex D. Each typical and excellent paragraph is held as one record."
outcomeLists: []
outcomes:
  - { outcome: "knowledge and understanding (BEng)", threshold: "qaa/engineering-2023/4.8.b1", typical: "none", excellent: "none", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "problem solving (BEng)", threshold: "qaa/engineering-2023/4.8.b2", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "analysis (BEng)", threshold: "qaa/engineering-2023/4.8.b3", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "delivery, skills and practice (BEng)", threshold: "qaa/engineering-2023/4.8.b4", typical: "none", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "values and principles (BEng)", threshold: "qaa/engineering-2023/4.8.b5", typical: "none", excellent: "none", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "knowledge and understanding (MEng)", threshold: "qaa/engineering-2023/4.11.b1", typical: "none", excellent: "none", basis: "stated", domain: "knowledge", award: "integrated master's" }
  - { outcome: "problem solving (MEng)", threshold: "qaa/engineering-2023/4.11.b2", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "integrated master's" }
  - { outcome: "analysis (MEng)", threshold: "qaa/engineering-2023/4.11.b3", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "integrated master's" }
  - { outcome: "delivery, skills and practice (MEng)", threshold: "qaa/engineering-2023/4.11.b4", typical: "none", excellent: "none", basis: "stated", domain: "generic-skill", award: "integrated master's" }
  - { outcome: "values and principles (MEng)", threshold: "qaa/engineering-2023/4.11.b5", typical: "none", excellent: "none", basis: "stated", domain: "understanding", award: "integrated master's" }
  - { outcome: "knowledge and understanding (MSc)", threshold: "qaa/engineering-2023/4.15.b1", typical: "none", excellent: "none", basis: "stated", domain: "knowledge", award: "postgraduate taught master's" }
  - { outcome: "problem solving (MSc)", threshold: "qaa/engineering-2023/4.15.b2", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "postgraduate taught master's" }
  - { outcome: "analysis (MSc)", threshold: "qaa/engineering-2023/4.15.b3", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "postgraduate taught master's" }
  - { outcome: "delivery, skills and practice (MSc)", threshold: "qaa/engineering-2023/4.15.b4", typical: "none", excellent: "none", basis: "stated", domain: "generic-skill", award: "postgraduate taught master's" }
  - { outcome: "values and principles (MSc)", threshold: "qaa/engineering-2023/4.15.b5", typical: "none", excellent: "none", basis: "stated", domain: "understanding", award: "postgraduate taught master's" }
  - { outcome: "all categories by marking scheme (BEng)", threshold: "none", typical: "qaa/engineering-2023/4.9", excellent: "qaa/engineering-2023/4.10", basis: "inferred", domain: "none", award: "bachelor's with honours" }
  - { outcome: "all categories by marking scheme (MEng)", threshold: "none", typical: "qaa/engineering-2023/4.12", excellent: "qaa/engineering-2023/4.13", basis: "inferred", domain: "none", award: "integrated master's" }
  - { outcome: "all categories by marking scheme (MSc)", threshold: "none", typical: "qaa/engineering-2023/4.16", excellent: "qaa/engineering-2023/4.17", basis: "inferred", domain: "none", award: "postgraduate taught master's" }
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
- { body: "Engineering Council", says: "the UK regulator of the engineering profession: licenses professional engineering institutions to register engineers and accredit degrees, sets AHEP and UK-SPEC, keeps a database of accredited courses and represents the UK in international accords (D1, 1.4, 1.21, 1.32, 1.33, 1.34, 2.16, 2.17, 2.22, 3.4, 4.4, 4.5)", requirements: "not yet ingested (Part E): AHEP and UK-SPEC" }
- { body: "professional engineering institutions (PEIs)", says: "more than 35 licensed bodies that accredit individual courses by peer review, may add discipline requirements and set the threshold for accredited courses (D1, 1.33, 2.10, 2.16, 2.18, 2.22, 3.4, 4.4, 4.8, 4.11, 4.15)", requirements: "not yet ingested (Part E): each institution's own accreditation requirements" }
- { body: "Royal Academy of Engineering", says: "co-author with the Engineering Council of the 2017 ethical principles; its Engineering X initiative offers safety case studies; supports courses through visiting professorships and exchanges (D1, 1.21, 1.24, 2.18)", requirements: "not-applicable-by-design: not an accrediting body" }
- { body: "Engineering Professors' Council", says: "represents engineering academics, researches admissions, skills and innovation, and publishes the Engineering Ethics Toolkit (D1, 1.21, 2.18)", requirements: "not-applicable-by-design" }
- { body: "International Engineering Alliance (IEA); ENGINEERS EUROPE (formerly FEANI); European Network for Accreditation of Engineering Education (ENAEE)", says: "international bodies in which the Engineering Council is the UK partner; the IEA's graduate attributes, the Washington Accord and ENAEE's EUR-ACE standards bear on recognition of UK degrees (D1, 2.17)", requirements: "not yet ingested (Part E)" }
- { body: "UK and Ireland Engineering Education Research Network; European Society for Engineering Education (SEFI)", says: "networks offering conferences for engineering education research (D1, 2.18)", requirements: "not-applicable-by-design" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.9", "1.13", "1.14", "1.15", "1.16", "2.3", "2.4", "2.14", "3.6", "3.14"], statements: ["1.15", "2.3.b6", "2.4", "2.14", "3.14.b14"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: Accessibility and the needs of disabled students)", carriedIn: ["1.16", "1.17", "1.18", "1.19", "2.3", "3.13", "3.14"], statements: ["1.16", "1.17", "1.18", "3.14.b2"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.2", "1.9", "1.19", "1.20", "2.3", "2.13", "3.8", "3.9", "4.8", "4.11", "4.15"], statements: ["1.2", "1.19", "2.3.b9"] }
  - { id: "theme:enterprise", named: "Industry and entrepreneurship (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.29", "1.30", "1.31", "2.11", "2.12", "2.13", "3.12", "3.14"], statements: ["1.31", "2.11", "3.14.b15"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["1.4", "1.5", "1.6", "2.3", "2.5", "2.7", "3.14", "4.4", "4.6"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["1.5", "1.6", "2.3", "2.5", "2.7", "4.4", "4.6"] }
  - { framework: "other: QF-EHEA (overarching framework of the European Higher Education Area)", levels: [], citedIn: ["1.5", "1.6", "1.8"] }
bodies:
  - { body: "Engineering Council", citedIn: ["1.4", "1.21", "1.32", "1.33", "1.34", "2.16", "2.17", "2.22", "3.4", "4.4", "4.5"] }
  - { body: "professional engineering institutions", citedIn: ["1.33", "2.10", "2.16", "2.18", "2.22", "3.4", "4.4", "4.8", "4.11", "4.15"] }
  - { body: "Royal Academy of Engineering", citedIn: ["1.21", "1.24", "2.18"] }
  - { body: "Engineering Professors' Council", citedIn: ["1.21", "2.18"] }
  - { body: "International Engineering Alliance; ENGINEERS EUROPE; ENAEE", citedIn: ["2.17"] }
  - { body: "UK and Ireland Engineering Education Research Network; SEFI", citedIn: ["2.18"] }
  - { body: "Intergovernmental Panel on Climate Change (IPCC)", citedIn: ["2.13"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework", named: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["1.6", "3.14"], role: "the master's descriptor the MEng meets; the rule that no award is made without the outcomes" }
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.6"], role: "the four honours classes, standing in for subject typical and excellent outcomes" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "The Education for Sustainable Development Guidance", citedIn: ["1.20"], role: "pedagogic approaches for ESD" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (2018)", citedIn: ["1.29"], role: "to be read with the industry and entrepreneurship section" }
  - { document: "QAA Characteristics Statement: Higher Education in Apprenticeships (not yet ingested: Part E)", named: "Characteristics Statement: Higher Education in Apprenticeships", citedIn: ["1.4"], role: "apprenticeships, outside scope" }
  - { document: "QAA Characteristics Statement: Master's Degrees (not yet ingested: Part E)", named: "the QAA characteristics statement on master's degrees", citedIn: ["1.8"], role: "types of master's degree" }
  - { document: "QAA UK Quality Code (not yet ingested: Part E)", named: "UK Quality Code", citedIn: ["1.34"], role: "expectations informing non-accredited provision" }
  - { document: "Engineering Council, AHEP (not yet ingested: Part E)", named: "Accreditation of Higher Education Programmes (AHEP)", citedIn: ["1.32", "2.10", "2.17", "2.22", "3.7", "4.5"], role: "the threshold and requirements for accredited courses" }
  - { document: "Engineering Council, UK-SPEC (not yet ingested: Part E)", named: "UK Standard for Professional Engineering Competence and Commitment (UK-SPEC)", citedIn: ["4.5"], role: "competence statements for IEng and CEng, read with AHEP" }
  - { document: "Engineering Council and Royal Academy of Engineering, Statement of Ethical Principles (external)", named: "a revised statement on these principles (2017)", citedIn: ["1.21"], role: "the profession's ethical principles" }
  - { document: "Engineering Professors' Council, Engineering Ethics Toolkit (external)", named: "Engineering Ethics Toolkit", citedIn: ["1.21"], role: "case studies for teaching ethics" }
  - { document: "Royal Academy of Engineering, Engineering X (external)", named: "The Engineering X initiative", citedIn: ["1.24"], role: "safety case studies" }
  - { document: "IEA Graduate Attributes and Professional Competences; Washington Accord; ENAEE EUR-ACE Framework Standards and Guidelines (external)", named: "Graduate Attributes and Professional Competences; EUR-ACE Framework Standards and Guidelines; the Washington Accord", citedIn: ["2.17"], role: "international recognition of UK degrees" }
  - { document: "UN Sustainable Development Goals (external)", named: "United Nations Sustainable Development Goals", citedIn: ["1.2", "1.19"], role: "the frame of the sustainability theme" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "broadly-defined-problem", definition: "a problem met by making suitable assumptions and balancing requirements, solvable with engineering science and learned analysis (D1, 1.10)", beneficiaryDefinition: "a problem with a clear goal that you can solve with the methods you have learned", scopeNote: "set against complex problems", category: "unknown", practices: ["education"] }
- { slug: "complex-engineering-problem", definition: "a problem with no obvious, known or optimal solution, possibly with wide or conflicting technical issues or user needs, met through creativity and innovative use of engineering (D1, 1.10)", beneficiaryDefinition: "a problem with no single right answer, where you have to weigh competing needs and think creatively", scopeNote: "named in every threshold list (4.8, 4.11, 4.15)", category: "unknown", practices: ["education"] }
- { slug: "security", definition: "relative freedom from threat or harm caused by deliberate hostile acts, from national security to crime, including protecting assets and personal data (D1, 1.25)", beneficiaryDefinition: "being protected against people who set out to cause harm", scopeNote: "one of the subject sections, beside ethics and safety", category: "unknown", practices: ["education"] }
- { slug: "accreditation", definition: "periodic peer review of a single course by a licensed professional engineering institution, checking it provides the grounding for professional registration (D1, 1.32, 1.33, 2.22)", beneficiaryDefinition: "a check by the profession that a course prepares you for registration as an engineer", scopeNote: "optional (1.34); AHEP sets its threshold (4.5)", category: "unknown", practices: ["education"] }
- { slug: "integrated-masters-degree", definition: "a course designed as one whole from entry to completion, spanning first and second cycles, with at least one year at FHEQ Level 7 or SCQF Level 11 (D1, 1.6)", beneficiaryDefinition: "a single course, usually four years, that takes you through a bachelor's level to a master's", scopeNote: "often denoted MEng", category: "unknown", practices: ["education"] }
- { slug: "threshold-level", definition: "the minimum attainment a graduate must show in every outcome category, mapped onto a third or a pass (D1, 4.8, 4.11, 4.14, 4.15)", beneficiaryDefinition: "the lowest standard you must reach to be awarded the degree", scopeNote: "for accredited courses AHEP's outcomes are the threshold (4.5)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "broadly-defined-problem", form: "broadly defined problems", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "complex-engineering-problem", form: "complex engineering problems", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "complex-engineering-problem", form: "complex problems", lang: "en", partOfSpeech: "noun-phrase", termStatus: "admitted", register: "discipline-specific" }
- { concept: "security", form: "security", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "accreditation", form: "accreditation", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "integrated-masters-degree", form: "integrated master's degree", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "integrated-masters-degree", form: "MEng", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "formal" }
- { concept: "threshold-level", form: "threshold level", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "contrasts-with", from: "broadly-defined-problem", to: "complex-engineering-problem", note: "1.10" }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement Engineering"
  edition: "March 2023 (fifth edition)"
  year: 2023
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/engineering-2023/engineering-2023.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: a8bb20ba437fd6f55c1873358eb5740f59a77dc8e43c8678e16678a80096aa0e
  heldFiles: ["wkspc2601-library/txt/qaa-2023-engineering-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2023-engineering-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2023-engineering-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2023-engineering-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0057", citation: "Engineering Council, The Accreditation of Higher Education Programmes (AHEP), current edition", settles: ["SB5", "S7", "SB6"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0058", citation: "Engineering Council, UK Standard for Professional Engineering Competence and Commitment (UK-SPEC)", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0036", citation: "QAA Characteristics Statements: Higher Education in Apprenticeships; Master's Degrees", settles: ["SB6", "S7"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- Rungs: three awards, each with threshold, typical and excellent. Only the threshold rungs carry outcome lists (five categories each, 15 records); the typical and excellent rungs (4.9, 4.10, 4.12, 4.13, 4.16, 4.17) state no outcomes and defer to provider marking schemes, so each is held as one record with domain none. Psychology had three parallel nine-item lists for one award.
- Rung labels differ by award: honours and MEng use 3rd, 2.2 or 2.1, and 1st; the MSc uses pass, merit and distinction. The rung headings sit inside the paragraph before in the held text (for example 4.8.b5 ends in "Typical level (2.2 or 2.1)"); records cut with `find` to leave them out.
- Threshold force: the stems 4.8, 4.11 and 4.15 say graduates "must demonstrate at least a threshold-level" and lead into "graduates will have demonstrated the following"; the items take force threshold (forceFrom the stem), as the issuer defines the rung as the minimum for the award. The stems themselves are not separate records; 4.14, a paragraph of its own restating the MSc threshold with must, is.
- gradeOf: the threshold items have no typical or excellent counterpart, so they link to nothing; 4.10, 4.13 and 4.17 link to 4.9, 4.12 and 4.16 (inferred: each is the same marking-scheme outcome one rung up). Inferred links: 4.10 to 4.9, 4.13 to 4.12, 4.17 to 4.16. The five threshold categories are named by the issuer, so the SB4 outcome rows for them are stated.
- The same five categories repeat across the three awards with small wording changes: MEng adds "broad", "in the absence of complete data, discussing the limitations", "effective" teamworking and leadership; MSc adds "or specialisation" and "research". Problem solving and values and principles are word for word the same at all three awards and both levels: P3 to note that the text does not grade them by level.
- 4.15 says the MSc threshold criteria follow marking schemes "for integrated master's courses": probably an issuer slip for master's courses (4.16 and 4.17 say master's courses). Recorded as the text has it.
- 4.6 sends honours readers to Annex D for the four classes; Annex D covers FHEQ Level 6 and FQHEIS Level 10 only, so no shared document covers MEng or MSc classes. Not cut as a statement (a reading instruction); recorded in SB4 rungBases and SB6.
- Obliging words outside the five (convention batch 1): "the expectation is that" (2.3.b1, 3.8) and "needs to" or "need" (1.22, 2.11, 3.3, 3.8) held as describes; "is encouraged" (1.19, 3.14.b3, 3.14.b15) held as describes where it carries the record; "are expected to (be able to)" (2.3.b4, 2.3.b7) and "there are expectations that ... will" (3.10) held as will, the meaning being a plain expected outcome; "requires" and "required" (2.4, 2.10, 1.33) held as must, as the brief now directs. For Abbott.
- Not cut as statements, with the obliging or "will" word they carry: 1.1 ("engineers of today require" these skills: a description of the profession); 1.6 ("academic requirements" for transfer); 1.13 ("This requires understanding": a condition, no one obliged); 1.14 (EDI "a core expectation" for professional engineers; "will support" as a prediction); 1.29 (a reading instruction, "should be read in conjunction with"); 1.30 ("will have" advisory boards: a description); 1.34 ("are not required to be accredited": no obligation); 2.13 ("graduates need to be socialised": reasoning); 2.17 ("readers are advised"); 2.21 (external examiners "will be asked": a description of the system); 4.1 to 4.3 (framing; the 4.1 list names awards, not outcomes); 4.6 (reading instruction); 4.7 (plain present). For Abbott.
- Plain-present provider norms (template open point 5), not statements: 1.3 and 1.8 (course types), 1.9 (five areas, recorded in SB3), 2.3.b5 and 2.3.b8, 2.12, 2.15, 3.5, 3.6, 3.9, 3.12, 3.13, 3.14.b12, and the assessment methods list 3.14.b4 to 3.14.b11 (SB3).
- Skeleton corrections: candidates 1.3.b1 to b3, 1.8.b1 to b3, 1.9.b1 to b5, 1.34.b1 to b3, 2.12.b1 to b6, 2.18.b1 to b4, 3.14.b4 to b12 and 4.1.b1 to b3 dropped (description, lists of courses, bodies or methods; 4.1's items name awards, not threshold outcomes, despite the skeleton's rung tag); 2.3.b7 extended across the page break to "working with complexity." (the skeleton cut it at "justified"); the 3.14 stem cut to its first sentence; paragraph records cut with `find` to drop trailing headings and page numbers. Candidates 1.5, 2.20 and 3.4 kept.
- Records added that the skeleton did not flag: 1.22, 1.26, 1.27, 1.28 ("are able to", "can", "need"), 2.1, 2.4, 2.5, 2.7, 2.9, 2.10, 2.11, 3.3, 3.8, 3.10, 3.14 (stem), 3.15, 4.4, 4.9, 4.10, 4.12, 4.13, 4.16, 4.17. The skeleton's rung counts (threshold 18, typical 0, excellent 0) are replaced by threshold 15, typical 3, excellent 3.
- Security outcomes (1.26 to 1.28) are stated in the plain present about "engineers" ("know", "are able to", "can"), outside any list; held as will outcomes across the three awards. P3 to confirm they count as outcome statements.
- Levels: statements that hold for all three awards carry fheq:6, the lowest award level; statements tied to the MEng or MSc, or to "higher FHEQ/FQHEIS levels" (2.3.b4, 2.3.b7), carry fheq:7. Generic skills (1.2, 2.3.b4, 2.3.b10, 3.10, 3.14.b14, 3.14.b15, and 4.8.b4, 4.11.b4, 4.15.b4) refine fheq:6 or fheq:7 as recorded; read against the frameworks, not stated by the issuer (inferred).
- Subject codes: CAH10-01 engineering matches the subject named; CAH10-01-01 engineering (non-specific) and HECoS 100184 general or integrated engineering are inferred (the text names no codes; 1.7 names general and multidisciplinary courses). For P3.
- Frameworks: FHEQ and FQHEIS (also as SCQF) cited; the CQFW is not named (Wales appears only as the Quality Assessment Framework for Wales, a quality framework, in the front matter). QF-EHEA cycles cited in 1.5, 1.6 and 1.8 are held as crosswalks to qfehea ids, which the FHEQ document records; they are not in the shared level list.
- Ethics, Safety and Security are subject sections beside the four cross-cutting themes, not themes the front matter names; no new theme id proposed (SB1 records them). Generative AI is not mentioned.
- Section order differs from Psychology: the four themes sit inside section 1 with ethics, safety, security and accreditation; section 2 covers design, progression, partnership and review; section 4 has an introduction (4.1 to 4.7) before the rungs, and a separate MSc block.
- Bodies: the Engineering Council and the professional engineering institutions are the PSRBs; their requirements (AHEP, UK-SPEC) are not yet ingested (D3). The IPCC (2.13) is named as a source, not a PSRB.
- S9 commentary not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:16: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0104 (P1); built by tools/bm_build.py.
