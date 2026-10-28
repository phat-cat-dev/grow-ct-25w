---
id: std:doc:qaa-biosciences-2023-benchmarks
title: "Subject Benchmark Statement Biosciences"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100345", label: "biological sciences", basis: "stated" }
  - { scheme: "cah", code: "CAH03-01-01", label: "biosciences (non-specific)", basis: "stated" }
  - { scheme: "cah", code: "CAH03-01", label: "biosciences", basis: "stated" }
  - { scheme: "hecos", code: "100344", label: "biochemistry", basis: "stated" }
  - { scheme: "hecos", code: "100347", label: "ecology", basis: "stated" }
  - { scheme: "hecos", code: "100346", label: "biology", basis: "inferred" }
edition: "March 2023 (fifth edition)"
published: 2023-03
status: current
supersedes: "the fourth edition (2019), named in the membership section; the text lists key changes from the previous Statement"
heldText: { method: sha256-bytes, raw: aea735fda4983391d834a61aa168673e3e8e9f5a1c1760265bb436f8fdff3706, normalised: ccabc5245ed54b82ba2bed1ea42b55cc6ded8f1c7205f055ee2645ae59a6ef1f }
heldTextStan: { method: sha256-stan, raw: aea735fda4983391d834a61aa168673e3e8e9f5a1c1760265bb436f8fdff3706, normalised: 8fe656ebc1b933ce36a6c0ae8ebb532c0976d9a729b3b4a9facab29e74eec75c }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, fifth edition series with cross-cutting themes (Biosciences fifth edition, published 8 March 2023)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0090 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:36"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Biosciences (QAA, March 2023)

> Run 0090, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2023-biosciences-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in the biosciences should know and be able to do at the end of an honours degree, with added outcomes for a master's degree: two tables of outcomes, each graded at a threshold and an excellent standard, and a set of course-design expectations on inclusion, accessibility, sustainability and employability. Reach for it when designing, reviewing or describing a biosciences course or its outcomes. It is not a curriculum, not an accrediting body's requirement and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2023 as the fifth edition, the statement sets out what the biosciences study, what is distinctive about a degree in them (design, progression, flexibility, partnership, monitoring and review), the content, teaching, learning and assessment of such a degree, and benchmark standards in two tables: seventeen outcomes for an honours degree and three groups for a master's degree, each graded at threshold and excellent (no typical rung). It treats the four cross-cutting themes (equality, diversity and inclusion; accessibility; education for sustainable development; employability, enterprise and entrepreneurship), cites the FHEQ and FQHEIS levels and Annex D, the degree classification descriptions, and names the Royal Society of Biology, CIEEM and CHES as accreditors.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Biosciences"
edition: "March 2023 (fifth edition)"
dates:
  published: 2023-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of the current quality arrangements in Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2023", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate in the biosciences can be expected to know, do and understand at the end of an honours degree, with added outcomes for a master's degree, and the nature and characteristics of awards in the subject (D1, front matter; 4.1; 4.5)"
