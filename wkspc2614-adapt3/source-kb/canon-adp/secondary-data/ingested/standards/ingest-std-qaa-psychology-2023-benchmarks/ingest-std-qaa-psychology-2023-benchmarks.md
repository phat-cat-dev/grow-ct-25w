---
id: std:doc:qaa-psychology-2023-benchmarks
title: Subject Benchmark Statement Psychology
profile: standards/subject-benchmark
profileVersion: 0.1.3-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: hecos, code: "100497", label: psychology, basis: stated }
  - { scheme: cah, code: CAH04-01-01, label: psychology (non-specific), basis: stated }
  - { scheme: cah, code: CAH04-01, label: psychology, basis: stated }
  - { scheme: cah, code: CAH04, label: psychology, basis: stated }
  - { scheme: hecos, code: "100993", label: cognitive psychology, basis: stated }
  - { scheme: hecos, code: "100952", label: developmental psychology, basis: stated }
  - { scheme: hecos, code: "100498", label: social psychology, basis: stated }
  - { scheme: hecos, code: "100959", label: research methods in psychology, basis: stated }
  - { scheme: hecos, code: "101344", label: psychobiology, basis: inferred }
edition: September 2023
published: 2023-09
status: current
supersedes: none
heldText: { method: sha256-bytes, raw: e99f2554cfa38665fb9c384b03d87c7e7e1d7d77f1cf911e892d3660d7265697, normalised: c413483ff226a08620c5e9ff852cca9fd399c9ab4c7f4c3ee8b70f2ed26b5f29 }
heldTextStan: { method: sha256-stan, raw: e99f2554cfa38665fb9c384b03d87c7e7e1d7d77f1cf911e892d3660d7265697, normalised: 621d0098dc6a065f91c4820d38c49fdd83153b685cb534dbcecb792aace0af68 }
licence: QAA copyright; held for study, never published (re-use terms to check, Part E)
series: QAA Subject Benchmark Statements, fifth edition series with cross-cutting themes (2022 onward; recall, to check)
awardsCovered: ["bachelor's with honours", "master's conversion"]
levelsCovered: [fheq:6, fheq:7, fqheis:10, fqheis:11]
nations: [England, Wales, Scotland, Northern Ireland]
parts:
  S: full
  B: "partial: no glossary in the document; terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.4.0-draft, benchmarkTemplate: 0.4.0-draft, runFrame: 0.1.1-draft, runLayer: 0.4.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.4.0-draft; std, run 0043
passes:
  P1: 2026-10-03, std (claude.ai, META Project)
  P2: "skipped: no trigger beyond the inferred codes and rung links, which P3 settles"
  P3: open
version: 0.2.1
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.4.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.4.0-draft -->
# Subject Benchmark Statement: Psychology (QAA, September 2023)

> Run 0043, P1 by std. The issuer's words are held beside this document's collection (`wkspc2601-library/txt/qaa-2023-psychology-subject-benchmark-statement-standard.norm.txt`) and never copied here: every statement points into them by character span. Everything else is our words. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in Psychology should know and be able to do at the end of an honours degree or a master's conversion course: the subject's outcome lists and its three rungs of achievement (threshold, typical, excellent). Reach for it when designing, reviewing or describing a psychology course or its outcomes. It is not a curriculum, not the professional body's accreditation standard and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in September 2023 for the sector, the statement describes the discipline, its purposes and distinctive features, the content, skills, teaching and assessment of a degree, and benchmark standards at threshold, typical and excellent levels for bachelor's degrees with honours and master's conversion courses. It adds the four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability; enterprise and entrepreneurship), points to QAA's degree classification descriptions (Annex D) for the generic skills each classification shows, and sets the subject beside its professional body (BPS) and regulator (HCPC). Providers, external examiners and PSRBs use it in design, approval and review; it replaced the previous Psychology statement (edition and date not given in the text: Part E).

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: Subject Benchmark Statement Psychology
edition: September 2023
dates:
  published: 2023-09
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: 'reference'   # a sector reference point, "not a regulatory requirement" (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of quality requirements in Northern Ireland (D1, front matter: Relationship to legislation)
licence: 'QAA copyright; the document gives no re-use terms in its text (D1, front matter)'
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2023", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: 'what a Psychology graduate can be expected to know, do and understand at the end of an honours degree or a master''s conversion course, and the nature and characteristics of awards in the subject (D1, front matter: About this Statement; 1.16; 4.1)'
appliesTo:
  awards: ["bachelor's degrees with honours, BPS-accredited or not", "master's conversion courses", "integrated master's (described, 2.10)"]
  levels: [fheq:6, fheq:7, fqheis:10, fqheis:11]
  providers: [UK higher education providers]
