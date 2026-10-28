---
id: std:doc:qaa-forensic-science-2022-benchmarks
title: "Subject Benchmark Statement Forensic Science"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100388", label: "forensic science", basis: "stated" }
  - { scheme: "cah", code: "CAH07-04-02", label: "forensic and archaeological sciences", basis: "stated" }
  - { scheme: "cah", code: "CAH07-04", label: "general, applied and forensic sciences", basis: "stated" }
  - { scheme: "hecos", code: "100386", label: "forensic biology", basis: "stated" }
  - { scheme: "hecos", code: "100385", label: "computer forensics", basis: "inferred" }
  - { scheme: "hecos", code: "101222", label: "crime scene investigation", basis: "inferred" }
edition: "March 2022"
published: 2022-03
status: current
supersedes: "the earlier Forensic Science statement (the back matter lists a 2012 advisory group and calls this the second edition; the front matter names key changes from the previous statement)"
heldText: { method: sha256-bytes, raw: 932e6c162d62defdec756fe02cf529ae2fdf2d510a5fcd02adcbc60890320c7d, normalised: b4b01a153a4eea6921a7e4a2fca9a3e7a734bbdefa605bdb1d1d011d0e43c6fe }
heldTextStan: { method: sha256-stan, raw: 932e6c162d62defdec756fe02cf529ae2fdf2d510a5fcd02adcbc60890320c7d, normalised: 5a4137d3ad8d1379d40323c9cff21e68a1abbfac383cee9858d61bbc1eb2410d }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, the 2022 revisions with cross-cutting themes (second edition of this subject)"
awardsCovered: ["bachelor's with honours", "master's", "integrated master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in its text"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0107 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:33"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Forensic Science (QAA, March 2022)

> Run 0107, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2022-forensic-science-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a Forensic Science graduate should know, understand and be able to do at the end of an honours degree, and at master's and integrated master's level: course aims, outcome lists for knowledge and skills, and benchmark standards at three rungs (threshold, typical, excellent), each split into generic standards and area standards for scene investigation, laboratory analysis and digital forensics, with a separate master's list. Reach for it when designing, reviewing or describing a forensic science course or its outcomes. It is not a curriculum, not the Chartered Society of Forensic Sciences' accreditation standard and not a regulatory requirement.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2022 with a foreword from the Forensic Science Regulator, the statement defines forensic science as science serving the law and organises the subject round three integrated components: scene investigation, laboratory analysis, and the interpretation, evaluation and presentation of evidence. It sets out course aims (honours and master's), distinctive features (accessibility, progression, flexibility, employer partnership, monitoring), content in the underpinning sciences, digital forensics and law, skills lists with master's additions, and benchmark standards at threshold (3rd), typical (2:2 or 2:1) and excellent (1st) for honours, plus one master's list. It carries the cross-cutting themes of equality, diversity and inclusion, accessibility, sustainability and enterprise; it cites the FHEQ and FQHEIS levels and Annex D, and names the Chartered Society of Forensic Sciences and the Forensic Science Regulator.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Forensic Science"
edition: "March 2022"
dates:
  published: 2022-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement; in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of the quality requirements in Northern Ireland (D1, front matter: Relationship to legislation and regulation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2022", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what can be expected of a Forensic Science graduate at the end of an honours degree, a master's degree or an integrated master's degree, and the nature of courses in the subject, including the forensic parts of courses based in other subjects (D1, front matter: About this Statement; 1.1; 1.2)"
appliesTo:
  awards: ["bachelor's with honours", "master's", "integrated master's"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This Statement sets out academic standards for courses at bachelor's degree with honours and master's degree levels (including integrated master's) in Forensic Science.\" (D1, 1.1)"
statedSubjects:
  - { name: "Forensic Science", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100388", label: "forensic science" }, { scheme: "cah", code: "CAH07-04-02", label: "forensic and archaeological sciences" }] }
  - { name: "Chemistry with Forensic Science", locator: "(D1, 1.2)", kind: "programme title", codes: [{ scheme: "hecos", code: "100417", label: "chemistry" }, { scheme: "hecos", code: "100388", label: "forensic science" }] }
  - { name: "Forensic Biology", locator: "(D1, 1.2)", kind: "programme title", codes: [{ scheme: "hecos", code: "100386", label: "forensic biology" }] }
  - { name: "digital forensics", locator: "(D1, 1.9; 3.19; 4.1; 4.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100385", label: "computer forensics" }] }
  - { name: "scene investigation", locator: "(D1, 1.14; 1.15; 3.11; 4.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "101222", label: "crime scene investigation" }] }
  - { name: "laboratory analysis", locator: "(D1, 1.14; 1.16; 3.12; 4.5)", kind: "specialism", codes: [] }
  - { name: "joint honours", locator: "(D1, 2.6)", kind: "programme title", codes: [{ scheme: "hecos", code: "100388", label: "forensic science" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Forensic Science degree", gloss: "scope: honours, master's and integrated master's courses; the working definition is in 1.3" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Forensic Science degree", gloss: "also covers the forensic parts of courses based in other benchmarked subjects; even-handed across the investigative process" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "forensic science as science in the service of law; differences between jurisdictions; the UK aim of ISO accreditation for scene, examination and reporting by 2025" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "testimony resting on sound science; the growth of degrees; accreditation by the professional society; equity of opportunity (S4)" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes of a Forensic Science degree", gloss: "a broad science degree with a vocational focus on investigation and justice" }
  - { number: "1.6", order: 8, componentType: stem, parent: "section 1", heading: "Purposes of a Forensic Science degree", gloss: "eighteen aims a course should pursue (S4, one record per item)" }
  - { number: "1.7", order: 9, componentType: stem, parent: "section 1", heading: "Purposes of a Forensic Science degree", gloss: "seven further aims for master's courses (S4)" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes of a Forensic Science degree", gloss: "courses to match the national qualification descriptors (S4); QAA's guidance on master's degrees" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Forensic Science degree", gloss: "most courses are laboratory-based analytical science; others lean towards digital forensics or investigation" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Forensic Science degree", gloss: "employers: justice-system bodies and forensic science providers; wider science, quality and communication roles" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Forensic Science degree", gloss: "a regulated field: quality standards, validation, law, codes; awareness of bias and ethics" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Forensic Science degree", gloss: "practitioners need relevant law and procedure, civil and criminal, in the UK and abroad" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Forensic Science degree", gloss: "multidisciplinary grounding in chemistry, biology, physics, mathematics and statistics" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Forensic Science degree", gloss: "three integrated components: scene, laboratory, and interpretation and presentation" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Forensic Science degree", gloss: "scene investigation read broadly: physical and digital scenes, safety, contamination, civil and coroner work, fieldwork" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Forensic Science degree", gloss: "laboratory work read broadly: chemical, biological, physical and digital examination; safety; many kinds of laboratory" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Forensic Science degree", gloss: "interpreting and evaluating evidence; what a report must be (S4); evidence and potential evidence" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Forensic Science degree", gloss: "techniques change fast; practitioners keep up with research" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion (EDI)", gloss: "the Equality Act 2010 and the equality duty; a shared responsibility for equal opportunity (S4)" }
  - { number: "1.20", order: 22, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion (EDI)", gloss: "reflective questions on equality in courses (not statements)" }
  - { number: "1.21", order: 23, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion (EDI)", gloss: "commitment to equality and the Act's three aims (not statements)" }
  - { number: "1.22", order: 24, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion (EDI)", gloss: "practices an equality review may cover (not statements)" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "education for sustainable development defined and embedded; lifelong learning; staff equipped (S4)" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainable development read through the Advance HE and QAA guidance (S4)" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship", gloss: "enterprise education; ambitious enterprise activities (S4)" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship", gloss: "entrepreneurship education beyond employment" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship", gloss: "enterprise thinking; spotting openings for business or process improvement (S4)" }
  - { number: "2.1", order: 31, componentType: paragraph, parent: "section 2", heading: "Distinctive features of a Forensic Science degree", gloss: "curriculum aligned to outcomes and employers, renewed with research and partners (S4)" }
  - { number: "2.2", order: 32, componentType: stem, parent: "section 2", heading: "Accessibility", gloss: "accessibility across the course, with examples of varied delivery (S4)" }
  - { number: "2.3", order: 33, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "digital accessibility (S4)" }
  - { number: "2.4", order: 34, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "the UK frameworks and their numbered levels" }
  - { number: "2.5", order: 35, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "honours at FHEQ 6 and FQHEIS 10; yearly progress towards the threshold; second-class graduates ready for postgraduate study" }
  - { number: "2.6", order: 36, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint honours students reach the core skills (S4)" }
  - { number: "2.7", order: 37, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's at FHEQ 7 and FQHEIS 11, and its length" }
  - { number: "2.8", order: 38, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards; four-year honours in Scotland" }
  - { number: "2.9", order: 39, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible study modes, blended and HyFlex delivery (S4)" }
  - { number: "2.10", order: 40, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "support plans and contingency for a change of delivery (S4)" }
  - { number: "2.11", order: 41, componentType: paragraph, parent: "section 2", heading: "Partnership and employer engagement", gloss: "partnerships with employers (S4)" }
  - { number: "2.12", order: 42, componentType: paragraph, parent: "section 2", heading: "Partnership and employer engagement", gloss: "research partnerships with organisations" }
  - { number: "2.13", order: 43, componentType: practice, parent: "section 2", heading: "Partnership and employer engagement", gloss: "placements need a programme of learning (S4); attributes a placement asks for (not statements)" }
  - { number: "2.14", order: 44, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review against external reference points (S4)" }
  - { number: "2.15", order: 45, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "working with examiners, students, partners and professional bodies (S4)" }
  - { number: "2.16", order: 46, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review (S4)" }
  - { number: "2.17", order: 47, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examining" }
  - { number: "2.18", order: 48, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "professional accreditation; monitoring that involves stakeholders (S4)" }
  - { number: "3.1", order: 50, componentType: paragraph, parent: "section 3", heading: "Content, structure and delivery", gloss: "the professional society's accreditation as a source of curriculum standards" }
  - { number: "3.2", order: 51, componentType: area, parent: "section 3", heading: "Content, structure and delivery", gloss: "core and optional curriculum areas" }
  - { number: "3.3", order: 52, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching and learning methods (S4)" }
  - { number: "3.4", order: 53, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "practical classes (S4)" }
  - { number: "3.5", order: 54, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "research experience at master's level (S4)" }
  - { number: "3.6", order: 55, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "design for outcomes; staff kept current; research-led content (S4)" }
  - { number: "3.7", order: 56, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "delivery modes; student-centred, active learning (S4)" }
  - { number: "3.8", order: 57, componentType: stem, parent: "section 3", heading: "Knowledge and understanding", gloss: "knowledge across the whole process from scene to court (S4, four items)" }
  - { number: "3.9", order: 58, componentType: paragraph, parent: "section 3", heading: "Knowledge and understanding", gloss: "justice and legal systems (S4)" }
  - { number: "3.10", order: 59, componentType: paragraph, parent: "section 3", heading: "Knowledge and understanding", gloss: "all three components as a minimum (S4)" }
  - { number: "3.11", order: 60, componentType: area, parent: "section 3", heading: "Knowledge and understanding", gloss: "scene investigation content (S4)" }
  - { number: "3.12", order: 61, componentType: area, parent: "section 3", heading: "Knowledge and understanding", gloss: "laboratory examination and analysis content (S4)" }
  - { number: "3.13", order: 62, componentType: area, parent: "section 3", heading: "Knowledge and understanding", gloss: "interpretation, evaluation and presentation content (S4)" }
  - { number: "3.14", order: 63, componentType: area, parent: "section 3", heading: "Knowledge and understanding", gloss: "the underpinning sciences (S4)" }
  - { number: "3.15", order: 64, componentType: area, parent: "section 3", heading: "Knowledge and understanding", gloss: "chemistry (S4)" }
  - { number: "3.16", order: 65, componentType: area, parent: "section 3", heading: "Knowledge and understanding", gloss: "biology (S4)" }
  - { number: "3.17", order: 66, componentType: area, parent: "section 3", heading: "Knowledge and understanding", gloss: "physics (S4)" }
  - { number: "3.18", order: 67, componentType: area, parent: "section 3", heading: "Knowledge and understanding", gloss: "mathematics and statistics (S4)" }
  - { number: "3.19", order: 68, componentType: area, parent: "section 3", heading: "Knowledge and understanding", gloss: "digital forensics (S4)" }
  - { number: "3.20", order: 69, componentType: area, parent: "section 3", heading: "Knowledge and understanding", gloss: "law (S4)" }
  - { number: "3.21", order: 70, componentType: paragraph, parent: "section 3", heading: "Skills and employability", gloss: "four groups of skills: scientific, forensic, generic and ethical" }
  - { number: "3.22", order: 71, componentType: stem, parent: "section 3", heading: "Scientific, laboratory and research skills", gloss: "scientific, laboratory and research skills (S4, seven items)" }
  - { number: "3.23", order: 72, componentType: stem, parent: "section 3", heading: "Scientific, laboratory and research skills", gloss: "master's additions to those skills (S4, four items)" }
  - { number: "3.24", order: 73, componentType: stem, parent: "section 3", heading: "Forensic science skills", gloss: "forensic science skills (S4, ten items)" }
  - { number: "3.25", order: 74, componentType: stem, parent: "section 3", heading: "Forensic science skills", gloss: "master's additions to those skills (S4, three items)" }
  - { number: "3.26", order: 75, componentType: stem, parent: "section 3", heading: "Generic graduate skills", gloss: "generic graduate skills (S4, eight items)" }
  - { number: "3.27", order: 76, componentType: stem, parent: "section 3", heading: "Generic graduate skills", gloss: "master's additions to those skills (S4, four items)" }
  - { number: "3.28", order: 77, componentType: stem, parent: "section 3", heading: "Ethical behaviour", gloss: "ethical behaviour (S4, stem and six items)" }
  - { number: "3.29", order: 78, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "varied assessment; reasonable adjustments (S4); kinds of assessment (not statements)" }
  - { number: "3.30", order: 79, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "what assessment tests (S4)" }
  - { number: "3.31", order: 80, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "briefs, criteria and inclusive design of assessment (S4)" }
  - { number: "3.32", order: 81, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "feedback mechanisms (not statements)" }
  - { number: "3.33", order: 82, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "prompt feedback; action plans (S4)" }
  - { number: "4.1", order: 84, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "two groups of standards: generic, and specific to three areas" }
  - { number: "4.2", order: 85, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the three rungs; the threshold is reached by every honours graduate; Annex D (S4)" }
  - { number: "4.3", order: 86, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the master's standard comes at the end" }
  - { number: "4.4", order: 87, componentType: stem, parent: "section 4", heading: "Threshold level (3rd class)", gloss: "threshold rung, generic standards (23 items)" }
  - { number: "4.5", order: 88, componentType: stem, parent: "section 4", heading: "Threshold level (3rd class)", gloss: "threshold rung, area standards (9 items)" }
  - { number: "4.6", order: 89, componentType: stem, parent: "section 4", heading: "Typical level (2:2 or 2:1)", gloss: "typical rung, generic standards (23 items)" }
  - { number: "4.7", order: 90, componentType: stem, parent: "section 4", heading: "Typical level (2:2 or 2:1)", gloss: "typical rung, area standards (9 items)" }
  - { number: "4.8", order: 91, componentType: stem, parent: "section 4", heading: "Excellent level (1st class)", gloss: "excellent rung, generic standards (23 items)" }
  - { number: "4.9", order: 92, componentType: stem, parent: "section 4", heading: "Excellent level (1st class)", gloss: "excellent rung, area standards (9 items)" }
  - { number: "4.10", order: 93, componentType: paragraph, parent: "section 4", heading: "Master's degrees (including integrated master's)", gloss: "integrated master's: at least typical honours, then master's outcomes (S4)" }
  - { number: "4.11", order: 94, componentType: stem, parent: "section 4", heading: "Master's degrees (including integrated master's)", gloss: "master's standards (10 items)" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Forensic Science degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Forensic Science degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "none", heading: "Foreword from the Forensic Science Regulator", kind: "other: front matter, read for SB1 and SB5" }
  - { number: "1, 2, 3, 4", heading: "section heading lines", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for SB6 and D3" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for Forensic Science", kind: "other: back matter, read for S8 (second edition; 2012 group)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 221 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/forensic-science-2022/1.4
  locator: { number: "1.4", headingPath: ["Context and purposes of a Forensic Science degree", "Context"] }
  span: { start: 12881, end: 14319 }
  source: "1.4 Over the past 20 years there has been an increasing realisation that all forensic testimony presented to the court needs to be underpinned by sound, peer-reviewed science (National Research Council, 2009; President's Council of Advisors on Science and Technology, 2016; House of Lords Science and Technology Select Committee, 2019). Over this same period, many universities both in the UK and in other countries have developed and delivered degree courses encompassing forensic science and its associated sub- disciplines. Such courses have appealed strongly to potential students looking for a science degree within a motivating and purposeful context and have provided employers, working within the criminal justice system and beyond, with a pool of potential graduate employees. To ensure degrees are fit for purpose within the professional context, the Educational Accreditation scheme set up by the Chartered Society of Forensic Sciences continues to support most higher education providers in the UK and some overseas with ongoing accreditation and surveillance activities. This scheme ensures productive close interaction between the profession, higher education providers and their students. Furthermore, the importance of equity of opportunity through inclusive practices is established within the field and should be supported and promoted by higher education institutions through accessible programmes and positive actions."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "higher education institutions teaching the subject"
  addressee: provider
  verbs: ["have", "select", "support", "provided", "reviewed", "underpinned"]
  about: "equity of opportunity through inclusive practice"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Forensic testimony needs to rest on sound, peer-reviewed science; forensic degrees have spread in the UK and abroad; the professional society's accreditation scheme covers most UK courses; and institutions should support and promote equity of opportunity through accessible courses and positive action."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b1
  locator: { number: "1.6.b1", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 14661, end: 14703 }
  source: "develop an enthusiasm for forensic science"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["develop"]
  about: "enthusiasm for the subject"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students build an enthusiasm for forensic science."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b2
  locator: { number: "1.6.b2", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 14706, end: 14775 }
  source: "have an intellectually stimulating and beneficial learning experience"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["have"]
  about: "a stimulating, worthwhile learning experience"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students have learning that stretches them intellectually and does them good."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b3
  locator: { number: "1.6.b3", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 14778, end: 15016 }
  source: "acquire underpinning scientific knowledge and skills of direct relevance to competence as a practitioner in forensic science, and to those organisations concerned principally with the collection or analysis of physical or digital evidence"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["acquire"]
  about: "science underpinning practitioner competence"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students gain the scientific knowledge and skills that competent forensic practice rests on, useful also to bodies that gather or analyse physical or digital evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b4
  locator: { number: "1.6.b4", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 15019, end: 15302 }
  source: "develop a sound knowledge of science and of laboratory and other transferable skills, which are of value not only within the forensic science profession, but also to businesses and organisations where analytical science, digital content or quality assurance underpin their activities"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["develop"]
  about: "sound science and transferable laboratory skills"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students gain a sound grounding in science and laboratory and transferable skills valued in forensic work and in any organisation built on analysis, digital content or quality assurance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b5
  locator: { number: "1.6.b5", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 15305, end: 15555 }
  source: "acquire an understanding of the purposes of and requirements for working within an ISO quality standards framework and of the need for high standards of professional and ethical behaviour at all times, with the aim of avoiding miscarriages of justice"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["acquire"]
  about: "quality standards and professional ethics"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students understand why ISO quality standards exist and what working under them involves, and why high professional and ethical standards matter at every moment if miscarriages of justice are to be avoided."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b6
  locator: { number: "1.6.b6", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 15558, end: 15702 }
  source: "acquire the communication skills required to present data, explain scientific arguments and justify outcomes to specialist and general audiences"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["acquire", "present", "justify"]
  about: "communicating science to varied audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students set out data, explain scientific reasoning and defend their conclusions to expert and lay audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b7
  locator: { number: "1.6.b7", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 15705, end: 16072 }
  source: "use independent learning at a level where they can enhance their professional development within the sector, build on knowledge and skills for their own and their potential employer's benefit, and to demonstrate initiative and flexibility with respect to changing needs and techniques; this may be achieved through a structured system of recorded personal development"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["demonstrate", "use", "respect"]
  about: "independent learning and professional development"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students learn independently, grow professionally, and show initiative and flexibility as needs and techniques change, perhaps by keeping a structured record of their personal development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b8
  locator: { number: "1.6.b8", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 16075, end: 16573 }
  source: "develop a clear understanding of the importance of the continuity of evidence from the (crime) scene to the court and beyond. Accepting that the value of findings at the laboratory are dependent on the knowledge and skill of those taking the appropriate samples at the scene to answer the questions relevant to the investigation. An awareness of the risks from contamination and cognitive bias at all stages in this process, together with effective mitigation strategies for avoidance and detection"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["develop"]
  about: "continuity of evidence, contamination and bias"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students understand how evidence stays continuous from scene to court and beyond, why laboratory findings depend on good sampling at the scene, and how to avoid and detect contamination and cognitive bias at each stage."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b9
  locator: { number: "1.6.b9", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 16576, end: 16949 }
  source: "become fa miliar with the justice system, including those requirements of the police, expert witness roles and the legal sector (such as record keeping, admissibility and disclosure) relevant to the procedures and practice of forensic science, including a knowledge of the different legal systems and their requirements relating to forensic science within the UK and beyond"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["become", "record"]
  about: "the justice system and its demands"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students become familiar with the justice system and what police, expert witnesses and lawyers need from forensic work (records, admissibility, disclosure), and with how legal systems differ in the UK and elsewhere."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b10
  locator: { number: "1.6.b10", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 16952, end: 17122 }
  source: "acquire problem-solving and research skills appropriate to degree-level study, with an appreciation of current and emerging research in forensic science and related areas"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["acquire"]
  about: "problem-solving, research and current research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students build problem-solving and research skills fit for degree study and keep aware of current and emerging forensic research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b11
  locator: { number: "1.6.b11", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 17125, end: 17312 }
  source: "recognise the relevance of sustainability, equality, diversity and inclusion and demonstrate a commitment to those values for forensic science both as an academic subject and a profession"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["demonstrate", "recognise"]
  about: "sustainability and inclusion as professional values"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students see why sustainability and equality, diversity and inclusion matter in forensic science, as a subject and as a profession, and commit to those values."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b12
  locator: { number: "1.6.b12", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 17315, end: 17497 }
  source: "develop a broad understanding of forensic opportunities and how these can support a forensic strategy, demonstrating impartial thought and investigative skills to progress an enquiry"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["develop", "support"]
  about: "forensic opportunities and strategy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students grasp the forensic opportunities in a case and how they serve a forensic strategy, thinking impartially and investigating so that an enquiry moves forward."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b13
  locator: { number: "1.6.b13", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 17500, end: 17665 }
  source: "develop an awareness of the digital forensic opportunities and how the different sub-disciplines of forensic science can maximise opportunities for forensic evidence"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["develop"]
  about: "digital forensic opportunities"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students see what digital forensics can offer and how the forensic specialisms together get the most from the evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b14
  locator: { number: "1.6.b14", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 17668, end: 17811 }
  source: "develop investigative skills, such as identifying relevant lines of enquiry, sources of evidence, artefacts, and the relationships between them"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["develop"]
  about: "investigative skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students build investigative skills, such as finding lines of enquiry, sources of evidence and artefacts and seeing how they connect."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b15
  locator: { number: "1.6.b15", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 17814, end: 17908 }
  source: "encourage an ability to critically review information, particularity the scientific literature"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["encourage", "review", "critically"]
  about: "critical review of information and literature"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students review information critically, published science above all."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b16
  locator: { number: "1.6.b16", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 17911, end: 18018 }
  source: "understand the scientific method, that is, the value of experimentation and gain ability to access findings"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["gain", "access", "understand"]
  about: "the scientific method"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students understand the scientific method and the worth of experiment, and judge findings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b17
  locator: { number: "1.6.b17", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 18021, end: 18192 }
  source: "gain an awareness of the relationship between the evidence recovered from the crime scene, the investigation process, the analysis of evidence and bringing a case to court"
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["gain"]
  about: "from scene to court"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students see how evidence from a scene, the investigation, the analysis and the court case link together."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.6.b18
  locator: { number: "1.6.b18", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 18198, end: 18314 }
  source: "gain an understanding of the duty to the court for forensic professionals, including the role of the expert witness."
  stem: "1.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["gain"]
  about: "duty to the court and the expert witness"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should aim to help students understand a forensic professional's duty to the court and what an expert witness does."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.7.b1
  locator: { number: "1.7.b1", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 18428, end: 18604 }
  source: "a deep knowledge and experience of examination and analytical techniques relevant to forensic science and their practical application within particular relevant specialisations"
  stem: "1.7"
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's courses and their students"
  addressee: both
  verbs: []
  about: "deep knowledge of techniques in a specialism"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also aim to help students gain deep knowledge and hands-on experience of forensic examination and analytical techniques and their use in chosen specialisms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.7.b2
  locator: { number: "1.7.b2", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 18607, end: 18690 }
  source: "a critical awareness of and engagement with current research methods and techniques"
  stem: "1.7"
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's courses and their students"
  addressee: both
  verbs: []
  about: "critical engagement with research methods"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also aim to help students engage critically with the research methods and techniques in use today."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.7.b3
  locator: { number: "1.7.b3", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 18693, end: 18845 }
  source: "the abilities and skills necessary to devise, plan, carry out and present an original, extended investigation or research project in an academic context"
  stem: "1.7"
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's courses and their students"
  addressee: both
  verbs: ["carry", "present", "plan", "devise"]
  about: "an extended original research project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also aim to help students conceive, plan, conduct and report a sizeable original research project in an academic setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.7.b4
  locator: { number: "1.7.b4", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 18848, end: 18985 }
  source: "a clear recognition of the constraints and opportunities of the current environment in which professional forensic science is carried out"
  stem: "1.7"
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's courses and their students"
  addressee: both
  verbs: []
  about: "the professional setting, its limits and openings"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also aim to help students see clearly what limits and what opens up professional forensic science today."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.7.b5
  locator: { number: "1.7.b5", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 18988, end: 19044 }
  source: "the ability to work within a quality standards framework"
  stem: "1.7"
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's courses and their students"
  addressee: both
  verbs: ["work"]
  about: "working to a quality standards framework"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also aim to help students work within a quality standards framework."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.7.b6
  locator: { number: "1.7.b6", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 19047, end: 19129 }
  source: "enhanced preparedness for entry to professional employment or doctoral-level study"
  stem: "1.7"
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's courses and their students"
  addressee: both
  verbs: []
  about: "readiness for employment or doctoral study"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also aim to help students be better prepared to enter professional work or doctoral study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.7.b7
  locator: { number: "1.7.b7", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 19132, end: 19214 }
  source: "the independent learning ability required for continuing professional development."
  stem: "1.7"
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's courses and their students"
  addressee: both
  verbs: []
  about: "independent learning for professional development"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also aim to help students keep learning on their own for continuing professional development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.8
  locator: { number: "1.8", headingPath: ["Context and purposes of a Forensic Science degree", "Purposes of a Forensic Science degree"] }
  span: { start: 19215, end: 19444 }
  source: "1.8 All degree courses should accord with the qualification descriptions in national qualification frameworks. QAA has published additional guidance on different kinds of master's degrees , which may also be helpful to providers."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "all degree courses in the subject"
  addressee: provider
  verbs: ["accord"]
  about: "matching national qualification descriptors"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's", "integrated master's"]
  gradeOf: none
  paraphrase: "Every degree course should match the qualification descriptions in the national frameworks; QAA's guidance on kinds of master's degree may also help."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of a Forensic Science degree", "Characteristics of a Forensic Science degree"] }
  span: { start: 24126, end: 24968 }
  source: "1.17 Interpretation and evaluation of evidence involves the reliable recording of evidential materials, experimentation, analysis and interpretation within the context of the case and data management. It also requires the clear and impartial presentation (written and oral) of the forensic examination and findings with an understanding of the significance of its outcomes within a legal context, including uncertainties. A report or witness statement must be robust, transparent, logical and unbiased and should distinguish between factual and expert reporting. It should be noted that admissible 'evidence' can only be decided by the courts and therefore, up to that point in the process, the items and findings are only 'potential evidence'. For the purpose of this document, the term evidence implies both evidence and potential evidence."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "anyone reporting forensic findings, students included"
  addressee: learner
  verbs: ["report", "distinguish"]
  about: "standards for forensic reports and witness statements"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Interpreting and evaluating evidence means reliable recording, experiment, analysis and interpretation within the case, and clear, impartial written and oral presentation that explains significance and uncertainty; reports and witness statements must be robust, transparent, logical and free of bias, and should separate fact from expert opinion. Only a court decides what counts as evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.19
  locator: { number: "1.19", headingPath: ["Context and purposes of a Forensic Science degree", "Equality, diversity and inclusion (EDI)"] }
  span: { start: 25391, end: 26310 }
  source: "1.19 This Subject Benchmark Statement is to be interpreted in the context of the Equality Act 2010 and seeks to embed equality, diversity and inclusivity across all educational practices within a Forensic Science course. The Equality Duty (section 149 of the Act) supports good decision-making by ensuring public bodies consider how different people will be affected by their activities, helping them to deliver policies and services which are efficient and effective, accessible to all and which meet different people's needs. In this section we pose some reflective questions, and set out aims and objectives which might help when reviewing and reflecting on course provision, to ensure everyone is treated equally with dignity and respect. All staff and students within Forensic Science courses have a responsibility to ensure equal opportunity for all regardless of background, ability, culture, gender or identity."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "Duty" read as must
  level: none
  appliesTo: "all staff and students on courses in the subject"
  addressee: both
  verbs: ["have", "deliver", "embed", "interpreted", "consider", "respect"]
  about: "a shared responsibility for equal opportunity"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The statement is to be read in the light of the Equality Act 2010 and its equality duty, and aims to embed equality, diversity and inclusion in all teaching; every member of staff and every student carries a responsibility to secure equal opportunity whatever a person's background, ability, culture, gender or identity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of a Forensic Science degree", "Sustainability"] }
  span: { start: 28899, end: 30166 }
  source: "1.23 Education for Sustainable Development (ESD) is defined as 'the process of creating curriculum structures and subject-relevant content to support sustainable development' by aligning teaching practices, where possible, to the UN Sustainable Development Goals. ESD should be embedded in teaching and learning practices to ensure students are aware of social, economic and ecological well-being factors, now and in the future. ESD can be used to empower students and staff to change the way they think and work towards a sustainable future using transdisciplinary, holistic and values-driven relevant material. For Forensic Science students this includes developing practices for lifelong learning through engagement with continual professional development to ensure their future practitioner skills and knowledge base are current. Staff should be equipped with tools and inspiration to mainstream sustainable development across a student's learning environment. Critical thinking, problem-solving skills and competencies related to ESD should be embedded in a student's learning process to ensure they can manage complexities such as uncertainty and risk. This invites the use of informed student-centred and inquiry-based teaching approaches within the programme."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and their staff"
  addressee: provider
  verbs: ["developing", "use", "manage", "work", "support", "embedded"]
  about: "embedding education for sustainable development"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Education for sustainable development should be built into teaching and learning so students grasp social, economic and ecological well-being now and later; for forensic students it includes lifelong learning through professional development; staff should be equipped to mainstream it; and critical thinking, problem-solving and related competencies should be embedded so students can handle uncertainty and risk."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of a Forensic Science degree", "Sustainability"] }
  span: { start: 30167, end: 30286 }
  source: "1.24 ESD should be interpreted in the context of the Advance HE and QAA Education for Sustainable Development Guidance."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["interpreted"]
  about: "reading sustainability through the national guidance"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Education for sustainable development should be read through the Advance HE and QAA guidance on it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/1.25
  locator: { number: "1.25", headingPath: ["Context and purposes of a Forensic Science degree", "Enterprise and entrepreneurship"] }
  span: { start: 30319, end: 31123 }
  source: "1.25 Education activities in enterprise and entrepreneurship may also contribute to Forensic Science courses by supporting behaviours, attributes and competencies that are likely to have a significant impact on the individual student in terms of successful careers. Enterprise activities should be ambitious and require students to develop creative, innovative, resilient and critical approaches to provide solutions, generate ideas and communicate issues aligned with forensic practice. Through entrepreneurship activities students learn to organise and manage business risk and associated business profit. Such activities prepare students for changing environments, and provide enhanced impact through placements and activities that build links between academic institutions and external organisations."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "enterprise activities in courses"
  addressee: provider
  verbs: ["develop", "have", "organise", "communicate", "prepare", "manage"]
  about: "ambitious enterprise activities"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Enterprise and entrepreneurship education can add to forensic courses; enterprise activities should be ambitious and should require students to be creative, innovative, resilient and critical in solving problems, generating ideas and communicating issues tied to forensic practice, with placements and partnerships adding to their effect."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/1.27
  locator: { number: "1.27", headingPath: ["Context and purposes of a Forensic Science degree", "Enterprise and entrepreneurship"] }
  span: { start: 31356, end: 31767 }
  source: "1.27 Enterprise thinking and entrepreneurship will drive the future of forensic science. Students should be able to identify opportunities for business development or process improvement whether this be through studies, partnerships or placements. The grounding of entrepreneurial thought is in making decisions, acting on ideas and individual creativity to support wider commercial or organisational interests."
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["identify", "support", "drive"]
  about: "spotting openings for business or process improvement"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Enterprise and entrepreneurial thinking will shape where forensic science goes; students should be able to spot chances to develop a business or improve a process, through study, partnerships or placements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of a Forensic Science degree", ""] }
  span: { start: 31824, end: 32605 }
  source: "2.1 The course and thus its curriculum should be designed to enable students to demonstrate the attainment of the stated learning outcomes of the course, and the assessment strategies should align to these outcomes. The course outcomes and content (section 3) should reflect the contemporary knowledge and skills required by relevant graduate employers. Therefore, course design should be frequently updated with developments in pedagogical and scientific research and collaboration or partnership with appropriate key stakeholders - for example, with forensic science providers, police forces, other investigative agencies and the judiciary. Students should be supported to progressively acquire subject knowledge and skills, gradually advancing towards more independent learning."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["demonstrate", "acquire", "design", "reflect", "designed", "updated"]
  about: "curriculum aligned to outcomes, employers and research"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The curriculum should let students show they have met the course's stated outcomes, with assessment aligned to them; outcomes and content should reflect what graduate employers need now; design should be refreshed often with pedagogical and scientific research and with partners such as forensic providers, police and the judiciary; and students should be supported to build knowledge and skills step by step towards independence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/2.2
  locator: { number: "2.2", headingPath: ["Distinctive features of a Forensic Science degree", "Accessibility"] }
  span: { start: 32620, end: 33401 }
  source: "2.2 Accessibility considerations should apply to all aspects of the course. This relates to physical access but also includes cultural awareness, language and sensitivity to victims of crime. Accessibility should consider whether all aspects of the course can be understood or used by people however it is encountered. This includes the recognition for curricula, tuition and assessment being accessible and reasonable adjustments being put in place. To ensure students who struggle with particular forms of teaching and learning scenarios are not disadvantaged, methods used within an individual course should be as varied as possible. There are many forms of delivery, too many to include all, but some examples are likely to comprise an appropriate combination of the following:"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["apply", "include", "includes", "consider", "access"]
  about: "accessibility across the whole course"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Accessibility should cover every part of the course, from physical access to awareness of culture and language, and sensitivity towards victims of crime; curricula, tuition and assessment should be accessible with reasonable adjustments in place; and teaching methods should vary as widely as possible so that no student is put at a disadvantage."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of a Forensic Science degree", "Accessibility"] }
  span: { start: 34151, end: 34572 }
  source: "2.3 Digital accessibility is the inclusive practice of ensuring that all people can equally access and navigate digital information and platforms, such as websites, electronic documents and mobile phone applications, irrespective of physical, situational or socio- economical impairments (W3C , 2018). The content, which will include text, images and sound, should be accessible and comprehensible without discrimination."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["include", "access"]
  about: "digital accessibility of course content"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Digital accessibility means everyone can reach and use digital information and platforms equally, whatever their impairment; course content in text, image and sound should be accessible and understandable without discrimination."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of a Forensic Science degree", "Progression"] }
  span: { start: 35834, end: 36153 }
  source: "2.6 Joint honours undergraduates will achieve core elements of the specific and generic skills for the subject, and will add others according to the subjects covered in joint courses. Additionally, they may explore the overlap between their two subject areas, creating further opportunities for interdisciplinary study."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint honours students"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "joint honours: the core skills of the subject"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Joint honours students will achieve the core subject-specific and generic skills of forensic science, add others from their second subject, and may explore where the two overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of a Forensic Science degree", "Flexibility"] }
  span: { start: 36806, end: 37624 }
  source: "2.9 Degree providers are encouraged to consider a range of learning modes to offer flexibility within their courses with the aim of meeting diverse learner needs including assisted learning including communication skills. Where possible, full-time, part-time and distanced learning options should be offered and within each of these modes, there are a variety of options. To enable wider participation, providers might consider a combination of classroom-based, online and employer-based learning or a blended approach to all of these such as the HyFlex (hybrid-flexible) delivery approach, blending online and on-site participation. Not only does this increase inclusivity and equity, but it empowers students by providing choices, where possible and appropriate, relating to the how, what, when and where they learn."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["meeting", "offered", "encouraged", "consider", "enable", "learn"]
  about: "flexible modes of study"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Providers are encouraged to offer a range of learning modes; where possible full-time, part-time and distance options should be offered, perhaps blending classroom, online and employer-based learning such as HyFlex, to widen participation and give students choice over how, what, when and where they learn."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of a Forensic Science degree", "Flexibility"] }
  span: { start: 37625, end: 38322 }
  source: "2.10 Flexibility should also encompass a plan of action for those with protected characteristics and, where there is a change in a student's circumstances, to support them to complete their course. In addition, it is important that providers have a plan in place for the sudden need to change content delivery mode, such as the need to move entirely to online and digital delivery to ensure continuation of learning. This flexibility may include altering the practical/theory content and may even involve the practical being concentrated into blocks. Certain aspects, particularly related to practical skills, may need to be considered in a particular way to ensure the required skill development."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["have", "plan", "support", "include"]
  about: "support plans and delivery contingency"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Flexibility should include a plan to support students with protected characteristics, or whose circumstances change, to finish the course, and a plan for sudden changes of delivery such as moving wholly online; practical teaching may then be reshaped, for example into blocks."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of a Forensic Science degree", "Partnership and employer engagement"] }
  span: { start: 38359, end: 39045 }
  source: "2.11 Degree providers should be encouraged to develop partnerships and engagement with forensic science employers (law enforcement agencies and private sector forensic service providers) and other wider organisations where degree activities can be related to the work environment. This will help prepare the students for the demands and expectations of the workplace while developing their workplace skills which are likely to include self- reliance, critical thinking, interpersonal, problem-solving and teamworking skills. For\n\n12\nemployers this helps resolve workplace skills shortages, grows a pipeline for recruitment, improves recruitment success and increases retention of staff."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["develop", "developing", "prepare", "work", "include", "encouraged"]
  about: "partnerships with forensic employers"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Providers should be encouraged to build partnerships with forensic employers and wider organisations so that course activities connect with real work, preparing students for the workplace and its skills while helping employers recruit and keep staff."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/2.13
  locator: { number: "2.13", headingPath: ["Distinctive features of a Forensic Science degree", "Partnership and employer engagement"] }
  span: { start: 39512, end: 39939 }
  source: "2.13 If students choose a work placement opportunity as part of their degree this should have a clear programme of learning. The typical activities a student may undertake as part of their placement could be quality assurance activities, data analysis, basic examination processes, administration of evidence and specific project work. In order to successfully secure a work placement, the student would likely need to display:"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "work placements taken as part of a course"
  addressee: both
  verbs: ["have", "work", "undertake", "display"]
  about: "a clear programme of learning on placement"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A work placement that a student chooses should have a clear programme of learning; typical tasks include quality assurance, data analysis, basic examinations, administering evidence and project work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of a Forensic Science degree", "Monitoring and review"] }
  span: { start: 40746, end: 41484 }
  source: "2.14 A major feature of academic quality assurance and enhancement at a higher education institution is having in place monitoring and regular review processes for the courses it delivers. Degree-awarding bodies routinely collect and analyse information and undertake periodic course review according to their own needs. They will draw on a range of external reference points, including this Statement, to ensure that their provision aligns with sector norms. Monitoring and evaluation is a periodic assessment of a course, conducted internally or by external independent evaluators. Evaluation uses information from both current and historic monitoring to develop an understanding of student achievement or inform future course planning."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["develop", "review", "undertake", "draw", "analyse"]
  about: "external reference points in review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Monitoring and periodic review are central to quality assurance; degree-awarding bodies will draw on external reference points, this statement among them, to keep their provision in line with sector norms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/2.15
  locator: { number: "2.15", headingPath: ["Distinctive features of a Forensic Science degree", "Monitoring and review"] }
  span: { start: 41485, end: 41845 }
  source: "2.15 Forensic Science degrees will work collaboratively with external examiners, student cohorts and external partners to enhance the educational experience. Close alignment with external bodies such as, but not limited to, the Chartered Society of Forensic Sciences and the Forensic Science Regulator ensure that the content as set out below remains relevant."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["work", "collaboratively"]
  about: "collaboration with examiners, students and professional bodies"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Forensic science degrees will work with external examiners, students and outside partners to improve the learning experience; close links with bodies such as the Forensic Science Regulator and the Chartered Society of Forensic Sciences keep content relevant."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/2.16
  locator: { number: "2.16", headingPath: ["Distinctive features of a Forensic Science degree", "Monitoring and review"] }
  span: { start: 41846, end: 42157 }
  source: "2.16 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["use", "gain", "review"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Providers will use external reviewers in periodic review to bring an outside view of proposed changes, confirm threshold standards are met and check that content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/2.18
  locator: { number: "2.18", headingPath: ["Distinctive features of a Forensic Science degree", "Monitoring and review"] }
  span: { start: 42957, end: 43461 }
  source: "2.18 Forensic science has professional and vocational outcomes that may also require evaluation and accreditation from professional and regulatory bodies as outlined above. These are usually done through a combination of site visits and desk-based reviews. Monitoring and evaluation processes should identify appropriate stakeholders and ensure dissemination of findings with regards to learning, teaching and assessment at various levels to reflect changes in cohorts, experience and pedagogic practice."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["identify", "reflect"]
  about: "stakeholders and findings in monitoring"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Forensic science's professional outcomes may also need evaluation and accreditation by professional and regulatory bodies, usually through visits and desk review; monitoring and evaluation should identify the right stakeholders and share findings on learning, teaching and assessment so courses respond to changing cohorts, experience and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 44490, end: 44720 }
  source: "3.3 Utilising a combination of teaching and learning practices (pedagogy and andragogy) should enable learners to develop their knowledge and understanding along with academic and professional skills. Teaching methods may include:"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["develop", "include", "enable"]
  about: "a mix of teaching and learning practices"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A mix of teaching and learning practices should let learners grow in knowledge, understanding and academic and professional skill; methods may run from lectures and practicals to simulations, fieldwork, problem-based learning and learning at work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 45181, end: 45745 }
  source: "3.4 Practical classes, for example in laboratories and/or computer rooms, should support the taught curriculum, and in particular allow the student to acquire transferable technical and practical skills. This will include familiarity with a variety of forensic experimental methods and their scientific basis, and with methods to deal with uncertainties in their outcomes, such as data handling and statistics to carry out probabilistic inference (expanded upon in paragraph 3.19). The contemporaneous preparation of records and reports is likely to be emphasised."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["acquire", "carry", "support", "include", "allow", "deal"]
  about: "practical classes and their purpose"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Practicals in laboratories or computer rooms should back up the taught curriculum and build transferable technical and practical skills, including forensic experimental methods, their scientific basis and ways of handling uncertainty through data handling and statistics; contemporaneous records and reports are likely to be stressed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/3.5
  locator: { number: "3.5", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 45746, end: 46014 }
  source: "3.5 At master's level, experience of research methods and of reading and interpreting research publications is expected, as is extended project work, including the preparation of an independent original report, for example, in the style of a journal article or thesis."
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: ["work", "report"]
  about: "research methods and an extended project at master's level"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At master's level students are expected to gain research-methods experience, read and interpret published research, and to complete extended project work ending in an independent original report, such as a journal-style article or thesis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.6
  locator: { number: "3.6", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 46015, end: 47126 }
  source: "3.6 As previously outlined in section 2, the programme of teaching and learning should be designed to enable students to demonstrate the attainment of the stated learning outcomes of the course using assessment strategies that align to these outcomes and the skills required by relevant graduate employers. As a result, the teaching and learning strategies suggested above should be reviewed and updated with advances in pedagogy,\n\n15\nandragogy and educational and professional information technology, although the balance between different methods may vary between institutions and courses. Teaching staff will need to maintain their knowledge of forensic science to remain current by suitable and regular continuous professional development engagement. Subject-specific content should also be underpinned and updated based on the latest research, innovation, practice and regulation within the sector. Overarching considerations will be the demonstrable acquisition by the student of a clear appreciation of the scientific approach, and of the knowledge and skills needed for the practice of forensic science."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["demonstrate", "designed", "reviewed", "updated", "maintain", "underpinned"]
  about: "design for outcomes; current staff and content"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Teaching and learning should be designed so students can show they meet the stated outcomes, with aligned assessment and the skills employers need; strategies should be reviewed as pedagogy and technology move on; teaching staff will need regular professional development to stay current; and subject content should rest on the latest research, practice and regulation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/3.7
  locator: { number: "3.7", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 47127, end: 47700 }
  source: "3.7 Depending on the course type, learning outcomes or learner demographics, the taught curriculum may be delivered using synchronous (live) and/or asynchronous approaches, on campus and/or from a distance (remote). Wherever possible, sessions should be designed to be student-centred and utilise active learning strategies to promote inclusivity, application and engagement. Design and delivery should also consider the use of technology, hardware and/or software, to enhance the learning experience and provide further opportunities to apply knowledge in problem-solving."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["use", "utilise", "apply", "design", "promote", "designed"]
  about: "student-centred, active delivery"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Delivery may be live or recorded, on campus or remote; wherever possible sessions should be student-centred and use active learning for inclusion, application and engagement, and design should consider technology that enriches learning and problem-solving."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/3.8.b1
  locator: { number: "3.8.b1", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 47898, end: 48076 }
  source: "an understanding of current ISO standards, legislation and Forensic Science Regulator Codes of Conduct and associated guidance, including impartiality and disclosure requirements"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["conduct"]
  about: "standards, law and the Regulator's codes"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Throughout the process from scene to court, students should work safely and show an understanding of current ISO standards, the law and the Forensic Science Regulator's codes and guidance, impartiality and disclosure included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.8.b2
  locator: { number: "3.8.b2", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 48079, end: 48224 }
  source: "familiarity with professional ethics, including respect for codes of practice and conduct, standards, rules and responsibilities (outlined above)"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["conduct", "respect"]
  about: "professional ethics and codes"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Throughout the process from scene to court, students should work safely and show familiarity with professional ethics: respect for the codes of practice and conduct, the standards and rules, and their responsibilities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.8.b3
  locator: { number: "3.8.b3", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 48227, end: 48377 }
  source: "knowledge and understanding of relevant types of cognitive bias, their consequences (including cumulative effects) and appropriate mitigation measures"
  stem: "3.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: []
  about: "cognitive bias and its mitigation"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Throughout the process from scene to court, students should work safely and show knowledge and understanding of the kinds of cognitive bias, what they lead to (cumulative effects included) and how to reduce them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.8.b4
  locator: { number: "3.8.b4", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 48380, end: 48529 }
  source: "an understanding of and ability to implement approaches such as Case Assessment and Interpretation in formulating and delivering a forensic strategy."
  stem: "3.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["implement"]
  about: "Case Assessment and Interpretation in forensic strategy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Throughout the process from scene to court, students should work safely and show an understanding of approaches such as Case Assessment and Interpretation and the ability to use them in building and delivering a forensic strategy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 48530, end: 49143 }
  source: "3.9 Students should also be expected to develop a knowledge of the criminal justice and legal systems within the UK and an appreciation of systems that operate globally in different jurisdictions. This should include an understanding of both the adversarial and inquisitorial approaches from the global perspective and, in particular, how forensic science and the role of the expert witness, including defence scientists operate within these systems. They should have an understanding of prevailing legal standards and legislation applicable to the recovery, storage, retention, analysis and disposal of evidence."
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop", "have", "include"]
  about: "criminal justice and legal systems"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should be expected to know the UK's criminal justice and legal systems and appreciate those elsewhere, including adversarial and inquisitorial approaches, how forensic science and expert witnesses (defence scientists among them) work within them, and the legal standards for recovering, storing, keeping, analysing and disposing of evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.10
  locator: { number: "3.10", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 49144, end: 49453 }
  source: "3.10 Within the three main themes of forensic science outlined in paragraph 1.14, different degree schemes may have different emphases, however, a basic knowledge of all three themes, appropriate to that degree, is a minimum expectation for all students. The content of these themes is expanded on as follows."
  stem: none
  statementType: expectation
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["have"]
  about: "basic knowledge of all three components"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses may weight the three components (scene investigation, laboratory analysis, and interpretation, evaluation and presentation) differently, but every student is expected, as a minimum, to have a basic knowledge of all three at a level fitting the degree."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.11
  locator: { number: "3.11", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 49454, end: 50394 }
  source: "3.11 Scene investigation encompasses knowledge of the principles and effective safe working practical application of the relevant techniques needed for the formulation of scene examination strategies which involve understanding the potential significance of various materials in a given context. This includes understanding the importance of the recognition, priority processing, recording, preservation, recovery, storage, scientific analysis and interpretation of evidence at the scene, including strategies for dealing with contamination issues throughout the process. Students will acquire, as appropriate, an understanding of the forensic principles and practices when using a range of imaging techniques, in particular (crime) scene photography together with a clear understanding of the responsibilities, roles\n\n16\nand liabilities of the individuals and agencies involved in a (crime) scene, and of information exchange between them."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["acquire", "includes"]
  about: "scene investigation: imaging, roles and information exchange"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Scene investigation covers the principles and safe practice of the techniques for planning scene examinations, from recognising, prioritising, recording and preserving evidence to recovering, storing and interpreting it and controlling contamination; students will gain, as their course requires, an understanding of imaging, scene photography above all, and of the roles, duties and liabilities of the people and agencies at a scene and how they share information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.12
  locator: { number: "3.12", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 50395, end: 51310 }
  source: "3.12 Laboratory examination and analysis requires competence in the selection and application of a range of methods used in the location, identification, recovery, examination, comparison (including mark comparison), extraction and scientific analysis of commonly encountered physical, chemical, biological and digital evidential materials, including appropriate storage practices, as appropriate. This is underpinned by safe working practices and knowledge of the theory, application and limitations of the principal laboratory methods used routinely in forensic science together with an understanding of the importance of validation, calibration and the use of accepted examination or analytical methods for all laboratory work, where appropriate. Students will also have a knowledge of the principles and application of control and reference samples, and the use of databases for the identification of materials."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["use", "have", "work", "underpinned"]
  about: "laboratory methods, control samples and databases"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Laboratory work needs competence in choosing and applying methods to find, identify, recover, examine, compare, extract and analyse common physical, chemical, biological and digital materials, with proper storage and safe practice, knowledge of each method's theory and limits, and attention to validation and calibration; students will also know the principles and use of control and reference samples and of databases for identifying materials."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.13
  locator: { number: "3.13", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 51311, end: 52472 }
  source: "3.13 Interpretation, evaluation and presentation of evidence encompasses the management and interpretation of the results from the examination of physical or digital evidence, in the context of casework. Fundamental to this is the understanding and application of accepted methods of interpretation and evaluation, in particular that of logical evaluation using likelihood ratio, and other appropriate statistical analysis, including the use of appropriate interpretive databases, together with an understanding of factors affecting the interpretation process that may contribute to uncertainty in the outcome and consequent expert opinion. Students will be able to interpret and assign conclusions to forensic findings and to distinguish between factual and expert reporting. They will be able to formulate expert opinion and have the knowledge and skills to write impartial, comprehensive and appropriate reports in a variety of formats and for a variety of audiences, including for both investigators and for the court. They will acquire the skills and expertise to convey and defend, both orally and in writing, a written report in the context of the court."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["acquire", "use", "have", "interpret", "formulate", "report"]
  about: "interpreting, reporting and defending findings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Interpretation, evaluation and presentation rest on accepted methods, logical evaluation by the likelihood ratio above all, suitable statistics and databases, and an understanding of what makes outcomes uncertain; students will be able to interpret findings and reach conclusions, keep factual apart from expert reporting, form expert opinion, write impartial and complete reports in formats fit for investigators and courts, and explain and defend a report in court, orally and in writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.14
  locator: { number: "3.14", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 52473, end: 53038 }
  source: "3.14 The three core components of forensic science above are underpinned by scientific knowledge and understanding drawn principally from chemistry, biology, physics, mathematics, computer science and law topics, but the list is not intended to be exhaustive and may include aspects of digital forensics. Again, different degree schemes may have different emphases, but a basic knowledge of these underpinning sciences appropriate to that degree course is expected. For courses in digital forensics, appropriate scientific and mathematical underpinning is expected."
  stem: none
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["have", "include", "underpinned"]
  about: "the underpinning sciences"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The three core components rest on science drawn mainly from chemistry, biology, physics, mathematics and computer science, and from law, the list being open; courses may weight these differently, but basic knowledge of the underpinning sciences fitting the course is expected, and digital forensics courses are expected to have suitable scientific and mathematical grounding."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 53039, end: 53529 }
  source: "3.15 In chemistry, students should be able to select, utilise and interpret data from appropriate analytical and microscopic techniques, to determine analytes in a sample, identify and compare materials and determine their composition within a forensic science context. The student should appreciate the underlying theoretical and operating principles of analytical and microscopic techniques and the limitations of the techniques, as well as chemical interactions that may be taking place."
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["utilise", "select", "interpret", "appreciate", "identify"]
  about: "chemistry: analytical and microscopic techniques"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "In chemistry, students should be able to choose, use and interpret analytical and microscopic techniques to find analytes and to identify, compare and characterise materials in forensic work, and should understand how those techniques work, their limits and the chemistry that may be going on."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.16
  locator: { number: "3.16", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 53530, end: 54036 }
  source: "3.16 In biology, the course should include practical microscopy, and molecular biology and biochemistry (with particular emphasis on body fluid identification and detection, nucleic acids, proteins, enzymes and biochemical processes, molecular genetics, genomics and principles of inheritance), forensic genetic techniques such as Short Tandem Repeat (STR) and may include anatomy, organ systems, some forensic medicine and other areas such as entomology, microbiology, palynology, botany and anthropology."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["include"]
  about: "biology in the curriculum"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The biology taught should include practical microscopy, molecular biology and biochemistry (body fluids, nucleic acids, proteins, enzymes, molecular genetics, genomics, inheritance) and forensic genetic techniques such as STR profiling, and may include anatomy, forensic medicine, entomology, microbiology, palynology, botany and anthropology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/3.17
  locator: { number: "3.17", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 54037, end: 54496 }
  source: "3.17 In physics, the course should include elementary optics (including principles of microscopy), the mechanics principles that underpin projectiles, ballistics, explosions and blood dynamics, aspects of the physical properties of materials, and an understanding of electromagnetism, atomic structure and radiation needed for an appreciation of the\n\n17\ntheoretical aspects of chemical instrumental analysis, forensic photography and other imaging techniques."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["include"]
  about: "physics in the curriculum"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Physics should include elementary optics and microscopy, the mechanics behind projectiles, ballistics, explosions and blood dynamics, the physical properties of materials, and enough electromagnetism, atomic structure and radiation to understand instrumental analysis, forensic photography and imaging."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/3.18
  locator: { number: "3.18", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 54497, end: 55186 }
  source: "3.18 In mathematics, there should be sufficient knowledge and facility in functions, algebra and trigonometry to cover the mathematical aspects of the physics, chemistry and biology in the course. Appropriate statistics would be a working knowledge of the basis and application of statistical methods and probability for analysis of experimental data and their uncertainties, including sampling methods and determining method uncertainty. This should also include an understanding of the principles and application of the likelihood ratio approach to the evaluation of evidence for the court, including the retrieval and use of frequency of occurrence information and the use of databases."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["use", "include"]
  about: "mathematics and statistics in the curriculum"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Mathematics should give enough skill with functions, algebra and trigonometry for the course's science; statistics should give a working grasp of statistical methods and probability for experimental data and its uncertainty, sampling and method uncertainty, and the likelihood ratio approach to evaluating evidence for court, with frequency data and databases."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/3.19
  locator: { number: "3.19", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 55187, end: 55863 }
  source: "3.19 Digital forensics builds upon principles based in computer science. Such principles are likely to include knowledge in data representation schemes (such as binary and hexadecimal), coding in a least one language (for example, Python), the different types of networks and the basic protocols in use, the principles of computer security, and an understanding of relational databases. From these principles, the course should develop to include reverse engineering techniques to understand the structure of unfamiliar data, linking artefacts from disparate data sources to develop a timeline of user activity and distinguishing between circumstantial and probative evidence."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["develop", "use", "include", "understand"]
  about: "digital forensics in the curriculum"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Digital forensics builds on computer science principles such as data representation, coding in at least one language, networks and protocols, security and relational databases; the course should go on to reverse engineering of unfamiliar data, linking artefacts from separate sources into a timeline of user activity, and telling circumstantial from probative evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/3.20
  locator: { number: "3.20", headingPath: ["Content, structure and delivery", "Knowledge and understanding"] }
  span: { start: 55864, end: 56321 }
  source: "3.20 In law, the course would be expected to include an awareness of criminal law, appropriate range of legislation, jurisdiction and procedures for working within a justice system. This includes the role of the expert witness as well as a working knowledge of the legislation that governs professional practice, such as the Police and Criminal Evidence Act 1984, the Data Protection Act 2018, and the Criminal Procedural Rules and Practice Directions 2020."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "be expected to" read as must
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["include", "includes"]
  about: "law in the curriculum"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The law taught would be expected to cover criminal law, relevant legislation, jurisdiction and procedure within a justice system, the expert witness, and the statutes governing practice, such as the Data Protection Act 2018, the Police and Criminal Evidence Act 1984 and the criminal procedure rules and practice directions of 2020."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/3.22.b1
  locator: { number: "3.22.b1", headingPath: ["Content, structure and delivery", "Scientific, laboratory and research skills"] }
  span: { start: 56837, end: 57043 }
  source: "work safely and effectively in a laboratory; this includes competent risk assessment, following documented procedures, ensuring calibration (where applicable), and rel iable recording of methods and results"
  stem: "3.22"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["work", "includes"]
  about: "safe, effective laboratory work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can work safely and well in a laboratory: assessing risk competently, following written procedures, calibrating where needed and recording methods and results reliably."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.22.b2
  locator: { number: "3.22.b2", headingPath: ["Content, structure and delivery", "Scientific, laboratory and research skills"] }
  span: { start: 57046, end: 57237 }
  source: "be confident in using advanced laboratory equipment (where applicable), and in learning how to use new facilities, including understanding the principles on which the instrumentation is based"
  stem: "3.22"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["use"]
  about: "advanced equipment and instrument principles"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can use advanced laboratory equipment with confidence where it applies, learn new facilities, and understand the principles behind the instruments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.22.b3
  locator: { number: "3.22.b3", headingPath: ["Content, structure and delivery", "Scientific, laboratory and research skills"] }
  span: { start: 57240, end: 57329 }
  source: "understand the need to carry out tasks in a consistent, reproducible and traceable manner"
  stem: "3.22"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["carry", "understand"]
  about: "consistent, reproducible, traceable work"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can see why tasks must be done consistently, reproducibly and traceably."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.22.b4
  locator: { number: "3.22.b4", headingPath: ["Content, structure and delivery", "Scientific, laboratory and research skills"] }
  span: { start: 57332, end: 57588 }
  source: "evaluate and critically interpret the results obtained via problem-solving; this will require the student to identify the appropriate scientific principles, plan strategies for solution and present conclusions in suitable textual, tabular or graphical form"
  stem: "3.22"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["interpret", "present", "evaluate", "plan", "identify", "critically"]
  about: "interpreting results through problem-solving"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can evaluate and critically interpret results by solving problems: finding the relevant scientific principles, planning how to solve them and presenting conclusions as text, tables or graphs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.22.b5
  locator: { number: "3.22.b5", headingPath: ["Content, structure and delivery", "Scientific, laboratory and research skills"] }
  span: { start: 57591, end: 57756 }
  source: "plan, execute and report the results of a scientific investigation using appropriate methods to critically analyse the data and evaluate the level of its uncertainty"
  stem: "3.22"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["evaluate", "plan", "execute", "report", "analyse", "critically"]
  about: "planning and reporting an investigation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can plan, carry out and report a scientific investigation, analysing the data critically and judging how uncertain it is."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.22.b6
  locator: { number: "3.22.b6", headingPath: ["Content, structure and delivery", "Scientific, laboratory and research skills"] }
  span: { start: 57759, end: 57917 }
  source: "apply scientific methods to tackle problems in science, including how to construct a suitable hypothesis and how to design experiments to test this hypothesis"
  stem: "3.22"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["construct", "apply", "design", "tackle", "test"]
  about: "hypotheses and experimental design"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can use scientific method on scientific problems, forming a hypothesis and designing experiments to test it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.22.b7
  locator: { number: "3.22.b7", headingPath: ["Content, structure and delivery", "Scientific, laboratory and research skills"] }
  span: { start: 57924, end: 58047 }
  source: "use ICT skills to analyse and organise data, including software appropriate to experimental equipment and use of databases."
  stem: "3.22"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["use", "organise", "analyse"]
  about: "ICT for data analysis"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can analyse and organise data with ICT, using the software that goes with instruments and working with databases."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.23.b1
  locator: { number: "3.23.b1", headingPath: ["Content, structure and delivery", "Scientific, laboratory and research skills"] }
  span: { start: 58158, end: 58233 }
  source: "work safely and effectively with minimal direct supervision in a laboratory"
  stem: "3.23"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: ["work"]
  about: "laboratory work with minimal supervision"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also be designed so that students can work safely and well in a laboratory with little direct supervision."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.23.b2
  locator: { number: "3.23.b2", headingPath: ["Content, structure and delivery", "Scientific, laboratory and research skills"] }
  span: { start: 58236, end: 58339 }
  source: "apply and adapt problem-solving skills to unfamiliar, complex, poorly defined and open-ended situations"
  stem: "3.23"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: ["apply", "adapt"]
  about: "problem-solving in unfamiliar, open-ended situations"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also be designed so that students can apply and adapt problem-solving to situations that are unfamiliar, complex, poorly defined and open-ended."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.23.b3
  locator: { number: "3.23.b3", headingPath: ["Content, structure and delivery", "Scientific, laboratory and research skills"] }
  span: { start: 58342, end: 58408 }
  source: "independently plan, design and execute new experimental procedures"
  stem: "3.23"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: ["plan", "execute", "design"]
  about: "designing new experimental procedures"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also be designed so that students can plan, design and run new experimental procedures on their own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.23.b4
  locator: { number: "3.23.b4", headingPath: ["Content, structure and delivery", "Scientific, laboratory and research skills"] }
  span: { start: 58411, end: 58490 }
  source: "independently plan, design, conduct and report an independent research project."
  stem: "3.23"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: ["plan", "report", "design", "conduct"]
  about: "an independent research project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also be designed so that students can plan, design, conduct and report a research project on their own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.24.b1
  locator: { number: "3.24.b1", headingPath: ["Content, structure and delivery", "Forensic science skills"] }
  span: { start: 58596, end: 58695 }
  source: "appreciate why standards and codes of conduct are necessary and the importance of adhering to these"
  stem: "3.24"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["conduct", "appreciate"]
  about: "why standards and codes matter"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can see why standards and codes of conduct are needed and why keeping to them matters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.24.b2
  locator: { number: "3.24.b2", headingPath: ["Content, structure and delivery", "Forensic science skills"] }
  span: { start: 58698, end: 58808 }
  source: "work effectively within a team and within a formalised system, following relevant quality assurance procedures"
  stem: "3.24"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["work"]
  about: "teamwork within a quality system"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can work well in a team and inside a formal system, following the relevant quality assurance procedures."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.24.b3
  locator: { number: "3.24.b3", headingPath: ["Content, structure and delivery", "Forensic science skills"] }
  span: { start: 58811, end: 58946 }
  source: "undertake the recording, recovery, scientific analysis, evaluation, interpretation, preservation and presentation of potential evidence"
  stem: "3.24"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["undertake"]
  about: "the handling of potential evidence from record to presentation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can record, recover, analyse, evaluate, interpret, preserve and present potential evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.24.b4
  locator: { number: "3.24.b4", headingPath: ["Content, structure and delivery", "Forensic science skills"] }
  span: { start: 58949, end: 58996 }
  source: "construct efficient case-examination strategies"
  stem: "3.24"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["construct"]
  about: "case-examination strategies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can build efficient strategies for examining a case."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.24.b5
  locator: { number: "3.24.b5", headingPath: ["Content, structure and delivery", "Forensic science skills"] }
  span: { start: 58999, end: 59082 }
  source: "be competent in procedures for maintaining the integrity and continuity of evidence"
  stem: "3.24"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: []
  about: "integrity and continuity of evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can apply competent procedures that keep evidence intact and its continuity unbroken."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.24.b6
  locator: { number: "3.24.b6", headingPath: ["Content, structure and delivery", "Forensic science skills"] }
  span: { start: 59085, end: 59201 }
  source: "use impartial written and oral presentation skills appropriate for the legal, court and law enforcement environments"
  stem: "3.24"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["use"]
  about: "impartial presentation for legal settings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can present impartially, in writing and in speech, in ways suited to legal, court and policing settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.24.b7
  locator: { number: "3.24.b7", headingPath: ["Content, structure and delivery", "Forensic science skills"] }
  span: { start: 59204, end: 59264 }
  source: "comply with safe working practices, both for self and others"
  stem: "3.24"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["comply"]
  about: "safe working practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can keep to safe working practice, for themselves and others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.24.b8
  locator: { number: "3.24.b8", headingPath: ["Content, structure and delivery", "Forensic science skills"] }
  span: { start: 59267, end: 59589 }
  source: "have an appreciation of the special issues, legal framework and practices involved with the recovery, storage, handling, retention, investigation, analysis and disposal of digital evidence and various contact trace materials, including human or other biological tissues and DNA with reference to the Human Tissue Act 2004."
  stem: "3.24"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["have"]
  about: "digital evidence, trace materials and the Human Tissue Act"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can appreciate the particular issues, legal framework and practice for digital evidence and trace materials, human and other biological tissue and DNA included, with reference to the Human Tissue Act 2004."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.24.b9
  locator: { number: "3.24.b9", headingPath: ["Content, structure and delivery", "Forensic science skills"] }
  span: { start: 59592, end: 59772 }
  source: "possess an awareness of the implications of modern technological advances, including databases and digital forensics, such as collection of data from mobile devices and PCs/laptops"
  stem: "3.24"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["possess"]
  about: "implications of technological advances"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can be aware of what modern technology, databases and digital forensics (such as data taken from phones and computers) mean for the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.24.b10
  locator: { number: "3.24.b10", headingPath: ["Content, structure and delivery", "Forensic science skills"] }
  span: { start: 59775, end: 59966 }
  source: "appreciate the ethical, legal and commercial responsibilities of a forensic science practitioner, and of the quality assurance and validation requirements relevant to professional competency."
  stem: "3.24"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["appreciate"]
  about: "practitioner responsibilities, quality and validation"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can appreciate a forensic practitioner's ethical, legal and commercial responsibilities and the quality assurance and validation that professional competence requires."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.25.b1
  locator: { number: "3.25.b1", headingPath: ["Content, structure and delivery", "Forensic science skills"] }
  span: { start: 60085, end: 60193 }
  source: "a deep experience of and a critical approach to an appropriate range of the methods used in forensic science"
  stem: "3.25"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: []
  about: "deep, critical experience of forensic methods"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also be designed so that students can gain deep experience of an apt range of forensic methods and take a critical approach to them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.25.b2
  locator: { number: "3.25.b2", headingPath: ["Content, structure and delivery", "Forensic science skills"] }
  span: { start: 60196, end: 60321 }
  source: "an open and innovative attitude to the development of new and emerging procedures and techniques relevant to forensic science"
  stem: "3.25"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: []
  about: "openness to new procedures and techniques"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also be designed so that students can be open and inventive towards new and emerging forensic procedures and techniques."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.25.b3
  locator: { number: "3.25.b3", headingPath: ["Content, structure and delivery", "Forensic science skills"] }
  span: { start: 60324, end: 60418 }
  source: "an understanding of the moral and ethical issues involved in the practice of forensic science."
  stem: "3.25"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: []
  about: "moral and ethical issues in practice"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also be designed so that students can understand the moral and ethical questions forensic practice raises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.26.b1
  locator: { number: "3.26.b1", headingPath: ["Content, structure and delivery", "Generic graduate skills"] }
  span: { start: 60509, end: 60612 }
  source: "personal and academic resilience by developing an awareness of their own well- being and that of others"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["developing"]
  about: "resilience and well-being"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can build personal and academic resilience by paying attention to their own well-being and that of others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.26.b2
  locator: { number: "3.26.b2", headingPath: ["Content, structure and delivery", "Generic graduate skills"] }
  span: { start: 60619, end: 60771 }
  source: "investigative skills, including the ability to carry out an independent investigation using multiple information sources and applying critical judgement"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["carry"]
  about: "independent investigation from many sources"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can investigate on their own, drawing on many sources of information and using critical judgement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.26.b3
  locator: { number: "3.26.b3", headingPath: ["Content, structure and delivery", "Generic graduate skills"] }
  span: { start: 60774, end: 61029 }
  source: "communication skills, including the ability to present complex concepts and information in a concise and effective manner, both orally and in writing, and the ability to interact and communicate effectively within a wide range of professional environments"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["present", "communicate", "interact"]
  about: "communication across professional settings"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can communicate complex ideas and information concisely and well, orally and in writing, and interact effectively across many professional settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.26.b4
  locator: { number: "3.26.b4", headingPath: ["Content, structure and delivery", "Generic graduate skills"] }
  span: { start: 61032, end: 61197 }
  source: "analytical skills, including the ability to pay attention to detail, to construct logical arguments based on incomplete data, and to use technical language correctly"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["use", "construct"]
  about: "analytical skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can analyse with attention to detail, build logical arguments from incomplete data and use technical language correctly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.26.b5
  locator: { number: "3.26.b5", headingPath: ["Content, structure and delivery", "Generic graduate skills"] }
  span: { start: 61200, end: 61295 }
  source: "ICT skills, including the use of databases, software packages and modern communications methods"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["use"]
  about: "ICT skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can use ICT well, including databases, software packages and modern means of communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.26.b6
  locator: { number: "3.26.b6", headingPath: ["Content, structure and delivery", "Generic graduate skills"] }
  span: { start: 61298, end: 61520 }
  source: "personal skills, including the ability to work both independently and as part of a team, and the ability to plan, organise and perform work efficiently and conscientiously in a timely way, meeting deadlines where necessary"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["organise", "work", "plan", "perform", "meeting"]
  about: "independent and team working; managing time"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can work alone and in a team, and plan, organise and complete work efficiently, conscientiously and on time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.26.b7
  locator: { number: "3.26.b7", headingPath: ["Content, structure and delivery", "Generic graduate skills"] }
  span: { start: 61523, end: 61680 }
  source: "personal development skills, including the ability to identify and reflect on where further training or skills acquisition is necessary for self-improvement."
  stem: "3.26"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["identify", "reflect"]
  about: "reflective personal development"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can see where further training or new skills would help them improve, and reflect on it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.26.b8
  locator: { number: "3.26.b8", headingPath: ["Content, structure and delivery", "Generic graduate skills"] }
  span: { start: 61683, end: 61782 }
  source: "an understanding of how to apply best practices with respect to equality, diversity and inclusivity"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["apply", "respect"]
  about: "applying good practice in equality, diversity and inclusion"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A course should be designed so that students can understand how to put good practice in equality, diversity and inclusion into effect."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.27.b1
  locator: { number: "3.27.b1", headingPath: ["Content, structure and delivery", "Generic graduate skills"] }
  span: { start: 61901, end: 61950 }
  source: "self-direction and originality in problem-solving"
  stem: "3.27"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: []
  about: "self-directed, original problem-solving"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also be designed so that students can solve problems with self-direction and originality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.27.b2
  locator: { number: "3.27.b2", headingPath: ["Content, structure and delivery", "Generic graduate skills"] }
  span: { start: 61953, end: 62042 }
  source: "an effective self-critical attitude in planning, carrying out and reporting investigation"
  stem: "3.27"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: []
  about: "a self-critical approach to investigation"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also be designed so that students can take a self-critical approach to planning, doing and reporting investigations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.27.b3
  locator: { number: "3.27.b3", headingPath: ["Content, structure and delivery", "Generic graduate skills"] }
  span: { start: 62045, end: 62182 }
  source: "competence in their ability to interpret complex technical information and to communicate it in a wide variety of professional situations"
  stem: "3.27"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: ["interpret", "communicate"]
  about: "interpreting and conveying complex information"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also be designed so that students can interpret complex technical information with competence and convey it across a wide variety of professional settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.27.b4
  locator: { number: "3.27.b4", headingPath: ["Content, structure and delivery", "Generic graduate skills"] }
  span: { start: 62185, end: 62267 }
  source: "the independent learning ability required for continuing professional development."
  stem: "3.27"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: []
  about: "independent learning for professional development"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's course should also be designed so that students can keep learning on their own for continuing professional development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.28
  locator: { number: "3.28", headingPath: ["Content, structure and delivery", "Ethical behaviour"] }
  span: { start: 62286, end: 62538 }
  source: "3.28 Students should fully appreciate that to fabricate, falsify, misrepresent or wilfully misinterpret evidence, data or the results of experiments is unethical and unacceptable. This should be referred to within the course material. They should also:"
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["appreciate", "fabricate", "falsify", "misrepresent", "misinterpret"]
  about: "fabrication and misrepresentation are unethical"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should fully understand that inventing, falsifying, misrepresenting or wilfully misreading evidence, data or experimental results is unethical and unacceptable, and course materials should say so."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.28.b1
  locator: { number: "3.28.b1", headingPath: ["Content, structure and delivery", "Ethical behaviour"] }
  span: { start: 62541, end: 62613 }
  source: "appreciate the serious consequences of careless or substandard practices"
  stem: "3.28"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["appreciate"]
  about: "consequences of careless practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should also understand how serious the results of careless or poor practice can be."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.28.b2
  locator: { number: "3.28.b2", headingPath: ["Content, structure and delivery", "Ethical behaviour"] }
  span: { start: 62616, end: 62680 }
  source: "be objective, unbiased and truthful in all aspects of their work"
  stem: "3.28"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["work"]
  about: "objectivity and honesty"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should also be objective, impartial and honest in every part of their work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.28.b3
  locator: { number: "3.28.b3", headingPath: ["Content, structure and delivery", "Ethical behaviour"] }
  span: { start: 62683, end: 62738 }
  source: "recognise and acknowledge the limits of their knowledge"
  stem: "3.28"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["recognise", "acknowledge"]
  about: "the limits of one's knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should also recognise and admit where their knowledge ends."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.28.b4
  locator: { number: "3.28.b4", headingPath: ["Content, structure and delivery", "Ethical behaviour"] }
  span: { start: 62741, end: 62798 }
  source: "recognise that plagiarism constitutes unethical behaviour"
  stem: "3.28"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["recognise"]
  about: "plagiarism as unethical"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should also recognise plagiarism as unethical conduct."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.28.b5
  locator: { number: "3.28.b5", headingPath: ["Content, structure and delivery", "Ethical behaviour"] }
  span: { start: 62801, end: 62847 }
  source: "be aware of equality and diversity legislation"
  stem: "3.28"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: []
  about: "equality and diversity legislation"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should also know the law on equality and diversity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.28.b6
  locator: { number: "3.28.b6", headingPath: ["Content, structure and delivery", "Ethical behaviour"] }
  span: { start: 62850, end: 63034 }
  source: "be aware of ethical issues, legal requirements and procedures involved in the conduct of research, particularly when working with animals and humans, and/or using an individual's data."
  stem: "3.28"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["conduct"]
  about: "research ethics and data"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should also know the ethical questions, legal rules and procedures in research, especially with animals or people or with a person's data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/3.29
  locator: { number: "3.29", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 63046, end: 63721 }
  source: "3.29 Within the multidisciplinary curriculum of forensic science, a diverse selection of assessment formats is expected to provide opportunities for students to develop a broad and contemporary skillset for the range of careers they may wish to pursue post-graduation. Assessments may be a combination of formative and summative to enhance students' skills and gain confidence, and may be delivered through in-person and/or online mechanisms. Reasonable adjustments for disabled students should be made to all assessment practices according to the student requirements. Assessment types could include some or all of the following elements at various levels of the curriculum:"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["develop", "gain", "include", "made"]
  about: "varied assessment and reasonable adjustments"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A forensic curriculum is expected to use varied assessment that builds a broad, current set of skills for later careers; assessment may be formative or summative, in person or online; and reasonable adjustments for disabled students should be made across all assessment as each student needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/3.30
  locator: { number: "3.30", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 64318, end: 64853 }
  source: "3.30 Assessment will test the successful achievement of subject knowledge, and the acquisition of generic and subject-specific skills embedded in the learning outcomes for the course. It is appropriate that some assessment elements will test a student's ability to organise and complete work, and to communicate effectively, under constraints of time and pressure. Elements of the assessment should also allow students the opportunity to demonstrate reflection, originality, creativity and integration of their knowledge into practice."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["demonstrate", "organise", "communicate", "work", "embedded", "test"]
  about: "what assessment tests"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Assessment will test subject knowledge and the generic and subject-specific skills in the course outcomes; some will test organising and completing work and communicating under time pressure, and some should let students show reflection, originality, creativity and the integration of knowledge into practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/3.31
  locator: { number: "3.31", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 64854, end: 65794 }
  source: "3.31 Assessments should be shared with students via an assessment brief with associated marking criteria mapped against the specific learning outcomes of the module or course. However, there may also be opportunities for students to design or co-create assessments with their tutors and/or peers as part of the learning process and these may or may not form part of the marking criteria. Assessments should be designed to be inclusive of all students, for example by using digital accessibility best practices, and meet learning support requirements, such as hearing impairments and colour blindness. While it still may be necessary on occasion to provide an alternative assessment to meet a specific learning support requirement, good assessment design should aim to anticipate such needs as much as possible. It is also important that alternative assessments enable students to demonstrate that they meet the expected learning outcome(s)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["demonstrate", "design", "support", "shared", "designed", "enable"]
  about: "briefs, criteria and inclusive assessment design"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should receive each assessment through a brief with marking criteria mapped to the outcomes, and may co-create some assessments; assessment should be inclusive, using good digital accessibility practice and meeting needs such as hearing impairment and colour blindness, anticipating needs rather than relying on alternatives, and it matters that any alternative still lets students show the outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/3.33
  locator: { number: "3.33", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 66273, end: 66545 }
  source: "3.33 To encourage students to engage with feedback, it should be provided in a timely manner. It is also suggested that the curriculum contains embedded, visible opportunities for students to create and implement their action plans to further promote personal development."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["encourage", "promote", "embedded", "engage", "provided", "implement"]
  about: "prompt feedback and action planning"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Feedback should come promptly so that students engage with it, and the statement suggests the curriculum give students visible chances to make and act on their own development plans."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 67043, end: 67857 }
  source: "4.2 In each case, the standards are divided into 'threshold', 'typical' and 'excellent'. These standards are intended to reflect the performance of the individual student. The threshold level is the core of the Subject Benchmark Statement and is achieved by anyone obtaining an honours degree. Many students will perform significantly better than the threshold standard, and it is expected that most should achieve the typical standard. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject and the teams that run them"
  addressee: provider
  verbs: ["reflect", "perform", "achieve", "refer"]
  about: "the three rungs and Annex D"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Each set of standards is split into threshold, typical and excellent and describes individual performance; the threshold is the core, reached by anyone gaining an honours degree, and most students are expected to reach the typical rung; each provider decides what counts as evidence of achievement and should refer to Annex D, which describes the degree classes at FHEQ level 6 and FQHEIS level 10."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68190, end: 68366 }
  source: "knowledge and understanding of those sciences, including mathematics and statistics (including the Bayesian approach and likelihood ratios), involved in forensic investigations"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: []
  about: "the sciences, mathematics and statistics behind forensic work"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show knowledge and understanding of the sciences that forensic investigation draws on, mathematics and statistics among them, with Bayesian reasoning and likelihood ratios."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68369, end: 68401 }
  source: "knowledge of forensic techniques"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: []
  about: "forensic techniques"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show knowledge of the techniques forensic science uses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68404, end: 68501 }
  source: "laboratory skills to carry out a range of tasks and technical processes with a degree of autonomy"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: ["carry"]
  about: "laboratory skills and autonomy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show laboratory skills for a range of tasks and technical processes, done with some autonomy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68504, end: 68661 }
  source: "an ability to select and carry out practical laboratory experiments in forensic investigations, including the ability to use appropriate laboratory equipment"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: ["use", "carry", "select"]
  about: "choosing and running laboratory experiments"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show choosing and running practical laboratory experiments for forensic investigations, using suitable equipment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68664, end: 68747 }
  source: "knowledge of the types of cognitive bias and how they may affect forensic processes"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: []
  about: "cognitive bias in forensic processes"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show knowledge of the kinds of cognitive bias and how they can distort forensic processes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68750, end: 68840 }
  source: "a range and knowledge of the general issues and techniques involved in scene investigation"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: []
  about: "scene investigation issues and techniques"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show a range of knowledge of the broad issues and methods of scene investigation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68843, end: 69032 }
  source: "the ability to interpret the results of laboratory and other investigations, with an appreciation of their limitations, including the hierarchy of propositions and activity level hypotheses"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: ["interpret"]
  about: "interpreting results within their limits"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show interpretation of laboratory and other results with a sense of their limits, with the hierarchy of propositions and hypotheses at activity level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69035, end: 69181 }
  source: "knowledge of the various legal and law enforcement environments within which forensic science is practiced, including working across jurisdictions"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: []
  about: "legal and law enforcement settings of practice"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show knowledge of the legal and policing settings in which forensic science is practised, work across jurisdictions included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69184, end: 69306 }
  source: "an understanding of the differences between the intelligence and evidential value of forensic findings in an investigation"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: []
  about: "intelligence value against evidential value"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show understanding of how the intelligence value of a forensic finding differs from its evidential value."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b10
  locator: { number: "4.4.b10", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69309, end: 69560 }
  source: "the ability to record results accurately, organise data, make deductions and present clearly the results of investigations both in written and oral form, in a manner which can be readily assimilated within a legal, law enforcement or court environment"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: ["record", "organise", "make", "present"]
  about: "recording, deducing and presenting results for legal audiences"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show accurate recording of results, orderly data, sound deductions and clear written and spoken presentation of findings in a form legal, policing or court audiences can take in."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b11
  locator: { number: "4.4.b11", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69567, end: 69628 }
  source: "an appreciation of how progress is made within the discipline"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: ["made"]
  about: "how progress is made in the discipline"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show an appreciation of how the discipline advances."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b12
  locator: { number: "4.4.b12", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69631, end: 69742 }
  source: "knowledge of, and commitment to, the ethical and legal obligations of science and particularly forensic science"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: []
  about: "the ethical and legal duties of forensic science"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show knowledge of the ethical and legal duties that bind science, forensic science above all, and commitment to meeting them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b13
  locator: { number: "4.4.b13", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69745, end: 69938 }
  source: "knowledge and understanding of and respect for issues and practices involved with the handling, storage and investigation of human tissues, DNA, digital data and other trace evidential material"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: ["respect"]
  about: "handling human tissue, DNA, digital data and trace material"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show knowledge, understanding and respect for what handling, storing and examining human tissue, DNA, digital data and other trace material involves."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b14
  locator: { number: "4.4.b14", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69941, end: 70035 }
  source: "competence in safe working practices at scenes and in the laboratory, both for self and others"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: []
  about: "safe working at scenes and in the laboratory"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show competent safe working at scenes and in the laboratory, for themselves and others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b15
  locator: { number: "4.4.b15", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 70038, end: 70119 }
  source: "an appreciation of quality assurance procedures within a forensic science context"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: []
  about: "quality assurance procedures"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show an appreciation of quality assurance procedures in forensic science."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b16
  locator: { number: "4.4.b16", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 70122, end: 70195 }
  source: "communication skills to an understandable level, verbally and in writing."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: []
  about: "spoken and written communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show spoken and written communication that others can follow."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b17
  locator: { number: "4.4.b17", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 70254, end: 70390 }
  source: "the ability to interpret and communicate forensic evidence and experimental results in the context of casework, including expert opinion"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: ["interpret", "communicate"]
  about: "interpreting and communicating evidence in casework"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show interpretation and communication of forensic evidence and experimental results in casework, expert opinion included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b18
  locator: { number: "4.4.b18", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 70393, end: 70526 }
  source: "ability to formulate and justify expert opinion using transparent arguments, including statistical likelihood ratio where appropriate"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: ["formulate", "justify"]
  about: "forming and justifying expert opinion"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show expert opinion formed and justified through transparent argument, using the likelihood ratio where it fits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b19
  locator: { number: "4.4.b19", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 70529, end: 70658 }
  source: "the ability to appraise, quantify and clearly communicate levels of uncertainty in expert opinion or associated experimental data"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: ["appraise", "quantify", "communicate"]
  about: "appraising and conveying uncertainty"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show appraising, quantifying and clearly reporting the uncertainty in expert opinion or the data behind it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b20
  locator: { number: "4.4.b20", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 70661, end: 70883 }
  source: "the ability to prepare and deliver impartial, comprehensible and comprehensive oral and written reports of a quality suitable for a wide variety of legal and law enforcement situations, including those involving the public"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: ["prepare", "deliver"]
  about: "impartial oral and written reports"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show impartial, clear and complete oral and written reports fit for a wide variety of legal and policing settings, those involving the public included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b21
  locator: { number: "4.4.b21", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 70886, end: 71009 }
  source: "a working knowledge of prevailing industry best practice and legal standards applicable to evidence, including digital data"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: []
  about: "best practice and legal standards for evidence"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show working knowledge of current industry best practice and the legal standards for evidence, digital data included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b22
  locator: { number: "4.4.b22", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 71012, end: 71188 }
  source: "the ability to construct, manage and deliver case-appropriate forensic strategies, including the Case Assessment and Interpretation framework ( Jackson, Aitken & Roberts, 2015)"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: ["deliver", "construct", "manage"]
  about: "case-appropriate forensic strategies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show building, managing and delivering forensic strategies suited to the case, using the Case Assessment and Interpretation framework."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.4.b23
  locator: { number: "4.4.b23", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 71191, end: 71290 }
  source: "the ability to adhere to contamination avoidance procedures including the handling of digital data."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours)"
  addressee: learner
  verbs: ["adhere"]
  about: "avoiding contamination"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show following procedures that avoid contamination, in handling digital data too."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 71553, end: 71737 }
  source: "knowledge and appreciation of the techniques and skills required for the recording (including photography), preserving, collection, processing and interpretation of evidence at a scene"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours) with emphasis on one area"
  addressee: learner
  verbs: []
  about: "scene investigation: techniques for evidence at a scene"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show knowledge and appreciation of the skills and techniques for recording (photography included), preserving, collecting, processing and interpreting evidence at a scene."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 71740, end: 71985 }
  source: "an understanding of the responsibilities, roles and liabilities of those involved in a scene investigation, including when to call upon specialist personnel and an ability to work safely, effectively and contribute positively within such a team."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours) with emphasis on one area"
  addressee: learner
  verbs: ["work", "contribute", "call"]
  about: "scene investigation: roles, liabilities and teamwork"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show understanding of the duties, roles and liabilities of everyone in a scene investigation, knowing when to call in specialists, and the ability to work safely and well and contribute within that team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 72008, end: 72115 }
  source: "knowledge and appreciation of the theory and application of the laboratory methods used in forensic science"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours) with emphasis on one area"
  addressee: learner
  verbs: []
  about: "laboratory analysis: theory and application of methods"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show knowledge and appreciation of the theory and use of forensic laboratory methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 72118, end: 72390 }
  source: "an ability in the selection and use of a wide range of methods used in the location, identification, recovery, extraction and scientific analysis of commonly encountered physical, digital, chemical and biological materials and marks, including trace materials such as DNA."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours) with emphasis on one area"
  addressee: learner
  verbs: ["use"]
  about: "laboratory analysis: choosing and using methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show choosing and using many methods to locate, identify, recover, extract and analyse common physical, digital, chemical and biological materials and marks, trace materials such as DNA included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 72411, end: 72679 }
  source: "knowledge and understanding of the principal techniques and skills required for the searching, identification, preservation, transport, handling, and continuity of\n\n23\ncommonly encountered physical devices likely or known to contain digital data from a range of scenes"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours) with emphasis on one area"
  addressee: learner
  verbs: []
  about: "digital forensics: devices that hold digital data"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show knowledge and understanding of the main techniques and skills for searching for, identifying, preserving, moving, handling and keeping continuity of common devices that hold or may hold digital data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 72682, end: 72809 }
  source: "the ability to select and thoroughly justify the use of a range of methods used in the acquisition and analysis of digital data"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours) with emphasis on one area"
  addressee: learner
  verbs: ["use", "select", "justify"]
  about: "digital forensics: choosing and justifying acquisition and analysis methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show choosing, and fully justifying, a range of methods for acquiring and analysing digital data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 72812, end: 73085 }
  source: "the ability to carry out an investigation through the examination of facts from a variety of sources (including those which require additional reading or experimentation to understand their operation) relating to an incident or allegation to establish the truth of a matter"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours) with emphasis on one area"
  addressee: learner
  verbs: ["carry", "understand"]
  about: "digital forensics: investigating facts from many sources"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show an investigation that examines facts from varied sources, some needing extra reading or testing to understand, to find out the truth of an incident or allegation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 73088, end: 73188 }
  source: "the ability to review, validate and verify methods and tools used for the processing of digital data"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours) with emphasis on one area"
  addressee: learner
  verbs: ["review", "validate", "verify"]
  about: "digital forensics: reviewing, validating and verifying tools"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show reviewing, validating and verifying the methods and tools that process digital data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 73191, end: 73337 }
  source: "the ability to construct and manage a forensic strategy, with regards to the search of multiple sites and the subsequent analysis of digital data."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold (third-class honours) with emphasis on one area"
  addressee: learner
  verbs: ["construct", "manage"]
  about: "digital forensics: strategy across multiple sites"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show building and managing a forensic strategy for searching several sites and then analysing the digital data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 73563, end: 73726 }
  source: "a strong knowledge and understanding of those sciences, including mathematics and statistics (including the Bayesian approach), involved in forensic investigations"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: []
  about: "the sciences, mathematics and statistics behind forensic work"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b1, basis: inferred }
  paraphrase: "Will be able to show strong knowledge and understanding of the sciences behind forensic investigation, mathematics and statistics included, with Bayesian reasoning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 73729, end: 73772 }
  source: "a thorough knowledge of forensic techniques"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: []
  about: "forensic techniques"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b2, basis: inferred }
  paraphrase: "Will be able to show thorough knowledge of the techniques forensic science uses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 73775, end: 73877 }
  source: "the laboratory skills to carry out a full range of tasks and technical processes, mainly independently"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: ["carry"]
  about: "laboratory skills and autonomy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b3, basis: inferred }
  paraphrase: "Will be able to show laboratory skills for every kind of task and technical process, done largely on their own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 73880, end: 74056 }
  source: "the ability to effectively select and carry out practical laboratory experiments in forensic investigations, including the confident use of the appropriate laboratory equipment"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: ["use", "carry", "select"]
  about: "choosing and running laboratory experiments"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b4, basis: inferred }
  paraphrase: "Will be able to show effective choice and running of such experiments, with confident use of the right equipment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 74059, end: 74234 }
  source: "a strong knowledge of the types of cognitive bias, how they may affect forensic processes and the ability to identify and apply mitigating measures across a range of scenarios"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: ["apply", "identify"]
  about: "cognitive bias in forensic processes"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b5, basis: inferred }
  paraphrase: "Will be able to show strong knowledge of cognitive bias and its effects on forensic processes, and the skill to spot it and apply ways to reduce it across a range of cases."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 74237, end: 74326 }
  source: "a thorough knowledge of the general issues and techniques involved in scene investigation"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: []
  about: "scene investigation issues and techniques"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b6, basis: inferred }
  paraphrase: "Will be able to show thorough knowledge of the broad issues and methods of scene investigation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b7
  locator: { number: "4.6.b7", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 74329, end: 74455 }
  source: "the ability to interpret the results of laboratory and other investigations, with a thorough appreciation of their limitations"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: ["interpret"]
  about: "interpreting results within their limits"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b7, basis: inferred }
  paraphrase: "Will be able to show interpretation of laboratory and other results with a thorough sense of their limits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b8
  locator: { number: "4.6.b8", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 74458, end: 74614 }
  source: "a strong knowledge of the various legal and law enforcement environments within which forensic science is practiced, including working across jurisdictions."
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: []
  about: "legal and law enforcement settings of practice"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b8, basis: inferred }
  paraphrase: "Will be able to show strong knowledge of the legal and policing settings in which forensic science is practised, work across jurisdictions included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b9
  locator: { number: "4.6.b9", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 74617, end: 74747 }
  source: "a thorough understanding of the differences between the intelligence and evidential value of forensic findings in an investigation"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: []
  about: "intelligence value against evidential value"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b9, basis: inferred }
  paraphrase: "Will be able to show thorough understanding of how the intelligence value of a forensic finding differs from its evidential value."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b10
  locator: { number: "4.6.b10", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 74750, end: 75018 }
  source: "the ability to record results accurately, organise data, make rational deductions and present clearly the results of complex investigations both in written and oral form, in a manner which can be readily assimilated within a legal, law enforcement or court environment"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: ["record", "organise", "make", "present"]
  about: "recording, deducing and presenting results for legal audiences"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b10, basis: inferred }
  paraphrase: "Will be able to show accurate recording, orderly data, rational deductions and clear written and spoken presentation of complex investigations for legal, policing or court audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b11
  locator: { number: "4.6.b11", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 75021, end: 75088 }
  source: "a strong appreciation of how progress is made within the discipline"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: ["made"]
  about: "how progress is made in the discipline"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b11, basis: inferred }
  paraphrase: "Will be able to show a strong appreciation of how the discipline advances."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b12
  locator: { number: "4.6.b12", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 75091, end: 75224 }
  source: "a thorough knowledge of, and consistent commitment to, the ethical and legal obligations of science and particularly forensic science"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: []
  about: "the ethical and legal duties of forensic science"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b12, basis: inferred }
  paraphrase: "Will be able to show thorough knowledge of the ethical and legal duties that bind science, forensic science above all, and a consistent commitment to meeting them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b13
  locator: { number: "4.6.b13", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 75227, end: 75429 }
  source: "a strong knowledge and understanding of and respect for issues and practices involved with the handling, storage and investigation of human tissues, DNA, digital data and other trace evidential material"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: ["respect"]
  about: "handling human tissue, DNA, digital data and trace material"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b13, basis: inferred }
  paraphrase: "Will be able to show strong knowledge, understanding and respect for what handling, storing and examining human tissue, DNA, digital data and other trace material involves."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b14
  locator: { number: "4.6.b14", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 75432, end: 75556 }
  source: "consistent and well-developed competence in safe working practices at scenes and in the laboratory, both for self and others"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: []
  about: "safe working at scenes and in the laboratory"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b14, basis: inferred }
  paraphrase: "Will be able to show consistent, well-developed competence in safe working at scenes and in the laboratory, for themselves and others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b15
  locator: { number: "4.6.b15", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 75559, end: 75648 }
  source: "a thorough appreciation of quality assurance procedures within a forensic science context"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: []
  about: "quality assurance procedures"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b15, basis: inferred }
  paraphrase: "Will be able to show a thorough appreciation of quality assurance procedures in forensic science."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b16
  locator: { number: "4.6.b16", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 75651, end: 75726 }
  source: "communication skills to a highly proficient level, verbally and in writing."
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: []
  about: "spoken and written communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b16, basis: inferred }
  paraphrase: "Will be able to show highly proficient spoken and written communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b17
  locator: { number: "4.6.b17", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 75789, end: 75952 }
  source: "the ability to manage, critically interpret and clearly communicate forensic evidence and experimental results in the context of casework, including expert opinion"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: ["interpret", "communicate", "manage", "critically"]
  about: "interpreting and communicating evidence in casework"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b17, basis: inferred }
  paraphrase: "Will be able to show management, critical interpretation and clear communication of forensic evidence and results in casework, expert opinion included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b18
  locator: { number: "4.6.b18", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 75955, end: 76103 }
  source: "the consistent ability to formulate and justify expert opinion using transparent arguments, including statistical likelihood ratio where appropriate"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: ["formulate", "justify"]
  about: "forming and justifying expert opinion"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b18, basis: inferred }
  paraphrase: "Will be able to show consistent forming and justifying of expert opinion through transparent argument, using the likelihood ratio where it fits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b19
  locator: { number: "4.6.b19", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 76106, end: 76246 }
  source: "the consistent ability to appraise, quantify and clearly communicate levels of uncertainty in expert opinion or associated experimental data"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: ["appraise", "quantify", "communicate"]
  about: "appraising and conveying uncertainty"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b19, basis: inferred }
  paraphrase: "Will be able to show consistent appraisal, quantification and clear reporting of the uncertainty in expert opinion or the data behind it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b20
  locator: { number: "4.6.b20", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 76249, end: 76464 }
  source: "the ability to prepare and deliver impartial, comprehensible and comprehensive oral and written reports of high quality in a wide variety of legal and law enforcement situations, including those involving the public"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: ["prepare", "deliver"]
  about: "impartial oral and written reports"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b20, basis: inferred }
  paraphrase: "Will be able to show impartial, clear and complete oral and written reports of high quality across legal and policing settings, those involving the public included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b21
  locator: { number: "4.6.b21", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 76467, end: 76597 }
  source: "a strong working knowledge of prevailing industry best practice and legal standards applicable to evidence, including digital data"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: []
  about: "best practice and legal standards for evidence"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b21, basis: inferred }
  paraphrase: "Will be able to show strong working knowledge of current industry best practice and the legal standards for evidence, digital data included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b22
  locator: { number: "4.6.b22", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 76600, end: 76708 }
  source: "a consistent ability to adhere to contamination avoidance procedures, including the handling of digital data"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: ["adhere"]
  about: "avoiding contamination"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b23, basis: inferred }
  paraphrase: "Will be able to show consistently following procedures that avoid contamination, in handling digital data too."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.6.b23
  locator: { number: "4.6.b23", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 76711, end: 76865 }
  source: "the ability to effectively construct, manage and deliver case-appropriate forensic strategies, including the Case Assessment and Interpretation framework."
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1)"
  addressee: learner
  verbs: ["deliver", "construct", "manage"]
  about: "case-appropriate forensic strategies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.4.b22, basis: inferred }
  paraphrase: "Will be able to show effective building, managing and delivering of forensic strategies suited to the case, using the Case Assessment and Interpretation framework."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 77133, end: 77342 }
  source: "a thorough knowledge and appreciation of the techniques and skills required for the collection, processing, recording (including appropriate photography), preservation and interpretation of evidence at a scene"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1) with emphasis on one area"
  addressee: learner
  verbs: []
  about: "scene investigation: techniques for evidence at a scene"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.5.b1, basis: inferred }
  paraphrase: "Will be able to show thorough knowledge and appreciation of the skills and techniques for collecting, processing, recording (with suitable photography), preserving and interpreting evidence at a scene."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 77345, end: 77549 }
  source: "a thorough understanding of the responsibilities, roles and liabilities of those involved in a (crime) scene investigation, and an ability to work effectively and contribute positively within such a team."
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1) with emphasis on one area"
  addressee: learner
  verbs: ["work", "contribute"]
  about: "scene investigation: roles, liabilities and teamwork"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.5.b2, basis: inferred }
  paraphrase: "Will be able to show thorough understanding of the duties, roles and liabilities of everyone in a scene investigation and the ability to work well and contribute within that team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 77573, end: 77691 }
  source: "a thorough knowledge and appreciation of the theory and application of the laboratory methods used in forensic science"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1) with emphasis on one area"
  addressee: learner
  verbs: []
  about: "laboratory analysis: theory and application of methods"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.5.b3, basis: inferred }
  paraphrase: "Will be able to show thorough knowledge and appreciation of the theory and use of forensic laboratory methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 77694, end: 77974 }
  source: "consistent ability in the selection and use of a wide range of methods used in the location, identification, recovery, extraction and scientific analysis of commonly encountered physical, digital, chemical and biological materials and marks, including trace materials such as DNA."
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1) with emphasis on one area"
  addressee: learner
  verbs: ["use"]
  about: "laboratory analysis: choosing and using methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.5.b4, basis: inferred }
  paraphrase: "Will be able to show consistent skill in choosing and using many methods to locate, identify, recover, extract and analyse common physical, digital, chemical and biological materials and marks, trace materials such as DNA included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 77995, end: 78269 }
  source: "a thorough knowledge and understanding of the principal techniques and skills required for the searching, identification, preservation, transport, handling and continuity of commonly encountered physical devices likely or known to contain digital data from a range of scenes"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1) with emphasis on one area"
  addressee: learner
  verbs: []
  about: "digital forensics: devices that hold digital data"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.5.b5, basis: inferred }
  paraphrase: "Will be able to show thorough knowledge and understanding of the main techniques and skills for searching for, identifying, preserving, moving, handling and keeping continuity of common devices that hold or may hold digital data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.7.b6
  locator: { number: "4.7.b6", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 78272, end: 78410 }
  source: "the consistent ability to select and thoroughly justify the use of a range of methods used in the acquisition and analysis of digital data"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1) with emphasis on one area"
  addressee: learner
  verbs: ["use", "select", "justify"]
  about: "digital forensics: choosing and justifying acquisition and analysis methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.5.b6, basis: inferred }
  paraphrase: "Will be able to show consistent choice, fully justified, of a range of methods for acquiring and analysing digital data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.7.b7
  locator: { number: "4.7.b7", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 78413, end: 78696 }
  source: "the ability to carry out an effective investigation through the examination of facts from a variety of sources (including those which require additional reading or experimentation to understand their operation) relating to an incident or allegation to establish the truth of a matter"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1) with emphasis on one area"
  addressee: learner
  verbs: ["carry", "understand"]
  about: "digital forensics: investigating facts from many sources"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.5.b7, basis: inferred }
  paraphrase: "Will be able to show an effective investigation that examines facts from varied sources, some needing extra reading or testing to understand, to find out the truth of an incident or allegation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.7.b8
  locator: { number: "4.7.b8", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 78699, end: 78810 }
  source: "the consistent ability to review, validate and verify methods and tools used for the processing of digital data"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1) with emphasis on one area"
  addressee: learner
  verbs: ["review", "validate", "verify"]
  about: "digital forensics: reviewing, validating and verifying tools"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.5.b8, basis: inferred }
  paraphrase: "Will be able to show consistently reviewing, validating and verifying the methods and tools that process digital data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.7.b9
  locator: { number: "4.7.b9", headingPath: ["Benchmark standards", "Typical level (2:2 or 2:1)"] }
  span: { start: 78813, end: 78970 }
  source: "the ability to construct and manage an effective forensic strategy, with regards to the search of multiple sites and the subsequent analysis of digital data."
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung (a 2:2 or 2:1) with emphasis on one area"
  addressee: learner
  verbs: ["construct", "manage"]
  about: "digital forensics: strategy across multiple sites"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.5.b9, basis: inferred }
  paraphrase: "Will be able to show building and managing an effective forensic strategy for searching several sites and then analysing the digital data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 79204, end: 79381 }
  source: "a consistent, detailed knowledge and understanding of those sciences, including mathematics and statistics (including the Bayesian approach), involved in forensic investigations"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: []
  about: "the sciences, mathematics and statistics behind forensic work"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b1, basis: inferred }
  paraphrase: "Will be able to show consistent, detailed command of the sciences behind forensic investigation, mathematics, statistics and Bayesian reasoning included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 79384, end: 79440 }
  source: "a detailed and thorough knowledge of forensic techniques"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: []
  about: "forensic techniques"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b2, basis: inferred }
  paraphrase: "Will be able to show detailed and thorough command of the techniques forensic science uses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 79443, end: 79568 }
  source: "the confidence and laboratory skills to carry out a full range of tasks and technical processes with a high level of autonomy"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: ["carry"]
  about: "laboratory skills and autonomy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b3, basis: inferred }
  paraphrase: "Will be able to show the confidence and laboratory skill for every kind of task and technical process, done with a high degree of autonomy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 79571, end: 79755 }
  source: "the ability to critically select, develop and carry out practical laboratory experiments in forensic investigations, including the confident use of the appropriate laboratory equipment"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: ["develop", "use", "carry", "select", "critically"]
  about: "choosing and running laboratory experiments"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b4, basis: inferred }
  paraphrase: "Will be able to show critical choice, development and running of such experiments, with confident use of the right equipment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 79758, end: 79951 }
  source: "a detailed knowledge of the types of cognitive bias, how they may affect forensic processes and the ability to critically identify and apply mitigating measures across a wide range of scenarios"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: ["apply", "identify", "critically"]
  about: "cognitive bias in forensic processes"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b5, basis: inferred }
  paraphrase: "Will be able to show detailed knowledge of cognitive bias and its effects, and critical skill in spotting it and applying ways to reduce it across a wide range of cases."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b6
  locator: { number: "4.8.b6", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 79954, end: 80060 }
  source: "a wide-ranging and critical knowledge of the general issues and techniques involved in scene investigation"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: []
  about: "scene investigation issues and techniques"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b6, basis: inferred }
  paraphrase: "Will be able to show wide-ranging, critical knowledge of the broad issues and methods of scene investigation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b7
  locator: { number: "4.8.b7", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 80063, end: 80211 }
  source: "the ability to consistently interpret the results of laboratory and other investigations, with a thorough critical appreciation of their limitations"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: ["interpret"]
  about: "interpreting results within their limits"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b7, basis: inferred }
  paraphrase: "Will be able to show consistent interpretation of laboratory and other results with a thorough, critical sense of their limits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b8
  locator: { number: "4.8.b8", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 80214, end: 80373 }
  source: "an extensive knowledge of the various legal and law enforcement environments within which forensic science is practiced, including working across jurisdictions"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: []
  about: "legal and law enforcement settings of practice"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b8, basis: inferred }
  paraphrase: "Will be able to show extensive knowledge of the legal and policing settings in which forensic science is practised, work across jurisdictions included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b9
  locator: { number: "4.8.b9", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 80376, end: 80510 }
  source: "an exceptional understanding of the differences between the intelligence and evidential value of forensic findings in an investigation"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: []
  about: "intelligence value against evidential value"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b9, basis: inferred }
  paraphrase: "Will be able to show exceptional understanding of how the intelligence value of a forensic finding differs from its evidential value."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b10
  locator: { number: "4.8.b10", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 80513, end: 80805 }
  source: "the ability to consistently record results accurately, critically organise data, make rational deductions and present clearly the results of complex investigations both in written and oral form, in a manner which can be readily assimilated within a legal, law enforcement or court environment"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: ["record", "organise", "make", "present", "critically"]
  about: "recording, deducing and presenting results for legal audiences"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b10, basis: inferred }
  paraphrase: "Will be able to show consistently accurate recording, critically organised data, rational deductions and clear written and spoken presentation of complex investigations for legal, policing or court audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b11
  locator: { number: "4.8.b11", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 80808, end: 80894 }
  source: "an exceptional and critical appreciation of how progress is made within the discipline"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: ["made"]
  about: "how progress is made in the discipline"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b11, basis: inferred }
  paraphrase: "Will be able to show an exceptional, critical appreciation of how the discipline advances."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b12
  locator: { number: "4.8.b12", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 80897, end: 81032 }
  source: "an extensive knowledge of, and consistent commitment to, the ethical and legal obligations of science and particularly forensic science"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: []
  about: "the ethical and legal duties of forensic science"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b12, basis: inferred }
  paraphrase: "Will be able to show extensive knowledge of the ethical and legal duties that bind science, forensic science above all, and a consistent commitment to meeting them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b13
  locator: { number: "4.8.b13", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 81035, end: 81249 }
  source: "an advanced knowledge and critical understanding of and respect for issues and practices involved with the handling, storage and investigation of human tissues, DNA, digital data and other trace evidential material"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: ["respect"]
  about: "handling human tissue, DNA, digital data and trace material"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b13, basis: inferred }
  paraphrase: "Will be able to show advanced knowledge, critical understanding and respect for what handling, storing and examining human tissue, DNA, digital data and other trace material involves."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b14
  locator: { number: "4.8.b14", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 81252, end: 81371 }
  source: "consistent and exemplary competence in safe working practices at scenes and in the laboratory, both for self and others"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: []
  about: "safe working at scenes and in the laboratory"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b14, basis: inferred }
  paraphrase: "Will be able to show consistent, exemplary competence in safe working at scenes and in the laboratory, for themselves and others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b15
  locator: { number: "4.8.b15", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 81374, end: 81463 }
  source: "a critical appreciation of quality assurance procedures within a forensic science context"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: []
  about: "quality assurance procedures"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b15, basis: inferred }
  paraphrase: "Will be able to show a critical appreciation of quality assurance procedures in forensic science."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b16
  locator: { number: "4.8.b16", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 81466, end: 81537 }
  source: "communication skills to an accomplished level, verbally and in writing."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: []
  about: "spoken and written communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b16, basis: inferred }
  paraphrase: "Will be able to show accomplished spoken and written communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b17
  locator: { number: "4.8.b17", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 81596, end: 81788 }
  source: "the ability to consistently and effectively manage, critically interpret and clearly communicate forensic evidence and experimental results in the context of casework, including expert opinion"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: ["interpret", "communicate", "manage", "critically"]
  about: "interpreting and communicating evidence in casework"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b17, basis: inferred }
  paraphrase: "Will be able to show consistent, effective management, critical interpretation and clear communication of forensic evidence and results in casework, expert opinion included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b18
  locator: { number: "4.8.b18", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 81791, end: 81936 }
  source: "exceptional ability to formulate and justify expert opinion using transparent arguments, including statistical likelihood ratio where appropriate"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: ["formulate", "justify"]
  about: "forming and justifying expert opinion"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b18, basis: inferred }
  paraphrase: "Will be able to show exceptional skill in forming and justifying expert opinion through transparent argument, using the likelihood ratio where it fits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b19
  locator: { number: "4.8.b19", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 81939, end: 82102 }
  source: "the ability to critically appraise, quantify and clearly communicate in a consistent fashion level of uncertainty in expert opinion or associated experimental data"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: ["appraise", "quantify", "communicate", "critically"]
  about: "appraising and conveying uncertainty"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b19, basis: inferred }
  paraphrase: "Will be able to show critical appraisal, quantification and consistently clear reporting of the uncertainty in expert opinion or the data behind it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b20
  locator: { number: "4.8.b20", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 82109, end: 82344 }
  source: "the ability to consistently prepare and deliver impartial, comprehensible and comprehensive oral and written reports of exceptional quality in a wide variety of legal and law enforcement situations, including those involving the public"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: ["prepare", "deliver"]
  about: "impartial oral and written reports"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b20, basis: inferred }
  paraphrase: "Will be able to show consistently impartial, clear and complete oral and written reports of exceptional quality across legal and policing settings, those involving the public included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b21
  locator: { number: "4.8.b21", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 82347, end: 82484 }
  source: "a comprehensive working knowledge of prevailing industry best practice and legal standards applicable to evidence, including digital data"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: []
  about: "best practice and legal standards for evidence"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b21, basis: inferred }
  paraphrase: "Will be able to show comprehensive working knowledge of current industry best practice and the legal standards for evidence, digital data included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b22
  locator: { number: "4.8.b22", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 82487, end: 82623 }
  source: "a consistent and exceptional ability to adhere to and develop contamination avoidance procedures, including the handling of digital data"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: ["develop", "adhere"]
  about: "avoiding contamination"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b22, basis: inferred }
  paraphrase: "Will be able to show consistent, exceptional adherence to procedures that avoid contamination, and their development, in handling digital data too."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.8.b23
  locator: { number: "4.8.b23", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 82626, end: 82798 }
  source: "the ability to consistently and effectively construct, manage and deliver case- appropriate forensic strategies, including the Case Assessment and Interpretation framework."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours)"
  addressee: learner
  verbs: ["deliver", "construct", "manage"]
  about: "case-appropriate forensic strategies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.6.b23, basis: inferred }
  paraphrase: "Will be able to show consistent, effective building, managing and delivering of forensic strategies suited to the case, using the Case Assessment and Interpretation framework."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.9.b1
  locator: { number: "4.9.b1", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 83061, end: 83281 }
  source: "an extensive knowledge and critical appreciation of the techniques and skills required for the collection, processing, recording (including appropriate photography), preservation and interpretation of evidence at a scene"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours) with emphasis on one area"
  addressee: learner
  verbs: []
  about: "scene investigation: techniques for evidence at a scene"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.7.b1, basis: inferred }
  paraphrase: "Will be able to show extensive knowledge and critical appreciation of the skills and techniques for collecting, processing, recording (with suitable photography), preserving and interpreting evidence at a scene."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.9.b2
  locator: { number: "4.9.b2", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 83284, end: 83516 }
  source: "a comprehensive and critical understanding of the responsibilities, roles and liabilities of those involved in a (crime) scene investigation, and a consistent ability to work effectively and contribute positively within such a team."
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours) with emphasis on one area"
  addressee: learner
  verbs: ["work", "contribute"]
  about: "scene investigation: roles, liabilities and teamwork"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.7.b2, basis: inferred }
  paraphrase: "Will be able to show comprehensive, critical understanding of the duties, roles and liabilities of everyone in a scene investigation and a consistent ability to work well and contribute within that team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.9.b3
  locator: { number: "4.9.b3", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 83540, end: 83669 }
  source: "an extensive knowledge and critical appreciation of the theory and application of the laboratory methods used in forensic science"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours) with emphasis on one area"
  addressee: learner
  verbs: []
  about: "laboratory analysis: theory and application of methods"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.7.b3, basis: inferred }
  paraphrase: "Will be able to show extensive, critical knowledge and appreciation of the theory and use of forensic laboratory methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.9.b4
  locator: { number: "4.9.b4", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 83672, end: 83974 }
  source: "consistent ability in the critical selection, use and development of a wide range of methods used in the location, identification, recovery, extraction and scientific analysis of commonly encountered physical, digital, chemical and biological materials and marks, including trace materials such as DNA."
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours) with emphasis on one area"
  addressee: learner
  verbs: ["use"]
  about: "laboratory analysis: choosing and using methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.7.b4, basis: inferred }
  paraphrase: "Will be able to show consistent skill in critically choosing, using and developing many methods to locate, identify, recover, extract and analyse common physical, digital, chemical and biological materials and marks, trace materials such as DNA included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.9.b5
  locator: { number: "4.9.b5", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 83995, end: 84279 }
  source: "an advanced knowledge and critical understanding of the principal techniques and skills required for the searching, identification, preservation, transport, handling and continuity of commonly encountered physical devices likely or known to contain digital data from a range of scenes"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours) with emphasis on one area"
  addressee: learner
  verbs: []
  about: "digital forensics: devices that hold digital data"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.7.b5, basis: inferred }
  paraphrase: "Will be able to show advanced knowledge and critical understanding of the main techniques and skills for searching for, identifying, preserving, moving, handling and keeping continuity of common devices that hold or may hold digital data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.9.b6
  locator: { number: "4.9.b6", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 84282, end: 84431 }
  source: "the consistent ability to critically select and thoroughly justify the use of a range of methods used in the acquisition and analysis of digital data"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours) with emphasis on one area"
  addressee: learner
  verbs: ["use", "select", "justify", "critically"]
  about: "digital forensics: choosing and justifying acquisition and analysis methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.7.b6, basis: inferred }
  paraphrase: "Will be able to show consistent, critical choice, fully justified, of a range of methods for acquiring and analysing digital data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.9.b7
  locator: { number: "4.9.b7", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 84434, end: 84719 }
  source: "the exceptional ability to carry out an investigation through the examination of facts from a variety of sources (including those which require additional reading or experimentation to understand their operation) relating to an incident or allegation to establish the truth of a matter"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours) with emphasis on one area"
  addressee: learner
  verbs: ["carry", "understand"]
  about: "digital forensics: investigating facts from many sources"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.7.b7, basis: inferred }
  paraphrase: "Will be able to show an exceptional investigation that examines facts from varied sources, some needing extra reading or testing to understand, to find out the truth of an incident or allegation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.9.b8
  locator: { number: "4.9.b8", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 84722, end: 84844 }
  source: "the consistent ability to critically review, validate and verify methods and tools used for the processing of digital data"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours) with emphasis on one area"
  addressee: learner
  verbs: ["review", "validate", "verify", "critically"]
  about: "digital forensics: reviewing, validating and verifying tools"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.7.b8, basis: inferred }
  paraphrase: "Will be able to show consistently and critically reviewing, validating and verifying the methods and tools that process digital data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.9.b9
  locator: { number: "4.9.b9", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 84847, end: 85005 }
  source: "the exceptional ability to construct and manage a forensic strategy, with regards to the search of multiple sites and the subsequent analysis of digital data."
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung (first-class honours) with emphasis on one area"
  addressee: learner
  verbs: ["construct", "manage"]
  about: "digital forensics: strategy across multiple sites"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/forensic-science-2022/4.7.b9, basis: inferred }
  paraphrase: "Will be able to show exceptional building and managing of a forensic strategy for searching several sites and then analysing the digital data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.10
  locator: { number: "4.10", headingPath: ["Benchmark standards", "Master's degrees (including integrated master's)"] }
  span: { start: 85079, end: 85471 }
  source: "4.10 An integrated master's degree is a combination of both bachelor's degree studies and master's level; students are therefore expected to have developed the graduate outcomes for Forensic Science associated with a degree to at least a typical level (paragraph 4.6) but will have extended their knowledge, skills and understanding into outcomes associated with aspects of a master's degree."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "integrated master's students"
  addressee: learner
  verbs: ["have"]
  about: "integrated master's: typical honours and beyond"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "An integrated master's joins bachelor's and master's study, so its students are expected to have reached at least the typical rung of the honours outcomes and will have taken their knowledge, skills and understanding on into master's-level outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.11.b1
  locator: { number: "4.11.b1", headingPath: ["Benchmark standards", "Master's degrees (including integrated master's)"] }
  span: { start: 85578, end: 85754 }
  source: "either a deep specialist knowledge and experience of techniques within a particular area of forensic science, or a wide knowledge and critical awareness of the whole discipline"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "deep specialist or broad critical knowledge"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to show either deep specialist knowledge and experience of techniques in one area of forensic science, or a broad, critical view of the discipline as a whole."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.11.b2
  locator: { number: "4.11.b2", headingPath: ["Benchmark standards", "Master's degrees (including integrated master's)"] }
  span: { start: 85757, end: 85850 }
  source: "engagement and familiarity with recent and current research methods, results and publications"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "engagement with current research"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to show active familiarity with recent and current research, its methods, findings and publications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.11.b3
  locator: { number: "4.11.b3", headingPath: ["Benchmark standards", "Master's degrees (including integrated master's)"] }
  span: { start: 85853, end: 85943 }
  source: "an effective self-critical attitude in planning, carrying out and reporting investigations"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "a self-critical approach to investigation"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to show a self-critical approach to planning, doing and reporting investigations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.11.b4
  locator: { number: "4.11.b4", headingPath: ["Benchmark standards", "Master's degrees (including integrated master's)"] }
  span: { start: 85946, end: 86064 }
  source: "the abilities and skills necessary to devise, plan, carry out and report an original investigation or research project"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["carry", "plan", "report", "devise"]
  about: "an original investigation or research project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to show the capability to conceive, plan and conduct original research or investigation and report on it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.11.b5
  locator: { number: "4.11.b5", headingPath: ["Benchmark standards", "Master's degrees (including integrated master's)"] }
  span: { start: 86067, end: 86196 }
  source: "a clear recognition of the constraints and opportunities of the environment in which professional forensic science is carried out"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "the professional setting"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to show a clear view of what limits and what opens up the setting in which professional forensic science works."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.11.b6
  locator: { number: "4.11.b6", headingPath: ["Benchmark standards", "Master's degrees (including integrated master's)"] }
  span: { start: 86199, end: 86327 }
  source: "self-direction and originality in applying and adapting problem-s olving skills to unfamiliar, complex and open-ended situations"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "independent, original problem-solving"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to show independent, original problem-solving that adapts to unfamiliar, complex and open-ended situations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.11.b7
  locator: { number: "4.11.b7", headingPath: ["Benchmark standards", "Master's degrees (including integrated master's)"] }
  span: { start: 86330, end: 86424 }
  source: "an open and innovative attitude in the ability to plan and execute new experimental procedures"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["plan", "execute"]
  about: "new experimental procedures"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to show openness and invention in planning and running new experimental procedures."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.11.b8
  locator: { number: "4.11.b8", headingPath: ["Benchmark standards", "Master's degrees (including integrated master's)"] }
  span: { start: 86427, end: 86519 }
  source: "a familiarity with the moral and ethical issues involved in the practice of forensic science"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "moral and ethical issues"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to show familiarity with the moral and ethical questions forensic practice raises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.11.b9
  locator: { number: "4.11.b9", headingPath: ["Benchmark standards", "Master's degrees (including integrated master's)"] }
  span: { start: 86522, end: 86659 }
  source: "confidence in their ability to interpret complex technical information and to communicate it in a wide variety of professional situations"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["interpret", "communicate"]
  about: "interpreting and conveying complex information"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to show confidence in interpreting complex technical information and conveying it across many professional settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/forensic-science-2022/4.11.b10
  locator: { number: "4.11.b10", headingPath: ["Benchmark standards", "Master's degrees (including integrated master's)"] }
  span: { start: 86662, end: 86744 }
  source: "the independent learning ability required for continuing professional development."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "independent learning for professional development"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to show the ability to go on learning independently for continuing professional development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/forensic-science-2022/1.4
  forPractitioner: { text: "Support and promote equity of opportunity: make the course accessible and take positive action. The paragraph also records that the professional society's accreditation scheme covers most UK courses.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.4. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/1.19, qaa/forensic-science-2022/2.2."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to equity of opportunity through inclusive practice, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/1.6.b1
  forPractitioner: { text: "Aim to help students build an enthusiasm for forensic science.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you build an enthusiasm for forensic science.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 1. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b6, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about enthusiasm for the subject. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What does this look like in your own experience of the course so far?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b2
  forPractitioner: { text: "Aim to help students have learning that stretches them intellectually and does them good.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you have learning that stretches you intellectually and does you good.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 2. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b6, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about a stimulating, worthwhile learning experience. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What does this look like in your own experience of the course so far?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b3
  forPractitioner: { text: "Aim to help students gain the scientific knowledge and skills that competent forensic practice rests on, useful also to bodies that gather or analyse physical or digital evidence.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you gain the scientific knowledge and skills that competent forensic practice rests on, useful also to bodies that gather or analyse physical or digital evidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 3. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about science underpinning practitioner competence. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b4
  forPractitioner: { text: "Aim to help students gain a sound grounding in science and laboratory and transferable skills valued in forensic work and in any organisation built on analysis, digital content or quality assurance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you gain a sound grounding in science and laboratory and transferable skills valued in forensic work and in any organisation built on analysis, digital content or quality assurance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 4. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about sound science and transferable laboratory skills. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b5
  forPractitioner: { text: "Aim to help students understand why ISO quality standards exist and what working under them involves, and why high professional and ethical standards matter at every moment if miscarriages of justice are to be avoided.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you understand why ISO quality standards exist and what working under you involves, and why high professional and ethical standards matter at every moment if miscarriages of justice are to be avoided.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 5. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about quality standards and professional ethics. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b6
  forPractitioner: { text: "Aim to help students set out data, explain scientific reasoning and defend their conclusions to expert and lay audiences.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you set out data, explain scientific reasoning and defend your conclusions to expert and lay audiences.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 6. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about communicating science to varied audiences. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b7
  forPractitioner: { text: "Aim to help students learn independently, grow professionally, and show initiative and flexibility as needs and techniques change, perhaps by keeping a structured record of their personal development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you learn independently, grow professionally, and show initiative and flexibility as needs and techniques change, perhaps by keeping a structured record of your personal development.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 7. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b5, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about independent learning and professional development. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b8
  forPractitioner: { text: "Aim to help students understand how evidence stays continuous from scene to court and beyond, why laboratory findings depend on good sampling at the scene, and how to avoid and detect contamination and cognitive bias at each stage.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you understand how evidence stays continuous from scene to court and beyond, why laboratory findings depend on good sampling at the scene, and how to avoid and detect contamination and cognitive bias at each stage.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 8. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about continuity of evidence, contamination and bias. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b9
  forPractitioner: { text: "Aim to help students become familiar with the justice system and what police, expert witnesses and lawyers need from forensic work (records, admissibility, disclosure), and with how legal systems differ in the UK and elsewhere.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you become familiar with the justice system and what police, expert witnesses and lawyers need from forensic work (records, admissibility, disclosure), and with how legal systems differ in the UK and elsewhere.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 9. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about the justice system and its demands. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b10
  forPractitioner: { text: "Aim to help students build problem-solving and research skills fit for degree study and keep aware of current and emerging forensic research.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you build problem-solving and research skills fit for degree study and keep aware of current and emerging forensic research.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 10. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about problem-solving, research and current research. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b11
  forPractitioner: { text: "Aim to help students see why sustainability and equality, diversity and inclusion matter in forensic science, as a subject and as a profession, and commit to those values.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you see why sustainability and equality, diversity and inclusion matter in forensic science, as a subject and as a profession, and commit to those values.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 11. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about sustainability and inclusion as professional values. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b12
  forPractitioner: { text: "Aim to help students grasp the forensic opportunities in a case and how they serve a forensic strategy, thinking impartially and investigating so that an enquiry moves forward.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you grasp the forensic opportunities in a case and how you serve a forensic strategy, thinking impartially and investigating so that an enquiry moves forward.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 12. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about forensic opportunities and strategy. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b13
  forPractitioner: { text: "Aim to help students see what digital forensics can offer and how the forensic specialisms together get the most from the evidence.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you see what digital forensics can offer and how the forensic specialisms together get the most from the evidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 13. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about digital forensic opportunities. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b14
  forPractitioner: { text: "Aim to help students build investigative skills, such as finding lines of enquiry, sources of evidence and artefacts and seeing how they connect.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you build investigative skills, such as finding lines of enquiry, sources of evidence and artefacts and seeing how you connect.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 14. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about investigative skills. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b15
  forPractitioner: { text: "Aim to help students review information critically, published science above all.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you review information critically, published science above all.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 15. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about critical review of information and literature. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b16
  forPractitioner: { text: "Aim to help students understand the scientific method and the worth of experiment, and judge findings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you understand the scientific method and the worth of experiment, and judge findings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 16. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about the scientific method. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b17
  forPractitioner: { text: "Aim to help students see how evidence from a scene, the investigation, the analysis and the court case link together.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you see how evidence from a scene, the investigation, the analysis and the court case link together.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 17. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about from scene to court. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.6.b18
  forPractitioner: { text: "Aim to help students understand a forensic professional's duty to the court and what an expert witness does.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should aim to help you understand a forensic professional's duty to the court and what an expert witness does.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.6, item 18. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about duty to the court and the expert witness. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.7.b1
  forPractitioner: { text: "At master's level, aim also to help students gain deep knowledge and hands-on experience of forensic examination and analytical techniques and their use in chosen specialisms.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also aim to help you gain deep knowledge and hands-on experience of forensic examination and analytical techniques and your use in chosen specialisms.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.7, item 1. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b1 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about deep knowledge of techniques in a specialism. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.7.b2
  forPractitioner: { text: "At master's level, aim also to help students engage critically with the research methods and techniques in use today.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also aim to help you engage critically with the research methods and techniques in use today.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.7, item 2. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b1 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about critical engagement with research methods. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.7.b3
  forPractitioner: { text: "At master's level, aim also to help students conceive, plan, conduct and report a sizeable original research project in an academic setting.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also aim to help you conceive, plan, conduct and report a sizeable original research project in an academic setting.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.7, item 3. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b3 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about an extended original research project. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.7.b4
  forPractitioner: { text: "At master's level, aim also to help students see clearly what limits and what opens up professional forensic science today.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also aim to help you see clearly what limits and what opens up professional forensic science today.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.7, item 4. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b1 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about the professional setting, its limits and openings. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.7.b5
  forPractitioner: { text: "At master's level, aim also to help students work within a quality standards framework.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also aim to help you work within a quality standards framework.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.7, item 5. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b3 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about working to a quality standards framework. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.7.b6
  forPractitioner: { text: "At master's level, aim also to help students be better prepared to enter professional work or doctoral study.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also aim to help you be better prepared to enter professional work or doctoral study.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.7, item 6. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b6 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about readiness for employment or doctoral study. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.7.b7
  forPractitioner: { text: "At master's level, aim also to help students keep learning on their own for continuing professional development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also aim to help you keep learning on your own for continuing professional development.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.7, item 7. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b7 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about independent learning for professional development. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.8
  forPractitioner: { text: "Check the course against the qualification descriptors of the national framework that applies (the FHEQ, or the FQHEIS in Scotland); for master's courses, QAA's guidance on master's degree types may help.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's and integrated master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.8. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/2.5, qaa/forensic-science-2022/2.7, qaa/forensic-science-2022/4.2 and qaa/fheq-2024/4.15.i1 and qaa/fheq-2024/4.17.i1."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to matching national qualification descriptors, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/1.17
  forPractitioner: { text: "Teach that reports and witness statements must be robust, transparent, logical and free of bias, and should keep factual reporting apart from expert opinion, as part of reliable recording, case-based interpretation and impartial presentation of findings and their uncertainty.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Any report or witness statement you write must be robust, transparent, logical and free of bias, and should keep the facts apart from your expert opinion.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a firm requirement (must) on professional reporting, taught as part of the course, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.17. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/3.13, qaa/forensic-science-2022/4.4.b20, qaa/forensic-science-2022/4.4.b18 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when a student is writing a report, a case file or a mock witness statement. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.19
  forPractitioner: { text: "Read the course against the Equality Act 2010 and the public sector equality duty; staff and students alike carry a responsibility to secure equal opportunity for everyone.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You share, with staff and other students, a responsibility to make sure everyone has an equal chance, whatever their background, ability, culture, gender or identity.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an expectation the statement gives without one of the five obliging words, so its force is descriptive, for the bachelor's with honours and master's degrees at the level each award sits at. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.19. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/1.4, qaa/forensic-science-2022/3.26.b8, qaa/forensic-science-2022/3.28.b5."
  author-agent-dialogue: "Raise this when someone asks about a shared responsibility for equal opportunity. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What does this look like in your own experience of the course so far?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/1.23
  forPractitioner: { text: "Build education for sustainable development into teaching, equip staff to mainstream it, and embed critical thinking and problem-solving so students can handle uncertainty and risk; for forensic students it also means keeping skills current through professional development. Student-centred, inquiry-based teaching suits it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student-facing aim is 1.6, item 11", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.23. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/1.24, qaa/forensic-science-2022/1.6.b11."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to embedding education for sustainable development, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/1.24
  forPractitioner: { text: "Interpret education for sustainable development through the Advance HE and QAA guidance (std:doc:qaa-advancehe-esd-2021-guidance).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.24. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/1.23, std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to reading sustainability through the national guidance, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/1.25
  forPractitioner: { text: "Make enterprise activities ambitious: they should require students to tackle forensic problems creatively, innovatively, resiliently and critically, to generate ideas and to communicate issues; tie them to placements and outside organisations.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design; the student-facing outcome is 1.27", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.25. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/1.27, qaa/forensic-science-2022/1.26."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to ambitious enterprise activities, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/1.27
  forPractitioner: { text: "Equip students to spot openings to develop a business or improve a process, whether in their studies, through partnerships or on placement.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to spot chances to develop a business or improve how things are done, in your studies, partnerships or placements.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 1.27. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/1.25, qaa/forensic-science-2022/2.11 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about spotting openings for business or process improvement. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/2.1
  forPractitioner: { text: "Align curriculum and assessment with the stated outcomes; keep outcomes and content current with what employers need, with research, and with input from partners such as police forces, forensic science providers, other investigators and the judiciary; and scaffold learning towards independence.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 2.1. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/3.6, qaa/forensic-science-2022/2.11."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to curriculum aligned to outcomes, employers and research, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/2.2
  forPractitioner: { text: "Make every part of the course accessible, including physical access, awareness of culture and language, and sensitivity towards victims of crime; build in reasonable adjustments; and vary teaching widely, for instance practicals with adjustments, individual risk assessments, accessible facilities, peer support and placements.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 2.2. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/2.3, qaa/forensic-science-2022/3.29, qaa/forensic-science-2022/3.31."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to accessibility across the whole course, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/2.3
  forPractitioner: { text: "Make all digital course content, text, images and sound alike, accessible and understandable to everyone, following W3C guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 2.3. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/2.2, qaa/forensic-science-2022/3.31."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to digital accessibility of course content, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/2.6
  forPractitioner: { text: "Joint honours students will reach the core of the subject's specific and generic skills and add others from the partner subject; leave room for interdisciplinary work where they meet.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study forensic science as part of a joint honours degree, you will achieve its core specific and generic skills, add others from your other subject, and may explore where the two meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement says students will reach, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 2.6. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4, qaa/forensic-science-2022/2.5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about joint honours: the core skills of the subject. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/2.9
  forPractitioner: { text: "Where you can, offer full-time, part-time and distance routes and consider blended or HyFlex delivery that mixes classroom, online and workplace learning, so that more people can take part and students have choice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 2.9. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/2.10, qaa/forensic-science-2022/3.7."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to flexible modes of study, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/2.10
  forPractitioner: { text: "Plan how to support students with protected characteristics or changed circumstances to complete, and keep a contingency for an abrupt move to online delivery, which may mean regrouping practical work into blocks.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 2.10. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/2.9, qaa/forensic-science-2022/1.19."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to support plans and delivery contingency, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/2.11
  forPractitioner: { text: "Build links with forensic employers (police and other law enforcement, private forensic service providers) and other organisations, so course work connects with real workplaces and students develop self-reliance, critical thinking, teamwork and problem-solving.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 2.11. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/2.12, qaa/forensic-science-2022/2.13, qaa/forensic-science-2022/1.27."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to partnerships with forensic employers, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/2.13
  forPractitioner: { text: "Give any placement a clear programme of learning; typical placement work includes quality assurance, data analysis, basic examination, administering evidence and set projects.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you choose a work placement, it should come with a clear programme of learning, often covering tasks such as quality checks, data analysis, basic examinations and handling evidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at the level each award sits at. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 2.13. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/2.11, qaa/forensic-science-2022/2.12."
  author-agent-dialogue: "Raise this when a student is weighing up a placement or a programme team is setting one up. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What does this look like in your own experience of the course so far?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/2.14
  forPractitioner: { text: "Use this statement, with the other external reference points, in monitoring and periodic review to keep the course in line with sector norms.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (will), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 2.14. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/2.16, qaa/forensic-science-2022/2.17, qaa/forensic-science-2022/2.18."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to external reference points in review, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/2.15
  forPractitioner: { text: "Work with external examiners, student cohorts and partners, and stay close to bodies such as the Forensic Science Regulator and the Chartered Society of Forensic Sciences, so that content stays relevant.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (will), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 2.15. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/2.14, qaa/forensic-science-2022/3.1."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to collaboration with examiners, students and professional bodies, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/2.16
  forPractitioner: { text: "Bring external reviewers into periodic review to test proposed changes, confirm threshold standards and check that content suits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (will), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 2.16. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/2.14, qaa/forensic-science-2022/2.17, qaa/forensic-science-2022/4.2."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to external reviewers in periodic review, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/2.18
  forPractitioner: { text: "Identify the right stakeholders in monitoring and evaluation, share what you learn about learning, teaching and assessment, and expect professional accreditation through visits and desk review.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 2.18. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/2.14, qaa/forensic-science-2022/2.15, qaa/forensic-science-2022/1.4."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to stakeholders and findings in monitoring, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/3.3
  forPractitioner: { text: "Combine approaches (pedagogy and andragogy) so learners grow in knowledge and in academic and professional skill: lectures, practicals, seminars, mock scenes and courtrooms, case studies, debates, fieldwork, problem-based and work-based learning among them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.3. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/3.4, qaa/forensic-science-2022/3.7."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to a mix of teaching and learning practices, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/3.4
  forPractitioner: { text: "Use practicals to support taught content and build transferable technical skill: forensic experimental methods and their basis, data handling and statistics for probabilistic inference, and contemporaneous records and reports.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.4. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/3.3, qaa/forensic-science-2022/3.18, qaa/forensic-science-2022/3.22.b1."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to practical classes and their purpose, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/3.5
  forPractitioner: { text: "At master's level, expect experience of research methods, reading and interpreting research publications, and an extended project written up as an independent original report, for example as a journal article or a thesis.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "On a master's course, you can expect to use research methods, read and interpret research papers, and complete an extended project written up as your own original report.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an expectation the statement gives without one of the five obliging words, so its force is descriptive, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.5. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/1.7.b3, qaa/forensic-science-2022/3.23.b4, qaa/forensic-science-2022/4.11.b4 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b3 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about research methods and an extended project at master's level. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.6
  forPractitioner: { text: "Design teaching around the stated outcomes and aligned assessment, review it as pedagogy and technology advance, keep teaching staff current through regular professional development, and ground content in current research, innovation, practice and regulation.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.6. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/2.1, qaa/forensic-science-2022/3.7."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to design for outcomes; current staff and content, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/3.7
  forPractitioner: { text: "Make sessions student-centred and active where you can, and use hardware and software to give students more chances to apply what they know to problems, whatever the mode of delivery.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.7. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/2.9, qaa/forensic-science-2022/3.3."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to student-centred, active delivery, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/3.8.b1
  forPractitioner: { text: "Across the whole process from scene to court, students should work safely and show an understanding of current ISO standards, the law and the Forensic Science Regulator's codes and guidance, impartiality and disclosure included.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "From scene to court, you should work safely and show an understanding of current ISO standards, the law and the Forensic Science Regulator's codes and guidance, impartiality and disclosure included.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.8, item 1. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/1.6.b5, qaa/forensic-science-2022/4.4.b21 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about standards, law and the Regulator's codes. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.8.b2
  forPractitioner: { text: "Across the whole process from scene to court, students should work safely and show familiarity with professional ethics: respect for the codes of practice and conduct, the standards and rules, and their responsibilities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "From scene to court, you should work safely and show familiarity with professional ethics: respect for the codes of practice and conduct, the standards and rules, and your responsibilities.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.8, item 2. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/3.28, qaa/forensic-science-2022/4.4.b12 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about professional ethics and codes. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.8.b3
  forPractitioner: { text: "Across the whole process from scene to court, students should work safely and show knowledge and understanding of the kinds of cognitive bias, what they lead to (cumulative effects included) and how to reduce them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "From scene to court, you should work safely and show knowledge and understanding of the kinds of cognitive bias, what you lead to (cumulative effects included) and how to reduce them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.8, item 3. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b5, qaa/forensic-science-2022/1.6.b8 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about cognitive bias and its mitigation. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.8.b4
  forPractitioner: { text: "Across the whole process from scene to court, students should work safely and show an understanding of approaches such as Case Assessment and Interpretation and the ability to use them in building and delivering a forensic strategy.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "From scene to court, you should work safely and show an understanding of approaches such as Case Assessment and Interpretation and the ability to use you in building and delivering a forensic strategy.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.8, item 4. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b22, qaa/forensic-science-2022/3.24.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about Case Assessment and Interpretation in forensic strategy. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.9
  forPractitioner: { text: "Students should come to know the UK criminal justice and legal systems and appreciate systems abroad: adversarial and inquisitorial models, the place of forensic science and the expert witness (defence scientists included), and the legal standards that govern evidence from recovery to disposal.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should come to know how the UK's criminal justice and legal systems work and how others differ, how forensic scientists and expert witnesses fit into them, and the legal rules for handling evidence from recovery to disposal.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.9. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/1.6.b9, qaa/forensic-science-2022/3.20, qaa/forensic-science-2022/4.4.b8 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about criminal justice and legal systems. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.10
  forPractitioner: { text: "Whatever the course's emphasis, make sure every student gains at least a basic knowledge of all three components: scene investigation, laboratory analysis, and interpreting, evaluating and presenting evidence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "Whatever your course focuses on, you will need at least a basic knowledge of all three areas: scene investigation, laboratory analysis, and interpreting, evaluating and presenting evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the floor every graduate of the award reaches, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.10. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/1.14, qaa/forensic-science-2022/3.11, qaa/forensic-science-2022/3.12, qaa/forensic-science-2022/3.13 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about basic knowledge of all three components. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.11
  forPractitioner: { text: "Students will come to understand, as suits the course, imaging and scene photography and the roles, duties and liabilities of everyone at a scene and how they exchange information, within safe, contamination-aware scene strategy.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will learn, as your course requires, how imaging and scene photography work, who does what at a scene, what each is responsible and liable for, and how they share information.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement says students will reach, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.11. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.5.b1, qaa/forensic-science-2022/4.5.b2, qaa/forensic-science-2022/3.24.b3 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about scene investigation: imaging, roles and information exchange. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.12
  forPractitioner: { text: "Students will know the principles and use of control and reference samples and of identification databases, alongside competent, safe, validated and calibrated use of the main laboratory methods.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how control and reference samples work and how databases help identify materials, alongside using the main laboratory methods safely, with proper validation and calibration.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement says students will reach, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.12. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.5.b3, qaa/forensic-science-2022/4.5.b4, qaa/forensic-science-2022/3.22.b1 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about laboratory methods, control samples and databases. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.13
  forPractitioner: { text: "Students will be able to interpret findings and reach conclusions, separate factual from expert reporting, form expert opinion, write impartial reports for investigators and the court in different formats, and defend a report orally and in writing, using likelihood-ratio evaluation and an understanding of uncertainty.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to interpret findings and draw conclusions, keep the facts apart from expert opinion, write impartial reports for investigators and courts, and explain and defend your report in court, in speech and in writing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement says students will reach, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.13. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/1.17, qaa/forensic-science-2022/4.4.b17, qaa/forensic-science-2022/4.4.b18, qaa/forensic-science-2022/4.4.b20 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about interpreting, reporting and defending findings. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.14
  forPractitioner: { text: "Make sure students gain basic knowledge of the sciences the course rests on (chemistry, biology, physics, mathematics, computer science, law); digital forensics courses need their own scientific and mathematical grounding.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to gain a basic knowledge of the sciences your course rests on, such as chemistry, biology, physics, mathematics, computing and law.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an expectation the statement gives without one of the five obliging words, so its force is descriptive, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.14. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/3.15, qaa/forensic-science-2022/3.16, qaa/forensic-science-2022/3.17, qaa/forensic-science-2022/3.18, qaa/forensic-science-2022/3.19, qaa/forensic-science-2022/3.20, qaa/forensic-science-2022/4.4.b1 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about the underpinning sciences. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.15
  forPractitioner: { text: "Students should be able to choose, apply and interpret analytical and microscopic techniques for forensic samples, and understand how the techniques work, where their limits lie and what chemical interactions are involved.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "In chemistry, you should be able to choose and use analytical and microscope techniques, interpret their data to identify and compare materials, and understand how the techniques work and where their limits lie.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.15. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/3.14, qaa/forensic-science-2022/4.4.b4, qaa/forensic-science-2022/4.5.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about chemistry: analytical and microscopic techniques. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.16
  forPractitioner: { text: "Include in biology practical microscopy, molecular biology and biochemistry with stress on body fluid identification and genetics, and STR profiling; anatomy, forensic medicine and fields such as entomology or palynology are options.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a content duty on the course; the student meets it as curriculum", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.16. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/3.14, qaa/forensic-science-2022/3.15, qaa/forensic-science-2022/3.17."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to biology in the curriculum, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/3.17
  forPractitioner: { text: "Teach the physics forensic work draws on: optics and microscopy, mechanics for ballistics, explosions and bloodstain dynamics, material properties, and the electromagnetism, atomic structure and radiation that instrumental analysis and imaging rely on.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a content duty on the course; the student meets it as curriculum", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.17. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/3.14, qaa/forensic-science-2022/3.16, qaa/forensic-science-2022/3.18."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to physics in the curriculum, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/3.18
  forPractitioner: { text: "Teach enough functions, algebra and trigonometry for the science, and working statistics: probability, experimental uncertainty, sampling and method uncertainty, and likelihood-ratio evaluation of evidence for court using frequency data and databases.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a content duty on the course; the student meets it as curriculum", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.18. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/3.14, qaa/forensic-science-2022/4.4.b1, qaa/forensic-science-2022/4.4.b18."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to mathematics and statistics in the curriculum, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/3.19
  forPractitioner: { text: "Ground digital forensics in computer science (data representation, a programming language such as Python, networks and protocols, security, relational databases) and build up to reverse engineering unfamiliar data, timelines from linked artefacts, and weighing circumstantial against probative evidence.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a content duty on the course; the student meets it as curriculum", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.19. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/3.14, qaa/forensic-science-2022/4.5.b5, qaa/forensic-science-2022/4.5.b6, qaa/forensic-science-2022/4.5.b8."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to digital forensics in the curriculum, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/3.20
  forPractitioner: { text: "Cover criminal law, jurisdiction and procedure, the expert witness's role, and the legislation that governs practice, such as the Data Protection Act 2018, PACE 1984 and the criminal procedure rules.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a content duty on the course; the student meets it as curriculum", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (describes), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.20. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/3.9, qaa/forensic-science-2022/3.14, qaa/forensic-science-2022/4.4.b8."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to law in the curriculum, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/3.22.b1
  forPractitioner: { text: "Design the course so that students can work safely and well in a laboratory: assessing risk competently, following written procedures, calibrating where needed and recording methods and results reliably.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you work safely and well in a laboratory: assessing risk competently, following written procedures, calibrating where needed and recording methods and results reliably.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.22, item 1. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b3, qaa/forensic-science-2022/4.4.b14 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about safe, effective laboratory work. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.22.b2
  forPractitioner: { text: "Design the course so that students can use advanced laboratory equipment with confidence where it applies, learn new facilities, and understand the principles behind the instruments.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you use advanced laboratory equipment with confidence where it applies, learn new facilities, and understand the principles behind the instruments.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.22, item 2. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about advanced equipment and instrument principles. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.22.b3
  forPractitioner: { text: "Design the course so that students can see why tasks must be done consistently, reproducibly and traceably.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you see why tasks must be done consistently, reproducibly and traceably.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.22, item 3. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b15, qaa/forensic-science-2022/3.24.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about consistent, reproducible, traceable work. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.22.b4
  forPractitioner: { text: "Design the course so that students can evaluate and critically interpret results by solving problems: finding the relevant scientific principles, planning how to solve them and presenting conclusions as text, tables or graphs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you evaluate and critically interpret results by solving problems: finding the relevant scientific principles, planning how to solve you and presenting conclusions as text, tables or graphs.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.22, item 4. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b7 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about interpreting results through problem-solving. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.22.b5
  forPractitioner: { text: "Design the course so that students can plan, carry out and report a scientific investigation, analysing the data critically and judging how uncertain it is.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you plan, carry out and report a scientific investigation, analysing the data critically and judging how uncertain it is.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.22, item 5. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b19, qaa/forensic-science-2022/4.4.b10 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about planning and reporting an investigation. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.22.b6
  forPractitioner: { text: "Design the course so that students can use scientific method on scientific problems, forming a hypothesis and designing experiments to test it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you use scientific method on scientific problems, forming a hypothesis and designing experiments to test it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.22, item 6. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/1.6.b16, qaa/forensic-science-2022/4.4.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about hypotheses and experimental design. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.22.b7
  forPractitioner: { text: "Design the course so that students can analyse and organise data with ICT, using the software that goes with instruments and working with databases.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you analyse and organise data with ICT, using the software that goes with instruments and working with databases.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.22, item 7. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/3.26.b5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about ICT for data analysis. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.23.b1
  forPractitioner: { text: "Design the master's course so that, beyond the honours abilities, students can work safely and well in a laboratory with little direct supervision.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also help you work safely and well in a laboratory with little direct supervision.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.23, item 1. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/3.22.b1, qaa/forensic-science-2022/4.11.b7 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b3 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about laboratory work with minimal supervision. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.23.b2
  forPractitioner: { text: "Design the master's course so that, beyond the honours abilities, students can apply and adapt problem-solving to situations that are unfamiliar, complex, poorly defined and open-ended.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also help you apply and adapt problem-solving to situations that are unfamiliar, complex, poorly defined and open-ended.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.23, item 2. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/4.11.b6, qaa/forensic-science-2022/3.27.b1 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b6 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about problem-solving in unfamiliar, open-ended situations. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.23.b3
  forPractitioner: { text: "Design the master's course so that, beyond the honours abilities, students can plan, design and run new experimental procedures on their own.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also help you plan, design and run new experimental procedures on your own.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.23, item 3. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/4.11.b7 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b3 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about designing new experimental procedures. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.23.b4
  forPractitioner: { text: "Design the master's course so that, beyond the honours abilities, students can plan, design, conduct and report a research project on their own.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also help you plan, design, conduct and report a research project on your own.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.23, item 4. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/4.11.b4, qaa/forensic-science-2022/3.5 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b3 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about an independent research project. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.24.b1
  forPractitioner: { text: "Design the course so that students can see why standards and codes of conduct are needed and why keeping to them matters.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you see why standards and codes of conduct are needed and why keeping to you matters.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.24, item 1. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/3.8.b1, qaa/forensic-science-2022/4.4.b15 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about why standards and codes matter. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.24.b2
  forPractitioner: { text: "Design the course so that students can work well in a team and inside a formal system, following the relevant quality assurance procedures.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you work well in a team and inside a formal system, following the relevant quality assurance procedures.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.24, item 2. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.5.b2, qaa/forensic-science-2022/4.4.b15 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about teamwork within a quality system. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.24.b3
  forPractitioner: { text: "Design the course so that students can record, recover, analyse, evaluate, interpret, preserve and present potential evidence.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you record, recover, analyse, evaluate, interpret, preserve and present potential evidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.24, item 3. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.5.b1, qaa/forensic-science-2022/4.4.b17 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about the handling of potential evidence from record to presentation. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.24.b4
  forPractitioner: { text: "Design the course so that students can build efficient strategies for examining a case.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you build efficient strategies for examining a case.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.24, item 4. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b22, qaa/forensic-science-2022/3.8.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about case-examination strategies. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.24.b5
  forPractitioner: { text: "Design the course so that students can apply competent procedures that keep evidence intact and its continuity unbroken.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you apply competent procedures that keep evidence intact and its continuity unbroken.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.24, item 5. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b23, qaa/forensic-science-2022/1.6.b8 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about integrity and continuity of evidence. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.24.b6
  forPractitioner: { text: "Design the course so that students can present impartially, in writing and in speech, in ways suited to legal, court and policing settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you present impartially, in writing and in speech, in ways suited to legal, court and policing settings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.24, item 6. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b20, qaa/forensic-science-2022/1.17 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about impartial presentation for legal settings. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.24.b7
  forPractitioner: { text: "Design the course so that students can keep to safe working practice, for themselves and others.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you keep to safe working practice, for yourself and others.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.24, item 7. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b14 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about safe working practice. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.24.b8
  forPractitioner: { text: "Design the course so that students can appreciate the particular issues, legal framework and practice for digital evidence and trace materials, human and other biological tissue and DNA included, with reference to the Human Tissue Act 2004.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you appreciate the particular issues, legal framework and practice for digital evidence and trace materials, human and other biological tissue and DNA included, with reference to the Human Tissue Act 2004.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.24, item 8. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b13 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about digital evidence, trace materials and the Human Tissue Act. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.24.b9
  forPractitioner: { text: "Design the course so that students can be aware of what modern technology, databases and digital forensics (such as data taken from phones and computers) mean for the field.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you be aware of what modern technology, databases and digital forensics (such as data taken from phones and computers) mean for the field.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.24, item 9. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/1.6.b13, qaa/forensic-science-2022/4.5.b5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about implications of technological advances. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.24.b10
  forPractitioner: { text: "Design the course so that students can appreciate a forensic practitioner's ethical, legal and commercial responsibilities and the quality assurance and validation that professional competence requires.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you appreciate a forensic practitioner's ethical, legal and commercial responsibilities and the quality assurance and validation that professional competence requires.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.24, item 10. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b12, qaa/forensic-science-2022/4.4.b15 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about practitioner responsibilities, quality and validation. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.25.b1
  forPractitioner: { text: "Design the master's course so that, beyond the honours abilities, students can gain deep experience of an apt range of forensic methods and take a critical approach to them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also help you gain deep experience of an apt range of forensic methods and take a critical approach to them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.25, item 1. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/4.11.b1, qaa/forensic-science-2022/1.7.b1 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b3 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about deep, critical experience of forensic methods. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.25.b2
  forPractitioner: { text: "Design the master's course so that, beyond the honours abilities, students can be open and inventive towards new and emerging forensic procedures and techniques.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also help you be open and inventive towards new and emerging forensic procedures and techniques.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.25, item 2. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/4.11.b7 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b3 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about openness to new procedures and techniques. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.25.b3
  forPractitioner: { text: "Design the master's course so that, beyond the honours abilities, students can understand the moral and ethical questions forensic practice raises.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also help you understand the moral and ethical questions forensic practice raises.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.25, item 3. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/4.11.b8, qaa/forensic-science-2022/3.28 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b1 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about moral and ethical issues in practice. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.26.b1
  forPractitioner: { text: "Design the course so that students can build personal and academic resilience by paying attention to their own well-being and that of others.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you build personal and academic resilience by paying attention to your own well-being and that of others.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.26, item 1. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b16 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about resilience and well-being. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.26.b2
  forPractitioner: { text: "Design the course so that students can investigate on their own, drawing on many sources of information and using critical judgement.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you investigate on your own, drawing on many sources of information and using critical judgement.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.26, item 2. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.5.b7, qaa/forensic-science-2022/1.6.b14 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b7, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about independent investigation from many sources. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.26.b3
  forPractitioner: { text: "Design the course so that students can communicate complex ideas and information concisely and well, orally and in writing, and interact effectively across many professional settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you communicate complex ideas and information concisely and well, orally and in writing, and interact effectively across many professional settings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.26, item 3. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b16, qaa/forensic-science-2022/4.4.b20 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about communication across professional settings. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.26.b4
  forPractitioner: { text: "Design the course so that students can analyse with attention to detail, build logical arguments from incomplete data and use technical language correctly.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you analyse with attention to detail, build logical arguments from incomplete data and use technical language correctly.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.26, item 4. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b10, qaa/forensic-science-2022/4.4.b18 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b7, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about analytical skills. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.26.b5
  forPractitioner: { text: "Design the course so that students can use ICT well, including databases, software packages and modern means of communication.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you use ICT well, including databases, software packages and modern means of communication.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.26, item 5. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/3.22.b7 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about ICT skills. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.26.b6
  forPractitioner: { text: "Design the course so that students can work alone and in a team, and plan, organise and complete work efficiently, conscientiously and on time.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you work alone and in a team, and plan, organise and complete work efficiently, conscientiously and on time.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.26, item 6. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/3.24.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about independent and team working; managing time. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.26.b7
  forPractitioner: { text: "Design the course so that students can see where further training or new skills would help them improve, and reflect on it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you see where further training or new skills would help you improve, and reflect on it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.26, item 7. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/1.6.b7 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b5, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about reflective personal development. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.26.b8
  forPractitioner: { text: "Design the course so that students can understand how to put good practice in equality, diversity and inclusion into effect.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you understand how to put good practice in equality, diversity and inclusion into effect.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.26, item 8. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/1.19, qaa/forensic-science-2022/3.28.b5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about applying good practice in equality, diversity and inclusion. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.27.b1
  forPractitioner: { text: "Design the master's course so that, beyond the honours abilities, students can solve problems with self-direction and originality.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also help you solve problems with self-direction and originality.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.27, item 1. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/4.11.b6, qaa/forensic-science-2022/3.23.b2 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b6 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about self-directed, original problem-solving. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.27.b2
  forPractitioner: { text: "Design the master's course so that, beyond the honours abilities, students can take a self-critical approach to planning, doing and reporting investigations.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also help you take a self-critical approach to planning, doing and reporting investigations.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.27, item 2. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/4.11.b3 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b6 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about a self-critical approach to investigation. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.27.b3
  forPractitioner: { text: "Design the master's course so that, beyond the honours abilities, students can interpret complex technical information with competence and convey it across a wide variety of professional settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also help you interpret complex technical information with competence and convey it across a wide variety of professional settings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.27, item 3. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/4.11.b9 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b5 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about interpreting and conveying complex information. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.27.b4
  forPractitioner: { text: "Design the master's course so that, beyond the honours abilities, students can keep learning on their own for continuing professional development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a master's, your course should also help you keep learning on your own for continuing professional development.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.27, item 4. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/4.11.b10, qaa/forensic-science-2022/1.7.b7 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b7 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about independent learning for professional development. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.28
  forPractitioner: { text: "Make sure students fully understand, and course materials state, that fabricating, falsifying, misrepresenting or wilfully misreading evidence, data or results is unethical and unacceptable.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should fully understand that making up, falsifying, misrepresenting or deliberately misreading evidence, data or experimental results is unethical and never acceptable.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.28. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/3.28.b2, qaa/forensic-science-2022/4.4.b12, qaa/forensic-science-2022/1.6.b5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about fabrication and misrepresentation are unethical. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.28.b1
  forPractitioner: { text: "Expect students, and help them, to understand how serious the results of careless or poor practice can be.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should also understand how serious the results of careless or poor practice can be.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.28, item 1. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b14, qaa/forensic-science-2022/4.4.b23 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about consequences of careless practice. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.28.b2
  forPractitioner: { text: "Expect students, and help them, to be objective, impartial and honest in every part of their work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should also be objective, impartial and honest in every part of your work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.28, item 2. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b20, qaa/forensic-science-2022/3.24.b6 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about objectivity and honesty. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.28.b3
  forPractitioner: { text: "Expect students, and help them, to recognise and admit where their knowledge ends.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should also recognise and admit where your knowledge ends.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.28, item 3. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/4.4.b7 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about the limits of one's knowledge. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.28.b4
  forPractitioner: { text: "Expect students, and help them, to recognise plagiarism as unethical conduct.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should also recognise plagiarism as unethical conduct.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.28, item 4. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/3.28 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about plagiarism as unethical. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.28.b5
  forPractitioner: { text: "Expect students, and help them, to know the law on equality and diversity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should also know the law on equality and diversity.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.28, item 5. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/1.19, qaa/forensic-science-2022/3.26.b8 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about equality and diversity legislation. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.28.b6
  forPractitioner: { text: "Expect students, and help them, to know the ethical questions, legal rules and procedures in research, especially with animals or people or with a person's data.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should also know the ethical questions, legal rules and procedures in research, especially with animals or people or with a person's data.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation stated with should, which a course is meant to enable rather than a pass condition, for the bachelor's with honours and master's degrees at fheq:6 (fheq:7 for the master's). Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.28, item 6. Do not claim it is a regulatory requirement or that it replaces the graded standards in 4.4 to 4.11. Set it beside qaa/forensic-science-2022/3.24.b8, qaa/forensic-science-2022/4.4.b13 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6."
  author-agent-dialogue: "Raise this when someone asks about research ethics and data. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/3.29
  forPractitioner: { text: "Use a wide mix of assessment formats, formative and summative, in person or online, and make reasonable adjustments for disabled students across all assessment, as their needs require.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.29. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/3.31, qaa/forensic-science-2022/2.2."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to varied assessment and reasonable adjustments, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/3.30
  forPractitioner: { text: "Assess knowledge and both kinds of skill named in the outcomes; include some timed tasks testing organisation and communication under pressure, and some that let students show reflection, originality, creativity and knowledge put into practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (will), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.30. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/3.29, qaa/forensic-science-2022/3.31, qaa/forensic-science-2022/4.2."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to what assessment tests, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/3.31
  forPractitioner: { text: "Issue a brief with criteria mapped to the outcomes; design assessments inclusively from the start, with digital accessibility good practice and attention to needs such as hearing impairment and colour blindness; and make sure any alternative still lets students show the outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.31. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/3.29, qaa/forensic-science-2022/2.2, qaa/forensic-science-2022/2.3."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to briefs, criteria and inclusive assessment design, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/3.33
  forPractitioner: { text: "Return feedback promptly, and build in visible points where students make and carry out action plans for their development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours and master's courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 3.33. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/3.32, qaa/forensic-science-2022/3.26.b7."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to prompt feedback and action planning, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/4.2
  forPractitioner: { text: "Read the three rungs as individual performance: the threshold is what every honours graduate reaches and typical is where most should land; set your own evidence of achievement and refer to Annex D of the frameworks for the four classes (1st, 2:1, 2:2, 3rd).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its team; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course and the team that runs it (should), not as an outcome students must show. It applies to bachelor's with honours courses in forensic science; cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.2. Do not present it as a regulatory requirement or as the student's own obligation. Read it beside qaa/forensic-science-2022/4.4, qaa/forensic-science-2022/4.6, qaa/forensic-science-2022/4.8 and qaa/fheq-2024/annex-d/summary/r1/3rd and SL6 of std:doc:qaa-fheq-2024-framework."
  author-agent-dialogue: "Raise this with a programme team or teacher when the talk turns to the three rungs and Annex D, and keep it in course-design terms. Ask: \"Where in the course is this done or checked now, and what evidence would show it?\" Do not read the issuer's text out at length, and do not hand it to a student as a duty of theirs."
- statement: qaa/forensic-science-2022/4.4.b1
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show knowledge and understanding of the sciences that forensic investigation draws on, mathematics and statistics among them, with Bayesian reasoning and likelihood ratios.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show knowledge and understanding of the sciences that forensic investigation draws on, mathematics and statistics among you, with Bayesian reasoning and likelihood ratios.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 1. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b1, qaa/forensic-science-2022/4.8.b1 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about the sciences, mathematics and statistics behind forensic work. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b2
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show knowledge of the techniques forensic science uses.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show knowledge of the techniques forensic science uses.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 2. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b2, qaa/forensic-science-2022/4.8.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about forensic techniques. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b3
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show laboratory skills for a range of tasks and technical processes, done with some autonomy.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show laboratory skills for a range of tasks and technical processes, done with some autonomy.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 3. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b3, qaa/forensic-science-2022/4.8.b3 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about laboratory skills and autonomy. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b4
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show choosing and running practical laboratory experiments for forensic investigations, using suitable equipment.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show choosing and running practical laboratory experiments for forensic investigations, using suitable equipment.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 4. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b4, qaa/forensic-science-2022/4.8.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about choosing and running laboratory experiments. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b5
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show knowledge of the kinds of cognitive bias and how they can distort forensic processes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show knowledge of the kinds of cognitive bias and how you can distort forensic processes.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 5. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b5, qaa/forensic-science-2022/4.8.b5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise this when someone asks about cognitive bias in forensic processes. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b6
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show a range of knowledge of the broad issues and methods of scene investigation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show a range of knowledge of the broad issues and methods of scene investigation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 6. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b6, qaa/forensic-science-2022/4.8.b6 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about scene investigation issues and techniques. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b7
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show interpretation of laboratory and other results with a sense of their limits, with the hierarchy of propositions and hypotheses at activity level.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show interpretation of laboratory and other results with a sense of your limits, with the hierarchy of propositions and hypotheses at activity level.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 7. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b7, qaa/forensic-science-2022/4.8.b7 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about interpreting results within their limits. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b8
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show knowledge of the legal and policing settings in which forensic science is practised, work across jurisdictions included.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show knowledge of the legal and policing settings in which forensic science is practised, work across jurisdictions included.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 8. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b8, qaa/forensic-science-2022/4.8.b8 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about legal and law enforcement settings of practice. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b9
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show understanding of how the intelligence value of a forensic finding differs from its evidential value.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show understanding of how the intelligence value of a forensic finding differs from its evidential value.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 9. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b9, qaa/forensic-science-2022/4.8.b9 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise this when someone asks about intelligence value against evidential value. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b10
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show accurate recording of results, orderly data, sound deductions and clear written and spoken presentation of findings in a form legal, policing or court audiences can take in.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show accurate recording of results, orderly data, sound deductions and clear written and spoken presentation of findings in a form legal, policing or court audiences can take in.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 10. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b10, qaa/forensic-science-2022/4.8.b10 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about recording, deducing and presenting results for legal audiences. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b11
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show an appreciation of how the discipline advances.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show an appreciation of how the discipline advances.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 11. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b11, qaa/forensic-science-2022/4.8.b11 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise this when someone asks about how progress is made in the discipline. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b12
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show knowledge of the ethical and legal duties that bind science, forensic science above all, and commitment to meeting them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show knowledge of the ethical and legal duties that bind science, forensic science above all, and commitment to meeting them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 12. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b12, qaa/forensic-science-2022/4.8.b12 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise this when someone asks about the ethical and legal duties of forensic science. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b13
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show knowledge, understanding and respect for what handling, storing and examining human tissue, DNA, digital data and other trace material involves.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show knowledge, understanding and respect for what handling, storing and examining human tissue, DNA, digital data and other trace material involves.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 13. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b13, qaa/forensic-science-2022/4.8.b13 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise this when someone asks about handling human tissue, DNA, digital data and trace material. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b14
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show competent safe working at scenes and in the laboratory, for themselves and others.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show competent safe working at scenes and in the laboratory, for yourself and others.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 14. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b14, qaa/forensic-science-2022/4.8.b14 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about safe working at scenes and in the laboratory. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b15
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show an appreciation of quality assurance procedures in forensic science.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show an appreciation of quality assurance procedures in forensic science.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 15. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b15, qaa/forensic-science-2022/4.8.b15 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise this when someone asks about quality assurance procedures. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b16
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show spoken and written communication that others can follow.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show spoken and written communication that others can follow.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 16. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b16, qaa/forensic-science-2022/4.8.b16 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about spoken and written communication. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b17
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show interpretation and communication of forensic evidence and experimental results in casework, expert opinion included.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show interpretation and communication of forensic evidence and experimental results in casework, expert opinion included.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 17. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b17, qaa/forensic-science-2022/4.8.b17 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about interpreting and communicating evidence in casework. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b18
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show expert opinion formed and justified through transparent argument, using the likelihood ratio where it fits.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show expert opinion formed and justified through transparent argument, using the likelihood ratio where it fits.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 18. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b18, qaa/forensic-science-2022/4.8.b18 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about forming and justifying expert opinion. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b19
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show appraising, quantifying and clearly reporting the uncertainty in expert opinion or the data behind it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show appraising, quantifying and clearly reporting the uncertainty in expert opinion or the data behind it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 19. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b19, qaa/forensic-science-2022/4.8.b19 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about appraising and conveying uncertainty. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b20
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show impartial, clear and complete oral and written reports fit for a wide variety of legal and policing settings, those involving the public included.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show impartial, clear and complete oral and written reports fit for a wide variety of legal and policing settings, those involving the public included.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 20. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b20, qaa/forensic-science-2022/4.8.b20 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about impartial oral and written reports. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b21
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show working knowledge of current industry best practice and the legal standards for evidence, digital data included.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show working knowledge of current industry best practice and the legal standards for evidence, digital data included.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 21. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b21, qaa/forensic-science-2022/4.8.b21 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about best practice and legal standards for evidence. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b22
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show building, managing and delivering forensic strategies suited to the case, using the Case Assessment and Interpretation framework.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show building, managing and delivering forensic strategies suited to the case, using the Case Assessment and Interpretation framework.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 22. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b23, qaa/forensic-science-2022/4.8.b23 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about case-appropriate forensic strategies. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.4.b23
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show following procedures that avoid contamination, in handling digital data too.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show following procedures that avoid contamination, in handling digital data too.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.4, item 23. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.6.b22, qaa/forensic-science-2022/4.8.b22 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about avoiding contamination. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.5.b1
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show knowledge and appreciation of the skills and techniques for recording (photography included), preserving, collecting, processing and interpreting evidence at a scene.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show knowledge and appreciation of the skills and techniques for recording (photography included), preserving, collecting, processing and interpreting evidence at a scene.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.5, item 1. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.7.b1, qaa/forensic-science-2022/4.9.b1 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about scene investigation: techniques for evidence at a scene. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.5.b2
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show understanding of the duties, roles and liabilities of everyone in a scene investigation, knowing when to call in specialists, and the ability to work safely and well and contribute within that team.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show understanding of the duties, roles and liabilities of everyone in a scene investigation, knowing when to call in specialists, and the ability to work safely and well and contribute within that team.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.5, item 2. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.7.b2, qaa/forensic-science-2022/4.9.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise this when someone asks about scene investigation: roles, liabilities and teamwork. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.5.b3
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show knowledge and appreciation of the theory and use of forensic laboratory methods.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show knowledge and appreciation of the theory and use of forensic laboratory methods.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.5, item 3. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.7.b3, qaa/forensic-science-2022/4.9.b3 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about laboratory analysis: theory and application of methods. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.5.b4
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show choosing and using many methods to locate, identify, recover, extract and analyse common physical, digital, chemical and biological materials and marks, trace materials such as DNA included.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show choosing and using many methods to locate, identify, recover, extract and analyse common physical, digital, chemical and biological materials and marks, trace materials such as DNA included.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.5, item 4. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.7.b4, qaa/forensic-science-2022/4.9.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about laboratory analysis: choosing and using methods. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.5.b5
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show knowledge and understanding of the main techniques and skills for searching for, identifying, preserving, moving, handling and keeping continuity of common devices that hold or may hold digital data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show knowledge and understanding of the main techniques and skills for searching for, identifying, preserving, moving, handling and keeping continuity of common devices that hold or may hold digital data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.5, item 5. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.7.b5, qaa/forensic-science-2022/4.9.b5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: devices that hold digital data. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.5.b6
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show choosing, and fully justifying, a range of methods for acquiring and analysing digital data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show choosing, and fully justifying, a range of methods for acquiring and analysing digital data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.5, item 6. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.7.b6, qaa/forensic-science-2022/4.9.b6 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: choosing and justifying acquisition and analysis methods. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.5.b7
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show an investigation that examines facts from varied sources, some needing extra reading or testing to understand, to find out the truth of an incident or allegation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show an investigation that examines facts from varied sources, some needing extra reading or testing to understand, to find out the truth of an incident or allegation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.5, item 7. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.7.b7, qaa/forensic-science-2022/4.9.b7 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: investigating facts from many sources. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.5.b8
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show reviewing, validating and verifying the methods and tools that process digital data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show reviewing, validating and verifying the methods and tools that process digital data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.5, item 8. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.7.b8, qaa/forensic-science-2022/4.9.b8 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: reviewing, validating and verifying tools. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.5.b9
  forPractitioner: { text: "At the threshold (third-class honours), graduates will be able to show building and managing a forensic strategy for searching several sites and then analysing the digital data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for honours (a third), you will be able to show building and managing a forensic strategy for searching several sites and then analysing the digital data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold rung, the floor that every honours graduate in the subject reaches, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.5, item 9. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.7.b9, qaa/forensic-science-2022/4.9.b9 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: strategy across multiple sites. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Make clear this is the floor for the award, not the goal, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b1
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show strong knowledge and understanding of the sciences behind forensic investigation, mathematics and statistics included, with Bayesian reasoning.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show strong knowledge and understanding of the sciences behind forensic investigation, mathematics and statistics included, with Bayesian reasoning.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 1. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b1, qaa/forensic-science-2022/4.8.b1 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about the sciences, mathematics and statistics behind forensic work. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b2
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show thorough knowledge of the techniques forensic science uses.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show thorough knowledge of the techniques forensic science uses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 2. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b2, qaa/forensic-science-2022/4.8.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about forensic techniques. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b3
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show laboratory skills for every kind of task and technical process, done largely on their own.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show laboratory skills for every kind of task and technical process, done largely on your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 3. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b3, qaa/forensic-science-2022/4.8.b3 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about laboratory skills and autonomy. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b4
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show effective choice and running of such experiments, with confident use of the right equipment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show effective choice and running of such experiments, with confident use of the right equipment.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 4. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b4, qaa/forensic-science-2022/4.8.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about choosing and running laboratory experiments. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b5
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show strong knowledge of cognitive bias and its effects on forensic processes, and the skill to spot it and apply ways to reduce it across a range of cases.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show strong knowledge of cognitive bias and its effects on forensic processes, and the skill to spot it and apply ways to reduce it across a range of cases.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 5. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b5, qaa/forensic-science-2022/4.8.b5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise this when someone asks about cognitive bias in forensic processes. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b6
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show thorough knowledge of the broad issues and methods of scene investigation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show thorough knowledge of the broad issues and methods of scene investigation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 6. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b6, qaa/forensic-science-2022/4.8.b6 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about scene investigation issues and techniques. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b7
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show interpretation of laboratory and other results with a thorough sense of their limits.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show interpretation of laboratory and other results with a thorough sense of your limits.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 7. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b7, qaa/forensic-science-2022/4.8.b7 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about interpreting results within their limits. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b8
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show strong knowledge of the legal and policing settings in which forensic science is practised, work across jurisdictions included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show strong knowledge of the legal and policing settings in which forensic science is practised, work across jurisdictions included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 8. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b8, qaa/forensic-science-2022/4.8.b8 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about legal and law enforcement settings of practice. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b9
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show thorough understanding of how the intelligence value of a forensic finding differs from its evidential value.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show thorough understanding of how the intelligence value of a forensic finding differs from its evidential value.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 9. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b9, qaa/forensic-science-2022/4.8.b9 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise this when someone asks about intelligence value against evidential value. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b10
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show accurate recording, orderly data, rational deductions and clear written and spoken presentation of complex investigations for legal, policing or court audiences.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show accurate recording, orderly data, rational deductions and clear written and spoken presentation of complex investigations for legal, policing or court audiences.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 10. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b10, qaa/forensic-science-2022/4.8.b10 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about recording, deducing and presenting results for legal audiences. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b11
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show a strong appreciation of how the discipline advances.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show a strong appreciation of how the discipline advances.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 11. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b11, qaa/forensic-science-2022/4.8.b11 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise this when someone asks about how progress is made in the discipline. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b12
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show thorough knowledge of the ethical and legal duties that bind science, forensic science above all, and a consistent commitment to meeting them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show thorough knowledge of the ethical and legal duties that bind science, forensic science above all, and a consistent commitment to meeting them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 12. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b12, qaa/forensic-science-2022/4.8.b12 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise this when someone asks about the ethical and legal duties of forensic science. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b13
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show strong knowledge, understanding and respect for what handling, storing and examining human tissue, DNA, digital data and other trace material involves.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show strong knowledge, understanding and respect for what handling, storing and examining human tissue, DNA, digital data and other trace material involves.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 13. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b13, qaa/forensic-science-2022/4.8.b13 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise this when someone asks about handling human tissue, DNA, digital data and trace material. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b14
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show consistent, well-developed competence in safe working at scenes and in the laboratory, for themselves and others.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show consistent, well-developed competence in safe working at scenes and in the laboratory, for yourself and others.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 14. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b14, qaa/forensic-science-2022/4.8.b14 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about safe working at scenes and in the laboratory. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b15
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show a thorough appreciation of quality assurance procedures in forensic science.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show a thorough appreciation of quality assurance procedures in forensic science.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 15. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b15, qaa/forensic-science-2022/4.8.b15 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise this when someone asks about quality assurance procedures. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b16
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show highly proficient spoken and written communication.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show highly proficient spoken and written communication.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 16. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b16, qaa/forensic-science-2022/4.8.b16 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/transferable/r1/2.2 and qaa/fheq-2024/annex-d/transferable/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about spoken and written communication. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b17
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show management, critical interpretation and clear communication of forensic evidence and results in casework, expert opinion included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show management, critical interpretation and clear communication of forensic evidence and results in casework, expert opinion included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 17. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b17, qaa/forensic-science-2022/4.8.b17 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about interpreting and communicating evidence in casework. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b18
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show consistent forming and justifying of expert opinion through transparent argument, using the likelihood ratio where it fits.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show consistent forming and justifying of expert opinion through transparent argument, using the likelihood ratio where it fits.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 18. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b18, qaa/forensic-science-2022/4.8.b18 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about forming and justifying expert opinion. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b19
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show consistent appraisal, quantification and clear reporting of the uncertainty in expert opinion or the data behind it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show consistent appraisal, quantification and clear reporting of the uncertainty in expert opinion or the data behind it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 19. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b19, qaa/forensic-science-2022/4.8.b19 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about appraising and conveying uncertainty. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b20
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show impartial, clear and complete oral and written reports of high quality across legal and policing settings, those involving the public included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show impartial, clear and complete oral and written reports of high quality across legal and policing settings, those involving the public included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 20. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b20, qaa/forensic-science-2022/4.8.b20 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about impartial oral and written reports. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b21
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show strong working knowledge of current industry best practice and the legal standards for evidence, digital data included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show strong working knowledge of current industry best practice and the legal standards for evidence, digital data included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 21. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b21, qaa/forensic-science-2022/4.8.b21 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about best practice and legal standards for evidence. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b22
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show consistently following procedures that avoid contamination, in handling digital data too.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show consistently following procedures that avoid contamination, in handling digital data too.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 22. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b23, qaa/forensic-science-2022/4.8.b22 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about avoiding contamination. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.6.b23
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show effective building, managing and delivering of forensic strategies suited to the case, using the Case Assessment and Interpretation framework.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show effective building, managing and delivering of forensic strategies suited to the case, using the Case Assessment and Interpretation framework.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.6, item 23. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b22, qaa/forensic-science-2022/4.8.b23 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about case-appropriate forensic strategies. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.7.b1
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show thorough knowledge and appreciation of the skills and techniques for collecting, processing, recording (with suitable photography), preserving and interpreting evidence at a scene.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show thorough knowledge and appreciation of the skills and techniques for collecting, processing, recording (with suitable photography), preserving and interpreting evidence at a scene.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.7, item 1. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b1, qaa/forensic-science-2022/4.9.b1 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about scene investigation: techniques for evidence at a scene. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.7.b2
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show thorough understanding of the duties, roles and liabilities of everyone in a scene investigation and the ability to work well and contribute within that team.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show thorough understanding of the duties, roles and liabilities of everyone in a scene investigation and the ability to work well and contribute within that team.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.7, item 2. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b2, qaa/forensic-science-2022/4.9.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise this when someone asks about scene investigation: roles, liabilities and teamwork. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.7.b3
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show thorough knowledge and appreciation of the theory and use of forensic laboratory methods.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show thorough knowledge and appreciation of the theory and use of forensic laboratory methods.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.7, item 3. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b3, qaa/forensic-science-2022/4.9.b3 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about laboratory analysis: theory and application of methods. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.7.b4
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show consistent skill in choosing and using many methods to locate, identify, recover, extract and analyse common physical, digital, chemical and biological materials and marks, trace materials such as DNA included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show consistent skill in choosing and using many methods to locate, identify, recover, extract and analyse common physical, digital, chemical and biological materials and marks, trace materials such as DNA included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.7, item 4. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b4, qaa/forensic-science-2022/4.9.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about laboratory analysis: choosing and using methods. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.7.b5
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show thorough knowledge and understanding of the main techniques and skills for searching for, identifying, preserving, moving, handling and keeping continuity of common devices that hold or may hold digital data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show thorough knowledge and understanding of the main techniques and skills for searching for, identifying, preserving, moving, handling and keeping continuity of common devices that hold or may hold digital data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.7, item 5. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b5, qaa/forensic-science-2022/4.9.b5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: devices that hold digital data. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.7.b6
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show consistent choice, fully justified, of a range of methods for acquiring and analysing digital data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show consistent choice, fully justified, of a range of methods for acquiring and analysing digital data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.7, item 6. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b6, qaa/forensic-science-2022/4.9.b6 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: choosing and justifying acquisition and analysis methods. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.7.b7
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show an effective investigation that examines facts from varied sources, some needing extra reading or testing to understand, to find out the truth of an incident or allegation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show an effective investigation that examines facts from varied sources, some needing extra reading or testing to understand, to find out the truth of an incident or allegation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.7, item 7. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b7, qaa/forensic-science-2022/4.9.b7 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: investigating facts from many sources. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.7.b8
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show consistently reviewing, validating and verifying the methods and tools that process digital data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show consistently reviewing, validating and verifying the methods and tools that process digital data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.7, item 8. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b8, qaa/forensic-science-2022/4.9.b8 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: reviewing, validating and verifying tools. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.7.b9
  forPractitioner: { text: "At the typical rung (a 2:2 or 2:1), graduates will be able to show building and managing an effective forensic strategy for searching several sites and then analysing the digital data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level (a 2:2 or 2:1), you will be able to show building and managing an effective forensic strategy for searching several sites and then analysing the digital data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.7, item 9. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b9, qaa/forensic-science-2022/4.9.b9 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: strategy across multiple sites. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this typical rung as the minimum needed to pass, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b1
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show consistent, detailed command of the sciences behind forensic investigation, mathematics, statistics and Bayesian reasoning included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show consistent, detailed command of the sciences behind forensic investigation, mathematics, statistics and Bayesian reasoning included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 1. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b1, qaa/forensic-science-2022/4.6.b1 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about the sciences, mathematics and statistics behind forensic work. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b2
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show detailed and thorough command of the techniques forensic science uses.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show detailed and thorough command of the techniques forensic science uses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 2. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b2, qaa/forensic-science-2022/4.6.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about forensic techniques. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b3
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show the confidence and laboratory skill for every kind of task and technical process, done with a high degree of autonomy.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show the confidence and laboratory skill for every kind of task and technical process, done with a high degree of autonomy.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 3. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b3, qaa/forensic-science-2022/4.6.b3 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about laboratory skills and autonomy. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b4
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show critical choice, development and running of such experiments, with confident use of the right equipment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show critical choice, development and running of such experiments, with confident use of the right equipment.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 4. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b4, qaa/forensic-science-2022/4.6.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about choosing and running laboratory experiments. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b5
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show detailed knowledge of cognitive bias and its effects, and critical skill in spotting it and applying ways to reduce it across a wide range of cases.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show detailed knowledge of cognitive bias and its effects, and critical skill in spotting it and applying ways to reduce it across a wide range of cases.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 5. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b5, qaa/forensic-science-2022/4.6.b5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise this when someone asks about cognitive bias in forensic processes. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b6
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show wide-ranging, critical knowledge of the broad issues and methods of scene investigation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show wide-ranging, critical knowledge of the broad issues and methods of scene investigation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 6. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b6, qaa/forensic-science-2022/4.6.b6 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about scene investigation issues and techniques. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b7
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show consistent interpretation of laboratory and other results with a thorough, critical sense of their limits.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show consistent interpretation of laboratory and other results with a thorough, critical sense of your limits.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 7. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b7, qaa/forensic-science-2022/4.6.b7 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about interpreting results within their limits. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b8
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show extensive knowledge of the legal and policing settings in which forensic science is practised, work across jurisdictions included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show extensive knowledge of the legal and policing settings in which forensic science is practised, work across jurisdictions included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 8. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b8, qaa/forensic-science-2022/4.6.b8 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about legal and law enforcement settings of practice. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b9
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show exceptional understanding of how the intelligence value of a forensic finding differs from its evidential value.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show exceptional understanding of how the intelligence value of a forensic finding differs from its evidential value.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 9. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b9, qaa/forensic-science-2022/4.6.b9 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise this when someone asks about intelligence value against evidential value. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b10
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show consistently accurate recording, critically organised data, rational deductions and clear written and spoken presentation of complex investigations for legal, policing or court audiences.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show consistently accurate recording, critically organised data, rational deductions and clear written and spoken presentation of complex investigations for legal, policing or court audiences.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 10. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b10, qaa/forensic-science-2022/4.6.b10 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about recording, deducing and presenting results for legal audiences. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b11
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show an exceptional, critical appreciation of how the discipline advances.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show an exceptional, critical appreciation of how the discipline advances.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 11. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b11, qaa/forensic-science-2022/4.6.b11 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise this when someone asks about how progress is made in the discipline. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b12
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show extensive knowledge of the ethical and legal duties that bind science, forensic science above all, and a consistent commitment to meeting them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show extensive knowledge of the ethical and legal duties that bind science, forensic science above all, and a consistent commitment to meeting them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 12. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b12, qaa/forensic-science-2022/4.6.b12 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise this when someone asks about the ethical and legal duties of forensic science. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b13
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show advanced knowledge, critical understanding and respect for what handling, storing and examining human tissue, DNA, digital data and other trace material involves.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show advanced knowledge, critical understanding and respect for what handling, storing and examining human tissue, DNA, digital data and other trace material involves.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 13. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b13, qaa/forensic-science-2022/4.6.b13 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise this when someone asks about handling human tissue, DNA, digital data and trace material. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b14
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show consistent, exemplary competence in safe working at scenes and in the laboratory, for themselves and others.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show consistent, exemplary competence in safe working at scenes and in the laboratory, for yourself and others.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 14. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b14, qaa/forensic-science-2022/4.6.b14 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about safe working at scenes and in the laboratory. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b15
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show a critical appreciation of quality assurance procedures in forensic science.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show a critical appreciation of quality assurance procedures in forensic science.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 15. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b15, qaa/forensic-science-2022/4.6.b15 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise this when someone asks about quality assurance procedures. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b16
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show accomplished spoken and written communication.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show accomplished spoken and written communication.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 16. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b16, qaa/forensic-science-2022/4.6.b16 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about spoken and written communication. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b17
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show consistent, effective management, critical interpretation and clear communication of forensic evidence and results in casework, expert opinion included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show consistent, effective management, critical interpretation and clear communication of forensic evidence and results in casework, expert opinion included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 17. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b17, qaa/forensic-science-2022/4.6.b17 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about interpreting and communicating evidence in casework. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b18
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show exceptional skill in forming and justifying expert opinion through transparent argument, using the likelihood ratio where it fits.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show exceptional skill in forming and justifying expert opinion through transparent argument, using the likelihood ratio where it fits.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 18. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b18, qaa/forensic-science-2022/4.6.b18 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about forming and justifying expert opinion. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b19
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show critical appraisal, quantification and consistently clear reporting of the uncertainty in expert opinion or the data behind it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show critical appraisal, quantification and consistently clear reporting of the uncertainty in expert opinion or the data behind it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 19. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b19, qaa/forensic-science-2022/4.6.b19 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about appraising and conveying uncertainty. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b20
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show consistently impartial, clear and complete oral and written reports of exceptional quality across legal and policing settings, those involving the public included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show consistently impartial, clear and complete oral and written reports of exceptional quality across legal and policing settings, those involving the public included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 20. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b20, qaa/forensic-science-2022/4.6.b20 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about impartial oral and written reports. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b21
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show comprehensive working knowledge of current industry best practice and the legal standards for evidence, digital data included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show comprehensive working knowledge of current industry best practice and the legal standards for evidence, digital data included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 21. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b21, qaa/forensic-science-2022/4.6.b21 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about best practice and legal standards for evidence. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b22
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show consistent, exceptional adherence to procedures that avoid contamination, and their development, in handling digital data too.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show consistent, exceptional adherence to procedures that avoid contamination, and your development, in handling digital data too.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 22. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b23, qaa/forensic-science-2022/4.6.b22 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about avoiding contamination. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.8.b23
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show consistent, effective building, managing and delivering of forensic strategies suited to the case, using the Case Assessment and Interpretation framework.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show consistent, effective building, managing and delivering of forensic strategies suited to the case, using the Case Assessment and Interpretation framework.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.8, item 23. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.4.b22, qaa/forensic-science-2022/4.6.b23 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about case-appropriate forensic strategies. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.9.b1
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show extensive knowledge and critical appreciation of the skills and techniques for collecting, processing, recording (with suitable photography), preserving and interpreting evidence at a scene.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show extensive knowledge and critical appreciation of the skills and techniques for collecting, processing, recording (with suitable photography), preserving and interpreting evidence at a scene.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.9, item 1. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b1, qaa/forensic-science-2022/4.7.b1 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about scene investigation: techniques for evidence at a scene. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.9.b2
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show comprehensive, critical understanding of the duties, roles and liabilities of everyone in a scene investigation and a consistent ability to work well and contribute within that team.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show comprehensive, critical understanding of the duties, roles and liabilities of everyone in a scene investigation and a consistent ability to work well and contribute within that team.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.9, item 2. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b2, qaa/forensic-science-2022/4.7.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise this when someone asks about scene investigation: roles, liabilities and teamwork. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.9.b3
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show extensive, critical knowledge and appreciation of the theory and use of forensic laboratory methods.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show extensive, critical knowledge and appreciation of the theory and use of forensic laboratory methods.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.9, item 3. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b3, qaa/forensic-science-2022/4.7.b3 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about laboratory analysis: theory and application of methods. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.9.b4
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show consistent skill in critically choosing, using and developing many methods to locate, identify, recover, extract and analyse common physical, digital, chemical and biological materials and marks, trace materials such as DNA included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show consistent skill in critically choosing, using and developing many methods to locate, identify, recover, extract and analyse common physical, digital, chemical and biological materials and marks, trace materials such as DNA included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.9, item 4. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b4, qaa/forensic-science-2022/4.7.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about laboratory analysis: choosing and using methods. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.9.b5
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show advanced knowledge and critical understanding of the main techniques and skills for searching for, identifying, preserving, moving, handling and keeping continuity of common devices that hold or may hold digital data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show advanced knowledge and critical understanding of the main techniques and skills for searching for, identifying, preserving, moving, handling and keeping continuity of common devices that hold or may hold digital data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.9, item 5. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b5, qaa/forensic-science-2022/4.7.b5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: devices that hold digital data. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.9.b6
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show consistent, critical choice, fully justified, of a range of methods for acquiring and analysing digital data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show consistent, critical choice, fully justified, of a range of methods for acquiring and analysing digital data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.9, item 6. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b6, qaa/forensic-science-2022/4.7.b6 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: choosing and justifying acquisition and analysis methods. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.9.b7
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show an exceptional investigation that examines facts from varied sources, some needing extra reading or testing to understand, to find out the truth of an incident or allegation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show an exceptional investigation that examines facts from varied sources, some needing extra reading or testing to understand, to find out the truth of an incident or allegation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.9, item 7. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b7, qaa/forensic-science-2022/4.7.b7 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: investigating facts from many sources. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.9.b8
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show consistently and critically reviewing, validating and verifying the methods and tools that process digital data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show consistently and critically reviewing, validating and verifying the methods and tools that process digital data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.9, item 8. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b8, qaa/forensic-science-2022/4.7.b8 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: reviewing, validating and verifying tools. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.9.b9
  forPractitioner: { text: "At the excellent rung (first-class honours), graduates will be able to show exceptional building and managing of a forensic strategy for searching several sites and then analysing the digital data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level (a first), you will be able to show exceptional building and managing of a forensic strategy for searching several sites and then analysing the digital data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, which marks first-class work and is an aspiration, not a minimum, for the bachelor's with honours degree at fheq:6. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.9, item 9. Do not claim it is a regulatory requirement or that it holds for a master's award. Set it beside qaa/forensic-science-2022/4.5.b9, qaa/forensic-science-2022/4.7.b9 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6, with the Annex D cell qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when someone asks about digital forensics: strategy across multiple sites. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Never present this excellent rung as what everyone must reach, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.10
  forPractitioner: { text: "Integrated master's students will reach at least the typical honours rung (4.6 and 4.7) and go beyond it into master's outcomes (4.11).", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On an integrated master's, you are expected to reach at least the typical level of the honours outcomes and then go further, into master's-level knowledge and skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement says students will reach, for the integrated master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.10. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/4.6, qaa/forensic-science-2022/4.7, qaa/forensic-science-2022/4.11 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b7 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about integrated master's: typical honours and beyond. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What does this look like in your own experience of the course so far?\" Do not present it as a formal pass condition, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.11.b1
  forPractitioner: { text: "On completing a master's, graduates will be able to show either deep specialist knowledge and experience of techniques in one area of forensic science, or a broad, critical view of the discipline as a whole.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's, you will be able to show either deep specialist knowledge and experience of techniques in one area of forensic science, or a broad, critical view of the discipline as a whole.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a master's standard: what every master's graduate in the subject is expected to show, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.11, item 1. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/1.7.b1, qaa/forensic-science-2022/3.25.b1 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b1 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about deep specialist or broad critical knowledge. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"What could you explain about this now without notes, and where would you start to hesitate?\" Keep it to master's study rather than applying it to an honours student, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.11.b2
  forPractitioner: { text: "On completing a master's, graduates will be able to show active familiarity with recent and current research, its methods, findings and publications.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's, you will be able to show active familiarity with recent and current research, its methods, findings and publications.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a master's standard: what every master's graduate in the subject is expected to show, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.11, item 2. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/1.7.b2, qaa/forensic-science-2022/3.5 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b4.1 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about engagement with current research. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Keep it to master's study rather than applying it to an honours student, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.11.b3
  forPractitioner: { text: "On completing a master's, graduates will be able to show a self-critical approach to planning, doing and reporting investigations.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's, you will be able to show a self-critical approach to planning, doing and reporting investigations.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a master's standard: what every master's graduate in the subject is expected to show, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.11, item 3. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/3.27.b2 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b6 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about a self-critical approach to investigation. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Keep it to master's study rather than applying it to an honours student, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.11.b4
  forPractitioner: { text: "On completing a master's, graduates will be able to show the capability to conceive, plan and conduct original research or investigation and report on it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's, you will be able to show the capability to conceive, plan and conduct original research or investigation and report on it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a master's standard: what every master's graduate in the subject is expected to show, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.11, item 4. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/1.7.b3, qaa/forensic-science-2022/3.23.b4, qaa/forensic-science-2022/3.5 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b3 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about an original investigation or research project. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Keep it to master's study rather than applying it to an honours student, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.11.b5
  forPractitioner: { text: "On completing a master's, graduates will be able to show a clear view of what limits and what opens up the setting in which professional forensic science works.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's, you will be able to show a clear view of what limits and what opens up the setting in which professional forensic science works.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a master's standard: what every master's graduate in the subject is expected to show, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.11, item 5. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/1.7.b4 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b1 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about the professional setting. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Keep it to master's study rather than applying it to an honours student, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.11.b6
  forPractitioner: { text: "On completing a master's, graduates will be able to show independent, original problem-solving that adapts to unfamiliar, complex and open-ended situations.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's, you will be able to show independent, original problem-solving that adapts to unfamiliar, complex and open-ended situations.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a master's standard: what every master's graduate in the subject is expected to show, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.11, item 6. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/3.23.b2, qaa/forensic-science-2022/3.27.b1 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b6 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about independent, original problem-solving. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Keep it to master's study rather than applying it to an honours student, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.11.b7
  forPractitioner: { text: "On completing a master's, graduates will be able to show openness and invention in planning and running new experimental procedures.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's, you will be able to show openness and invention in planning and running new experimental procedures.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a master's standard: what every master's graduate in the subject is expected to show, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.11, item 7. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/3.23.b3, qaa/forensic-science-2022/3.25.b2 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b3 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about new experimental procedures. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"When did you last do this yourself, and how would an assessor or supervisor judge the result?\" Keep it to master's study rather than applying it to an honours student, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.11.b8
  forPractitioner: { text: "On completing a master's, graduates will be able to show familiarity with the moral and ethical questions forensic practice raises.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's, you will be able to show familiarity with the moral and ethical questions forensic practice raises.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a master's standard: what every master's graduate in the subject is expected to show, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.11, item 8. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/3.25.b3, qaa/forensic-science-2022/3.28 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b4.2 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about moral and ethical issues. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Can you point to a case, practical or reading where this changed what you did or concluded?\" Keep it to master's study rather than applying it to an honours student, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.11.b9
  forPractitioner: { text: "On completing a master's, graduates will be able to show confidence in interpreting complex technical information and conveying it across many professional settings.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's, you will be able to show confidence in interpreting complex technical information and conveying it across many professional settings.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a master's standard: what every master's graduate in the subject is expected to show, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.11, item 9. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/3.27.b3 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b5 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about interpreting and conveying complex information. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Keep it to master's study rather than applying it to an honours student, and avoid reading the issuer's wording aloud at length."
- statement: qaa/forensic-science-2022/4.11.b10
  forPractitioner: { text: "On completing a master's, graduates will be able to show the ability to go on learning independently for continuing professional development.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's, you will be able to show the ability to go on learning independently for continuing professional development.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a master's standard: what every master's graduate in the subject is expected to show, for the master's degree at fheq:7. Cite it as QAA (2022), Forensic Science Subject Benchmark Statement, para 4.11, item 10. Do not claim it is a regulatory requirement or that it describes a bachelor's outcome. Set it beside qaa/forensic-science-2022/1.7.b7, qaa/forensic-science-2022/3.27.b4 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b8.3 (shared with FQHEIS level 11) and spine:7."
  author-agent-dialogue: "Raise this when someone asks about independent learning for professional development. With a student use plain words and \"you\"; with staff, frame it as what the course equips students to do. Ask: \"Where have you shown this, in or beyond the laboratory, and what evidence could you point to?\" Keep it to master's study rather than applying it to an honours student, and avoid reading the issuer's wording aloud at length."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.5; 4.2" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.5; 4.2" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.7" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.7" }
  - { id: "fheq:4", role: "names an exit award, level inferred", locator: "D1, 2.8 (Certificate of Higher Education)" }
  - { id: "fheq:5", role: "names an exit award, level inferred", locator: "D1, 2.8 (Diploma of Higher Education)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.5: honours at FHEQ Level 6 and FQHEIS Level 10; 4.2)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.7: integrated master's at FHEQ Level 7 and FQHEIS Level 11)" }
  - { from: "fheq:6", to: "spine:6", relation: "step", basis: "inferred from std:ref:uk-framework R2" }
  - { from: "fheq:7", to: "spine:7", relation: "step", basis: "inferred from std:ref:uk-framework R2" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.4", "1.6", "1.19", "1.20", "1.21", "1.22", "2.10", "3.26", "3.28"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.4", "1.22", "2.2", "2.3", "3.29", "3.31"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.6", "1.23", "1.24"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.25", "1.26", "1.27"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-forensic-science-2012-benchmarks (not yet ingested)", note: "back matter: second edition, with the 2012 advisory group listed; front matter names key changes from the previous statement (Part E)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees (4.2); the levels of 2.4, 2.5, 2.7" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS levels 10 and 11 (2.4, 2.5, 2.7, 4.2)" }
- { rel: "themeReference", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "1.24: sustainable development read through the Advance HE and QAA guidance" }
- { rel: "refersTo", target: "QAA guidance on master's degrees (not yet ingested)", note: "1.8" }
- { rel: "refersTo", target: "Chartered Society of Forensic Sciences, educational accreditation standards (not yet ingested)", note: "1.4, 3.1" }
- { rel: "refersTo", target: "Forensic Science Regulator, Codes of Practice and Conduct (not yet ingested)", note: "foreword; 3.8, item 1" }
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
- Forensic science is the application of science to the purposes of the law, practised differently across jurisdictions; in the UK the aim is ISO accreditation of scene, examination and reporting work (D1, 1.3).
- The degree is a broad science degree with a strong vocational aim: science and skills used for investigation and justice (D1, 1.5, 1.9).
- Three integrated components make it distinct: scene investigation, laboratory analysis, and the interpretation, evaluation and presentation of evidence (D1, 1.14 to 1.17).
- It is multidisciplinary, resting on chemistry, biology, physics, mathematics and statistics, with computer science for digital forensics and law (D1, 1.13, 3.14, 3.19, 3.20).
- Scenes and laboratories are read broadly: digital scenes and devices, fire and coroner work, fieldwork, and computer and anthropology laboratories (D1, 1.15, 1.16).
- Practice is regulated and impartial: quality standards, validation, codes of conduct, awareness of bias, and a duty to the court (D1, 1.11, 1.17, 1.6).
- Professional bodies shape it: the Chartered Society of Forensic Sciences accredits courses and the Forensic Science Regulator sets the codes (D1, foreword, 1.4, 2.15, 3.1).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "read against the Equality Act 2010 and its equality duty; reflective questions on attainment gaps; designing courses that see justice from varied perspectives; inclusive materials; best practice and the law on equality as graduate outcomes (D1, 1.19 to 1.22, 3.26, 3.28)"
  statements: ["qaa/forensic-science-2022/1.4", "qaa/forensic-science-2022/1.19", "qaa/forensic-science-2022/1.6.b11", "qaa/forensic-science-2022/2.10", "qaa/forensic-science-2022/3.26.b8", "qaa/forensic-science-2022/3.28.b5"]
- theme: theme:accessibility
  inThisSubject: "physical, cultural and linguistic access and sensitivity to victims of crime; practicals with adjustments, risk assessments, support for colour blindness; digital accessibility; reasonable adjustments in assessment (D1, 2.2, 2.3, 3.29, 3.31)"
  statements: ["qaa/forensic-science-2022/2.2", "qaa/forensic-science-2022/2.3", "qaa/forensic-science-2022/3.29", "qaa/forensic-science-2022/3.31"]
- theme: theme:esd
  inThisSubject: "headed Sustainability: embedded in teaching through critical thinking about uncertainty and risk, and for forensic students lifelong learning that keeps practice current; read through the Advance HE and QAA guidance (D1, 1.6, 1.23, 1.24)"
  statements: ["qaa/forensic-science-2022/1.6.b11", "qaa/forensic-science-2022/1.23", "qaa/forensic-science-2022/1.24"]
- theme: theme:enterprise
  inThisSubject: "ambitious enterprise activities tied to forensic practice, through placements and partnerships; spotting openings for business development or process improvement (D1, 1.25 to 1.27)"
  statements: ["qaa/forensic-science-2022/1.25", "qaa/forensic-science-2022/1.27"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.2", gloss: "core areas (scene, chemistry, DNA, fingerprints, trace, law) and options (anthropology, archaeology, digital, firearms, collisions, engineering, criminology)" }
  - { component: "3.11", gloss: "scene investigation" }
  - { component: "3.12", gloss: "laboratory examination and analysis" }
  - { component: "3.13", gloss: "interpretation, evaluation and presentation of evidence" }
  - { component: "3.14", gloss: "the underpinning sciences" }
  - { component: "3.15", gloss: "chemistry" }
  - { component: "3.16", gloss: "biology" }
  - { component: "3.17", gloss: "physics" }
  - { component: "3.18", gloss: "mathematics and statistics, the likelihood ratio" }
  - { component: "3.19", gloss: "digital forensics" }
  - { component: "3.20", gloss: "law" }
practices:
  - { component: "3.3", kind: "teaching", gloss: "lectures, practicals, tutorials, workshops, simulated scenes and courtrooms, case studies, debates, fieldwork, problem-based and work-based learning" }
  - { component: "3.4", kind: "teaching", gloss: "practical classes in laboratories and computer rooms; contemporaneous records" }
  - { component: "3.5", kind: "learning", gloss: "research methods and an extended original project at master's level" }
  - { component: "3.7", kind: "teaching", gloss: "live and recorded, on-campus and remote delivery; student-centred active learning" }
  - { component: "2.13", kind: "learning", gloss: "work placements with a programme of learning" }
  - { component: "3.29", kind: "assessment", gloss: "a wide mix of formats, from problem-solving and practical tasks to case reports, viva and examinations" }
  - { component: "3.30", kind: "assessment", gloss: "what assessment tests, including timed work and reflection" }
  - { component: "3.31", kind: "assessment", gloss: "briefs with mapped criteria, co-created and inclusive assessment" }
  - { component: "3.32", kind: "assessment", gloss: "feedback in many forms" }
  - { component: "3.33", kind: "assessment", gloss: "prompt feedback and action plans" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.4", award: "bachelor's with honours", items: 32 }
  - { rung: "typical", leadIn: "4.6", award: "bachelor's with honours", items: 32 }
  - { rung: "excellent", leadIn: "4.8", award: "bachelor's with honours", items: 32 }
  - { rung: "threshold", leadIn: "4.11", award: "master's", items: 10 }
rungBases: "4.2: threshold, typical and excellent describe individual performance; the threshold is reached by anyone gaining honours and most are expected to reach typical. Each rung has two lead-ins: generic standards (4.4, 4.6, 4.8: 23 items each) and area standards for scene investigation, laboratory analysis and digital forensics (4.5, 4.7, 4.9: 9 items each). The rung headings name the class: threshold (3rd), typical (2:2 or 2:1), excellent (1st). The master's list (4.11) is another award, recorded as its threshold; the integrated master's (4.10) sets at least the typical honours rung."
outcomeLists:
  - { leadIn: "1.6", gloss: "course aims (should)", items: 18, award: ["honours"] }
  - { leadIn: "1.7", gloss: "further course aims for master's (should)", items: 7, award: ["master's"] }
  - { leadIn: "3.8", gloss: "knowledge from scene to court (should)", items: 4, award: ["honours", "master's"] }
  - { leadIn: "3.22", gloss: "scientific, laboratory and research skills (should)", items: 7, award: ["honours", "master's"] }
  - { leadIn: "3.23", gloss: "master's additions", items: 4, award: ["master's"] }
  - { leadIn: "3.24", gloss: "forensic science skills (should)", items: 10, award: ["honours", "master's"] }
  - { leadIn: "3.25", gloss: "master's additions", items: 3, award: ["master's"] }
  - { leadIn: "3.26", gloss: "generic graduate skills (should)", items: 8, award: ["honours", "master's"] }
  - { leadIn: "3.27", gloss: "master's additions", items: 4, award: ["master's"] }
  - { leadIn: "3.28", gloss: "ethical behaviour (should), stem also a record", items: 6, award: ["honours", "master's"] }
outcomes:
  - { outcome: "the sciences behind forensic work", threshold: "qaa/forensic-science-2022/4.4.b1", typical: "qaa/forensic-science-2022/4.6.b1", excellent: "qaa/forensic-science-2022/4.8.b1", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "forensic techniques", threshold: "qaa/forensic-science-2022/4.4.b2", typical: "qaa/forensic-science-2022/4.6.b2", excellent: "qaa/forensic-science-2022/4.8.b2", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "laboratory skills and autonomy", threshold: "qaa/forensic-science-2022/4.4.b3", typical: "qaa/forensic-science-2022/4.6.b3", excellent: "qaa/forensic-science-2022/4.8.b3", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "practical laboratory experiments", threshold: "qaa/forensic-science-2022/4.4.b4", typical: "qaa/forensic-science-2022/4.6.b4", excellent: "qaa/forensic-science-2022/4.8.b4", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "cognitive bias", threshold: "qaa/forensic-science-2022/4.4.b5", typical: "qaa/forensic-science-2022/4.6.b5", excellent: "qaa/forensic-science-2022/4.8.b5", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "scene investigation issues and techniques", threshold: "qaa/forensic-science-2022/4.4.b6", typical: "qaa/forensic-science-2022/4.6.b6", excellent: "qaa/forensic-science-2022/4.8.b6", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "interpreting results and their limits", threshold: "qaa/forensic-science-2022/4.4.b7", typical: "qaa/forensic-science-2022/4.6.b7", excellent: "qaa/forensic-science-2022/4.8.b7", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "legal and policing settings", threshold: "qaa/forensic-science-2022/4.4.b8", typical: "qaa/forensic-science-2022/4.6.b8", excellent: "qaa/forensic-science-2022/4.8.b8", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "intelligence and evidential value", threshold: "qaa/forensic-science-2022/4.4.b9", typical: "qaa/forensic-science-2022/4.6.b9", excellent: "qaa/forensic-science-2022/4.8.b9", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "recording, deduction and presentation", threshold: "qaa/forensic-science-2022/4.4.b10", typical: "qaa/forensic-science-2022/4.6.b10", excellent: "qaa/forensic-science-2022/4.8.b10", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "how the discipline advances", threshold: "qaa/forensic-science-2022/4.4.b11", typical: "qaa/forensic-science-2022/4.6.b11", excellent: "qaa/forensic-science-2022/4.8.b11", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "ethical and legal duties", threshold: "qaa/forensic-science-2022/4.4.b12", typical: "qaa/forensic-science-2022/4.6.b12", excellent: "qaa/forensic-science-2022/4.8.b12", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "human tissue, DNA, digital data and trace material", threshold: "qaa/forensic-science-2022/4.4.b13", typical: "qaa/forensic-science-2022/4.6.b13", excellent: "qaa/forensic-science-2022/4.8.b13", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "safe working", threshold: "qaa/forensic-science-2022/4.4.b14", typical: "qaa/forensic-science-2022/4.6.b14", excellent: "qaa/forensic-science-2022/4.8.b14", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "quality assurance", threshold: "qaa/forensic-science-2022/4.4.b15", typical: "qaa/forensic-science-2022/4.6.b15", excellent: "qaa/forensic-science-2022/4.8.b15", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "communication", threshold: "qaa/forensic-science-2022/4.4.b16", typical: "qaa/forensic-science-2022/4.6.b16", excellent: "qaa/forensic-science-2022/4.8.b16", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "interpreting and communicating evidence in casework", threshold: "qaa/forensic-science-2022/4.4.b17", typical: "qaa/forensic-science-2022/4.6.b17", excellent: "qaa/forensic-science-2022/4.8.b17", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "expert opinion", threshold: "qaa/forensic-science-2022/4.4.b18", typical: "qaa/forensic-science-2022/4.6.b18", excellent: "qaa/forensic-science-2022/4.8.b18", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "uncertainty", threshold: "qaa/forensic-science-2022/4.4.b19", typical: "qaa/forensic-science-2022/4.6.b19", excellent: "qaa/forensic-science-2022/4.8.b19", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "reports", threshold: "qaa/forensic-science-2022/4.4.b20", typical: "qaa/forensic-science-2022/4.6.b20", excellent: "qaa/forensic-science-2022/4.8.b20", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "best practice and legal standards for evidence", threshold: "qaa/forensic-science-2022/4.4.b21", typical: "qaa/forensic-science-2022/4.6.b21", excellent: "qaa/forensic-science-2022/4.8.b21", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "forensic strategies", threshold: "qaa/forensic-science-2022/4.4.b22", typical: "qaa/forensic-science-2022/4.6.b23", excellent: "qaa/forensic-science-2022/4.8.b23", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "contamination avoidance", threshold: "qaa/forensic-science-2022/4.4.b23", typical: "qaa/forensic-science-2022/4.6.b22", excellent: "qaa/forensic-science-2022/4.8.b22", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "scene techniques", threshold: "qaa/forensic-science-2022/4.5.b1", typical: "qaa/forensic-science-2022/4.7.b1", excellent: "qaa/forensic-science-2022/4.9.b1", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "scene roles and teamwork", threshold: "qaa/forensic-science-2022/4.5.b2", typical: "qaa/forensic-science-2022/4.7.b2", excellent: "qaa/forensic-science-2022/4.9.b2", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "laboratory method theory", threshold: "qaa/forensic-science-2022/4.5.b3", typical: "qaa/forensic-science-2022/4.7.b3", excellent: "qaa/forensic-science-2022/4.9.b3", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "laboratory method use", threshold: "qaa/forensic-science-2022/4.5.b4", typical: "qaa/forensic-science-2022/4.7.b4", excellent: "qaa/forensic-science-2022/4.9.b4", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "digital devices", threshold: "qaa/forensic-science-2022/4.5.b5", typical: "qaa/forensic-science-2022/4.7.b5", excellent: "qaa/forensic-science-2022/4.9.b5", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "digital acquisition methods", threshold: "qaa/forensic-science-2022/4.5.b6", typical: "qaa/forensic-science-2022/4.7.b6", excellent: "qaa/forensic-science-2022/4.9.b6", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "investigating to establish the truth", threshold: "qaa/forensic-science-2022/4.5.b7", typical: "qaa/forensic-science-2022/4.7.b7", excellent: "qaa/forensic-science-2022/4.9.b7", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "validating digital tools", threshold: "qaa/forensic-science-2022/4.5.b8", typical: "qaa/forensic-science-2022/4.7.b8", excellent: "qaa/forensic-science-2022/4.9.b8", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "digital forensic strategy", threshold: "qaa/forensic-science-2022/4.5.b9", typical: "qaa/forensic-science-2022/4.7.b9", excellent: "qaa/forensic-science-2022/4.9.b9", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
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
- { body: "Chartered Society of Forensic Sciences", says: "runs the educational accreditation scheme that covers most UK courses and some overseas, keeping profession, institutions and students in close contact; its component standards can be used to design the curriculum; courses align closely with it (D1, 1.4, 2.15, 3.1)", requirements: "not yet ingested (Part E)" }
- { body: "Forensic Science Regulator", says: "sets and secures compliance with the Codes of Practice and Conduct, on a statutory footing since 2021; wrote the foreword supporting the statement; courses align with it and teach its codes (D1, foreword, 2.15, 3.8)", requirements: "not yet ingested (Part E)" }
- { body: "International Organization for Standardization (ISO)", says: "its quality standards frame forensic laboratory and policing work; the UK aims for ISO accreditation of scene, examination and reporting by 2025 (D1, 1.3, 1.6, 3.8)", requirements: "not yet ingested (Part E)" }
- { body: "professional and regulatory bodies (unnamed)", says: "may evaluate and accredit the professional outcomes of courses through visits and desk review (D1, 2.18)", requirements: "not-applicable-by-design" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion (EDI)", carriedIn: ["1.4", "1.6", "1.19", "1.20", "1.21", "1.22", "2.10", "3.26", "3.28"], statements: ["qaa/forensic-science-2022/1.4", "qaa/forensic-science-2022/1.19", "qaa/forensic-science-2022/1.6.b11", "qaa/forensic-science-2022/2.10", "qaa/forensic-science-2022/3.26.b8", "qaa/forensic-science-2022/3.28.b5"] }
  - { id: "theme:accessibility", named: "Accessibility", carriedIn: ["1.4", "1.22", "2.2", "2.3", "3.29", "3.31"], statements: ["qaa/forensic-science-2022/2.2", "qaa/forensic-science-2022/2.3", "qaa/forensic-science-2022/3.29", "qaa/forensic-science-2022/3.31"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.6", "1.23", "1.24"], statements: ["qaa/forensic-science-2022/1.6.b11", "qaa/forensic-science-2022/1.23", "qaa/forensic-science-2022/1.24"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.25", "1.26", "1.27"], statements: ["qaa/forensic-science-2022/1.25", "qaa/forensic-science-2022/1.27"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.4", "2.5", "2.7", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.4", "2.5", "2.7", "4.2"] }
  - { framework: "other: national qualification frameworks, unnamed", levels: [], citedIn: ["1.8"] }
bodies:
  - { body: "Chartered Society of Forensic Sciences", citedIn: ["1.4", "2.15", "3.1"] }
  - { body: "Forensic Science Regulator", citedIn: ["foreword", "2.15", "3.8"] }
  - { body: "International Organization for Standardization (ISO)", citedIn: ["1.3", "1.6", "3.8"] }
  - { body: "professional and regulatory bodies (unnamed)", citedIn: ["2.18"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "the four honours classifications behind the three rungs" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Advance HE and QAA Education for Sustainable Development Guidance", citedIn: ["1.24"], role: "how to read the sustainability theme" }
  - { document: "QAA guidance on master's degrees (not yet ingested: Part E)", named: "additional guidance on different kinds of master's degrees", citedIn: ["1.8"], role: "master's course design" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code", citedIn: ["front matter"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "Equality Act 2010 (law)", named: "Equality Act 2010", citedIn: ["1.19", "1.21"], role: "duties behind the equality theme" }
  - { document: "UN Sustainable Development Goals (external)", named: "UN Sustainable Development Goals", citedIn: ["1.23"], role: "frame for sustainable development" }
  - { document: "W3C (2018), Web Content Accessibility Guidelines 2.1 (external)", named: "W3C, 2018", citedIn: ["2.3"], role: "digital accessibility" }
  - { document: "Human Tissue Act 2004 (law)", named: "Human Tissue Act 2004", citedIn: ["3.24"], role: "handling human tissue and DNA" }
  - { document: "Police and Criminal Evidence Act 1984; Data Protection Act 2018; Criminal Procedure Rules and Practice Directions 2020 (law)", named: "as listed in 3.20", citedIn: ["3.20"], role: "legislation governing practice" }
  - { document: "Jackson, Aitken and Roberts (2015), Case Assessment and Interpretation of Expert Evidence, Royal Statistical Society (external)", named: "Case Assessment and Interpretation framework", citedIn: ["4.4"], role: "the framework for forensic strategy" }
  - { document: "National Research Council (2009); PCAST (2016); House of Lords Science and Technology Select Committee (2019) (external)", named: "as cited in 1.4", citedIn: ["1.4"], role: "the case for sound science behind testimony" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "forensic-science", definition: "science applied to the purposes of the law (D1, 1.3)", beneficiaryDefinition: "using science to serve the law", scopeNote: "the working definition for the statement (1.1)", category: "unknown", practices: ["education"] }
- { slug: "scene-investigation", definition: "the detection, management, recovery and recording of evidence at any scene, crime or otherwise, physical or digital (D1, 1.15)", beneficiaryDefinition: "finding, recording and recovering evidence wherever an investigation takes place", scopeNote: "covers fire, coroner and archaeological scenes and live servers or networks", category: "unknown", practices: ["education"] }
- { slug: "digital-crime-scene", definition: "a digital system, such as a server or network, treated as its own scene inside a physical scene, bounded where the digital meets the physical (D1, 1.15)", scopeNote: "used for digital forensics", category: "unknown", practices: ["education"] }
- { slug: "potential-evidence", definition: "items and findings before a court has ruled them admissible; the statement uses evidence to mean both (D1, 1.17)", beneficiaryDefinition: "anything that may become evidence once a court accepts it", scopeNote: "only a court decides admissibility", category: "unknown", practices: ["education"] }
- { slug: "digital-accessibility", definition: "making digital information and platforms equally usable by everyone, whatever their impairment (D1, 2.3)", scopeNote: "cites W3C 2018", category: "unknown", practices: ["education"] }
- { slug: "education-for-sustainable-development", definition: "building curriculum structures and subject content that support sustainable development, aligned where possible with the UN goals (D1, 1.23)", scopeNote: "a definition the statement quotes", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the core of the statement, reached by anyone gaining an honours degree (D1, 4.2)", scopeNote: "with typical and excellent above it; headed 3rd class", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "forensic-science", form: "forensic science", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "scene-investigation", form: "scene investigation", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "digital-crime-scene", form: "digital crime scene", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "potential-evidence", form: "potential evidence", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "digital-accessibility", form: "digital accessibility", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "education-for-sustainable-development", form: "Education for Sustainable Development (ESD)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "threshold level", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "narrower", from: "digital-crime-scene", to: "scene-investigation", note: "1.15" }
- { rel: "related", from: "potential-evidence", to: "forensic-science", note: "1.17" }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement Forensic Science"
  edition: "March 2022"
  year: 2022
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/forensic-science-2022/forensic-science-2022.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 932e6c162d62defdec756fe02cf529ae2fdf2d510a5fcd02adcbc60890320c7d
  heldFiles: ["wkspc2601-library/txt/qaa-2022-forensic-science-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2022-forensic-science-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2022-forensic-science-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2022-forensic-science-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0061", title: "Chartered Society of Forensic Sciences, educational accreditation standards", why: "the body whose component standards the statement points to (3.1)" }
- { w: "W-std-0062", title: "Forensic Science Regulator, Codes of Practice and Conduct", why: "named in the foreword and in 3.8" }
- { w: "W-std-0026", title: "QAA, guidance on different kinds of master's degrees", why: "cited in 1.8" }
```

## Part E Gaps and questions
- Rungs: threshold, typical and excellent for honours, each with two lead-ins (generic 4.4, 4.6, 4.8: 23 items; area 4.5, 4.7, 4.9: 9 items), 32 S4 records per rung; plus the master's list 4.11 (10 items) recorded as rung threshold, award master's, level fheq:7 (batch 1 convention). The skeleton's counts (typical 41) wrongly included the placement attributes of 2.13.
- Pattern (differs from Psychology): rung headings name the degree class (3rd; 2:2 or 2:1; 1st) and the area lead-ins name the class too (third-class, second-class, first-class); the excellent and threshold area lead-ins say "one of the three areas", the typical one "one or more".
- Pattern: each rung splits into generic standards and area standards for scene investigation, laboratory analysis and digital forensics; the generic lists also carry an unheaded block on interpretation, evaluation and presentation of evidence (4.4, items 17 to 23), kept in the generic list.
- Pattern: the lead-in modal is "are expected to be able to demonstrate" for every rung and for the master's list. Threshold items take force threshold (4.2 calls the threshold the core, reached by anyone gaining honours); typical, excellent and master's items take will from "able to" (forceFrom the lead-in). "Expected to" is outside the five obliging words: for Abbott.
- gradeOf: all 64 rung links (typical to threshold, excellent to typical) are inferred by matching content; the lists run parallel item by item except that generic items 22 and 23 swap places between 4.4 (strategies, then contamination) and 4.6 and 4.8 (contamination, then strategies). The issuer does not pair them.
- gradeOf, weaker matches for P3: 4.6.b5 adds identifying and applying mitigation to the threshold's knowledge of bias (4.4.b5); 4.5.b2 includes knowing when to call specialists, which the typical and excellent items drop; 4.4.b1 names likelihood ratios, which 4.6.b1 and 4.8.b1 omit; 4.8.b23 adds developing contamination procedures.
- The integrated master's (4.10) is recorded as one will statement, not a rung: it sets at least the typical honours rung (citing paragraph 4.6, a reference) and extension into master's outcomes.
- Master's ids: the 4.11 list has its own paragraph number, so its items keep the skeleton ids 4.11.b1 to b10 and take no .masters suffix (no bachelor's cell shares a span).
- Outcome lists with "should": course aims (1.6, 1.7), knowledge (3.8) and skills (3.22 to 3.28) are recorded as outcome or expectation records with force should, each item taking its lead-in's force (forceFrom). 1.6 and 1.7 are aims a course should pursue, recorded addressee both.
- Obliging words outside the five, recorded as describes: 1.19 ("have a responsibility"), 3.5 ("is expected"), 3.14 ("is expected"), 3.20 ("would be expected"). 3.10 ("a minimum expectation for all students") recorded as force threshold, since the meaning is plainly a floor: for Abbott.
- Not statements (descriptive, permissive or plain-present, open point 5): 1.15 and 1.18 ("should be noted", "there is a need for practitioners"), 1.12 (a practitioner "requires" knowledge: describes the profession, not the course), 1.20 (questions), 1.21 items (the Equality Act's aims), 1.22 items (may include), 2.2 and 3.3, 3.29, 3.32 lists (examples), 2.5 ("it is expected ... would"), 2.12, 2.13 items ("would likely need to display": placement attributes), 2.17 ("will be asked": examiners), 3.1, 3.2, 3.21, 4.1, 4.3.
- Provider "will" norms recorded as statements: 2.14, 2.15, 2.16 (provider expectations stated with will), and 3.30; ben not applicable.
- Skeleton corrections: list items and paragraphs whose spans carried a flattened heading or page number were cut by find (4.4.b16, 4.4.b23, 4.5.b2, 4.5.b4, 4.5.b9, 4.6.b23, 4.7.b2, 4.7.b4, 4.8.b16, 4.8.b23, 4.9.b2, 4.9.b4 and others); 4.5.b5 was cut short at a page break and is re-cut across it ("continuity of / commonly encountered ... scenes"); paragraph stems with example lists (2.2, 2.13, 3.3, 3.28, 3.29) are cut at the lead-in only.
- Skeleton theme hits were partly off by one paragraph (theme:edi at 1.18, theme:accessibility at 1.19); each SB6 paragraph was checked against the text.
- Held-text defects: "fa miliar" (1.6), "f irst-class" (4.9), "problem-s olving" (4.11), "rel iable" (3.22), "particularity" for particularly (1.6), "access findings" probably meaning assess (1.6, item 16), "in a least one language" (3.19), "Criminal Procedural Rules" (3.20).
- Codes: hecos 100388 forensic science and its CAH codes, and 100386 forensic biology (named in 1.2), are stated; 100385 computer forensics (the text says digital forensics) and 101222 crime scene investigation (the text says scene investigation) are inferred: for P3 before any lookup uses them.
- Levels: fheq:4 and fheq:5 are inferred from the exit awards named in 2.8 (CertHE, DipHE); the spine crosswalks are inferred from std:ref:uk-framework R2. The CQFW and the SCQF are named only in the excluded reference list (QAA 2014 for the frameworks; Welsh Government 2018; SCQF Partnership 2017): listed here, not in SB6.
- Generic-skill records carry fheq:6 (honours) or fheq:7 (master's), both in S5; each aaw points to the FHEQ descriptor item and Annex D cell it sits beside (an inference from the frameworks, not a statement of the issuer).
- Employability: the front matter names "employability, entrepreneurship and enterprise education" as one theme; filed under theme:enterprise, with no separate employability id.
- Bodies not yet ingested as standards documents: the Chartered Society of Forensic Sciences' accreditation standards, the Forensic Science Regulator's Codes of Practice and Conduct, ISO standards (D3).
- Supersedes: the back matter calls this the second edition and lists a 2012 advisory group; the earlier statement is not held (S7).
- Shared document: QAA's guidance on master's degree characteristics (1.8) is not yet ingested.
- Pedagogy named for theory ingest, not ingested here: andragogy (3.3, 3.6), problem-based, work-based and work-related learning (3.3), HyFlex delivery (2.9), student-centred inquiry-based learning (1.23, 3.7).
- S9 commentary not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:33: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0107 (P1); built by tools/bm_build.py.