appliesTo:
  awards: ["bachelor's degrees with honours", "master's degrees (Table 2; integrated master's described, 2.14, 3.13)"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"Biosciences is the study of life, and, as such, lies at the heart of human endeavour.\" (D1, 1.1)"
statedSubjects:
  - { name: "Biosciences", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100345", label: "biological sciences" }, { scheme: "cah", code: "CAH03-01-01", label: "biosciences (non-specific)" }] }
  - { name: "Biochemistry courses", locator: "(D1, 2.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100344", label: "biochemistry" }] }
  - { name: "courses addressing ecology, the environment and/or conservation", locator: "(D1, 2.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100347", label: "ecology" }] }
  - { name: "Integrated master's degrees", locator: "(D1, 2.14; 3.13)", kind: "programme title", codes: [{ scheme: "hecos", code: "100345", label: "biological sciences" }] }
  - { name: "combined, joint or major-minor route", locator: "(D1, 2.13)", kind: "programme title", codes: [{ scheme: "hecos", code: "100345", label: "biological sciences" }] }
  - { name: "Standalone master's degree (MSc and MRes)", locator: "(D1, 2.17)", kind: "programme title", codes: [{ scheme: "hecos", code: "100345", label: "biological sciences" }] }
  - { name: "Degree Apprenticeships at Level 6 or 7", locator: "(D1, 2.15)", kind: "programme title", codes: [{ scheme: "hecos", code: "100345", label: "biological sciences" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Biosciences degree", gloss: "the study of life: vast, fast-growing, needing depth and breadth" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Biosciences degree", gloss: "graduates work across many sectors, most outside research" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Biosciences degree", gloss: "knowledge, skills and behaviours for society and careers" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Biosciences degree", gloss: "a foundation from molecules to ecosystems" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Biosciences degree", gloss: "broad understanding with specialised depth" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Biosciences degree", gloss: "contributions from other disciplines; related statements" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Biosciences degree", gloss: "degrees equip students to promote sustainability" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Biosciences degree", gloss: "opportunities to apply sustainable strategies" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Biosciences degree", gloss: "practical skills: inclusive, enquiry-led, built before the final project" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Biosciences degree", gloss: "equal chances to succeed; understanding EDI and its history" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Biosciences degree", gloss: "communicating science and its uncertainty" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Biosciences degree", gloss: "fair, authentic, valid and inclusive assessment" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive course environments and shared responsibility" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "confronting the history of bias in biology" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "diverse contributors, lived experience and ethical reflection" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "equitable access, inclusive design and adjustments" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "fully accessible curricula, fieldwork and placements" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development", gloss: "sustainability in practice; animal use and the three Rs" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development", gloss: "ESD defined; the SDGs across the curriculum" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development", gloss: "pointer to the ESD guidance; working with students" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship", gloss: "employability and entrepreneurship defined" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship", gloss: "employer links; co-created enterprise education" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship", gloss: "outside contributors, teamwork and personal development" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship", gloss: "pointer to the enterprise guidance" }
  - { number: "2.1", order: 28, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "a broad, fast-moving field facing global challenges" }
  - { number: "2.2", order: 29, componentType: area, parent: "section 2", heading: "Design", gloss: "the breadth of the subject, in six areas" }
  - { number: "2.3", order: 30, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "no course need cover every sub-discipline" }
  - { number: "2.4", order: 31, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "what honours courses provide; postgraduate options" }
  - { number: "2.5", order: 32, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "overlaps with neighbouring subjects" }
  - { number: "2.6", order: 33, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "theory and experiment; field, computational and simulated work" }
  - { number: "2.7", order: 34, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "transferable skills for the workplace" }
  - { number: "2.8", order: 35, componentType: stem, parent: "section 2", heading: "Design", gloss: "graduate employment areas" }
  - { number: "2.9", order: 36, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through levels to the course outcomes" }
  - { number: "2.10", order: 37, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression that recognises prior experience" }
  - { number: "2.11", order: 38, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "reassessment of failed modules" }
  - { number: "2.12", order: 39, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards; four-year Scottish honours" }
  - { number: "2.13", order: 40, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined routes" }
  - { number: "2.14", order: 41, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's: the extra year" }
  - { number: "2.15", order: 42, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "degree apprenticeships and the end-point assessment" }
  - { number: "2.16", order: 43, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "readiness for postgraduate study" }
  - { number: "2.17", order: 44, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "standalone master's courses" }
  - { number: "2.18", order: 45, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible length and mode of study" }
  - { number: "2.19", order: 46, componentType: practice, parent: "section 2", heading: "Flexibility", gloss: "campus-based, blended and active learning" }
  - { number: "2.20", order: 47, componentType: practice, parent: "section 2", heading: "Flexibility", gloss: "distance learning" }
  - { number: "2.21", order: 48, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "micro-credentials" }
  - { number: "2.22", order: 49, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "adaptable curricula; joint honours" }
  - { number: "2.23", order: 50, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "varied methods support inclusivity" }
  - { number: "2.24", order: 51, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership across a collaborative subject" }
  - { number: "2.25", order: 52, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "collaboration with further education" }
  - { number: "2.26", order: 53, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "shared modules, placements and study abroad" }
  - { number: "2.27", order: 54, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "work-integrated learning and placements" }
  - { number: "2.28", order: 55, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "industry projects, careers fairs and steering groups" }
  - { number: "2.29", order: 56, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "student and learned societies" }
  - { number: "2.30", order: 57, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "students as partners; the student voice" }
  - { number: "2.31", order: 58, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "course monitoring and evaluation" }
  - { number: "2.32", order: 59, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "feedback sources for review" }
  - { number: "2.33", order: 60, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "review embeds ESD and EDI" }
  - { number: "2.34", order: 61, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "performance data with expert review" }
  - { number: "2.35", order: 62, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.36", order: 63, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "the external examining system" }
  - { number: "2.37", order: 64, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accrediting bodies" }
  - { number: "3.1", order: 66, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "providers define their own content" }
  - { number: "3.2", order: 67, componentType: area, parent: "section 3", heading: "Content", gloss: "a foundation across the range of processes" }
  - { number: "3.3", order: 68, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "contested knowledge, critical thinking and uncertainty" }
  - { number: "3.4", order: 69, componentType: area, parent: "section 3", heading: "Content", gloss: "typical content: core knowledge, wider context, skills, personal development" }
  - { number: "3.5", order: 70, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "scaffolded teaching towards independence" }
  - { number: "3.6", order: 71, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "inclusive, adaptive strategies; staff development" }
  - { number: "3.7", order: 72, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "synchronous learning activities" }
  - { number: "3.8", order: 73, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "asynchronous learning activities" }
  - { number: "3.9", order: 74, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment strategy: varied, progressive, authentic" }
  - { number: "3.10", order: 75, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "principles for inclusive assessment" }
  - { number: "3.11", order: 76, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "themes for authentic assessment" }
  - { number: "3.12", order: 77, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formats for examining the themes" }
  - { number: "3.13", order: 78, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "integrated master's: unfamiliar problems and research skills" }
  - { number: "3.14", order: 79, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "qualities of good feedback" }
  - { number: "4.1", order: 81, componentType: paragraph, parent: "section 4", heading: "Benchmark standards", gloss: "the statement sets minimum standards and indicates excellence" }
  - { number: "4.2", order: 82, componentType: paragraph, parent: "section 4", heading: "Benchmark standards", gloss: "most exceed the threshold; Annex D for evidence" }
  - { number: "4.3", order: 83, componentType: paragraph, parent: "section 4", heading: "Benchmark standards", gloss: "broad, generic standards" }
  - { number: "4.4", order: 84, componentType: stem, parent: "section 4", heading: "Benchmark standards", gloss: "threshold and excellent standards defined" }
  - { number: "4.5", order: 85, componentType: paragraph, parent: "section 4", heading: "Benchmark standards", gloss: "compensation across outcomes; Tables 1 and 2" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Biosciences degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Biosciences degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1 and S2" }
  - { number: "none", heading: "Contents", kind: "other: table of contents" }
  - { number: "section headings 1 to 4", heading: "section heading lines", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for SB6 and S7" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for Biosciences", kind: "other: membership; read for the edition history" }
  - { number: "none", heading: "Fifth Edition; Published - 8 March 2023; copyright", kind: "other: imprint, read for S1 and S8" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 105 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/biosciences-2023/1.1
  locator: { number: "1.1", headingPath: ["Context and purposes of a Biosciences degree", ""] }
  span: { start: 7816, end: 8630 }
  source: "1.1 Biosciences is the study of life, and, as such, lies at the heart of human endeavour. An understanding of what ‘life’ is remains central to so many of the great questions that humans ask about the world and ourselves. The subject area of Biosciences now encompasses such a breadth and depth of knowledge and skills that it would be impossible to cover the whole subject in a lifetime of study. Biosciences continues to expand more rapidly than ever before, in a multitude of directions. To meet the challenges of such a large and rapidly expanding subject area, Biosciences degrees need to be able to produce graduates who have the knowledge and skills appropriate to current specialisms within the discipline, but to also have the breadth of knowledge and understanding to adapt to an ever- changing subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: none
  appliesTo: "degrees in the subject"
  addressee: provider
  verbs: ["produce", "adapt"]
  about: "depth and breadth for a fast-growing subject"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Because the subject is vast and grows quickly in many directions, degrees need to turn out graduates with current specialist knowledge and skills and enough breadth to adjust as the field changes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/1.3
  locator: { number: "1.3", headingPath: ["Context and purposes of a Biosciences degree", "Purposes and characteristics of a Biosciences degree"] }
  span: { start: 9201, end: 9587 }
  source: "1.3 Biosciences graduates should gain the disciplinary knowledge, practical and transferable skills and behaviours required for them to make a positive contribution to society and the environment. Biosciences graduates should be able to link their biological knowledge to real-world issues and challenges, and be prepared to succeed in a range of biological and non-biological careers.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["gain", "link", "succeed"]
  about: "knowledge, skills and behaviours for society and careers"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates should acquire subject knowledge, practical and transferable skills and behaviours that let them benefit society and the environment, connect biology to real problems and do well in biological and other careers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/1.4
  locator: { number: "1.4", headingPath: ["Context and purposes of a Biosciences degree", "Purposes and characteristics of a Biosciences degree"] }
  span: { start: 9587, end: 9857 }
  source: "1.4 Biosciences graduates should gain a foundation of knowledge and understanding in a wide range of processes and concepts across the biological kingdoms, from the fundamental molecular basis of life to an appreciation of systems biology and whole ecosystems research.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["gain"]
  about: "a foundation from molecules to ecosystems"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates should build a base of knowledge and understanding of processes and concepts across all the kingdoms of life, from the molecular basis of life up to systems biology and whole-ecosystem research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/1.5
  locator: { number: "1.5", headingPath: ["Context and purposes of a Biosciences degree", "Purposes and characteristics of a Biosciences degree"] }
  span: { start: 9857, end: 10351 }
  source: "1.5 The great diversity within the Biosciences makes it impossible to gain a detailed understanding of the entire subject area. While Biosciences graduates should have a broad understanding across the subject, they will usually specialise and develop a depth of understanding in a smaller number of sub-disciplines. This specialist knowledge and skills base will differentiate graduates in different sub-disciplines of the biosciences, which may be indicated with a more specific degree title.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["have", "specialise", "develop"]
  about: "broad understanding with specialised depth"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "No one can understand the whole subject in detail, so graduates should have a broad grasp of it and usually go deep in a few sub-disciplines, which may be reflected in a narrower degree title."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/1.6
  locator: { number: "1.6", headingPath: ["Context and purposes of a Biosciences degree", "Purposes and characteristics of a Biosciences degree"] }
  span: { start: 10351, end: 10849 }
  source: "1.6 Reflecting the breadth of the discipline, Biosciences degrees may include contributions from other disciplines. As such, Biosciences course designers may also need to refer to other Subject Benchmark Statements, including, but not limited to, Biomedical Sciences, Chemistry, Geography and ES3 (Earth Sciences, Environmental Sciences and Environmental Studies), to inform curricula. The emphasis should be on how other disciplines can make valuable contributions to the study of living systems.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course designers in the subject"
  addressee: provider
  verbs: ["include", "refer"]
  about: "contributions from other disciplines"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Degrees may draw on other disciplines, so designers may need to consult other subject statements such as those for biomedical sciences, chemistry, geography and the earth and environmental sciences; the focus should be on what those disciplines add to the study of living systems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/1.8
  locator: { number: "1.8", headingPath: ["Context and purposes of a Biosciences degree", "Purposes and characteristics of a Biosciences degree"] }
  span: { start: 11241, end: 11774 }
  source: "1.8 Biosciences degrees will provide students with opportunities to investigate, review and apply sustainable strategies based on a sound in-depth review of present sustainability\n\n4\nideas, including available technology, economic viability and subject-specific scientific robustness. There is an opportunity to reinforce the importance of sustainability but also to frame it in terms of the importance of the subject area, in terms of producing future sustainable ecosystems and a sustainable human population within these systems.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "degrees in the subject"
  addressee: provider
  verbs: ["provide", "investigate", "review", "apply"]
  about: "opportunities to apply sustainable strategies"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Degrees will give students chances to examine, review and use sustainable strategies grounded in a sound review of current ideas, including technology, cost and scientific robustness, and to see sustainability as central to future ecosystems and populations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/1.9
  locator: { number: "1.9", headingPath: ["Context and purposes of a Biosciences degree", "Purposes and characteristics of a Biosciences degree"] }
  span: { start: 11774, end: 12454 }
  source: "1.9 Biosciences graduates should gain practical skills, which may be developed in laboratory, field and/or computational contexts. Practical work should be inclusive and all students should be provided with high-quality skills training in appropriate formats that can accommodate individual needs. Practical skills development should be enquiry-driven where possible, with students exposed to the authentic research process throughout their degree. Students undertaking final-year capstone projects should have significant opportunity to develop practical and research skills before this point. Final-year projects should not be the only area in which these skills are developed.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates and their courses"
  addressee: both
  verbs: ["gain", "developed", "provided", "exposed"]
  about: "inclusive, enquiry-led practical skills before the final project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates should gain practical skills in laboratory, field or computational settings; practical work should be inclusive and adaptable to individual needs, enquiry-led where possible, and well developed before the final-year project, which should not be the only place they are built."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of a Biosciences degree", "Purposes and characteristics of a Biosciences degree"] }
  span: { start: 12454, end: 12779 }
  source: "1.10 Biosciences degrees can be structured so that all students have equivalent opportunity to succeed. Biosciences graduates should also understand the importance of equality, diversity and inclusion in both disciplinary and societal contexts, including how historical events have shaped disciplinary thinking and cultures.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["understand", "shaped"]
  about: "understanding EDI and its history in the discipline"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Degrees can be built so every student has an equal chance to succeed; graduates should also understand why equality, diversity and inclusion matter in the discipline and in society, including how history has shaped the field's thinking and cultures."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/1.11
  locator: { number: "1.11", headingPath: ["Context and purposes of a Biosciences degree", "Purposes and characteristics of a Biosciences degree"] }
  span: { start: 12779, end: 13176 }
  source: "1.11 Graduates in Biosciences need to be aware of the importance of communicating scientific information to a wide range of audiences and in a variety of formats, and students can have opportunities to develop relevant communication skills. Graduates should be able to gather and evaluate information in order to synthesise ideas and key messages, including effectively communicating uncertainty.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["gather", "evaluate", "synthesise", "communicating"]
  about: "communicating science and its uncertainty"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates need to see why communicating science to many audiences and formats matters, and courses can help them build those skills; graduates should be able to collect and judge information, draw out key messages and convey uncertainty well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of a Biosciences degree", "Purposes and characteristics of a Biosciences degree"] }
  span: { start: 13176, end: 13487 }
  source: "1.12 Assessment of students in Biosciences needs to be fair, authentic and valid. Assessments should be designed to test application of knowledge and skills, including transferable skills. Inclusivity should be considered at all stages of assessment design and implementation. Equality, diversity and inclusion\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment in the subject"
  addressee: provider
  verbs: ["designed", "test", "considered"]
  about: "fair, authentic, valid and inclusive assessment"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment needs to be fair, authentic and valid; it should test how students apply knowledge and skills, transferable ones included, and inclusivity should be considered at every stage of designing and running it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of a Biosciences degree", "Equality, diversity and inclusion"] }
  span: { start: 13487, end: 14746 }
  source: "1.13 This Subject Benchmark Statement addresses issues of inclusion throughout, and advocates intentional support for diverse student cohorts, acknowledging that equality and diversity are interdependent. Promoting equity of opportunity for all is underpinned by valuing and harnessing differences, treating everyone with dignity and respect, supporting aspirations and enabling people with diverse abilities, identities and backgrounds to succeed. Biosciences courses should be designed to create an environment that encourages openness and participation, where everyone feels respected, supported and valued and understands their own personal responsibility for equality and inclusive practice. An inclusive environment for learning anticipates and accommodates the varied requirements of students and ensures equitable access to educational opportunities. Biosciences courses should proactively raise awareness of equality, equity, diversity and inclusivity through integrated activities and discussions and should be regularly reviewed and updated in line with institutional and government guidance. Course providers, staf f and students all have a role in, and responsibility for, promoting equality and diversity and challenging biases and stereotypes.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["designed", "raise", "reviewed"]
  about: "inclusive course environments and shared responsibility"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The statement treats inclusion throughout; courses should create an open, respectful environment where everyone feels valued and knows their own part in inclusive practice, should actively raise awareness of equality, equity, diversity and inclusion, and should be reviewed regularly against institutional and government guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/1.14
  locator: { number: "1.14", headingPath: ["Context and purposes of a Biosciences degree", "Equality, diversity and inclusion"] }
  span: { start: 14746, end: 16009 }
  source: "1.14 Biosciences is a subject underpinned by objective observation. It is important, however, to recognise and proactively discuss and confront the historical factors that have influenced the biological sciences. Courses should critically engage with how the subject has contributed to and benefited from social injustice, for example presenting a balanced and informed history of the field and acknowledging that influential scientists might have benefited from and perpetuated misogyny, racism, homophobia, ableism and other prejudices. Students will be encouraged to consider that individual biases, culture and\n\n5\nsociety as a whole influence the biological sciences, including what science is done, what is considered ethical, who does that science, how data is interpreted and how biological knowledge is used. This should include critical examination of current as well as past practice and incorporation of a diverse range of underrepresented sources, including work from scientists from marginalised communities and references, case studies and learning materials representing the full range of human diversity. Consideration should be given to whether teaching materials and subject matter covered might inadvertently perpetuate biases and stereotypes.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["engage", "include", "given"]
  about: "confronting the history of bias in biology"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should engage critically with how the subject has both fed and gained from social injustice, give a balanced history, encourage students to see how bias and culture shape science, examine present as well as past practice, draw on under-represented sources and check whether materials repeat stereotypes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/1.15
  locator: { number: "1.15", headingPath: ["Context and purposes of a Biosciences degree", "Equality, diversity and inclusion"] }
  span: { start: 16009, end: 16920 }
  source: "1.15 Curricula should recognise the discoveries and contributions of biological scientists with diverse backgrounds and identities and acknowledge that different cultural backgrounds provide different insights and lead to new discoveries. Furthermore, students should have the opportunity to explore Biosciences topics that inspire them and that allow them to situate their knowledge in the light of their lived experiences or cultural backgrounds. Students should be encouraged to evaluate both the positive and negative impacts of potential applications of biological discoveries and reflect on the ways in which knowledge of Biosciences might be exploited for political, commercial or capital ends in ways that further exacerbate inequality. Curricula should facilitate the development of culturally aware graduates, with ethical and open approaches to thinking and practising the Biosciences. Accessibility\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "curricula in the subject"
  addressee: provider
  verbs: ["recognise", "acknowledge", "encouraged", "facilitate"]
  about: "diverse contributors, lived experience and ethical reflection"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Curricula should credit scientists of diverse backgrounds and the insight different cultures bring, let students explore topics that connect with their own experience, encourage them to weigh the good and harm of applying discoveries, including misuse that deepens inequality, and help produce culturally aware, ethical graduates."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/1.16
  locator: { number: "1.16", headingPath: ["Context and purposes of a Biosciences degree", "Accessibility"] }
  span: { start: 16920, end: 18275 }
  source: "1.16 Equity involves enabling access to the course of study for people who have differing individual requirements and eliminating arbitrary and unnecessary barriers to successf ul learning. Equity of access should be considered in accordance with, but not limited to, the requirements set out in the Equality Act 2010, and should encompass both physical and digital resources. Entry to Biosciences courses should be equitable and selection should be based on an individual’s potential to complete the course. Biosciences course teams must ensure that all students are offered learning and assessment opportunities that are equally accessible to them, using inclusive design wherever possible, and by means of reasonable individual adjustments where necessary. Learning and assessment experiences should be diverse, reflecting the varied nature of the subject and increasing accessibility for all students. Biosciences course teams should provide opportunities for applicants to engage with disability teams to discuss reasonable adjustments from the outset, with respect to teaching, assessment and practical work. This should include opportunities for students to provide appropriate evidence of their disability and the provision of guidance on the type of evidence required to allow consideration of adjustments to education and assessment activities.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "course teams in the subject"
  addressee: provider
  verbs: ["ensure", "considered", "provide"]
  about: "equitable access, inclusive design and reasonable adjustments"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Access should be equitable, in line with and beyond the Equality Act 2010, for physical and digital resources; entry should rest on potential; course teams must make sure all learning and assessment are equally accessible, by inclusive design and reasonable adjustments, and should let applicants talk to disability teams early."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of a Biosciences degree", "Accessibility"] }
  span: { start: 18275, end: 19033 }
  source: "1.17 Biosciences course teams must ensure that curricula, pedagogy, assessments and practical elements of courses are designed to be ful ly accessible and flexible. Equitable access to the course for all students should be proactively and flexibly considered, including fieldwork, laboratory work and placements, both at home and abroad. Further adjustments should be offered on an individual basis where required. Social capital, culture, sexuality, disability, neurodivergence and other characteristics should not prevent students from having equitable access to the entire curriculum. Teams should engage with, and respond to, feedback from a variety of sources to improve the course and remove barriers to learning. Education for Sustainable Development\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "course teams in the subject"
  addressee: provider
  verbs: ["ensure", "designed", "considered", "offered"]
  about: "fully accessible curricula, fieldwork and placements"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Course teams must make curricula, teaching, assessment and practical work fully accessible and flexible; access to fieldwork, laboratory work and placements at home and abroad should be planned ahead, with individual adjustments where needed, so no characteristic bars a student from any part of the curriculum, and feedback should be used to remove barriers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of a Biosciences degree", "Education for Sustainable Development"] }
  span: { start: 19033, end: 20641 }
  source: "1.18 Sustainability and sustainable development are key considerations in Biosciences: they are vital to managing Earth’s resources to promote the long-term well-being of the planet and all its inhabitants. It is important to note that sustainability is not solely about the environment. It is an ongoing process of addressing societal, environmental and economic concerns to create a better world, and, as such, has particular relevance to Biosciences.\n\n6\nPractical considerations might include reducing paper use, engaging with various professional recognition schemes, and discussion of the ethics and environmental impact of laboratory work (for example, replacing chemicals with sustainable alternatives, if possible, and considering glassware in place of disposable plastic), and fieldwork (for example, offering virtual opportunities and considering factors involved with international travel, including carbon footprint and promoting ethical travel). An awareness of waste reduction, bioremediation, careful use of all non-renewable resources, alternative energy sources and pollution control can be explored in the curriculum. In Biosciences it is also particularly important to consider living plant and animal resources. For example, collection of samples can endanger threatened species and the use of animals in any manner is a major ethical concern. Relevant legislation should be upheld, for example the Animals (Scientific Procedures) Act welfare standards, and courses should make every effort to adhere to the principles of replacement, reduction and refinement with respect to animal use.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["upheld", "make", "adhere"]
  about: "sustainable practice; animal use and the three Rs"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Sustainability is central to the subject and wider than the environment; practical steps include cutting waste and plastics and weighing the impact of lab and field work; living resources need care, relevant law such as the Animals (Scientific Procedures) Act should be upheld, and courses should strive to follow replacement, reduction and refinement in animal use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/1.19
  locator: { number: "1.19", headingPath: ["Context and purposes of a Biosciences degree", "Education for Sustainable Development"] }
  span: { start: 20641, end: 21324 }
  source: "1.19 The application of sustainable development in the higher education sector takes place through education for sustainable development (ESD), which is the process of creating curriculum structures and subject-relevant content to support and enact sustainable development. As defined by UNESCO in 2019, ‘ESD is holistic and transformational education which addresses learning content and outcomes, pedagogy and the learning environment. It achieves its purpose by transforming society’. An understanding of the United Nation’s Sustainable Development Goals (SDGs) is essential to this vision and, where appropriate, the SDGs should be integrated holistically across the curriculum.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "curricula in the subject"
  addressee: provider
  verbs: ["integrated"]
  about: "the SDGs across the curriculum"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Education for sustainable development builds curriculum structures and content that support sustainable development; understanding the UN Sustainable Development Goals is essential to it, and where fitting the goals should be woven through the whole curriculum."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/1.20
  locator: { number: "1.20", headingPath: ["Context and purposes of a Biosciences degree", "Education for Sustainable Development"] }
  span: { start: 21324, end: 21849 }
  source: "1.20 To support the inclusion of sustainable development within Biosciences, users should refer to the QAA and Advance HE Education for Sustainable Development Guidance\n\nto address teaching and learning for sustainable development, key competencies, learning outcomes and assessment within the curricula. Working with student representatives, higher education providers and sustainability teams might be an effective approach to facilitate curriculum structures to support ESD. Employability, enterprise and entrepreneurship\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "users of the statement"
  addressee: provider
  verbs: ["refer"]
  about: "using the ESD guidance"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Those including sustainable development in the subject should consult the QAA and Advance HE ESD guidance on teaching, competencies, outcomes and assessment; working with student representatives and sustainability teams may help."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of a Biosciences degree", "Employability, enterprise and entrepreneurship"] }
  span: { start: 22633, end: 23428 }
  source: "1.22 Developing close links with employers and involving them in curriculum and assessment design will positively enhance graduate employability. Employability and entrepreneurship focus on competencies (knowledge, skills and behaviours) plus transferable themes such as business awareness, professional ethics, health and safety and personal motivation. Enterprise and entrepreneurship education should be co-created with multiple stakeholders, for example employers, professional bodies, service users, and may cover a range of topics, such as project planning and management, financial, environmental or personal sustainability, innovation, intellectual property and commercialisation. Ideally, these topics may be explored through subject-specific applications based on real-world examples.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["co-created", "cover", "explored"]
  about: "employer links and co-created enterprise education"
  themes: [theme:enterprise]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Close links with employers in curriculum and assessment design will help employability; teaching on enterprise and entrepreneurship should be built jointly with employers, professional bodies and others and may cover planning, finance, sustainability, innovation and intellectual property, ideally through subject examples."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of a Biosciences degree", "Employability, enterprise and entrepreneurship"] }
  span: { start: 23428, end: 23986 }
  source: "1.23 Alumni, entrepreneurs and other relevant specialists, for example practitioners, may be invited to contribute to courses and the development of tasks and assessments that are\n\n7\nauthentic and support learning through self-reflection. Collaborative work by students during their courses should promote teamworking, negotiation and leadership skills. Students should take responsibility for their own personal and professional development, demonstrating a commitment to learning, self-improvement and supporting the development of others, as appropriate.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students and their courses"
  addressee: both
  verbs: ["promote", "take", "demonstrating"]
  about: "teamwork and responsibility for one's own development"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Alumni, entrepreneurs and practitioners may help shape authentic, reflective tasks; group work should foster teamwork, negotiation and leadership; students should own their personal and professional development, showing commitment to learning, self-improvement and helping others grow."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of a Biosciences degree", "Progression"] }
  span: { start: 29014, end: 29727 }
  source: "2.9 Over the course of a degree with honours (FHEQ Level 6; FQHEIS Level 10) a Biosciences student will progress from one level of study to the next, in line with the regulations and processes for each institution, and having achieved the appropriate course- level learning outcomes each year. Each level would see the attainment of knowledge, skills and experience that build towards the final achievement of meeting the overall course learning outcomes and threshold-level subject-specific and transferable skills listed in this Statement. This would include successf ul completion and the award of credit for the full range of learning and assessment, including practicals and field courses where appropriate.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours students in the subject"
  addressee: learner
  verbs: ["progress", "achieved"]
  about: "progression through levels to the course outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Across an honours degree a student will move from one level to the next under the institution's rules after achieving each year's outcomes, building towards the course outcomes and the threshold skills, including credit for all learning and assessment such as practicals and field courses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of a Biosciences degree", "Progression"] }
  span: { start: 29727, end: 30025 }
  source: "2.10 Progression should recognise the diversity of prior experience and the challenges of transition, allowing all students to aim to achieve their ambitions, irrespective of their background. Support should be provided for academic and personal development as well as for learning course content.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "progression arrangements"
  addressee: provider
  verbs: ["recognise", "provided"]
  about: "progression that recognises prior experience and transition"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Progression should take account of students' varied prior experience and the difficulty of transition, so all can aim high whatever their background, with support for personal and academic growth, not only for the subject content."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/2.13
  locator: { number: "2.13", headingPath: ["Distinctive features of a Biosciences degree", "Progression"] }
  span: { start: 30771, end: 31138 }
  source: "2.13 Undergraduates studying a combined, joint or major-minor route will achieve core elements of the subject-specific and generic skills for the subject, and will add others according to the subjects covered in joint courses. Additionally, they may explore the overlap between their two subject areas, creating further opportunities for interdisciplinary study.\n\n10\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint, combined and major-minor students"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "core skills on joint and combined routes"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students on combined, joint or major-minor routes will achieve the core subject-specific and generic skills of the subject and add others from their other subject; they may also explore where the two meet."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of a Biosciences degree", "Progression"] }
  span: { start: 31138, end: 31736 }
  source: "2.14 Integrated master’s degrees (FHEQ Level 7; FQHEIS Level 11) are available in Biosciences in the UK and comprise a four-year full-time course (five-year full-time course in Scotland). In this extra academic year of study, it is expected that students are able to demonstrate increased critical thinking, evaluation and research skills and independence. Integrated master’s degrees typically also offer a bachelor’s degree with honours as an exit award for those who have attained sufficient credit, but are not able, or do not wish, to complete the course onto which they ori ginally enrolled.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "integrated master's students"
  addressee: learner
  verbs: ["demonstrate"]
  about: "increased critical thinking, research skills and independence in the extra year"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Integrated master's degrees run four years full-time (five in Scotland); in the extra year students are expected to show sharper critical thinking, evaluation and research skills and more independence, and the course usually offers an honours exit award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/2.15
  locator: { number: "2.15", headingPath: ["Distinctive features of a Biosciences degree", "Progression"] }
  span: { start: 31736, end: 31976 }
  source: "2.15 Students undertaking Degree Apprenticeships at Level 6 or 7 will be subject to the normal rules for progression and award of the degree, but will be required to pass the end- point assessment in order to be awarded the apprenticeship.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "degree apprentices in the subject"
  addressee: learner
  verbs: ["pass", "awarded"]
  about: "the end-point assessment for apprentices"
  themes: [none]
  domain: none
  award: ["degree apprenticeship (Level 6 or 7)"]
  gradeOf: none
  paraphrase: "Degree apprentices at Level 6 or 7 follow the usual rules for progression and the degree award, but must also pass the end-point assessment to receive the apprenticeship."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/2.22
  locator: { number: "2.22", headingPath: ["Distinctive features of a Biosciences degree", "Flexibility"] }
  span: { start: 35158, end: 35943 }
  source: "2.22 The dynamism of the Biosciences discipline promotes and sustains diverse curricula. Courses need to be adaptable to respond to, and anticipate, advances in the subject, other disciplines and the needs of its graduates and employers. Providers may offer students the possibility to study a general Biosciences course or specialise within a particular interest. These may be level dependent and some modules may require pre or co-requisites. Due to the multi and interdisciplinary nature of Biosciences, many providers will offer joint- honours courses that can include Biosciences with, for example, Geography, Sustainable Development, Psychology, Mathematics or Chemistry. There may also be the opportunity to study extra credits or additional modules in different subject areas.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["respond", "anticipate"]
  about: "adaptable curricula and joint honours"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The field's pace keeps curricula varied; courses need to adapt to and anticipate advances in the subject and other fields and the needs of graduates and employers; providers may offer general or specialist routes and joint honours with other subjects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/2.25
  locator: { number: "2.25", headingPath: ["Distinctive features of a Biosciences degree", "Partnership"] }
  span: { start: 36872, end: 37252 }
  source: "2.25 Courses may be run in collaboration with further education providers, particularly in the development and delivery of foundation years or in some cases within Biomedical Sciences and Degree Apprenticeships. These collaborations will consist of a clear programme of learning, with agreed learning outcomes, delivery modes and responsibilities and quality assurance processes.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "collaborations with further education"
  addressee: provider
  verbs: ["consist"]
  about: "collaboration with further education providers"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses may be run with further education partners, especially for foundation years, some biomedical courses and degree apprenticeships; such collaborations will have a clear programme with agreed outcomes, delivery modes, responsibilities and quality processes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/2.27
  locator: { number: "2.27", headingPath: ["Distinctive features of a Biosciences degree", "Partnership"] }
  span: { start: 38414, end: 39464 }
  source: "2.27 Enhancing student employability is a fundamental outcome for Biosciences courses. Therefore, engagement with the relevant employment sectors should be extensive. Biosciences courses should have a clear work-integrated learning strategy where students have the opportunity to develop employment-focused skills and engage with employers.\n\n12\nWithin the framework, courses may include modular-based work-simulated learning, where students are provided with the opportunity to experience, practice and develop relevant technical skills. These should be informed by sector norms, current techniques and predicted advances within the discipline and offer an inclusive and accessible experience for all students on the course. Students may engage with employers through paid and/or unpaid placements of various durations during which students will be fully immersed in the workplace and experience the day-to-day routine of employment. Funding or payment should be considered to ensure that placement opportunities are inclusive and accessible to all.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["have", "informed", "considered"]
  about: "work-integrated learning and inclusive placements"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Employability is a core aim, so engagement with employment sectors should be extensive and each course should set out a plain strategy for learning integrated with work; simulated work should reflect sector practice and be inclusive, and funding should be considered so placements are open to all."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/2.28
  locator: { number: "2.28", headingPath: ["Distinctive features of a Biosciences degree", "Partnership"] }
  span: { start: 39464, end: 40394 }
  source: "2.28 Undergraduate and postgraduate taught students may also collaborate with an industrial partner for their capstone research project experience where they undertake focused research that addresses the needs of the employer and has real-world applications. Industrial and business collaborations may also be utilised for partnership delivery of Degree Apprenticeships. Most courses should offer careers fairs where students can meet employers and learn about the types of employment available and skills required. Applied areas of the Biosciences may also liaise with employers to form an industry steering group to inform and influence curriculum and pedagogic design. Each of these learning opportunities promotes professional skills development, entrepreneurship, encourages students to learn about how to organise and manage business risk and profit as an outcome, and can allow graduates to create a unique career profile.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["offer"]
  about: "industry projects and careers fairs"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Taught students may do their capstone project with an industrial partner; industry may help deliver apprenticeships; most courses should offer careers fairs; applied areas may set up industry steering groups; these build professional and entrepreneurial skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/2.30
  locator: { number: "2.30", headingPath: ["Distinctive features of a Biosciences degree", "Partnership"] }
  span: { start: 40917, end: 41777 }
  source: "2.30 Students should expect to be embraced as partners within their own courses. The student voice should play a significant role in course development, delivery, review and the overall student experience within Biosciences. Students are able to provide guidance, feedback and support for their own learning in several ways; this can be through departmental representatives or student surveys such as the National Student Survey (NSS). Furthermore, students can feed into, and collaborate with, their students’ union, and many universities offer public social media platforms to receive feedback from students and discuss current trends in the student experience. Students involved in quality review processes can be invaluable during the curriculum review and development of new courses where student steering groups may be established. Monitoring and review\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "students and their courses"
  addressee: both
  verbs: ["expect", "play"]
  about: "students as partners and the student voice"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Students should expect to be treated as partners in their courses, and their voice should count in development, delivery and review, through representatives, surveys, the union and review groups."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/2.32
  locator: { number: "2.32", headingPath: ["Distinctive features of a Biosciences degree", "Monitoring and review"] }
  span: { start: 42365, end: 42664 }
  source: "2.32 Monitoring and review should include feedback from current students, external stakeholders, such as employers and placement providers, and alumni, to influence curriculum design, content and delivery. There should also be feedback from employers and apprentices for Degree Apprenticeships.\n\n13\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "monitoring and review"
  addressee: provider
  verbs: ["include"]
  about: "feedback sources for monitoring and review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Monitoring and review should draw on feedback from current students, employers, placement providers and alumni to shape the curriculum, and from employers and apprentices for apprenticeships."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/2.34
  locator: { number: "2.34", headingPath: ["Distinctive features of a Biosciences degree", "Monitoring and review"] }
  span: { start: 42825, end: 43004 }
  source: "2.34 Evaluation of student performance data and various measures of the student experience should be integrated with expert review, including that provided by external examiners.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "monitoring and review"
  addressee: provider
  verbs: ["integrated"]
  about: "performance data with expert review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Student performance data and measures of the student experience should be combined with expert review, including external examiners' views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/2.35
  locator: { number: "2.35", headingPath: ["Distinctive features of a Biosciences degree", "Monitoring and review"] }
  span: { start: 43004, end: 43316 }
  source: "2.35 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["use", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Externality is essential to UK quality assurance: providers will use external reviewers in periodic review to bring an outside view on changes and confirm that threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.2
  locator: { number: "3.2", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 45123, end: 45488 }
  source: "3.2 Biosciences is a diverse subject, and not all aspects can be covered in equal breadth and depth within a single undergraduate or postgraduate curriculum. Biosciences students should gain a foundation in a wide range of processes from the fundamental molecular basis of life to systems biology and whole ecosystems, as appropriate to the emphasis of the course.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["gain"]
  about: "a foundation across the range of processes"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "No single curriculum can cover everything equally, but students should build a grounding in a wide range of processes, from the molecular basis of life to systems and ecosystems, to suit the course's emphasis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 45488, end: 45931 }
  source: "3.3 Biosciences courses should support students to recognise that some of what they are taught is contested and provisional, particularly in the light of continuing scientific advances. Students should be supported to appropriately challenge, question, think critically about their subject, and understand that uncertainty is a key concept in Biosciences. The historical context of the subject should be considered, as discussed in section 1.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students and their courses"
  addressee: both
  verbs: ["support", "recognise", "challenge", "question", "understand"]
  about: "contested knowledge, critical thinking and uncertainty"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students see that some of what they learn is contested and provisional; students should be helped to question and think critically about their subject and to understand uncertainty as central to it, with its history in view."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/3.4.b1
  locator: { number: "3.4.b1", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 46044, end: 46506 }
  source: "A broadly based core curriculum defined by the particular emphasis of the course, and providing knowledge and skills relevant to the wider context of Biosciences, including specialised in-depth study of selected aspects of the subject. Biosciences courses should adopt an interdisciplinary and multidisciplinary approach to advancing knowledge and understanding of the processes and mechanisms of life, from molecular to cellular, and from organism to ecosystem."
  stem: "3.4"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["adopt"]
  about: "a broad core curriculum, interdisciplinary in approach"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses generally include a broad core shaped by their emphasis, with in-depth study of selected topics; courses should take an interdisciplinary and multidisciplinary approach to the processes of life from molecule to ecosystem."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.5
  locator: { number: "3.5", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 49485, end: 50480 }
  source: "3.5 Teaching and learning strategies are designed to scaffold the acquisition of subject knowledge and skills by moving from study methods that are structured and supported towards more independent and self-directed activities. As the course advances, students become increasingly responsible for their own learning in preparation for the rest of their professional careers. Progression is enabled and reinforced by a diversity of learning and teaching methods that are matched to the expressed learning outcomes. This Subject Benchmark Statement does not aim to be directive about the methods used for a particular course but, rather, provides the basis for reflection in relation to what might be appropriate for a course, and the modules contained within that course. Integrating topics across the course is essential to ensure effective teaching and integrated learning. Teaching and learning strategies should be designed to be enriching, stimulating, challenging, effective and enjoyable.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "teaching and learning strategies"
  addressee: provider
  verbs: ["designed"]
  about: "scaffolded teaching towards independence"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching moves students from structured, supported study to independent, self-directed work, with varied methods matched to outcomes; integrating topics is essential, and strategies should be enriching, stimulating, challenging, effective and enjoyable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.6
  locator: { number: "3.6", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 50480, end: 51728 }
  source: "3.6 Learning and teaching strategies in the Biosciences are not static but adapt to changes in philosophy and technology in innovative ways that are accessible and inclusive to all. In this context, there is an expectation that all staf f who contribute to student learning - including demonstrators, and temporary and visiting lecturers, as well as permanent academic staf f - should have access to a range of educational professional development\n\n16\nopportunities. Strategies should be student-centred and utilise a range of delivery methods, as appropriate, to incorporate experiential, practical and formal academic practice. Teaching sessions may be synchronous, asynchronous, or a blend of modes. Synchronous delivery may be face-to-face, remote or a hybrid of these, to increase accessibility. Asynchronous learning is typically delivered using a range of digital tools and techniques. Live sessions may be recorded for self-directed study and consolidation of learning. Independent learning can be encouraged using pre/post-sessional student activity. It is considered good practice to use a range of different activities and reflect on how, for example, module choice by students might influence the range of activities available to them.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "teaching staff and strategies"
  addressee: provider
  verbs: ["have", "utilise"]
  about: "staff development and student-centred delivery"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching strategies adapt to new thinking and technology in accessible, inclusive ways; all staff who teach, including demonstrators and visiting lecturers, should have access to professional development, and strategies should be student-centred and use varied, blended modes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 52724, end: 53749 }
  source: "3.9 Assessment strategies are designed to recognise achievement of learning outcomes and competencies, and to discriminate between such achievement at threshold and higher levels. Strategies include a varied range of formative and summative assessment and may include self and peer-assessment. They provide evidence to employers of graduate attributes. Assessment is progressive in terms of level and content and leads to effective feedback to enable development of students' knowledge and skills, including transferable skills. In this increasingly digital world, such skills include digital literacy. Opportunities are present to exploit this and diversify how students are assessed, ensuring a range of methodologies which allow students from all backgrounds and characteristics to demonstrate their learning and development. Assessments should be authentic, with real-world application to enhance employability skills and professional development. They should also allow for reasonable adjustments to ensure inclusivity.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment strategies"
  addressee: provider
  verbs: ["allow"]
  about: "authentic, progressive and adjustable assessment"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment recognises achievement at threshold and higher levels through varied formative and summative tasks that grow with level and give useful feedback, including on digital literacy; assessments should be authentic and real-world and should allow reasonable adjustments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.10.b1
  locator: { number: "3.10.b1", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 53866, end: 53948 }
  source: "Assessment should be of, and for, learning and associated with effective feedback."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment strategies"
  addressee: provider
  verbs: ["associated"]
  about: "assessment of and for learning, with feedback"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment should serve learning as well as measure it, and come with useful feedback."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.10.b2
  locator: { number: "3.10.b2", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 53951, end: 54072 }
  source: "Assessments should be valid, reliable and consistent, and provide a means for students to demonstrate mastery of a topic."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment strategies"
  addressee: provider
  verbs: ["provide"]
  about: "valid, reliable, consistent assessment"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessments should be valid, reliable and consistent and let students show mastery."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.10.b3
  locator: { number: "3.10.b3", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54079, end: 54176 }
  source: "Assessment and feedback should explicitly take into account accessibility and EDI considerations."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment strategies"
  addressee: provider
  verbs: ["take"]
  about: "accessibility and EDI in assessment"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment and feedback should openly allow for accessibility and equality, diversity and inclusion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.10.b4
  locator: { number: "3.10.b4", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54179, end: 54277 }
  source: "Information provided about assessment and feedback should be explicit, accessible and transparent."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment strategies"
  addressee: provider
  verbs: ["provided"]
  about: "clear assessment information"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "What students are told about assessment and feedback should be clear, open and easy to access."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.10.b5
  locator: { number: "3.10.b5", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54280, end: 54391 }
  source: "Assessment and feedback should be planned to ensure students and staf f can manage their workloads effectively."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment strategies"
  addressee: provider
  verbs: ["planned", "manage"]
  about: "manageable workloads"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment and feedback should be planned so students and staff can manage their workloads."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.10.b6
  locator: { number: "3.10.b6", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54394, end: 54505 }
  source: "Assessments and feedback should be integral to the course of study and clearly relate to the learning outcomes."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment strategies"
  addressee: provider
  verbs: ["relate"]
  about: "assessment tied to outcomes"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment and feedback should be part of the course and clearly linked to the learning outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.10.b7
  locator: { number: "3.10.b7", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54508, end: 54612 }
  source: "Assessment and feedback should give the student the opportunity to validate knowledge and understanding."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment strategies"
  addressee: provider
  verbs: ["give", "validate"]
  about: "a chance to confirm knowledge"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment and feedback should let students confirm what they know and understand."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.10.b8
  locator: { number: "3.10.b8", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54615, end: 54710 }
  source: "Assessment and feedback should align with accreditation and approval requirements as necessary."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment strategies"
  addressee: provider
  verbs: ["align"]
  about: "alignment with accreditation"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment and feedback should fit accreditation and approval requirements where these apply."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.10.b9
  locator: { number: "3.10.b9", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54713, end: 54845 }
  source: "An appropriate balance of formative and summative assessments should be provided, with helpful interrelation between the two f orms."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment strategies"
  addressee: provider
  verbs: ["provided"]
  about: "balance of formative and summative"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "A suitable mix of formative and summative assessment should be provided, each supporting the other."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/3.13
  locator: { number: "3.13", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 55666, end: 55981 }
  source: "3.13 At integrated master’s level, there is a strong emphasis on requiring students to apply their knowledge of Biosciences to the solution of unfamiliar problems. Assessment of the full range of research skills is also considered crucial in determining whether master’s level learning outcomes have been achieved.\n"
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: fheq:7
  appliesTo: "integrated master's students"
  addressee: both
  verbs: ["apply", "determining"]
  about: "unfamiliar problems and research skills at integrated master's level"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At integrated master's level the emphasis falls on students applying their knowledge to unfamiliar problems, and assessing the full range of research skills is treated as crucial in judging whether master's outcomes are met."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/3.14
  locator: { number: "3.14", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 55981, end: 56424 }
  source: "3.14 Feedback should be personal, individual, understandable, empowering, manageable and developmental. It should be timely, relevant to the assessment brief and accompanied by access to interpretative support/advice. Feedback should allow students the opportunity for supportive reflection on their academic and professional development. The nature, extent and timing of feedback for each assessment task should be made clear in advance.\n\n18\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "feedback on assessment"
  addressee: provider
  verbs: ["allow", "made"]
  about: "qualities of good feedback"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Feedback should be personal, understandable, empowering, manageable, developmental, timely and tied to the brief, with support to interpret it; it should allow reflection on development, and its nature and timing should be made clear in advance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 56943, end: 57441 }
  source: "4.2 The majority of students will perform significantly better than the minimum threshold standards articulated below. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be, and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["refer"]
  about: "using Annex D to judge achievement above the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will perform well above the minimum threshold; each provider sets what counts as evidence of higher achievement and should refer to Annex D, which describes the outcome classes for honours degrees at FHEQ Level 6 and FQHEIS Level 10."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 59187, end: 59323 }
  source: "Recall basic knowledge of key biological concepts and phenomena relevant to the course, and explain these using appropriate terminology."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["recall", "explain"]
  about: "recalling and explaining key concepts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, will remember the basics of the course's key concepts and phenomena and explain them in correct terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b1.excellent
  locator: { number: "4.5.b1.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 59325, end: 59491 }
  source: "Apply a comprehensive knowledge of biological concepts and phenomena to discuss and explain essential aspects of the course, and show evidence of enquiry beyond this."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["apply", "discuss", "explain", "show"]
  about: "applying comprehensive knowledge and enquiring further"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b1, basis: stated }
  paraphrase: "At the excellent level, uses thorough knowledge of concepts and phenomena to discuss and explain the essentials of the course, and shows enquiry that goes further."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b1.outcome
  locator: { number: "4.5.b1.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 58999, end: 59186 }
  source: "Describe, discuss and understand the key biological concepts and phenomena relevant to the course (see paragraph 3.4) confidently, accurately and in detail, using appropriate terminology."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["describe", "discuss", "understand"]
  about: "key concepts and phenomena, explained with the right terms"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to explain, discuss and understand the main biological concepts and phenomena of the course with confidence, accuracy and detail, in the correct terminology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 59601, end: 59660 }
  source: "Demonstrate an awareness of the breadth of the Biosciences."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "showing awareness of breadth"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, shows awareness of how broad the subject is."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b2.excellent
  locator: { number: "4.5.b2.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 59661, end: 59767 }
  source: "Apply a broad awareness of the breadth of the Biosciences to biological phenomena, processes and problems."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["apply"]
  about: "using breadth on phenomena and problems"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b2, basis: stated }
  paraphrase: "At the excellent level, brings a wide view of the subject to bear on biological phenomena, processes and problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b2.outcome
  locator: { number: "4.5.b2.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 59492, end: 59600 }
  source: "Be aware of the full breadth of the Biosciences, from molecular to cellular, and from organism to ecosystem."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["aware"]
  about: "awareness of the full range of the subject"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know the whole span of the subject, from molecules and cells to organisms and ecosystems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 59995, end: 60216 }
  source: "Demonstrate an understanding of basic experimental design and application of methods to solve routine problems relevant to the course, with some awareness of appropriate controls, possible bias, ethics and sustainability."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["demonstrate", "solve"]
  about: "basic experimental design for routine problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, shows understanding of basic experimental design and uses methods on routine problems, with some attention to controls, bias, ethics and sustainability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b3.excellent
  locator: { number: "4.5.b3.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 60217, end: 60405 }
  source: "Devise and evaluate solutions to solve both routine and unfamiliar problems using a range of methods, including awareness of appropriate controls, possible bias, ethics and sustainability."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["devise", "evaluate", "solve", "using"]
  about: "devising and judging solutions to unfamiliar problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b3, basis: stated }
  paraphrase: "At the excellent level, creates and judges solutions to familiar and new problems with varied methods, alert to controls, bias, ethics and sustainability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b3.outcome
  locator: { number: "4.5.b3.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 59768, end: 59994 }
  source: "Apply knowledge and understanding of biological systems and methodologies to design experiments and to solve theoretical and practical problems, with awareness of appropriate controls, possible bias, ethics and sustainability."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["apply", "design", "solve"]
  about: "designing experiments and solving problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will use knowledge of biological systems and methods to plan experiments and solve theoretical and practical problems, mindful of controls, bias, ethics and sustainability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 60601, end: 60711 }
  source: "Produce and follow risk assessments for completing practical work in a saf e and reliable manner with support."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["produce", "follow"]
  about: "risk assessments with support"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, writes and follows risk assessments for practical work, with support, so it is done safely and reliably."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b4.excellent
  locator: { number: "4.5.b4.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 60713, end: 60823 }
  source: "Independently produce and apply risk assessments for completing practical work in a saf e and reliable manner."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["produce", "apply"]
  about: "risk assessments independently"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b4, basis: stated }
  paraphrase: "At the excellent level, writes and applies risk assessments without help so practical work is safe and reliable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b4.outcome
  locator: { number: "4.5.b4.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 60406, end: 60600 }
  source: "Describe, document and enact saf e working practices in terms of managing biological, chemical, laboratory or field-based risk, through knowledge-based risk assessments and practical activities."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["describe", "document", "enact"]
  about: "managing risk in practical work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will explain, record and carry out safe ways of working that manage biological, chemical, laboratory and field risks, through informed risk assessment and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 61074, end: 61239 }
  source: "Demonstrate competence in a broad range of appropriate qualitative and quantitative practical (laboratory, field or computational) techniques relevant to the course."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "competence in a range of techniques"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, shows competence across a wide set of suitable practical techniques for the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b5.excellent
  locator: { number: "4.5.b5.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 61240, end: 61473 }
  source: "Design, optimise and demonstrate competence in a broad range of appropriate qualitative and quantitative practical (laboratory, field or computational) techniques relevant to the course, with a high degree of autonomy and efficiency."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["design", "optimise", "demonstrate"]
  about: "designing and optimising techniques autonomously"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b5, basis: stated }
  paraphrase: "At the excellent level, designs, refines and competently uses a wide set of techniques, largely on their own and efficiently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b5.outcome
  locator: { number: "4.5.b5.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 60824, end: 61073 }
  source: "Select and carry out appropriate quantitative and qualitative practical (laboratory, field or computational) techniques to solve problems relevant to the course, including consideration of the theoretical basis and limitations of various techniques."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["select", "carry", "solve"]
  about: "choosing and using practical techniques"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will choose and carry out suitable quantitative and qualitative techniques in the lab, field or on computer to solve course problems, understanding their theory and limits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 61606, end: 61767 }
  source: "Apply computational techniques and tools to investigate familiar biological concepts covered in course content and report outcomes using appropriate terminology."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["apply", "investigate", "report"]
  about: "computational work on familiar concepts"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, uses computational methods on familiar course concepts and reports the results in correct terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b6.excellent
  locator: { number: "4.5.b6.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 61768, end: 61938 }
  source: "Select and apply appropriate computational techniques and tools to investigate complex biological concepts and evaluate and report outcomes using appropriate terminology."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["select", "apply", "investigate", "evaluate", "report"]
  about: "computational work on complex concepts"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b6, basis: stated }
  paraphrase: "At the excellent level, chooses and uses fitting computational methods on complex concepts and evaluates and reports the outcomes in correct terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b6.outcome
  locator: { number: "4.5.b6.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 61478, end: 61605 }
  source: "Use appropriate databases computational techniques and tools, to aid further understanding and insight of biological processes."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["use", "aid"]
  about: "databases and computational tools"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will use suitable databases and computational methods to deepen understanding of biological processes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 62020, end: 62197 }
  source: "Demonstrate knowledge of the evidence base for scientific claims, by accessing primary literature and commenting on the adequacy of the methods, data and interpretation therein."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["demonstrate", "accessing", "commenting"]
  about: "the evidence base in primary literature"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, shows knowledge of the evidence behind claims by finding primary papers and commenting on whether their methods, data and interpretation hold up."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b7.excellent
  locator: { number: "4.5.b7.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 62198, end: 62411 }
  source: "Identify and select appropriate sources of biological information, including primary literature, and appraise and evaluate the adequacy of methods, data and their interpretation with a high degree of independence."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["identify", "select", "appraise", "evaluate"]
  about: "independent appraisal of sources"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b7, basis: stated }
  paraphrase: "At the excellent level, finds and picks suitable sources, primary papers included, and judges their methods, data and interpretation largely independently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b7.outcome
  locator: { number: "4.5.b7.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 61939, end: 62019 }
  source: "Engage with literature from the Biosciences to develop insight into the subject."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["engage", "develop"]
  about: "reading the literature for insight"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will work with the subject's literature to deepen insight."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 62669, end: 62917 }
  source: "Demonstrate planning, execution and presentation of a piece of independently produced work which includes analysis or evaluation of data within a supported framework, demonstrating some evidence of time management, problem-solving and independence."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "planning and presenting supported independent work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, plans, carries out and presents a piece of own work with data analysis or evaluation inside a supported structure, with some sign of time management, problem-solving and independence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b8.excellent
  locator: { number: "4.5.b8.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 62918, end: 63182 }
  source: "Demonstrate highly independent and competent planning, execution and presentation of a piece of independently produced work which includes the analysis and critical evaluation of data, demonstrating high levels of time management, problem-solving and independence."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "highly independent project work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b8, basis: stated }
  paraphrase: "At the excellent level, plans, carries out and presents own work very independently and competently, with critical data evaluation and strong time management and problem-solving."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b8.outcome
  locator: { number: "4.5.b8.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 62412, end: 62668 }
  source: "Complete independent open-ended investigative work through a project/research- based assignment relevant to the course. This could be a laboratory or field-based project, a literature review, and/or collecting and evaluating data from a variety of sources."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["complete", "collecting", "evaluating"]
  about: "an independent, open-ended project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will carry out independent, open-ended investigation in a project or research assignment, such as lab or field work, a literature review or gathering and judging data from varied sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 63407, end: 63581 }
  source: "Identify and discuss application of Biosciences in solving current and future challenges in the world and demonstrate some understanding of the role of Bioscientists in this."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["identify", "discuss", "demonstrate"]
  about: "naming applications to world challenges"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, names and discusses uses of the subject in tackling present and future challenges, with some understanding of the scientists' role."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b9.excellent
  locator: { number: "4.5.b9.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 63582, end: 63718 }
  source: "Explain, suggest and critique ways in which Biosciences and Bioscientists can contribute to solving current and future world challenges."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["explain", "suggest", "critique", "contribute"]
  about: "critiquing contributions to world challenges"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b9, basis: stated }
  paraphrase: "At the excellent level, explains, proposes and critically assesses ways the subject and its scientists can help with present and future challenges."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b9.outcome
  locator: { number: "4.5.b9.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 63183, end: 63406 }
  source: "Appreciate the contribution of Biosciences to the innovations that characterise the modern world, and the potential of Biosciences graduates from this field to develop sustainable solutions to current and future challenges."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["appreciate", "develop"]
  about: "the subject's part in innovation and sustainable solutions"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will value how the subject has driven modern innovation and how its graduates can build sustainable answers to present and future challenges."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 63932, end: 64037 }
  source: "Identify and explain relationships between Biosciences and other subjects relevant to the course content."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["identify", "explain"]
  about: "naming links to other subjects"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, names and explains how the subject relates to other fields relevant to the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b10.excellent
  locator: { number: "4.5.b10.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 64039, end: 64206 }
  source: "Explain and evaluate the contribution of Biosciences to solving interdisciplinary challenges and the role of interdisciplinary thinking in solving scientific problems."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["explain", "evaluate"]
  about: "judging interdisciplinary contributions"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b10, basis: stated }
  paraphrase: "At the excellent level, explains and judges what the subject brings to interdisciplinary problems and how cross-disciplinary thinking helps solve scientific ones."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b10.outcome
  locator: { number: "4.5.b10.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 63720, end: 63931 }
  source: "Recognise the relationships and interfaces between Biosciences and other subjects (both scientific and outside of the sciences), such that they are able to operate effectively in a multidisciplinary environment."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["recognise", "operate"]
  about: "working across disciplines"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will see how the subject connects with other fields, scientific and otherwise, well enough to work effectively in mixed teams."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b11
  locator: { number: "4.5.b11", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 64299, end: 64406 }
  source: "Use mathematical and statistical concepts, processes and tools to solve familiar problems or evaluate data."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["use", "solve", "evaluate"]
  about: "maths and statistics on familiar problems"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, uses mathematical and statistical methods to solve familiar problems or assess data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b11.excellent
  locator: { number: "4.5.b11.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 64407, end: 64482 }
  source: "Select, use and evaluate appropriate mathematical and statistical concepts,"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["select", "use", "evaluate"]
  about: "choosing and judging quantitative methods"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b11, basis: stated }
  paraphrase: "At the excellent level, chooses, uses and judges suitable mathematical and statistical methods and tools to solve problems or assess data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b11.outcome
  locator: { number: "4.5.b11.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 64207, end: 64298 }
  source: "Deploy mathematical and statistical concepts, processes and tools, such as the manipulation"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["deploy"]
  about: "mathematical and statistical tools"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will use mathematical and statistical ideas, methods and tools, such as handling equations, graphs and statistical analysis, to solve problems or assess data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b12
  locator: { number: "4.5.b12", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 64894, end: 65136 }
  source: "Demonstrate accurate data collection, including selection of appropriate methods for analysis, interpretation of findings to test hypotheses, consideration of further lines of investigation and manipulation of data for effective presentation."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "accurate data collection and analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, collects data accurately, chooses suitable analysis, interprets findings against hypotheses, considers next steps and prepares data for clear presentation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b12.excellent
  locator: { number: "4.5.b12.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 65137, end: 65479 }
  source: "Demonstrate independent and accurate data collection, including selection of appropriate methods for analysis, interpretation of findings to test hypotheses, consideration of further lines of investigation and manipulation of data for effective presentation, with a thorough understanding of the context of the investigation within the field."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "independent data work in its field context"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b12, basis: stated }
  paraphrase: "At the excellent level, does all of this independently and accurately, with a thorough grasp of where the investigation sits in its field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b12.outcome
  locator: { number: "4.5.b12.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 64632, end: 64892 }
  source: "Collect qualitative and quantitative data from investigations relevant to the course, and analyse and interpret this data to allow testing of hypotheses, contextualising of findings, presentation of findings, and suggestions for further lines of investigation."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["collect", "analyse", "interpret"]
  about: "collecting and interpreting data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will gather qualitative and quantitative data from course investigations and analyse and interpret it to test hypotheses, place and present findings and propose next steps."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b13
  locator: { number: "4.5.b13", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 65609, end: 65702 }
  source: "Effectively participate in group and teamwork, demonstrating clear contributions to the work."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["participate", "demonstrating"]
  about: "taking part with clear contributions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, takes part effectively in group work and makes clear contributions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b13.excellent
  locator: { number: "4.5.b13.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 65703, end: 65893 }
  source: "Identify and apply effective strategies for working in a group environment and provide clear and valuable contributions to team outputs, demonstrating good teamwork and/or leadership skills."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["identify", "apply", "provide", "demonstrating"]
  about: "group strategies, teamwork and leadership"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b13, basis: stated }
  paraphrase: "At the excellent level, finds and uses good strategies for group work, adds clear value to team outputs and shows strong teamwork or leadership."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b13.outcome
  locator: { number: "4.5.b13.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 65480, end: 65608 }
  source: "Collaborate and work successf ully and inclusively in a group environment, contributing positively and flexibly to team outputs."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["collaborate", "work", "contributing"]
  about: "inclusive, effective group work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will work with others successfully and inclusively, contributing positively and flexibly to what the team produces."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b14
  locator: { number: "4.5.b14", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 66007, end: 66125 }
  source: "Communicate information, ideas, problems and solutions, verbally and/or non-verbally, with clear expression and style."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["communicate"]
  about: "clear communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, conveys information, ideas, problems and solutions clearly, in speech or other forms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b14.excellent
  locator: { number: "4.5.b14.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 66126, end: 66290 }
  source: "Communicate information, ideas, problems and solutions to an accomplished level, verbally and/or non-verbally, at a level consistently appropriate for the audience."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["communicate"]
  about: "accomplished, audience-fitted communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b14, basis: stated }
  paraphrase: "At the excellent level, communicates information, ideas, problems and solutions to an accomplished standard, always fitted to the audience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b14.outcome
  locator: { number: "4.5.b14.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 65894, end: 66006 }
  source: "Communicate effectively, selecting appropriate content, media and methods for the audience, purpose and subject."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["communicate", "selecting"]
  about: "communication fitted to audience and purpose"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will communicate well, choosing content, media and methods to suit audience, purpose and topic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b15
  locator: { number: "4.5.b15", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 66452, end: 66608 }
  source: "Describe some of the ethical issues and societal impacts of advances in the Biosciences, with some acknowledgement of the historical context of the subject."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["describe"]
  about: "describing ethical issues and impacts"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, describes some ethical issues and social effects of advances, with some recognition of the subject's history."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b15.excellent
  locator: { number: "4.5.b15.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 66609, end: 66769 }
  source: "Understand and evaluate ethical issues and the societal impact of advances in the Biosciences, with some understanding of the historical context of the subject."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["understand", "evaluate"]
  about: "evaluating ethical issues and impacts"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b15, basis: stated }
  paraphrase: "At the excellent level, understands and judges ethical issues and social effects of advances, with some understanding of the subject's history."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b15.outcome
  locator: { number: "4.5.b15.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 66291, end: 66451 }
  source: "Apply ethical awareness to working in the Biosciences, appreciate the historical context of the subject and the societal impacts of advances in the Biosciences."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["apply", "appreciate"]
  about: "ethics, history and societal impact"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will bring ethical awareness to work in the subject and understand its history and how its advances affect society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b16
  locator: { number: "4.5.b16", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 66939, end: 67165 }
  source: "Awareness of how new findings may change current understandings of various topics in the Biosciences, that many aspects of the subject are not fully understood and demonstrate some ability to stay up to date with new findings."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, threshold standard)"
  addressee: learner
  verbs: ["change", "demonstrate"]
  about: "awareness that findings change understanding"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At minimum, knows that new findings can change current understanding and that much is not yet understood, and shows some ability to keep up."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b16.excellent
  locator: { number: "4.5.b16.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 67166, end: 67333 }
  source: "Clear appreciation of the fluid nature of knowledge in the Biosciences, including an ability to incorporate new findings into previous understanding of various topics."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1, excellent standard)"
  addressee: learner
  verbs: ["incorporate"]
  about: "folding new findings into existing understanding"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b16, basis: stated }
  paraphrase: "At the excellent level, clearly grasps that knowledge is fluid and can fold new findings into existing understanding."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b16.outcome
  locator: { number: "4.5.b16.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 66770, end: 66938 }
  source: "Stay up to date with advances in the Biosciences, including aspects of sustainability, and appreciate the fluid nature of knowledge that evolves as new findings emerge."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["stay", "appreciate", "evolves"]
  about: "keeping current; knowledge as provisional"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will keep up with advances, sustainability included, and accept that knowledge shifts as new findings arrive."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b17.outcome
  locator: { number: "4.5.b17.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 67334, end: 67543 }
  source: "Act professionally, with due regard for legal, ethical and societal responsibilities, modelling good practice that promotes positive, sustainable and inclusive perceptions of the Biosciences and Bioscientists."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject (Table 1)"
  addressee: learner
  verbs: ["act", "modelling", "promotes"]
  about: "professional, ethical and inclusive conduct"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will behave professionally, respecting legal, ethical and social duties and setting an example that gives a positive, sustainable and inclusive picture of the subject and its scientists."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b18
  locator: { number: "4.5.b18", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 67901, end: 67939 }
  source: "With significant support and guidance."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the subject (Table 2 (master's), threshold standard)"
  addressee: learner
  verbs: []
  about: "master's threshold: with significant support"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At the master's threshold, achieves the row's outcomes with considerable support and guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b18.excellent
  locator: { number: "4.5.b18.excellent", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 67941, end: 67989 }
  source: "With a high degree of independence and autonomy."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:7
  appliesTo: "graduates of the subject (Table 2 (master's), excellent standard)"
  addressee: learner
  verbs: []
  about: "master's excellent: highly independent"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: { statement: qaa/biosciences-2023/4.5.b18, basis: stated }
  paraphrase: "At the master's excellent level, achieves the row's outcomes largely independently and autonomously."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b18.outcome
  locator: { number: "4.5.b18.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 67741, end: 67900 }
  source: "Develop, integrate, synthesise and apply the systematic and broad understanding of relevant and state-of-the-art biological concepts to solve complex problems."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "graduates of the subject (Table 2 (master's))"
  addressee: learner
  verbs: ["develop", "integrate", "synthesise", "apply", "solve"]
  about: "synthesising current concepts for complex problems"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should be able to build, combine, synthesise and apply a systematic, broad understanding of relevant and current biological concepts to solve complex problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b19.outcome
  locator: { number: "4.5.b19.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 67991, end: 68262 }
  source: "Interrogate and integrate diverse sources of scientific literature alongside other information sources, in order to design and develop methods for investigation and analysis, including in areas at the forefront of knowledge and outside their current specialist knowledge."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "graduates of the subject (Table 2 (master's))"
  addressee: learner
  verbs: ["interrogate", "integrate", "design", "develop"]
  about: "designing methods from wide reading, at the forefront"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should be able to question and combine varied literature and other sources to design and develop methods of investigation and analysis, including at the forefront and beyond their own specialism."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/biosciences-2023/4.5.b20.outcome
  locator: { number: "4.5.b20.outcome", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 68263, end: 68592 }
  source: "Project plan, including, as appropriate, evaluation of ethics, hazards, environmental effects, sustainability and appreciation of costs. Develop advanced experimental and investigative skills as appropriate for the project. Discuss the background, context, methods, results and potential impact of a significant research project."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "graduates of the subject (Table 2 (master's))"
  addressee: learner
  verbs: ["develop", "discuss"]
  about: "planning, conducting and discussing a significant research project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should be able to plan a project, weighing ethics, hazards, environmental effects, sustainability and cost where relevant; build advanced experimental and investigative skills for it; and discuss its background, context, methods, results and likely impact."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/biosciences-2023/1.1
  forPractitioner: { text: "Design for depth in a current specialism and enough breadth that graduates can adjust as the field moves; the text words this as a need, not with should or must.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as context worded as a need ('need to'), not one of the graded outcomes, for honours and master's courses in the subject. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.1. Do not claim that it carries the force of must or should. Set it beside 1.4 and 1.5 on breadth and depth, Table 1 row 2 (4.5.b2) and the honours descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a programme team is weighing specialist depth against breadth. Frame it for staff as the subject's case for keeping both. Ask: where does the course leave room to adapt as the field changes? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/1.3
  forPractitioner: { text: "Plan the course so graduates should leave with disciplinary knowledge, practical and transferable skills and professional behaviours, able to connect biology to real-world problems and ready for careers inside and outside biology.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should come away with subject knowledge, practical and transferable skills and ways of working that let you contribute to society and the environment, connect biology to real problems and do well in many kinds of career.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded expectation of graduates, an aim rather than a graded threshold, for the honours award at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.3. Do not claim that it is a regulatory requirement or a pass criterion. Set it beside Table 1 rows 9 and 17 (4.5.b9.outcome, 4.5.b17.outcome), the honours descriptor qaa/fheq-2024/4.15.b9.1 and spine:6."
  author-agent-dialogue: "Raise it when a student or team asks what the degree is ultimately for. To a student, say in plain words that the course aims to prepare you for many careers and to use biology on real problems; to staff, frame it as a purpose to design towards. Ask: where in your course have you linked what you know in biology to a real issue? Avoid reading the paragraph aloud and treating it as a mark scheme."
- statement: qaa/biosciences-2023/1.4
  forPractitioner: { text: "Give every graduate a grounding, at the right emphasis for the course, in processes and concepts across the kingdoms of life, from the molecular to systems and ecosystems.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should build a base of knowledge across living things, from the molecules life depends on to whole systems and ecosystems.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded expectation about breadth of knowledge, for the honours award at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.4. Do not claim that every course must teach every level of biological organisation in equal depth (3.2 qualifies it by the course emphasis). Set it beside 3.2, Table 1 row 2 (4.5.b2.outcome) and the honours descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student wonders why modules range from molecules to ecosystems. Explain to a student that this breadth is the base you build on; to staff, frame it as the foundation the course emphasis shapes. Ask: which levels of life, from molecules to ecosystems, feel least familiar to you so far? Avoid implying the student must master every area in detail."
- statement: qaa/biosciences-2023/1.5
  forPractitioner: { text: "Expect a broad understanding of the whole subject from every graduate, with depth in a smaller set of sub-disciplines; the specialism may justify a more specific award title.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should understand the subject broadly, and you will usually go deeper into a few areas of it; your specialism may show in the name of your degree.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded expectation pairing breadth with specialism, for the honours award at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.5. Do not claim that the specialism is fixed by the statement; the course decides it. Set it beside 1.4, 2.3, Table 1 row 2 (4.5.b2.outcome) and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student is choosing options or a named pathway. Say plainly that you need the broad picture and can then go deep in a few areas; for staff, frame it as balancing core and specialist modules. Ask: which areas do you want to go deeper in, and do you still have the broad picture around them? Avoid suggesting one specialism is required for the award."
- statement: qaa/biosciences-2023/1.6
  forPractitioner: { text: "Where the curriculum draws on other disciplines, consult their subject statements (for example biomedical sciences, chemistry, geography, earth and environmental sciences) and keep the focus on what each adds to the study of living systems.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded expectation on course designers, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.6. Do not claim that the other subject statements apply to a biosciences award in full. Set it beside 2.5, Table 1 row 10 (4.5.b10.outcome) and the related statements in S7."
  author-agent-dialogue: "Raise it when a team is designing modules that borrow from chemistry, geography or other subjects. Frame it for staff as a prompt to read the neighbouring subject statements. Ask: which neighbouring subject statements has the team checked, and what does each add to the study of living systems? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/1.8
  forPractitioner: { text: "Build in activities where students examine and apply sustainable strategies, judged on technology, economic viability and scientific soundness, and connect sustainability to the subject's stake in future ecosystems.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-worded commitment about what courses offer, a provider expectation and not a student outcome, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.8. Do not claim that a student must show sustainable practice to pass. Set it beside 1.7, 1.18, 1.19, Table 1 row 9 (4.5.b9.outcome) and std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise it when a team is auditing where sustainability appears in the curriculum. For staff, frame it as an opportunity the course promises to provide. Ask: in which modules do students weigh up a sustainable strategy against cost and evidence? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/1.9
  forPractitioner: { text: "Teach practical skills throughout, in laboratory, field or computational settings, inclusively and in formats that suit individual needs; make the work enquiry-led and make sure students have substantial practice before any final-year capstone project.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should build practical skills in the lab, in the field or on the computer throughout your course, in a way that suits your needs, and you should get plenty of practice before your final-year project.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded expectation on both graduates and course design, for the honours award at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.9. Do not claim that the final-year project alone can meet it. Set it beside Table 1 rows 4, 5 and 8 (4.5.b4, 4.5.b5, 4.5.b8), the honours descriptor qaa/fheq-2024/4.15.b2 and Annex D qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks how much practical work to expect, or a team plans the practical curriculum. To a student, say you should get practical experience throughout, suited to your needs; to staff, frame it as spreading practical training across the years. Ask: before your final project, where have you practised the techniques you will need? Avoid treating the capstone project as the only practical training."
- statement: qaa/biosciences-2023/1.10
  forPractitioner: { text: "Structure the course so all students have equivalent chances to succeed, and make sure graduates should grasp why equality, diversity and inclusion matter in the discipline and in society, and how history shaped the field.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should understand why equality, diversity and inclusion matter in biology and in society, and how past events have shaped the way the field thinks and works.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded expectation of graduate understanding, for the honours award at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.10. Do not claim that it is a legal duty on the student. Set it beside 1.13 to 1.15, Table 1 row 15 (4.5.b15.outcome) and Annex D qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Raise it when a student or team discusses inclusion or the history of the discipline. To a student, put it as understanding why inclusion matters in biology and how history shaped it; to staff, frame it as an expected graduate understanding. Ask: can you name one way past events shaped what biology studied or who did it? Avoid lecturing at length and treating the history as settled."
- statement: qaa/biosciences-2023/1.11
  forPractitioner: { text: "Give students chances to practise science communication for varied audiences and formats; graduates should be able to gather and weigh information, synthesise key messages and communicate uncertainty effectively.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to gather and weigh up information, pull out the main messages and explain them, including what is still uncertain, to different audiences in different formats.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded expectation of graduate communication skills, for the honours award at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.11. Do not claim that a single format or audience is enough. Set it beside Table 1 row 14 (4.5.b14 and its excellent cell), the honours descriptor qaa/fheq-2024/4.15.b8 and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student prepares a talk, poster or public-facing piece. To a student, say you should be able to explain findings and their uncertainty to different audiences; to staff, frame it as a communication outcome to assess in varied formats. Ask: how would you explain what is still uncertain in this finding to someone outside biology? Avoid reading the paragraph aloud and stressing format over clarity."
- statement: qaa/biosciences-2023/1.12
  forPractitioner: { text: "Design assessments that are fair, authentic and valid, that test the application of knowledge and skills (transferable skills too), and that build in inclusivity from design through to delivery.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded expectation on assessment design, a provider duty, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.12. Do not claim that it sets marks or grade boundaries. Set it beside 3.9, 3.10.b1 to 3.10.b9 and 3.11."
  author-agent-dialogue: "Raise it when a team is reviewing an assessment strategy. Frame it for staff as three tests for every task: fair, authentic and valid, with inclusion considered throughout. Ask: does this task test applied knowledge, and who might it disadvantage? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/1.13
  forPractitioner: { text: "Design the course for openness and participation, where everyone feels respected and knows their role in inclusive practice; build awareness of equality, equity, diversity and inclusion into activities and discussions; review and update it regularly.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation within the equality, diversity and inclusion theme, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.13. Do not claim that it imposes legal duties beyond those the provider already holds. Set it beside 1.14, 1.15, 2.33 and the shared theme record theme:edi."
  author-agent-dialogue: "Raise it when a team is reviewing the course climate or its EDI activity. Frame it for staff as designing the environment and reviewing it on a cycle. Ask: how does the course show every student their own part in inclusive practice? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/1.14
  forPractitioner: { text: "Teach a balanced history of the field, including its part in social injustice; help students see how culture and bias shape what science is done and how; use diverse sources and case studies; and audit materials for hidden bias.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation within the equality, diversity and inclusion theme, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.14. Do not claim that it asks students to adopt a particular view. Set it beside 1.10, 1.15, Table 1 row 15 (4.5.b15.outcome) and theme:edi."
  author-agent-dialogue: "Raise it when a team is revising reading lists, case studies or the history taught. Frame it for staff as a curriculum audit for balance and bias. Ask: whose work and which communities are missing from the sources the course uses? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/1.15
  forPractitioner: { text: "Credit discoveries by scientists of diverse backgrounds, offer topic choice that lets students draw on their own experience and culture, and build in reflection on the benefits, harms and possible misuse of biological knowledge.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation within the equality, diversity and inclusion theme, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.15. Do not claim that it is a graded student outcome. Set it beside 1.14, Table 1 row 15 (4.5.b15.outcome and 4.5.b15.excellent) and theme:edi."
  author-agent-dialogue: "Raise it when a team is planning topic choice or ethics content. Frame it for staff as giving students room to connect topics to their own background. Ask: where can students choose a topic that connects with their own experience? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/1.16
  forPractitioner: { text: "You must make learning and assessment equally accessible to every student, through inclusive design first and individual adjustments where needed; select on potential, cover digital as well as physical resources, and connect applicants with disability teams from the start.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a provider duty worded with must (accessibility), with should-worded parts around it, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.16. Do not claim that the statement itself creates the legal duty; it points to the Equality Act 2010. Set it beside 1.17, 3.10.b3 and theme:accessibility."
  author-agent-dialogue: "Raise it when a team is planning adjustments or admissions for disabled students. Frame it for staff as a must: inclusive design first, then individual adjustments. Ask: which parts of the course would a disabled student find hardest to reach, and what is designed in now? Avoid putting the duty to a student as theirs, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/1.17
  forPractitioner: { text: "You must design curricula, pedagogy, assessment and practicals to be fully accessible and flexible, plan access to fieldwork, labs and placements in advance, offer individual adjustments, and use feedback to remove barriers.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a provider duty worded with must (accessibility), with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.17. Do not claim that adjustments alone meet it; the text asks for accessible design. Set it beside 1.16, 2.6, 2.27 and theme:accessibility."
  author-agent-dialogue: "Raise it when a team plans fieldwork, labs or placements. Frame it for staff as a must that reaches practical and off-site work. Ask: how would a student with a mobility or sensory impairment take part in this field course? Avoid putting the duty to a student as theirs, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/1.18
  forPractitioner: { text: "Model sustainable practice in labs and fieldwork, teach waste reduction and resource care, uphold the relevant animal welfare law and apply the three Rs (replacement, reduction, refinement) wherever animals are used.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation within the education for sustainable development theme, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.18. Do not claim that the statement sets animal welfare law; it points to the Act. Set it beside 1.19, 1.20, Table 1 row 3 (4.5.b3.outcome) and theme:esd."
  author-agent-dialogue: "Raise it when a team reviews the environmental and ethical footprint of practical work. Frame it for staff as practical sustainability and the three Rs. Ask: where could this practical replace, reduce or refine animal use, or cut single-use plastic? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/1.19
  forPractitioner: { text: "Treat ESD as a curriculum design task: where appropriate, integrate the Sustainable Development Goals across the curriculum rather than in one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation within the education for sustainable development theme, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.19. Do not claim that every module must address the goals; the text says where appropriate. Set it beside 1.18, 1.20, 2.33 and std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise it when a team maps the Sustainable Development Goals onto modules. Frame it for staff as integration across the curriculum where it fits. Ask: which goals connect naturally to which modules? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/1.20
  forPractitioner: { text: "Use the ESD guidance published by QAA and Advance HE when writing sustainability teaching, outcomes and assessment, and involve student representatives and sustainability teams.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded pointer to a shared guidance document, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.20. Do not claim that the guidance is part of this statement. Set it beside std:doc:qaa-advancehe-esd-2021-guidance, 1.19 and theme:esd."
  author-agent-dialogue: "Raise it when a team asks where to find help embedding sustainability. Frame it for staff as a pointer to the ESD guidance and to student partners. Ask: has the team read the ESD guidance, and who from the student body is involved? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/1.22
  forPractitioner: { text: "Co-create enterprise and entrepreneurship education with employers, professional bodies and service users; topics may include project management, sustainability, innovation and intellectual property, taught through real subject examples.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation within the employability, enterprise and entrepreneurship theme, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.22. Do not claim that any listed topic is compulsory; the text says may. Set it beside 1.21, 1.23, 2.27, 2.28 and std:doc:qaa-enterprise-2018-guidance."
  author-agent-dialogue: "Raise it when a team plans employer involvement or enterprise content. Frame it for staff as co-creation with outside partners. Ask: which employers or bodies helped shape this module, and how? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/1.23
  forPractitioner: { text: "Use group work to build teamwork, negotiation and leadership, invite alumni and practitioners into authentic tasks, and expect students to take charge of their own development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should take charge of your own personal and professional development, keep learning and improving, and help others develop too; group work should help you build teamwork, negotiation and leadership.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded expectation on students and on group work, at the honours award, FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 1.23. Do not claim that it is graded in itself; Table 1 row 13 grades teamwork. Set it beside Table 1 row 13 (4.5.b13 and 4.5.b13.excellent), the honours descriptor qaa/fheq-2024/4.15.b9.1 and Annex D qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks who is responsible for their development, or how group work helps. To a student, say you should take ownership of your growth; to staff, frame it as designing group tasks that build leadership and negotiation. Ask: what is one thing you are actively working to improve this term, and how? Avoid presenting it as a test with marks attached."
- statement: qaa/biosciences-2023/2.9
  forPractitioner: { text: "Students will progress level by level under institutional rules, each year's outcomes building towards the course outcomes and the threshold subject-specific and transferable skills; credit covers practicals and field courses where they apply.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will move up a level each year once you have met that year's learning outcomes, building towards the outcomes for the whole course, including passing practicals and field courses where your course has them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-worded statement of how progression works, for the honours award at FHEQ Level 6 (FQHEIS Level 10); the text gives the levels itself. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 2.9. Do not claim that the statement sets the progression rules; each institution does. Set it beside 2.10, 2.11, Table 1 (4.5.b1 to 4.5.b16) and the FHEQ level records fheq:4 to fheq:6."
  author-agent-dialogue: "Raise it when a student asks how they move from one year to the next. Say plainly that you move on each year by meeting that year's outcomes under your institution's rules; for staff, frame it as the build-up to the course outcomes. Ask: do you know which outcomes you need to meet this year to move on? Avoid quoting institutional rules the statement does not set."
- statement: qaa/biosciences-2023/2.10
  forPractitioner: { text: "Plan progression and transition support around students' varied backgrounds, and support academic and personal development as well as subject learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation on progression and support, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 2.10. Do not claim that it guarantees a student any particular support. Set it beside 2.9, 1.13 and theme:edi."
  author-agent-dialogue: "Raise it when a team reviews transition or first-year support. Frame it for staff as support for development, not only for content. Ask: what support does the course give students arriving from different routes? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/2.13
  forPractitioner: { text: "Make sure joint, combined and major-minor students will achieve the core subject-specific and generic skills, adding others from the partner subject, with scope to study the overlap.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study the subject alongside another, you will still gain its core subject and general skills, add skills from your other subject, and may get to explore where the two overlap.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-worded expectation for joint and combined routes, for the honours award at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 2.13. Do not claim that joint students meet every outcome in full; the text says core elements. Set it beside Table 1 (4.5.b1 to 4.5.b17) and the partner subject's own statement."
  author-agent-dialogue: "Raise it when a joint-honours student asks what they must cover of each subject. Say plainly that you will gain the core skills of this subject and add others from your second subject; for staff, frame it as choosing the core. Ask: which core skills of this subject does your route cover, and where? Avoid implying joint students must match single-honours coverage."
- statement: qaa/biosciences-2023/2.14
  forPractitioner: { text: "In the integrated master's year, expect students to show greater critical thinking, evaluation, research skill and independence than at honours; an honours degree is usually available as an exit award.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "In the extra master's year you will be expected to show stronger critical thinking, judgement and research skills, and to work more independently.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation for the integrated master's year ('it is expected that students are able to', recorded as will), at FHEQ Level 7 (FQHEIS Level 11). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 2.14. Do not claim that it applies at honours level. Set it beside 3.13, Table 2 (4.5.b18.outcome to 4.5.b20.outcome), the master's descriptor qaa/fheq-2024/4.17.b6 and spine:7."
  author-agent-dialogue: "Raise it when a student weighs an integrated master's or is starting the final year. To a student, say the extra year asks for more independence and stronger research and critical skills; to staff, frame it as the step from Level 6 to Level 7. Ask: where in your work this year are you deciding things on your own that a tutor used to decide? Avoid treating the master's expectations as the honours minimum."
- statement: qaa/biosciences-2023/2.15
  forPractitioner: { text: "Tell apprentices that the degree follows normal rules but the apprenticeship itself needs a pass in the end-point assessment.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you are a degree apprentice, the usual rules apply to your degree, but you must also pass the end-point assessment to complete the apprenticeship.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a requirement ('will be required', recorded as must) for degree apprentices, at Level 6 or 7 as the text states. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 2.15. Do not claim that it adds conditions to the degree award itself. Set it beside 2.9, 2.25, 2.32 and the shared document on apprenticeships listed in Part E."
  author-agent-dialogue: "Raise it when a degree apprentice asks what they need to finish. Say plainly that you must pass the end-point assessment as well as the degree; for staff, frame it as two separate gates. Ask: do you know when and how your end-point assessment happens? Avoid mixing up the degree award and the apprenticeship award."
- statement: qaa/biosciences-2023/2.22
  forPractitioner: { text: "Keep the curriculum under review so it adapts to, and anticipates, advances and the needs of graduates and employers; the text words this as a need.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as context worded as a need ('need to'), recorded as describes, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 2.22. Do not claim that it carries must or should. Set it beside 1.1, 2.31 and 2.32."
  author-agent-dialogue: "Raise it when a team plans a curriculum refresh. Frame it for staff as keeping pace with the field and with employers. Ask: which recent advances in the field are not yet in the course? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/2.25
  forPractitioner: { text: "When working with a further education partner, agree and write down the programme, outcomes, delivery, responsibilities and quality assurance.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-worded provider expectation on partnerships, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 2.25. Do not claim that it governs every partnership the provider has. Set it beside 2.24, 2.26 and 2.15."
  author-agent-dialogue: "Raise it when a team sets up or reviews a further education partnership. Frame it for staff as a checklist for the partnership agreement. Ask: are outcomes, responsibilities and quality processes agreed in writing? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/2.27
  forPractitioner: { text: "Write a work-integrated learning strategy, give students contact with employers, keep simulated work current with sector practice and accessible, and consider funding so all students can take placements.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation within the employability theme, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 2.27. Do not claim that placements are compulsory; the text says may. Set it beside 1.22, 2.28, theme:enterprise and theme:accessibility."
  author-agent-dialogue: "Raise it when a team reviews employability or placement access. Frame it for staff as a strategy question and an equity question. Ask: which students currently cannot take a placement, and why? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/2.28
  forPractitioner: { text: "Offer careers fairs, consider industry-partnered capstone projects and, in applied areas, an industry steering group for the curriculum.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation within the enterprise theme, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 2.28. Do not claim that an industry project is required. Set it beside 2.27, 1.22 and theme:enterprise."
  author-agent-dialogue: "Raise it when a team plans careers provision. Frame it for staff as the careers fair expectation plus optional industry links. Ask: when did students last meet employers through the course? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/2.30
  forPractitioner: { text: "Treat students as partners: give the student voice a real part in development, delivery and review, through representatives, surveys, the union and steering groups.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should expect to be treated as a partner in your course: your views should shape how it is developed, taught and reviewed, through representatives, surveys and your students' union.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded expectation on partnership with students, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 2.30. Do not claim that it is a learning outcome. Set it beside 2.32 and 2.31."
  author-agent-dialogue: "Raise it when a student wonders whether their feedback matters, or a team plans student involvement. To a student, say you should expect your views to count and name the routes; to staff, frame it as partnership in review. Ask: how have you given feedback on your course so far, and did you see anything change? Avoid promising a student specific changes."
- statement: qaa/biosciences-2023/2.32
  forPractitioner: { text: "Gather feedback from students, employers, placement hosts and alumni (and apprentices) for every review.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation on review, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 2.32. Do not claim that it sets a review cycle. Set it beside 2.31, 2.34 and 2.35."
  author-agent-dialogue: "Raise it when a team prepares for periodic review. Frame it for staff as the list of voices a review hears. Ask: which of these groups did the last review hear from? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/2.34
  forPractitioner: { text: "Read student performance and experience data together with external examiners' and other expert views.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation on review, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 2.34. Do not claim that it names which data to use. Set it beside 2.32, 2.35 and 2.36."
  author-agent-dialogue: "Raise it when a team analyses outcomes data. Frame it for staff as reading data and expert judgement side by side. Ask: what did the external examiner say about the patterns the data show? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/2.35
  forPractitioner: { text: "Involve external reviewers in periodic review to test proposed changes, threshold standards and subject content.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a will-worded provider expectation on externality, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 2.35. Do not claim that the statement appoints reviewers. Set it beside 2.34, 2.36 and Table 1 (the threshold cells)."
  author-agent-dialogue: "Raise it when a team plans a periodic review panel. Frame it for staff as the external check on threshold standards. Ask: who is the external voice on the next review, and what will they test? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.2
  forPractitioner: { text: "Give every student a grounding across processes from the molecular to the ecosystem, weighted to the course's emphasis.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should build a grounding in many biological processes, from molecules to whole ecosystems, weighted to what your course focuses on.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded expectation about breadth of knowledge, for the honours award at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.2. Do not claim that every area must be taught in equal depth. Set it beside 1.4, Table 1 row 2 (4.5.b2) and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student asks why the course covers such different scales of biology. To a student, say you should have a grounding across the scales, weighted to your course; to staff, frame it as breadth set by emphasis. Ask: which scale of biology do you find hardest to connect to your specialism? Avoid implying equal depth everywhere is required."
- statement: qaa/biosciences-2023/3.3
  forPractitioner: { text: "Teach that some knowledge is contested and provisional, support students to question it critically, treat uncertainty as a core idea and bring in the subject's history.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should come to see that some of what you are taught is still debated or may change, and you should be supported to question it, think critically and treat uncertainty as a normal part of biology.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded expectation on courses and students about the provisional nature of knowledge, for the honours award at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.3. Do not claim that it licenses rejecting established findings. Set it beside Table 1 row 16 (4.5.b16 and its outcome), 1.11, the honours descriptor qaa/fheq-2024/4.15.b4 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a student is unsettled that textbook claims change, or a team plans critical-thinking teaching. To a student, say that some knowledge is open to question and that weighing it is part of the subject; to staff, frame it as teaching uncertainty. Ask: what is one thing you were taught that is still debated, and what evidence would settle it? Avoid implying all knowledge is equally uncertain."
- statement: qaa/biosciences-2023/3.4.b1
  forPractitioner: { text: "Build a broad core curriculum set by the course emphasis, with specialised depth in places, and teach it across disciplines from molecular to ecosystem scales.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation inside the typical-content list, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.4 (first item). Do not claim that the other content items carry should; they are plain description. Set it beside 1.4, 3.2 and Table 1 row 2 (4.5.b2.outcome)."
  author-agent-dialogue: "Raise it when a team designs the core curriculum. Frame it for staff as a core set by emphasis, taught across disciplines. Ask: where does the core cross from molecular to ecosystem scale? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.5
  forPractitioner: { text: "Scaffold learning from supported to independent study, match methods to outcomes, integrate topics across the course and aim for teaching that is enriching, stimulating, challenging, effective and enjoyable.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation on teaching strategy, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.5. Do not claim that it prescribes methods; the text says it does not. Set it beside 3.6, 3.7, 3.8 and qaa/fheq-2024/4.15.b5 on managing one's own learning."
  author-agent-dialogue: "Raise it when a team plans how independence grows across the years. Frame it for staff as scaffolding towards self-direction. Ask: where does the course hand responsibility for learning over to students? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.6
  forPractitioner: { text: "Give everyone who teaches, demonstrators and visiting staff included, access to professional development, and use student-centred strategies across synchronous and asynchronous modes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation on teaching staff and delivery, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.6. Do not claim that it sets a staff qualification. Set it beside 3.5, 3.7, 3.8 and theme:accessibility."
  author-agent-dialogue: "Raise it when a team reviews staff development or delivery modes. Frame it for staff as development for all who teach. Ask: do demonstrators and visiting lecturers have access to development? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.9
  forPractitioner: { text: "Use varied, progressive formative and summative assessment that separates threshold from higher achievement, make tasks authentic, and allow reasonable adjustments.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation on assessment strategy, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.9. Do not claim that it sets grade boundaries. Set it beside 3.10.b1 to 3.10.b9, 3.11, Table 1 (threshold and excellent cells) and Annex D qaa/fheq-2024/annex-d/summary/r1/3rd."
  author-agent-dialogue: "Raise it when a team reviews an assessment strategy. Frame it for staff as authentic tasks that can tell threshold from higher work. Ask: can this assessment tell threshold work from excellent work? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.10.b1
  forPractitioner: { text: "Make each assessment both a measure of and a means of learning, with feedback attached.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as one of nine should-worded principles for an inclusive, accessible assessment strategy (assessment of and for learning, with feedback), with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.10 (item 1). Do not claim that the principle is a student outcome. Set it beside 1.12, 3.9 and the other 3.10 principles."
  author-agent-dialogue: "Raise it when a team checks an assessment against the principle of assessment of and for learning, with feedback. Frame it for staff as one test in a checklist of nine. Ask: how does this task meet the principle of assessment of and for learning, with feedback? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.10.b2
  forPractitioner: { text: "Check each assessment is valid, reliable and consistent and lets students show mastery of the topic.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as one of nine should-worded principles for an inclusive, accessible assessment strategy (valid, reliable, consistent assessment), with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.10 (item 2). Do not claim that the principle is a student outcome. Set it beside 1.12, 3.9 and the other 3.10 principles."
  author-agent-dialogue: "Raise it when a team checks an assessment against the principle of valid, reliable, consistent assessment. Frame it for staff as one test in a checklist of nine. Ask: how does this task meet the principle of valid, reliable, consistent assessment? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.10.b3
  forPractitioner: { text: "Build accessibility and EDI into assessment and feedback from the start.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as one of nine should-worded principles for an inclusive, accessible assessment strategy (accessibility and EDI in assessment), with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.10 (item 3). Do not claim that the principle is a student outcome. Set it beside 1.12, 3.9 and the other 3.10 principles."
  author-agent-dialogue: "Raise it when a team checks an assessment against the principle of accessibility and EDI in assessment. Frame it for staff as one test in a checklist of nine. Ask: how does this task meet the principle of accessibility and EDI in assessment? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.10.b4
  forPractitioner: { text: "Publish clear, accessible, transparent information about every assessment and its feedback.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as one of nine should-worded principles for an inclusive, accessible assessment strategy (clear assessment information), with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.10 (item 4). Do not claim that the principle is a student outcome. Set it beside 1.12, 3.9 and the other 3.10 principles."
  author-agent-dialogue: "Raise it when a team checks an assessment against the principle of clear assessment information. Frame it for staff as one test in a checklist of nine. Ask: how does this task meet the principle of clear assessment information? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.10.b5
  forPractitioner: { text: "Plan assessment and feedback so workloads stay manageable for students and staff.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as one of nine should-worded principles for an inclusive, accessible assessment strategy (manageable workloads), with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.10 (item 5). Do not claim that the principle is a student outcome. Set it beside 1.12, 3.9 and the other 3.10 principles."
  author-agent-dialogue: "Raise it when a team checks an assessment against the principle of manageable workloads. Frame it for staff as one test in a checklist of nine. Ask: how does this task meet the principle of manageable workloads? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.10.b6
  forPractitioner: { text: "Make assessment integral to the course and map each task to learning outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as one of nine should-worded principles for an inclusive, accessible assessment strategy (assessment tied to outcomes), with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.10 (item 6). Do not claim that the principle is a student outcome. Set it beside 1.12, 3.9 and the other 3.10 principles."
  author-agent-dialogue: "Raise it when a team checks an assessment against the principle of assessment tied to outcomes. Frame it for staff as one test in a checklist of nine. Ask: how does this task meet the principle of assessment tied to outcomes? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.10.b7
  forPractitioner: { text: "Give students chances, through assessment and feedback, to confirm what they know and understand.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as one of nine should-worded principles for an inclusive, accessible assessment strategy (a chance to confirm knowledge), with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.10 (item 7). Do not claim that the principle is a student outcome. Set it beside 1.12, 3.9 and the other 3.10 principles."
  author-agent-dialogue: "Raise it when a team checks an assessment against the principle of a chance to confirm knowledge. Frame it for staff as one test in a checklist of nine. Ask: how does this task meet the principle of a chance to confirm knowledge? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.10.b8
  forPractitioner: { text: "Align assessment and feedback with accreditation and approval requirements where relevant.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as one of nine should-worded principles for an inclusive, accessible assessment strategy (alignment with accreditation), with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.10 (item 8). Do not claim that the principle is a student outcome. Set it beside 1.12, 3.9 and the other 3.10 principles."
  author-agent-dialogue: "Raise it when a team checks an assessment against the principle of alignment with accreditation. Frame it for staff as one test in a checklist of nine. Ask: how does this task meet the principle of alignment with accreditation? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.10.b9
  forPractitioner: { text: "Balance formative and summative assessment and link the two.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as one of nine should-worded principles for an inclusive, accessible assessment strategy (balance of formative and summative), with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.10 (item 9). Do not claim that the principle is a student outcome. Set it beside 1.12, 3.9 and the other 3.10 principles."
  author-agent-dialogue: "Raise it when a team checks an assessment against the principle of balance of formative and summative. Frame it for staff as one test in a checklist of nine. Ask: how does this task meet the principle of balance of formative and summative? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/3.13
  forPractitioner: { text: "Set unfamiliar problems in the master's year and assess the whole range of research skills when deciding whether master's outcomes are met.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At master's level you will be asked to use what you know on problems you have not met before, and your full range of research skills will be assessed.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as an emphasis worded with 'requiring' and 'crucial', recorded as describes, at FHEQ Level 7 (FQHEIS Level 11). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.13. Do not claim that it is worded with must. Set it beside 2.14, Table 2 (4.5.b18.outcome to 4.5.b20.outcome) and the master's descriptor qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise it when a master's student asks how the final year is assessed. To a student, say you will face unfamiliar problems and be assessed on your whole set of research skills; to staff, frame it as the assessment emphasis at Level 7. Ask: when did you last tackle a problem you had not been shown how to solve? Avoid presenting it as a hard rule with must force."
- statement: qaa/biosciences-2023/3.14
  forPractitioner: { text: "Give feedback that is personal, timely, tied to the brief and developmental, offer help in reading it, and state in advance what feedback each task will get and when.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation on feedback, with no level of its own. Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 3.14. Do not claim that it sets turnaround times. Set it beside 3.10.b1, 3.10.b4 and 3.9."
  author-agent-dialogue: "Raise it when a team reviews feedback practice. Frame it for staff as what good feedback does and when students hear about it. Ask: do students know before each task what feedback they will get and when? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/4.2
  forPractitioner: { text: "When deciding what evidence shows achievement above the threshold, refer to Annex D, the outcome classification descriptions for honours degrees (now in the 2024 Frameworks).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-worded provider expectation pointing to Annex D, for the honours award at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.2. Do not claim that the statement itself sets the classification bands. Set it beside std:doc:qaa-fheq-2024-framework Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd to qaa/fheq-2024/annex-d/summary/r1/1st) and Table 1 (4.5.b1 to 4.5.b17)."
  author-agent-dialogue: "Raise it when a team calibrates classification against the threshold. Frame it for staff as reading the threshold here with the Annex D bands. Ask: how does the team tell a 2.1 from a 2.2 on this outcome, using Annex D? Avoid putting it to a student as something they must do, and reading the paragraph aloud."
- statement: qaa/biosciences-2023/4.5.b1
  forPractitioner: { text: "At threshold, graduates recall the basics of the key concepts and phenomena and explain them using correct terms.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will remember the basics of the key ideas in your course and explain them using the right terms.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for core biological concepts: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b1.outcome, the excellent cell 4.5.b1.excellent, the descriptor qaa/fheq-2024/4.15.b1 and the Annex D third-class band qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in core biological concepts, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: can you explain the basics of this concept in the right terms? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b1.excellent
  forPractitioner: { text: "At the excellent level, graduates apply thorough knowledge to explain the essentials and show they have read and enquired beyond the course.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will use a thorough knowledge of biology to discuss the essentials of your course and show you have explored beyond it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for core biological concepts: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b1, which it grades upward, the descriptor qaa/fheq-2024/4.15.b1 and the Annex D first-class band qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in core biological concepts looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: where have you followed a topic beyond what the course taught? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b1.outcome
  forPractitioner: { text: "Graduates will describe and discuss the course's key concepts and phenomena confidently, accurately and in detail, using correct terms.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to explain and discuss the main ideas and processes of your course clearly, accurately and in detail, using the right scientific terms.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for core biological concepts: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b1 and 4.5.b1.excellent, the descriptor qaa/fheq-2024/4.15.b1 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in core biological concepts. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: which key concepts of your course could you explain to a classmate without notes? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b2
  forPractitioner: { text: "At threshold, graduates show awareness of the subject's breadth.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will show that you know how broad the subject is.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for the breadth of the subject: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b2.outcome, the excellent cell 4.5.b2.excellent, the descriptor qaa/fheq-2024/4.15.b1 and the Annex D third-class band qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in the breadth of the subject, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: which areas of the subject can you name outside your own? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b2.excellent
  forPractitioner: { text: "At the excellent level, graduates use their wide view of the subject on phenomena, processes and problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will use your wide view of the subject to make sense of biological processes and problems.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for the breadth of the subject: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b2, which it grades upward, the descriptor qaa/fheq-2024/4.15.b1 and the Annex D first-class band qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in the breadth of the subject looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: how does knowledge from another scale help you with a problem in your area? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b2.outcome
  forPractitioner: { text: "Graduates will be aware of the subject's full span, from molecules and cells to organisms and ecosystems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will know how far the subject reaches, from molecules and cells to whole organisms and ecosystems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for the breadth of the subject: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b2 and 4.5.b2.excellent, the descriptor qaa/fheq-2024/4.15.b1 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in the breadth of the subject. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: can you place your specialism on the map from molecules to ecosystems? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b3
  forPractitioner: { text: "At threshold, graduates understand basic design and solve routine problems, with some attention to controls, bias, ethics and sustainability.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will understand basic experimental design and use methods on routine problems, thinking a little about controls, bias, ethics and sustainability.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for experimental design and problem-solving: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b3.outcome, the excellent cell 4.5.b3.excellent, the descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D third-class band qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in experimental design and problem-solving, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: can you explain the controls in a routine practical you have done? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b3.excellent
  forPractitioner: { text: "At the excellent level, graduates devise and evaluate solutions to routine and unfamiliar problems by several methods, alert to controls, bias, ethics and sustainability.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will work out and judge solutions to new as well as familiar problems, using several methods and thinking about controls, bias, ethics and sustainability.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for experimental design and problem-solving: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b3, which it grades upward, the descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D first-class band qaa/fheq-2024/annex-d/cognitive/r3/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in experimental design and problem-solving looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: how would you tackle a problem you have not seen before? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b3.outcome
  forPractitioner: { text: "Graduates will design experiments and solve problems using their understanding of systems and methods, attending to controls, bias, ethics and sustainability.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to design experiments and solve problems using what you know about living systems and methods, thinking about controls, bias, ethics and sustainability.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for experimental design and problem-solving: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b3 and 4.5.b3.excellent, the descriptor qaa/fheq-2024/4.15.b3.1 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in experimental design and problem-solving. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: in your last experiment, what controls did you choose and why? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b4
  forPractitioner: { text: "At threshold, graduates write and follow risk assessments with support so practical work is safe and reliable.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will write and follow risk assessments for practical work, with support, so you work safely and reliably.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for safe working and risk assessment: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b4.outcome, the excellent cell 4.5.b4.excellent, the descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D third-class band qaa/fheq-2024/annex-d/professional/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in safe working and risk assessment, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: can you complete a risk assessment for this practical with your supervisor? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b4.excellent
  forPractitioner: { text: "At the excellent level, graduates write and apply risk assessments independently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will write and apply your own risk assessments without help.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for safe working and risk assessment: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b4, which it grades upward, the descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D first-class band qaa/fheq-2024/annex-d/professional/r2/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in safe working and risk assessment looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: could you write this risk assessment on your own and defend each control? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b4.outcome
  forPractitioner: { text: "Graduates will describe, record and follow safe practice for biological, chemical, lab and field risks, using informed risk assessments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to explain, write down and follow safe ways of working with biological, chemical, lab and field risks, using proper risk assessments.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for safe working and risk assessment: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b4 and 4.5.b4.excellent, the descriptor qaa/fheq-2024/4.15.b9.1 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in safe working and risk assessment. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: what are the main risks in the practical you are planning, and how will you manage them? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b5
  forPractitioner: { text: "At threshold, graduates show competence in a broad range of suitable lab, field or computational techniques.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will show you can use a wide range of practical techniques suited to your course.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for practical techniques: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b5.outcome, the excellent cell 4.5.b5.excellent, the descriptor qaa/fheq-2024/4.15.b2 and the Annex D third-class band qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in practical techniques, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: which techniques can you run competently now? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b5.excellent
  forPractitioner: { text: "At the excellent level, graduates design and optimise techniques and use them competently, autonomously and efficiently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will design and improve techniques as well as use them, working efficiently and largely on your own.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for practical techniques: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b5, which it grades upward, the descriptor qaa/fheq-2024/4.15.b2 and the Annex D first-class band qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in practical techniques looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: have you ever adapted or improved a method yourself? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b5.outcome
  forPractitioner: { text: "Graduates will select and use fitting lab, field or computational techniques, quantitative and qualitative, aware of their theoretical basis and limits.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to choose and use the right practical techniques in the lab, in the field or on a computer, knowing how they work and where they fall short.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for practical techniques: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b5 and 4.5.b5.excellent, the descriptor qaa/fheq-2024/4.15.b2 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in practical techniques. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: which techniques have you used, and what are their limits? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b6
  forPractitioner: { text: "At threshold, graduates apply computational tools to familiar concepts and report results in correct terms.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will use computer tools to look into familiar topics from your course and report what you find in the right terms.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for computational tools and databases: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b6.outcome, the excellent cell 4.5.b6.excellent, the descriptor qaa/fheq-2024/4.15.b2 and the Annex D third-class band qaa/fheq-2024/annex-d/practical/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in computational tools and databases, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: can you run a familiar analysis and report it in the right terms? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b6.excellent
  forPractitioner: { text: "At the excellent level, graduates choose computational tools for complex concepts, then evaluate and report results in correct terms.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will choose the right computer tools for complex questions, judge the results and report them clearly.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for computational tools and databases: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b6, which it grades upward, the descriptor qaa/fheq-2024/4.15.b2 and the Annex D first-class band qaa/fheq-2024/annex-d/practical/r3/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in computational tools and databases looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: how did you choose the tool for a complex question? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b6.outcome
  forPractitioner: { text: "Graduates will use suitable databases and computational tools to gain insight into biological processes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to use databases and computer tools to understand biological processes better.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for computational tools and databases: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b6 and 4.5.b6.excellent, the descriptor qaa/fheq-2024/4.15.b2 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in computational tools and databases. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: which databases or tools have you used, and what did they show you? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b7
  forPractitioner: { text: "At threshold, graduates find primary papers and comment on how adequate their methods, data and interpretation are.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will find original research papers and comment on whether their methods, data and conclusions are sound.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for the scientific literature: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b7.outcome, the excellent cell 4.5.b7.excellent, the descriptor qaa/fheq-2024/4.15.b5 and the Annex D third-class band qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in the scientific literature, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: can you say whether the methods in this paper support its claims? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b7.excellent
  forPractitioner: { text: "At the excellent level, graduates select sources and appraise methods, data and interpretation with a high degree of independence.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will find and choose good sources yourself and judge their methods, data and conclusions largely on your own.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for the scientific literature: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b7, which it grades upward, the descriptor qaa/fheq-2024/4.15.b5 and the Annex D first-class band qaa/fheq-2024/annex-d/cognitive/r1/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in the scientific literature looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: how did you find and choose the sources for your last assignment? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b7.outcome
  forPractitioner: { text: "Graduates will read and use the subject's literature to build insight.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to read and use research papers and other writing in the subject to deepen your understanding.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for the scientific literature: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b7 and 4.5.b7.excellent, the descriptor qaa/fheq-2024/4.15.b5 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in the scientific literature. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: which primary paper have you read closely this term, and what did you make of it? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b8
  forPractitioner: { text: "At threshold, graduates plan, carry out and present their own work, analysing data within a supported framework and showing some time management and independence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will plan, carry out and present your own piece of work, analysing data with support, and show some time management, problem-solving and independence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for independent investigative work: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b8.outcome, the excellent cell 4.5.b8.excellent, the descriptor qaa/fheq-2024/4.15.b6 and the Annex D third-class band qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in independent investigative work, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: what support have you used in planning your project, and what did you decide yourself? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b8.excellent
  forPractitioner: { text: "At the excellent level, graduates run their own project highly independently, evaluate data critically and manage time and problems well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will plan, run and present your own project very independently, judge your data critically and manage your time and problems well.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for independent investigative work: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b8, which it grades upward, the descriptor qaa/fheq-2024/4.15.b6 and the Annex D first-class band qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in independent investigative work looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: which decisions in your project did you make entirely on your own? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b8.outcome
  forPractitioner: { text: "Graduates will complete an independent, open-ended investigation: a lab or field project, a literature review or work with data from several sources.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will complete an open-ended investigation of your own, such as a lab or field project, a literature review or a study of data from different sources.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for independent investigative work: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b8 and 4.5.b8.excellent, the descriptor qaa/fheq-2024/4.15.b6 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in independent investigative work. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: what is your project question, and how will you know you have answered it? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b9
  forPractitioner: { text: "At threshold, graduates identify and discuss applications to global challenges and show some grasp of the scientist's role.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will name and discuss ways biology helps with world problems and show some understanding of what biologists contribute.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for the subject's contribution to world challenges: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b9.outcome, the excellent cell 4.5.b9.excellent, the descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D third-class band qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in the subject's contribution to world challenges, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: can you name one application of biology to a world problem? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b9.excellent
  forPractitioner: { text: "At the excellent level, graduates explain, propose and critique the subject's possible contributions to global challenges.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will explain, propose and critically judge how biology and biologists can help with world problems.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for the subject's contribution to world challenges: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b9, which it grades upward, the descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D first-class band qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in the subject's contribution to world challenges looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: what are the limits of the solution you are proposing? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b9.outcome
  forPractitioner: { text: "Graduates will appreciate the subject's role in modern innovation and their own potential to develop sustainable solutions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will understand how biology has shaped the modern world and how people trained in it can help solve today's and tomorrow's problems sustainably.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for the subject's contribution to world challenges: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b9 and 4.5.b9.excellent, the descriptor qaa/fheq-2024/4.15.b3.1 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in the subject's contribution to world challenges. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: which current global problem could biology help with, and how? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b10
  forPractitioner: { text: "At threshold, graduates identify and explain links to other subjects relevant to the course.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will name and explain how your subject connects to others relevant to your course.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for links with other subjects: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b10.outcome, the excellent cell 4.5.b10.excellent, the descriptor qaa/fheq-2024/4.15.b7 and the Annex D third-class band qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in links with other subjects, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: can you explain one link between your course and another subject? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b10.excellent
  forPractitioner: { text: "At the excellent level, graduates evaluate the subject's part in interdisciplinary challenges and the value of interdisciplinary thinking.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will explain and judge what biology adds to problems that cross subjects, and how thinking across subjects helps solve scientific questions.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for links with other subjects: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b10, which it grades upward, the descriptor qaa/fheq-2024/4.15.b7 and the Annex D first-class band qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in links with other subjects looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: when did combining ideas from two fields help you solve a problem? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b10.outcome
  forPractitioner: { text: "Graduates will recognise the subject's links with other disciplines and work effectively in multidisciplinary settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will see how biology connects with other subjects, in and beyond science, and be able to work well with people from other fields.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for links with other subjects: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b10 and 4.5.b10.excellent, the descriptor qaa/fheq-2024/4.15.b7 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in links with other subjects. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: which other subject has mattered most to your understanding of biology? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b11
  forPractitioner: { text: "At threshold, graduates use mathematical and statistical methods on familiar problems or data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will use maths and statistics to solve familiar problems or assess data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for mathematics and statistics: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b11.outcome, the excellent cell 4.5.b11.excellent, the descriptor qaa/fheq-2024/4.15.b2 and the Annex D third-class band qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in mathematics and statistics, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: can you run the analysis this familiar dataset needs? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b11.excellent
  forPractitioner: { text: "At the excellent level, graduates select, use and evaluate suitable mathematical and statistical methods for problems and data.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will choose the right maths and statistics for a problem, use them well and judge whether they were the right choice.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for mathematics and statistics: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b11, which it grades upward, the descriptor qaa/fheq-2024/4.15.b2 and the Annex D first-class band qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in mathematics and statistics looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: how did you decide which method fitted the data? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b11.outcome
  forPractitioner: { text: "Graduates will deploy mathematical and statistical methods and tools, such as equations, graphs and statistics, to solve problems or evaluate data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to use maths and statistics, such as equations, graphs and statistical tests, to solve problems and make sense of data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for mathematics and statistics: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b11 and 4.5.b11.excellent, the descriptor qaa/fheq-2024/4.15.b2 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in mathematics and statistics. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: which statistical test did you last use, and why that one? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b12
  forPractitioner: { text: "At threshold, graduates collect data accurately, pick suitable analyses, test hypotheses, consider next steps and present data clearly.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will collect data accurately, choose a suitable analysis, test your hypothesis, think about next steps and present your data clearly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for data collection and analysis: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b12.outcome, the excellent cell 4.5.b12.excellent, the descriptor qaa/fheq-2024/4.15.b7 and the Annex D third-class band qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in data collection and analysis, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: how did you choose the analysis for your data? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b12.excellent
  forPractitioner: { text: "At the excellent level, graduates handle data independently and accurately and understand the investigation's place in the field thoroughly.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will handle your data independently and accurately and understand fully where your investigation fits in the field.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for data collection and analysis: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b12, which it grades upward, the descriptor qaa/fheq-2024/4.15.b7 and the Annex D first-class band qaa/fheq-2024/annex-d/practical/r4/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in data collection and analysis looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: where does your investigation fit in current research in the field? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b12.outcome
  forPractitioner: { text: "Graduates will collect, analyse and interpret qualitative and quantitative data to test hypotheses, set findings in context, present them and suggest further work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to collect and analyse data from your investigations, test hypotheses, put your findings in context, present them and suggest what to study next.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for data collection and analysis: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b12 and 4.5.b12.excellent, the descriptor qaa/fheq-2024/4.15.b7 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in data collection and analysis. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: what hypothesis did your data test, and what would you investigate next? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b13
  forPractitioner: { text: "At threshold, graduates take part effectively in teams and contribute clearly.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will take an effective part in group work and make a clear contribution.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for teamwork: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b13.outcome, the excellent cell 4.5.b13.excellent, the descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D third-class band qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in teamwork, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: what was your clear contribution to the team's work? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b13.excellent
  forPractitioner: { text: "At the excellent level, graduates use effective group strategies, add real value and show good teamwork or leadership.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will choose good ways of working as a group, add real value to the team's work and show strong teamwork or leadership.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for teamwork: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b13, which it grades upward, the descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D first-class band qaa/fheq-2024/annex-d/transferable/r2/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in teamwork looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: what strategy did you use to help the group work well? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b13.outcome
  forPractitioner: { text: "Graduates will collaborate successfully and inclusively in groups and contribute positively and flexibly to team outputs.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to work well and inclusively in a group, contributing positively and flexibly to what the team produces.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for teamwork: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b13 and 4.5.b13.excellent, the descriptor qaa/fheq-2024/4.15.b9.1 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in teamwork. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: what did you contribute to your last group project, and how did the group include everyone? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b14
  forPractitioner: { text: "At threshold, graduates convey information, ideas, problems and solutions clearly, spoken or otherwise.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will explain information, ideas, problems and solutions clearly, in speech or in other ways.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for communication: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b14.outcome, the excellent cell 4.5.b14.excellent, the descriptor qaa/fheq-2024/4.15.b8 and the Annex D third-class band qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in communication, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: can you explain this result clearly in a few sentences? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b14.excellent
  forPractitioner: { text: "At the excellent level, graduates communicate to an accomplished standard and consistently suit the audience.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will communicate in an accomplished way and always pitch it right for your audience.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for communication: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b14, which it grades upward, the descriptor qaa/fheq-2024/4.15.b8 and the Annex D first-class band qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in communication looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: how would you change this talk for a non-specialist audience? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b14.outcome
  forPractitioner: { text: "Graduates will communicate effectively, choosing content, media and methods for audience, purpose and subject.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to communicate well, choosing what to say and how to say it for your audience and purpose.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for communication: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b14 and 4.5.b14.excellent, the descriptor qaa/fheq-2024/4.15.b8 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in communication. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: who was the audience for your last piece of communication, and how did you adapt it? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b15
  forPractitioner: { text: "At threshold, graduates describe some ethical issues and social effects, with some regard to history.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will describe some ethical issues and effects on society of new advances, with some sense of the subject's history.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for ethics, history and societal impact: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b15.outcome, the excellent cell 4.5.b15.excellent, the descriptor qaa/fheq-2024/4.15.b4 and the Annex D third-class band qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in ethics, history and societal impact, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: can you describe one ethical issue in a recent advance? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b15.excellent
  forPractitioner: { text: "At the excellent level, graduates evaluate ethical issues and social effects, with some understanding of history.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will understand and weigh up ethical issues and effects on society of new advances, with some grasp of the subject's history.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for ethics, history and societal impact: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b15, which it grades upward, the descriptor qaa/fheq-2024/4.15.b4 and the Annex D first-class band qaa/fheq-2024/annex-d/transferable/r5/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in ethics, history and societal impact looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: how would you weigh the benefits and harms of this advance? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b15.outcome
  forPractitioner: { text: "Graduates will apply ethical awareness and appreciate the subject's history and the social effects of its advances.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to think ethically about work in biology and understand its history and how new discoveries affect society.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for ethics, history and societal impact: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b15 and 4.5.b15.excellent, the descriptor qaa/fheq-2024/4.15.b4 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in ethics, history and societal impact. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: which ethical question does your area of biology raise most sharply? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b16
  forPractitioner: { text: "At threshold, graduates know findings can shift understanding and much remains unknown, and show some ability to keep current.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum, you will know that new findings can change what we think, that much is still not understood, and show you can keep up to some extent.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the threshold cell for keeping up with a changing field: the minimum for the award, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b16.outcome, the excellent cell 4.5.b16.excellent, the descriptor qaa/fheq-2024/4.15.b4 and the Annex D third-class band qaa/fheq-2024/annex-d/knowledge/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in keeping up with a changing field, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: can you name a recent finding that changed what was thought? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b16.excellent
  forPractitioner: { text: "At the excellent level, graduates clearly see knowledge as fluid and integrate new findings into what they knew.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top level, you will clearly see that knowledge keeps moving and be able to build new findings into what you already understand.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for keeping up with a changing field: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b16, which it grades upward, the descriptor qaa/fheq-2024/4.15.b4 and the Annex D first-class band qaa/fheq-2024/annex-d/knowledge/r3/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in keeping up with a changing field looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: how has a new finding changed your own understanding of a topic? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b16.outcome
  forPractitioner: { text: "Graduates will stay current with advances, including sustainability, and appreciate that knowledge changes with new findings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will keep up with new work in biology, including on sustainability, and accept that what we know changes as new findings appear.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for keeping up with a changing field: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b16 and 4.5.b16.excellent, the descriptor qaa/fheq-2024/4.15.b4 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in keeping up with a changing field. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: how do you keep up with new research in your area? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b17.outcome
  forPractitioner: { text: "Graduates will act professionally with regard to legal, ethical and social duties, modelling practice that shows the subject in a positive, sustainable and inclusive light.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will act professionally, respecting your legal, ethical and social duties and setting an example that shows biology and biologists in a positive, sustainable and inclusive light.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for professional conduct: what a graduate will have on graduating (Table 1 lead-in), graded by the cells beside it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 1, benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside the honours descriptor alone (no rung cells for this row), the descriptor qaa/fheq-2024/4.15.b9.1 and the reference step spine:6."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in professional conduct. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: what does acting professionally look like in your lab, field or placement work? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b18
  forPractitioner: { text: "At the master's threshold, graduates reach these outcomes with significant support and guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "As a minimum at master's level, you should reach these outcomes with a good deal of support and guidance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold cell for advanced problem-solving with state-of-the-art concepts: the minimum for the award, at FHEQ Level 7 (FQHEIS Level 11). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 2 (master's), threshold standard. Do not present it as the typical class of degree or as a rule binding the provider. Set it beside the outcome 4.5.b18.outcome, the excellent cell 4.5.b18.excellent, the descriptor qaa/fheq-2024/4.17.b5 and the Annex D third-class band qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must at least manage in advanced problem-solving with state-of-the-art concepts, or staff check a module against the pass line. Tell a student plainly, in the second person, that this is the floor for the award; tell staff it is the threshold column. Ask: how much support did you need to reach this outcome? Avoid reading the cell aloud word for word, and letting it stand for the level most students reach."
- statement: qaa/biosciences-2023/4.5.b18.excellent
  forPractitioner: { text: "At the master's excellent level, graduates reach these outcomes with a high degree of independence and autonomy.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top master's level, you will reach these outcomes largely on your own.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the excellent cell for advanced problem-solving with state-of-the-art concepts: the level the statement ties to a first-class result, an aspiration and not a requirement, at FHEQ Level 7 (FQHEIS Level 11). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 2 (master's), excellent standard. Do not describe it as the pass standard or as what most graduates reach. Set it beside the threshold cell 4.5.b18, which it grades upward, the descriptor qaa/fheq-2024/4.17.b5 and the Annex D first-class band qaa/fheq-2024/annex-d/cognitive/r3/1st."
  author-agent-dialogue: "Raise it when a student aiming high asks what top work in advanced problem-solving with state-of-the-art concepts looks like, or staff calibrate top marks. Put it as what the strongest work shows, not as a demand; for staff, frame it as the top of the range. Ask: which parts of this work did you take forward entirely on your own? Avoid presenting it as the minimum or as the level every student must hit."
- statement: qaa/biosciences-2023/4.5.b18.outcome
  forPractitioner: { text: "Master's graduates should develop and apply a systematic, broad grasp of current concepts to complex problems, integrating and synthesising across them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to bring together a broad, systematic understanding of current biology and use it to solve complex problems.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for advanced problem-solving with state-of-the-art concepts: what a graduate will have on graduating (Table 2 (master's) lead-in), graded by the cells beside it, at FHEQ Level 7 (FQHEIS Level 11). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 2 (master's), benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside 4.5.b18 and 4.5.b18.excellent, the descriptor qaa/fheq-2024/4.17.b5 and the reference step spine:7."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in advanced problem-solving with state-of-the-art concepts. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: which complex problem in your project needed ideas from several areas? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b19.outcome
  forPractitioner: { text: "Master's graduates should interrogate and combine diverse sources to design methods of investigation, including at the forefront and outside their specialism.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to question and combine many kinds of source to design your own methods of investigation, even at the cutting edge or outside your specialism.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for literature-led design of methods: what a graduate will have on graduating (Table 2 (master's) lead-in), graded by the cells beside it, at FHEQ Level 7 (FQHEIS Level 11). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 2 (master's), benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside the honours descriptor alone (no rung cells for this row), the descriptor qaa/fheq-2024/4.17.b4.2 and the reference step spine:7."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in literature-led design of methods. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: which sources outside your specialism shaped the methods you chose? Avoid reciting the table text at length."
- statement: qaa/biosciences-2023/4.5.b20.outcome
  forPractitioner: { text: "Master's graduates should plan a significant research project (ethics, hazards, environment, sustainability, cost), develop advanced investigative skills for it and discuss its background, methods, results and impact.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to plan a substantial research project, thinking about ethics, hazards, environmental effects, sustainability and cost, build advanced practical skills for it, and discuss its background, methods, results and possible impact.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the benchmark outcome for the master's research project: what a graduate will have on graduating (Table 2 (master's) lead-in), graded by the cells beside it, at FHEQ Level 7 (FQHEIS Level 11). Cite it as QAA (2023), Biosciences Subject Benchmark Statement, para 4.5, Table 2 (master's), benchmark outcome column. Do not lift it into module outcomes unchanged or claim it holds at another level. Set it beside the honours descriptor alone (no rung cells for this row), the descriptor qaa/fheq-2024/4.17.b6 and the reference step spine:7."
  author-agent-dialogue: "Raise it when someone asks what the degree should leave a graduate able to do in the master's research project. Explain it to a student in plain words, in the second person, and to staff as a course-level outcome, then turn to the cells that grade it. Ask: what ethical, safety or cost questions did your project plan have to answer? Avoid reciting the table text at length."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.9; 4.2" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.9; 4.2" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.14" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.14" }
  - { id: "spine:6", role: "refers", locator: "inferred: std:ref:uk-framework R2 (honours, Table 1 and generic skills)" }
  - { id: "spine:7", role: "refers", locator: "inferred: std:ref:uk-framework R2 (master's, Table 2)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.9: \"a degree with honours (FHEQ Level 6; FQHEIS Level 10)\"; 4.2)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.14: integrated master's, FHEQ Level 7; FQHEIS Level 11)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.9", "1.10", "1.12", "1.13", "1.14", "1.15", "2.6", "2.20", "2.23", "2.27", "2.33", "3.4", "3.6", "3.9", "3.10", "4.5"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.16", "1.17", "2.6", "2.20", "2.27", "3.6", "3.10"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.7", "1.8", "1.18", "1.19", "1.20", "1.22", "2.6", "2.20", "2.33", "3.4", "4.5"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.21", "1.22", "1.23", "1.24", "2.27", "2.28", "3.4", "3.9"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "4.2 names Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees (QAA 2019; now in the Frameworks 2024)" }
- { rel: "cites", target: "std:doc:qaa-fheq-2024-framework", note: "2.9, 2.14: FHEQ Levels 6 and 7" }
- { rel: "cites", target: "std:doc:qaa-fqheis-2024-framework", note: "2.9, 2.14: FQHEIS Levels 10 and 11" }
- { rel: "themeReference", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "1.20: QAA and Advance HE Education for Sustainable Development Guidance" }
- { rel: "themeReference", target: "std:doc:qaa-enterprise-2018-guidance", note: "1.24: Enterprise and Entrepreneurship Education guidance (2018)" }
- { rel: "refersTo", target: "QAA Characteristics Statement for Micro-credentials", note: "2.21; not yet ingested (Part E)" }
- { rel: "readWith", target: "std:doc:qaa-biomedical-science-and-biomedical-sciences-2023-benchmarks", note: "1.6, 2.5: Biomedical Sciences" }
- { rel: "readWith", target: "std:doc:qaa-chemistry-2022-benchmarks", note: "1.6, 2.5: Chemistry" }
- { rel: "readWith", target: "std:doc:qaa-geography-2022-benchmarks", note: "1.6, 2.5: Geography" }
- { rel: "readWith", target: "std:doc:qaa-earth-sciences-environmental-sciences-and-environmental-studies-2022-benchmarks", note: "1.6, 2.5: ES3" }
- { rel: "refersTo", target: "Royal Society of Biology", note: "2.37: a major accreditor; requirements not yet ingested (Part E)" }
- { rel: "refersTo", target: "Chartered Institute of Ecology and Environmental Management", note: "2.37: accredits courses; not yet ingested" }
- { rel: "refersTo", target: "Committee of Heads of Environmental Science", note: "2.37: accredits courses; not yet ingested" }
- { rel: "refersTo", target: "Equality Act 2010", note: "1.16: legislation; not a standards document here" }
- { rel: "refersTo", target: "Animals (Scientific Procedures) Act", note: "1.18: legislation; not a standards document here" }
- { rel: "refersTo", target: "United Nations Sustainable Development Goals", note: "1.7, 1.19" }
- { rel: "relatedTo", target: "Office for Students regulatory framework; Quality Assessment Framework for Wales; Quality Enhancement Framework (Scotland)", note: "front matter: the statement's regulatory status by nation" }
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
- Biosciences is the study of life, a subject so wide and fast-growing that no one could cover it all, so degrees balance current specialisms with breadth (D1, 1.1)
- Graduates work across industry, government, NGOs and education, most of them outside research (D1, 1.2)
- The subject rests on objective observation, yet its history includes bias that courses are asked to confront (D1, 1.14)
- A broad, fast-moving field central to understanding life on Earth and often at the front line of global challenges (D1, 2.1)
- Its range runs from cell chemistry and evolution to physiology, populations, ecology and biotechnology (D1, 2.2)
- No course need span every sub-discipline; many valid paths exist within it (D1, 2.3)
- Often interdisciplinary, overlapping with biomedical science, chemistry, geography, the environmental sciences and data science (D1, 2.5)
- Courses mix experimental and theoretical work, often with fieldwork, and increasingly computational and simulated learning (D1, 2.6)
- Highly collaborative, with partnerships across education, employers and learned societies (D1, 2.24)
- Knowledge in it is often contested and provisional, and uncertainty is a key concept (D1, 3.3)

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "Asks courses to confront the field's history of bias, credit diverse scientists, check materials for stereotypes and make practical work inclusive; graduates should understand EDI in the discipline and work inclusively in teams (D1, 1.10, 1.13 to 1.15)"
  statements: ["qaa/biosciences-2023/1.9", "qaa/biosciences-2023/1.10", "qaa/biosciences-2023/1.12", "qaa/biosciences-2023/1.13", "qaa/biosciences-2023/1.14", "qaa/biosciences-2023/1.15", "qaa/biosciences-2023/3.10.b3", "qaa/biosciences-2023/4.5.b13.outcome", "qaa/biosciences-2023/4.5.b17.outcome"]
- theme: theme:accessibility
  inThisSubject: "Reaches laboratory, field and placement work at home and abroad: course teams must make the curriculum fully accessible by design, with individual adjustments and early contact with disability teams (D1, 1.16, 1.17)"
  statements: ["qaa/biosciences-2023/1.16", "qaa/biosciences-2023/1.17", "qaa/biosciences-2023/2.27", "qaa/biosciences-2023/3.6", "qaa/biosciences-2023/3.9", "qaa/biosciences-2023/3.10.b3", "qaa/biosciences-2023/3.10.b4"]
- theme: theme:esd
  inThisSubject: "Framed through the Sustainable Development Goals and practical lab and field sustainability, with particular weight on living resources and the three Rs in animal use; carried into the experimental design, challenges and professional conduct outcomes (D1, 1.7, 1.8, 1.18 to 1.20)"
  statements: ["qaa/biosciences-2023/1.8", "qaa/biosciences-2023/1.18", "qaa/biosciences-2023/1.19", "qaa/biosciences-2023/1.20", "qaa/biosciences-2023/4.5.b3.outcome", "qaa/biosciences-2023/4.5.b3", "qaa/biosciences-2023/4.5.b3.excellent", "qaa/biosciences-2023/4.5.b9.outcome", "qaa/biosciences-2023/4.5.b16.outcome", "qaa/biosciences-2023/4.5.b17.outcome", "qaa/biosciences-2023/4.5.b20.outcome"]
- theme: theme:enterprise
  inThisSubject: "Employability is named a fundamental outcome: co-created enterprise education, work-integrated learning, placements, industry projects and careers fairs (D1, 1.21 to 1.23, 2.27, 2.28)"
  statements: ["qaa/biosciences-2023/1.22", "qaa/biosciences-2023/1.23", "qaa/biosciences-2023/2.27", "qaa/biosciences-2023/2.28", "qaa/biosciences-2023/3.9"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "2.2", gloss: "six areas spanning the subject, from cell chemistry to applied biotechnology" }
  - { component: "3.2", gloss: "a foundation across processes, weighted to the course emphasis" }
  - { component: "3.4", gloss: "typical content in four groups: core knowledge, wider context, practical and transferable skills, personal development" }
practices:
  - { component: "2.19", kind: "learning", gloss: "campus-based, blended and flipped learning" }
  - { component: "2.20", kind: "learning", gloss: "distance learning, synchronous and asynchronous" }
  - { component: "3.5", kind: "teaching", gloss: "scaffolding from supported to independent study" }
  - { component: "3.6", kind: "teaching", gloss: "student-centred, blended delivery; staff development" }
  - { component: "3.7", kind: "learning", gloss: "synchronous activities, from lectures to placements" }
  - { component: "3.8", kind: "learning", gloss: "asynchronous activities, from simulations to portfolios" }
  - { component: "3.9", kind: "assessment", gloss: "varied, progressive, authentic assessment" }
  - { component: "3.10", kind: "assessment", gloss: "nine principles for inclusive assessment" }
  - { component: "3.11", kind: "assessment", gloss: "themes for authentic assessment" }
  - { component: "3.12", kind: "assessment", gloss: "coursework and examination formats" }
  - { component: "3.13", kind: "assessment", gloss: "integrated master's: unfamiliar problems and research skills" }
  - { component: "3.14", kind: "assessment", gloss: "qualities of feedback" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.5", award: ["bachelor's with honours", "master's"], items: 17 }
  - { rung: "typical", leadIn: "none", award: "none", items: 0 }
  - { rung: "excellent", leadIn: "4.5", award: ["bachelor's with honours", "master's"], items: 17 }
rungBases: "Two rungs only, threshold and excellent, defined in 4.4 and laid out in Tables 1 (honours, 'graduates will have') and 2 (master's, 'graduates should be able to'), both inside 4.5. Each row pairs a benchmark outcome with its threshold and excellent cells, so gradeOf is stated. Table 1 row 17 has no rung cells; Table 2's two rung cells sit in its first row."
outcomeLists:
  - { leadIn: "4.5", gloss: "Table 1 benchmark outcome column: what an honours graduate will have", items: 17, award: ["bachelor's with honours"] }
  - { leadIn: "4.5", gloss: "Table 2 benchmark outcome column: master's outcomes in addition to Table 1", items: 3, award: ["master's"] }
outcomes:
  - { outcome: "core concepts", threshold: "qaa/biosciences-2023/4.5.b1", typical: "none", excellent: "qaa/biosciences-2023/4.5.b1.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "breadth of the subject", threshold: "qaa/biosciences-2023/4.5.b2", typical: "none", excellent: "qaa/biosciences-2023/4.5.b2.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "experimental design and problem-solving", threshold: "qaa/biosciences-2023/4.5.b3", typical: "none", excellent: "qaa/biosciences-2023/4.5.b3.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "safe working and risk assessment", threshold: "qaa/biosciences-2023/4.5.b4", typical: "none", excellent: "qaa/biosciences-2023/4.5.b4.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "practical techniques", threshold: "qaa/biosciences-2023/4.5.b5", typical: "none", excellent: "qaa/biosciences-2023/4.5.b5.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "computational tools", threshold: "qaa/biosciences-2023/4.5.b6", typical: "none", excellent: "qaa/biosciences-2023/4.5.b6.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "scientific literature", threshold: "qaa/biosciences-2023/4.5.b7", typical: "none", excellent: "qaa/biosciences-2023/4.5.b7.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "independent project", threshold: "qaa/biosciences-2023/4.5.b8", typical: "none", excellent: "qaa/biosciences-2023/4.5.b8.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "contribution to world challenges", threshold: "qaa/biosciences-2023/4.5.b9", typical: "none", excellent: "qaa/biosciences-2023/4.5.b9.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "links with other subjects", threshold: "qaa/biosciences-2023/4.5.b10", typical: "none", excellent: "qaa/biosciences-2023/4.5.b10.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "mathematics and statistics", threshold: "qaa/biosciences-2023/4.5.b11", typical: "none", excellent: "qaa/biosciences-2023/4.5.b11.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "data collection and analysis", threshold: "qaa/biosciences-2023/4.5.b12", typical: "none", excellent: "qaa/biosciences-2023/4.5.b12.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "teamwork", threshold: "qaa/biosciences-2023/4.5.b13", typical: "none", excellent: "qaa/biosciences-2023/4.5.b13.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "communication", threshold: "qaa/biosciences-2023/4.5.b14", typical: "none", excellent: "qaa/biosciences-2023/4.5.b14.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "ethics, history and societal impact", threshold: "qaa/biosciences-2023/4.5.b15", typical: "none", excellent: "qaa/biosciences-2023/4.5.b15.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "keeping current", threshold: "qaa/biosciences-2023/4.5.b16", typical: "none", excellent: "qaa/biosciences-2023/4.5.b16.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "professional conduct", threshold: "none", typical: "none", excellent: "none", basis: "none", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "master's: complex problems", threshold: "qaa/biosciences-2023/4.5.b18", typical: "none", excellent: "qaa/biosciences-2023/4.5.b18.excellent", basis: "stated", domain: "subject-skill", award: "master's" }
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
- { body: "Royal Society of Biology", says: "currently a major accreditor of courses in the subject, across a wide range of courses (D1, 2.37)", requirements: "not yet ingested (Part E)" }
- { body: "Chartered Institute of Ecology and Environmental Management (CIEEM)", says: "accredits courses at undergraduate or postgraduate taught level (D1, 2.37)", requirements: "not yet ingested (Part E)" }
- { body: "Committee of Heads of Environmental Science (CHES)", says: "accredits courses at undergraduate or postgraduate taught level (D1, 2.37)", requirements: "not yet ingested (Part E)" }
- { body: "accrediting and approval bodies (unnamed)", says: "assessment and feedback should fit their requirements where needed (D1, 3.10)", requirements: "not yet ingested (Part E)" }
- { body: "professional bodies and learned societies (unnamed)", says: "partners in co-creating enterprise education and in student engagement (D1, 1.22, 2.24, 2.29)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.9", "1.10", "1.12", "1.13", "1.14", "1.15", "2.6", "2.20", "2.23", "2.27", "2.33", "3.4", "3.6", "3.9", "3.10", "4.5"], statements: ["1.9", "1.10", "1.12", "1.13", "1.14", "1.15", "3.10.b3", "4.5.b13.outcome", "4.5.b17.outcome"] }
  - { id: "theme:accessibility", named: "Accessibility (accessibility and the needs of disabled students)", carriedIn: ["1.16", "1.17", "2.6", "2.20", "2.27", "3.6", "3.10"], statements: ["1.16", "1.17", "2.27", "3.6", "3.9", "3.10.b3", "3.10.b4"] }
  - { id: "theme:esd", named: "Education for Sustainable Development", carriedIn: ["1.7", "1.8", "1.18", "1.19", "1.20", "1.22", "2.6", "2.20", "2.33", "3.4", "4.5"], statements: ["1.8", "1.18", "1.19", "1.20", "4.5.b3.outcome", "4.5.b3", "4.5.b3.excellent", "4.5.b9.outcome", "4.5.b16.outcome", "4.5.b17.outcome", "4.5.b20.outcome"] }
  - { id: "theme:enterprise", named: "Employability, enterprise and entrepreneurship", carriedIn: ["1.21", "1.22", "1.23", "1.24", "2.27", "2.28", "3.4", "3.9"], statements: ["1.22", "1.23", "2.27", "2.28", "3.9"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.9", "2.14", "4.2"] }
  - { framework: "scqf", named: "FQHEIS", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.9", "2.14", "4.2"] }
bodies:
  - { body: "Royal Society of Biology", citedIn: ["2.37"] }
  - { body: "Chartered Institute of Ecology and Environmental Management", citedIn: ["2.37"] }
  - { body: "Committee of Heads of Environmental Science", citedIn: ["2.37"] }
  - { body: "accrediting and approval bodies (unnamed)", citedIn: ["3.10"] }
  - { body: "professional bodies and learned societies (unnamed)", citedIn: ["1.22", "2.24", "2.29"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "evidence of achievement above the threshold" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA and Advance HE Education for Sustainable Development Guidance", citedIn: ["1.20"], role: "embedding sustainable development in the curriculum" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers", citedIn: ["1.24"], role: "more on enterprise education" }
  - { document: "not yet ingested: listed in Part E", named: "QAA Characteristics Statement for Micro-credentials", citedIn: ["2.21"], role: "more on micro-credentials" }
  - { document: "std:doc:qaa-biomedical-science-and-biomedical-sciences-2023-benchmarks", named: "Biomedical Sciences", citedIn: ["1.6", "2.5"], role: "neighbouring subject statement" }
  - { document: "std:doc:qaa-chemistry-2022-benchmarks", named: "Chemistry", citedIn: ["1.6", "2.5"], role: "neighbouring subject statement" }
  - { document: "std:doc:qaa-geography-2022-benchmarks", named: "Geography", citedIn: ["1.6", "2.5"], role: "neighbouring subject statement" }
  - { document: "std:doc:qaa-earth-sciences-environmental-sciences-and-environmental-studies-2022-benchmarks", named: "ES3 (Earth Sciences, Environmental Sciences and Environmental Studies)", citedIn: ["1.6", "2.5"], role: "neighbouring subject statement" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "threshold-standard", definition: "the minimum level for an honours degree, at which graduates show acceptable ability and skills (D1, 4.4)", beneficiaryDefinition: "the least you need to show to gain the honours award", scopeNote: "honours; Table 2 uses it for the master's threshold too", category: "unknown", practices: ["education"] }
- { slug: "excellent-standard", definition: "the level tied to a first-class degree, where graduates consistently show advanced knowledge, understanding and skills (D1, 4.4)", beneficiaryDefinition: "the level of the strongest work, linked to a first-class result", scopeNote: "honours; Table 2 uses it for master's", category: "unknown", practices: ["education"] }
- { slug: "employability", definition: "a set of competencies, combining knowledge, skills and behaviours, that make people more likely to find work and succeed in it, to their own and society's benefit (D1, 1.21)", beneficiaryDefinition: "the mix of knowledge, skills and behaviours that helps you get and do well in work", scopeNote: "the statement pairs it with entrepreneurship", category: "unknown", practices: ["education"] }
- { slug: "education-for-sustainable-development", definition: "building curriculum structures and subject content that support and enact sustainable development, quoting UNESCO's 2019 definition (D1, 1.19)", beneficiaryDefinition: "learning that helps you understand and act for sustainable development", scopeNote: "shared theme theme:esd", category: "unknown", practices: ["education"] }
- { slug: "micro-credential", definition: "a credit-bearing unit at a recognised framework level, quality assured but carrying no award in its own right (D1, 2.21)", beneficiaryDefinition: "a short course that earns credit but is not a full award", scopeNote: "often for professionals upskilling; credits may be stacked", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "threshold-standard", form: "threshold standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "excellent-standard", form: "excellent standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "employability", form: "Employability", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "education-for-sustainable-development", form: "education for sustainable development (ESD)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "micro-credential", form: "Micro-credentials", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Biosciences"
  edition: "March 2023 (fifth edition)"
  year: 2023
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/biosciences-2023/biosciences-2023.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: aea735fda4983391d834a61aa168673e3e8e9f5a1c1760265bb436f8fdff3706
  heldFiles: ["wkspc2601-library/txt/qaa-2023-biosciences-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2023-biosciences-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2023-biosciences-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2023-biosciences-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0038", title: "QAA Characteristics Statement for Micro-credentials", issuer: "QAA", why: "cited in 2.21; not yet ingested" }
- { w: "W-std-0036", title: "QAA Characteristics Statement: Higher Education in Apprenticeships (2019)", issuer: "QAA", why: "in the reference list; bears on 2.15 and 2.25" }
- { w: "W-std-0039", title: "Royal Society of Biology degree accreditation requirements", issuer: "Royal Society of Biology", why: "SB5: the major accreditor named in 2.37" }
```

## Part E Gaps and questions
- Rungs: two only, threshold and excellent (4.4); no typical rung, unlike Psychology. The skeleton found no rung lists; the rungs sit in Tables 1 and 2 within the span of 4.5, which the skeleton took as one paragraph. Records cut by `find` with our ids 4.5.b<k>.outcome, 4.5.b<k> (threshold) and 4.5.b<k>.excellent.
- Table shape new to the batch: three columns per row (benchmark outcome, threshold standard, excellent standard), each cell different text. The outcome column is recorded as type outcome, rung none; the excellent cell takes gradeOf the threshold cell in the same row, basis stated (paired by row).
- Force on Table 1: the lead-in says "graduates will have". Outcome and threshold cells are recorded as force threshold (a condition of award, D-std-0004 (a); 4.1 calls them the minimum a student will have demonstrated when awarded the degree); excellent cells as describes (the column describes a level tied to a first-class result and binds no graduate; 4.1 says the excellent levels assist course teams). The builder's force check looks only 600 characters back and cannot see the table lead-in, so will could not be recorded. For Abbott.
- Force on Table 2: the lead-in says "graduates should be able to"; outcome and threshold cells keep should; the excellent cell is describes, as in Table 1.
- Table extraction: pdftotext interleaved the cells. Row 11 (mathematics and statistics) is split by a page break: the outcome span holds only its first part ("... such as the manipulation"), the rest ("of equations and graphical and statistical analysis, to solve problems or evaluate data.") follows the next page number; the excellent span likewise holds only "Select, use and evaluate appropriate mathematical and statistical concepts,", its end ("processes and tools to solve problems or evaluate data.") after the outcome's. Paraphrases cover the whole cell.
- Table 1 row 17 ("Act professionally ...") shows no threshold or excellent cell in the extraction: recorded as an outcome only; it may span the rung columns in the original. To check against the PDF.
- Table 2: "With significant support and guidance." and "With a high degree of independence and autonomy." are attached to the first row (4.5.b18, 4.5.b18.excellent); the original may merge them across all rows. The last three items ("Project plan ...", "Develop advanced experimental ...", "Discuss the background ...") are cut as one outcome (4.5.b20.outcome), the research project, since the second refers to "the project"; they may be three rows. To check against the PDF.
- Table 2 award: "a master's degree in Biosciences"; the statement does not say integrated or standalone, though 2.14 and 3.13 describe integrated master's. Recorded as master's at fheq:7 and fqheis:11.
- A number after "see paragraph" (Table 1 row 1: 3.4) and after "indicated in paragraph" (2.3: 2.2) is a reference, not a statement (DPN-1).
- Obliging words outside the five: "need(s) to" in 1.1, 1.11, 1.12, 2.22 (1.1 and 2.22 recorded as describes; 1.11 and 1.12 take should from their own should sentences); "is essential" in 3.5 and 1.19; "requiring" and "considered crucial" in 3.13 (recorded as describes); "it is expected that students are able to" in 2.14 (recorded as will); "will be required to pass" in 2.15 (recorded as must). For Abbott.
- Plain-present provider norms, not recorded as statements (template open point 5): 1.7 ("are designed to equip"), 2.4 ("are designed to provide"), 2.11 ("are normally offered"), 2.33 ("A review ensures the embedding of ESD and EDI"), 3.4 items b2 to b19 and the unbulleted item on responsible research ("generally include"), 3.5 opening, 3.9 opening, 4.5 ("students demonstrate achievement across the main outcomes").
- Will-worded predictions read as description, not statements: 1.2 ("will equip graduates", "will use their knowledge"), 2.3 ("will not attempt"), 2.5 ("there will be overlap"), 2.7 ("It will also include"), 2.26 ("many courses will collaborate"), 2.36 ("external examiners will be asked"), 4.2 first sentence ("The majority of students will perform significantly better"). 4.1 (the minimum threshold standards a student will have demonstrated) is read as the frame for the tables, not a statement.
- 4.4 defines the two rungs (threshold standard, excellent standard); the skeleton marked its two items as threshold candidates: they are definitions, held in Part B, not statements.
- Section-1 graduate paragraphs (1.3, 1.4, 1.5, 1.9, 1.10, 1.11, 1.23) and 3.2, 3.3 are recorded at fheq:6 for the honours award (inferred: the paragraphs name graduates of the subject without an award).
- 2.15 degree apprenticeships at "Level 6 or 7": level recorded as none, award as degree apprenticeship (Level 6 or 7); the text does not name the framework.
- Skeleton theme hits are shifted by one paragraph where a sub-heading is printed at the end of the paragraph before (for example the EDI heading ends 1.12): SB6 and S6 use the paragraphs that carry the theme words.
- Subject code inferred: hecos 100346 biology (the text names "biological" and "Biosciences" but not biology as a subject). HECoS 100345 is labelled "biological sciences"; the statement uses Biosciences and "biological sciences" (1.14) for the same subject: recorded as stated. For P3.
- Not named as benchmarks in S7 or SB6: "Marine Sciences", "Analytical Chemistry", "Data Analytics or Information Technology" (2.5) and the joint-honours partners in 2.22 (Geography, Sustainable Development, Psychology, Mathematics, Chemistry): named as subject areas, not as statements to consult.
- CQFW: not cited by the statement. Shared documents in the excluded front matter and reference list (UK Quality Code 2019, Advice and Guidance, QAA Glossary, HEA Framework for embedding employability 2016, Characteristics Statement on apprenticeships) are not in SB6 (excluded matter).
- Annex D is cited in its 2019 form (4.2; reference list); pointed to here as std:doc:qaa-fheq-2024-framework, Annex D, where QAA now publishes it.
- Every SB5 body's requirements are not yet ingested; D3 lists the Royal Society of Biology's.
- Differences from Psychology: no typical rung; three-column rung tables; a master's table added to honours; no stated statement of scope sentence (statedScope quotes 1.1); accreditors are three bodies, none a regulator; the cross-cutting themes sit as sub-sections of section 1 with their headings printed at the end of the paragraph before.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:36: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0090 (P1); built by tools/bm_build.py.