whoMustUse: none-stated; it is a reference point, not a requirement (D1, front matter)
howUsed: [design, approval, review, other: external examining; PSRBs' reference for academic standards; information for prospective students and employers]
doesNot: it is not a national curriculum and does not prescribe teaching, learning or assessment; it does not interpret legislation or carry statutory or regulatory requirements (D1, front matter)
beneficiary: the student
statedScope: '"This Subject Benchmark Statement applies to conversion level as well as undergraduate courses." (D1, 1.16)'
statedSubjects:
  - { name: Psychology, locator: (D1, title; 1.1), kind: subject, codes: [{ scheme: hecos, code: "100497", label: psychology }, { scheme: cah, code: CAH04-01-01, label: psychology (non-specific) }] }
  - { name: "conversion degree at master's level", locator: (D1, 1.16; 2.8; 4.5), kind: programme title, codes: [{ scheme: hecos, code: "100497", label: psychology }] }
  - { name: "single honours ... joint honours ... combined joint or major/minor honours", locator: (D1, 1.13), kind: programme title, codes: [{ scheme: hecos, code: "100497", label: psychology }] }
  - { name: "Bachelor's degree in Science (BSc) or Arts (BA)", locator: (D1, 2.1), kind: programme title, codes: [{ scheme: hecos, code: "100497", label: psychology }] }
  - { name: Biological psychology, locator: (D1, 3.4), kind: specialism, codes: [] }
  - { name: Cognitive psychology, locator: (D1, 3.4), kind: specialism, codes: [{ scheme: hecos, code: "100993", label: cognitive psychology }] }
  - { name: Developmental psychology, locator: (D1, 3.4), kind: specialism, codes: [{ scheme: hecos, code: "100952", label: developmental psychology }] }
  - { name: Individual differences, locator: (D1, 3.4), kind: specialism, codes: [] }
  - { name: Social psychology, locator: (D1, 3.4), kind: specialism, codes: [{ scheme: hecos, code: "100498", label: social psychology }] }
  - { name: Methods of research and enquiry, locator: (D1, 3.6), kind: specialism, codes: [{ scheme: hecos, code: "100959", label: research methods in psychology }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->

```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Psychology Degree", gloss: "psychology as a scientific, reflective, theoretical and applied discipline, and the statement as a roadmap grounded in inclusion and ethics" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Purposes of a Psychology degree", gloss: "the purpose of the degree: understanding self, others and society through empirical enquiry, building psychological literacy" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Purposes of a Psychology degree", gloss: "graduates go on to further study, training, research and employment in every sector" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes of a Psychology degree", gloss: "the BPS accredits courses; chartered status needs an accredited route plus postgraduate training; the statement covers all honours degrees, accredited or not" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes of a Psychology degree", gloss: "degree titles must not mislead, and avoid the protected postgraduate titles" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes of a Psychology degree", gloss: "practising as a psychologist needs postgraduate training and HCPC registration for the nine protected titles (S4)" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes of a Psychology degree", gloss: "the HCPC protects the public; wider workforce roles are registered by the Professional Standards Authority" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes of a Psychology degree", gloss: "careers outside the title of psychologist, in public, private and third sectors" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes of a Psychology degree", gloss: "research careers, and the PhD route" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes of a Psychology degree", gloss: "the statement is a UK reference point that recognises international standards" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Psychology Degree", gloss: "breadth and depth of knowledge and a wide set of skills, interpersonal skills among them" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Psychology Degree", gloss: "critical thinking about social justice, diversity and inclusion; links to the UN Sustainable Development Goals" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Psychology Degree", gloss: "single, joint, combined and major or minor honours" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Psychology Degree", gloss: "full-time and part-time study; study abroad and placements" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Psychology Degree", gloss: "where psychology sits in a provider (sciences or social sciences) and the different emphases that follow" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Psychology Degree", gloss: "master's-level conversion degrees, and the statement's coverage of them" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "the Equality Act 2010 duty to embed EDI; the discipline's history of marginalising some groups" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "how equality is achieved, and the expectation that graduates value and live EDI (S4)" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "curricula built on narrow populations; the call for diverse voices" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive learning environments and their aims" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "critique of dominant systems of thought; commitment to social justice" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "the discipline as a driver of positive social change" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "mental health, belonging and the language of the discipline" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "the Equality Act duty to anticipate accessibility in course design (S4)" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "anticipatory reasonable adjustments in every setting" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "individual discussion of adjustments, including alternative assessment" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "flexible approaches to structural inequality" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "psychology's contribution to local and global challenges; graduates as global citizens" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "the SDGs and psychology's part in them, naming SDGs 3 to 5, 8, 11 and 16" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "ESD and UNESCO's key competencies as core to the curriculum" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "transformative pedagogies for ESD in course and module design" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "inclusion and climate action as part of sustainable development" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise education, historically under-used in psychology" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise opportunities, employability and venture creation" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "forms enterprise education takes" }
  - { number: "2.1", order: 39, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "awards (BSc, BA, conversion, MSc, MSci, MA) and design flexibility around a broad scientific core" }
  - { number: "2.2", order: 40, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "historical and contemporary theory, integrated and culturally diverse" }
  - { number: "2.3", order: 41, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "subject-specific and transferable skills defined" }
  - { number: "2.4", order: 42, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "psychological literacy and its value" }
  - { number: "2.5", order: 43, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "ethics at the core; students able to act ethically and judge others' ethics (S4)" }
  - { number: "2.6", order: 44, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "an evolving discipline; emerging areas as examples" }
  - { number: "2.7", order: 45, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through levels to the threshold skills (FHEQ level 6; FQHEIS level 10)" }
  - { number: "2.8", order: 46, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "postgraduate entry, and the BPS Graduate Basis for Chartered Membership rule (S4)" }
  - { number: "2.9", order: 47, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined programmes" }
  - { number: "2.10", order: 48, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's degrees (FHEQ level 7; FQHEIS level 11)" }
  - { number: "2.11", order: 49, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards; Scottish four-year degrees; part-time equivalence" }
  - { number: "2.12", order: 50, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes of delivery and digital flexibility" }
  - { number: "2.13", order: 51, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "technology-enhanced learning and digital skills" }
  - { number: "2.14", order: 52, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "student input into curriculum and assessment" }
  - { number: "2.15", order: 53, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "work-based learning and placements with partners" }
  - { number: "2.16", order: 54, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnerships for enterprise skills" }
  - { number: "2.17", order: 55, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "working with PSRBs: BPS and HCPC" }
  - { number: "2.18", order: 56, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and review against external reference points" }
  - { number: "2.19", order: 57, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external review" }
  - { number: "2.20", order: 58, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and their use of the statement" }
  - { number: "2.21", order: 59, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "BPS accreditation and chartered membership (repeats 1.4)" }
  - { number: "3.1", order: 61, componentType: paragraph, parent: "section 3", heading: "Subject knowledge and understanding", gloss: "the core areas, with example topics that are neither prescriptive nor exhaustive" }
  - { number: "3.2", order: 62, componentType: paragraph, parent: "section 3", heading: "Subject knowledge and understanding", gloss: "delivery of core areas, and their ethical issues" }
  - { number: "3.3", order: 63, componentType: paragraph, parent: "section 3", heading: "Subject knowledge and understanding", gloss: "links between areas; multiple perspectives; limits of Western samples" }
  - { number: "3.4", order: 64, componentType: area, parent: "section 3", heading: "Subject knowledge and understanding", gloss: "applications of theory; the five core areas with example topics (SB3)" }
  - { number: "3.5", order: 65, componentType: paragraph, parent: "section 3", heading: "Conceptual and historical issues in psychology and interdisciplinarity", gloss: "conceptual and historical issues and interdisciplinarity" }
  - { number: "3.6", order: 66, componentType: paragraph, parent: "section 3", heading: "Methods of research and enquiry", gloss: "rigour in research design and methods; progressive empirical work" }
  - { number: "3.7", order: 67, componentType: paragraph, parent: "section 3", heading: "Methods of research and enquiry", gloss: "quantitative and qualitative skills" }
  - { number: "3.8", order: 68, componentType: paragraph, parent: "section 3", heading: "Methods of research and enquiry", gloss: "context, inclusion and ethics in research; reflexivity" }
  - { number: "3.9", order: 69, componentType: paragraph, parent: "section 3", heading: "Methods of research and enquiry", gloss: "research approaches by core area" }
  - { number: "3.10", order: 70, componentType: paragraph, parent: "section 3", heading: "Methods of research and enquiry", gloss: "ethical data collection, open science, specialist methods training" }
  - { number: "3.11", order: 71, componentType: paragraph, parent: "section 3", heading: "Methods of research and enquiry", gloss: "research reports culminating in an empirical project (S4)" }
  - { number: "3.12", order: 72, componentType: paragraph, parent: "section 3", heading: "Skills", gloss: "attributes drawn from the sciences and humanities" }
  - { number: "3.13", order: 73, componentType: paragraph, parent: "section 3", heading: "Skills", gloss: "transferable skills grounded in psychological knowledge" }
  - { number: "3.14", order: 74, componentType: paragraph, parent: "section 3", heading: "Skills", gloss: "subject-specific and transferable skills distinguished" }
  - { number: "3.15", order: 75, componentType: paragraph, parent: "section 3", heading: "Skills", gloss: "skills and employability" }
  - { number: "3.16", order: 76, componentType: stem, parent: "section 3", heading: "Subject-specific skills", gloss: "lead-in: the subject-specific skills of honours and conversion graduates (S4, 15 items)" }
  - { number: "3.17", order: 77, componentType: stem, parent: "section 3", heading: "Transferable skills", gloss: "lead-in: the transferable skills of graduates (S4, 11 items)" }
  - { number: "3.18", order: 78, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "what the degree covers, with emphasis on empirical research" }
  - { number: "3.19", order: 79, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "fitness of teaching and assessment methods; co-creation" }
  - { number: "3.20", order: 80, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "student-centred and varied delivery" }
  - { number: "3.21", order: 81, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "ethical principles across contexts, following BPS guidance" }
  - { number: "3.22", order: 82, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "awareness of the expectations of PSRBs" }
  - { number: "3.23", order: 83, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "progression from supported to independent study" }
  - { number: "3.24", order: 84, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "practical work across methodologies" }
  - { number: "3.25", order: 85, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "lead-in: forms of learning and teaching, listed (SB3)" }
  - { number: "3.26", order: 86, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "further good-practice approaches to learning" }
  - { number: "3.27", order: 87, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "professional development for all teaching staff" }
  - { number: "3.28", order: 88, componentType: paragraph, parent: "section 3", heading: "Assessment and feedback", gloss: "purpose of assessment and feedback" }
  - { number: "3.29", order: 89, componentType: paragraph, parent: "section 3", heading: "Assessment and feedback", gloss: "a coherent assessment and feedback strategy" }
  - { number: "3.30", order: 90, componentType: paragraph, parent: "section 3", heading: "Assessment and feedback", gloss: "a range of assessment methods for EDI; authentic assessment" }
  - { number: "3.31", order: 91, componentType: paragraph, parent: "section 3", heading: "Assessment and feedback", gloss: "assessment criteria; co-developed assessment; integrity and AI" }
  - { number: "3.32", order: 92, componentType: paragraph, parent: "section 3", heading: "Assessment and feedback", gloss: "assessment for self-monitoring and skills development" }
  - { number: "4.1", order: 94, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the statement sets minimum threshold standards for honours and master's conversion degrees" }
  - { number: "4.2", order: 95, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "four categories of achievement; the classification annex (QAA 2019, Annex D) as a reference" }
  - { number: "4.5", order: 96, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "assessment against outcomes; framework levels; conversion courses at FHEQ 7 or FQHEIS 11 (S4)" }
  - { number: "4.6", order: 97, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "lead-in: the four bases on which typical and excellent go beyond threshold (SB4)" }
  - { number: "4.7", order: 98, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "subject criteria accompany the annex; providers interpret them; uneven achievement across categories" }
  - { number: "4.8", order: 99, componentType: stem, parent: "section 4", heading: "Threshold", gloss: "lead-in: the threshold rung (S4, 9 items)" }
  - { number: "4.9", order: 100, componentType: stem, parent: "section 4", heading: "Typical", gloss: "lead-in: the typical rung (S4, 9 items)" }
  - { number: "4.10", order: 101, componentType: stem, parent: "section 4", heading: "Excellent", gloss: "lead-in: the excellent rung, \"consistently\" (S4, 9 items)" }
  - { number: "4.11", order: 102, componentType: paragraph, parent: "section 4", heading: "Postgraduate study", gloss: "postgraduate qualifications in the psychological professions" }
  - { number: "4.12", order: 103, componentType: paragraph, parent: "section 4", heading: "Postgraduate study", gloss: "Stage One and Stage Two professional training" }
  - { number: "4.13", order: 104, componentType: paragraph, parent: "section 4", heading: "Award nomenclature", gloss: "postgraduate award titles; provider duty on protected titles (S4)" }
  - { number: "4.14", order: 105, componentType: paragraph, parent: "section 4", heading: "Award nomenclature", gloss: "wider workforce routes and professional registers" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Psychology Degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Psychology degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: none, heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1 and S2" }
  - { number: none, heading: Contents, kind: contents }
  - { number: "5", heading: List of references and further resources, kind: references }
  - { number: "6", heading: Membership of the Advisory Group, kind: acknowledgements }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 61 records. The issuer's words are each record's span; never copied here. -->
```yaml
- id: qaa/psychology-2023/1.6
  locator: { number: "1.6", headingPath: ["Context and purposes of a Psychology Degree", "Purposes of a Psychology degree"] }
  span: { start: 12508, end: 13164 }
  source: "1.6 To become a practitioner psychologist - that is, someone who can formally call themselves a practising psychologist - further postgraduate study and supervised training are required. By law (Health Professions Order 2001), anyone using one of the nine protected registered psychologist titles must be registered with the HCPC and have successfully completed an HCPC-approved course of training. The protected titles are: Clinical Psychologist; Counselling Psychologist; Educational Psychologist; Forensic Psychologist; Health Psychologist; Occupational Psychologist; Practitioner Psychologist; Registered Psychologist; Sport and Exercise Psychologist.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "anyone seeking to practise as a psychologist"
  addressee: learner
  verbs: [registered, completed]
  about: "protected practitioner psychologist titles"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Practising as a psychologist needs postgraduate study and supervised training beyond the degree; by law anyone using one of the nine protected practitioner titles must be on the HCPC register and have finished an HCPC-approved training course."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of a Psychology Degree", "Equality, diversity and inclusion"] }
  span: { start: 18417, end: 18988 }
  source: "1.18 Equality can be achieved by designing and creating learning, teaching and assessment experiences that promote equality of opportunity and eliminate discrimination, across all stages of the student journey. It can also be achieved by challenging inappropriate and inaccurate narratives about the 'psychological' world that continue to be reproduced. In achieving this it is expected that future graduates of Psychology will value and incorporate equality, diversity and inclusivity into their personal and professional lives, contributing to a socially just society.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: [value, incorporate]
  about: "equality, diversity and inclusion in personal and professional life"
  themes: [theme:edi]
  domain: generic-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Equality is advanced by learning, teaching and assessment that widen opportunity, remove discrimination and question inaccurate accounts of people; graduates are expected to value equality, diversity and inclusion and carry them into their lives and work."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of a Psychology Degree", "Accessibility"] }
  span: { start: 21866, end: 22241 }
  source: "1.24 The Equality Act 2010 places a legal duty on education providers to adopt a proactive rather than reactive approach, where issues of accessibility of teaching, learning, assessment and the wider student experience are anticipated for disabled students. Consideration of accessibility must be considered in course design as well as planning the wider student experience.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "course design and the wider student experience"
  addressee: provider
  verbs: [considered, anticipated]
  about: "anticipating accessibility for disabled students"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The Equality Act 2010 requires providers to anticipate the accessibility needs of disabled students across teaching, learning, assessment and student life, and accessibility must be considered when courses are designed."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/psychology-2023/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of a Psychology degree", "Design"] }
  span: { start: 30423, end: 30854 }
  source: "2.5 At the core of the discipline is ethical understanding and ethical behaviour and this is often at the heart of course design. For example, there will be a range of activities that will facilitate the comprehensive application of ethics in research, professional practice and everyday conduct. Students will be able to apply this to their own ethical behaviour as well as critically evaluating the ethical behaviour of others.\n\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: [apply, evaluating]
  about: "ethical understanding and behaviour"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Ethics sits at the core of the discipline and of course design, with activities that apply it to research, practice and daily conduct; students will be able to apply ethics to their own behaviour and judge the ethical conduct of others critically."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of a Psychology degree", "Progression"] }
  span: { start: 32187, end: 32899 }
  source: "2.8 Students may also study Psychology as a conversion degree at postgraduate level. Upon graduation from an undergraduate degree, it would be expected that a student who had achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in Psychology or an associated discipline. For some postgraduate study there is a requirement for students to have passed a BPS-accredited Psychology degree. Students must gain a second-class degree or higher and pass the empirical project, or an accredited conversion course, with a pass mark of 50% or equivalent\n- for example, a second-class degree or merit - to gain the Graduate Basis for Chartered Member (GBC) of BPS.\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "students seeking Graduate Basis for Chartered Membership"
  addressee: learner
  verbs: [gain, pass]
  about: "the professional body route to chartered membership"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A second-class degree or above usually fits a graduate for postgraduate study; to gain the professional body's Graduate Basis for Chartered Membership, a student must achieve at least a second-class degree and pass the empirical project, or pass an accredited conversion course at 50% or equivalent."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.11
  locator: { number: "3.11", headingPath: ["Content, structure and delivery", "Methods of research and enquiry"] }
  span: { start: 45813, end: 46222 }
  source: "3.11 A graduate of Psychology will have successfully completed a series of research reports throughout their course, culminating in an empirical project or equivalent reporting on a substantial piece of research. The project involves the collection of original quantitative, qualitative or mixed methods data, or equivalent alternatives such as computational modelling or secondary data analysis.\n\n15\n\nSkills\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: [completed, culminating, reporting]
  about: "research reports and the empirical project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will have written a series of research reports through the course, ending in an empirical project (or equivalent) that reports a substantial piece of research collecting original data or using an accepted alternative such as modelling or secondary analysis."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b1
  locator: { number: "3.16.b1", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 48226, end: 48310 }
  source: "understand the conceptual and historical underpinnings of psychology as a discipline"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [understand]
  about: "conceptual and historical foundations"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to understand the ideas and history on which psychology as a discipline rests."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b2
  locator: { number: "3.16.b2", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 48313, end: 48499 }
  source: "apply multiple perspectives to psychological issues, recognising that psychology involves a range of methods of research and enquiry, theories, evidence, interpretations and applications"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [apply, recognising]
  about: "multiple perspectives on psychological issues"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to bring several perspectives to bear on psychological questions, aware that the discipline uses many methods, theories, kinds of evidence, readings and applications."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b3
  locator: { number: "3.16.b3", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 48502, end: 48682 }
  source: "integrate ideas and findings across multiple perspectives and approaches in psychology and apply psychological knowledge ethically, professionally and safely to real-world problems"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [integrate, apply]
  about: "integrating findings and applying knowledge ethically"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to bring together ideas and findings from different approaches, and use psychological knowledge on real problems in ways that are ethical, professional and safe."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b4
  locator: { number: "3.16.b4", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 48685, end: 48793 }
  source: "identify, contextualise and evaluate diverse patterns in behaviour, psychological functioning and experience"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [identify, contextualise, evaluate]
  about: "patterns in behaviour and experience"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to recognise, place in context and judge the varied patterns found in behaviour, mental functioning and experience."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b5
  locator: { number: "3.16.b5", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 48796, end: 48903 }
  source: "apply critical-thinking skills to address complex problems to identifying creative and innovative solutions"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [apply, address, identifying]
  about: "critical thinking for complex problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to use critical thinking on complex problems to find creative and innovative answers."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b6
  locator: { number: "3.16.b6", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 48906, end: 49079 }
  source: "generate and explore appropriate psychological hypotheses and research questions, drawing on relevant theory, research and practice, design studies and collect original data"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [generate, explore, design, collect]
  about: "hypotheses, research questions and original data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to form and examine suitable hypotheses and research questions grounded in theory, research and practice, then design studies and gather original data."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b7
  locator: { number: "3.16.b7", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 49082, end: 49260 }
  source: "apply a variety of methods of inquiry, such as experiments, observation, questionnaires, psychometric tests, interviews, focus groups, creative methods or secondary data analysis"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [apply]
  about: "a range of methods of inquiry"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to use varied methods of inquiry, from experiments and observation to interviews and focus groups, questionnaires and psychometric testing, creative approaches or analysis of existing data."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b8
  locator: { number: "3.16.b8", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 49263, end: 49404 }
  source: "understand and appreciate the value of participatory and/or action research and user involvement in research and community, and peer research"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [understand, appreciate]
  about: "participatory, action and peer research"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to understand and value participatory or action research, the involvement of users, and community and peer research."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b9
  locator: { number: "3.16.b9", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 49407, end: 49521 }
  source: "analyse, present and evaluate quantitative, qualitative data and mixed methods data and critique research findings"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [analyse, present, evaluate, critique]
  about: "analysing data and critiquing findings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to analyse, present and assess quantitative, qualitative and mixed-methods data, and critique the findings of research."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b10
  locator: { number: "3.16.b10", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 49529, end: 49652 }
  source: "the ability to manage, synthesise and evaluate potentially conflicting sources such as primary research studies or theories"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [manage, synthesise, evaluate]
  about: "handling conflicting sources"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to manage, combine and judge sources that may conflict, such as primary studies or rival theories."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b11
  locator: { number: "3.16.b11", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 49655, end: 49807 }
  source: "employ evidence-based reasoning and examine practical, theoretical and ethical issues associated with a range of methods of inquiry and other activities"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [employ, examine]
  about: "evidence-based reasoning and the issues of inquiry"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to reason from evidence and examine the practical, theoretical and ethical questions raised by methods of inquiry and other activities."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b12
  locator: { number: "3.16.b12", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 49810, end: 49941 }
  source: "use and critique a variety of psychological tools, including specialist software, laboratory equipment and psychometric instruments"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [use, critique]
  about: "psychological tools and instruments"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to use and critically assess psychological tools, such as specialist software, laboratory equipment and psychometric instruments."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b13
  locator: { number: "3.16.b13", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 49944, end: 50014 }
  source: "critically and reflectively evaluate psychological theory and research"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [evaluate]
  about: "critical evaluation of theory and research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to assess psychological theory and research critically and reflectively."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b14
  locator: { number: "3.16.b14", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 50017, end: 50138 }
  source: "understand and apply the process of theory development and be capable of developing theory driven psychological questions"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [understand, apply, developing]
  about: "theory development"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to understand how theory is developed, apply that process, and frame psychological questions driven by theory."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.16.b15
  locator: { number: "3.16.b15", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 50141, end: 50418 }
  source: "carry out an extensive independent piece of empirical research that requires students individually to demonstrate a range of research skills, including designing and planning, considering and resolving ethical issues, analysis and dissemination of findings. Transferable skills"
  stem: "3.16"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and conversion graduates"
  addressee: learner
  verbs: [carry, demonstrate, designing, planning, resolving]
  about: "the independent empirical project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to complete a substantial independent empirical study that shows, for each student, research skills from design and planning, through ethical questions, to analysis and dissemination."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.17.b1
  locator: { number: "3.17.b1", headingPath: ["Content, structure and delivery", "Transferable skills"] }
  span: { start: 50492, end: 50565 }
  source: "communicate effectively using a range of verbal and/or non-verbal methods"
  stem: "3.17"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: [communicate]
  about: "effective communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to communicate well by verbal and non-verbal means."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.17.b2
  locator: { number: "3.17.b2", headingPath: ["Content, structure and delivery", "Transferable skills"] }
  span: { start: 50568, end: 50708 }
  source: "interact professionally with others, respond inclusively in a manner sensitive to the needs and expectations of a diverse range of audiences"
  stem: "3.17"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: [interact, respond]
  about: "professional and inclusive interaction"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to deal with others professionally and respond inclusively, attentive to the needs and expectations of varied audiences."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.17.b3
  locator: { number: "3.17.b3", headingPath: ["Content, structure and delivery", "Transferable skills"] }
  span: { start: 50711, end: 50826 }
  source: "demonstrate numerical reasoning skills including the analysis, presentation and interpretation of quantitative data"
  stem: "3.17"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: [demonstrate]
  about: "numerical reasoning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to show numerical reasoning, including analysing, presenting and interpreting quantitative data."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.17.b4
  locator: { number: "3.17.b4", headingPath: ["Content, structure and delivery", "Transferable skills"] }
  span: { start: 50829, end: 50903 }
  source: "demonstrate the ability to analyse, interpret and present qualitative data"
  stem: "3.17"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: [demonstrate, analyse, interpret, present]
  about: "qualitative data skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to show that one can analyse, interpret and present qualitative data."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.17.b5
  locator: { number: "3.17.b5", headingPath: ["Content, structure and delivery", "Transferable skills"] }
  span: { start: 50906, end: 51057 }
  source: "demonstrate digital literacy through the use of online databases and analytic software, and digital approaches to personal and professional development"
  stem: "3.17"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: [demonstrate]
  about: "digital literacy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to show digital literacy by using online databases, analysis software and digital tools for personal and professional development."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.17.b6
  locator: { number: "3.17.b6", headingPath: ["Content, structure and delivery", "Transferable skills"] }
  span: { start: 51060, end: 51198 }
  source: "understand the function and role of artificial intelligence in the context of learning and teaching, problem-solving and working practices"
  stem: "3.17"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: [understand]
  about: "artificial intelligence in learning and work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to understand what artificial intelligence does and its role in learning, teaching, problem-solving and working practice."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.17.b7
  locator: { number: "3.17.b7", headingPath: ["Content, structure and delivery", "Transferable skills"] }
  span: { start: 51201, end: 51386 }
  source: "understand the ethical, practical and legal issues associated with the collection, management, storage, processing, sharing and presentation of information, including in digital formats"
  stem: "3.17"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: [understand]
  about: "information ethics and handling"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to understand the ethical, practical and legal questions in collecting, managing, storing, processing, sharing and presenting information, digital information included."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.17.b8
  locator: { number: "3.17.b8", headingPath: ["Content, structure and delivery", "Transferable skills"] }
  span: { start: 51389, end: 51651 }
  source: "retrieve and organise information found in a range of sources (for example, academic books, policy documents and non-academic sources) while recognising the different perspectives and influences that amplify or marginalise certain forms of knowledge and evidence"
  stem: "3.17"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: [retrieve, organise, recognising]
  about: "finding information and recognising whose knowledge counts"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to find and organise information from varied sources, academic and non-academic, while recognising the perspectives and influences that raise up or push aside some kinds of knowledge and evidence."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.17.b9
  locator: { number: "3.17.b9", headingPath: ["Content, structure and delivery", "Transferable skills"] }
  span: { start: 51654, end: 51811 }
  source: "demonstrate inclusive and collaborative working and reflect on the value of engagement with a variety of views in reaching consensus in solutions to problems"
  stem: "3.17"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: [demonstrate, reflect]
  about: "inclusive collaboration and consensus"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to work inclusively and collaboratively, and reflect on the worth of engaging with differing views when reaching agreed solutions."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.17.b10
  locator: { number: "3.17.b10", headingPath: ["Content, structure and delivery", "Transferable skills"] }
  span: { start: 51814, end: 51924 }
  source: "reflect on and articulate personal strengths and areas for development and identify how these may be addressed"
  stem: "3.17"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: [reflect, articulate, identify]
  about: "self-assessment and development"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to reflect on and explain one's own strengths and areas to develop, and how to address them."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/3.17.b11
  locator: { number: "3.17.b11", headingPath: ["Content, structure and delivery", "Transferable skills"] }
  span: { start: 51927, end: 52087 }
  source: "take ownership for one's own learning, employability and development, including effective personal planning and project management skills. Teaching and learning"
  stem: "3.17"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: [take]
  about: "ownership of learning and employability"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's conversion"]
  gradeOf: none
  paraphrase: "Will be able to take charge of one's own learning, employability and development, including personal planning and project management."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.5
  locator: { number: "4.5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58067, end: 58866 }
  source: "4.5 Students will undertake a variety of assessments matched against the learning outcomes for their particular curricula of study. This allows them to achieve the standard required and to develop and demonstrate characteristics associated with higher levels of learning within a bachelor's degree with honours. At the base level, the classification means that students will have achieved the characteristics of Level 6 in England, Wales and Northern Ireland, and Level 10 in Scotland of the respective qualification. The standards also provide a reference point for setting and maintaining academic standards for Psychology conversion courses at Level 7 (FHEQ) or 11 (FQHEIS), although outcomes for these courses must ultimately align with the appropriate levels on the Qualifications Frameworks.\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "conversion courses"
  addressee: provider
  verbs: [align]
  about: "conversion course outcomes and framework levels"
  themes: [none]
  domain: none
  award: ["master's conversion"]
  gradeOf: none
  paraphrase: "Assessments matched to learning outcomes let students reach the standard; the base classification corresponds to framework level 6 (FHEQ, outside Scotland) or level 10 (FQHEIS, Scotland); the standards guide conversion courses at FHEQ level 7 or FQHEIS level 11, whose outcomes must ultimately align with the right framework levels."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/psychology-2023/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Threshold"] }
  span: { start: 60242, end: 60329 }
  source: "identified the core areas of psychology and the contexts in which they might be applied"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: [identified]
  about: "core areas and their applications"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have named the core areas of psychology and the settings where each can be applied."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Threshold"] }
  span: { start: 60332, end: 60398 }
  source: "systematically reviewed and evaluated key psychological literature"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: [reviewed, evaluated]
  about: "reviewing the literature"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have reviewed and assessed the key psychological literature systematically."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Threshold"] }
  span: { start: 60406, end: 60528 }
  source: "understood the interrelatedness of different areas of psychology and compared different perspectives within the discipline"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: [understood, compared]
  about: "links between areas and perspectives"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have understood how the areas of psychology relate and compared the perspectives within it."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Threshold"] }
  span: { start: 60531, end: 60600 }
  source: "appreciated the role of evidence in forming conclusions in psychology"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: [appreciated]
  about: "the role of evidence"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have grasped the part evidence plays in reaching conclusions in psychology."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Threshold"] }
  span: { start: 60603, end: 60760 }
  source: "understood the principles and protocols required for conducting psychological investigations, and applied relevant legal, ethical and professional guidelines"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: [understood, applied]
  about: "research principles, protocols and guidelines"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have understood the principles and protocols of psychological investigation and followed the relevant legal, ethical and professional guidance."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.8.b6
  locator: { number: "4.8.b6", headingPath: ["Benchmark standards", "Threshold"] }
  span: { start: 60763, end: 60913 }
  source: "constructed and tested research hypotheses and undertaken supervised research investigating specific lines of enquiry, both individually and in groups"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: [constructed, tested, undertaken]
  about: "hypotheses and supervised research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have formed and tested hypotheses and carried out supervised research on defined questions, alone and in groups."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.8.b7
  locator: { number: "4.8.b7", headingPath: ["Benchmark standards", "Threshold"] }
  span: { start: 60916, end: 61061 }
  source: "summarised research findings emerging from the application of quantitative and qualitative methods and understood their contribution to knowledge"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: [summarised, understood]
  about: "summarising findings from quantitative and qualitative methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have summarised findings from quantitative and qualitative methods and understood what they add to knowledge."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.8.b8
  locator: { number: "4.8.b8", headingPath: ["Benchmark standards", "Threshold"] }
  span: { start: 61064, end: 61137 }
  source: "used appropriate hardware and software for learning and research purposes"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: [used]
  about: "hardware and software for learning and research"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have used suitable hardware and software for study and research."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.8.b9
  locator: { number: "4.8.b9", headingPath: ["Benchmark standards", "Threshold"] }
  span: { start: 61140, end: 61229 }
  source: "communicated psychological knowledge and research findings in a range of formats. Typical"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: [communicated]
  about: "communicating knowledge and findings"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have conveyed psychological knowledge and findings in several formats."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.9.b1
  locator: { number: "4.9.b1", headingPath: ["Benchmark standards", "Typical"] }
  span: { start: 61308, end: 61418 }
  source: "understood the breadth of psychology and its potential for impact across a wide range of real-world challenges"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: [understood]
  about: "breadth of the discipline and its impact"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.8.b1, basis: inferred }
  paraphrase: "Will have understood how wide psychology is and how it can make a difference to many real problems."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.9.b2
  locator: { number: "4.9.b2", headingPath: ["Benchmark standards", "Typical"] }
  span: { start: 61421, end: 61585 }
  source: "conducted in-depth reviews of psychological literature, reflected on historical concepts and theories in psychology, and explored ramifications for current thinking"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: [conducted, reflected, explored]
  about: "in-depth literature review and history of ideas"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.8.b2, basis: inferred }
  paraphrase: "Will have reviewed the literature in depth, reflected on historical concepts and theories, and traced what they mean for thinking now."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.9.b3
  locator: { number: "4.9.b3", headingPath: ["Benchmark standards", "Typical"] }
  span: { start: 61588, end: 61726 }
  source: "adopted multiple perspectives in psychology and systematically analysed research paradigms, methods of enquiry, and measurement techniques"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: [adopted, analysed]
  about: "multiple perspectives and research paradigms"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.8.b3, basis: inferred }
  paraphrase: "Will have taken several perspectives and analysed research paradigms, methods and measures systematically."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.9.b4
  locator: { number: "4.9.b4", headingPath: ["Benchmark standards", "Typical"] }
  span: { start: 61729, end: 61828 }
  source: "reflected on the role of evidence in forming conclusions and reasoning scientifically in psychology"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: [reflected]
  about: "evidence and scientific reasoning"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.8.b4, basis: inferred }
  paraphrase: "Will have reflected on how evidence supports conclusions and on scientific reasoning in psychology."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.9.b5
  locator: { number: "4.9.b5", headingPath: ["Benchmark standards", "Typical"] }
  span: { start: 61831, end: 61968 }
  source: "posed and critiqued research questions leading to the demonstration of competence in a wide range of quantitative and qualitative methods"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: [posed, critiqued]
  about: "research questions and competence across methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.8.b5, basis: inferred }
  paraphrase: "Will have set and critiqued research questions in a way that shows competence in many quantitative and qualitative methods."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.9.b6
  locator: { number: "4.9.b6", headingPath: ["Benchmark standards", "Typical"] }
  span: { start: 61971, end: 62085 }
  source: "initiated and completed psychological enquiries, recognising theoretical, practical and methodological limitations"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: [initiated, completed, recognising]
  about: "self-started enquiries and their limits"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.8.b6, basis: inferred }
  paraphrase: "Will have started and finished psychological enquiries while recognising their theoretical, practical and methodological limits."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.9.b7
  locator: { number: "4.9.b7", headingPath: ["Benchmark standards", "Typical"] }
  span: { start: 62088, end: 62297 }
  source: "drawn conclusions from research findings, including evaluating their psychological significance, accounting for the diverse nature of individual experience, and making recommendations for further investigation"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: [drawn, evaluating, accounting, making]
  about: "conclusions, significance and further research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.8.b7, basis: inferred }
  paraphrase: "Will have drawn conclusions from findings, judging their psychological importance, allowing for the diversity of individual experience and proposing further research."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.9.b8
  locator: { number: "4.9.b8", headingPath: ["Benchmark standards", "Typical"] }
  span: { start: 62300, end: 62454 }
  source: "understood the implications and consequences of using different subject-relevant hardware and software, and of adopting different theoretical perspectives"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: [understood]
  about: "consequences of tools and theoretical choices"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.8.b8, basis: inferred }
  paraphrase: "Will have understood what follows from using different subject hardware and software and from taking different theoretical positions."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.9.b9
  locator: { number: "4.9.b9", headingPath: ["Benchmark standards", "Typical"] }
  span: { start: 62457, end: 62611 }
  source: "disseminated psychological research findings to peers and academic supervisors, tailoring communication according to different audiences' needs. Excellent"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: [disseminated, tailoring]
  about: "communicating findings to different audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.8.b9, basis: inferred }
  paraphrase: "Will have shared research findings with peers and supervisors, adapting communication to what each audience needs."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.10.b1
  locator: { number: "4.10.b1", headingPath: ["Benchmark standards", "Excellent"] }
  span: { start: 62706, end: 62865 }
  source: "demonstrated the ability to engage in precise technical discussion about the nature of psychology, pointing to potential misinterpretation or misunderstandings"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: [demonstrated, engage, pointing]
  about: "precise technical discussion of the discipline"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.9.b1, basis: inferred }
  paraphrase: "Will consistently have shown precise technical discussion of the nature of psychology, picking out possible misreadings."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.10.b2
  locator: { number: "4.10.b2", headingPath: ["Benchmark standards", "Excellent"] }
  span: { start: 62868, end: 63076 }
  source: "engaged in original theoretical and practical reviews of psychological knowledge, and identified the limits of psychological understanding, including challenging myths and offering alternative interpretations"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: [engaged, identified, challenging, offering]
  about: "original reviews and the limits of understanding"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.9.b2, basis: inferred }
  paraphrase: "Will consistently have produced original theoretical and practical reviews, found where psychological understanding runs out, challenged myths and offered other readings."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.10.b3
  locator: { number: "4.10.b3", headingPath: ["Benchmark standards", "Excellent"] }
  span: { start: 63079, end: 63276 }
  source: "interpreted a wide range of evidence within and across psychology sub-specialisms and related disciplines, making significant connections and showing comprehensive applications of subject knowledge"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: [interpreted, making, showing]
  about: "interpreting evidence across sub-specialisms"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.9.b3, basis: inferred }
  paraphrase: "Will consistently have interpreted a wide range of evidence within and beyond psychology's sub-specialisms, making significant connections and applying knowledge comprehensively."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.10.b4
  locator: { number: "4.10.b4", headingPath: ["Benchmark standards", "Excellent"] }
  span: { start: 63279, end: 63440 }
  source: "demonstrated the use of critical-thinking skills and the ability to evaluate the rigour and significance of evidence when forming novel conclusions in psychology"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: [demonstrated, evaluate, forming]
  about: "critical evaluation of evidence for novel conclusions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.9.b4, basis: inferred }
  paraphrase: "Will consistently have shown critical thinking and judged the rigour and weight of evidence in reaching new conclusions."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.10.b5
  locator: { number: "4.10.b5", headingPath: ["Benchmark standards", "Excellent"] }
  span: { start: 63443, end: 63529 }
  source: "articulated complex psychological arguments and concepts in coherent and balanced ways"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: [articulated]
  about: "articulating complex arguments"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.9.b5, basis: inferred }
  paraphrase: "Will consistently have expressed complex arguments and concepts clearly and even-handedly."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.10.b6
  locator: { number: "4.10.b6", headingPath: ["Benchmark standards", "Excellent"] }
  span: { start: 63537, end: 63657 }
  source: "demonstrated creative thinking when designing psychological research with relevance to contemporary psychological issues"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: [demonstrated, designing]
  about: "creative research design"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.9.b6, basis: inferred }
  paraphrase: "Will consistently have designed research creatively, relevant to current psychological issues."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.10.b7
  locator: { number: "4.10.b7", headingPath: ["Benchmark standards", "Excellent"] }
  span: { start: 63660, end: 63814 }
  source: "reflected on the significance of historical and contemporary findings within psychology when applied to social, political and ethical debates and policies"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: [reflected, applied]
  about: "findings in social, political and ethical debate"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.9.b7, basis: inferred }
  paraphrase: "Will consistently have reflected on what historical and current findings mean when brought to social, political and ethical debates and policy."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.10.b8
  locator: { number: "4.10.b8", headingPath: ["Benchmark standards", "Excellent"] }
  span: { start: 63817, end: 64006 }
  source: "understood the importance of personal and professional skills and gained transferable employability skills - for example, mastery of specific hardware and software and analytical capability"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: [understood, gained]
  about: "personal, professional and employability skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.9.b8, basis: inferred }
  paraphrase: "Will consistently have understood the value of personal and professional skills and acquired transferable employability skills, such as command of particular hardware and software and analytical ability."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.10.b9
  locator: { number: "4.10.b9", headingPath: ["Benchmark standards", "Excellent"] }
  span: { start: 64009, end: 64173 }
  source: "imparted to peers, tutors, supervisors and mixed audiences a comprehensive grasp of psychology as it informs popular debates and decision making. Postgraduate study"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: [imparted]
  about: "conveying a comprehensive grasp to varied audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/psychology-2023/4.9.b9, basis: inferred }
  paraphrase: "Will consistently have conveyed to peers, tutors, supervisors and mixed audiences a full grasp of how psychology informs public debate and decisions."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/psychology-2023/4.13
  locator: { number: "4.13", headingPath: ["Benchmark standards", "Award nomenclature"] }
  span: { start: 65011, end: 65731 }
  source: "4.13 It is important that all postgraduate study in Psychology accurately reflects the level of students/trainees' achievements, represents appropriately the nature of the field(s) of study undertaken and is not misleading, either to potential employers or to the general public. Hence, postgraduate study in specific domains of Psychology reflects the discipline of study in the course title. Furthermore, the course provider must ensure that students are made aware that the psychological professions regulated by the HCPC have one or more designated titles that are protected by law and professionals must be registered to use them. More information regarding the protected titles is available on the HCPC website .\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "postgraduate courses"
  addressee: provider
  verbs: [ensure, registered]
  about: "award titles and protected titles"
  themes: [none]
  domain: none
  award: ["postgraduate"]
  gradeOf: none
  paraphrase: "It matters that postgraduate award titles reflect achievement and the field studied truthfully; the course provider must make sure students know that HCPC-regulated professions have titles protected by law that only registrants may use."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. Light rewrites keep the issuer's structure in our words; full rewrites recast it. -->
