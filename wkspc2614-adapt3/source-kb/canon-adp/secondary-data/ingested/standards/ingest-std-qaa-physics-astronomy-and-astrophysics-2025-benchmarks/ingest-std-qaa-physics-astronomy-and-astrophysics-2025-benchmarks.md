---
id: std:doc:qaa-physics-astronomy-and-astrophysics-2025-benchmarks
title: "Subject Benchmark Statement Physics, Astronomy and Astrophysics"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100425", label: "physics", basis: "stated" }
  - { scheme: "hecos", code: "100414", label: "astronomy", basis: "stated" }
  - { scheme: "hecos", code: "100415", label: "astrophysics", basis: "stated" }
  - { scheme: "cah", code: "CAH07-01-01", label: "physics", basis: "stated" }
  - { scheme: "cah", code: "CAH07-01-02", label: "astronomy", basis: "stated" }
  - { scheme: "cah", code: "CAH07-01", label: "physics and astronomy", basis: "stated" }
  - { scheme: "hecos", code: "100426", label: "theoretical physics", basis: "stated" }
  - { scheme: "hecos", code: "101060", label: "applied physics", basis: "stated" }
  - { scheme: "hecos", code: "100416", label: "chemical physics", basis: "stated" }
  - { scheme: "hecos", code: "100949", label: "biophysical science", basis: "inferred" }