```yaml
- statement: qaa/psychology-2023/1.6
  forPractitioner: { text: "An undergraduate or conversion degree does not by itself lead to a protected title: anyone using one of the nine practitioner psychologist titles (Health Professions Order 2001) must be an HCPC registrant who has completed approved training.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you want to work as a practitioner psychologist (clinical, forensic, educational and others), you must first complete further postgraduate study and supervised training and register with the professional regulator: the titles are protected by law.", rewrite: full, force: must, status: drafted }
- statement: qaa/psychology-2023/1.18
  forPractitioner: { text: "Learning, teaching and assessment that widen opportunity and challenge biased narratives in the discipline are the means; the expected result is that graduates will value equality, diversity and inclusion and act on them in their personal and professional lives.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will come to value equality, diversity and inclusion and build them into how you live and work, helping to make society fairer.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/1.24
  forPractitioner: { text: "Build accessibility in from the start: under the Equality Act 2010 you must consider disabled students' needs when designing the course and planning the wider student experience, not only when an adjustment is asked for.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
- statement: qaa/psychology-2023/2.5
  forPractitioner: { text: "Ethics is often at the heart of course design, with activities that bring it into research, practice and daily life; students will be able to act ethically themselves and critically judge the ethics of others.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to apply ethical principles to how you behave in research, in practice and day to day, and to judge critically how ethically others act.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/2.8
  forPractitioner: { text: "For the BPS Graduate Basis for Chartered Membership, students must gain at least a second-class degree and pass the empirical project, or pass an accredited conversion course at 50% (a merit or equivalent).", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you want the first step towards chartered membership of the professional body, you must achieve at least a second-class degree and pass your empirical project on an accredited course, or pass an accredited conversion course with 50% or more.", rewrite: full, force: must, status: drafted }
- statement: qaa/psychology-2023/3.11
  forPractitioner: { text: "Graduates will have completed a sequence of research reports leading to a substantial empirical project in which each collects original quantitative, qualitative or mixed data, or uses an accepted alternative such as computational modelling or secondary data analysis.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will write a series of research reports during your studies, leading up to a substantial project of your own in which you gather and report original data, or work with an accepted alternative such as existing datasets or computer models.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b1
  forPractitioner: { text: "Graduates will understand the conceptual and historical foundations of psychology as a discipline.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand the ideas and history that psychology is built on.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b2
  forPractitioner: { text: "Graduates will apply more than one perspective to psychological issues and recognise the range of methods, theories, evidence, interpretations and applications the discipline uses.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to look at psychological questions from several angles, knowing that psychology uses many methods, theories, kinds of evidence and ways of applying them.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b3
  forPractitioner: { text: "Graduates will integrate ideas and findings across approaches and apply psychological knowledge to real-world problems ethically, professionally and safely.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to combine ideas and findings from different approaches and use what you know about psychology on real problems, ethically, professionally and safely.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b4
  forPractitioner: { text: "Graduates will identify, contextualise and evaluate the diversity of patterns in behaviour, psychological functioning and experience.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to spot, put in context and assess the many patterns in how people behave, think and experience the world.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b5
  forPractitioner: { text: "Graduates will apply critical thinking to complex problems and reach creative, innovative solutions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to think critically about complex problems and come up with creative, new solutions.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b6
  forPractitioner: { text: "Graduates will generate and explore hypotheses and research questions grounded in existing theory, studies and practice, then design their own studies and gather new data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to form your own hypotheses and research questions from theory, research and practice, then design studies and gather new data.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b7
  forPractitioner: { text: "Graduates will apply a range of inquiry methods, experimental and observational, survey and psychometric, interview and focus group, creative, and secondary analysis.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to use many research methods, such as experiments, observation, questionnaires, tests, interviews, focus groups, creative methods or existing datasets.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b8
  forPractitioner: { text: "Graduates will understand and value participatory and action research, user involvement, and community and peer research.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand why research done with people, not only on them, matters: participatory and action research, and research led by users, communities and peers.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b9
  forPractitioner: { text: "Graduates will analyse, present and evaluate quantitative, qualitative and mixed-methods data and critique research findings.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to analyse, present and assess numerical, qualitative and mixed data, and question what research findings show.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b10
  forPractitioner: { text: "Graduates will manage, synthesise and evaluate sources that may conflict, such as primary studies or competing theories.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to handle, combine and weigh up sources that disagree, such as different studies or theories.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b11
  forPractitioner: { text: "Graduates will reason from evidence and examine the practical, theoretical and ethical issues that methods of inquiry and related activities raise.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reason from evidence and think through the practical, theoretical and ethical questions your research methods raise.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b12
  forPractitioner: { text: "Graduates will use and critique the tools of the discipline: specialist software, lab equipment and psychometric instruments.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to use, and judge the limits of, the tools of psychology, such as specialist software, lab equipment and psychometric tests.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b13
  forPractitioner: { text: "Graduates will evaluate psychological theory and research critically and reflectively.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to assess psychological theories and research critically and reflectively.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b14
  forPractitioner: { text: "Graduates will understand and use the process of theory development and can frame theory-driven psychological questions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how theories are built and be able to ask psychological questions that grow out of theory.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.16.b15
  forPractitioner: { text: "Each graduate will complete an extensive independent empirical project demonstrating research skills across design, planning, ethics, analysis and dissemination.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will carry out a substantial research project of your own, showing that you can plan and design it, deal with its ethical questions, analyse the results and share what you found.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.17.b1
  forPractitioner: { text: "Graduates will communicate effectively through a range of verbal and non-verbal means.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to communicate well, in speech and in other ways.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.17.b2
  forPractitioner: { text: "Graduates will interact professionally and respond inclusively, sensitive to the needs and expectations of diverse audiences.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to work with others professionally and respond inclusively to people with different needs and expectations.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.17.b3
  forPractitioner: { text: "Graduates will demonstrate numerical reasoning: analysing, presenting and interpreting quantitative data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reason with numbers and analyse, present and interpret numerical data.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.17.b4
  forPractitioner: { text: "Graduates will demonstrate that they can analyse, interpret and present qualitative data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to analyse, interpret and present qualitative data, such as interviews or text.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.17.b5
  forPractitioner: { text: "Graduates will demonstrate digital literacy: online databases, analysis software and digital tools for their own personal and professional growth.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be confident with digital tools: online databases, analysis software and digital ways of developing yourself personally and professionally.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.17.b6
  forPractitioner: { text: "Graduates will understand what artificial intelligence does and where it fits in learning and teaching, problem-solving and working practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand what artificial intelligence does and how it is used in learning, solving problems and at work.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.17.b7
  forPractitioner: { text: "Graduates will understand the ethical, practical and legal issues across the life of information, from collection to presentation, including in digital formats.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand the ethical, practical and legal rules for collecting, storing, using and sharing information, including digital information.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.17.b8
  forPractitioner: { text: "Graduates will retrieve and organise information from academic, policy and non-academic sources and recognise the influences that amplify or marginalise particular knowledge and evidence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to find and organise information from many kinds of sources and notice whose knowledge and evidence gets heard and whose gets left out.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.17.b9
  forPractitioner: { text: "Graduates will work inclusively and collaboratively and reflect on the value of engaging varied views when reaching consensus on solutions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to work inclusively with others and reflect on why hearing different views helps a group agree on solutions.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.17.b10
  forPractitioner: { text: "Graduates will reflect on and articulate their strengths and development needs and identify how to address them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reflect on and explain your own strengths and what you need to develop, and work out how to do it.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/3.17.b11
  forPractitioner: { text: "Graduates will take ownership of their learning, employability and development, including personal planning and project management.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will take charge of your own learning, career readiness and development, planning your time and managing projects well.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.5
  forPractitioner: { text: "These standards are a reference point for conversion courses, but a conversion course's outcomes must ultimately align with FHEQ level 7 or FQHEIS level 11.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in setting outcome levels", rewrite: full, force: must, status: drafted }
- statement: qaa/psychology-2023/4.8.b1
  forPractitioner: { text: "At threshold, graduates will have named the discipline's core areas and the settings where each applies.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will have identified the main areas of psychology and where each can be used.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.8.b2
  forPractitioner: { text: "At threshold, graduates will have systematically reviewed and evaluated the key literature.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will have worked through and assessed the key research writing in psychology in a systematic way.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.8.b3
  forPractitioner: { text: "At threshold, graduates will have understood how areas of psychology interrelate and compared perspectives within the discipline.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will understand how the areas of psychology connect and be able to compare its different perspectives.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.8.b4
  forPractitioner: { text: "At threshold, graduates will have appreciated the role of evidence in reaching conclusions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will understand why evidence matters when drawing conclusions in psychology.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.8.b5
  forPractitioner: { text: "At threshold, graduates will have understood the principles and protocols of psychological investigation and applied legal, ethical and professional guidelines.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will know the rules and procedures for psychological research and have followed the legal, ethical and professional guidance that applies.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.8.b6
  forPractitioner: { text: "At threshold, graduates will have constructed and tested hypotheses and undertaken supervised research, individually and in groups.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will have built and tested hypotheses and carried out supervised research on set questions, on your own and with others.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.8.b7
  forPractitioner: { text: "At threshold, graduates will have summarised quantitative and qualitative findings and understood their contribution to knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will have summed up results from numerical and qualitative research and understood what they add to what we know.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.8.b8
  forPractitioner: { text: "At threshold, graduates will have used suitable equipment and software in their study and research.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will have used the right equipment and software for your study and research.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.8.b9
  forPractitioner: { text: "At threshold, graduates will have communicated psychological knowledge and findings in a range of formats.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will have shared psychological knowledge and research findings in different formats.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.9.b1
  forPractitioner: { text: "At the typical level, graduates will have grasped how broad psychology is and how it can bear on many real-world challenges.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will understand how broad psychology is and how it can help with many real-world problems.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.9.b2
  forPractitioner: { text: "At the typical level, graduates will have conducted in-depth literature reviews, reflected on historical concepts and theories, and explored their bearing on current thinking.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will have reviewed research in depth, thought about older ideas and theories, and worked out what they mean for today.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.9.b3
  forPractitioner: { text: "At the typical level, graduates will have adopted multiple perspectives and systematically analysed paradigms, methods of enquiry and measurement techniques.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will have looked at psychology from several viewpoints and analysed its research approaches, methods and measures carefully.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.9.b4
  forPractitioner: { text: "At the typical level, graduates will have reflected on the role of evidence and on scientific reasoning.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will have thought carefully about how evidence supports conclusions and how to reason scientifically in psychology.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.9.b5
  forPractitioner: { text: "At the typical level, graduates will have posed and critiqued research questions and shown competence across a wide range of quantitative and qualitative methods.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will have set and questioned research questions and shown you can use many numerical and qualitative methods well.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.9.b6
  forPractitioner: { text: "At the typical level, graduates will have initiated and completed enquiries, recognising their theoretical, practical and methodological limitations.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will have started and finished your own research, aware of its theoretical, practical and method limits.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.9.b7
  forPractitioner: { text: "At the typical level, graduates will have drawn conclusions from findings, weighed their significance with regard to diverse individual experience, and recommended further investigation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will have drawn conclusions from your findings, judged how much they matter, taken account of how differently people experience things, and suggested what to study next.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.9.b8
  forPractitioner: { text: "At the typical level, graduates will have understood the implications of choosing different subject-relevant hardware and software and different theoretical perspectives.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will understand how your choice of equipment, software and theory shapes your work.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.9.b9
  forPractitioner: { text: "At the typical level, graduates will have disseminated findings to peers and supervisors, tailoring communication to each audience.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will have shared your research with fellow students and supervisors, adjusting how you communicate to suit each audience.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.10.b1
  forPractitioner: { text: "At the excellent level, graduates will consistently have discussed the nature of psychology with technical precision and identified likely misinterpretations.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will have consistently discussed what psychology is with technical precision, pointing out where it is often misunderstood.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.10.b2
  forPractitioner: { text: "At the excellent level, graduates will consistently have produced original theoretical and practical reviews, identified the limits of current understanding, challenged myths and offered alternative interpretations.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will have consistently written original reviews of what psychology knows, shown where that knowledge stops, challenged myths and offered other explanations.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.10.b3
  forPractitioner: { text: "At the excellent level, graduates will consistently have interpreted evidence across sub-specialisms and related disciplines, made significant connections and applied knowledge comprehensively.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will have consistently made sense of wide-ranging evidence across areas of psychology and beyond, linking it in significant ways and applying it thoroughly.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.10.b4
  forPractitioner: { text: "At the excellent level, graduates will consistently have shown critical thinking and evaluated the rigour and significance of evidence when reaching novel conclusions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will have consistently thought critically, judging how strong and important evidence is when reaching new conclusions of your own.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.10.b5
  forPractitioner: { text: "At the excellent level, graduates will consistently have articulated complex arguments and concepts coherently and in a balanced way.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will have consistently explained complex arguments and ideas clearly and fairly.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.10.b6
  forPractitioner: { text: "At the excellent level, graduates will consistently have shown creativity in designing research relevant to contemporary issues.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will have consistently designed creative research that speaks to current issues in psychology.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.10.b7
  forPractitioner: { text: "At the excellent level, graduates will consistently have weighed what past and present findings mean for social, political and ethical debate and policy.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will have consistently thought about what past and present findings mean for social, political and ethical debates and policies.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.10.b8
  forPractitioner: { text: "At the excellent level, graduates will consistently have shown they value personal and professional skills and have built transferable employability skills, such as command of particular tools and strong analysis.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will have consistently shown that you value personal and professional skills and built skills employers want, such as mastery of particular tools and strong analysis.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.10.b9
  forPractitioner: { text: "At the excellent level, graduates will consistently have shown peers, staff and wider audiences a full command of how psychology informs public debate and decisions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will have consistently shown fellow students, tutors and wider audiences a thorough grasp of how psychology shapes public debate and decisions.", rewrite: full, force: will, status: drafted }
- statement: qaa/psychology-2023/4.13
  forPractitioner: { text: "It matters that postgraduate titles reflect the field and level honestly; and the provider must make sure students know that HCPC-regulated psychology professions carry legally protected titles open only to registrants.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student-facing point is in 1.6", rewrite: full, force: must, status: drafted }
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: fheq:6, role: cites, locator: "D1, 2.7; 4.5" }
  - { id: fheq:7, role: cites, locator: "D1, 2.10; 4.5" }
  - { id: fqheis:10, role: cites, locator: "D1, 2.7; 4.2; 4.5" }
  - { id: fqheis:11, role: cites, locator: "D1, 2.10; 4.5" }
crosswalks:
  - { from: fheq:6, to: fqheis:10, relation: equivalent, basis: "stated (D1, 2.7; 4.5: honours at level 6 in England, Wales and Northern Ireland, level 10 in Scotland)" }
  - { from: fheq:7, to: fqheis:11, relation: equivalent, basis: "stated (D1, 2.10; 4.5)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: theme:edi, role: carries, carriedIn: ["1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "3.30"] }
- { id: theme:accessibility, role: carries, carriedIn: ["1.24", "1.25", "1.26", "1.27", "2.12", "2.20"] }
- { id: theme:esd, role: carries, carriedIn: ["1.12", "1.28", "1.29", "1.30", "1.31", "1.32"] }
- { id: theme:enterprise, role: carries, carriedIn: ["1.33", "1.34", "1.35", "2.16"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: partOf, target: "collection: QAA Subject Benchmark Statements", note: one of 54 held by stan }
- { rel: supersedes, target: "std:doc:qaa-psychology-<previous year>-benchmarks (not yet ingested)", note: "the front matter names key changes from the previous statement but not its date: Part E" }
- { rel: refersTo, target: "std:doc:qaa-fheq-2024-framework (not yet ingested; run queue S-03), Annex D", note: "the degree classification descriptions for FHEQ level 6 and FQHEIS level 10, cited as QAA 2019 (4.2, 4.6, 4.7)" }
- { rel: refersTo, target: "std:doc:fheq (not yet ingested; S-03)", note: levels 6 and 7 }
- { rel: refersTo, target: "QAA Quality Code, Advice and Guidance", note: front matter }
- { rel: refersTo, target: "BPS accreditation standards (not yet ingested)", note: "1.4, 2.8, 2.21, 3.21" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: 2023-09
lastReviewed: none-stated
reviewCycle: none-stated
consultation: none-stated
replacedBy: none
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: S9 not researched in the pilot (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- A scientific and reflective discipline studying mind, brain, experience, behaviour and socio-cultural context in human and non-human animals, both theoretical and applied, with roots in philosophy, biology and physics (D1, 1.1).
- Its aim is psychological literacy: using disciplinary knowledge and insight on real problems, ethically and critically (D1, 1.2, 2.4).
- Ethics is at its core, in research, practice and conduct (D1, 2.5, 3.21).
- It is empirical: progressive laboratory and naturalistic work across quantitative, qualitative and mixed methods, culminating in an independent project (D1, 3.6, 3.7, 3.11).
- It is evolving and interdisciplinary, and critical of its own historical narrowness of populations and voices (D1, 1.19, 2.6, 3.3, 3.5).
- Professional routes run beyond the degree, through the BPS and the HCPC (D1, 1.4, 1.6).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "the discipline names its own history of marginalising groups and of research on narrow populations; it asks for diverse curricula, inclusive environments, critique of dominant systems of thought and attention to the language of mental health (D1, 1.17 to 1.23)"
  statements: [qaa/psychology-2023/1.18]
- theme: theme:accessibility
  inThisSubject: "the Equality Act's anticipatory duty in course design, reasonable adjustments in every setting and flexible alternative assessment (D1, 1.24 to 1.27); digital and blended delivery to widen access (D1, 2.12)"
  statements: [qaa/psychology-2023/1.24]
- theme: theme:esd
  inThisSubject: "headed Sustainability in the text: psychology's part in the SDGs (naming SDGs 3 to 5, 8, 11 and 16), UNESCO's key competencies as core to the curriculum, behaviour change for climate action, transformative pedagogies (D1, 1.28 to 1.32)"
  statements: []
- theme: theme:enterprise
  inThisSubject: "acknowledged as under-used in the subject; enterprise skills for employability and venture creation, through partnerships and placements (D1, 1.33 to 1.35, 2.16)"
  statements: []
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.4", gloss: "five core areas, each with example topics: biological psychology; cognitive psychology; developmental psychology; individual differences; social psychology" }
  - { component: "3.5", gloss: conceptual and historical issues; interdisciplinarity }
  - { component: "3.6", gloss: methods of research and enquiry, quantitative, qualitative and mixed (3.6 to 3.11) }
practices:
  - { component: "3.25", kind: teaching, gloss: "lectures, laboratory classes, workshops, seminars, tutorials, independent study, collaborative work, project supervision" }
  - { component: "3.26", kind: learning, gloss: "problem-based, team-based, experiential, student-led and work-based learning" }
  - { component: "3.30", kind: assessment, gloss: "a range of methods for EDI, authentic and innovative tasks, assessment for non-academic audiences" }
  - { component: "3.31", kind: assessment, gloss: "clear criteria, co-developed assessment, integrity with AI" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: threshold, leadIn: "4.8", award: "bachelor's with honours", items: 9 }
  - { rung: typical, leadIn: "4.9", award: "bachelor's with honours", items: 9 }
  - { rung: excellent, leadIn: "4.10", award: "bachelor's with honours", items: 9 }
rungBases: "4.6: typical and excellent go beyond threshold on four bases: depth and breadth of knowledge; engagement in research and independent study; critical insight; advanced application of theory and method to current issues"
outcomeLists:
  - { leadIn: "3.16", gloss: subject-specific skills at graduation, items: 15, award: [honours, conversion] }
  - { leadIn: "3.17", gloss: transferable skills at graduation, items: 11, award: [honours, conversion] }
outcomes:
  - { outcome: "core areas and breadth", threshold: qaa/psychology-2023/4.8.b1, typical: qaa/psychology-2023/4.9.b1, excellent: qaa/psychology-2023/4.10.b1, basis: inferred, domain: knowledge, award: "bachelor's with honours" }
  - { outcome: "literature review", threshold: qaa/psychology-2023/4.8.b2, typical: qaa/psychology-2023/4.9.b2, excellent: qaa/psychology-2023/4.10.b2, basis: inferred, domain: subject-skill, award: "bachelor's with honours" }
  - { outcome: "perspectives", threshold: qaa/psychology-2023/4.8.b3, typical: qaa/psychology-2023/4.9.b3, excellent: qaa/psychology-2023/4.10.b3, basis: inferred, domain: understanding, award: "bachelor's with honours" }
  - { outcome: "evidence and reasoning", threshold: qaa/psychology-2023/4.8.b4, typical: qaa/psychology-2023/4.9.b4, excellent: qaa/psychology-2023/4.10.b4, basis: inferred, domain: understanding, award: "bachelor's with honours" }
  - { outcome: "research questions and methods", threshold: qaa/psychology-2023/4.8.b5, typical: qaa/psychology-2023/4.9.b5, excellent: qaa/psychology-2023/4.10.b5, basis: inferred, domain: subject-skill, award: "bachelor's with honours" }  # (weaker content match: Part E)
  - { outcome: "conducting research", threshold: qaa/psychology-2023/4.8.b6, typical: qaa/psychology-2023/4.9.b6, excellent: qaa/psychology-2023/4.10.b6, basis: inferred, domain: subject-skill, award: "bachelor's with honours" }
  - { outcome: "findings and their significance", threshold: qaa/psychology-2023/4.8.b7, typical: qaa/psychology-2023/4.9.b7, excellent: qaa/psychology-2023/4.10.b7, basis: inferred, domain: subject-skill, award: "bachelor's with honours" }  # (weaker content match: Part E)
  - { outcome: "hardware, software and skills", threshold: qaa/psychology-2023/4.8.b8, typical: qaa/psychology-2023/4.9.b8, excellent: qaa/psychology-2023/4.10.b8, basis: inferred, domain: generic-skill, award: "bachelor's with honours" }  # (weaker content match: Part E)
  - { outcome: "communicating to audiences", threshold: qaa/psychology-2023/4.8.b9, typical: qaa/psychology-2023/4.9.b9, excellent: qaa/psychology-2023/4.10.b9, basis: inferred, domain: generic-skill, award: "bachelor's with honours" }
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
- body: British Psychological Society (BPS)
  says: "accredits undergraduate and postgraduate study and training; chartered status needs an accredited route to the Graduate Basis for Chartered Membership (a second-class degree and a passed empirical project, or an accredited conversion course at 50%) and further training; reviews accredited courses cyclically; its ethics guidance underpins teaching (D1, 1.4, 2.8, 2.9, 2.17, 2.21, 3.21, 3.22)"
  requirements: not yet ingested (Part E)
- body: Health and Care Professions Council (HCPC)
  says: "regulator protecting the public; nine practitioner psychologist titles are protected by law and need HCPC registration and approved training; course titles must not borrow them (D1, 1.5, 1.6, 1.7, 2.17, 3.22, 4.13)"
  requirements: not yet ingested (Part E)
- body: Professional Standards Authority
  says: "registers wider psychological workforce roles, such as psychological wellbeing practitioners (D1, 1.7; 4.14 calls it the Professional Standards Association, Part E)"
  requirements: not-applicable-by-design
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: theme:edi, named: "Equality, diversity and inclusion", carriedIn: ["1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "3.30"], statements: [qaa/psychology-2023/1.18] }
  - { id: theme:accessibility, named: Accessibility, carriedIn: ["1.24", "1.25", "1.26", "1.27", "2.12", "2.20"], statements: [qaa/psychology-2023/1.24] }
  - { id: theme:esd, named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.12", "1.28", "1.29", "1.30", "1.31", "1.32"], statements: [] }
  - { id: theme:enterprise, named: "Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.33", "1.34", "1.35", "2.16"], statements: [] }
frameworks:
  - { framework: fheq, levels: [fheq:6, fheq:7], citedIn: ["2.7", "2.10", "4.5"] }
  - { framework: scqf, levels: [fqheis:10, fqheis:11], citedIn: ["2.7", "2.10", "4.2", "4.5"] }   # cited by its Scottish name, FQHEIS
bodies:
  - { body: British Psychological Society, citedIn: ["1.4", "2.8", "2.9", "2.17", "2.21", "3.21", "3.22"] }
  - { body: Health and Care Professions Council, citedIn: ["1.5", "1.6", "1.7", "2.17", "3.22", "4.13"] }
  - { body: Professional Standards Authority, citedIn: ["1.7", "4.14"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D (not yet ingested: S-03, W-std-0002)", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2", "4.6", "4.7"], role: "descriptions of the four honours classifications (1st, 2.1, 2.2, 3rd); the statement says its subject criteria accompany the annex's more generic transferable skills (4.7)" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: Advice and Guidance, citedIn: [front matter], role: course design, teaching, external expertise, monitoring }
  - { document: "QAA Glossary (not ingested)", named: QAA's Glossary, citedIn: [front matter], role: explains unfamiliar terms }
  - { document: "UN Sustainable Development Goals (external)", named: Sustainable Development Goals, citedIn: ["1.12", "1.29"], role: the frame of the sustainability theme }
  - { document: "Equality Act 2010 (law)", named: Equality Act 2010, citedIn: ["1.17", "1.24", "1.25"], role: duties behind EDI and accessibility }
  - { document: "Health Professions Order 2001 (law)", named: Health Professions Order 2001, citedIn: ["1.6"], role: protected titles }
```

## Part B Terminology
<!-- label: both; status: drafted; basis: primary -->
<!-- The statement has no glossary of its own and sends readers to QAA's Glossary; these are the terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: psychological-literacy, definition: "the capability to use disciplinary knowledge, theory, principles and insight to respond to opportunities and challenges (D1, 1.2)", beneficiaryDefinition: "being able to use what you know about psychology to deal with real situations", scopeNote: "used throughout as the aim of the degree", category: unknown, practices: [education] }
- { slug: subject-specific-skills, definition: "skills that relate closely to subject knowledge or are integral to any Psychology degree (D1, 2.3)", scopeNote: "contrasted with transferable skills; the line is not clear-cut (3.14)", category: unknown, practices: [education] }
- { slug: transferable-skills, definition: "skills less tied to the subject matter of psychology (D1, 2.3, 3.14)", scopeNote: "listed in 3.17", category: unknown, practices: [education] }
- { slug: graduate-basis-for-chartered-membership, definition: "the BPS standing gained by completing an accredited degree or conversion course to the stated marks (D1, 1.4, 2.8)", scopeNote: "first step to chartered psychologist", category: unknown, practices: [education] }
- { slug: conversion-course, definition: "a master's-level course letting graduates of other disciplines study psychology, accredited by the BPS (D1, 1.4, 1.16)", scopeNote: "covered by the statement", category: unknown, practices: [education] }
- { slug: threshold-standard, definition: "the minimum a student will have demonstrated to be awarded the degree (D1, 4.1, 4.8)", scopeNote: "with typical and excellent above it (4.6, 4.9, 4.10)", category: unknown, practices: [education] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: psychological-literacy, form: psychological literacy, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: subject-specific-skills, form: subject-specific skills, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: formal }
- { concept: transferable-skills, form: transferable skills, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: formal }
- { concept: graduate-basis-for-chartered-membership, form: Graduate Basis for Chartered Member, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: graduate-basis-for-chartered-membership, form: GBC, lang: en, partOfSpeech: noun, termStatus: admitted, register: discipline-specific }
- { concept: conversion-course, form: conversion course, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: formal }
- { concept: threshold-standard, form: threshold level, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: formal }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: contrasts-with, from: subject-specific-skills, to: transferable-skills, note: "3.14: the distinction is not clear-cut" }
- { rel: related, from: conversion-course, to: graduate-basis-for-chartered-membership, note: "an accredited conversion course is a direct route (1.16)" }
```

### B5 Rules
<!-- label: editorial; status: drafted; basis: discussion -->
- conversion course: say "master's conversion course", because the statement covers it beside honours degrees and a bare "conversion course" is ambiguous across subjects.

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: Subject Benchmark Statement Psychology
  edition: September 2023
  year: 2023
  url: unknown (the QAA page; the text came by stan's extraction, origin below)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/psychology-2023/psychology-2023.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; ADAPT a3c925b; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: e99f2554cfa38665fb9c384b03d87c7e7e1d7d77f1cf911e892d3660d7265697
  heldFiles: [wkspc2601-library/txt/qaa-2023-psychology-subject-benchmark-statement-standard.txt, wkspc2601-library/txt/qaa-2023-psychology-subject-benchmark-statement-standard.norm.txt, wkspc2601-library/records/qaa-2023-psychology-subject-benchmark-statement-standard.chunks.json, wkspc2601-library/records/<name>.held.json]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6, B1, B2a]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; every part" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (ADAPT 096e25b)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { citation: "QAA (2024) The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies, 2nd edn, Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees (first published separately in 2019, as this statement cites it)", settles: [SB6, S7, S5], asked: 2026-10-03 (W-std-0002), state: wanted }
```