edition: "April 2025 (fourth edition)"
published: 2025-04
status: current
supersedes: "the previous Physics, Astronomy and Astrophysics statement (its date is not given in the text; the advisory group list names a 2019 minor update: Part E)"
heldText: { method: sha256-bytes, raw: bef95f82a3eeea033684140c144425d870646ea1e7f85a65e2ee1bec1ced72da, normalised: 044c52be987c399ff1fdec376dc35a3e0145a5106472842091d63b1cb70d205c }
heldTextStan: { method: sha256-stan, raw: bef95f82a3eeea033684140c144425d870646ea1e7f85a65e2ee1bec1ced72da, normalised: 124dbc730692776c82009bc8c274d177f5956638992a44fd6bfc7085a4105062 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2022 onward series with cross-cutting themes (this the fourth edition for the subject)"
awardsCovered: ["bachelor's with honours", "integrated master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document; it sends readers to QAA's Glossary; terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0125 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:22"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Physics, Astronomy and Astrophysics (QAA, April 2025)

> Run 0125, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2025-physics-astronomy-astrophysics-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in Physics, Astronomy or Astrophysics should know and be able to do at the end of a bachelor's degree with honours or an integrated master's degree: two threshold lists (subject and generic) and a typical list for honours, then a threshold and a typical list for the integrated master's. Reach for it when designing, reviewing or describing a physics or astronomy course or its outcomes. It sets no excellent rung, is not the Institute of Physics accreditation standard and is not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2025 for the sector, the statement describes physics as an empirical, mathematical and computational science, the purposes of a degree, its distinctive features (design, progression, flexibility, partnership, review), content, teaching and assessment, then benchmark standards at threshold and typical levels for the bachelor's degree with honours (FHEQ 6, FQHEIS 10) and the integrated master's (FHEQ 7, FQHEIS 11). It treats five cross-cutting themes (equity, diversity and inclusion; accessibility and the needs of disabled students; education for sustainable development; employability, enterprise and entrepreneurship; generative artificial intelligence), sends providers to Annex D of QAA's Frameworks (2024) for the degree classifications and names the Institute of Physics, which accredits many courses. Course teams, external examiners and PSRBs use it in design, approval and review.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Physics, Astronomy and Astrophysics"
edition: "April 2025 (fourth edition)"
dates:
  published: 2025-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; part of current quality arrangements in Scotland, Wales and Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2025", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate in Physics, Astronomy or Astrophysics can be expected to know, do and understand at the end of an honours degree or an integrated master's, and the nature of awards in the subject (D1, front matter: About this Statement; 4.1)"
appliesTo:
  awards: ["bachelor's degrees with honours (BSc)", "integrated master's degrees with honours", "joint, combined and major or minor honours (2.5)"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"In this Statement we will therefore use 'Physics' to refer to all of Physics, Astronomy and Astrophysics.\" (D1, 1.1)"
statedSubjects:
  - { name: "Physics", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100425", label: "physics" }, { scheme: "cah", code: "CAH07-01-01", label: "physics" }] }
  - { name: "Astronomy", locator: "(D1, title; 1.1; 1.17)", kind: "subject", codes: [{ scheme: "hecos", code: "100414", label: "astronomy" }, { scheme: "cah", code: "CAH07-01-02", label: "astronomy" }] }
  - { name: "Astrophysics", locator: "(D1, title; 1.1; 1.17)", kind: "subject", codes: [{ scheme: "hecos", code: "100415", label: "astrophysics" }, { scheme: "cah", code: "CAH07-01-02", label: "astronomy" }] }
  - { name: "theoretical physics courses", locator: "(D1, 1.12)", kind: "programme title", codes: [{ scheme: "hecos", code: "100426", label: "theoretical physics" }] }
  - { name: "Applied physics courses", locator: "(D1, 1.13)", kind: "programme title", codes: [{ scheme: "hecos", code: "101060", label: "applied physics" }] }
  - { name: "joint honours degrees and Physics with a specialism", locator: "(D1, 2.1; 1.13)", kind: "programme title", codes: [{ scheme: "hecos", code: "100425", label: "physics" }] }
  - { name: "chemical physics, biophysics, or geophysics", locator: "(D1, 2.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100416", label: "chemical physics" }, { scheme: "hecos", code: "100949", label: "biophysical science" }] }
  - { name: "placements in industry, research groups or publicly funded bodies", locator: "(D1, 2.2)", kind: "programme title", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "What is Physics?", gloss: "physics studies natural and made systems; the statement uses the one word for all three subjects" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "What is Physics?", gloss: "big questions about the universe and pressing practical issues; mathematics, experiment and computing" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "What is Physics?", gloss: "the many disciplines physics feeds" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "What is Physics?", gloss: "a few key quantities and universal laws explain much; mechanics as the example" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "What is Physics?", gloss: "idealised mathematical models and approximation, reused across very different systems" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "What is Physics?", gloss: "computation and machine learning at the centre of the subject" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "What is Physics?", gloss: "an empirical science: measurement tests theory; instruments spread to other fields" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "What is Physics?", gloss: "progress through imagination and diverse collaboration" }
  - { number: "1.9", order: 11, componentType: stem, parent: "section 1", heading: "What is Physics?", gloss: "lasting benefits of studying the subject (a descriptive list, not outcomes)" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "What is Physics?", gloss: "where graduates find work" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree", gloss: "what the degree develops: deep understanding and a wide set of skills" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree", gloss: "core plus advanced topics; theoretical courses trade lab work for mathematics and computing" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree", gloss: "applied, joint and dual honours courses; placements; the integrated master's adds depth and research" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree", gloss: "courses serve future researchers and those wanting a broad education" }
  - { number: "1.15", order: 17, componentType: area, parent: "section 1", heading: "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree", gloss: "the fundamental areas every degree covers and principles that cross them (S4)" }
  - { number: "1.16", order: 18, componentType: area, parent: "section 1", heading: "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree", gloss: "application areas a degree may include" }
  - { number: "1.17", order: 19, componentType: area, parent: "section 1", heading: "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree", gloss: "what astronomy and astrophysics degrees add" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree", gloss: "recent developments and enough depth to read current research (S4)" }
  - { number: "1.19", order: 21, componentType: area, parent: "section 1", heading: "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree", gloss: "what every degree covers in some measure: mathematics, computing, problem solving and more (provider norm, not a statement: Part E)" }
  - { number: "1.20", order: 22, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree", gloss: "professional skills graduates will have built (outcome list, S4)" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree", gloss: "points to the threshold lists in section 4" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "physics open to all; the Equality Act spirit in culture, curricula and assessment (S4)" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "a curriculum that reflects who has built the discipline (S4)" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "inclusive and accessible activities, safe placements, EDI awareness in students (S4)" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "EDI principles throughout teaching, practice and support (S4)" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "removing stereotypes and barriers; a shared inclusive culture (S4)" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessible learning and assessment by inclusive design and adjustments (S4)" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "inclusive design defined" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "fair entry to courses (S4)" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "course teams, the Disabled Student Commitment and accessible labs, code and maths (S4)" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "adaptive technologies fall short for code, maths and diagrams; resources to compensate (S4)" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "equal access to placements and volunteering (S4)" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "agreeing individual adjustments with students and support services (S4)" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "training and resources for course teams (S4)" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "physics and the UN Sustainable Development Goals" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "instruments and models that quantify sustainability problems" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "technologies for energy and climate; examples from ice cores, photocells and LEDs" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "clear communication to tackle global challenges" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "embedding the goals in the curriculum through examples, projects and lectures" }
  - { number: "1.40", order: 42, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "enterprise, entrepreneurship and employability defined" }
  - { number: "1.41", order: 43, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "why enterprise education matters for careers" }
  - { number: "1.42", order: 44, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "why employers value physics graduates; growing sectors" }
  - { number: "1.43", order: 45, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "helping students articulate the value of their degree (S4)" }
  - { number: "1.44", order: 46, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "innovation fields and spinouts" }
  - { number: "1.45", order: 47, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "optional entrepreneurial skills, ideally taught through physics" }
  - { number: "1.46", order: 48, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "external input from industry, alumni and advisory boards" }
  - { number: "1.47", order: 49, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "generative AI: principles rather than rules" }
  - { number: "1.48", order: 50, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "preparing students to use generative AI ethically and well (S4)" }
  - { number: "1.49", order: 51, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "embrace the technology, aware of its risks (S4)" }
  - { number: "1.50", order: 52, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "assessment that acknowledges generative AI (S4)" }
  - { number: "1.51", order: 53, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "responsible use, data protection and critique of AI output (S4)" }
  - { number: "2.1", order: 55, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "a broad subject with a common core and provider-specific options" }
  - { number: "2.2", order: 56, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "placements, credit-bearing or experiential" }
  - { number: "2.3", order: 57, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression by level towards the threshold; framework levels named" }
  - { number: "2.4", order: 58, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "a second-class degree as preparation for postgraduate study" }
  - { number: "2.5", order: 59, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined degrees reach the core skills and add others (S4)" }
  - { number: "2.6", order: 60, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards at lower levels" }
  - { number: "2.7", order: 61, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "course length in the four nations" }
  - { number: "2.8", order: 62, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "part-time study and credit" }
  - { number: "2.9", order: 63, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes and formats of study; micro-credentials and prior learning" }
  - { number: "2.10", order: 64, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "foundation years and access routes" }
  - { number: "2.11", order: 65, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnerships for study abroad and industry" }
  - { number: "2.12", order: 66, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "credit from study abroad and calibrating partner marks (S4)" }
  - { number: "2.13", order: 67, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "professional placements and their value" }
  - { number: "2.14", order: 68, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "internal and external review with the student voice" }
  - { number: "2.15", order: 69, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "2.16", order: 70, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "externality and accreditation review by the Institute of Physics" }
  - { number: "3.1", order: 72, componentType: paragraph, parent: "section 3", heading: "Content, structure and delivery", gloss: "what section 3 covers" }
  - { number: "3.2", order: 73, componentType: practice, parent: "section 3", heading: "Content and teaching", gloss: "a hierarchical, empirical subject and its teaching methods" }
  - { number: "3.3", order: 74, componentType: paragraph, parent: "section 3", heading: "Content and teaching", gloss: "the mix of methods varies and changes over time" }
  - { number: "3.4", order: 75, componentType: practice, parent: "section 3", heading: "Content and teaching", gloss: "skills developed through physics applications; open-ended lab work at higher levels (S4)" }
  - { number: "3.5", order: 76, componentType: paragraph, parent: "section 3", heading: "Content and teaching", gloss: "computing skills, generative AI among them" }
  - { number: "3.6", order: 77, componentType: paragraph, parent: "section 3", heading: "Content and teaching", gloss: "skills valued by quantitative professions" }
  - { number: "3.7", order: 78, componentType: paragraph, parent: "section 3", heading: "Content and teaching", gloss: "no prescribed methods; inclusive design for outcomes (S4)" }
  - { number: "3.8", order: 79, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "assessment aligned to outcomes" }
  - { number: "3.9", order: 80, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "the range of assessment methods" }
  - { number: "3.10", order: 81, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "matching assessment styles to outcomes" }
  - { number: "3.11", order: 82, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "uneven module marks and flexible regulations (S4)" }
  - { number: "4.1", order: 84, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the statement sets threshold and typical standards for honours" }
  - { number: "4.2", order: 85, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed the threshold; Annex D for classifications (S4)" }
  - { number: "4.3", order: 86, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "not competence standards; Equality Act and EHRC guidance (S4)" }
  - { number: "4.4", order: 87, componentType: stem, parent: "section 4", heading: "Threshold level: Subject knowledge, understanding and skills", gloss: "threshold: subject knowledge, understanding and skills (rung list)" }
  - { number: "4.5", order: 88, componentType: stem, parent: "section 4", heading: "Threshold level: Generic skills", gloss: "threshold: generic skills (rung list)" }
  - { number: "4.6", order: 89, componentType: stem, parent: "section 4", heading: "Typical level", gloss: "typical honours level (rung list)" }
  - { number: "4.7", order: 90, componentType: stem, parent: "section 4", heading: "Integrated master's", gloss: "integrated master's threshold (rung list)" }
  - { number: "4.8", order: 91, componentType: stem, parent: "section 4", heading: "Integrated master's", gloss: "integrated master's typical level (rung list)" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Physics, Astronomy or Astrophysics degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of the Physics degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "none", heading: "section heading lines (1 to 4)", kind: "other: headings, recorded in S3 as sections" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for S7 and SB6" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: back matter, read for S8" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 76 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/physics-astronomy-and-astrophysics-2025/1.15
  locator: { number: "1.15", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree"] }
  span: { start: 14901, end: 15359 }
  source: "1.15 The fundamental areas of Physics - which all Physics degrees will cover to some extent - include classical mechanics, relativity, quantum physics, electromagnetism, thermodynamics and statistical physics, the physics of light and waves, and the properties of matter. All Physics degrees will provide students with an appreciation of underlying principles which cross the fundamental areas - for example, principles of equilibrium and conservation laws.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "all Physics degrees"
  addressee: both
  verbs: ["cover", "provide"]
  about: "the fundamental areas and the principles across them"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Every physics degree will treat, in some measure, classical mechanics, relativity, quantum physics, electromagnetism, thermodynamics with statistical physics, light and waves and the properties of matter, and will give students a sense of the principles, such as conservation and equilibrium, that run through them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree"] }
  span: { start: 16045, end: 16288 }
  source: "1.18 Physics degrees provide students with an appreciation of recent developments in Physics and will cover some of the fundamental areas to sufficiently advanced level to enable students to engage with current scientific research literature.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "all Physics degrees"
  addressee: both
  verbs: ["provide", "cover", "engage"]
  about: "recent developments and reading current research"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Degrees give students a sense of recent advances and will take some core areas far enough for students to work with today's research papers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.20.b1
  locator: { number: "1.20.b1", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree"] }
  span: { start: 17148, end: 17207 }
  source: "the ability to approach new problems flexibly and adaptably"
  stem: "1.20"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["approach"]
  about: "flexible approach to new problems"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to tackle unfamiliar problems with flexibility and adaptability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.20.b2
  locator: { number: "1.20.b2", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree"] }
  span: { start: 17210, end: 17343 }
  source: "clear communication of complex data and ideas using media appropriate to the information being conveyed and the audience receiving it"
  stem: "1.20"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "communicating complex data and ideas to fit the audience"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will communicate complex data and ideas clearly, choosing media that suit the content and the audience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.20.b3
  locator: { number: "1.20.b3", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree"] }
  span: { start: 17346, end: 17396 }
  source: "the ability to work both individually and in teams"
  stem: "1.20"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["work"]
  about: "working alone and in teams"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to work both independently and as part of a team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.20.b4
  locator: { number: "1.20.b4", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree"] }
  span: { start: 17399, end: 17427 }
  source: "time and deadline management"
  stem: "1.20"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "managing time and deadlines"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will manage time and meet deadlines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.20.b5
  locator: { number: "1.20.b5", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree"] }
  span: { start: 17433, end: 17480 }
  source: "critical analysis of their own and others' work"
  stem: "1.20"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "critical analysis of own and others' work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will analyse critically both their own work and the work of others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.20.b6
  locator: { number: "1.20.b6", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree"] }
  span: { start: 17483, end: 17549 }
  source: "the ability to identify the potential ethical issues in their work"
  stem: "1.20"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["identify"]
  about: "spotting ethical issues in one's work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to recognise the ethical questions their work may raise."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.20.b7
  locator: { number: "1.20.b7", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree"] }
  span: { start: 17552, end: 17901 }
  source: "an appreciation that to fabricate, falsify or misrepresent data or to commit plagiarism constitutes unethical scientific behaviour. A professional physicist should be objective, unbiased and truthful in all aspects of their work and recognise the limitations of their experimental techniques and calculations and, more fundamentally, their knowledge"
  stem: "1.20"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["fabricate", "falsify", "misrepresent", "commit", "recognise"]
  about: "research integrity and honest limits"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will understand that fabricating, falsifying or misrepresenting data or plagiarising is unethical in science; the statement adds that a professional physicist should be impartial and truthful in all their work and recognise the limits of their methods, calculations and knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.20.b8
  locator: { number: "1.20.b8", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree"] }
  span: { start: 17904, end: 17967 }
  source: "an understanding of what constitutes a safe working environment"
  stem: "1.20"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "safe working environments"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will understand what makes a working environment safe."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.20.b9
  locator: { number: "1.20.b9", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree"] }
  span: { start: 17970, end: 18028 }
  source: "an appreciation of environmental and sustainability issues"
  stem: "1.20"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "environmental and sustainability issues"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will appreciate environmental and sustainability questions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.20.b10
  locator: { number: "1.20.b10", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Purposes and characteristics of a Physics, Astronomy or Astrophysics degree"] }
  span: { start: 18031, end: 18176 }
  source: "knowledge of professional practice. Some examples may include business awareness, project management, entrepreneurship and intellectual property."
  stem: "1.20"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["include"]
  about: "knowledge of professional practice"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will know about professional practice, for instance business awareness, project management, entrepreneurship and intellectual property."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Equity, diversity and inclusion"] }
  span: { start: 18357, end: 19439 }
  source: "1.22 Physics is fundamental to understanding the world around us and should be open to all through inclusive teaching covering the wide range of experiences, cultures and backgrounds of students. Physics can only be truly open to all when the defining equity, diversity and inclusion (EDI) principles and spirit of the Equality Act (covering England, Scotland and Wales) and related legislation that applies to Northern Ireland, are embedded in Physics culture, curricula, teaching and assessment methods. Protected characteristics (including age; gender reassignment; being married or in a civil partnership; being pregnant or on maternity leave; disability; race including colour, nationality, ethnic or national origin; religion or belief; sex and sexual orientation) and personal circumstances (such as caring responsibilities or regional or more general economic disadvantage) can all affect the way in which individuals experience the world and the way they are perceived by others. In Physics, the contribution of every individual should be welcomed, enabled and encouraged.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the discipline, its curricula, teaching and assessment"
  addressee: provider
  verbs: ["embedded", "welcomed", "enabled", "encouraged"]
  about: "physics open to all; EDI embedded"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Physics should be open to everyone through inclusive teaching that reflects students' range of experience and background; that needs EDI principles and the spirit of equality law built into the culture, curricula, teaching and assessment, and every person's contribution should be welcomed and supported."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Equity, diversity and inclusion"] }
  span: { start: 19439, end: 19948 }
  source: "1.23 The Physics curriculum encompasses subject content, delivery, engagement, assessment methods, and the professional practices that students prepare for. It should reflect the diversity of people, ideas and applications that contribute, and have contributed, to the development of the discipline and make use of its discoveries. Physics is of global relevance, and, as such, is a global collaboration. We should acknowledge the past, learn from it, and move forward with a positive attitude to the future.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the Physics curriculum"
  addressee: provider
  verbs: ["reflect", "acknowledge", "learn"]
  about: "a curriculum reflecting the diversity of contributors"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "The curriculum, taken broadly to include content, delivery, assessment and professional preparation, should show the variety of people and ideas behind the discipline and its uses; as a global endeavour, physics should face its past and learn from it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Equity, diversity and inclusion"] }
  span: { start: 19948, end: 20756 }
  source: "1.24 The Physics curriculum should be inclusive with activities that are accessible to all students. Where this is not possible, suitable alternatives should be provided to allow all students to meet the learning outcomes, while maintaining a sense of belonging and acceptance. Physics students will build an awareness of EDI to enable them to accept and support their peers and staff, and to be equipped as graduates to enter the employment arena and work in a professional manner. The curriculum should not have any compulsory or optional elements where some students are discriminated against, or made unwelcome or unsafe. For example, when planning placement and field trip locations, care should be taken to verify that there is minimal risk of discrimination on the basis of protected characteristics.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "the Physics curriculum and its students"
  addressee: both
  verbs: ["provided", "build", "accept", "support"]
  about: "inclusive activities, safe placements and EDI awareness"
  themes: [theme:edi]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Curriculum activities should be inclusive and open to all, with suitable alternatives where they cannot be, and no compulsory or optional element should leave students facing discrimination or danger; placements and field trips need checking for that risk. Students will build an awareness of EDI that lets them support peers and staff and work professionally after graduating."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.25
  locator: { number: "1.25", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Equity, diversity and inclusion"] }
  span: { start: 20756, end: 21113 }
  source: "1.25 The principles of equity, diversity and inclusion are effectively maintained when all individuals are offered equivalent opportunities and share the same responsibilities to embody them in their practice. EDI principles should appear throughout learning, teaching, practicing and supporting Physics, and permeate the staff and student environments.\n\n7\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "learning, teaching, practice and support in Physics"
  addressee: provider
  verbs: ["appear", "permeate"]
  about: "EDI principles throughout the department"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "EDI works when everyone has equivalent chances and the same duty to live it out; its principles should run through learning, teaching, practice and support for staff and students alike."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.26
  locator: { number: "1.26", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Equity, diversity and inclusion"] }
  span: { start: 21113, end: 21583 }
  source: "1.26 Positive steps should be taken to eradicate harmful stereotypes and language, to remove barriers to inclusivity, and to challenge systemic and structural disadvantages impacting specific cultural or social groups. Ways to achieve this include partnerships between students and staff, empowering all to make meaningful contributions in a respectful environment. All are responsible for building an inclusive culture. Accessibility and the needs of disabled students\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "staff and students in Physics"
  addressee: both
  verbs: ["taken", "eradicate", "remove", "challenge"]
  about: "removing stereotypes and barriers; shared responsibility"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Active steps should be taken against harmful stereotypes and language, barriers to inclusion and the structural disadvantages some groups face, for instance through staff and student partnership in a respectful setting; building an inclusive culture is everyone's responsibility."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.27
  locator: { number: "1.27", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Accessibility and the needs of disabled students"] }
  span: { start: 21583, end: 22080 }
  source: "1.27 Accessibility involves enabling access for people with differing individual requirements, eliminating unnecessary barriers to successful learning and assessment. Physics courses can give all students the opportunity to thrive, maintaining a sense of belonging and acceptance; students should be offered learning and assessment opportunities that are equally accessible to them, by means of inclusive design wherever possible and by means of reasonable individual adjustments where necessary.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Physics courses"
  addressee: provider
  verbs: ["offered"]
  about: "accessible learning and assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Accessibility means removing needless barriers for people with different needs; students should be given learning and assessment that are equally open to them, through inclusive design where possible and reasonable individual adjustments where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.29
  locator: { number: "1.29", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Accessibility and the needs of disabled students"] }
  span: { start: 22426, end: 22560 }
  source: "1.29 Entry to Physics courses should be equitable and not influenced by any perceptions by staff or students of barriers to learning.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "entry to Physics courses"
  addressee: provider
  verbs: ["influenced"]
  about: "fair entry"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Admission to physics courses should be fair and free of assumptions, by staff or students, about barriers to learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.30
  locator: { number: "1.30", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Accessibility and the needs of disabled students"] }
  span: { start: 22560, end: 23407 }
  source: "1.30 Course teams should take full advantage of the guidance and interpretation of legislative principles set out in the Disabled Student Commitment. They should ensure that all students are provided with appropriate and inclusive support and training to develop the key knowledge, skills and behaviours outlined in this Statement. It is important for course teams to consider the accessibility of their communications to students. Particular attention should be given to the accessibility of laboratories, computing activities, and mathematical and graphical content. Flexibility of delivery can improve accessibility to learning for a diverse community. A mix of synchronous and asynchronous delivery can be beneficial for a broad range of learners who may face barriers, especially, but not restricted to, disabled and neurodivergent students.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Physics course teams"
  addressee: provider
  verbs: ["take", "ensure", "provided", "develop", "given"]
  about: "course teams, the Disabled Student Commitment and accessible delivery"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Course teams should use the guidance in the Disabled Student Commitment and make sure every student gets inclusive support and training to reach the knowledge, skills and behaviours the statement sets out; they should attend to accessible communication and especially to laboratories, computing and mathematical and graphical material, and a blend of live and recorded delivery can help."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.31
  locator: { number: "1.31", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Accessibility and the needs of disabled students"] }
  span: { start: 23407, end: 23845 }
  source: "1.31 Adaptive technologies are important in removing barriers to access and are rapidly developing. However, at the time of writing, mainstream adaptive technologies do not effectively support students to engage with some areas that are critical to the discipline, for example, computer programming, mathematics, and diagrammatical content. Higher education providers should provide the resources necessary to mitigate these limitations.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["provide", "mitigate"]
  about: "resources where adaptive technology falls short"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Adaptive technologies help remove barriers but, as yet, do not serve students well for programming, mathematics and diagrams; providers should supply the resources needed to make up for this."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.32
  locator: { number: "1.32", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Accessibility and the needs of disabled students"] }
  span: { start: 23845, end: 24083 }
  source: "1.32 All practical efforts should be made to ensure equal access to extracurricular activities such as placements and volunteering opportunities, given the additional challenges faced by some students and the hidden costs often involved.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "extracurricular opportunities"
  addressee: provider
  verbs: ["made", "ensure"]
  about: "equal access to placements and volunteering"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Every practical effort should be made so that placements, volunteering and similar extras are equally open to all, given that some students face added hurdles and hidden costs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.33
  locator: { number: "1.33", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Accessibility and the needs of disabled students"] }
  span: { start: 24083, end: 24260 }
  source: "1.33 Physics course teams should engage with students and with the relevant student support services to discuss and implement reasonable individual adjustments where necessary.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Physics course teams"
  addressee: provider
  verbs: ["engage", "discuss", "implement"]
  about: "agreeing individual adjustments"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Physics course teams should work with students and student support services to agree and put in place reasonable individual adjustments where they are needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.34
  locator: { number: "1.34", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Accessibility and the needs of disabled students"] }
  span: { start: 24260, end: 24452 }
  source: "1.34 Higher education providers should ensure Physics course teams have the appropriate training and resources to implement accessibility in practice.\n\n8\nEducation for sustainable development\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["ensure", "implement"]
  about: "training and resources for course teams"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Providers should see that physics course teams have the training and resources to put accessibility into practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.43
  locator: { number: "1.43", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Employability, enterprise and entrepreneurship education"] }
  span: { start: 28131, end: 28431 }
  source: "1.43 Physics course teams should engage with students and relevant careers advisers to help students understand and articulate the value of the skills, knowledge and behaviours gained from a Physics degree and how the Physics degree aligns with work-based learning opportunities or graduate careers.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Physics course teams"
  addressee: provider
  verbs: ["engage", "help", "understand", "articulate"]
  about: "helping students articulate the value of their degree"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Physics course teams should work with students and careers advisers so that students grasp and can put into words what their degree has given them and how it connects with work-based learning or graduate jobs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.48
  locator: { number: "1.48", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Generative artificial intelligence"] }
  span: { start: 29919, end: 30387 }
  source: "1.48 Physics has contributed to the development of machine learning and artificial intelligence and these are routinely used to process experimental data and model systems. GenAI has the potential to enhance productivity in many areas of life. Students need to be prepared to use it in their studies and future employment, but they need careful guidance, training and practice within the curriculum to develop strategies for using GenAI in ethical and effective ways.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: none
  appliesTo: "students and the curriculum"
  addressee: provider
  verbs: ["prepared", "use", "develop"]
  about: "guided preparation to use generative AI"
  themes: [theme:generative-ai]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Machine learning and AI already serve physics in data processing and modelling, and generative AI can raise productivity; students need preparing to use it in study and work, which calls for careful guidance, training and practice inside the curriculum so they develop ethical and effective habits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.49
  locator: { number: "1.49", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Generative artificial intelligence"] }
  span: { start: 30387, end: 30768 }
  source: "1.49 GenAI generates text, images, video, computer code, and other outputs yet to be developed. This impacts on the skills required of a Physics graduate in the workplace and hence on the skills, activities and learning outcomes central to a Physics degree. As with other technological advances, this should be embraced while maintaining an awareness of the risks and limitations.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the Physics degree and its outcomes"
  addressee: provider
  verbs: ["embraced", "maintaining"]
  about: "embracing generative AI with awareness of risk"
  themes: [theme:generative-ai]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Generative AI produces text, images, code and more, which changes the skills a physics graduate needs and so the skills, activities and outcomes of the degree; like earlier technologies, it should be embraced with an eye on its risks and limits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.50
  locator: { number: "1.50", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Generative artificial intelligence"] }
  span: { start: 30768, end: 31080 }
  source: "1.50 The availability of AI tools encourages the development of assessment protocols that acknowledge the use of GenAI. Assessments that recognise the potential of GenAI in Physics, develop students' critical thinking, and equip them with the ability to solve complex problems creatively should be welcomed.\n\n10\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment in Physics"
  addressee: provider
  verbs: ["recognise", "develop", "equip", "welcomed"]
  about: "assessment that acknowledges generative AI"
  themes: [theme:generative-ai]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "AI tools prompt assessment designs that take generative AI into account; assessments that see its potential in physics, build students' critical thinking and prepare them to solve complex problems creatively should be welcomed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/1.51
  locator: { number: "1.51", headingPath: ["Context and purposes of a Physics, Astronomy or Astrophysics degree", "Generative artificial intelligence"] }
  span: { start: 31080, end: 31476 }
  source: "1.51 Students should use GenAI responsibly, sustainably, ethically and safely. Care should be taken to ensure that sensitive data is not released into the public domain. For example, there may be issues with the General Data Protection Regulation and intellectual property. Students should also be trained to critique the output from any GenAI tool regarding its accuracy, relevance or bias.\n\n11\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students and those who train them"
  addressee: both
  verbs: ["use", "taken", "ensure", "trained", "critique"]
  about: "responsible use and critique of generative AI"
  themes: [theme:generative-ai]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Students should use generative AI responsibly, sustainably, ethically and safely, keeping sensitive data out of public view with data protection and intellectual property in mind, and should be trained to question AI output for accuracy, relevance and bias."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of the Physics degree", "Progression"] }
  span: { start: 33593, end: 34155 }
  source: "2.5 Undergraduates studying Physics, Astronomy and Astrophysics courses as part of a combined or joint degree with other subjects (including courses that specify major and minor options) will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the areas covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study, examples being chemical physics, biophysics, or geophysics.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on combined or joint degrees"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "joint and combined degrees and the core skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students taking physics, astronomy or astrophysics within a combined or joint degree will reach the core of the subject-specific and generic skills set out here and add others from their other subject, with room for interdisciplinary work such as chemical physics or biophysics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of the Physics degree", "Partnership"] }
  span: { start: 36409, end: 36885 }
  source: "2.12 The amount of credit associated with a period of study abroad will reflect the duration and the regulations of the home provider. In addition to broadening the horizons of the student, any credit earned during the time spent studying abroad will contribute towards progression. In cases where the marks awarded by the partner contribute to the student's final degree classification, these should be carefully calibrated to ensure equivalence to the awarding institution.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "study abroad and partner marks"
  addressee: provider
  verbs: ["calibrated", "ensure"]
  about: "credit from study abroad and calibrating partner marks"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Credit for time abroad follows its length and the home provider's rules and counts towards progression; where a partner's marks feed the final classification they should be carefully calibrated to match the awarding institution."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Content and teaching"] }
  span: { start: 40244, end: 40606 }
  source: "3.4 Approaches to skills development encompass both generic and subject-specific skills. These should, where appropriate, be developed with reference to applications in Physics. Development between levels of study may be evident; for example, laboratory (and observational) work may become open-ended with more demanding reporting criteria at the higher levels.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "skills development in Physics courses"
  addressee: provider
  verbs: ["developed"]
  about: "skills taught through physics applications"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Skills work covers both generic and subject skills, which should be developed through physics applications where appropriate; progress across levels may show, for example in laboratory and observing work growing more open-ended with tougher reporting standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/3.7
  locator: { number: "3.7", headingPath: ["Content, structure and delivery", "Content and teaching"] }
  span: { start: 41206, end: 41721 }
  source: "3.7 This Subject Benchmark Statement does not aim to be prescriptive about which teaching or learning methods are used by a particular course. Higher education providers use appropriate teaching methods to ensure that students are engaged, motivated and\n\n15\nchallenged to learn as well as delivering the course learning outcomes. Attention should be paid in the design process to ensure that teaching methods support achievement of the learning outcomes and are inclusive and accessible to all students. Assessment\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course design"
  addressee: provider
  verbs: ["paid", "ensure", "support"]
  about: "teaching methods that support outcomes and inclusion"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "The statement does not dictate teaching methods; providers pick methods that engage, motivate and stretch students while delivering outcomes, and in design attention should go to methods that support the outcomes and are inclusive and accessible to all."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/3.11
  locator: { number: "3.11", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 43552, end: 44401 }
  source: "3.11 The performance of an individual student may vary significantly between modules and the student's marks on some modules may not be commensurate with their overall performance. This is an inherent feature of quantitative subjects and reflects both the\n\n16\nconceptual difficulty and the need to solve quantitative problems. In assessments that include significant amounts of problem-solving, frequently requiring extensive use of mathematics, marks often span the entire range of an assessment continuum. Students towards the lower end of the performance range may fail some modules while still meeting the overall learning outcomes of the course. Assessment regulations need to be flexible enough to take account of the variability, with providers allowing examiners to judge overall performance within the context of all learning outcomes.\n\n17\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: none
  appliesTo: "assessment regulations"
  addressee: provider
  verbs: ["take", "allowing", "judge"]
  about: "flexible regulations for uneven module marks"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "A student's marks can vary widely between modules in a quantitative subject, and those near the bottom of the range may fail some modules yet meet the course outcomes overall; regulations need enough flexibility to let examiners judge overall performance against all outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44833, end: 45318 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["refer"]
  about: "Annex D for performance above threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students do far better than the minimum; each provider decides how to evidence that and should refer to Annex D of the qualifications frameworks, which describes the four honours classifications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 45318, end: 45919 }
  source: "4.3 Please note that the minimum threshold and typical standards for undergraduate and integrated master's levels are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards (as defined by the Equality Act 2010) as part of a programme specification, these can be informed by the relevant Subject Benchmark Statement along with any PSRB requirements. In these circumstances providers should follow the most recent guidance from the Equality and Human Rights Commission. Threshold level Subject knowledge, understanding and skills\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers developing competence standards"
  addressee: provider
  verbs: ["follow", "informed"]
  about: "not competence standards; EHRC guidance"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "The rung standards at both honours and integrated master's level are not universal competence standards; a provider that sets competence standards under the Equality Act 2010 may draw on this statement and PSRB requirements and should follow the latest guidance from the Equality and Human Rights Commission."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 46033, end: 46088 }
  source: "understand and apply basic physical laws and principles"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["understand", "apply"]
  about: "basic physical laws and principles"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to grasp and use the basic laws and principles of physics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 46091, end: 46179 }
  source: "identify and use relevant physical laws and principles when dealing with simple problems"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "use"]
  about: "choosing laws for simple problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to pick out and use the laws and principles that bear on simple problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 46182, end: 46262 }
  source: "solve problems in Physics using appropriate mathematical and physical techniques"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["solve", "using"]
  about: "solving problems with mathematical and physical techniques"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to work physics problems through with fitting mathematical and physical methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 46265, end: 46401 }
  source: "execute and analyse the results of an experiment (if on an experimental course), with an appreciation of the safe use of basic apparatus"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["execute", "analyse"]
  about: "carrying out experiments safely"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able, on an experimental course, to carry out an experiment, analyse its results and understand how to use basic apparatus safely."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 46404, end: 46559 }
  source: "competently use appropriate software packages/systems for the analysis of data, simulation of physical systems and the retrieval of appropriate information"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["use"]
  about: "software for data, simulation and information"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to use suitable software competently to analyse data, simulate physical systems and find information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 46562, end: 46655 }
  source: "undertake numerical manipulation of data and to present and interpret information graphically"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["undertake", "present", "interpret"]
  about: "handling data numerically and graphically"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to manipulate data numerically and show and read information in graphs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 46658, end: 46806 }
  source: "perform an investigation and analyse the results. Such analysis will include the evaluation of the level of uncertainty or limitation in the results"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["perform", "analyse"]
  about: "investigation with uncertainty and limits"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to carry out an investigation and analyse its results, including judging their uncertainty or limitations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 46809, end: 46969 }
  source: "communicate scientific information, typically through a selection of visualisation, scientific reports and/or presentations, suitable for a variety of audiences"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating scientific information to audiences"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to convey scientific information to varied audiences, usually through visualisations, reports or presentations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 46972, end: 47062 }
  source: "articulate the value of the skills, knowledge and behaviours gained from a Physics degree."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["articulate"]
  about: "articulating the value of the degree"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to explain the worth of the skills, knowledge and behaviours their degree has given them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 47193, end: 47232 }
  source: "identify issues, questions and problems"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify"]
  about: "identifying issues and problems"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to recognise issues, questions and problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 47235, end: 47297 }
  source: "identify gaps in their own knowledge and acquire new knowledge"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "acquire"]
  about: "closing gaps in one's own knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to find gaps in their own knowledge and fill them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 47300, end: 47333 }
  source: "analyse and interpret information"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["analyse", "interpret"]
  about: "analysing and interpreting information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to analyse and make sense of information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 47336, end: 47391 }
  source: "synthesise the state of knowledge on a particular topic"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["synthesise"]
  about: "synthesising knowledge on a topic"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to pull together what is known about a given topic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 47394, end: 47460 }
  source: "apply knowledge and understanding to provide evidenced conclusions"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["apply", "provide"]
  about: "evidenced conclusions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to use their knowledge and understanding to reach conclusions backed by evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 47463, end: 47504 }
  source: "communicate effectively and appropriately"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["communicate"]
  about: "effective, fitting communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to communicate well and in a way that fits the situation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 47507, end: 47581 }
  source: "present knowledge or an argument in a way that is comprehensible to others"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["present"]
  about: "presenting knowledge or argument clearly"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to set out knowledge or an argument so that others can follow it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 47584, end: 47664 }
  source: "work with a range of data, including qualitative and quantitative empirical data"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["work"]
  about: "working with qualitative and quantitative data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to handle many kinds of data, qualitative and quantitative empirical data among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 47667, end: 47780 }
  source: "critically engage with a range of forms of digital technology to collate, analyse, select and present information"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["engage", "collate", "analyse", "select", "present"]
  about: "critical use of digital technology"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to use varied digital technologies critically to gather, analyse, choose and present information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 47783, end: 47970 }
  source: "assert intellectual independence, including undertaking tasks independently (with appropriate guidance and support), conducting self-directed research and demonstrating critical judgement"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["assert", "undertaking", "conducting", "demonstrating"]
  about: "intellectual independence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to show intellectual independence: working alone with suitable guidance, carrying out self-directed research and exercising critical judgement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.5.b11
  locator: { number: "4.5.b11", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 47973, end: 48133 }
  source: "work collaboratively, including undertaking work in a group or team and/or participating in discussions, showing an appreciation for diversity within the group."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["work", "undertaking", "participating", "showing"]
  about: "collaboration that values diversity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to work with others, in groups, teams or discussion, valuing the diversity of the group."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 48346, end: 48412 }
  source: "the application of physical principles to diverse areas of Physics"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: []
  about: "applying principles across diverse areas"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b2, basis: inferred }
  paraphrase: "Will have shown competence in applying physical principles across varied areas of physics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 48415, end: 48522 }
  source: "the solution of problems in Physics by selecting and using appropriate mathematical and physical techniques"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["selecting", "using"]
  about: "choosing techniques to solve problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b3, basis: inferred }
  paraphrase: "Will have shown competence in solving physics problems by choosing and using fitting mathematical and physical techniques."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 48525, end: 48580 }
  source: "making appropriate approximations when solving problems"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["making", "solving"]
  about: "making approximations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown competence in making suitable approximations when solving problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 48583, end: 48867 }
  source: "critical analysis of the results of an experiment or investigation, evaluation of their significance (both conceptually and statistically) and setting them in context, including a comparison of the results with expected outcomes, theoretical and computational models or published data"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["setting"]
  about: "critical analysis and context of results"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b7, basis: inferred }
  paraphrase: "Will have shown competence in analysing experimental or investigative results critically, judging their conceptual and statistical significance and placing them in context against expectations, models or published data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 48870, end: 48940 }
  source: "the design and execution of experiments (if on an experimental course)"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: []
  about: "designing and running experiments"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b4, basis: inferred }
  paraphrase: "Will have shown competence, on an experimental course, in designing and carrying out experiments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 48943, end: 49032 }
  source: "use of mathematical and computational techniques and analysis to model physical behaviour"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["model"]
  about: "mathematical and computational modelling"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b5, basis: inferred }
  paraphrase: "Will have shown competence in using mathematical and computational techniques and analysis to model how physical systems behave."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.6.b7
  locator: { number: "4.6.b7", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 49035, end: 49116 }
  source: "clear and accurate communication of scientific information to different audiences"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: []
  about: "clear communication to different audiences"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b8, basis: inferred }
  paraphrase: "Will have shown competence in communicating scientific information clearly and accurately to different audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.6.b8
  locator: { number: "4.6.b8", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 49119, end: 49165 }
  source: "management and use of research-based materials"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: []
  about: "managing and using research-based materials"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown competence in managing and using research-based materials."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.6.b9
  locator: { number: "4.6.b9", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 49168, end: 49390 }
  source: "where appropriate, an appreciation of topics related to enterprise and entrepreneurship\n- for example, with design thinking, innovation, project and risk management, business and financial awareness, and commercialisation."
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: []
  about: "enterprise and entrepreneurship"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, where appropriate, an appreciation of enterprise and entrepreneurship, such as design thinking, innovation, managing projects and risk, business and finance and bringing products to market."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.7.b1.masters
  locator: { number: "4.7.b1.masters", headingPath: ["Benchmark standards", "Integrated master's"] }
  span: { start: 49611, end: 49763 }
  source: "a working knowledge of a variety of experimental, mathematical and/or computational techniques applicable to current research or applications in Physics"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "integrated master's graduates at the threshold"
  addressee: learner
  verbs: []
  about: "techniques used in current research"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will also have a working command of a range of experimental, mathematical or computational techniques used in current physics research or applications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.7.b2.masters
  locator: { number: "4.7.b2.masters", headingPath: ["Benchmark standards", "Integrated master's"] }
  span: { start: 49766, end: 49802 }
  source: "undertaken an extended investigation"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "integrated master's graduates at the threshold"
  addressee: learner
  verbs: ["undertaken"]
  about: "an extended investigation"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will also have carried out an extended investigation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.7.b3.masters
  locator: { number: "4.7.b3.masters", headingPath: ["Benchmark standards", "Integrated master's"] }
  span: { start: 49805, end: 49841 }
  source: "encountered research-level material."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "integrated master's graduates at the threshold"
  addressee: learner
  verbs: ["encountered"]
  about: "research-level material"
  themes: [none]
  domain: knowledge
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will also have met material at research level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.8.b1.masters
  locator: { number: "4.8.b1.masters", headingPath: ["Benchmark standards", "Integrated master's"] }
  span: { start: 50052, end: 50197 }
  source: "apply fundamental laws and principles to a variety of areas in Physics, some of which are at (or are informed by) the forefront of the discipline"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "integrated master's graduates at the typical level"
  addressee: learner
  verbs: ["apply"]
  about: "applying laws to areas at the forefront"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to apply fundamental laws and principles across several areas of physics, some at or informed by the forefront."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.8.b2.masters
  locator: { number: "4.8.b2.masters", headingPath: ["Benchmark standards", "Integrated master's"] }
  span: { start: 50200, end: 50264 }
  source: "apply relevant, recent, research to current questions in Physics"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "integrated master's graduates at the typical level"
  addressee: learner
  verbs: ["apply"]
  about: "applying recent research to current questions"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to bring recent, relevant research to bear on current questions in physics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.8.b3.masters
  locator: { number: "4.8.b3.masters", headingPath: ["Benchmark standards", "Integrated master's"] }
  span: { start: 50267, end: 50342 }
  source: "interpret and contextualise mathematical descriptions of physical phenomena"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "integrated master's graduates at the typical level"
  addressee: learner
  verbs: ["interpret", "contextualise"]
  about: "interpreting mathematical descriptions"
  themes: [none]
  domain: understanding
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to interpret mathematical descriptions of physical phenomena and set them in context."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.8.b4.masters
  locator: { number: "4.8.b4.masters", headingPath: ["Benchmark standards", "Integrated master's"] }
  span: { start: 50345, end: 50450 }
  source: "plan and execute an open-ended extended research project or investigation, demonstrating some originality"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "integrated master's graduates at the typical level"
  addressee: learner
  verbs: ["plan", "execute", "demonstrating"]
  about: "an open-ended research project with originality"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: { statement: qaa/physics-astronomy-and-astrophysics-2025/4.7.b2.masters, basis: inferred }
  paraphrase: "Will be able to plan and carry out an open-ended, extended research project or investigation that shows some originality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.8.b5.masters
  locator: { number: "4.8.b5.masters", headingPath: ["Benchmark standards", "Integrated master's"] }
  span: { start: 50453, end: 50538 }
  source: "show the competent use of specialised equipment or research grade software or methods"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "integrated master's graduates at the typical level"
  addressee: learner
  verbs: ["show"]
  about: "specialised equipment and research-grade tools"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: { statement: qaa/physics-astronomy-and-astrophysics-2025/4.7.b1.masters, basis: inferred }
  paraphrase: "Will be able to use specialised equipment or research-grade software or methods competently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.8.b6.masters
  locator: { number: "4.8.b6.masters", headingPath: ["Benchmark standards", "Integrated master's"] }
  span: { start: 50541, end: 50618 }
  source: "master new techniques in a theoretical, computational or experimental context"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "integrated master's graduates at the typical level"
  addressee: learner
  verbs: ["master"]
  about: "mastering new techniques"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to learn new theoretical, computational or experimental techniques thoroughly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.8.b7.masters
  locator: { number: "4.8.b7.masters", headingPath: ["Benchmark standards", "Integrated master's"] }
  span: { start: 50621, end: 50761 }
  source: "communicate complex scientific ideas, including the concise, accurate and informative conclusions of an experiment, investigation or project"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "integrated master's graduates at the typical level"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating complex ideas and conclusions"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to convey complex scientific ideas, including brief, precise and informative conclusions from an experiment, investigation or project."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/physics-astronomy-and-astrophysics-2025/4.8.b8.masters
  locator: { number: "4.8.b8.masters", headingPath: ["Benchmark standards", "Integrated master's"] }
  span: { start: 50764, end: 50884 }
  source: "demonstrate an understanding of scientific research and propose realistic suggestions as to how it may progress further."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "integrated master's graduates at the typical level"
  addressee: learner
  verbs: ["demonstrate", "propose"]
  about: "understanding research and how it may progress"
  themes: [none]
  domain: understanding
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show an understanding of scientific research and suggest realistic next steps for it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.15
  forPractitioner: { text: "Make sure the curriculum touches each fundamental area (mechanics, relativity, quantum, electromagnetism, thermal and statistical physics, waves and optics, matter) and draws out the principles that cut across them, such as conservation laws and equilibrium.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Whatever route you take, your course will introduce you to the core areas of physics, from mechanics and relativity to quantum and thermal physics, and help you see the principles, such as conservation laws, that link them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe paragraph 1.15 as the statement's expected common core (will) for every honours and integrated master's degree in the subject, held at FHEQ level 6 and FQHEIS level 10. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.15). Do not claim it fixes how much time each area receives, since it says each is covered to some extent. Set it beside 1.16 and 1.17 (application and astronomy topics), 2.1 and the honours descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student asks what every physics degree contains or a team checks its core modules. For a student, name the core areas plainly and ask which of them feel secure and which feel thin; for staff, ask where each area and the cross-cutting principles are taught. Do not read out the list of areas at length or suggest that every area is taught to the same depth."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.18
  forPractitioner: { text: "Take at least some core areas to a level where students can read and use current research literature, and give them a feel for recent advances in the field.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your course will take some core topics far enough that you can read and make sense of current research papers, and will show you recent advances in physics.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe paragraph 1.18 as an expected outcome (will) of every degree in the subject: depth in some core areas sufficient to read current research, at FHEQ level 6. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.18). Do not claim it asks for depth in every area or for original research at honours level. Set it beside 4.6.b8 (research-based materials), 4.7.b3.masters and the honours descriptor qaa/fheq-2024/4.15.b3.2."
  author-agent-dialogue: "Raise it when a student wonders why final-year modules lean on journal papers or a team plans advanced options. Ask a student: which recent paper in your area could you explain to a friend? Ask staff which core areas reach research depth. Avoid suggesting the student must master the literature across the whole subject."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.20.b1
  forPractitioner: { text: "Graduates will be able to meet unfamiliar problems flexibly and adapt their approach.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to tackle problems you have not met before, adapting your approach as you go.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 1.20.b1 as an expected outcome (will) of every degree in the subject, a professional skill (meeting new problems flexibly) held at FHEQ level 6 for honours and carried into the integrated master's. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.20). Do not present it as one of the threshold rungs in section 4 or as a professional body requirement. Set it beside 4.5.b1 and 4.6.b3 and qaa/fheq-2024/4.15.b9.2."
  author-agent-dialogue: "Raise it when a student feels stuck on an unfamiliar problem or a team designs open-ended tasks. For a student, put it in plain second-person terms and ask: what did you try first, and what did you change when it did not work? For staff, ask where the course builds and checks this skill. Avoid reading the list aloud or treating it as an assessed threshold."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.20.b2
  forPractitioner: { text: "Graduates will communicate complex data and ideas clearly, matching the medium to the content and to who is listening.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to explain complex data and ideas clearly, picking the format that suits your material and your audience.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 1.20.b2 as an expected outcome (will) of every degree in the subject, a professional skill (clear communication of complex material to suit the audience) held at FHEQ level 6 for honours and carried into the integrated master's. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.20). Do not present it as one of the threshold rungs in section 4 or as a professional body requirement. Set it beside 4.4.b8, 4.5.b6 and 4.6.b7 and qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise it when a student prepares a talk, poster or report. For a student, put it in plain second-person terms and ask: who is your audience, and what will they need from your figures? For staff, ask where the course builds and checks this skill. Avoid reading the list aloud or treating it as an assessed threshold."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.20.b3
  forPractitioner: { text: "Graduates will work effectively on their own and in teams.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to work well both on your own and as part of a team.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 1.20.b3 as an expected outcome (will) of every degree in the subject, a professional skill (working individually and in teams) held at FHEQ level 6 for honours and carried into the integrated master's. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.20). Do not present it as one of the threshold rungs in section 4 or as a professional body requirement. Set it beside 4.5.b11 and 4.5.b10 and qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student reflects on group work or a team plans team projects. For a student, put it in plain second-person terms and ask: what did you contribute to the group, and what did you do better alone? For staff, ask where the course builds and checks this skill. Avoid reading the list aloud or treating it as an assessed threshold."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.20.b4
  forPractitioner: { text: "Graduates will manage their time and deadlines.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to manage your time and meet your deadlines.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 1.20.b4 as an expected outcome (will) of every degree in the subject, a professional skill (time and deadline management) held at FHEQ level 6 for honours and carried into the integrated master's. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.20). Do not present it as one of the threshold rungs in section 4 or as a professional body requirement. Set it beside 4.5.b10 and qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student struggles with workload or a team spaces deadlines. For a student, put it in plain second-person terms and ask: how do you plan your week when three deadlines fall together? For staff, ask where the course builds and checks this skill. Avoid reading the list aloud or treating it as an assessed threshold."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.20.b5
  forPractitioner: { text: "Graduates will critically analyse their own work and that of others.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to assess your own work and other people's work critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 1.20.b5 as an expected outcome (will) of every degree in the subject, a professional skill (critical analysis of one's own and others' work) held at FHEQ level 6 for honours and carried into the integrated master's. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.20). Do not present it as one of the threshold rungs in section 4 or as a professional body requirement. Set it beside 4.5.b3 and 4.6.b4 and qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student reviews a peer's report or receives feedback. For a student, put it in plain second-person terms and ask: what is the weakest point in this piece of work, and how would you fix it? For staff, ask where the course builds and checks this skill. Avoid reading the list aloud or treating it as an assessed threshold."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.20.b6
  forPractitioner: { text: "Graduates will be able to identify potential ethical issues in their own work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to spot the ethical questions your own work might raise.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 1.20.b6 as an expected outcome (will) of every degree in the subject, a professional skill (identifying ethical issues in one's own work) held at FHEQ level 6 for honours and carried into the integrated master's. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.20). Do not present it as one of the threshold rungs in section 4 or as a professional body requirement. Set it beside 1.20.b7 and 1.51 and qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Raise it when a student plans a project with data, people or AI tools. For a student, put it in plain second-person terms and ask: who could be affected by this work, and how? For staff, ask where the course builds and checks this skill. Avoid reading the list aloud or treating it as an assessed threshold."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.20.b7
  forPractitioner: { text: "Graduates will understand that fabrication, falsification, misrepresentation and plagiarism are scientific misconduct, and will see that a professional physicist should be objective and honest about the limits of methods and knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand that inventing, altering or misreporting data or plagiarising is scientific misconduct, and that a professional physicist should be objective, honest and open about the limits of their methods and knowledge.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 1.20.b7 as an expected outcome (will) of every degree in the subject, a professional skill (research integrity and honesty about limits) held at FHEQ level 6 for honours and carried into the integrated master's. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.20). Do not present it as one of the threshold rungs in section 4 or as a professional body requirement. Set it beside 1.20.b6, 4.4.b7 and 1.51 and qaa/fheq-2024/4.15.b4."
  author-agent-dialogue: "Raise it when a student is tempted to tidy awkward data or asks about referencing. For a student, put it in plain second-person terms and ask: what would you report if your result disagreed with theory? For staff, ask where the course builds and checks this skill. Avoid reading the list aloud or treating it as an assessed threshold."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.20.b8
  forPractitioner: { text: "Graduates will understand what a safe working environment requires.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand what it takes to keep a workplace or laboratory safe.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 1.20.b8 as an expected outcome (will) of every degree in the subject, a professional skill (understanding of safe working) held at FHEQ level 6 for honours and carried into the integrated master's. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.20). Do not present it as one of the threshold rungs in section 4 or as a professional body requirement. Set it beside 4.4.b4 (safe use of apparatus) and qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Raise it when a student starts lab work or a placement. For a student, put it in plain second-person terms and ask: what are the main hazards in this lab, and who would you tell about a problem? For staff, ask where the course builds and checks this skill. Avoid reading the list aloud or treating it as an assessed threshold."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.20.b9
  forPractitioner: { text: "Graduates will appreciate environmental and sustainability issues.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand environmental and sustainability issues and why they matter in physics.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 1.20.b9 as an expected outcome (will) of every degree in the subject, a professional skill (an appreciation of environmental and sustainability issues) held at FHEQ level 6 for honours and carried into the integrated master's. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.20). Do not present it as one of the threshold rungs in section 4 or as a professional body requirement. Set it beside 1.35 to 1.39 (the sustainability theme) and spine:6."
  author-agent-dialogue: "Raise it when a student asks how physics connects to climate or energy. For a student, put it in plain second-person terms and ask: which part of your course connects most clearly to a sustainability problem? For staff, ask where the course builds and checks this skill. Avoid reading the list aloud or treating it as an assessed threshold."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.20.b10
  forPractitioner: { text: "Graduates will know about professional practice, such as business awareness, project management, entrepreneurship and intellectual property.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know how professional work in physics runs, from business and project management to entrepreneurship and intellectual property.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 1.20.b10 as an expected outcome (will) of every degree in the subject, a professional skill (knowledge of professional practice) held at FHEQ level 6 for honours and carried into the integrated master's. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.20). Do not present it as one of the threshold rungs in section 4 or as a professional body requirement. Set it beside 4.6.b9 and 1.40 to 1.46 and qaa/fheq-2024/4.15.b9.3."
  author-agent-dialogue: "Raise it when a student considers industry, a start-up or a placement. For a student, put it in plain second-person terms and ask: what do you know about how a physics company protects its ideas? For staff, ask where the course builds and checks this skill. Avoid reading the list aloud or treating it as an assessed threshold."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.22
  forPractitioner: { text: "Build equity, diversity and inclusion into the department's culture, curriculum, teaching and assessment, aware of protected characteristics and personal circumstances such as caring or economic disadvantage, so that every student's contribution is welcomed and enabled.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.22 as advice the statement gives to course teams and providers (should), opening the discipline to all through inclusive culture, curricula, teaching and assessment; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.22). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation (here the Equality Act 2010). Set it beside 1.23 to 1.26 (the rest of the EDI theme), 1.27 (accessibility) and 4.3."
  author-agent-dialogue: "Raise it with a programme team when it reviews its culture, curriculum or assessment for inclusion. Frame it for staff as what the course should do, and ask: whose experiences and backgrounds does the current curriculum reflect, and whose does it miss? Do not put it to a student as something they must do. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.23
  forPractitioner: { text: "Show in content and examples the range of people, cultures and ideas that have shaped physics and its applications, and treat the discipline's history honestly as a shared, worldwide enterprise.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.23 as advice the statement gives to course teams and providers (should), a curriculum that reflects the range of people and ideas behind physics; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.23). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 1.22, 1.24 and 1.8 (diverse collaboration)."
  author-agent-dialogue: "Raise it with a programme team when it chooses examples, case studies or reading lists. Frame it for staff as what the course should do, and ask: whose work appears in the examples students meet, and what does that tell them about who does physics? Do not put it to a student as something they must do. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.24
  forPractitioner: { text: "Design every activity to be accessible, offer equivalent alternatives where one cannot be, and check placement and field-trip locations for risk of discrimination; expect students to leave with an awareness of EDI they can use at work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to take part in every activity on your course, or be offered a fair alternative, without facing discrimination. Along the way you will build an awareness of equity, diversity and inclusion that helps you support others and work professionally.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.24 as two things: advice to course teams (should) that every activity be inclusive with fair alternatives, and an expected outcome (will) that students gain EDI awareness, a generic skill at FHEQ level 6. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.24). Do not merge the two forces or claim it guarantees every placement is free of risk. Set it beside 1.22, 4.5.b11 (working with diversity in a group) and qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it with a student worried about a placement, a field trip or being left out, and with a team planning off-site activities. Ask a student: has any part of your course felt closed to you, and what alternative would help? Ask staff how they check a location for risk of discrimination. Avoid placing on the student the duty to secure alternatives; that sits with the course."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.25
  forPractitioner: { text: "Treat EDI as part of every activity, for staff and students alike, rather than as a separate module or policy, and give everyone equivalent opportunities and a shared responsibility for it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.25 as advice the statement gives to course teams and providers (should), equity, diversity and inclusion running through all learning, teaching, practice and support; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.25). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 1.22, 1.26 and qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Raise it with a programme team when it asks whether EDI is confined to one place in the course. Frame it for staff as what the course should do, and ask: where do students meet EDI outside a single session or policy document? Do not put it to a student as something they must do. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.26
  forPractitioner: { text: "Act to remove harmful stereotypes, language and barriers, and to challenge structural disadvantage, working in partnership with students; make clear that staff and students share responsibility for an inclusive culture.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Everyone in physics, you included, shares responsibility for an inclusive culture: you can help by challenging stereotypes and careless language and by working with staff to remove barriers.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.26 as advice (should) to take active steps against stereotypes, barriers and structural disadvantage, with the responsibility for an inclusive culture shared by staff and students. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.26). Do not present it as a rule a student can be assessed against or as a legal duty. Set it beside 1.22, 1.25 and 1.24."
  author-agent-dialogue: "Raise it when a student or team describes unwelcoming language or a barrier to taking part. For a student, put it plainly as a shared job and ask: what is one thing you or your group could change? For staff, ask how students are brought into removing barriers. Avoid making the student responsible for fixing structural problems on their own."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.27
  forPractitioner: { text: "Design learning and assessment to be equally accessible from the outset and add reasonable individual adjustments where a student still needs them, so that all can thrive and feel they belong.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.27 as advice the statement gives to course teams and providers (should), learning and assessment equally accessible through inclusive design first and individual adjustments second; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.27). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation (here equality law). Set it beside 1.28 (inclusive design defined), 1.30, 1.33 and 3.7."
  author-agent-dialogue: "Raise it with a programme team when it designs assessment or responds to a request for adjustment. Frame it for staff as what the course should do, and ask: which barriers in this module could inclusive design remove for everyone, before any individual adjustment? A student may ask about it; tell them what they can expect, but do not frame it as their task. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.29
  forPractitioner: { text: "Keep admissions fair: decisions should not rest on staff or student assumptions about a candidate's barriers to learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.29 as advice the statement gives to course teams and providers (should), equitable entry unaffected by assumptions about barriers to learning; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.29). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 1.27, 2.10 (alternative entry routes) and 1.22."
  author-agent-dialogue: "Raise it with a programme team when it reviews admissions or interview practice. Frame it for staff as what the course should do, and ask: what assumptions about a disabled applicant could creep into this decision, and how would we know? Do not put it to a student as something they must do. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.30
  forPractitioner: { text: "Use the Disabled Student Commitment, check that communications are accessible, and give particular attention to labs, computing work and mathematical or graphical content; consider mixing synchronous and asynchronous delivery for disabled and neurodivergent students.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.30 as advice the statement gives to course teams and providers (should), using the Disabled Student Commitment and making labs, computing and mathematical content accessible; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.30). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 1.27, 1.31 (limits of adaptive technology) and 1.33."
  author-agent-dialogue: "Raise it with a programme team when it plans labs, coding sessions or mathematical materials. Frame it for staff as what the course should do, and ask: how would a screen-reader user or a neurodivergent student work through this lab script or problem sheet? Do not put it to a student as something they must do. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.31
  forPractitioner: { text: "Recognise that current assistive tools handle code, equations and diagrams poorly, and fund the extra support and resources that close the gap.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.31 as advice the statement gives to course teams and providers (should), resourcing support where assistive technology does not yet cope with code, mathematics and diagrams; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.31). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 1.30, 1.34 and 1.27."
  author-agent-dialogue: "Raise it with a programme team when it budgets for accessibility support. Frame it for staff as what the course should do, and ask: which parts of the course rely on code, equations or diagrams that assistive tools render badly, and what support fills the gap? Do not put it to a student as something they must do. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.32
  forPractitioner: { text: "Widen access to placements, volunteering and other extras by anticipating the hidden costs and extra hurdles some students face.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.32 as advice the statement gives to course teams and providers (should), equal access to placements, volunteering and similar opportunities; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.32). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 2.2, 2.13 (placements) and 1.27."
  author-agent-dialogue: "Raise it with a programme team when it advertises placements or volunteering. Frame it for staff as what the course should do, and ask: what hidden costs or hurdles might stop some students taking this up, and what can the course do about them? Do not put it to a student as something they must do. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.33
  forPractitioner: { text: "Agree reasonable adjustments with the student and the support service together, and see that they are carried through in teaching and assessment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.33 as advice the statement gives to course teams and providers (should), agreeing reasonable individual adjustments with students and support services; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.33). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 1.27, 1.30 and 1.34."
  author-agent-dialogue: "Raise it with a programme team when a student needs an adjustment. Frame it for staff as what the course should do, and ask: who speaks with the student and the support service, and how is the agreed adjustment checked in practice? With a student, say plainly that the course should talk this through with them; do not make it their task. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.34
  forPractitioner: { text: "Give course teams the training and resources they need to deliver accessibility in practice, not only in policy.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.34 as advice the statement gives to course teams and providers (should), training and resourcing course teams to make accessibility work in practice; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.34). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 1.30, 1.31 and 1.33."
  author-agent-dialogue: "Raise it with a programme team when it reviews staff development. Frame it for staff as what the course should do, and ask: what training has the team had in accessible teaching of laboratory and mathematical work? Do not put it to a student as something they must do. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.43
  forPractitioner: { text: "Work with careers advisers to help students recognise and express the skills, knowledge and behaviours they have gained and link them to work-based learning and graduate roles.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.43 as advice the statement gives to course teams and providers (should), working with careers advisers so students can explain the value of what they have learned; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.43). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 4.4.b9 (the threshold outcome it supports), 1.40 to 1.42 and qaa/fheq-2024/4.15.b9.3."
  author-agent-dialogue: "Raise it with a programme team when it plans careers input or personal tutoring. Frame it for staff as what the course should do, and ask: where in the course do students practise explaining their skills to an employer? With a student, turn it into the related outcome at 4.4.b9 rather than a duty on them. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.48
  forPractitioner: { text: "Build guidance, training and practice in generative AI into the curriculum so students learn to use it ethically and effectively for study and later work.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe paragraph 1.48 as the statement's view that students need guided preparation in generative AI within the curriculum; its obliging word is 'need', outside the five, so record its force as descriptive and do not raise it to must or should. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.48). Do not claim it requires any particular tool or policy. Set it beside 1.49 to 1.51, 3.5 and 4.5.b9 (digital technology)."
  author-agent-dialogue: "Raise it with a programme team when it decides how generative AI appears in teaching. Frame it for staff as what the course should do, and ask: where do students practise using AI tools under guidance, and how do they learn when not to? With a student, talk about the guidance they can expect; do not treat it as a rule they have broken or met. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.49
  forPractitioner: { text: "Revisit skills, activities and learning outcomes in light of generative AI, adopting it where it helps while teaching its risks and limitations.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.49 as advice the statement gives to course teams and providers (should), adopting generative AI in the degree while keeping its risks and limits in view; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.49). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 1.48, 1.50 and 1.51."
  author-agent-dialogue: "Raise it with a programme team when it reviews outcomes or activities that generative AI now affects. Frame it for staff as what the course should do, and ask: which learning outcome has AI changed most, and what risk do students need to understand? Do not put it to a student as something they must do. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.50
  forPractitioner: { text: "Design some assessments that openly use generative AI, testing critical thinking and creative problem solving rather than simply banning the tools.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.50 as advice the statement gives to course teams and providers (should), welcoming assessment that recognises generative AI and builds critical, creative problem solving; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.50). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 1.51, 3.9 (critical use of AI outputs as an assessment method) and 3.10."
  author-agent-dialogue: "Raise it with a programme team when it designs or revises assessments. Frame it for staff as what the course should do, and ask: in which assessment could students use AI openly and be judged on how critically they handle it? Do not put it to a student as something they must do. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/1.51
  forPractitioner: { text: "Teach responsible, ethical and safe use of generative AI, including data protection and intellectual property, and train students to check AI output for accuracy, relevance and bias.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should use generative AI responsibly, ethically and safely, never feeding it sensitive data, and you should check what it gives you for accuracy, relevance and bias.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.51 as advice (should) addressed both to students, on responsible use of generative AI, and to courses, on training them to critique its output; treat the critique as a generic skill at FHEQ level 6. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 1.51). Do not claim it bans generative AI or sets a legal standard beyond data protection law. Set it beside 1.48, 1.50, 4.5.b9 and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student uses or plans to use an AI tool for code, writing or data, or a team sets AI rules. Ask a student: what did you check before trusting that output, and did any of the data you gave it need protecting? Ask staff where students are trained to critique AI output. Avoid moralising or reading the paragraph aloud; keep it practical."
- statement: qaa/physics-astronomy-and-astrophysics-2025/2.5
  forPractitioner: { text: "On joint, combined and major or minor routes, make sure students still reach the core subject and generic skills, and use the overlap with the other subject for interdisciplinary study.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study physics alongside another subject, you will still gain the core physics and general skills, add skills from your other subject and may find interesting ground where the two meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe paragraph 2.5 as an expected outcome (will) for joint and combined honours students: the core of the threshold lists at FHEQ level 6, plus skills from the other subject. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 2.5). Do not claim joint students must meet every item of 4.4 and 4.5 in full; the statement says core elements. Set it beside 4.4, 4.5, 1.13 and the honours descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a joint honours student asks whether they count as a physicist or a team designs a combined route. Ask a student: which core physics skills feel strongest, and where does your other subject add something? Ask staff which items of the threshold lists the joint route secures. Avoid implying the joint route is a lesser award."
- statement: qaa/physics-astronomy-and-astrophysics-2025/2.12
  forPractitioner: { text: "Set credit for study abroad by duration and home regulations, and calibrate partner marks with care before they count towards the classification.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 2.12 as advice the statement gives to course teams and providers (should), calibrating marks earned with a partner before they count towards the classification; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 2.12). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 2.11, 2.13 and 4.2 (Annex D)."
  author-agent-dialogue: "Raise it with a programme team when it approves a study-abroad partnership or converts partner marks. Frame it for staff as what the course should do, and ask: how are this partner's marks mapped onto the home scale, and who checks the mapping? With a student going abroad, explain how credit will count; do not make calibration their task. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/3.4
  forPractitioner: { text: "Teach generic skills through physics contexts where it makes sense, and let laboratory and observational work become more open-ended, with stricter reporting expectations, as students advance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 3.4 as advice the statement gives to course teams and providers (should), developing generic and subject skills through physics applications, with lab work growing more open-ended; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 3.4). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 4.5 (generic skills), 4.4.b4, 4.6.b5 and spine:6."
  author-agent-dialogue: "Raise it with a programme team when it maps skills across years. Frame it for staff as what the course should do, and ask: how does laboratory work become more open-ended from first year to final year? Do not put it to a student as something they must do. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/3.7
  forPractitioner: { text: "Choose teaching methods freely, but check in design that each supports the learning outcomes and is inclusive and accessible to every student.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 3.7 as advice the statement gives to course teams and providers (should), checking in design that teaching methods support the outcomes and are inclusive and accessible; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 3.7). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 3.2, 1.27 and 1.28."
  author-agent-dialogue: "Raise it with a programme team when it designs or reviews a module. Frame it for staff as what the course should do, and ask: how does each teaching method serve an outcome, and who might it leave out? Do not put it to a student as something they must do. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/3.11
  forPractitioner: { text: "Write assessment regulations that let examiners judge a student's overall performance against all outcomes, since problem-heavy modules often produce marks across the whole range.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe paragraph 3.11 as the statement's view that regulations need flexibility for uneven marks in a quantitative subject; its obliging word is 'need', outside the five, so record the force as descriptive. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 3.11). Do not claim it permits failed modules to be ignored or overrides a provider's regulations. Set it beside 3.10, 4.2 and qaa/fheq-2024/annex-d/summary/r1/3rd."
  author-agent-dialogue: "Raise it with a programme team when an exam board meets a student who failed a module but did well overall. Frame it for staff as what the course should do, and ask: do our regulations let the board weigh this student's whole profile against the course outcomes? Do not promise a student that a failed module will be overlooked. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.2
  forPractitioner: { text: "Use Annex D's descriptions of the first, upper second, lower second and third to judge and evidence performance above the threshold.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 4.2 as advice the statement gives to course teams and providers (should), referring to Annex D of the Frameworks (2024) to evidence achievement above the threshold; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.2). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation. Set it beside 4.1, the 4.4 and 4.6 rungs and qaa/fheq-2024/annex-d/summary/r1/3rd to qaa/fheq-2024/annex-d/summary/r1/1st."
  author-agent-dialogue: "Raise it with a programme team when it writes marking criteria or classification rules. Frame it for staff as what the course should do, and ask: how do our criteria for a first or an upper second draw on Annex D, and do they go beyond the threshold lists? With a student, explain that most graduates go well beyond the threshold; do not treat the threshold as the target. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.3
  forPractitioner: { text: "Do not treat the rung lists as competence standards; if you write competence standards into a programme specification, draw on them and any PSRB requirements and follow current Equality and Human Rights Commission guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 4.3 as advice the statement gives to course teams and providers (should), following current Equality and Human Rights Commission guidance when competence standards are set, since the rungs are not competence standards; it binds no student and is not a condition of the award. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.3). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation (here the Equality Act 2010). Set it beside 4.1, 4.4 to 4.8, 1.22 and SB5 (bodies)."
  author-agent-dialogue: "Raise it with a programme team when it writes competence standards or reviews them for disabled students. Frame it for staff as what the course should do, and ask: which items here are genuine competence standards, and have we checked them against current EHRC guidance? Do not put it to a student as something they must do. Summarise rather than reading the paragraph aloud."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b1
  forPractitioner: { text: "At threshold, honours graduates should understand the basic laws and principles of physics and apply them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you should be able to understand the basic laws and principles of physics and put them to use.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.4.b1 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: understanding and using the basic laws and principles of physics. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.4). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.4.b2 and 1.15 and qaa/fheq-2024/4.15.b1 (with qaa/fqheis-2024/4.16.b1)."
  author-agent-dialogue: "Raise it when a student doubts their grasp of the fundamentals. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: which basic law could you explain and use on a problem today without notes? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b2
  forPractitioner: { text: "At threshold, honours graduates should identify which physical laws and principles apply to a simple problem and use them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you should be able to work out which physical laws apply to a straightforward problem and use them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.4.b2 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: selecting and using relevant laws on simple problems. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.4). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.4.b3 and the typical item 4.6.b1 and qaa/fheq-2024/4.15.b3.1."
  author-agent-dialogue: "Raise it when a student can recall laws but not pick the right one. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: faced with this problem, how did you decide which principle to start from? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b3
  forPractitioner: { text: "At threshold, honours graduates should solve physics problems using suitable mathematical and physical techniques.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you should be able to solve physics problems with the right mathematical and physical methods.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.4.b3 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: problem solving with suitable mathematical and physical techniques. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.4). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.6.b2 (its typical counterpart) and 1.19 and qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise it when a student struggles with problem sheets. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: where does a solution usually go wrong for you, the physics or the mathematics? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b4
  forPractitioner: { text: "At threshold, honours graduates on experimental courses should run an experiment, analyse its results and use basic apparatus safely.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you should be able to run an experiment and analyse what it shows, using basic equipment safely, if your course includes lab work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.4.b4 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: executing and analysing an experiment with safe use of basic apparatus, on experimental courses only. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.4). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.6.b5 (its typical counterpart), 1.20.b8 and 1.12 (theoretical courses) and qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise it when a student prepares for lab work or asks about a theory-only route. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: in your last experiment, what did you check before trusting your results? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b5
  forPractitioner: { text: "At threshold, honours graduates should use suitable software packages or systems competently for data analysis, simulation and information retrieval.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you should be able to use the right software confidently to analyse data, simulate physical systems and find information.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.4.b5 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: competent use of software for data analysis, simulation and finding information. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.4). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.6.b6, 4.5.b9 and 3.5 and qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student talks about coding or data tools. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: which software do you reach for to analyse or simulate, and what can you not yet do with it? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b6
  forPractitioner: { text: "At threshold, honours graduates should handle data numerically and present and interpret information graphically.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you should be able to work with data numerically and present and read information in graphs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.4.b6 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: numerical handling of data and graphical presentation and interpretation. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.4). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.4.b7 and 4.5.b8 and qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Raise it when a student prepares figures or a data analysis. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: what does this graph tell a reader at a glance? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b7
  forPractitioner: { text: "At threshold, honours graduates should conduct an investigation and analyse its results, evaluating their uncertainty or limitations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you should be able to carry out an investigation, analyse what you find and judge how uncertain or limited your results are.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.4.b7 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: carrying out an investigation and analysing results with their uncertainty and limits. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.4). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.6.b4 (its typical counterpart) and 1.20.b7 and qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise it when a student writes up a project or lab report. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: how sure are you of this result, and what limits it? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b8
  forPractitioner: { text: "At threshold, honours graduates should communicate scientific information for a range of audiences through visuals, reports or presentations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you should be able to explain scientific information to different audiences through figures, reports or talks.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.4.b8 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: communicating scientific information for several audiences. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.4). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.6.b7 (its typical counterpart), 4.5.b6 and 1.20.b2 and qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise it when a student prepares a report, talk or poster. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: how would you change this for a non-specialist audience? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.4.b9
  forPractitioner: { text: "At threshold, honours graduates should articulate the value of what their physics degree has developed in them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you should be able to explain clearly what your degree has given you in skills, knowledge and behaviours, for example to an employer.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.4.b9 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: explaining the value of what the degree has developed, a generic skill. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.4). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 1.43 (the course duty that supports it) and 1.20.b10 and qaa/fheq-2024/4.15.b9.3 and qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Raise it when a student prepares a CV, application or interview. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: which three skills from your degree would you lead with, and what evidence do you have? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.5.b1
  forPractitioner: { text: "At threshold, honours graduates should identify issues, questions and problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, as a general skill, you should be able to spot the issues, questions and problems in a situation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.5.b1 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: identifying issues, questions and problems, a generic skill. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.5). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.5.b3 and 1.20.b1 and qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student begins a project or open problem. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: what exactly is the question here? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.5.b2
  forPractitioner: { text: "At threshold, honours graduates should identify gaps in their knowledge and acquire what they need.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, as a general skill, you should be able to notice what you do not yet know and go and learn it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.5.b2 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: finding and filling gaps in one's own knowledge. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.5). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.5.b10 and 4.6.b8 and qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student meets a topic they have not covered. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: what do you need to learn for this, and where will you find it? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.5.b3
  forPractitioner: { text: "At threshold, honours graduates should analyse and interpret information.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, as a general skill, you should be able to analyse information and work out what it means.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.5.b3 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: analysis and interpretation of information. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.5). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.5.b8 and 4.4.b6 and qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student reads a source or dataset. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: what does this information show, and what does it not show? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.5.b4
  forPractitioner: { text: "At threshold, honours graduates should synthesise the current state of knowledge on a topic.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, as a general skill, you should be able to bring together what is known on a topic into a clear overview.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.5.b4 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: synthesising what is known on a topic. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.5). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.6.b8 and 1.18 and qaa/fheq-2024/4.15.b3.2 and qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise it when a student writes a literature review or project introduction. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: what are the two or three main things known on this topic, and where do sources disagree? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.5.b5
  forPractitioner: { text: "At threshold, honours graduates should apply knowledge and understanding to reach evidenced conclusions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, as a general skill, you should be able to use what you know to reach conclusions you can back with evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.5.b5 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: reaching conclusions supported by evidence. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.5). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.4.b7 and 4.6.b4 and qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a student drafts a conclusion. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: which evidence supports this conclusion most strongly? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.5.b6
  forPractitioner: { text: "At threshold, honours graduates should communicate effectively and appropriately.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, as a general skill, you should be able to communicate well and in a way that suits the situation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.5.b6 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: effective and appropriate communication, a generic skill. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.5). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.4.b8 and 4.5.b7 and qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student prepares any written or spoken work. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: who will read or hear this, and what tone suits them? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.5.b7
  forPractitioner: { text: "At threshold, honours graduates should present knowledge or an argument comprehensibly to others.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, as a general skill, you should be able to set out what you know or an argument so others can follow it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.5.b7 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: presenting knowledge or argument so others can follow it. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.5). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.5.b6 and 4.4.b8 and qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a student plans an essay, talk or viva. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: could someone outside physics follow your argument step by step? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.5.b8
  forPractitioner: { text: "At threshold, honours graduates should work with a range of data, both qualitative and quantitative.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, as a general skill, you should be able to work with many kinds of data, numerical and descriptive.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.5.b8 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: working with a range of qualitative and quantitative data. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.5). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.4.b6 and 4.5.b3 and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student meets non-numerical evidence, such as interview or survey data. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: how would you handle evidence here that is not a number? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.5.b9
  forPractitioner: { text: "At threshold, honours graduates should engage critically with varied digital technologies to collate, analyse, select and present information.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, as a general skill, you should be able to use a range of digital tools critically to gather, analyse, choose and present information.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.5.b9 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: critical engagement with digital technology for information. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.5). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.4.b5 and 1.51 (generative AI) and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student relies on a digital tool or AI output. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: how do you know this tool gave you something reliable? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.5.b10
  forPractitioner: { text: "At threshold, honours graduates should show intellectual independence, working independently with guidance, doing self-directed research and judging critically.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, as a general skill, you should be able to show independent thinking: working on your own with the right guidance, doing your own research and judging critically.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.5.b10 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: intellectual independence with guidance. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.5). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 4.5.b2, 4.7.b2.masters and 1.20.b3 and qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student moves into a project or dissertation. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: what decisions in this project did you make yourself, and where did you seek guidance? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.5.b11
  forPractitioner: { text: "At threshold, honours graduates should collaborate in groups, teams or discussion and appreciate the group's diversity.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, as a general skill, you should be able to work with others in groups or discussions and value the different people in the group.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.5.b11 as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), the minimum the statement sets: collaboration that appreciates diversity. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.5). Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement. Set it beside 1.20.b3 and 1.24 (EDI awareness) and qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student reflects on team projects or group tension. Put it to a student in plain words, as something you should be able to do by graduation, the minimum, and ask: how did the different backgrounds in your group help the work? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or treating this minimum as the goal."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.6.b1
  forPractitioner: { text: "At the typical level, honours graduates will have applied physical principles competently across diverse areas of physics.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you will have shown you can apply physical principles across many different areas of physics.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.6.b1 as the typical level for the bachelor's degree with honours (FHEQ level 6), what most graduates reach above the threshold: applying physical principles across diverse areas. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.6). Do not present it as a minimum for the award or as an excellent rung, which the statement does not set. Set it beside 4.4.b2 (the threshold item it grades) and 4.8.b1.masters and qaa/fheq-2024/4.15.b6 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise it when a student wants to move beyond the minimum. Put it to a student in plain words, as what most graduates show, not a minimum, and ask: which principle have you used in two very different areas of physics? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum to pass."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.6.b2
  forPractitioner: { text: "At the typical level, honours graduates will have solved problems by choosing for themselves, and then using, suitable mathematical and physical techniques.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you will have shown you can solve physics problems by choosing the right mathematical and physical methods yourself.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.6.b2 as the typical level for the bachelor's degree with honours (FHEQ level 6), what most graduates reach above the threshold: selecting as well as using techniques to solve problems. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.6). Do not present it as a minimum for the award or as an excellent rung, which the statement does not set. Set it beside 4.4.b3 (the threshold item it grades) and qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/cognitive/r3/2.1."
  author-agent-dialogue: "Raise it when a student can follow worked methods but not choose them. Put it to a student in plain words, as what most graduates show, not a minimum, and ask: why did you pick this method over another? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum to pass."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.6.b3
  forPractitioner: { text: "At the typical level, honours graduates will have made appropriate approximations when solving problems.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you will have shown you can make sensible approximations when solving problems.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.6.b3 as the typical level for the bachelor's degree with honours (FHEQ level 6), what most graduates reach above the threshold: making appropriate approximations. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.6). Do not present it as a minimum for the award or as an excellent rung, which the statement does not set. Set it beside 1.5 (models and approximation) and 1.19 (estimation) and qaa/fheq-2024/4.15.b4."
  author-agent-dialogue: "Raise it when a student is unsure when an approximation is safe. Put it to a student in plain words, as what most graduates show, not a minimum, and ask: what did you neglect here, and how would you check it was safe to do so? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum to pass."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.6.b4
  forPractitioner: { text: "At the typical level, honours graduates will have critically analysed results, evaluated their conceptual and statistical significance and compared them with expected outcomes, models or published data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you will have shown you can analyse your results critically, judge how significant they are and compare them with theory, models or published work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.6.b4 as the typical level for the bachelor's degree with honours (FHEQ level 6), what most graduates reach above the threshold: critical analysis of results, their significance and their context. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.6). Do not present it as a minimum for the award or as an excellent rung, which the statement does not set. Set it beside 4.4.b7 (the threshold item it grades) and 4.8.b7.masters and qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/practical/r4/2.1."
  author-agent-dialogue: "Raise it when a student writes the discussion of a report. Put it to a student in plain words, as what most graduates show, not a minimum, and ask: how does your result compare with theory or published data, and is the difference significant? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum to pass."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.6.b5
  forPractitioner: { text: "At the typical level, honours graduates on experimental courses will have designed and executed experiments.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you will have shown you can design and carry out your own experiments, if your course includes lab work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.6.b5 as the typical level for the bachelor's degree with honours (FHEQ level 6), what most graduates reach above the threshold: designing as well as executing experiments, on experimental courses only. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.6). Do not present it as a minimum for the award or as an excellent rung, which the statement does not set. Set it beside 4.4.b4 (the threshold item it grades) and 3.4 and qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise it when a student moves from scripted to open lab work. Put it to a student in plain words, as what most graduates show, not a minimum, and ask: what would you change in this experiment if you designed it from scratch? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum to pass."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.6.b6
  forPractitioner: { text: "At the typical level, honours graduates will have modelled physical behaviour with mathematical and computational techniques.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you will have shown you can build mathematical and computer models of how physical systems behave.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.6.b6 as the typical level for the bachelor's degree with honours (FHEQ level 6), what most graduates reach above the threshold: modelling physical behaviour mathematically and computationally. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.6). Do not present it as a minimum for the award or as an excellent rung, which the statement does not set. Set it beside 4.4.b5 (the threshold item it grades, a weaker match) and 1.6 and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise it when a student works on simulation or modelling. Put it to a student in plain words, as what most graduates show, not a minimum, and ask: what does your model leave out, and does it matter? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum to pass."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.6.b7
  forPractitioner: { text: "At the typical level, honours graduates will have communicated scientific information clearly and accurately to varied audiences.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you will have shown you can explain science clearly and accurately to different audiences.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.6.b7 as the typical level for the bachelor's degree with honours (FHEQ level 6), what most graduates reach above the threshold: clear and accurate communication to different audiences. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.6). Do not present it as a minimum for the award or as an excellent rung, which the statement does not set. Set it beside 4.4.b8 (the threshold item it grades) and 4.8.b7.masters and qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/transferable/r1/2.1."
  author-agent-dialogue: "Raise it when a student prepares outreach or a final presentation. Put it to a student in plain words, as what most graduates show, not a minimum, and ask: how would you check that your audience understood you correctly? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum to pass."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.6.b8
  forPractitioner: { text: "At the typical level, honours graduates will have managed and used research-based materials competently.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you will have shown you can find, organise and use research papers and other research-based sources.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.6.b8 as the typical level for the bachelor's degree with honours (FHEQ level 6), what most graduates reach above the threshold: managing and using research-based materials. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.6). Do not present it as a minimum for the award or as an excellent rung, which the statement does not set. Set it beside 1.18, 4.5.b4 and 4.7.b3.masters and qaa/fheq-2024/4.15.b5."
  author-agent-dialogue: "Raise it when a student starts a literature search. Put it to a student in plain words, as what most graduates show, not a minimum, and ask: how do you keep track of the papers you read and decide which to rely on? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum to pass."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.6.b9
  forPractitioner: { text: "At the typical level and where the course offers it, honours graduates will have an appreciation of enterprise and entrepreneurship topics, from design thinking and innovation to risk, business, finance and commercialisation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you will have shown an understanding of enterprise and entrepreneurship, such as design thinking, innovation and turning ideas into products, where your course covers it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.6.b9 as the typical level for the bachelor's degree with honours (FHEQ level 6), what most graduates reach above the threshold: an appreciation of enterprise and entrepreneurship where appropriate. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.6). Do not present it as a minimum for the award or as an excellent rung, which the statement does not set. Set it beside 1.20.b10, 1.40 to 1.46 (the enterprise theme) and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Raise it when a student is curious about start-ups or commercial physics. Put it to a student in plain words, as what most graduates show, not a minimum, and ask: how could an idea from your project become a product or service? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum to pass."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.7.b1.masters
  forPractitioner: { text: "At the integrated master's threshold, graduates will have working knowledge of varied experimental, mathematical or computational techniques used in current research or applications.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for an integrated master's, you will also have a working command of several experimental, mathematical or computing techniques used in current physics research.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.7.b1.masters as part of the threshold the integrated master's degree with honours requires (FHEQ level 7, FQHEIS level 11), on top of the typical honours level: working knowledge of techniques used in current research. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.7). Do not apply it to the bachelor's degree or to a taught master's course, which the statement does not cover. Set it beside 4.8.b5.masters (its typical counterpart) and the honours typical list 4.6 and qaa/fheq-2024/4.17.b2 and spine:7."
  author-agent-dialogue: "Raise it when an integrated master's student chooses project methods. Put it to a student in plain words, as the minimum for the integrated master's, and ask: which research technique could you use without step-by-step help? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or applying it to a bachelor's student."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.7.b2.masters
  forPractitioner: { text: "At the integrated master's threshold, graduates will have completed an extended investigation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for an integrated master's, you will also have completed an extended investigation of your own.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.7.b2.masters as part of the threshold the integrated master's degree with honours requires (FHEQ level 7, FQHEIS level 11), on top of the typical honours level: having completed an extended investigation. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.7). Do not apply it to the bachelor's degree or to a taught master's course, which the statement does not cover. Set it beside 4.8.b4.masters (its typical counterpart) and 1.13 and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Raise it when a student plans the master's project. Put it to a student in plain words, as the minimum for the integrated master's, and ask: how will this investigation be longer and deeper than your bachelor's-level work? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or applying it to a bachelor's student."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.7.b3.masters
  forPractitioner: { text: "At the integrated master's threshold, graduates will have engaged with research-level material.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for an integrated master's, you will also have worked with material at the level of current research.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe 4.7.b3.masters as part of the threshold the integrated master's degree with honours requires (FHEQ level 7, FQHEIS level 11), on top of the typical honours level: having met research-level material. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.7). Do not apply it to the bachelor's degree or to a taught master's course, which the statement does not cover. Set it beside 4.8.b2.masters, 4.8.b8.masters and 1.18 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student first reads research papers in depth. Put it to a student in plain words, as the minimum for the integrated master's, and ask: which research-level paper have you worked through, and what did you take from it? With staff, ask where the course teaches and assesses it. Avoid reading the list aloud or applying it to a bachelor's student."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.8.b1.masters
  forPractitioner: { text: "At the integrated master's typical level, graduates will apply fundamental laws and principles to varied areas, some at or near the forefront.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical integrated master's level, you will be able to apply the fundamental laws of physics to several areas, including some at the leading edge.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.8.b1.masters as the typical level for the integrated master's degree with honours (FHEQ level 7), above its threshold: applying fundamental laws to areas at or near the forefront. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.8). Do not present it as the minimum for the integrated master's or apply it to the bachelor's degree. Set it beside 4.6.b1 and 4.8.b2.masters and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student connects coursework to current research. Put it to a student in plain words, as what most integrated master's graduates show, not a minimum, and ask: which leading-edge area can you analyse with the laws you already know? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum for the master's."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.8.b2.masters
  forPractitioner: { text: "At the integrated master's typical level, graduates will apply relevant recent research to current questions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical integrated master's level, you will be able to use recent research to tackle open questions in physics.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.8.b2.masters as the typical level for the integrated master's degree with honours (FHEQ level 7), above its threshold: applying recent research to current questions. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.8). Do not present it as the minimum for the integrated master's or apply it to the bachelor's degree. Set it beside 4.7.b3.masters and 4.8.b8.masters and qaa/fheq-2024/4.17.b4.1."
  author-agent-dialogue: "Raise it when a student frames a research question. Put it to a student in plain words, as what most integrated master's graduates show, not a minimum, and ask: which recent result changes how you would approach this question? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum for the master's."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.8.b3.masters
  forPractitioner: { text: "At the integrated master's typical level, graduates will interpret and contextualise mathematical descriptions of physical phenomena.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical integrated master's level, you will be able to read the mathematics behind a physical phenomenon and explain what it means and where it fits.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.8.b3.masters as the typical level for the integrated master's degree with honours (FHEQ level 7), above its threshold: interpreting and contextualising mathematical descriptions. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.8). Do not present it as the minimum for the integrated master's or apply it to the bachelor's degree. Set it beside 4.6.b6 and 1.5 and qaa/fheq-2024/4.17.b3."
  author-agent-dialogue: "Raise it when a student can manipulate equations but not explain them. Put it to a student in plain words, as what most integrated master's graduates show, not a minimum, and ask: what does each term in this equation mean physically? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum for the master's."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.8.b4.masters
  forPractitioner: { text: "At the integrated master's typical level, graduates will plan and carry out an open-ended extended research project showing some originality.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical integrated master's level, you will be able to plan and run an open-ended research project of your own that shows some original thinking.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.8.b4.masters as the typical level for the integrated master's degree with honours (FHEQ level 7), above its threshold: planning and executing an open-ended project with some originality. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.8). Do not present it as the minimum for the integrated master's or apply it to the bachelor's degree. Set it beside 4.7.b2.masters (the threshold item it grades) and qaa/fheq-2024/4.17.b6 and qaa/fheq-2024/4.17.b3."
  author-agent-dialogue: "Raise it when a student scopes the master's project. Put it to a student in plain words, as what most integrated master's graduates show, not a minimum, and ask: what part of this project is your own idea? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum for the master's."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.8.b5.masters
  forPractitioner: { text: "At the integrated master's typical level, graduates will use specialised equipment or research-grade software or methods competently.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical integrated master's level, you will be able to use specialist equipment or research-grade software and methods with confidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.8.b5.masters as the typical level for the integrated master's degree with honours (FHEQ level 7), above its threshold: confident handling of specialist instruments or research-grade codes and methods. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.8). Do not present it as the minimum for the integrated master's or apply it to the bachelor's degree. Set it beside 4.7.b1.masters (the threshold item it grades) and qaa/fheq-2024/4.17.b2."
  author-agent-dialogue: "Raise it when a student learns a research instrument or code base. Put it to a student in plain words, as what most integrated master's graduates show, not a minimum, and ask: which research tool can you now use without supervision? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum for the master's."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.8.b6.masters
  forPractitioner: { text: "At the integrated master's typical level, graduates will master new techniques in theoretical, computational or experimental work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical integrated master's level, you will be able to pick up and master new theoretical, computing or lab techniques.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.8.b6.masters as the typical level for the integrated master's degree with honours (FHEQ level 7), above its threshold: mastering new techniques. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.8). Do not present it as the minimum for the integrated master's or apply it to the bachelor's degree. Set it beside 4.5.b2 and 4.8.b5.masters and qaa/fheq-2024/4.17.b7."
  author-agent-dialogue: "Raise it when a student must learn a method not taught in class. Put it to a student in plain words, as what most integrated master's graduates show, not a minimum, and ask: how did you learn the last new technique you needed? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum for the master's."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.8.b7.masters
  forPractitioner: { text: "At the integrated master's typical level, graduates will communicate complex ideas and give concise, accurate conclusions from their work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical integrated master's level, you will be able to explain complex scientific ideas and give short, accurate and useful conclusions from your work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.8.b7.masters as the typical level for the integrated master's degree with honours (FHEQ level 7), above its threshold: communicating complex ideas and concise conclusions. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.8). Do not present it as the minimum for the integrated master's or apply it to the bachelor's degree. Set it beside 4.6.b7 and 4.6.b4 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise it when a student writes an abstract or final talk. Put it to a student in plain words, as what most integrated master's graduates show, not a minimum, and ask: can you state your main conclusion in two sentences? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum for the master's."
- statement: qaa/physics-astronomy-and-astrophysics-2025/4.8.b8.masters
  forPractitioner: { text: "At the integrated master's typical level, graduates will understand scientific research and propose realistic ways it could progress.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical integrated master's level, you will be able to show you understand how research works and suggest realistic next steps for it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe 4.8.b8.masters as the typical level for the integrated master's degree with honours (FHEQ level 7), above its threshold: understanding research and proposing how it may progress. Cite it as (QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para 4.8). Do not present it as the minimum for the integrated master's or apply it to the bachelor's degree. Set it beside 4.8.b2.masters and 4.7.b3.masters and qaa/fheq-2024/4.17.b4.2."
  author-agent-dialogue: "Raise it when a student ends a project or plans further study. Put it to a student in plain words, as what most integrated master's graduates show, not a minimum, and ask: what would you do next if you had another year on this work? With staff, ask where the course teaches and assesses it. Avoid presenting this typical level as the minimum for the master's."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.3" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.3" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.3" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.3" }
  - { id: "fheq:4", role: "cites", locator: "D1, 2.6 (exit award)" }
  - { id: "fheq:5", role: "cites", locator: "D1, 2.6 (exit award)" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 2.6 (stated for the CertHE; the frameworks place it at fqheis:7: Part E)" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.6 (stated for the DipHE; the frameworks place it at fqheis:8: Part E)" }
  - { id: "spine:6", role: "reads-against", locator: "std:ref:uk-framework R2, R8 (inferred)" }
  - { id: "spine:7", role: "reads-against", locator: "std:ref:uk-framework R2, R8 (inferred)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.3: the standard undergraduate degree with honours); agrees with std:doc:qaa-fheq-2024-framework Table 1" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.3: the integrated master's); agrees with std:doc:qaa-fheq-2024-framework Table 1" }
  - { from: "fheq:4", to: "fqheis:8", relation: "equivalent", basis: "stated (D1, 2.6, CertHE); conflicts with std:doc:qaa-fheq-2024-framework Table 1 (CertHE at SCQF 7): Part E" }
  - { from: "fheq:5", to: "fqheis:9", relation: "equivalent", basis: "stated (D1, 2.6, DipHE); conflicts with std:doc:qaa-fheq-2024-framework Table 1 (DipHE at SCQF 8): Part E" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.22", "1.23", "1.24", "1.25", "1.26"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.24", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "3.7", "3.8"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.2", "1.20", "1.35", "1.36", "1.37", "1.38", "1.39"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.14", "1.20", "1.40", "1.41", "1.42", "1.43", "1.44", "1.45", "1.46", "3.10", "4.6"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["1.47", "1.48", "1.49", "1.50", "1.51", "3.5", "3.9"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-physics-astronomy-and-astrophysics-<previous year>-benchmarks (not yet ingested)", note: "the front matter names key changes from the previous statement without its date; the advisory group list names a 2019 minor update: Part E" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the four honours classifications, for achievement above the threshold (4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "levels 4 to 7 named in 2.3 and 2.6; the Frameworks document named in 2.3 and 4.2" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "levels 8 to 11 named in 2.3 and 2.6" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "listed in the references (section 5); the ESD theme 1.35 to 1.39" }
- { rel: "refersTo", target: "std:doc:qaa-enterprise-2018-guidance", note: "listed in the references (section 5); the enterprise theme 1.40 to 1.46" }
- { rel: "refersTo", target: "QAA Quality Code 2024 (not yet ingested)", note: "front matter; references" }
- { rel: "refersTo", target: "Institute of Physics accreditation requirements (not yet ingested)", note: "2.16" }
- { rel: "refersTo", target: "Disabled Student Commitment (not yet ingested)", note: "1.30" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2025-04"
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
- The study of natural phenomena and made systems by observation, understanding and prediction; astronomy and astrophysics share its core and apply it to astrophysical systems (D1, 1.1, 1.17).
- It explains much with little: a few key quantities, such as energy and momentum, and universal laws that hold well beyond physics (D1, 1.4).
- It works through idealised mathematical models and approximation, and models often transfer between very different systems (D1, 1.5).
- Computation and, increasingly, machine learning are central to modelling and data analysis (D1, 1.6).
- It is empirical: measurement tests theory and new instruments open new fields and spread to other sciences (D1, 1.7).
- It is hierarchical, lending itself to ordered, cumulative learning, and it feeds many neighbouring disciplines (D1, 1.3, 3.2).
- Progress rests on imagination and collaboration across cultures and sub-fields (D1, 1.8).
- Degrees share a common core with provider-specific options; the integrated master's adds research depth and extended project work (D1, 1.13, 2.1).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "named Equity, diversity and inclusion: physics open to all, a curriculum that reflects who built the discipline, safe placements and field trips and a culture all share in building (D1, 1.22 to 1.26)"
  statements: ["qaa/physics-astronomy-and-astrophysics-2025/1.22", "qaa/physics-astronomy-and-astrophysics-2025/1.23", "qaa/physics-astronomy-and-astrophysics-2025/1.24", "qaa/physics-astronomy-and-astrophysics-2025/1.25", "qaa/physics-astronomy-and-astrophysics-2025/1.26"]
- theme: theme:accessibility
  inThisSubject: "named Accessibility and the needs of disabled students: inclusive design first, then adjustments; the Disabled Student Commitment; the particular difficulty of making code, mathematics and diagrams accessible; equal access to placements (D1, 1.27 to 1.34; 3.7)"
  statements: ["qaa/physics-astronomy-and-astrophysics-2025/1.27", "qaa/physics-astronomy-and-astrophysics-2025/1.29", "qaa/physics-astronomy-and-astrophysics-2025/1.30", "qaa/physics-astronomy-and-astrophysics-2025/1.31", "qaa/physics-astronomy-and-astrophysics-2025/1.32", "qaa/physics-astronomy-and-astrophysics-2025/1.33", "qaa/physics-astronomy-and-astrophysics-2025/1.34", "qaa/physics-astronomy-and-astrophysics-2025/3.7"]
- theme: theme:esd
  inThisSubject: "physics' part in the UN goals through instruments, models and technologies for energy and climate, with examples from ice cores to LEDs; sustainability embedded through problems, projects and lectures (D1, 1.35 to 1.39); graduates appreciate sustainability issues (1.20)"
  statements: ["qaa/physics-astronomy-and-astrophysics-2025/1.20.b9"]
- theme: theme:enterprise
  inThisSubject: "enterprise, entrepreneurship and employability defined; physics' innovation fields and spinouts; careers advisers help students articulate their degree's value; enterprise topics at the typical honours level (D1, 1.40 to 1.46; 4.6)"
  statements: ["qaa/physics-astronomy-and-astrophysics-2025/1.43", "qaa/physics-astronomy-and-astrophysics-2025/1.20.b10", "qaa/physics-astronomy-and-astrophysics-2025/4.6.b9"]
- theme: theme:generative-ai
  inThisSubject: "guiding principles rather than rules: guided practice in the curriculum, assessment that recognises AI, responsible use and critique of output; AI also appears among computing skills and assessment methods (D1, 1.47 to 1.51; 3.5; 3.9)"
  statements: ["qaa/physics-astronomy-and-astrophysics-2025/1.48", "qaa/physics-astronomy-and-astrophysics-2025/1.49", "qaa/physics-astronomy-and-astrophysics-2025/1.50", "qaa/physics-astronomy-and-astrophysics-2025/1.51"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "1.15", gloss: "the fundamental areas: mechanics, relativity, quantum, electromagnetism, thermal and statistical physics, light and waves, matter" }
  - { component: "1.16", gloss: "application areas such as astrophysics, condensed matter, medical, nuclear and particle physics, optics and plasmas" }
  - { component: "1.17", gloss: "astronomy and astrophysics topics: cosmology, stars and galaxies, planetary systems, high-energy phenomena" }
  - { component: "1.19", gloss: "what all degrees cover in some measure: mathematics, computing, problem solving, estimation, experiment planning, project management, data analysis" }
practices:
  - { component: "3.2", kind: "teaching", gloss: "lectures with problem classes, flipped classes, tutorials, labs, observing, projects, team work, placements" }
  - { component: "3.4", kind: "learning", gloss: "skills through physics applications; lab work more open-ended at higher levels" }
  - { component: "3.9", kind: "assessment", gloss: "exams and tests, adaptive testing, lab books, projects, posters, vivas, critical use of AI output, reflection, peer and self-assessment" }
  - { component: "3.10", kind: "assessment", gloss: "assessment styles matched to outcomes" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.4", award: "bachelor's with honours", items: 9 }
  - { rung: "threshold", leadIn: "4.5", award: "bachelor's with honours", items: 11 }
  - { rung: "typical", leadIn: "4.6", award: "bachelor's with honours", items: 9 }
  - { rung: "threshold", leadIn: "4.7", award: "integrated master's", items: 3 }
  - { rung: "typical", leadIn: "4.8", award: "integrated master's", items: 8 }
  - { rung: "excellent", leadIn: "none", award: "none stated", items: 0 }
rungBases: "4.1 sets minimum threshold and typical standards only; 4.2 leaves achievement above threshold to Annex D. Threshold is split into subject (4.4) and generic (4.5) lists; each typical list and the master's threshold build on the rung below by an explicit \"in addition\"."
outcomeLists:
  - { leadIn: "1.20", gloss: "professional skills graduates will have developed", items: 10, award: ["honours", "integrated master's"] }
outcomes:
  - { outcome: "applying principles to problems and areas", threshold: "qaa/physics-astronomy-and-astrophysics-2025/4.4.b2", typical: "qaa/physics-astronomy-and-astrophysics-2025/4.6.b1", excellent: "none", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "solving problems with techniques", threshold: "qaa/physics-astronomy-and-astrophysics-2025/4.4.b3", typical: "qaa/physics-astronomy-and-astrophysics-2025/4.6.b2", excellent: "none", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "analysing results of investigations", threshold: "qaa/physics-astronomy-and-astrophysics-2025/4.4.b7", typical: "qaa/physics-astronomy-and-astrophysics-2025/4.6.b4", excellent: "none", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "experiments", threshold: "qaa/physics-astronomy-and-astrophysics-2025/4.4.b4", typical: "qaa/physics-astronomy-and-astrophysics-2025/4.6.b5", excellent: "none", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "computation and modelling", threshold: "qaa/physics-astronomy-and-astrophysics-2025/4.4.b5", typical: "qaa/physics-astronomy-and-astrophysics-2025/4.6.b6", excellent: "none", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "communicating science", threshold: "qaa/physics-astronomy-and-astrophysics-2025/4.4.b8", typical: "qaa/physics-astronomy-and-astrophysics-2025/4.6.b7", excellent: "none", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "extended investigation and research project", threshold: "qaa/physics-astronomy-and-astrophysics-2025/4.7.b2.masters", typical: "qaa/physics-astronomy-and-astrophysics-2025/4.8.b4.masters", excellent: "none", basis: "inferred", domain: "subject-skill", award: "integrated master's" }
  - { outcome: "research techniques and tools", threshold: "qaa/physics-astronomy-and-astrophysics-2025/4.7.b1.masters", typical: "qaa/physics-astronomy-and-astrophysics-2025/4.8.b5.masters", excellent: "none", basis: "inferred", domain: "subject-skill", award: "integrated master's" }
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
- { body: "Institute of Physics", says: "many physics, astronomy and astrophysics degrees go through its accreditation review (D1, 2.16); it is represented on the advisory group (back matter)", requirements: "not yet ingested (Part E)" }
- { body: "Equality and Human Rights Commission", says: "providers setting competence standards should follow its latest guidance (D1, 4.3)", requirements: "not yet ingested (Part E)" }
- { body: "professional, statutory and regulatory bodies (PSRBs), unnamed", says: "the statement can support their reading of academic standards; their requirements are among the reference points providers weigh and can inform competence standards (D1, front matter; 4.3)", requirements: "not-applicable-by-design" }
- { body: "Office for Students", says: "in England the statement is not a sector-recognised standard under its regulatory framework (D1, front matter)", requirements: "not-applicable-by-design" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equity, diversity and inclusion", carriedIn: ["front matter", "1.22", "1.23", "1.24", "1.25", "1.26"], statements: ["1.22", "1.23", "1.24", "1.25", "1.26"] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["front matter", "1.24", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "3.7", "3.8"], statements: ["1.27", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "3.7"] }
  - { id: "theme:esd", named: "Education for sustainable development", carriedIn: ["front matter", "1.2", "1.20", "1.35", "1.36", "1.37", "1.38", "1.39", "section 5"], statements: ["1.20.b9"] }
  - { id: "theme:enterprise", named: "Employability, enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education; 1.14: Employment, enterprise and entrepreneurship)", carriedIn: ["front matter", "1.14", "1.20", "1.40", "1.41", "1.42", "1.43", "1.44", "1.45", "1.46", "3.10", "4.6", "section 5"], statements: ["1.43", "1.20.b10", "4.6.b9"] }
  - { id: "theme:generative-ai", named: "Generative artificial intelligence", carriedIn: ["front matter", "1.47", "1.48", "1.49", "1.50", "1.51", "3.5", "3.9"], statements: ["1.48", "1.49", "1.50", "1.51"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["2.3", "2.6"] }
  - { framework: "scqf", levels: ["fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.3", "2.6"] }
bodies:
  - { body: "Institute of Physics", citedIn: ["2.16"] }
  - { body: "Equality and Human Rights Commission", citedIn: ["4.3"] }
  - { body: "PSRBs (unnamed)", citedIn: ["front matter", "4.3"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "common descriptions of the four honours classifications, for achievement above the threshold" }
  - { document: "std:doc:qaa-fheq-2024-framework", named: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["2.3", "4.2", "section 5"], role: "defines the levels of qualifications" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Education for Sustainable Development Guidance (Advance HE and QAA, 2021)", citedIn: ["section 5"], role: "reference for the ESD theme" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (QAA, 2018)", citedIn: ["section 5"], role: "reference for the enterprise theme" }
  - { document: "QAA Quality Code 2024 (not yet ingested)", named: "the Quality Code (2024 update)", citedIn: ["front matter", "section 5"], role: "companion reference point for using the statement" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "UN Sustainable Development Goals (external)", named: "United Nations Sustainable Development Goals (UN SDGs)", citedIn: ["1.35", "1.36", "1.37", "1.39"], role: "frame of the sustainability theme" }
  - { document: "Equality Act 2010 (law)", named: "the Equality Act", citedIn: ["1.22", "4.3"], role: "EDI principles; competence standards" }
  - { document: "Disabled Student Commitment (not yet ingested)", named: "the Disabled Student Commitment", citedIn: ["1.30"], role: "guidance on legislative principles for disabled students" }
  - { document: "General Data Protection Regulation (law)", named: "the General Data Protection Regulation", citedIn: ["1.51"], role: "a risk in using generative AI" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "inclusive-design", definition: "a process that anticipates every student's needs in designing, delivering and assessing the curriculum and in all processes touching students from entry to graduation, so all can take full part (D1, 1.28)", beneficiaryDefinition: "designing a course so that everyone can take part from the start, without needing to ask", scopeNote: "set beside reasonable individual adjustments (1.27)", category: "unknown", practices: ["education"] }
- { slug: "accessibility", definition: "enabling access for people with differing needs by removing needless barriers to learning and assessment (D1, 1.27)", scopeNote: "the theme heading adds the needs of disabled students", category: "unknown", practices: ["education"] }
- { slug: "enterprise", definition: "generating new ideas and turning them into practical action, drawing on creativity, innovation, adaptability, problem solving, communication and reflection (D1, 1.40)", scopeNote: "paired with entrepreneurship and employability", category: "unknown", practices: ["education"] }
- { slug: "entrepreneurship", definition: "acting on new ideas and opportunities to create cultural, social or economic value (D1, 1.40)", scopeNote: "", category: "unknown", practices: ["education"] }
- { slug: "employability", definition: "the mix of skills, knowledge and behaviours that makes a person likelier to gain work and succeed in a career (D1, 1.40)", scopeNote: "", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the minimum standard a student will have shown on being awarded the honours degree (D1, 4.1, 4.2)", scopeNote: "with the typical level above it (4.6); the integrated master's has its own threshold and typical levels (4.7, 4.8)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "inclusive-design", form: "inclusive design", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "accessibility", form: "accessibility", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "enterprise", form: "enterprise", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "entrepreneurship", form: "entrepreneurship", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "employability", form: "employability", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "minimum threshold standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "threshold level", lang: "en", partOfSpeech: "noun-phrase", termStatus: "admitted", register: "formal" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "contrasts-with", from: "inclusive-design", to: "reasonable individual adjustments", note: "1.27: inclusive design wherever possible, adjustments where necessary" }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement Physics, Astronomy and Astrophysics"
  edition: "April 2025 (fourth edition)"
  year: 2025
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/physics-astronomy-and-astrophysics-2025/physics-astronomy-and-astrophysics-2025.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: bef95f82a3eeea033684140c144425d870646ea1e7f85a65e2ee1bec1ced72da
  heldFiles: ["wkspc2601-library/txt/qaa-2025-physics-astronomy-astrophysics-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2025-physics-astronomy-astrophysics-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2025-physics-astronomy-astrophysics-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2025-physics-astronomy-astrophysics-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0091", citation: "Institute of Physics, degree accreditation framework (current edition)", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0092", citation: "Disabled Students' Commission, Disabled Student Commitment", settles: ["S7", "SB6"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0052", citation: "QAA (2024) The UK Quality Code for Higher Education", settles: ["S7", "SB6"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- S4, rungs: no excellent rung. 4.1 sets out minimum threshold and typical standards only and 4.2 sends providers to Annex D for performance above threshold; SB4 records excellent with items 0.
- S4, rungs: the threshold is two lists, subject knowledge, understanding and skills (4.4, 9) and generic skills (4.5, 11), both under one heading; Psychology has one. Rung totals: threshold 23 (20 honours, 3 integrated master's), typical 17 (9 honours, 8 integrated master's).
- S4, force: the threshold lead-ins say 'students should be able to' (4.4, 4.5); recorded as force threshold, since 4.1 and 4.3 define these lists as the minimum for the award (forceFrom 4.1, 4.3). For Abbott: keep threshold or record the lead-in's should.
- S4, force: the typical lead-ins (4.6, 4.8) carry no modal ('has demonstrated'); force will taken from 4.1 ('will have demonstrated') for 4.6 and from 4.7 ('will also have') for 4.8.
- S4, integrated master's: a separate award, not a rung (BM-BRIEF convention). 4.7 and 4.8 recorded as threshold and typical with award integrated master's, level fheq:7, ids with suffix .masters (found by text); the brief's award value is master's: integrated master's kept as the issuer's award, for P3.
- S4, rung lead-ins: a new pattern for the typical and master's lists, which each build on the rung below explicitly ('has demonstrated the capabilities and skills of the threshold honours degree level and, in addition'); 4.7's master's threshold builds on the honours typical level, not the honours threshold.
- S3, skeleton: 4.5.b11's span ran into the 'Typical level' heading; cut back by find. 4.6.b10 ('- for example, with design thinking...') is a wrapped clause of 4.6.b9, not an item; merged into 4.6.b9 by find (typical honours list has 9 items, not 10).
- S3, skeleton: the script read 4.7 as the only threshold lead-in (it names 'threshold level') and missed 4.4 and 4.5, whose lead-ins say 'on graduating ... should be able to' under the heading 'Threshold level'.
- SB4, gradeOf: every link is inferred (the lists are not paired). Plain content matches: 4.6.b1 to 4.4.b2, 4.6.b2 to 4.4.b3, 4.6.b4 to 4.4.b7, 4.6.b5 to 4.4.b4, 4.6.b7 to 4.4.b8, 4.8.b4.masters to 4.7.b2.masters, 4.8.b5.masters to 4.7.b1.masters. Weaker: 4.6.b6 (modelling) to 4.4.b5 (software for simulation). 4.6.b3, b8 and b9 and 4.8.b1 to b3 and b6 to b8 have no counterpart below.
- SB4, domains: 4.4.b8 (communicating scientific information) and its typical and master's counterparts are recorded as subject-skill because the issuer lists it under subject skills; 4.4.b9 (articulating the value of the degree) is recorded as generic-skill though it sits in the same list. For P3.
- S4, D-std-0002 (a): 1.20 is an outcome list ('graduates will have developed'), taken as 10 statements; 1.20.b7 holds a second sentence with should ('A professional physicist should be objective...') inside the item, kept as one record with the lead-in's will.
- S4, provider norms not taken as statements (template open point 5): 1.19 ('All Physics degrees cover to some extent', 7 items), 3.2 teaching methods and 3.9 assessment methods ('may include', 'typically used'), 3.10 ('will typically employ'), 1.14 and 1.45 (predictive or hedged will), 1.9 (benefits of study, descriptive).
- S4, obliging words outside the five: 'need to' (1.48 'Students need to be prepared', 3.11 'Assessment regulations need to be flexible') recorded with force describes; 'it is expected that' (2.3) and 'it would be expected that' (2.4) not taken as statements; 'are responsible for' (1.26, inside a should paragraph). For Abbott: should 'need to' read as should?
- S4, mixed force: 1.24 carries should (curriculum, provider) and will (students build EDI awareness); recorded as should, addressee both, with the will outcome in the versions. 1.51 is addressed to students (should) as well as to trainers.
- S5, crosswalk: 2.6 places the CertHE at FQHEIS level 8 and the DipHE at FQHEIS level 9; the Frameworks (std:doc:qaa-fheq-2024-framework Table 1; std:doc:qaa-fqheis-2024-framework 4.11, 4.13) place them at SCQF 7 and 8. Recorded as stated, flagged here: an issuer error to confirm at P3.
- S5, levels: spine:6 and spine:7 (std:ref:uk-framework R2, R8) are inferred reading aids for the agent instructions, not cited by the statement.
- S2 and front matter: biophysical science (100949) is inferred for the text's 'biophysics' (2.5; 1.3); geophysics (2.5) has no HECoS term under physics and is not coded. Inferred codes are held back from lookups until P3.
- S7 and S0.2: the previous statement's date is not given; the text calls this the fourth edition, and the advisory groups listed are those of 2025, 2019 (minor update), 2008 and 2002 (recall to check: the previous edition is the 2019 minor update).
- SB6, themes: 4.5.b11 ('appreciation for diversity within the group') touches EDI without naming it; not tagged. 1.14 names 'the section on Employment, enterprise and entrepreneurship', a different heading from 1.40's.
- SB6: the front matter's five cross-cutting themes include generative artificial intelligence, recorded as theme:generative-ai (BM-BRIEF convention).
- SB5: the Institute of Physics' accreditation requirements and the EHRC guidance are not yet ingested (D3). The Office for Students appears only in the front matter.
- S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are to check (template open point 3).
- S9: not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:22: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0125 (P1); built by tools/bm_build.py.