## Part E Gaps and questions
- S3: the held text runs 4.1, 4.2, 4.5: no 4.3 or 4.4. Settled: the gap is in the issuer's original, not an extraction loss (Abbott, 03:47: "They're not in the original"). Recorded as the issuer's numbering; nothing is missing.
- S3, std-prep: the script read 4.6's four bullets as threshold items because the lead-in names "threshold"; they are the bases on which typical and excellent go beyond threshold (SB4 `rungBases`). Lesson for the script: a rung lead-in is "has attained the <rung> level", not any mention of the word.
- S3: 2.8's line beginning "- for example" is a wrapped clause, not a list item (the script split it): 2.8 is one paragraph statement.
- S4, D-std-0002 (a) in practice: paragraphs carrying an expected outcome in "will" inside descriptive prose (1.18, 2.5, 3.11) were taken as statements; others with predictive "will" ("many graduates will pursue careers", 1.8) were not. The line is judgement: for Abbott at P3.
- S4, force: three paragraphs oblige in words outside the list: "need to demonstrate" (3.19, providers), "it is expected that" (3.27, staff development) and "it is important that" (4.13's first sentence). Not taken as statements; for Abbott: should "expected" and "need to" read as `should`?
- S4, 3.16.b10 begins "the ability to", not a verb, breaking its list's grammar; its verbs are taken from the clause.
- SB4: the three rung lists run outcome by outcome in position (nine each); each `gradeOf` link is inferred. Weaker content matches: typical 5 to threshold 5; excellent 5, 7 and 8 to typical 5, 7 and 8.
- SB4: 4.10's lead-in adds "consistently"; every excellent version keeps it.
- S2, statedSubjects: no HECoS term for "biological psychology" or "individual differences"; psychobiology (101344) is the nearest for the first, entered in front matter as inferred.
- S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are to check (template open point 3).
- S7, S0.2: the previous Psychology statement's edition and date are not given in the text.
- SB5: 1.7 names the Professional Standards Authority, 4.14 the "Professional Standards Association": the issuer's inconsistency, kept; the body is the Authority.
- SB5: the BPS's and HCPC's own requirements are not yet ingested.
- S9: not researched in the pilot.
- S4, themes: list items that touch a theme without naming it (3.17.b2 and b9 on inclusion, 3.17.b11 on employability) are not tagged, since tags are what the source says; a consumer may map them.
- Levels: `fqheis:10` and `fqheis:11` used as shared ids for the Scottish framework's levels as this statement names them; not yet in a shared level list (template open point 2).
- ST-12: the length range for audience versions is still unset; versions here run 10 to 41 words.

---

## Change notes
- 0.2.1, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`; texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.2.0, 3 October 2026, 11:00: every statement record now carries the issuer's statement in full (`source`, taken from its span in the held text) beside our paraphrase and versions, for language analysis; private, never published (Abbott, 10:56 and 10:59; D-std-0014). No paraphrase changed.
- 0.1.1, 3 October 2026, 07:34: provenance lines added to Parts B and C; wanted sources in D3 given their W-std ids from the wanted-sources list (the ingest tool's G3 and G7 warnings; std N-0100). No statement changed.
- 0.1.0: 2026-10-03: researched by run frame 0.1.1-draft and standards run layer 0.4.0-draft, std, run 0043 (P1).
