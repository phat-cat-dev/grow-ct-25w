---
id: std:doc:qaa-communication-media-film-and-cultural-studies-2024-benchmarks
title: "Subject Benchmark Statement Communication, Media, Film and Cultural Studies"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100444", label: "media and communication studies", basis: "stated" }
  - { scheme: "hecos", code: "100058", label: "film studies", basis: "stated" }
  - { scheme: "hecos", code: "101233", label: "cultural studies", basis: "stated" }
  - { scheme: "cah", code: "CAH24-01-05", label: "media studies", basis: "stated" }
  - { scheme: "cah", code: "CAH15-01-06", label: "cultural studies", basis: "stated" }
  - { scheme: "cah", code: "CAH24-01", label: "media, journalism and communications", basis: "inferred" }
edition: "April 2024 (fifth edition)"
published: 2024-04
status: current
supersedes: "Subject Benchmark Statement for Communication, Media, Film and Cultural Studies, fourth edition (2019), as section 6 names it"
heldText: { method: sha256-bytes, raw: de1b3b0e48d4a85ac72b6e16d89f18d4d196b3570aff52d242f707c1358dbe67, normalised: 5d4d44a49ead0885a842b9fe9ae16fcd2c83b34fab164993ad637f4881e06799 }
heldTextStan: { method: sha256-stan, raw: de1b3b0e48d4a85ac72b6e16d89f18d4d196b3570aff52d242f707c1358dbe67, normalised: ae48a88af112e7711255b05386c8b34df7acdf051c4210b7dbc82141abc6197a }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, April 2024 revision with the cross-cutting themes (fifth edition of this statement)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0094 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:52"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Communication, Media, Film and Cultural Studies (QAA, April 2024)

> Run 0094, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2024-communication-media-film-cultural-studies-subject-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what an honours graduate in communication, media, film or cultural studies knows, understands and can do, across a family of courses from journalism and advertising to film, games and cultural studies. Its standards are three rung lists (threshold, typical, excellent), each split into subject knowledge and skills and generic skills, plus four added expectations for the master's degree; section 1 adds outcome lists on research, citizenship and transferable skills. Reach for it when designing, reviewing or describing a course or its outcomes in these fields. It is not a curriculum and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2024 as the fifth edition, the statement sets out the context and purposes of degrees in the field, with outcome lists for research and practice (12 items), citizenship (9) and transferable skills (12); its distinctive features (eleven shared propositions, progression, flexibility, partnerships, review); its content, teaching, learning and assessment; and its benchmark standards for the bachelor's degree with honours at three rungs: threshold (33 items), typical (34) and excellent (33), each split into subject and generic skills, with four further expectations for master's degrees. It carries the four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability; employability, enterprise and entrepreneurship) and a paragraph on emerging technologies and generative AI, cites FHEQ and FQHEIS levels and Annex D, draws on the QAA and Advance HE ESD guidance, the SDGs and UNESCO's competencies, and names PSRBs only in general, with BAFTA albert and the EAUC as sustainability resources.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Communication, Media, Film and Cultural Studies"
edition: "April 2024 (fifth edition)"
dates:
  published: 2024-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2024", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what can be expected of a graduate in communication, media, film or cultural studies at the end of an honours degree, of master's graduates, and of courses in these fields"
appliesTo:
  awards: ["bachelor's with honours", "master's"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This document is a QAA Subject Benchmark Statement for Communication, Media, Film and Cultural Studies that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies.\" (D1, front matter)"
statedSubjects:
  - { name: "Communication, Media, Film and Cultural Studies", locator: "(D1, front matter; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100444", label: "media and communication studies" }, { scheme: "hecos", code: "100058", label: "film studies" }, { scheme: "hecos", code: "101233", label: "cultural studies" }, { scheme: "cah", code: "CAH24-01-05", label: "media studies" }, { scheme: "cah", code: "CAH15-01-06", label: "cultural studies" }] }
  - { name: "advertising", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "100074", label: "advertising" }] }
  - { name: "broadcasting", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "100439", label: "broadcast journalism (inferred: Part E)" }] }
  - { name: "communication studies; media studies", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "100444", label: "media and communication studies" }] }
  - { name: "cultural studies", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "101233", label: "cultural studies" }] }
  - { name: "digital, film, television, media or screen studies", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "100440", label: "digital media" }, { scheme: "hecos", code: "100058", label: "film studies" }, { scheme: "hecos", code: "100920", label: "television studies" }] }
  - { name: "interactive media", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "100636", label: "interactive and electronic design (inferred: Part E)" }] }
  - { name: "journalism", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "100442", label: "journalism" }] }
  - { name: "film, television and media production", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "100441", label: "film production" }, { scheme: "hecos", code: "100923", label: "television production" }, { scheme: "hecos", code: "100443", label: "media production" }] }
  - { name: "animation", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "100057", label: "animation" }] }
  - { name: "games studies", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "101267", label: "computer games (inferred: Part E)" }] }
  - { name: "publishing", locator: "(D1, 1.3, named twice)", kind: "programme title", codes: [{ scheme: "hecos", code: "100925", label: "publishing" }] }
  - { name: "public relations", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "100076", label: "public relations" }] }
  - { name: "political communication and lobbying; content creation; cultural management; subject histories", locator: "(D1, 1.3)", kind: "programme title", codes: [] }
  - { name: "combined and joint honours", locator: "(D1, 1.5; 2.12)", kind: "programme title", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "cultural and communicative activity as a force in social life" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "roots in arts, humanities, social sciences and the creative industries" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "varied emphases; a long list of course titles; not prescriptive" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "growth of the creative industries; skills that travel; an agile field" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "focus on single honours; joint and combined honours draw on it" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "scope: honours courses at FHEQ 4 to 6 and FQHEIS 7 to 10" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "taught postgraduate degrees at FHEQ 7 and FQHEIS 11" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Communication, Media, Film and Cultural Studies degree", gloss: "links to neighbouring disciplines; growing creative practice" }
  - { number: "1.9", order: 11, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of a Communication, Media, Film and Cultural Studies degree", gloss: "four skills graduates show, varying by course" }
  - { number: "1.10", order: 12, componentType: stem, parent: "section 1", heading: "Research, critical analysis, production and professional practice", gloss: "research, analysis and practice outcomes (twelve)" }
  - { number: "1.11", order: 13, componentType: stem, parent: "section 1", heading: "Citizenship", gloss: "outcomes for citizenship (nine)" }
  - { number: "1.12", order: 14, componentType: stem, parent: "section 1", heading: "Transferable skills", gloss: "transferable skills (twelve)" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "the fields reflect society and foster EDI" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "a history of critiquing power; staff as agents of change" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusivity as a norm; EDI guidance kept under review" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive environments; EDI built into every course" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI as an ethical obligation in course design" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "active recruitment of students and staff from all of society" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "accessibility built into design, delivery and assessment" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "reasonable adjustments; closing attainment gaps" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "accessible resources, individual support, a pedagogy of care" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainability as an intellectual and ethical frame; the SDGs" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainability lenses in course design; the ESD guidance" }
  - { number: "1.24", order: 26, componentType: stem, parent: "section 1", heading: "Sustainability", gloss: "UNESCO's eight sustainability competencies" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "the competencies as ways of thinking, practising and being" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "ESD questions the subjects take up" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "ESD integrated across courses, not confined to modules" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "the SDGs to frame the curriculum; other references" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "students reflect on sustainability in their practice; BAFTA albert" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainable facilities, equipment and resources; the EAUC" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "enterprise education for changing careers" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "creative industries in the UK economy" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "enterprise skills for creative careers and lives" }
  - { number: "2.1", order: 37, componentType: paragraph, parent: "section 2", heading: "Characteristics", gloss: "defining focus and varied emphases of courses" }
  - { number: "2.2", order: 38, componentType: paragraph, parent: "section 2", heading: "Characteristics", gloss: "the three Cs of media literacy" }
  - { number: "2.3", order: 39, componentType: area, parent: "section 2", heading: "Characteristics", gloss: "practical, business, theoretical and other emphases" }
  - { number: "2.4", order: 40, componentType: area, parent: "section 2", heading: "Characteristics", gloss: "historical or contemporary emphasis" }
  - { number: "2.5", order: 41, componentType: area, parent: "section 2", heading: "Characteristics", gloss: "modes of human communication or specific media" }
  - { number: "2.6", order: 42, componentType: area, parent: "section 2", heading: "Characteristics", gloss: "professional practice, critical practice or activist approaches" }
  - { number: "2.7", order: 43, componentType: area, parent: "section 2", heading: "Characteristics", gloss: "artistic qualities of media and cultural forms" }
  - { number: "2.8", order: 44, componentType: area, parent: "section 2", heading: "Nature and scope", gloss: "eleven propositions shared across courses" }
  - { number: "2.9", order: 45, componentType: paragraph, parent: "section 2", heading: "Nature and scope", gloss: "courses combine the propositions differently" }
  - { number: "2.10", order: 46, componentType: paragraph, parent: "section 2", heading: "Nature and scope", gloss: "a mix of understanding and skills; an extended project" }
  - { number: "2.11", order: 47, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression between levels; postgraduate readiness" }
  - { number: "2.12", order: 48, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined degrees reach the core skills" }
  - { number: "2.13", order: 49, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards; three or four years; part-time study" }
  - { number: "2.14", order: 50, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes and patterns of study; micro-credentials" }
  - { number: "2.15", order: 51, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "partnerships with industry and professional bodies" }
  - { number: "2.16", order: 52, componentType: practice, parent: "section 2", heading: "Partnerships", gloss: "work-based learning, live briefs and placements" }
  - { number: "2.17", order: 53, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "partner providers and study exchanges" }
  - { number: "2.18", order: 54, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "course monitoring, review and the student voice" }
  - { number: "2.19", order: 55, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.20", order: 56, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "2.21", order: 57, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation by professional bodies" }
  - { number: "3.1", order: 59, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "course aims, progression and coherence made known" }
  - { number: "3.2", order: 60, componentType: practice, parent: "section 3", heading: "Content", gloss: "learning from a wide range of materials" }
  - { number: "3.3", order: 61, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "growing self-direction across the course" }
  - { number: "3.4", order: 62, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "six learning processes teaching promotes" }
  - { number: "3.5", order: 63, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "online, in-person and blended delivery" }
  - { number: "3.6", order: 64, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "engagement with forms, practices and outside speakers" }
  - { number: "3.7", order: 65, componentType: paragraph, parent: "section 3", heading: "Embedding equality, diversity and inclusion", gloss: "curricula diverse beyond tokenism" }
  - { number: "3.8", order: 66, componentType: paragraph, parent: "section 3", heading: "Embedding equality, diversity and inclusion", gloss: "courses designed for diverse students; challenging paradigms" }
  - { number: "3.9", order: 67, componentType: paragraph, parent: "section 3", heading: "Embedding equality, diversity and inclusion", gloss: "critical, self-reflective learners" }
  - { number: "3.10", order: 68, componentType: paragraph, parent: "section 3", heading: "Embedding equality, diversity and inclusion", gloss: "inclusive, accessible learning; a pedagogy of care" }
  - { number: "3.11", order: 69, componentType: paragraph, parent: "section 3", heading: "Embedding equality, diversity and inclusion", gloss: "safe, respectful dialogue and belonging" }
  - { number: "3.12", order: 70, componentType: paragraph, parent: "section 3", heading: "Embedding equality, diversity and inclusion", gloss: "courses as part of the change needed" }
  - { number: "3.13", order: 71, componentType: paragraph, parent: "section 3", heading: "Developing entrepreneurship and enterprise skills", gloss: "an entrepreneurial, creative and technical skill mix" }
  - { number: "3.14", order: 72, componentType: paragraph, parent: "section 3", heading: "Developing entrepreneurship and enterprise skills", gloss: "critical perspectives; skills that transfer" }
  - { number: "3.15", order: 73, componentType: area, parent: "section 3", heading: "Developing entrepreneurship and enterprise skills", gloss: "enterprise content some courses offer" }
  - { number: "3.16", order: 74, componentType: paragraph, parent: "section 3", heading: "Developing entrepreneurship and enterprise skills", gloss: "enterprise teaching that serves inclusion" }
  - { number: "3.17", order: 75, componentType: paragraph, parent: "section 3", heading: "Developing entrepreneurship and enterprise skills", gloss: "enterprise aligned with sustainable development" }
  - { number: "3.18", order: 76, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "assessment addresses the skills of 1.8 to 1.12" }
  - { number: "3.19", order: 77, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "students as participants in assessment" }
  - { number: "3.20", order: 78, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment matched to aims; varied assessment" }
  - { number: "3.21", order: 79, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "emerging technologies, AI and academic integrity" }
  - { number: "3.22", order: 80, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "sixteen kinds of assessment" }
  - { number: "3.23", order: 81, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "constructive feedback throughout" }
  - { number: "3.24", order: 82, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formative and summative feedback; feedforward" }
  - { number: "3.25", order: 83, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "an extended final-year project" }
  - { number: "4.1", order: 85, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the three rungs for honours and the master's standards" }
  - { number: "4.2", order: 86, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed the threshold; Annex D" }
  - { number: "4.3", order: 87, componentType: paragraph, parent: "section 4", heading: "Threshold level", gloss: "threshold rung: lead-in" }
  - { number: "4.4", order: 88, componentType: stem, parent: "section 4", heading: "Threshold level", gloss: "threshold: subject knowledge and skills (20)" }
  - { number: "4.5", order: 89, componentType: stem, parent: "section 4", heading: "Threshold level", gloss: "threshold: generic skills (13)" }
  - { number: "4.6", order: 90, componentType: paragraph, parent: "section 4", heading: "Typical level", gloss: "typical rung: lead-in" }
  - { number: "4.7", order: 91, componentType: stem, parent: "section 4", heading: "Typical level", gloss: "typical: subject knowledge and skills (21)" }
  - { number: "4.8", order: 92, componentType: stem, parent: "section 4", heading: "Typical level", gloss: "typical: generic skills (13)" }
  - { number: "4.9", order: 93, componentType: stem, parent: "section 4", heading: "Excellent level", gloss: "excellent: subject knowledge and skills (20)" }
  - { number: "4.10", order: 94, componentType: stem, parent: "section 4", heading: "Excellent level", gloss: "excellent rung lead-in with its generic skills (13)" }
  - { number: "4.11", order: 95, componentType: paragraph, parent: "section 4", heading: "Master's level", gloss: "the place of master's study in the field" }
  - { number: "4.12", order: 96, componentType: paragraph, parent: "section 4", heading: "Master's level", gloss: "routes into master's study" }
  - { number: "4.13", order: 97, componentType: stem, parent: "section 4", heading: "Master's level", gloss: "what master's graduates add (four items)" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Communication, Media, Film and Cultural Studies degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Communication, Media, Film and Cultural Studies degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2, S7 and SB6" }
  - { number: "1, 2, 3, 4", heading: "section heading lines", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for SB6 and D3" }
  - { number: "6", heading: "Membership of the Advisory Group (2024, 2019, 2016, 2008, 2002)", kind: "other: authorship history, read for S7 supersedes" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 164 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/communication-media-film-and-cultural-studies-2024/1.7
  locator: { number: "1.7", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Context"] }
  span: { start: 13391, end: 13940 }
  source: "Postgraduate taught degrees (FHEQ Level 7 and FQHEIS Level 11) are underpinned by the same core attributes as the undergraduate degree level study, but require students to demonstrate advanced and nuanced knowledge and skills in terms of their subject specialism, their critical and creative skills, development of practice, or a combination thereof. Achievement of the appropriate outcomes at this level lies in the consolidation of existing knowledge and/or the generation of new knowledge through a diverse range of outputs or creative artifacts."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "students on taught postgraduate degrees in the subject"
  addressee: learner
  verbs: ["require", "demonstrate"]
  about: "what taught master's degrees add"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Taught postgraduate degrees rest on the same core attributes as undergraduate study but require students to show advanced, nuanced knowledge and skills in their specialism, their critical and creative skills, their practice or a mix of these, consolidating or creating knowledge through varied outputs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.9.b1
  locator: { number: "1.9.b1", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Purposes and characteristics of a Communication, Media, Film and Cultural Studies degree"] }
  span: { start: 14765, end: 14906 }
  source: "to contextualise their learning historically, politically, globally, socially, economically, culturally, environmentally, and technologically"
  stem: "1.9"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["contextualise"]
  about: "placing learning in its many contexts"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Depending on the course, graduates will be able to set what they learn in its historical, political, global, social, economic, cultural, environmental and technological settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.9.b2
  locator: { number: "1.9.b2", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Purposes and characteristics of a Communication, Media, Film and Cultural Studies degree"] }
  span: { start: 14909, end: 15070 }
  source: "to comprehend how different social groups intersect, and how these groups and individuals variably make use of, and engage with, forms of media and communication"
  stem: "1.9"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["comprehend"]
  about: "how social groups intersect and use media"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Depending on the course, graduates will be able to grasp how social groups overlap and how groups and individuals take up and engage with media and communication in different ways."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.9.b3
  locator: { number: "1.9.b3", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Purposes and characteristics of a Communication, Media, Film and Cultural Studies degree"] }
  span: { start: 15073, end: 15299 }
  source: "to make critical judgements in the understanding, production and evaluation of relevant forms, contexts and scenarios and demonstrate the real-world professional application of knowledge and skills developed through the degree"
  stem: "1.9"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["make", "demonstrate"]
  about: "critical judgement and professional application"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Depending on the course, graduates will be able to judge critically when understanding, making and evaluating relevant forms, contexts and scenarios, and show how the knowledge and skills of the degree apply in real professional settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.9.b4
  locator: { number: "1.9.b4", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Purposes and characteristics of a Communication, Media, Film and Cultural Studies degree"] }
  span: { start: 15302, end: 15468 }
  source: "to consider and evaluate their own work in a reflexive manner, with reference to the academic and/or professional codes of practices, conventions, issues and debates."
  stem: "1.9"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["consider", "evaluate"]
  about: "reflexive evaluation of own work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Depending on the course, graduates will be able to weigh and evaluate their own work reflexively against academic or professional codes, conventions, issues and debates."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.10.b1
  locator: { number: "1.10.b1", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Research, critical analysis, production and professional practice"] }
  span: { start: 15596, end: 15694 }
  source: "engage critically with major thinkers and debates within the field, putting them to productive use"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["engage"]
  about: "the field's major thinkers and debates"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will typically be able to engage critically with the field's leading thinkers and arguments and put them to good use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.10.b2
  locator: { number: "1.10.b2", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Research, critical analysis, production and professional practice"] }
  span: { start: 15697, end: 15934 }
  source: "understand forms of communication, media, film and culture as they have emerged historically and appreciate the processes through which they have come into being, with reference to social, cultural, environmental and technological change"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["understand", "appreciate"]
  about: "how media and cultural forms emerged"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will typically be able to understand how forms of communication, media, film and culture arose over time and how social, cultural, environmental and technological change shaped them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.10.b3
  locator: { number: "1.10.b3", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Research, critical analysis, production and professional practice"] }
  span: { start: 15937, end: 16003 }
  source: "carry out sustained, independent and critical enquiry and research"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["carry"]
  about: "sustained independent enquiry"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will typically be able to pursue sustained, independent, critical enquiry and research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.10.b4
  locator: { number: "1.10.b4", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Research, critical analysis, production and professional practice"] }
  span: { start: 16006, end: 16080 }
  source: "formulate appropriate research questions or enquiries that inform practice"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["formulate"]
  about: "framing research questions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will typically be able to frame research questions or lines of enquiry that feed into practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.10.b5
  locator: { number: "1.10.b5", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Research, critical analysis, production and professional practice"] }
  span: { start: 16083, end: 16188 }
  source: "identify, employ and evaluate research methods suitable for the context and defined research problematics"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["identify", "employ", "evaluate"]
  about: "choosing and using research methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will typically be able to choose, use and evaluate research methods that fit the context and the problem being researched."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.10.b6
  locator: { number: "1.10.b6", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Research, critical analysis, production and professional practice"] }
  span: { start: 16194, end: 16366 }
  source: "locate, retrieve, evaluate and draw upon a range of data, sources and conceptual frameworks appropriate to research, production and professional practice in the chosen area"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["locate", "retrieve", "evaluate", "draw"]
  about: "finding and using sources and frameworks"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will typically be able to find, retrieve, judge and use data, sources and conceptual frameworks that suit research, production and professional practice in their own area."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.10.b7
  locator: { number: "1.10.b7", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Research, critical analysis, production and professional practice"] }
  span: { start: 16369, end: 16534 }
  source: "draw on the strengths and understand the limits of relevant quantitative and/or qualitative methods, and be able to apply this knowledge critically in their own work"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["draw", "understand", "apply"]
  about: "strengths and limits of methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will typically be able to use the strengths, and know the limits, of fitting quantitative or qualitative methods, and apply this critically in their own work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.10.b8
  locator: { number: "1.10.b8", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Research, critical analysis, production and professional practice"] }
  span: { start: 16537, end: 16673 }
  source: "show analytical ability and the capacity to consider and solve problems, which might be theoretical, practical or professional in nature"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["show", "consider", "solve"]
  about: "analysis and problem-solving"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will typically be able to analyse well and work through problems that may be theoretical, practical or professional."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.10.b9
  locator: { number: "1.10.b9", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Research, critical analysis, production and professional practice"] }
  span: { start: 16676, end: 16862 }
  source: "demonstrate sensitivity to the subjectivities and intersections of different cultural positions, including their own, understanding that research and production are not neutral processes"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "sensitivity to cultural positions"
  themes: [theme:edi]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will typically be able to show sensitivity to the subjective positions and intersections of different cultures, their own included, knowing that research and production are never neutral."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.10.b10
  locator: { number: "1.10.b10", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Research, critical analysis, production and professional practice"] }
  span: { start: 16865, end: 16937 }
  source: "exhibit imaginative insight and creativity as appropriate to the context"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["exhibit"]
  about: "imagination and creativity"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will typically be able to show imagination and creative insight that suit the context."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.10.b11
  locator: { number: "1.10.b11", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Research, critical analysis, production and professional practice"] }
  span: { start: 16940, end: 17000 }
  source: "show awareness and/or consideration of sustainable practices"
  stem: "1.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["show"]
  about: "awareness of sustainable practice"
  themes: [theme:esd]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will typically be able to show awareness of, or attention to, sustainable ways of working."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.10.b12
  locator: { number: "1.10.b12", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Research, critical analysis, production and professional practice"] }
  span: { start: 17003, end: 17141 }
  source: "locate, understand, critique and comply with ethical codes produced by relevant subject and industry associations, and research standards."
  stem: "1.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["locate", "understand", "critique", "comply"]
  about: "ethical codes and research standards"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will typically be able to find, understand, criticise and keep to the ethical codes of relevant subject and industry bodies and to research standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.11.b1
  locator: { number: "1.11.b1", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Citizenship"] }
  span: { start: 17357, end: 17555 }
  source: "apply their critical understanding to ethically and culturally responsible use of communication, media, film and cultural forms, practices and technologies in both professional and everyday contexts"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["apply"]
  about: "ethical, responsible use of media forms"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to bring critical understanding to the ethical, culturally responsible use of media and cultural forms, practices and technologies of every kind, at work and in daily life."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.11.b2
  locator: { number: "1.11.b2", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Citizenship"] }
  span: { start: 17558, end: 17707 }
  source: "use communication, media, film and cultural expression in ways informed by cultural and media literacies (including digital and information literacy)"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["use"]
  about: "expression informed by literacies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to express themselves through communication, media, film and culture in ways shaped by cultural, media, digital and information literacies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.11.b3
  locator: { number: "1.11.b3", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Citizenship"] }
  span: { start: 17710, end: 17817 }
  source: "critically appraise socio-cultural and political debates relevant to communication, media, film and culture"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["appraise"]
  about: "socio-cultural and political debates"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to appraise critically the social, cultural and political debates that bear on communication, media, film and culture."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.11.b4
  locator: { number: "1.11.b4", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Citizenship"] }
  span: { start: 17820, end: 17896 }
  source: "develop and foster confidence to engage as responsible and informed citizens"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["develop", "foster"]
  about: "confidence as an informed citizen"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to build the confidence to take part as responsible, informed citizens."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.11.b5
  locator: { number: "1.11.b5", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Citizenship"] }
  span: { start: 17899, end: 17994 }
  source: "understand media and cultural policies and the ways in which they are developed and implemented"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["understand"]
  about: "media and cultural policy"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to understand media and cultural policies and how they are made and put into effect."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.11.b6
  locator: { number: "1.11.b6", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Citizenship"] }
  span: { start: 17997, end: 18140 }
  source: "consider the ways in which diverse communities and organisations can contribute to the development of media and cultural policies and practices"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["consider"]
  about: "communities shaping policy and practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to think about how varied communities and organisations can help shape media and cultural policy and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.11.b7
  locator: { number: "1.11.b7", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Citizenship"] }
  span: { start: 18143, end: 18298 }
  source: "analyse the role of community and participatory media and communication forms in contributing to cultural and political debates and the contesting of power"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["analyse"]
  about: "community media and contests over power"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to analyse how community and participatory media and communication feed cultural and political debate and challenges to power."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.11.b8
  locator: { number: "1.11.b8", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Citizenship"] }
  span: { start: 18301, end: 18401 }
  source: "consider global sustainability practices and debates in relation to communication and cultural forms"
  stem: "1.11"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["consider"]
  about: "global sustainability debates"
  themes: [theme:esd]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to think about global sustainability practice and debate as they bear on communication and cultural forms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.11.b9
  locator: { number: "1.11.b9", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Citizenship"] }
  span: { start: 18404, end: 18549 }
  source: "demonstrate an openness to diverse discussions and debates in which their own informed opinion and lived experiences may be challenged by others."
  stem: "1.11"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "openness when views are challenged"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to stay open to varied discussion and debate in which others may question their own informed views and lived experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.12.b1
  locator: { number: "1.12.b1", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Transferable skills"] }
  span: { start: 18622, end: 18755 }
  source: "work in flexible, creative and independent ways, with an awareness of relevant ethical considerations, self-direction and reflexivity"
  stem: "1.12"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["work"]
  about: "flexible, ethical, self-directed working"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to work flexibly, creatively and independently, aware of ethical issues, directing themselves and reflecting on what they do."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.12.b2
  locator: { number: "1.12.b2", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Transferable skills"] }
  span: { start: 18758, end: 18926 }
  source: "communicate effectively in interpersonal settings, expressing sensitivity to cultural differences, and an openness to knowledge, ideas and approaches unfamiliar to them"
  stem: "1.12"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["communicate"]
  about: "interpersonal communication across cultures"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to communicate well with others in person, sensitive to cultural difference and open to knowledge, ideas and approaches new to them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.12.b3
  locator: { number: "1.12.b3", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Transferable skills"] }
  span: { start: 18929, end: 19124 }
  source: "collate, organise and deploy ideas and information in order to formulate arguments cogently, and express them effectively in written, verbal and/or non-verbal communication, visual or other forms"
  stem: "1.12"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["collate", "organise", "deploy", "formulate", "express"]
  about: "building and expressing arguments"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to gather, order and use ideas and information to build clear arguments and put them across well in writing, speech, non-verbal, visual or other forms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.12.b4
  locator: { number: "1.12.b4", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Transferable skills"] }
  span: { start: 19127, end: 19220 }
  source: "retrieve and generate information, and evaluate sources, in carrying out independent research"
  stem: "1.12"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["retrieve", "generate", "evaluate"]
  about: "information for independent research"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to find and produce information and judge sources when doing independent research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.12.b5
  locator: { number: "1.12.b5", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Transferable skills"] }
  span: { start: 19223, end: 19277 }
  source: "organise and manage supervised, self-directed projects"
  stem: "1.12"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["organise", "manage"]
  about: "managing supervised self-directed projects"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to plan and run supervised projects that they direct."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.12.b6
  locator: { number: "1.12.b6", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Transferable skills"] }
  span: { start: 19280, end: 19405 }
  source: "work productively in a group or team, showing abilities at different times to listen, contribute and also to lead effectively"
  stem: "1.12"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["work"]
  about: "team working and leadership"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to work well in a group or team, listening, contributing and leading well at different times."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.12.b7
  locator: { number: "1.12.b7", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Transferable skills"] }
  span: { start: 19408, end: 19568 }
  source: "deliver work to a given length, format, brief and deadline, properly referencing sources and ideas and making use, as appropriate, of a problem-solving approach"
  stem: "1.12"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["deliver"]
  about: "delivering to brief and deadline"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to produce work to a set length, format, brief and deadline, citing sources and ideas properly and solving problems where that helps."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.12.b8
  locator: { number: "1.12.b8", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Transferable skills"] }
  span: { start: 19571, end: 19703 }
  source: "apply entrepreneurial skills, if and where appropriate, in dealing with audiences, users, clients, consumers, markets and/or sources"
  stem: "1.12"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["apply"]
  about: "entrepreneurial skills with audiences and markets"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to use entrepreneurial skills, where they fit, with audiences, users, clients, consumers, markets or sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.12.b9
  locator: { number: "1.12.b9", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Transferable skills"] }
  span: { start: 19706, end: 19843 }
  source: "develop an information literacy to identify and evaluate appropriate sources and evidence considering cultural contexts and sensitivities"
  stem: "1.12"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["develop"]
  about: "information literacy with cultural sensitivity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to build the information literacy to find and judge suitable sources and evidence with an eye to cultural context and sensitivity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.12.b10
  locator: { number: "1.12.b10", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Transferable skills"] }
  span: { start: 19846, end: 19913 }
  source: "engage critically with a variety of media practices and competences"
  stem: "1.12"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["engage"]
  about: "engaging critically with media practices"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to engage critically with a range of media practices and competences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.12.b11
  locator: { number: "1.12.b11", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Transferable skills"] }
  span: { start: 19916, end: 20132 }
  source: "understand that communication technologies, practices and products are not 'neutral' but are developed and accessed in relation to their social, cultural, economic, historical, environmental and geographical contexts"
  stem: "1.12"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["understand"]
  about: "media technologies are not neutral"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to see that communication technologies, practices and products are never neutral but take shape in their social, cultural, economic, historical, environmental and geographical settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.12.b12
  locator: { number: "1.12.b12", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Transferable skills"] }
  span: { start: 20135, end: 20222 }
  source: "explore career opportunities in order to prepare for potential employment destinations."
  stem: "1.12"
  statementType: outcome
  rung: none
  force: may
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["explore"]
  about: "exploring careers"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates may be able to look into career openings to get ready for possible jobs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.16
  locator: { number: "1.16", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Equality, diversity and inclusion"] }
  span: { start: 21834, end: 22253 }
  source: "Our students, and staff, are drawn from diverse backgrounds and deserve to learn, and work in inclusive environments which support people regardless of age, gender, race, disability, neurodiversity, sexual orientation, religion and belief, or socio-economic background. Commitment to EDI as both a policy and practice should be embedded into all courses and practices in Communication, Media, Film and Cultural Studies."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["embedded"]
  about: "EDI built into every course"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students and staff come from varied backgrounds and deserve inclusive places to learn and work, whatever their age, gender, race, disability, neurodivergence, sexual orientation, religion or belief, or social and economic background; commitment to EDI, in policy and in practice, should be built into every course and practice in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Equality, diversity and inclusion"] }
  span: { start: 22259, end: 22642 }
  source: "EDI is not optional and comes with ethical obligations, permeating all aspects of course design and delivery. Establishing policies, practices and systems that must strive for fairness and equity for all, champions the importance of EDI and ensures that these values are reliably, consistently and transparently supported in integrated ways which underline its intersectional nature."
  stem: none
  statementType: expectation
  rung: none
  force: must
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["strive", "champions", "ensures"]
  about: "EDI as an obligation in course design"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "EDI is not optional and brings ethical obligations to every part of course design and delivery; policies, practices and systems must work for fairness and equity for all, so that these values are supported reliably, consistently and openly in joined-up ways that reflect how inequalities intersect."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Equality, diversity and inclusion"] }
  span: { start: 22648, end: 22943 }
  source: "Students, and staff, should be actively recruited from across society, with active recruitment policies that seek to identify and support underrepresented people in recruitment campaigns and application processes. Selection and interview processes should embody good practice in all its aspects."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["recruited", "embody"]
  about: "recruiting students and staff from all of society"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students and staff should be recruited actively from across society, with policies that find and support under-represented people in recruitment and applications, and selection and interviews should follow good practice throughout."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.19
  locator: { number: "1.19", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Accessibility"] }
  span: { start: 22963, end: 23813 }
  source: "Accessibility involves ensuring that every part of the educational experience is designed to optimise access for everyone. It is understood that accessibility is not a single point of reference and can have emotional, functional and technical aspects that courses should consider holistically to ensure inclusivity and equality. Being inclusive is about giving equal access and opportunities to everyone wherever possible and to establishing practices and structures that allow equal access and chance of success regardless of education, cultural or social backgrounds, neurodiversity, or disability status. Communication, Media, Film and Cultural Studies courses should ensure that accessibility is a core part of all aspects of course design, delivery and assessment, and that inclusivity is a guiding principle in the field of study at all levels."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["consider", "ensure"]
  about: "accessibility in design, delivery and assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Accessibility means designing every part of learning so that everyone can take part; it has emotional, functional and technical sides that courses should weigh as a whole, and courses should make accessibility central to design, delivery and assessment, with inclusion guiding the field at every level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.20
  locator: { number: "1.20", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Accessibility"] }
  span: { start: 23819, end: 24116 }
  source: "Reasonable adjustments should be provided to ensure equality of access and a drive toward the eradication of attainment gaps based on accessibility in all its formats. Communication, Media, Film and Cultural Studies programmes should approach accessibility requests with respect and understanding."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["provided", "approach"]
  about: "reasonable adjustments and attainment gaps"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Reasonable adjustments should be made to give equal access and to push towards ending attainment gaps linked to accessibility, and requests for accessibility support should be handled with respect and understanding."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.21
  locator: { number: "1.21", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Accessibility"] }
  span: { start: 24122, end: 24560 }
  source: "Learning resources should also be accessible to all and presented in a timely way using appropriate methods of delivery dependent on student needs. Learning support should be individualised to the needs of students and managed in a supportive environment. Utilising a pedagogy of care that focuses on trust, inclusion, respect and support is crucial to ensuring that everyone feels included, valued and able to contribute and participate."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["presented", "individualised", "managed"]
  about: "accessible resources and individual support"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Learning resources should be open to everyone and supplied on time in forms that suit students' needs, and support should be fitted to each student within a supportive setting; a pedagogy of care built on trust, inclusion, respect and support helps everyone feel included and able to take part."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Sustainability"] }
  span: { start: 25220, end: 25897 }
  source: "Sustainability agendas offer new lenses through which to view the relationships between social, cultural, economic and environmental challenges. Higher education is pivotal in enabling the knowledge and skills that are needed to address such challenges. Course design processes should use these lenses in considering content, assessment, employability, delivery practices and facilities, and the role of higher education in changing rather than reproducing or perpetuating unsustainable social practices. This Subject Benchmark Statement should be further considered in the context of the Guidance on Education for Sustainable Development (ESD) published by QAA and Advance HE."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["use", "considered"]
  about: "sustainability lenses in course design"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Sustainability offers new ways to see how social, cultural, economic and environmental challenges connect; course design should use these lenses for content, assessment, employability, delivery and facilities, and on how higher education can change unsustainable practice, and the statement should be read with the QAA and Advance HE ESD guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.27
  locator: { number: "1.27", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Sustainability"] }
  span: { start: 27812, end: 28485 }
  source: "ESD offers vital opportunities to challenge established approaches and assumptions not only within higher education in these subject areas, but also within the industries and sectors employing their graduates. For example, assessment, placement and employability strategies can look beyond aiming to prepare learners for industries and can also work to influence those industries to better engage with sustainability goals. ESD to this end offers an opportunity to reflect on and challenge established approaches to Communication, Media, Film and Cultural Studies. As such, it should be integrated throughout degree courses and not be simply confined to specialist modules."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["integrated"]
  about: "ESD across the whole course"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "ESD lets the field question settled approaches in higher education and in the industries that employ its graduates, for example through assessment, placements and employability work that try to move those industries towards sustainability; it should run through degree courses, not sit only in specialist modules."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.28
  locator: { number: "1.28", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Sustainability"] }
  span: { start: 28491, end: 28897 }
  source: "The SDGs can help to frame Communication, Media, Film and Cultural Studies curricula in ways that reflects the rich and diverse context of ESD. This critical thinking should also extend to a reflexive and agile approach in considering other external references\n\n9\nfor sustainable development to also serve as a force for advancing action on sustainability through global and interdisciplinary perspectives."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["extend"]
  about: "the SDGs and other references in the curriculum"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The SDGs can help frame curricula in the field; this critical thinking should reach, reflexively and with agility, to other external references on sustainable development, so that the curriculum also drives action on sustainability through global and interdisciplinary views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/1.29
  locator: { number: "1.29", headingPath: ["Context and purposes of a Communication, Media, Film and Cultural Studies degree", "Sustainability"] }
  span: { start: 28903, end: 29295 }
  source: "Students should also be encouraged to reflect on sustainability in and of their practice and embed elements such as self-assessment of activities. There are a number of external frameworks and resources that can be incorporated into curriculum design, which may also offer external recognition, such as that provided by the BAFTA albert Education Partnership for production and screen skills."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["encouraged", "reflect", "embed"]
  about: "students reflecting on sustainable practice"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be encouraged to think about how sustainable their own practice is, and about sustainability within it, and to build in steps such as assessing their own activities; external frameworks, some with recognition such as BAFTA albert's education partnership for production and screen skills, can feed curriculum design."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of a Communication, Media, Film and Cultural Studies degree", "Progression"] }
  span: { start: 40082, end: 40553 }
  source: "Undergraduates studying Communication, Media, Film and Cultural Studies courses as part of a combined or joint degree with other subjects will achieve core elements of the specific and generic skills outlined in this Subject Benchmark Statement and will add others according to the topics covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint and combined honours students"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "core skills on joint and combined degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students taking the subject in a combined or joint degree will reach core parts of its subject-specific and generic skills and add others from their other subjects, and may explore where the disciplines meet."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/3.7
  locator: { number: "3.7", headingPath: ["Content, structure and delivery", "Embedding equality, diversity and inclusion"] }
  span: { start: 48802, end: 49320 }
  source: "Curricula should embed a diverse range of methods, viewpoints, subjects and approaches, aiming to go beyond tokenism. Equality, diversity and inclusion should not be compartmentalised, but embedded across the course with a commitment to ongoing development of good EDI knowledge, understanding and practice as they pertain to the diversity of programmes within Communication, Media, Film and Cultural Studies. This includes diversifying module content, learning resources, theoretical approaches and assessment design."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["embed", "compartmentalised"]
  about: "a diverse curriculum beyond tokenism"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Curricula should build in a varied mix of methods, viewpoints, subjects and approaches and go further than token gestures; EDI should run across the whole course, not sit in one place, with a lasting commitment to good EDI knowledge and practice, which covers module content, resources, theory and assessment design."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/3.8
  locator: { number: "3.8", headingPath: ["Content, structure and delivery", "Embedding equality, diversity and inclusion"] }
  span: { start: 49325, end: 49668 }
  source: "Courses will aim to be designed to cater to a diverse range of students from various backgrounds, with a focus on inclusivity and belonging. Students will be encouraged to engage in critical dialogue and challenge established paradigms related to, for example, gender, sexuality, religion, class, race, disability, colonialism and imperialism."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["designed", "encouraged", "engage", "challenge"]
  about: "designing for diverse students; challenging paradigms"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses will aim to be designed for a diverse range of students, with inclusion and belonging in focus, and students will be encouraged to take part in critical dialogue and challenge settled paradigms on matters such as gender, sexuality, faith, class, race, disability and the legacies of empire and colonial rule."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Embedding equality, diversity and inclusion"] }
  span: { start: 49673, end: 49997 }
  source: "To critically examine dominant approaches to the discipline(s) and ways in which they can perpetuate exclusion, courses should actively engage and support students in their development as critical and self-reflective learners, encouraging reflection on ways in which they are taught and how they themselves learn and behave."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["engage", "support"]
  about: "critical, self-reflective learners"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "To examine critically the leading approaches to the discipline and how they can exclude people, courses should engage and support students as critical, self-reflective learners, inviting them to reflect on the teaching they receive and on their own learning and conduct."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/3.10
  locator: { number: "3.10", headingPath: ["Content, structure and delivery", "Embedding equality, diversity and inclusion"] }
  span: { start: 50003, end: 50584 }
  source: "Courses will create inclusive learning experiences, ensuring accessibility for all students, regardless of their background, and promote equity. Learning resources should also be accessible to all and presented in a timely way using appropriate methods of delivery dependent on student needs. Learning support should be individualised to the needs of students and managed in a supportive environment. Utilising a pedagogy of care that focuses on trust, inclusion, respect and support is crucial to ensure that everyone feels included, valued and able to contribute and participate."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["create", "ensuring", "promote"]
  about: "inclusive, accessible learning"
  themes: [theme:edi, theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses will create inclusive learning, accessible to all students whatever their background, and promote equity; resources should be accessible and timely in suitable formats, support fitted to each student, and a pedagogy of care built on trust, inclusion, respect and support helps everyone feel included and able to take part."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/3.17
  locator: { number: "3.17", headingPath: ["Content, structure and delivery", "Developing entrepreneurship and enterprise skills"] }
  span: { start: 53967, end: 54470 }
  source: "Furthermore, students should be encouraged to explore the ways in which enterprise and entrepreneurial mindsets can align with sustainable development goals by fostering innovative and sustainable approaches to media production and distribution, promoting responsible consumption and production, and addressing social and environmental challenges through projects that contribute to the achievement of international sustainability framework, for example the United Nations Sustainable Development Goals."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["encouraged", "explore"]
  about: "enterprise aligned with sustainable development"
  themes: [theme:enterprise, theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be encouraged to explore how enterprise and entrepreneurial thinking can serve sustainable development, through new and sustainable ways of making and distributing media, responsible consumption and production, and projects that address social and environmental challenges and help meet international aims such as the SDGs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/3.18
  locator: { number: "3.18", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54487, end: 54640 }
  source: "Assessment is an integral part of the learning process, and assessment of learning outcomes should address the skills highlighted in paragraphs 1.8-1.12."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["address"]
  about: "assessment covering the skills of section 1"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessment is part of learning, and the assessment of learning outcomes should address the skills set out earlier in section 1, from the purposes of the degree to its transferable skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/3.21
  locator: { number: "3.21", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 55718, end: 56726 }
  source: "Students should learn to make effective and ethical use of emerging technologies, while maintaining a critical awareness of how these may alter or challenge established professional norms and practices. This may range from (semi-)automated workflows, accessible user interfaces replacing coding or complex operations, through to use of adaptive technologies, machine learning and artificial intelligence. Courses in Communication, Media, Film and Cultural Studies have a history of responding in agile ways to rapidly evolving forms and practices, and graduates in these disciplines are important in how society responds to such advances. Assessment strategies should be responsive to these developments, while ensuring students can still be assessed on the requisite subject knowledge, understanding and skills. This should also be seen in the context of preserving academic integrity in relation to use of artificial intelligence. For further guidance on this, please consult QAA guidance on generative AI."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students and assessment strategies in the subject"
  addressee: both
  verbs: ["learn", "make", "maintaining"]
  about: "emerging technologies, AI and assessment"
  themes: [theme:generative-ai]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should learn to use emerging technologies effectively and ethically while staying critical of how they may change professional norms, from automated workflows to adaptive tools, machine learning and AI; assessment strategies should respond to these changes while still testing subject knowledge, understanding and skills, with academic integrity in view."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/3.23
  locator: { number: "3.23", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 58102, end: 58555 }
  source: "Feedback is an essential part of assessment, to help students evaluate their progress and identify how they can improve further. Students should receive constructive feedback throughout their studies, with particular attention paid to building skills of self-reflection and self-criticality. Feedback is provided through various mechanisms, including written and spoken comments, group discussion and technology-aided systems, peer and self- assessment."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["receive"]
  about: "constructive feedback throughout"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Feedback is central to assessment, helping students judge their progress and see how to improve; students should get constructive feedback throughout their studies, with attention to building self-reflection and self-criticism, through written and spoken comments, group discussion, technology and peer and self-assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/3.24
  locator: { number: "3.24", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 58561, end: 59212 }
  source: "Feedback should be both formative as well as summative. It should focus on supporting students to understand how to improve their work (feedforward), both in terms of the assignment's specifics as well as their wider skill set and knowledge. Formative assessment enables students to see how well they are progressing and gives them feedback to develop further. Effective formative assessment and feedback occurs early,\n\n18\nduring and after the assessment process to help the student develop. The summative feedback evaluates how the student is doing, providing the student with a judgement on their abilities in line with the stated learning outcomes."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["focus", "supporting"]
  about: "formative, summative and feedforward feedback"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Feedback should be both formative and summative and should help students see how to improve, in the task at hand and in their wider skills and knowledge; formative feedback comes early, during and after assessment, while summative feedback judges performance against the stated outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60094, end: 60742 }
  source: "The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd. It can also be used as a reference point for other qualifications at FHEQ Level 7 and FQHEIS Level 11, including postgraduate certifications and postgraduate diplomas."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["refer"]
  about: "Annex D for achievement above threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do well above the minimum threshold; each provider decides what evidence shows this and should refer to Annex D of the qualification frameworks, which describes the four honours classifications and can also serve as a reference for postgraduate certificates, diplomas and other awards at Level 7 (FHEQ) or 11 (FQHEIS)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 61319, end: 61509 }
  source: "demonstrate a knowledge and understanding of key debates and theoretical perspectives in Communication, Media, Film and Cultural Studies, including those that extend beyond the Western canon"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "key debates and theories of the field"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can show knowledge and understanding of the field's main debates and theoretical positions, including ones from beyond Western traditions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 61512, end: 61630 }
  source: "demonstrate an ability to engage in an analysis of media texts, using theoretical material, concepts and understanding"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "engage"]
  about: "analysing media texts with theory"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can analyse media texts with the help of theory and concepts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 61633, end: 61767 }
  source: "understand the representational, technological and cultural significance of communication, media, film and cultural texts and contexts"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand"]
  about: "why texts and contexts matter"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can grasp why texts and contexts in these fields matter for representation, for technology and for culture."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 61770, end: 61909 }
  source: "consider the ways in which diverse communities and organisations contribute to the development of media and cultural policies and practices"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["consider"]
  about: "communities shaping media and cultural policy"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can think about how varied communities and organisations help shape media and cultural policy and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 61912, end: 62069 }
  source: "analyse the role of media forms, including community and participatory media, in contributing to political and cultural debates and the contestation of power"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["analyse"]
  about: "media forms, debate and power"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can analyse how media forms, community and participatory media among them, feed political and cultural debate and struggles over power."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 62072, end: 62190 }
  source: "consider global issues, including sustainability practices and debates in relation to communication and cultural forms"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["consider"]
  about: "global issues and sustainability"
  themes: [theme:esd]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can think about global questions, sustainability among them, as they bear on communication and cultural forms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 62193, end: 62409 }
  source: "understand that communication technologies, practices and products are not 'neutral' but are developed and accessed in relation to their social, cultural, economic, historical, environmental and geographical contexts"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand"]
  about: "technologies and products are not neutral"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can see that communication technologies, practices and products are never neutral but are made and reached through their social, cultural, economic, historical, environmental and geographical settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 62412, end: 62684 }
  source: "appreciate the ways in which questions of cultural value are experienced and understood, including how accounts of the world are created, maintained and\n\n20\nreproduced, and how understandings of the self and the world are formed in relation to cultural texts and practices"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["appreciate"]
  about: "cultural value and how it is formed"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can recognise how cultural value is lived and understood, including how versions of the world get made, kept going and passed on and how people form a sense of self and world through cultural texts and practices."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 62687, end: 62819 }
  source: "understand how different social groups and organisations interact, engage with and make use of various forms of media to communicate"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand"]
  about: "how social groups use media"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can understand how social groups and organisations interact with one another and use various media to communicate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b10
  locator: { number: "4.4.b10", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 62822, end: 63106 }
  source: "identify, evaluate and employ research methods suitable for the context - these may include digital methodologies, close textual analysis, archive research, research-by- practice, (auto)ethnography, critically reflective practice, audience research methods or participatory approaches"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["identify", "evaluate", "employ"]
  about: "choosing and using research methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can choose, weigh and use research methods that suit the context, such as digital methods, close reading of texts, archives, practice-based research, (auto)ethnography, reflective practice, audience research or participatory designs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b11
  locator: { number: "4.4.b11", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 63109, end: 63292 }
  source: "be able to locate, retrieve, evaluate and draw upon a range of data, sources and conceptual frameworks appropriate to research, production and professional practice in the chosen area"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["locate", "retrieve", "evaluate", "draw"]
  about: "finding and judging sources and frameworks"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can find, retrieve, assess and use a range of data, sources and conceptual frameworks suited to research, production and professional practice in their own area."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b12
  locator: { number: "4.4.b12", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 63295, end: 63449 }
  source: "draw on the strengths and understand the limits of relevant quantitative and/or qualitative methods, and be able to apply this knowledge in their own work"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["draw", "understand", "apply"]
  about: "strengths and limits of quantitative and qualitative methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can use the strengths, and know the limits, of the quantitative or qualitative methods that fit, applying that knowledge in their own work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b13
  locator: { number: "4.4.b13", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 63452, end: 63526 }
  source: "research and present an extended piece of research or practical equivalent"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["research", "present"]
  about: "an extended research or practical project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can research and present an extended project, written or practical."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b14
  locator: { number: "4.4.b14", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 63529, end: 63736 }
  source: "demonstrate an understanding of and/or ability to engage in cultural and production practices, applying their theoretical understanding to production processes depending on the specific focus of their course"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "engage", "applying"]
  about: "theory in cultural and production practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can show understanding of, or skill in, cultural and production practice, bringing theory to bear on how things are made, as the course's focus allows."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b15
  locator: { number: "4.4.b15", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 63739, end: 63835 }
  source: "demonstrate creative expression through practice depending on the specific focus of their course"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "creative expression through practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can show creative expression in practice, as the course's focus allows."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b16
  locator: { number: "4.4.b16", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 63838, end: 63961 }
  source: "demonstrate an ability to reflect on new knowledge and understanding, and on their own learning experiences and performance"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "reflect"]
  about: "reflecting on learning and performance"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can think back on what they have newly learned and understood, and on their own learning and performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b17
  locator: { number: "4.4.b17", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 63964, end: 64129 }
  source: "understand the development of media, communication and/or film studies as a subject and understand its implications for the discipline today and its cultural context"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand"]
  about: "how the subject developed"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can understand how media, communication or film studies grew as a subject and what that means for the discipline and its cultural setting now."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b18
  locator: { number: "4.4.b18", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 64132, end: 64246 }
  source: "understand the need for an inclusive discipline and accord respect to diverse others within and beyond the subject"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand", "accord"]
  about: "an inclusive discipline and respect for others"
  themes: [theme:edi]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can understand why the discipline needs to be inclusive, and show respect to diverse people inside and outside the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b19
  locator: { number: "4.4.b19", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 64249, end: 64363 }
  source: "demonstrate an openness to diverse discussions and debates in which their own opinions may be challenged by others"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "openness in discussion and debate"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can stay open to varied discussion and debate in which others may challenge their own views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.4.b20
  locator: { number: "4.4.b20", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 64366, end: 64545 }
  source: "apply their understanding to ethically and culturally responsible use of communication, media, film and cultural forms and technologies in both professional and everyday contexts."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["apply"]
  about: "ethical, responsible use of media forms"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can use communication, media, film and cultural forms and technologies ethically and with cultural responsibility, at work and in daily life."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 64695, end: 64829 }
  source: "demonstrate the ability to select, evaluate and comment on reading, research and primary sources using appropriate referencing formats"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "select", "evaluate", "comment"]
  about: "selecting and referencing sources"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can choose, judge and comment on reading, research and primary sources, referencing them properly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 64832, end: 64938 }
  source: "show the ability to devise, sustain and critique an argument, with some consideration of alternative views"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["show", "devise", "sustain", "critique"]
  about: "building and testing an argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can build, hold and criticise an argument, giving some thought to other views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 64941, end: 64984 }
  source: "explain sometimes complex matters and ideas"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["explain"]
  about: "explaining complex ideas"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can explain matters and ideas that are at times complex."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 64987, end: 65110 }
  source: "demonstrate an ability to solve problems, applying a range of methods and degree of creativity and open mindedness to do so"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "solve", "applying"]
  about: "solving problems creatively"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can solve problems using a range of methods with some creativity and an open mind."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 65113, end: 65210 }
  source: "present research findings clearly using a range of data visualisation and presentation techniques"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["present"]
  about: "presenting research findings"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can show research findings clearly through a range of methods for visualising and presenting data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 65217, end: 65323 }
  source: "analyse, evaluate and interpret information and ideas using insights from relevant literature in the field"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["analyse", "evaluate", "interpret"]
  about: "analysing and interpreting information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can analyse, judge and interpret information and ideas, drawing on the field's literature."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 65326, end: 65520 }
  source: "communicate information, ideas, problems and solutions effectively verbally and/or non-verbally, electronically and in writing, showing sensitivity and openness to different ideas and approaches"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating in many forms"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can get information, ideas, problems and solutions across well in speech or other non-written forms, online and in writing, with sensitivity and openness to other ideas and approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 65523, end: 65581 }
  source: "demonstrate competent numeracy and digital literacy skills"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "numeracy and digital literacy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can show competent numeracy and digital literacy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 65584, end: 65728 }
  source: "make useful contributions to group discussions and collaborative projects, showing an ability to listen, and, where necessary, leadership skills"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["make"]
  about: "group work, listening and leadership"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can contribute usefully to group discussion and shared projects, listening well and leading where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 65731, end: 65831 }
  source: "manage their learning and work with minimal supervision, responding to specific briefs and deadlines"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["manage", "responding"]
  about: "managing own learning to brief and deadline"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can manage their own learning and work with little supervision, meeting set briefs and deadlines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.5.b11
  locator: { number: "4.5.b11", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 65834, end: 65911 }
  source: "demonstrate flexibility, initiative and/or personal responsibility/resilience"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "flexibility, initiative and responsibility"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can show flexibility, initiative or personal responsibility and resilience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.5.b12
  locator: { number: "4.5.b12", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 65914, end: 65961 }
  source: "demonstrate an ability to reflect on their work"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "reflect"]
  about: "reflecting on own work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can reflect on their own work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.5.b13
  locator: { number: "4.5.b13", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 65964, end: 66094 }
  source: "apply entrepreneurial skills, if and where appropriate, in dealing with audiences, users, clients, consumers, markets and sources."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["apply"]
  about: "entrepreneurial skills"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate can use entrepreneurial skills, where they fit, with audiences, users, clients, consumers, markets and sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 66565, end: 66775 }
  source: "demonstrate a comprehensive knowledge and solid understanding of key debates and theoretical perspectives in Communication, Media, Film and Cultural Studies, including those that extend beyond the Western canon"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "key debates and theories of the field"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b1, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to show wide knowledge and secure understanding of the field's main debates and theoretical positions, including ones from beyond Western traditions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 66778, end: 66906 }
  source: "demonstrate an ability to engage in the critical analysis of media texts, using theoretical material, concepts and understanding"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "engage"]
  about: "analysing media texts with theory"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b2, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to analyse media texts critically with the help of theory and concepts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 66909, end: 67059 }
  source: "understand and interrogate the representational, technological and cultural significance of media, film, communication and cultural texts and contexts"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand", "interrogate"]
  about: "why texts and contexts matter"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b3, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to grasp and question why texts and contexts in these fields matter for representation, for technology and for culture."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 67062, end: 67235 }
  source: "demonstrate an ability to understand and critique the representational, technological and cultural significance of media, film, communication and cultural texts and contexts"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "understand", "critique"]
  about: "why texts and contexts matter"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b3, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to show that they understand, and can criticise, why texts and contexts in these fields matter for representation, for technology and for culture."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 67238, end: 67405 }
  source: "critically assess the role of media forms, including community and participatory media, in contributing to political and cultural debates and the contestation of power"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["assess"]
  about: "media forms, debate and power"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b5, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to assess critically how media forms, community and participatory media among them, feed political and cultural debate and struggles over power."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b6
  locator: { number: "4.7.b6", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 67408, end: 67572 }
  source: "consider the complex and intersecting ways in which diverse communities and organisations contribute to the development of media and cultural policies and practices"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["consider"]
  about: "communities shaping media and cultural policy"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b4, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to think through the complex, overlapping ways in which varied communities and organisations help shape media and cultural policy and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b7
  locator: { number: "4.7.b7", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 67575, end: 67707 }
  source: "critically engage with global issues, including sustainability practices and debates in relation to communication and cultural forms"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["engage"]
  about: "global issues and sustainability"
  themes: [theme:esd]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b6, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to engage critically with global questions, sustainability among them, as they bear on communication and cultural forms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b8
  locator: { number: "4.7.b8", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 67710, end: 67947 }
  source: "understand and apply understandings of communication technologies, practices and products not as 'neutral' but as developed and accessed in relation to their social, cultural, economic, historical, environmental and geographical contexts"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand", "apply"]
  about: "technologies and products are not neutral"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b7, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to understand and put to use the idea that communication technologies, practices and products are never neutral but take shape in their social, cultural, economic, historical, environmental and geographical settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b9
  locator: { number: "4.7.b9", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 67954, end: 68108 }
  source: "understand and critically assess how different social groups and organisations interact, engage with and make use of various forms of media to communicate"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand", "assess"]
  about: "how social groups use media"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b9, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to understand and assess critically how social groups and organisations interact with one another and use various media to communicate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b10
  locator: { number: "4.7.b10", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 68111, end: 68403 }
  source: "understand and critically assess diverse experiences and understandings of cultural value, including questions relating to how accounts of the world are created, maintained and reproduced, and how understandings of the self and the world are formed in relation to cultural texts and practices"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand", "assess"]
  about: "cultural value and how it is formed"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b8, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to understand and assess critically the varied ways cultural value is lived and understood, including how versions of the world get made, kept going and passed on and how people form a sense of self and world through cultural texts and practices."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b11
  locator: { number: "4.7.b11", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 68406, end: 68788 }
  source: "identify, critically evaluate and competently employ research methods suitable to a particular research context - these may include digital methodologies, close textual analysis, archive research, quantitative textual analysis and social research methods, research-by-practice, (auto)ethnography, critically reflective practice, audience research methods or participatory approaches"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["identify", "evaluate", "employ"]
  about: "choosing and using research methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b10, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to choose, weigh critically and use competently research methods fitted to a given research context, the range widened to quantitative textual analysis and social research methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b12
  locator: { number: "4.7.b12", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 68791, end: 68986 }
  source: "be able to locate, retrieve, critically evaluate and synthesise a range of data, sources and conceptual frameworks appropriate to research, production and professional practice in the chosen area"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["locate", "retrieve", "evaluate", "synthesise"]
  about: "finding and judging sources and frameworks"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b11, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to find, retrieve, assess critically and bring together a range of data, sources and conceptual frameworks suited to research, production and professional practice in their own area."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b13
  locator: { number: "4.7.b13", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 68989, end: 69155 }
  source: "draw on the strengths and evaluate the limits of relevant quantitative and/or qualitative methods, and be able to independently apply this knowledge in their own work"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["draw", "evaluate", "apply"]
  about: "strengths and limits of quantitative and qualitative methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b12, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to use the strengths, and judge the limits, of the quantitative or qualitative methods that fit, applying that knowledge independently in their own work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b14
  locator: { number: "4.7.b14", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 69158, end: 69259 }
  source: "design, research and present to a high standard an extended piece of research or practical equivalent"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["design", "research", "present"]
  about: "an extended research or practical project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b13, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to design, research and present an extended project, written or practical, to a high standard."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b15
  locator: { number: "4.7.b15", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 69262, end: 69429 }
  source: "demonstrate and apply theoretical understandings in their critical engagement with cultural and production practices depending on the specific focus of their programme"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "apply"]
  about: "theory in cultural and production practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b14, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to show and apply theoretical understanding when engaging critically with cultural and production practice, as the programme's focus allows."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b16
  locator: { number: "4.7.b16", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 69432, end: 69550 }
  source: "demonstrate a high standard of creative expression through practice depending on the specific focus of their programme"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "creative expression through practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b15, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to show creative expression of a high standard in practice, as the programme's focus allows."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b17
  locator: { number: "4.7.b17", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 69553, end: 69694 }
  source: "be able to creatively and critically synthesise new knowledge and understanding and reflect on their own learning experiences and performance"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["synthesise", "reflect"]
  about: "reflecting on learning and performance"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b16, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to bring new knowledge and understanding together creatively and critically, and reflect on their own learning and performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b18
  locator: { number: "4.7.b18", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 69697, end: 69931 }
  source: "understand and critically reflect on different traditions and trajectories in the development of media, communication and/or film studies as a subject and understand their implications for the discipline today and its cultural context"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand", "reflect"]
  about: "how the subject developed"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b17, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to understand and reflect critically on the different traditions and paths by which media, communication or film studies grew, and what they mean for the discipline and its cultural setting now."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b19
  locator: { number: "4.7.b19", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 69934, end: 70048 }
  source: "understand the need for an inclusive discipline and accord respect to diverse others within and beyond the subject"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand", "accord"]
  about: "an inclusive discipline and respect for others"
  themes: [theme:edi]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b18, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to understand why the discipline needs to be inclusive, and show respect to diverse people inside and outside the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b20
  locator: { number: "4.7.b20", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 70051, end: 70183 }
  source: "demonstrate an ability to actively engage in diverse discussions and debates in which their own opinions may be challenged by others"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "engage"]
  about: "openness in discussion and debate"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b19, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to take an active part in varied discussion and debate in which others may challenge their own views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.7.b21
  locator: { number: "4.7.b21", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 70186, end: 70384 }
  source: "apply their understanding to ethically and culturally responsible use of communication, media, film and cultural forms and technologies in both professional and everyday contexts to a high standard."
  stem: "4.7"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["apply"]
  about: "ethical, responsible use of media forms"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b20, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to use communication, media, film and cultural forms and technologies ethically and with cultural responsibility, at work and in daily life, to a high standard."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 70534, end: 70684 }
  source: "demonstrate a strong ability to select, critically evaluate and synthesise reading, research and primary sources using appropriate referencing formats"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "select", "evaluate", "synthesise"]
  about: "selecting and referencing sources"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b1, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to choose, judge critically and combine reading, research and primary sources with real skill, referencing them properly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 70687, end: 70794 }
  source: "show the ability to devise, sustain and critique an argument, including the evaluation of alternative views"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["show", "devise", "sustain", "critique"]
  about: "building and testing an argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b2, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to build, hold and criticise an argument, weighing other views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 70797, end: 70851 }
  source: "clearly explain complex concepts, theories and debates"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["explain"]
  about: "explaining complex ideas"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b3, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to explain complex concepts, theories and debates clearly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 70854, end: 71018 }
  source: "demonstrate a creative ability to solve problems, applying a range of methods to do so, and the ability to make decisions in complex and unpredictable circumstances"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "solve", "applying", "make"]
  about: "solving problems creatively"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b4, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to solve problems creatively with a range of methods, and make decisions in complex, unpredictable situations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 71025, end: 71122 }
  source: "present research findings clearly using a range of data visualisation and presentation techniques"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["present"]
  about: "presenting research findings"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b5, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to show research findings clearly through a range of methods for visualising and presenting data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.8.b6
  locator: { number: "4.8.b6", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 71125, end: 71254 }
  source: "analyse, critically evaluate, synthesise and interpret information and ideas using insights from relevant literature in the field"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["analyse", "evaluate", "synthesise", "interpret"]
  about: "analysing and interpreting information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b6, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to analyse, judge critically, combine and interpret information and ideas, drawing on the field's literature."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.8.b7
  locator: { number: "4.8.b7", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 71257, end: 71472 }
  source: "communicate information, ideas, problems and solutions verbally and/or non-verbally, electronically and in writing, with clear expression and style, showing sensitivity and openness to different ideas and approaches"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating in many forms"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b7, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to get information, ideas, problems and solutions across in speech or other non-written forms, online and in writing, with clear expression and style, and with sensitivity and openness to other ideas and approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.8.b8
  locator: { number: "4.8.b8", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 71475, end: 71533 }
  source: "demonstrate competent numeracy and digital literacy skills"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "numeracy and digital literacy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b8, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to show competent numeracy and digital literacy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.8.b9
  locator: { number: "4.8.b9", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 71536, end: 71731 }
  source: "consistently participate in group discussion and collaborative work, and make useful contributions to collaborative projects, showing an ability to listen, and, where necessary, leadership skills"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["participate", "make"]
  about: "group work, listening and leadership"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b9, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to take part consistently in group discussion and joint work and contribute usefully to shared projects, listening well and leading where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.8.b10
  locator: { number: "4.8.b10", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 71734, end: 71838 }
  source: "systematically manage their learning and work independently in response to specific briefs and deadlines"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["manage"]
  about: "managing own learning to brief and deadline"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b10, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to manage their own learning and work systematically and independently, meeting set briefs and deadlines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.8.b11
  locator: { number: "4.8.b11", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 71841, end: 71928 }
  source: "consistently demonstrate flexibility, initiative and personal responsibility/resilience"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "flexibility, initiative and responsibility"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b11, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to show flexibility, initiative and personal responsibility and resilience consistently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.8.b12
  locator: { number: "4.8.b12", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 71931, end: 71989 }
  source: "demonstrate an ability to reflect critically on their work"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "reflect"]
  about: "reflecting on own work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b12, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to reflect critically on their own work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.8.b13
  locator: { number: "4.8.b13", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 71992, end: 72138 }
  source: "apply a high level of entrepreneurial skills, if and where appropriate, in dealing with audiences, users, clients, consumers, markets and sources."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["apply"]
  about: "entrepreneurial skills"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b13, basis: inferred }
  paraphrase: "At the typical level, above the minimum, the graduate should be able to use entrepreneurial skills of a high level, where they fit, with audiences, users, clients, consumers, markets and sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b1
  locator: { number: "4.9.b1", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 72333, end: 72533 }
  source: "demonstrate exceptional knowledge and understanding of key debates and theoretical perspectives in Communication, Media, Film and Cultural Studies, including those that extend beyond the Western canon"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "key debates and theories of the field"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b1, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to show outstanding knowledge and understanding of the field's main debates and theoretical positions, including ones from beyond Western traditions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b2
  locator: { number: "4.9.b2", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 72536, end: 72676 }
  source: "demonstrate an exceptional ability to engage in the critical analysis of media texts, using theoretical material, concepts and understanding"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "engage"]
  about: "analysing media texts with theory"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b2, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to analyse media texts critically, with the help of theory and concepts, to an outstanding degree."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b3
  locator: { number: "4.9.b3", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 72679, end: 72846 }
  source: "demonstrate an exceptional understanding of the representational, technological and cultural significance of media, film, communication and cultural texts and contexts"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "why texts and contexts matter"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b4, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to show an outstanding grasp of why texts and contexts in these fields matter for representation, for technology and for culture."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b4
  locator: { number: "4.9.b4", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 72849, end: 73040 }
  source: "critically assess to an exceptional level the role of media forms, including community and participatory media, in contributing to political and cultural debates and the contestation of power"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["assess"]
  about: "media forms, debate and power"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b5, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to assess critically, to an outstanding level, how media forms, community and participatory media among them, feed political and cultural debate and struggles over power."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b5
  locator: { number: "4.9.b5", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 73043, end: 73218 }
  source: "critically evaluate the complex and intersecting ways in which diverse communities and organisations contribute to the development of media and cultural policies and practices"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["evaluate"]
  about: "communities shaping media and cultural policy"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b6, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to evaluate critically the complex, overlapping ways in which varied communities and organisations help shape media and cultural policy and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b6
  locator: { number: "4.9.b6", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 73221, end: 73353 }
  source: "critically engage with global issues, including sustainability practices and debates in relation to communication and cultural forms"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["engage"]
  about: "global issues and sustainability"
  themes: [theme:esd]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b7, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to engage critically with global questions, sustainability among them, as they bear on communication and cultural forms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b7
  locator: { number: "4.9.b7", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 73356, end: 73606 }
  source: "understand and consistently apply understandings of communication technologies, practices and products not as 'neutral' but as developed and accessed in relation to their social, cultural, economic, historical, environmental and geographical contexts"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand", "apply"]
  about: "technologies and products are not neutral"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b8, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to understand and consistently put to use the idea that communication technologies, practices and products are never neutral but take shape in their social, cultural, economic, historical, environmental and geographical settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b8
  locator: { number: "4.9.b8", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 73609, end: 73788 }
  source: "understand and critically assess to an exceptional level how different social groups and organisations interact, engage with, and make use of various forms of media to communicate"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand", "assess"]
  about: "how social groups use media"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b9, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to understand and assess critically, to an outstanding level, how social groups and organisations interact with one another and use various media to communicate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b9
  locator: { number: "4.9.b9", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 73795, end: 74089 }
  source: "understand and critically evaluate diverse experiences and understandings of cultural value, including questions relating to how accounts of the world are created, maintained and reproduced, and how understandings of the self and the world are formed in relation to cultural texts and practices"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand", "evaluate"]
  about: "cultural value and how it is formed"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b10, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to understand and evaluate critically the varied ways cultural value is lived and understood, including how versions of the world get made, kept going and passed on and how people form a sense of self and world through cultural texts and practices."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b10
  locator: { number: "4.9.b10", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 74092, end: 74474 }
  source: "identify, critically evaluate and competently employ research methods suitable to a particular research context - these may include digital methodologies, close textual analysis, archive research, quantitative textual analysis and social research methods, research-by-practice, (auto)ethnography, critically reflective practice, audience research methods or participatory approaches"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["identify", "evaluate", "employ"]
  about: "choosing and using research methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b11, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to choose, weigh critically and use competently research methods fitted to a given research context, the range widened to quantitative textual analysis and social research methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b11
  locator: { number: "4.9.b11", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 74477, end: 74672 }
  source: "be able to locate, retrieve, critically evaluate and synthesise a range of data, sources and conceptual frameworks appropriate to research, production and professional practice in the chosen area"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["locate", "retrieve", "evaluate", "synthesise"]
  about: "finding and judging sources and frameworks"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b12, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to find, retrieve, assess critically and bring together a range of data, sources and conceptual frameworks suited to research, production and professional practice in their own area."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b12
  locator: { number: "4.9.b12", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 74675, end: 74872 }
  source: "draw on the strengths and evaluate the limits of relevant quantitative and/or qualitative methods, and be able to independently apply this knowledge in their own work with minimal or no supervision"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["draw", "evaluate", "apply"]
  about: "strengths and limits of quantitative and qualitative methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b13, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to use the strengths, and judge the limits, of the quantitative or qualitative methods that fit, applying that knowledge independently in their own work with little or no supervision."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b13
  locator: { number: "4.9.b13", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 74875, end: 75013 }
  source: "design, research and present to an exceptional standard, and in a perceptive manner, an extended piece of research or practical equivalent"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["design", "research", "present"]
  about: "an extended research or practical project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b14, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to design, research and present an extended project, written or practical, to an outstanding standard and with insight."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b14
  locator: { number: "4.9.b14", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 75016, end: 75213 }
  source: "demonstrate and apply theoretical understandings consistently and convincingly in their critical engagement with cultural and production practices depending on the specific focus of their programme"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "apply"]
  about: "theory in cultural and production practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b15, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to show and apply theoretical understanding consistently and convincingly when engaging critically with cultural and production practice, as the programme's focus allows."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b15
  locator: { number: "4.9.b15", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 75216, end: 75352 }
  source: "demonstrate an exceptional standard of creative expression and flair through practice depending on the specific focus of their programme"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "creative expression through practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b16, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to show creative expression and flair of an outstanding standard in practice, as the programme's focus allows."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b16
  locator: { number: "4.9.b16", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 75355, end: 75507 }
  source: "be able to creatively and critically synthesise new knowledge and understanding and reflect critically on their own learning experiences and performance"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["synthesise", "reflect"]
  about: "reflecting on learning and performance"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b17, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to bring new knowledge and understanding together creatively and critically, and reflect critically on their own learning and performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b17
  locator: { number: "4.9.b17", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 75510, end: 75744 }
  source: "understand and critically reflect on different traditions and trajectories in the development of media, communication and/or film studies as a subject and understand their implications for the discipline today and its cultural context"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand", "reflect"]
  about: "how the subject developed"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b18, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to understand and reflect critically on the different traditions and paths by which media, communication or film studies grew, and what they mean for the discipline and its cultural setting now."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b18
  locator: { number: "4.9.b18", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 75747, end: 75861 }
  source: "understand the need for an inclusive discipline and accord respect to diverse others within and beyond the subject"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand", "accord"]
  about: "an inclusive discipline and respect for others"
  themes: [theme:edi]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b19, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to understand why the discipline needs to be inclusive, and show respect to diverse people inside and outside the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b19
  locator: { number: "4.9.b19", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 75864, end: 76008 }
  source: "demonstrate an exceptional ability to actively engage in diverse discussions and debates in which their own opinions may be challenged by others"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "engage"]
  about: "openness in discussion and debate"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b20, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to take an active part, to an outstanding degree, in varied discussion and debate in which others may challenge their own views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.9.b20
  locator: { number: "4.9.b20", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 76011, end: 76217 }
  source: "apply their understanding to ethically and culturally responsible use of communication, media, film and cultural forms and technologies in both professional and everyday contexts to an exceptional standard."
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["apply"]
  about: "ethical, responsible use of media forms"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b21, basis: inferred }
  paraphrase: "At the excellent level the graduate should be able to use communication, media, film and cultural forms and technologies ethically and with cultural responsibility, at work and in daily life, to an outstanding standard."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.10.b1
  locator: { number: "4.10.b1", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 76521, end: 76716 }
  source: "consistently demonstrate an exceptional ability to select, consider, evaluate, comment on and synthesise a broad range of research, primary sources, views and information and integrate references"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "select", "consider", "evaluate", "comment", "synthesise", "integrate"]
  about: "selecting and referencing sources"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b1, basis: inferred }
  paraphrase: "At the excellent level the graduate will be able to consistently choose, weigh, judge, comment on and combine a wide range of research, primary sources, views and information to an outstanding degree, working references in smoothly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.10.b2
  locator: { number: "4.10.b2", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 76719, end: 76837 }
  source: "show an exceptional ability to devise, sustain and critique an argument, including the evaluation of alternative views"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["show", "devise", "sustain", "critique"]
  about: "building and testing an argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b2, basis: inferred }
  paraphrase: "At the excellent level the graduate will be able to build, hold and criticise an argument to an outstanding degree, weighing other views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.10.b3
  locator: { number: "4.10.b3", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 76844, end: 76939 }
  source: "explain complex concepts, theories and debates in a sophisticated way and with critical insight"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["explain"]
  about: "explaining complex ideas"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b3, basis: inferred }
  paraphrase: "At the excellent level the graduate will be able to explain complex concepts, theories and debates with sophistication and critical insight."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.10.b4
  locator: { number: "4.10.b4", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 76942, end: 77041 }
  source: "demonstrate an exceptional creative ability to solve problems, applying a range of methods to do so"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "solve", "applying"]
  about: "solving problems creatively"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b4, basis: inferred }
  paraphrase: "At the excellent level the graduate will be able to solve problems with outstanding creativity, using a range of methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.10.b5
  locator: { number: "4.10.b5", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 77044, end: 77133 }
  source: "present research findings using a range of data visualisation and presentation techniques"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["present"]
  about: "presenting research findings"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b5, basis: inferred }
  paraphrase: "At the excellent level the graduate will be able to show research findings through a range of methods for visualising and presenting data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.10.b6
  locator: { number: "4.10.b6", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 77136, end: 77301 }
  source: "analyse, critically evaluate, synthesise and interpret information and ideas to a consistently exceptional level using insights from relevant literature in the field"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["analyse", "evaluate", "synthesise", "interpret"]
  about: "analysing and interpreting information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b6, basis: inferred }
  paraphrase: "At the excellent level the graduate will be able to analyse, judge critically, combine and interpret information and ideas to a consistently outstanding level, drawing on the field's literature."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.10.b7
  locator: { number: "4.10.b7", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 77304, end: 77543 }
  source: "communicate information, ideas, problems and solutions to an accomplished level verbally and/or non-verbally, electronically and in writing, with clear expression and style showing sensitivity and openness to different ideas and approaches"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating in many forms"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b7, basis: inferred }
  paraphrase: "At the excellent level the graduate will be able to get information, ideas, problems and solutions across to an accomplished level in speech or other non-written forms, online and in writing, with clear expression and style, and with sensitivity and openness to other ideas and approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.10.b8
  locator: { number: "4.10.b8", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 77546, end: 77606 }
  source: "demonstrate exceptional numeracy and digital literacy skills"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "numeracy and digital literacy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b8, basis: inferred }
  paraphrase: "At the excellent level the graduate will be able to show outstanding numeracy and digital literacy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.10.b9
  locator: { number: "4.10.b9", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 77609, end: 77806 }
  source: "able to lead and participate in group discussions and make clear, authoritative and valuable contributions to collaborative projects, showing an exceptional ability to listen to the views of others"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["lead", "participate", "make"]
  about: "group work, listening and leadership"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b9, basis: inferred }
  paraphrase: "At the excellent level the graduate will be able to lead and take part in group discussion and make clear, authoritative and valuable contributions to shared projects, listening to others with outstanding care."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.10.b10
  locator: { number: "4.10.b10", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 77809, end: 77911 }
  source: "consistently manage their learning and work independently in response to specific briefs and deadlines"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["manage"]
  about: "managing own learning to brief and deadline"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b10, basis: inferred }
  paraphrase: "At the excellent level the graduate will be able to manage their own learning and work consistently and independently, meeting set briefs and deadlines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.10.b11
  locator: { number: "4.10.b11", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 77914, end: 78013 }
  source: "demonstrate exceptional initiative and personal responsibility and the ability to work autonomously"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "work"]
  about: "flexibility, initiative and responsibility"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b11, basis: inferred }
  paraphrase: "At the excellent level the graduate will be able to show outstanding initiative and personal responsibility, and work autonomously."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.10.b12
  locator: { number: "4.10.b12", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 78016, end: 78075 }
  source: "demonstrate an exceptional ability to reflect on their work"
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "reflect"]
  about: "reflecting on own work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b12, basis: inferred }
  paraphrase: "At the excellent level the graduate will be able to reflect on their own work with outstanding ability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.10.b13
  locator: { number: "4.10.b13", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 78078, end: 78232 }
  source: "apply an exceptional level of entrepreneurial skills, if and where appropriate, in dealing with audiences, users, clients, consumers, markets and sources."
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["apply"]
  about: "entrepreneurial skills"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b13, basis: inferred }
  paraphrase: "At the excellent level the graduate will be able to use entrepreneurial skills of an outstanding level, where they fit, with audiences, users, clients, consumers, markets and sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.13
  locator: { number: "4.13", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 79078, end: 79347 }
  source: "Master's degrees are awarded to students who demonstrate systematic subject- specific knowledge, understanding and skills, and exceptional mastery of general skills as listed in the undergraduate standards but with the additional expectations that students demonstrate:"
  stem: none
  statementType: requirement
  rung: none
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["awarded", "demonstrate"]
  about: "master's award: the excellent-level general skills and more"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's degree in the subject is awarded to students who show systematic subject knowledge, understanding and skills and outstanding command of the general skills listed for undergraduates, together with four further expectations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.13.b1
  locator: { number: "4.13.b1", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 79350, end: 79517 }
  source: "understanding and awareness that is at, or informed by, the forefront of Communication, Media, Film and Cultural Studies academic research and/or professional practice"
  stem: "4.13"
  statementType: requirement
  rung: none
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: []
  about: "understanding at the forefront of research or practice"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Beyond the honours standards, master's graduates show understanding and awareness that reach, or draw on, the leading edge of academic research or professional practice in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.13.b2
  locator: { number: "4.13.b2", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 79520, end: 79675 }
  source: "originality in the application of knowledge, and practical understanding of how the boundaries of knowledge in the discipline are advanced through research"
  stem: "4.13"
  statementType: requirement
  rung: none
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: []
  about: "originality and how knowledge advances"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Beyond the honours standards, master's graduates show originality in applying knowledge, with a practical grasp of how research pushes the discipline's knowledge forward."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.13.b3
  locator: { number: "4.13.b3", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 79682, end: 79819 }
  source: "understanding and enabling the critical evaluation of current research, research methodologies and advanced scholarship in the discipline"
  stem: "4.13"
  statementType: requirement
  rung: none
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["enabling"]
  about: "evaluating current research and methodologies"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Beyond the honours standards, master's graduates show understanding that allows critical evaluation of current research, research methods and advanced scholarship in the discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/communication-media-film-and-cultural-studies-2024/4.13.b4
  locator: { number: "4.13.b4", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 79822, end: 79927 }
  source: "development of their disciplinary knowledge and understanding, development of new skills to a high level."
  stem: "4.13"
  statementType: requirement
  rung: none
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: []
  about: "developing knowledge and new skills"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Beyond the honours standards, master's graduates show growth in disciplinary knowledge and understanding, and new skills built to a high level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.7
  forPractitioner: { text: "Design taught master's courses on the undergraduate core but require advanced, nuanced work in the specialism, in critical and creative skill or in practice, with outputs that consolidate or create knowledge.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "On a taught master's in the subject, you must show advanced and nuanced knowledge and skills in your specialism, your critical and creative work or your practice, consolidating what is known or adding to it through your outputs.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a requirement (the issuer's word is 'require') for taught postgraduate degrees at FHEQ Level 7 and FQHEIS Level 11. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.7. Do not apply it to honours study or claim it sets a fixed output type. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.13, its items qaa/communication-media-film-and-cultural-studies-2024/4.13.b1 to qaa/communication-media-film-and-cultural-studies-2024/4.13.b4 and the FHEQ master's descriptor qaa/fheq-2024/4.17.b1 (spine:7)."
  author-agent-dialogue: "Raise it when a student weighs a master's or a team designs one. Say plainly that master's work builds on the degree but asks for advanced, nuanced work in a specialism or practice. Ask: 'Where would your work need to go further than it did at honours level?' Avoid judging an undergraduate against it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.9.b1
  forPractitioner: { text: "Where the course's focus includes it, plan for graduates to be able to set what they learn in its historical, political, global, social, economic, cultural, environmental and technological settings.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on your course, you will be able to set what you learn in its historical, political, global, social, economic, cultural, environmental and technological settings.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (purposes and characteristics, section 1), outside the rungs: graduates will, depending on the course, show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.9. Do not present it as a threshold standard or as required of every graduate. Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the reference framework's strand:knowledge at spine:6."
  author-agent-dialogue: "Raise it when a student or a team asks what graduates of these varied courses can do. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'What changes when you read a media text against its economic or environmental setting rather than its style alone?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.9.b2
  forPractitioner: { text: "Where the course's focus includes it, plan for graduates to be able to grasp how social groups overlap and how groups and individuals take up and engage with media and communication in different ways.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on your course, you will be able to grasp how social groups overlap and how groups and individuals take up and engage with media and communication in different ways.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (purposes and characteristics, section 1), outside the rungs: graduates will, depending on the course, show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.9. Do not present it as a threshold standard or as required of every graduate. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b9, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the reference framework's strand:knowledge at spine:6."
  author-agent-dialogue: "Raise it when a student or a team asks what graduates of these varied courses can do. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Which groups use the media you study differently, and why?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.9.b3
  forPractitioner: { text: "Where the course's focus includes it, plan for graduates to be able to judge critically when understanding, making and evaluating relevant forms, contexts and scenarios, and show how the knowledge and skills of the degree apply in real professional settings.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on your course, you will be able to judge critically when understanding, making and evaluating relevant forms, contexts and scenarios, and show how the knowledge and skills of the degree apply in real professional settings.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (purposes and characteristics, section 1), outside the rungs: graduates will, depending on the course, show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.9. Do not present it as a threshold standard or as required of every graduate. Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and the reference framework's strand:application at spine:6."
  author-agent-dialogue: "Raise it when a student or a team asks what graduates of these varied courses can do. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Where have you used something from your course in a real or simulated professional task?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.9.b4
  forPractitioner: { text: "Where the course's focus includes it, plan for graduates to be able to weigh and evaluate their own work reflexively against academic or professional codes, conventions, issues and debates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on your course, you will be able to weigh and evaluate your own work reflexively against academic or professional codes, conventions, issues and debates.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (purposes and characteristics, section 1), outside the rungs: graduates will, depending on the course, show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.9. Do not present it as a threshold standard or as required of every graduate. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b12, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3 and the reference framework's strand:autonomy at spine:6."
  author-agent-dialogue: "Raise it when a student or a team asks what graduates of these varied courses can do. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Which professional or academic code would you judge your last project against?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.10.b1
  forPractitioner: { text: "Plan for graduates to be able to engage critically with the field's leading thinkers and arguments and put them to good use; the issuer expects this of most graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually be able to engage critically with the field's leading thinkers and arguments and put them to good use.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (research, critical analysis, production and professional practice, section 1), outside the rungs: graduates will typically show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.10. Do not present it as a threshold standard or as required of every graduate. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the reference framework's strand:knowledge at spine:6."
  author-agent-dialogue: "Raise it when a student asks what research and practice skills the degree builds, or a team maps them. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Which thinker in the field do you find most useful, and what have you done with their ideas?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.10.b2
  forPractitioner: { text: "Plan for graduates to be able to understand how forms of communication, media, film and culture arose over time and how social, cultural, environmental and technological change shaped them; the issuer expects this of most graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually be able to understand how forms of communication, media, film and culture arose over time and how social, cultural, environmental and technological change shaped them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (research, critical analysis, production and professional practice, section 1), outside the rungs: graduates will typically show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.10. Do not present it as a threshold standard or as required of every graduate. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b17, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the reference framework's strand:knowledge at spine:6."
  author-agent-dialogue: "Raise it when a student asks what research and practice skills the degree builds, or a team maps them. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'How did a form you study come about, and what changes drove it?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.10.b3
  forPractitioner: { text: "Plan for graduates to be able to pursue sustained, independent, critical enquiry and research; the issuer expects this of most graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually be able to pursue sustained, independent, critical enquiry and research.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (research, critical analysis, production and professional practice, section 1), outside the rungs: graduates will typically show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.10. Do not present it as a threshold standard or as required of every graduate. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b13, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and the reference framework's strand:application at spine:6."
  author-agent-dialogue: "Raise it when a student asks what research and practice skills the degree builds, or a team maps them. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'What is the longest piece of independent research you have carried through, and what kept it going?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.10.b4
  forPractitioner: { text: "Plan for graduates to be able to frame research questions or lines of enquiry that feed into practice; the issuer expects this of most graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually be able to frame research questions or lines of enquiry that feed into practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (research, critical analysis, production and professional practice, section 1), outside the rungs: graduates will typically show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.10. Do not present it as a threshold standard or as required of every graduate. Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Raise it when a student asks what research and practice skills the degree builds, or a team maps them. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'What question is your current project really asking, and how does it shape what you make or do?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.10.b5
  forPractitioner: { text: "Plan for graduates to be able to choose, use and evaluate research methods that fit the context and the problem being researched; the issuer expects this of most graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually be able to choose, use and evaluate research methods that fit the context and the problem being researched.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (research, critical analysis, production and professional practice, section 1), outside the rungs: graduates will typically show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.10. Do not present it as a threshold standard or as required of every graduate. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the reference framework's strand:application at spine:6."
  author-agent-dialogue: "Raise it when a student asks what research and practice skills the degree builds, or a team maps them. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Why is your chosen method right for this question, and what would another method have shown?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.10.b6
  forPractitioner: { text: "Plan for graduates to be able to find, retrieve, judge and use data, sources and conceptual frameworks that suit research, production and professional practice in their own area; the issuer expects this of most graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually be able to find, retrieve, judge and use data, sources and conceptual frameworks that suit research, production and professional practice in your own area.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (research, critical analysis, production and professional practice, section 1), outside the rungs: graduates will typically show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.10. Do not present it as a threshold standard or as required of every graduate. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b11, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Raise it when a student asks what research and practice skills the degree builds, or a team maps them. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'How did you find and judge the sources behind your last project?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.10.b7
  forPractitioner: { text: "Plan for graduates to be able to use the strengths, and know the limits, of fitting quantitative or qualitative methods, and apply this critically in their own work; the issuer expects this of most graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually be able to use the strengths, and know the limits, of fitting quantitative or qualitative methods, and apply this critically in your own work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (research, critical analysis, production and professional practice, section 1), outside the rungs: graduates will typically show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.10. Do not present it as a threshold standard or as required of every graduate. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b12, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and the reference framework's strand:application at spine:6."
  author-agent-dialogue: "Raise it when a student asks what research and practice skills the degree builds, or a team maps them. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'What could your method not tell you, and how did you allow for that?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.10.b8
  forPractitioner: { text: "Plan for graduates to be able to analyse well and work through problems that may be theoretical, practical or professional; the issuer expects this of most graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually be able to analyse well and work through problems that may be theoretical, practical or professional.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (research, critical analysis, production and professional practice, section 1), outside the rungs: graduates will typically show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.10. Do not present it as a threshold standard or as required of every graduate. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b4, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.2 and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Raise it when a student asks what research and practice skills the degree builds, or a team maps them. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'What problem in your work took the most thought to solve, and how did you go about it?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.10.b9
  forPractitioner: { text: "Plan for graduates to be able to show sensitivity to the subjective positions and intersections of different cultures, their own included, knowing that research and production are never neutral; the issuer expects this of most graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually be able to show sensitivity to the subjective positions and intersections of different cultures, your own included, knowing that research and production are never neutral.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (research, critical analysis, production and professional practice, section 1), outside the rungs: graduates will typically show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.10. Do not present it as a threshold standard or as required of every graduate. Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Raise it when a student asks what research and practice skills the degree builds, or a team maps them. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'How did your own position shape the research or production you did?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.10.b10
  forPractitioner: { text: "Plan for graduates to be able to show imagination and creative insight that suit the context; the issuer expects this of most graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually be able to show imagination and creative insight that suit the context.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (research, critical analysis, production and professional practice, section 1), outside the rungs: graduates will typically show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.10. Do not present it as a threshold standard or as required of every graduate. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b15, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and the reference framework's strand:application at spine:6."
  author-agent-dialogue: "Raise it when a student asks what research and practice skills the degree builds, or a team maps them. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Where in your recent work did you take a creative risk, and did it suit the brief?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.10.b11
  forPractitioner: { text: "Plan for graduates to be able to show awareness of, or attention to, sustainable ways of working; the issuer expects this of most graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually be able to show awareness of, or attention to, sustainable ways of working.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (research, critical analysis, production and professional practice, section 1), outside the rungs: graduates will typically show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.10. Do not present it as a threshold standard or as required of every graduate. Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Raise it when a student asks what research and practice skills the degree builds, or a team maps them. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'What did you do in your last production or project to reduce its environmental cost?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.10.b12
  forPractitioner: { text: "Plan for graduates to be able to find, understand, criticise and keep to the ethical codes of relevant subject and industry bodies and to research standards; the issuer expects this of most graduates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually be able to find, understand, criticise and keep to the ethical codes of relevant subject and industry bodies and to research standards.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (research, critical analysis, production and professional practice, section 1), outside the rungs: graduates will typically show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.10. Do not present it as a threshold standard or as required of every graduate. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b20, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and the reference framework's strand:application at spine:6."
  author-agent-dialogue: "Raise it when a student asks what research and practice skills the degree builds, or a team maps them. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Which ethical code applies to your project, and where would you question it?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.11.b1
  forPractitioner: { text: "Where it fits the course, give students the chance to bring critical understanding to the ethical, culturally responsible use of media and cultural forms, practices and technologies of every kind, at work and in daily life.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to bring critical understanding to the ethical, culturally responsible use of media and cultural forms, practices and technologies of every kind, at work and in daily life.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (citizenship, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.11. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b20, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and the reference framework's strand:application at spine:6."
  author-agent-dialogue: "Raise it when the talk turns to media, culture and civic life. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'When did you last make a choice about using media responsibly, and what guided it?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.11.b2
  forPractitioner: { text: "Where it fits the course, give students the chance to express themselves through communication, media, film and culture in ways shaped by cultural, media, digital and information literacies.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to express yourself through communication, media, film and culture in ways shaped by cultural, media, digital and information literacies.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (citizenship, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.11. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and the reference framework's strand:communication at spine:6."
  author-agent-dialogue: "Raise it when the talk turns to media, culture and civic life. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'How does what you know about media literacy change the way you post or publish?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.11.b3
  forPractitioner: { text: "Where it fits the course, give students the chance to appraise critically the social, cultural and political debates that bear on communication, media, film and culture.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to appraise critically the social, cultural and political debates that bear on communication, media, film and culture.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (citizenship, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.11. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Raise it when the talk turns to media, culture and civic life. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Which current debate about the media do you have a view on, and what is it based on?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.11.b4
  forPractitioner: { text: "Where it fits the course, give students the chance to build the confidence to take part as responsible, informed citizens.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to build the confidence to take part as responsible, informed citizens.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (citizenship, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.11. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and the reference framework's strand:autonomy at spine:6."
  author-agent-dialogue: "Raise it when the talk turns to media, culture and civic life. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Where outside your studies have you used what you know to take part in public life?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.11.b5
  forPractitioner: { text: "Where it fits the course, give students the chance to understand media and cultural policies and how they are made and put into effect.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to understand media and cultural policies and how they are made and put into effect.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (citizenship, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.11. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the reference framework's strand:knowledge at spine:6."
  author-agent-dialogue: "Raise it when the talk turns to media, culture and civic life. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Which media policy affects your area, and who shaped it?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.11.b6
  forPractitioner: { text: "Where it fits the course, give students the chance to think about how varied communities and organisations can help shape media and cultural policy and practice.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to think about how varied communities and organisations can help shape media and cultural policy and practice.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (citizenship, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.11. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b4, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the reference framework's strand:knowledge at spine:6."
  author-agent-dialogue: "Raise it when the talk turns to media, culture and civic life. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Which community or group has changed how the media in your area work?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.11.b7
  forPractitioner: { text: "Where it fits the course, give students the chance to analyse how community and participatory media and communication feed cultural and political debate and challenges to power.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to analyse how community and participatory media and communication feed cultural and political debate and challenges to power.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (citizenship, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.11. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Raise it when the talk turns to media, culture and civic life. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'What has a community or participatory medium achieved that mainstream media did not?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.11.b8
  forPractitioner: { text: "Where it fits the course, give students the chance to think about global sustainability practice and debate as they bear on communication and cultural forms.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to think about global sustainability practice and debate as they bear on communication and cultural forms.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (citizenship, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.11. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b6, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Raise it when the talk turns to media, culture and civic life. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'How do the media you study report or shape debates on sustainability?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.11.b9
  forPractitioner: { text: "Where it fits the course, give students the chance to stay open to varied discussion and debate in which others may question their own informed views and lived experience.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to stay open to varied discussion and debate in which others may question your own informed views and lived experience.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (citizenship, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.11. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b19, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and the reference framework's strand:communication at spine:6."
  author-agent-dialogue: "Raise it when the talk turns to media, culture and civic life. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'When did someone's view change your mind, and how did you respond?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.12.b1
  forPractitioner: { text: "Where it fits the course, give students the chance to work flexibly, creatively and independently, aware of ethical issues, directing themselves and reflecting on what they do.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to work flexibly, creatively and independently, aware of ethical issues, directing yourself and reflecting on what you do.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (transferable skills, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.12. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and the reference framework's strand:autonomy at spine:6."
  author-agent-dialogue: "Raise it when a student asks about transferable or employability skills. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'How do you organise your own work when no one is setting the pace?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.12.b2
  forPractitioner: { text: "Where it fits the course, give students the chance to communicate well with others in person, sensitive to cultural difference and open to knowledge, ideas and approaches new to them.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to communicate well with others in person, sensitive to cultural difference and open to knowledge, ideas and approaches new to you.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (transferable skills, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.12. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and the reference framework's strand:communication at spine:6."
  author-agent-dialogue: "Raise it when a student asks about transferable or employability skills. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'When did you last have to explain something to someone with a very different background, and how did it go?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.12.b3
  forPractitioner: { text: "Where it fits the course, give students the chance to gather, order and use ideas and information to build clear arguments and put them across well in writing, speech, non-verbal, visual or other forms.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to gather, order and use ideas and information to build clear arguments and put them across well in writing, speech, non-verbal, visual or other forms.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (transferable skills, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.12. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b2, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Raise it when a student asks about transferable or employability skills. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'How did you turn your notes into an argument, and which form suited it best?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.12.b4
  forPractitioner: { text: "Where it fits the course, give students the chance to find and produce information and judge sources when doing independent research.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to find and produce information and judge sources when doing independent research.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (transferable skills, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.12. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b1, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Raise it when a student asks about transferable or employability skills. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'How do you decide whether a source is good enough to use?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.12.b5
  forPractitioner: { text: "Where it fits the course, give students the chance to plan and run supervised projects that they direct.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to plan and run supervised projects that you direct.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (transferable skills, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.12. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and the reference framework's strand:autonomy at spine:6."
  author-agent-dialogue: "Raise it when a student asks about transferable or employability skills. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'What did you do to keep your last self-directed project on track?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.12.b6
  forPractitioner: { text: "Where it fits the course, give students the chance to work well in a group or team, listening, contributing and leading well at different times.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to work well in a group or team, listening, contributing and leading well at different times.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (transferable skills, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.12. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b9, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and the reference framework's strand:communication at spine:6."
  author-agent-dialogue: "Raise it when a student asks about transferable or employability skills. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'What role did you play in your last group project, and would you choose it again?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.12.b7
  forPractitioner: { text: "Where it fits the course, give students the chance to produce work to a set length, format, brief and deadline, citing sources and ideas properly and solving problems where that helps.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to produce work to a set length, format, brief and deadline, citing sources and ideas properly and solving problems where that helps.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (transferable skills, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.12. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b10, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and the reference framework's strand:autonomy at spine:6."
  author-agent-dialogue: "Raise it when a student asks about transferable or employability skills. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'What helps you meet a brief and a deadline at the same time?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.12.b8
  forPractitioner: { text: "Where it fits the course, give students the chance to use entrepreneurial skills, where they fit, with audiences, users, clients, consumers, markets or sources.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to use entrepreneurial skills, where they fit, with audiences, users, clients, consumers, markets or sources.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (transferable skills, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.12. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b13, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and the reference framework's strand:application at spine:6."
  author-agent-dialogue: "Raise it when a student asks about transferable or employability skills. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Where could you turn a project into something an audience or client would pay for or use?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.12.b9
  forPractitioner: { text: "Where it fits the course, give students the chance to build the information literacy to find and judge suitable sources and evidence with an eye to cultural context and sensitivity.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to build the information literacy to find and judge suitable sources and evidence with an eye to cultural context and sensitivity.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (transferable skills, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.12. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Raise it when a student asks about transferable or employability skills. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'How would you check whether a source treats the culture it describes fairly?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.12.b10
  forPractitioner: { text: "Where it fits the course, give students the chance to engage critically with a range of media practices and competences.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to engage critically with a range of media practices and competences.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (transferable skills, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.12. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Raise it when a student asks about transferable or employability skills. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Which media practice have you tried that you would now question?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.12.b11
  forPractitioner: { text: "Where it fits the course, give students the chance to see that communication technologies, practices and products are never neutral but take shape in their social, cultural, economic, historical, environmental and geographical settings.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to see that communication technologies, practices and products are never neutral but take shape in their social, cultural, economic, historical, environmental and geographical settings.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (transferable skills, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.12. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b7, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Raise it when a student asks about transferable or employability skills. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Whose interests shaped a technology you use every day?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.12.b12
  forPractitioner: { text: "Where it fits the course, give students the chance to look into career openings to get ready for possible jobs.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "You may be able to look into career openings to get ready for possible jobs.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an outcome in the subject's purposes (transferable skills, section 1), outside the rungs: graduates may show it, at FHEQ Level 6 (FQHEIS Level 10) for the honours degree. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.12. Do not present it as a threshold standard or as required of every graduate (the issuer says 'may'). Set it beside the threshold lists 4.4 and 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3 and the reference framework's strand:autonomy at spine:6."
  author-agent-dialogue: "Raise it when a student asks about transferable or employability skills. Put it plainly, in the second person, to a student, and as a course design aim to staff. Ask: 'Which careers have you looked into, and what would you need to get there?' Do not read the issuer's list aloud or present it as a pass requirement."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.16
  forPractitioner: { text: "Build a commitment to equality, diversity and inclusion into every course and practice, in policy and in what staff do, so that all students and staff learn and work in inclusive settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on courses and their institutions; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) under the EDI theme, for every course in the field. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.16. Do not claim it sets a legal duty or names measures. Set it beside qaa/communication-media-film-and-cultural-studies-2024/1.17, qaa/communication-media-film-and-cultural-studies-2024/3.7 and the student outcome qaa/communication-media-film-and-cultural-studies-2024/4.4.b18."
  author-agent-dialogue: "Raise it with a programme team reviewing inclusion. Ask: 'Where in this course is the commitment to EDI visible in practice, not only in policy?' Do not present it to a student as their duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.17
  forPractitioner: { text: "Treat EDI as compulsory in course design and delivery: set policies, practices and systems that must work for fairness and equity for everyone and support these values consistently and openly, mindful of intersecting inequalities.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design and the systems around it; the student meets its effect", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a provider obligation (must) under the EDI theme, the strongest wording in the statement. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.17. Do not claim it is a statutory duty: the front matter says the statement carries none. Set it beside qaa/communication-media-film-and-cultural-studies-2024/1.16 and qaa/communication-media-film-and-cultural-studies-2024/3.7."
  author-agent-dialogue: "Raise it when a team audits its policies or systems for fairness. Ask: 'Which of our processes would treat two students with different backgrounds differently, and is that fair?' Do not give it to a student as their duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.18
  forPractitioner: { text: "Recruit students and staff from across society, with active policies that reach and support under-represented groups, and run selection and interviews to good practice in every respect.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on recruitment and admissions; not a standard for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on admissions and staffing under the EDI theme. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.18. Do not claim it sets quotas or targets. Set it beside qaa/communication-media-film-and-cultural-studies-2024/1.16 and qaa/communication-media-film-and-cultural-studies-2024/1.17."
  author-agent-dialogue: "Raise it with admissions or a programme team reviewing who applies and who is selected. Ask: 'Which groups are under-represented among our applicants, and what are we doing to reach them?' Do not present it to a student as their duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.19
  forPractitioner: { text: "Weigh the emotional, functional and technical sides of accessibility together, and make it central to how the course is designed, taught and assessed, with inclusion as a guiding principle at every level.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) under the accessibility theme. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.19. Do not claim it sets legal accessibility standards. Set it beside qaa/communication-media-film-and-cultural-studies-2024/1.20, qaa/communication-media-film-and-cultural-studies-2024/1.21 and qaa/communication-media-film-and-cultural-studies-2024/3.10."
  author-agent-dialogue: "Raise it when a team reviews a module for access. Ask: 'Which emotional, functional or technical barrier in this module have we not yet removed?' Do not give it to a student as their task."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.20
  forPractitioner: { text: "Make reasonable adjustments for equal access, work to close attainment gaps linked to accessibility, and handle each accessibility request with respect and understanding.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and institution; the student benefits from it", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) under the accessibility theme. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.20. Do not restate it as a legal test of what is reasonable. Set it beside qaa/communication-media-film-and-cultural-studies-2024/1.19 and qaa/communication-media-film-and-cultural-studies-2024/1.21."
  author-agent-dialogue: "Raise it when a team handles accessibility requests or reviews attainment data. Ask: 'How quickly and respectfully do we respond to a request for adjustment?' With a student, point to the support it promises rather than any duty on them."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.21
  forPractitioner: { text: "Supply learning resources on time in formats that suit students' needs, fit support to each student in a supportive setting, and teach with a pedagogy of care built on trust, inclusion, respect and support.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on teaching and support; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) under the accessibility theme; 3.10 repeats much of it under EDI. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.21. Do not claim it fixes formats or deadlines. Set it beside qaa/communication-media-film-and-cultural-studies-2024/1.19, qaa/communication-media-film-and-cultural-studies-2024/1.20 and qaa/communication-media-film-and-cultural-studies-2024/3.10."
  author-agent-dialogue: "Raise it when a team plans resources or student support. Ask: 'Would every student in this cohort be able to use these materials on the day they need them?' Do not put it to a student as their duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.23
  forPractitioner: { text: "Use sustainability as a lens when designing content, assessment, employability, delivery and facilities, ask how the course can change unsustainable practice rather than repeat it, and read this statement with the QAA and Advance HE guidance on education for sustainable development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) under the sustainability theme. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.23. Do not claim it sets an ESD outcome by itself. Set it beside qaa/communication-media-film-and-cultural-studies-2024/1.27, qaa/communication-media-film-and-cultural-studies-2024/1.29, the student outcomes qaa/communication-media-film-and-cultural-studies-2024/4.4.b6 and qaa/communication-media-film-and-cultural-studies-2024/1.10.b11, and std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise it when a team redesigns a course or reviews its facilities. Ask: 'Where does this course help students challenge unsustainable practice rather than reproduce it?' Do not present it to a student as their duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.27
  forPractitioner: { text: "Integrate education for sustainable development throughout the course, not only in specialist modules, and use assessment, placements and employability work to influence industry practice as well as prepare students for it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on curriculum design; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) under the sustainability theme. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.27. Do not claim it bans specialist modules: it asks that ESD not be confined to them. Set it beside qaa/communication-media-film-and-cultural-studies-2024/1.23 and qaa/communication-media-film-and-cultural-studies-2024/1.28."
  author-agent-dialogue: "Raise it when a team maps where sustainability appears. Ask: 'If we removed the specialist module, where would sustainability still be taught and assessed?' Do not give it to a student as their duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.28
  forPractitioner: { text: "Use the SDGs to help frame the curriculum, and look reflexively to other external references on sustainable development so that the course pushes action on sustainability through global and interdisciplinary perspectives.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on curriculum framing; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) under the sustainability theme, on the external references a curriculum uses. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.28. Do not claim the SDGs are required content. Set it beside qaa/communication-media-film-and-cultural-studies-2024/1.27, qaa/communication-media-film-and-cultural-studies-2024/1.29 and qaa/communication-media-film-and-cultural-studies-2024/3.17."
  author-agent-dialogue: "Raise it when a team chooses the frameworks behind its sustainability teaching. Ask: 'Besides the SDGs, which external reference would best fit what our students make and study?' Do not present it to a student as their duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/1.29
  forPractitioner: { text: "Encourage students to reflect on the sustainability of their own practice, for example through self-assessment of their activities, and draw on external frameworks, such as BAFTA albert's education partnership, in curriculum design.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on teaching to encourage reflection; the student outcome is 1.10.b11", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) under the sustainability theme. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 1.29. Do not claim BAFTA albert accreditation is required: the issuer names it as one possible resource. Set it beside the student outcome qaa/communication-media-film-and-cultural-studies-2024/1.10.b11, qaa/communication-media-film-and-cultural-studies-2024/1.23 and qaa/communication-media-film-and-cultural-studies-2024/1.28."
  author-agent-dialogue: "Raise it when a student plans a production or a team designs reflective tasks. With staff ask: 'Where do students assess the sustainability of their own production work?' With a student, invite reflection rather than present a duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/2.12
  forPractitioner: { text: "On joint and combined routes, plan for students to reach the core subject and generic skills and add others from the partner subject, with room for interdisciplinary work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study the subject as part of a joint or combined degree, you will gain its core subject and general skills and add others from your other subject, with chances to explore where the two meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expected outcome (will) for joint and combined honours students at FHEQ Level 6. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 2.12. Do not claim it names which skills are core: the statement does not mark them. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b1 and qaa/communication-media-film-and-cultural-studies-2024/4.5.b1 at the threshold."
  author-agent-dialogue: "Raise it when a joint honours student asks whether the same standards apply to them. Ask: 'Which core skills does this subject give you, and what does your other subject add?' Avoid suggesting they must meet every item on every list."
- statement: qaa/communication-media-film-and-cultural-studies-2024/3.7
  forPractitioner: { text: "Diversify methods, viewpoints, subjects and approaches across the whole course, not in one module, and keep developing EDI knowledge and practice in module content, learning resources, theory and assessment design.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on curriculum design; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) under the EDI theme. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 3.7. Do not claim it sets a quota for diverse content. Set it beside qaa/communication-media-film-and-cultural-studies-2024/1.16, qaa/communication-media-film-and-cultural-studies-2024/3.8 and the student outcome qaa/communication-media-film-and-cultural-studies-2024/4.4.b1 on traditions beyond the West."
  author-agent-dialogue: "Raise it in a curriculum or reading-list review. Ask: 'Whose methods and viewpoints are missing from this module, and is what we have more than a token?' Do not put it to a student as their duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/3.8
  forPractitioner: { text: "Design the course for a diverse student body, with inclusion and belonging in view, and encourage students into critical dialogue that challenges settled paradigms on gender, sexuality, faith, class, race, disability and the legacies of empire.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a statement of course design and what courses encourage; its outcomes for the student are 4.4.b18 and 4.4.b19", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a provider expectation (will) under the EDI theme. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 3.8. Do not claim the list of topics is compulsory content: the issuer gives it as examples. Set it beside qaa/communication-media-film-and-cultural-studies-2024/3.7, qaa/communication-media-film-and-cultural-studies-2024/3.9 and the student outcomes qaa/communication-media-film-and-cultural-studies-2024/4.4.b18 and qaa/communication-media-film-and-cultural-studies-2024/4.4.b19."
  author-agent-dialogue: "Raise it when a team plans seminars on contested topics. Ask: 'Where do students get to challenge an established paradigm, and how do we keep that dialogue safe?' Do not give it to a student as a duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/3.9
  forPractitioner: { text: "Engage and support students as critical, self-reflective learners who examine how the discipline's leading approaches can exclude people, and invite reflection on how they are taught and how they learn and behave.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on teaching; its outcomes for the student are 4.4.b16 and 4.5.b12", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) under the EDI theme. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 3.9. Do not claim it requires a set reflective assignment. Set it beside qaa/communication-media-film-and-cultural-studies-2024/3.8, qaa/communication-media-film-and-cultural-studies-2024/4.4.b16 and qaa/communication-media-film-and-cultural-studies-2024/4.5.b12."
  author-agent-dialogue: "Raise it when a team designs reflective tasks. Ask: 'Where do students reflect on how the way they are taught might exclude others?' With a student, invite that reflection rather than present a duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/3.10
  forPractitioner: { text: "Create inclusive learning that is accessible to every student and promotes equity: supply accessible resources on time, fit support to each student, and teach with a pedagogy of care built on trust, inclusion, respect and support.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on teaching and support; the student meets its effect", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a provider expectation (will, then should) carried by both the EDI and the accessibility themes; its later sentences repeat 1.21. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 3.10. Do not count it twice when mapping: cite 1.21 for the shared sentences. Set it beside qaa/communication-media-film-and-cultural-studies-2024/1.19, qaa/communication-media-film-and-cultural-studies-2024/1.21 and qaa/communication-media-film-and-cultural-studies-2024/3.7."
  author-agent-dialogue: "Raise it when a team reviews inclusion and access in a module. Ask: 'Could every student here take part fully this week, and how would we know?' Do not put it to a student as their duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/3.17
  forPractitioner: { text: "Encourage students to explore how enterprise can serve sustainable development: sustainable media production and distribution, responsible consumption and production, and projects that tackle social and environmental problems in line with frameworks such as the SDGs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on teaching to encourage; the student outcomes are 4.5.b13 and 4.4.b6", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) joining the enterprise and sustainability themes. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 3.17. Do not claim the SDGs are a required framework. Set it beside qaa/communication-media-film-and-cultural-studies-2024/1.28, qaa/communication-media-film-and-cultural-studies-2024/4.5.b13 and qaa/communication-media-film-and-cultural-studies-2024/4.4.b6."
  author-agent-dialogue: "Raise it when a team plans enterprise teaching or a student pitches a venture. With staff ask: 'Where do students test a business idea against its environmental and social cost?' With a student, invite the question rather than present a duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/3.18
  forPractitioner: { text: "Map assessment of learning outcomes to the skills set out in section 1 (the purposes, research and practice, citizenship and transferable skills lists) and treat assessment as part of learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on assessment design. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 3.18; its 'paragraphs 1.8-1.12' is a cross-reference, not a statement. Do not claim every listed skill must be assessed separately. Set it beside the outcome lists qaa/communication-media-film-and-cultural-studies-2024/1.9.b1, qaa/communication-media-film-and-cultural-studies-2024/1.10.b1, qaa/communication-media-film-and-cultural-studies-2024/1.11.b1 and qaa/communication-media-film-and-cultural-studies-2024/1.12.b1."
  author-agent-dialogue: "Raise it when a team maps assessments to outcomes. Ask: 'Which of the section 1 skills does no assessment on this course touch?' Do not present it to a student as their duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/3.21
  forPractitioner: { text: "Teach students to use emerging technologies, AI among them, well and ethically and to question how they change professional norms; make assessment responsive to these tools while still assessing subject knowledge, understanding and skills and protecting academic integrity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should learn to use new technologies, including AI, well and ethically, and keep asking how they change the norms of professional work; expect your assessments to test your own knowledge and skills.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) on students and on assessment design, the statement's one passage on generative AI. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 3.21, and point to QAA's guidance on generative AI, which the issuer names. Do not claim it bans or mandates particular AI tools. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b8 on digital literacy and qaa/communication-media-film-and-cultural-studies-2024/4.4.b20 on ethical use."
  author-agent-dialogue: "Raise it when a student asks how far they may use AI tools, or when a team revises assessment. Say plainly that you should use such tools well and ethically and think about how they change the work. Ask: 'How did a tool change your work, and what did you check yourself?' Avoid giving rules the course has not set."
- statement: qaa/communication-media-film-and-cultural-studies-2024/3.23
  forPractitioner: { text: "Give students constructive feedback throughout their studies, by several means (written and spoken comments, group discussion, technology, peer and self-assessment), and use it to build self-reflection and self-criticism.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on teaching staff to give feedback; the student benefits from it", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on feedback. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 3.23. Do not claim it sets turnaround times. Set it beside qaa/communication-media-film-and-cultural-studies-2024/3.24, qaa/communication-media-film-and-cultural-studies-2024/4.5.b12 and qaa/communication-media-film-and-cultural-studies-2024/4.4.b16."
  author-agent-dialogue: "Raise it when a team reviews its feedback practice or a student says feedback is not helping. With staff ask: 'Does our feedback build the student's own ability to judge their work?' With a student, ask what feedback they have had and how they used it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/3.24
  forPractitioner: { text: "Give formative as well as summative feedback, early, during and after assessment, aimed at how the student can improve both the task and their wider skills and knowledge, with summative judgements tied to the stated outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on teaching staff; the student benefits from it", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on feedback design, with the issuer's term feedforward. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 3.24. Do not claim it prescribes how many formative tasks to set. Set it beside qaa/communication-media-film-and-cultural-studies-2024/3.23."
  author-agent-dialogue: "Raise it when a team plans assessment calendars. Ask: 'Where does a student get feedback early enough to act on it before the summative task?' With a student, ask how they used their last feedforward."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.2
  forPractitioner: { text: "When judging achievement above the threshold, use the institution's own method and refer to Annex D's descriptions of the four honours classifications; Annex D can also guide postgraduate certificates and diplomas at Level 7 or 11.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the institution in setting its classification criteria; not a standard for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) that links the rungs to Annex D (std:doc:qaa-fheq-2024-framework, Annex D). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.2. Do not claim the typical or excellent rung equals a given class: the statement makes no such match. Set it beside qaa/fheq-2024/annex-d/summary/r1/3rd to /1st and the rung items qaa/communication-media-film-and-cultural-studies-2024/4.4.b1, qaa/communication-media-film-and-cultural-studies-2024/4.7.b1 and qaa/communication-media-film-and-cultural-studies-2024/4.9.b1."
  author-agent-dialogue: "Raise it when a team writes marking criteria or classification rules. Ask: 'How do our criteria for each class line up with Annex D and with the three rungs?' Do not give it to a student as their duty."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b1
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can show knowledge and understanding of the field's main debates and theoretical positions, including ones from beyond Western traditions; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to show knowledge and understanding of the field's main debates and theoretical positions, including ones from beyond Western traditions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on key debates and theories of the field, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 1). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b1 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r2/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on key debates and theories of the field, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Which major debate in the field could you explain, and whose voices from beyond Western traditions does it take in?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b2
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can analyse media texts with the help of theory and concepts; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to analyse media texts with the help of theory and concepts.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on analysing media texts with theory, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 2). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b2 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and Annex D's qaa/fheq-2024/annex-d/knowledge/r2/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on analysing media texts with theory, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Which concept helped you most in reading your last media text?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b3
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can grasp why texts and contexts in these fields matter for representation, for technology and for culture; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to grasp why texts and contexts in these fields matter for representation, for technology and for culture.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on why texts and contexts matter, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 3). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b3 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r1/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on why texts and contexts matter, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Why does this text or setting matter beyond its content?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b4
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can think about how varied communities and organisations help shape media and cultural policy and practice; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to think about how varied communities and organisations help shape media and cultural policy and practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on communities shaping media and cultural policy, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 4). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b6 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r3/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on communities shaping media and cultural policy, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Which community or organisation has shaped a media policy you know?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b5
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can analyse how media forms, community and participatory media among them, feed political and cultural debate and struggles over power; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to analyse how media forms, community and participatory media among them, feed political and cultural debate and struggles over power.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on media forms, debate and power, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 5). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b5 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's qaa/fheq-2024/annex-d/knowledge/r3/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on media forms, debate and power, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Which medium has given a group a voice in a political debate?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b6
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can think about global questions, sustainability among them, as they bear on communication and cultural forms; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to think about global questions, sustainability among them, as they bear on communication and cultural forms.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on global issues and sustainability, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 6). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b7 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and Annex D's qaa/fheq-2024/annex-d/knowledge/r3/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on global issues and sustainability, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Which global issue shows up in the media you study?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b7
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can see that communication technologies, practices and products are never neutral but are made and reached through their social, cultural, economic, historical, environmental and geographical settings; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to see that communication technologies, practices and products are never neutral but are made and reached through their social, cultural, economic, historical, environmental and geographical settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on technologies and products are not neutral, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 7). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b8 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and Annex D's qaa/fheq-2024/annex-d/knowledge/r2/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on technologies and products are not neutral, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Whose interests shaped a technology you use every day?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b8
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can recognise how cultural value is lived and understood, including how versions of the world get made, kept going and passed on and how people form a sense of self and world through cultural texts and practices; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to recognise how cultural value is lived and understood, including how versions of the world get made, kept going and passed on and how people form a sense of self and world through cultural texts and practices.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on cultural value and how it is formed, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 8). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b10 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r2/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on cultural value and how it is formed, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Who decides what counts as good culture, and how?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b9
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can understand how social groups and organisations interact with one another and use various media to communicate; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to understand how social groups and organisations interact with one another and use various media to communicate.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on how social groups use media, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 9). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b9 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r1/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on how social groups use media, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'How does one group you know use media differently from another?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b10
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can choose, weigh and use research methods that suit the context, such as digital methods, close reading of texts, archives, practice-based research, (auto)ethnography, reflective practice, audience research or participatory designs; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to choose, weigh and use research methods that suit the context, such as digital methods, close reading of texts, archives, practice-based research, (auto)ethnography, reflective practice, audience research or participatory designs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on choosing and using research methods, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 10). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b11 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and Annex D's qaa/fheq-2024/annex-d/practical/r1/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on choosing and using research methods, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Which method would suit your question, and why?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b11
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can find, retrieve, assess and use a range of data, sources and conceptual frameworks suited to research, production and professional practice in their own area; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to find, retrieve, assess and use a range of data, sources and conceptual frameworks suited to research, production and professional practice in your own area.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on finding and judging sources and frameworks, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 11). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b12 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and Annex D's qaa/fheq-2024/annex-d/cognitive/r1/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on finding and judging sources and frameworks, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Where did you find the sources for your last project, and how did you judge them?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b12
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can use the strengths, and know the limits, of the quantitative or qualitative methods that fit, applying that knowledge in their own work; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to use the strengths, and know the limits, of the quantitative or qualitative methods that fit, applying that knowledge in your own work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on strengths and limits of quantitative and qualitative methods, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 12). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b13 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and Annex D's qaa/fheq-2024/annex-d/practical/r2/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on strengths and limits of quantitative and qualitative methods, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'What can your method not tell you?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b13
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can research and present an extended project, written or practical; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to research and present an extended project, written or practical.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on an extended research or practical project, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 13). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b14 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r2/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on an extended research or practical project, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'What is your extended project, and how will you present it?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b14
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can show understanding of, or skill in, cultural and production practice, bringing theory to bear on how things are made, as the course's focus allows; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to show understanding of, or skill in, cultural and production practice, bringing theory to bear on how things are made, as the course's focus allows.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on theory in cultural and production practice, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 14). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b15 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r1/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on theory in cultural and production practice, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Where did a theory change how you made something?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b15
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can show creative expression in practice, as the course's focus allows; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to show creative expression in practice, as the course's focus allows.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on creative expression through practice, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 15). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b16 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r3/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on creative expression through practice, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Which piece of practice best shows your creative voice?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b16
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can think back on what they have newly learned and understood, and on their own learning and performance; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to think back on what you have newly learned and understood, and on your own learning and performance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on reflecting on learning and performance, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 16). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b17 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3 and Annex D's qaa/fheq-2024/annex-d/transferable/r5/3rd (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on reflecting on learning and performance, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'What did you learn from your last piece of feedback?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b17
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can understand how media, communication or film studies grew as a subject and what that means for the discipline and its cultural setting now; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to understand how media, communication or film studies grew as a subject and what that means for the discipline and its cultural setting now.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on how the subject developed, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 17). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b18 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r1/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on how the subject developed, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Where did the subject come from, and why does that matter now?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b18
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can understand why the discipline needs to be inclusive, and show respect to diverse people inside and outside the subject; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to understand why the discipline needs to be inclusive, and show respect to diverse people inside and outside the subject.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on an inclusive discipline and respect for others, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 18). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b19 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r2/3rd (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on an inclusive discipline and respect for others, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Whose voices are missing from what you study?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b19
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can stay open to varied discussion and debate in which others may challenge their own views; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to stay open to varied discussion and debate in which others may challenge your own views.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on openness in discussion and debate, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 19). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b20 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r1/3rd (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on openness in discussion and debate, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'When did someone challenge your view, and how did you respond?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.4.b20
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can use communication, media, film and cultural forms and technologies ethically and with cultural responsibility, at work and in daily life; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to use communication, media, film and cultural forms and technologies ethically and with cultural responsibility, at work and in daily life.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on ethical, responsible use of media forms, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.4 (threshold level, subject knowledge and skills, item 20). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b21 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r1/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on ethical, responsible use of media forms, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'What ethical choice did you make in your last piece of media work?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b1
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can choose, judge and comment on reading, research and primary sources, referencing them properly; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to choose, judge and comment on reading, research and primary sources, referencing them properly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on selecting and referencing sources, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.5 (threshold level, generic skills, item 1). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b1 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and Annex D's qaa/fheq-2024/annex-d/cognitive/r1/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on selecting and referencing sources, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'How do you choose which sources to use and cite?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b2
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can build, hold and criticise an argument, giving some thought to other views; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to build, hold and criticise an argument, giving some thought to other views.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on building and testing an argument, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.5 (threshold level, generic skills, item 2). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b2 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and Annex D's qaa/fheq-2024/annex-d/cognitive/r2/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on building and testing an argument, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'What is the strongest objection to your argument?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b3
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can explain matters and ideas that are at times complex; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to explain matters and ideas that are at times complex.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on explaining complex ideas, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.5 (threshold level, generic skills, item 3). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b3 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r1/3rd (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on explaining complex ideas, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Can you explain the hardest idea in your last essay in two sentences?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b4
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can solve problems using a range of methods with some creativity and an open mind; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to solve problems using a range of methods with some creativity and an open mind.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on solving problems creatively, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.5 (threshold level, generic skills, item 4). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b4 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.2 and Annex D's qaa/fheq-2024/annex-d/cognitive/r3/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on solving problems creatively, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'What problem did you solve recently, and how?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b5
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can show research findings clearly through a range of methods for visualising and presenting data; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to show research findings clearly through a range of methods for visualising and presenting data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on presenting research findings, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.5 (threshold level, generic skills, item 5). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b5 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/practical/r4/3rd (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on presenting research findings, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Which chart or format best showed your findings?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b6
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can analyse, judge and interpret information and ideas, drawing on the field's literature; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to analyse, judge and interpret information and ideas, drawing on the field's literature.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on analysing and interpreting information, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.5 (threshold level, generic skills, item 6). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b6 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's qaa/fheq-2024/annex-d/knowledge/r3/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on analysing and interpreting information, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'What did the literature help you see in your material?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b7
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can get information, ideas, problems and solutions across well in speech or other non-written forms, online and in writing, with sensitivity and openness to other ideas and approaches; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to get information, ideas, problems and solutions across well in speech or other non-written forms, online and in writing, with sensitivity and openness to other ideas and approaches.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on communicating in many forms, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.5 (threshold level, generic skills, item 7). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b7 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r1/3rd (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on communicating in many forms, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Which form of communication do you find hardest, and why?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b8
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can show competent numeracy and digital literacy; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to show competent numeracy and digital literacy.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on numeracy and digital literacy, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.5 (threshold level, generic skills, item 8). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b8 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r1/3rd (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on numeracy and digital literacy, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Where have you used numbers or digital tools in your work?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b9
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can contribute usefully to group discussion and shared projects, listening well and leading where needed; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to contribute usefully to group discussion and shared projects, listening well and leading where needed.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on group work, listening and leadership, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.5 (threshold level, generic skills, item 9). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b9 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and Annex D's qaa/fheq-2024/annex-d/transferable/r2/3rd (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on group work, listening and leadership, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'What did you add to your last group project?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b10
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can manage their own learning and work with little supervision, meeting set briefs and deadlines; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to manage your own learning and work with little supervision, meeting set briefs and deadlines.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on managing own learning to brief and deadline, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.5 (threshold level, generic skills, item 10). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b10 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and Annex D's qaa/fheq-2024/annex-d/transferable/r3/3rd (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on managing own learning to brief and deadline, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'How do you plan your work to meet a deadline?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b11
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can show flexibility, initiative or personal responsibility and resilience; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to show flexibility, initiative or personal responsibility and resilience.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on flexibility, initiative and responsibility, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.5 (threshold level, generic skills, item 11). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b11 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and Annex D's qaa/fheq-2024/annex-d/transferable/r4/3rd (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on flexibility, initiative and responsibility, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'When did you have to adapt a plan, and how did you cope?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b12
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can reflect on their own work; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to reflect on your own work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on reflecting on own work, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.5 (threshold level, generic skills, item 12). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b12 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3 and Annex D's qaa/fheq-2024/annex-d/transferable/r5/3rd (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on reflecting on own work, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'What would you change in your last piece of work?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.5.b13
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate can use entrepreneurial skills, where they fit, with audiences, users, clients, consumers, markets and sources; this is the floor for the award.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, at the least, be able to use entrepreneurial skills, where they fit, with audiences, users, clients, consumers, markets and sources.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate in the subject will have shown on entrepreneurial skills, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.5 (threshold level, generic skills, item 13). Do not call it a regulatory requirement or claim it holds at another level. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b13 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r1/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on entrepreneurial skills, or when a programme team checks a module against the threshold. Put it in plain words, in the second person, to a student, and as the floor the course must evidence to staff. Ask: 'Where could your work meet a real audience or client?' Do not read the list aloud or offer the typical or excellent level as the pass standard."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b1
  forPractitioner: { text: "Typical level: design for most students to be able to show wide knowledge and secure understanding of the field's main debates and theoretical positions, including ones from beyond Western traditions, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to show wide knowledge and secure understanding of the field's main debates and theoretical positions, including ones from beyond Western traditions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on key debates and theories of the field, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 1). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b1 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b1 (excellent), qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r2/2.1, a match we infer (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on key debates and theories of the field asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'Could you set two theoretical positions side by side and say where they truly disagree?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b2
  forPractitioner: { text: "Typical level: design for most students to be able to analyse media texts critically with the help of theory and concepts, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to analyse media texts critically with the help of theory and concepts.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on analysing media texts with theory, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 2). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b2 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b2 (excellent), qaa/fheq-2024/4.15.b2 and Annex D's qaa/fheq-2024/annex-d/knowledge/r2/2.1, a match we infer (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on analysing media texts with theory asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'Where does your analysis question the text rather than describe it?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b3
  forPractitioner: { text: "Typical level: design for most students to be able to grasp and question why texts and contexts in these fields matter for representation, for technology and for culture, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to grasp and question why texts and contexts in these fields matter for representation, for technology and for culture.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on why texts and contexts matter, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 3). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b3 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b3 (excellent), qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r1/2.1, a match we infer (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on why texts and contexts matter asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'What question would you put to the way this text represents people?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b4
  forPractitioner: { text: "Typical level: design for most students to be able to show that they understand, and can criticise, why texts and contexts in these fields matter for representation, for technology and for culture, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to show that you understand, and can criticise, why texts and contexts in these fields matter for representation, for technology and for culture.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on why texts and contexts matter, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 4). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b3 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b3 (excellent), qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r1/2.1, a match we infer (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on why texts and contexts matter asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'Where would you criticise the accepted view of why this text matters?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b5
  forPractitioner: { text: "Typical level: design for most students to be able to assess critically how media forms, community and participatory media among them, feed political and cultural debate and struggles over power, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to assess critically how media forms, community and participatory media among them, feed political and cultural debate and struggles over power.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on media forms, debate and power, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 5). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b5 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b4 (excellent), qaa/fheq-2024/4.15.b7 and Annex D's qaa/fheq-2024/annex-d/knowledge/r3/2.1, a match we infer (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on media forms, debate and power asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How far did that medium really shift power, and how do you know?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b6
  forPractitioner: { text: "Typical level: design for most students to be able to think through the complex, overlapping ways in which varied communities and organisations help shape media and cultural policy and practice, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to think through the complex, overlapping ways in which varied communities and organisations help shape media and cultural policy and practice.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on communities shaping media and cultural policy, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 6). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b4 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b5 (excellent), qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r3/2.1, a match we infer (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on communities shaping media and cultural policy asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How do several groups' interests overlap or clash in one policy you know?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b7
  forPractitioner: { text: "Typical level: design for most students to be able to engage critically with global questions, sustainability among them, as they bear on communication and cultural forms, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to engage critically with global questions, sustainability among them, as they bear on communication and cultural forms.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on global issues and sustainability, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 7). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b6 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b6 (excellent), qaa/fheq-2024/4.15.b4 and Annex D's qaa/fheq-2024/annex-d/knowledge/r3/2.1, a match we infer (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on global issues and sustainability asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How do the media you study frame a global issue, and what do they leave out?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b8
  forPractitioner: { text: "Typical level: design for most students to be able to understand and put to use the idea that communication technologies, practices and products are never neutral but take shape in their social, cultural, economic, historical, environmental and geographical settings, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to understand and put to use the idea that communication technologies, practices and products are never neutral but take shape in their social, cultural, economic, historical, environmental and geographical settings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on technologies and products are not neutral, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 8). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b7 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b7 (excellent), qaa/fheq-2024/4.15.b4 and Annex D's qaa/fheq-2024/annex-d/knowledge/r2/2.1, a match we infer (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on technologies and products are not neutral asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How did that idea change the way you analysed or made something?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b9
  forPractitioner: { text: "Typical level: design for most students to be able to understand and assess critically how social groups and organisations interact with one another and use various media to communicate, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to understand and assess critically how social groups and organisations interact with one another and use various media to communicate.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on how social groups use media, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 9). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b9 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b8 (excellent), qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r1/2.1, a match we infer (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on how social groups use media asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'What explains those differences, and how sure are you?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b10
  forPractitioner: { text: "Typical level: design for most students to be able to understand and assess critically the varied ways cultural value is lived and understood, including how versions of the world get made, kept going and passed on and how people form a sense of self and world through cultural texts and practices, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to understand and assess critically the varied ways cultural value is lived and understood, including how versions of the world get made, kept going and passed on and how people form a sense of self and world through cultural texts and practices.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on cultural value and how it is formed, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 10). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b8 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b9 (excellent), qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r2/2.1, a match we infer (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on cultural value and how it is formed asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How would you challenge a common judgement of cultural value?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b11
  forPractitioner: { text: "Typical level: design for most students to be able to choose, weigh critically and use competently research methods fitted to a given research context, the range widened to quantitative textual analysis and social research methods, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to choose, weigh critically and use competently research methods fitted to a given research context, the range widened to quantitative textual analysis and social research methods.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on choosing and using research methods, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 11). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b10 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b10 (excellent), qaa/fheq-2024/4.15.b2 and Annex D's qaa/fheq-2024/annex-d/practical/r1/2.1, a match we infer (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on choosing and using research methods asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'What would a different method have shown, and why did you not use it?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b12
  forPractitioner: { text: "Typical level: design for most students to be able to find, retrieve, assess critically and bring together a range of data, sources and conceptual frameworks suited to research, production and professional practice in their own area, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to find, retrieve, assess critically and bring together a range of data, sources and conceptual frameworks suited to research, production and professional practice in your own area.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on finding and judging sources and frameworks, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 12). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b11 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b11 (excellent), qaa/fheq-2024/4.15.b5 and Annex D's qaa/fheq-2024/annex-d/cognitive/r1/2.1, a match we infer (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on finding and judging sources and frameworks asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How did you combine sources that disagreed?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b13
  forPractitioner: { text: "Typical level: design for most students to be able to use the strengths, and judge the limits, of the quantitative or qualitative methods that fit, applying that knowledge independently in their own work, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to use the strengths, and judge the limits, of the quantitative or qualitative methods that fit, applying that knowledge independently in your own work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on strengths and limits of quantitative and qualitative methods, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 13). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b12 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b12 (excellent), qaa/fheq-2024/4.15.b2 and Annex D's qaa/fheq-2024/annex-d/practical/r2/2.1, a match we infer (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on strengths and limits of quantitative and qualitative methods asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How did you allow for the limits of your method without being told to?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b14
  forPractitioner: { text: "Typical level: design for most students to be able to design, research and present an extended project, written or practical, to a high standard, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to design, research and present an extended project, written or practical, to a high standard.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on an extended research or practical project, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 14). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b13 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b13 (excellent), qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r2/2.1, a match we infer (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on an extended research or practical project asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'What makes your project design sound, from question to presentation?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b15
  forPractitioner: { text: "Typical level: design for most students to be able to show and apply theoretical understanding when engaging critically with cultural and production practice, as the programme's focus allows, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to show and apply theoretical understanding when engaging critically with cultural and production practice, as the programme's focus allows.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on theory in cultural and production practice, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 15). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b14 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b14 (excellent), qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r1/2.1, a match we infer (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on theory in cultural and production practice asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How does theory shape your critique of a production practice?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b16
  forPractitioner: { text: "Typical level: design for most students to be able to show creative expression of a high standard in practice, as the programme's focus allows, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to show creative expression of a high standard in practice, as the programme's focus allows.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on creative expression through practice, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 16). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b15 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b15 (excellent), qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r3/2.1, a match we infer (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on creative expression through practice asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'What would lift the craft of your best piece further?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b17
  forPractitioner: { text: "Typical level: design for most students to be able to bring new knowledge and understanding together creatively and critically, and reflect on their own learning and performance, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to bring new knowledge and understanding together creatively and critically, and reflect on your own learning and performance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on reflecting on learning and performance, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 17). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b16 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b16 (excellent), qaa/fheq-2024/4.15.b9.3 and Annex D's qaa/fheq-2024/annex-d/transferable/r5/2.1, a match we infer (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on reflecting on learning and performance asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How have new ideas changed the way you work?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b18
  forPractitioner: { text: "Typical level: design for most students to be able to understand and reflect critically on the different traditions and paths by which media, communication or film studies grew, and what they mean for the discipline and its cultural setting now, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to understand and reflect critically on the different traditions and paths by which media, communication or film studies grew, and what they mean for the discipline and its cultural setting now.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on how the subject developed, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 18). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b17 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b17 (excellent), qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r1/2.1, a match we infer (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on how the subject developed asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'Which tradition in the subject do you work in, and what are its blind spots?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b19
  forPractitioner: { text: "Typical level: design for most students to be able to understand why the discipline needs to be inclusive, and show respect to diverse people inside and outside the subject, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to understand why the discipline needs to be inclusive, and show respect to diverse people inside and outside the subject.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on an inclusive discipline and respect for others, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 19). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b18 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b18 (excellent), qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r2/2.1, a match we infer (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on an inclusive discipline and respect for others asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How does your own work make room for voices that are missing?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b20
  forPractitioner: { text: "Typical level: design for most students to be able to take an active part in varied discussion and debate in which others may challenge their own views, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to take an active part in varied discussion and debate in which others may challenge your own views.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on openness in discussion and debate, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 20). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b19 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b19 (excellent), qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r1/2.1, a match we infer (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on openness in discussion and debate asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How do you join a debate when you expect to be challenged?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.7.b21
  forPractitioner: { text: "Typical level: design for most students to be able to use communication, media, film and cultural forms and technologies ethically and with cultural responsibility, at work and in daily life, to a high standard, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to use communication, media, film and cultural forms and technologies ethically and with cultural responsibility, at work and in daily life, to a high standard.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on ethical, responsible use of media forms, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.7 (typical level, subject knowledge and skills, item 21). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.4.b20 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.9.b20 (excellent), qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r1/2.1, a match we infer (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on ethical, responsible use of media forms asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How did you test the ethics of your work before releasing it?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b1
  forPractitioner: { text: "Typical level: design for most students to be able to choose, judge critically and combine reading, research and primary sources with real skill, referencing them properly, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to choose, judge critically and combine reading, research and primary sources with real skill, referencing them properly.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on selecting and referencing sources, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.8 (typical level, generic skills, item 1). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b1 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.10.b1 (excellent), qaa/fheq-2024/4.15.b5 and Annex D's qaa/fheq-2024/annex-d/cognitive/r1/2.1, a match we infer (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on selecting and referencing sources asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How did you bring your sources together into one view?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b2
  forPractitioner: { text: "Typical level: design for most students to be able to build, hold and criticise an argument, weighing other views, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to build, hold and criticise an argument, weighing other views.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on building and testing an argument, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.8 (typical level, generic skills, item 2). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b2 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.10.b2 (excellent), qaa/fheq-2024/4.15.b3.1 and Annex D's qaa/fheq-2024/annex-d/cognitive/r2/2.1, a match we infer (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on building and testing an argument asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How did you weigh the other views against your own?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b3
  forPractitioner: { text: "Typical level: design for most students to be able to explain complex concepts, theories and debates clearly, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to explain complex concepts, theories and debates clearly.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on explaining complex ideas, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.8 (typical level, generic skills, item 3). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b3 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.10.b3 (excellent), qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r1/2.1, a match we infer (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on explaining complex ideas asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How would you explain that theory to a first-year student?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b4
  forPractitioner: { text: "Typical level: design for most students to be able to solve problems creatively with a range of methods, and make decisions in complex, unpredictable situations, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to solve problems creatively with a range of methods, and make decisions in complex, unpredictable situations.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on solving problems creatively, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.8 (typical level, generic skills, item 4). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b4 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.10.b4 (excellent), qaa/fheq-2024/4.15.b9.2 and Annex D's qaa/fheq-2024/annex-d/cognitive/r3/2.1, a match we infer (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on solving problems creatively asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'What decision did you make when the situation was unclear?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b5
  forPractitioner: { text: "Typical level: design for most students to be able to show research findings clearly through a range of methods for visualising and presenting data, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to show research findings clearly through a range of methods for visualising and presenting data.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on presenting research findings, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.8 (typical level, generic skills, item 5). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b5 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.10.b5 (excellent), qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/practical/r4/2.1, a match we infer (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on presenting research findings asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How did you choose between ways of showing your data?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b6
  forPractitioner: { text: "Typical level: design for most students to be able to analyse, judge critically, combine and interpret information and ideas, drawing on the field's literature, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to analyse, judge critically, combine and interpret information and ideas, drawing on the field's literature.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on analysing and interpreting information, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.8 (typical level, generic skills, item 6). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b6 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.10.b6 (excellent), qaa/fheq-2024/4.15.b7 and Annex D's qaa/fheq-2024/annex-d/knowledge/r3/2.1, a match we infer (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on analysing and interpreting information asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'Where did you combine ideas from different authors into your own reading?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b7
  forPractitioner: { text: "Typical level: design for most students to be able to get information, ideas, problems and solutions across in speech or other non-written forms, online and in writing, with clear expression and style, and with sensitivity and openness to other ideas and approaches, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to get information, ideas, problems and solutions across in speech or other non-written forms, online and in writing, with clear expression and style, and with sensitivity and openness to other ideas and approaches.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on communicating in many forms, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.8 (typical level, generic skills, item 7). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b7 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.10.b7 (excellent), qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r1/2.1, a match we infer (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on communicating in many forms asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How do you adjust your style for different readers?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b8
  forPractitioner: { text: "Typical level: design for most students to be able to show competent numeracy and digital literacy, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to show competent numeracy and digital literacy.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on numeracy and digital literacy, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.8 (typical level, generic skills, item 8). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b8 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.10.b8 (excellent), qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r1/2.1, a match we infer (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on numeracy and digital literacy asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'Which digital tool could you teach someone else to use?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b9
  forPractitioner: { text: "Typical level: design for most students to be able to take part consistently in group discussion and joint work and contribute usefully to shared projects, listening well and leading where needed, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to take part consistently in group discussion and joint work and contribute usefully to shared projects, listening well and leading where needed.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on group work, listening and leadership, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.8 (typical level, generic skills, item 9). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b9 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.10.b9 (excellent), qaa/fheq-2024/4.15.b9.1 and Annex D's qaa/fheq-2024/annex-d/transferable/r2/2.1, a match we infer (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on group work, listening and leadership asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How do you keep up your part in a group over a whole project?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b10
  forPractitioner: { text: "Typical level: design for most students to be able to manage their own learning and work systematically and independently, meeting set briefs and deadlines, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to manage your own learning and work systematically and independently, meeting set briefs and deadlines.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on managing own learning to brief and deadline, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.8 (typical level, generic skills, item 10). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b10 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.10.b10 (excellent), qaa/fheq-2024/4.15.b5 and Annex D's qaa/fheq-2024/annex-d/transferable/r3/2.1, a match we infer (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on managing own learning to brief and deadline asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'What system keeps your independent work on track?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b11
  forPractitioner: { text: "Typical level: design for most students to be able to show flexibility, initiative and personal responsibility and resilience consistently, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to show flexibility, initiative and personal responsibility and resilience consistently.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on flexibility, initiative and responsibility, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.8 (typical level, generic skills, item 11). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b11 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.10.b11 (excellent), qaa/fheq-2024/4.15.b9.1 and Annex D's qaa/fheq-2024/annex-d/transferable/r4/2.1, a match we infer (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on flexibility, initiative and responsibility asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'Where have you taken the lead without being asked?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b12
  forPractitioner: { text: "Typical level: design for most students to be able to reflect critically on their own work, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to reflect critically on your own work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on reflecting on own work, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.8 (typical level, generic skills, item 12). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b12 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.10.b12 (excellent), qaa/fheq-2024/4.15.b9.3 and Annex D's qaa/fheq-2024/annex-d/transferable/r5/2.1, a match we infer (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on reflecting on own work asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'What weakness in your work did you find yourself, before anyone told you?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.8.b13
  forPractitioner: { text: "Typical level: design for most students to be able to use entrepreneurial skills of a high level, where they fit, with audiences, users, clients, consumers, markets and sources, beyond the threshold for the award.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To work at the typical level of your honours degree, you should be able to use entrepreneurial skills of a high level, where they fit, with audiences, users, clients, consumers, markets and sources.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a typical-level standard (should): what most honours graduates show on entrepreneurial skills, above the threshold, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.8 (typical level, generic skills, item 13). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.5.b13 (threshold), qaa/communication-media-film-and-cultural-studies-2024/4.10.b13 (excellent), qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r1/2.1, a match we infer (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student who meets the minimum on entrepreneurial skills asks how to do well, or when staff set marking criteria for the middle of the range. Present it as a step above the threshold, plainly to a student and as a design aim to staff. Ask: 'How did you shape a project for a real audience or client?' Avoid treating it as the minimum or reading the issuer's list aloud."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b1
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students show outstanding knowledge and understanding of the field's main debates and theoretical positions, including ones from beyond Western traditions; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to show outstanding knowledge and understanding of the field's main debates and theoretical positions, including ones from beyond Western traditions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on key debates and theories of the field, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 1). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b1 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r2/1st (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on key debates and theories of the field looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'Where would you take a debate in the field further than the readings do?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b2
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students analyse media texts critically, with the help of theory and concepts, to an outstanding degree; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to analyse media texts critically, with the help of theory and concepts, to an outstanding degree.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on analysing media texts with theory, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 2). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b2 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and Annex D's qaa/fheq-2024/annex-d/knowledge/r2/1st (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on analysing media texts with theory looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'What does your reading of the text show that others have missed?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b3
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students show an outstanding grasp of why texts and contexts in these fields matter for representation, for technology and for culture; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to show an outstanding grasp of why texts and contexts in these fields matter for representation, for technology and for culture.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on why texts and contexts matter, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 3). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b4 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r1/1st (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on why texts and contexts matter looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'How would you explain this text's significance to someone who has never studied media?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b4
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students assess critically, to an outstanding level, how media forms, community and participatory media among them, feed political and cultural debate and struggles over power; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to assess critically, to an outstanding level, how media forms, community and participatory media among them, feed political and cultural debate and struggles over power.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on media forms, debate and power, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 4). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b5 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's qaa/fheq-2024/annex-d/knowledge/r3/1st (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on media forms, debate and power looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'What would a full account of that medium's political effect need to include?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b5
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students evaluate critically the complex, overlapping ways in which varied communities and organisations help shape media and cultural policy and practice; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to evaluate critically the complex, overlapping ways in which varied communities and organisations help shape media and cultural policy and practice.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on communities shaping media and cultural policy, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 5). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b6 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r3/1st (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on communities shaping media and cultural policy looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'Whose influence on that policy would you judge greatest, and on what evidence?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b6
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students engage critically with global questions, sustainability among them, as they bear on communication and cultural forms; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to engage critically with global questions, sustainability among them, as they bear on communication and cultural forms.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on global issues and sustainability, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 6). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b7 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and Annex D's qaa/fheq-2024/annex-d/knowledge/r3/1st (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on global issues and sustainability looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'What new angle on a global issue could your own work open up?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b7
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students understand and consistently put to use the idea that communication technologies, practices and products are never neutral but take shape in their social, cultural, economic, historical, environmental and geographical settings; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to understand and consistently put to use the idea that communication technologies, practices and products are never neutral but take shape in their social, cultural, economic, historical, environmental and geographical settings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on technologies and products are not neutral, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 7). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b8 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and Annex D's qaa/fheq-2024/annex-d/knowledge/r2/1st (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on technologies and products are not neutral looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'Where in your recent work does that idea run through the whole argument?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b8
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students understand and assess critically, to an outstanding level, how social groups and organisations interact with one another and use various media to communicate; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to understand and assess critically, to an outstanding level, how social groups and organisations interact with one another and use various media to communicate.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on how social groups use media, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 8). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b9 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r1/1st (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on how social groups use media looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'What would you need to study to explain those differences fully?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b9
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students understand and evaluate critically the varied ways cultural value is lived and understood, including how versions of the world get made, kept going and passed on and how people form a sense of self and world through cultural texts and practices; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to understand and evaluate critically the varied ways cultural value is lived and understood, including how versions of the world get made, kept going and passed on and how people form a sense of self and world through cultural texts and practices.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on cultural value and how it is formed, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 9). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b10 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r2/1st (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on cultural value and how it is formed looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'What is your own account of how cultural value is made, and what would test it?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b10
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students choose, weigh critically and use competently research methods fitted to a given research context, the range widened to quantitative textual analysis and social research methods; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to choose, weigh critically and use competently research methods fitted to a given research context, the range widened to quantitative textual analysis and social research methods.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on choosing and using research methods, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 10). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b11 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and Annex D's qaa/fheq-2024/annex-d/practical/r1/1st (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on choosing and using research methods looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'How would you defend your choice of method to a sceptical examiner?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b11
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students find, retrieve, assess critically and bring together a range of data, sources and conceptual frameworks suited to research, production and professional practice in their own area; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to find, retrieve, assess critically and bring together a range of data, sources and conceptual frameworks suited to research, production and professional practice in your own area.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on finding and judging sources and frameworks, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 11). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b12 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and Annex D's qaa/fheq-2024/annex-d/cognitive/r1/1st (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on finding and judging sources and frameworks looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'What did bringing those sources together let you see that none showed alone?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b12
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students use the strengths, and judge the limits, of the quantitative or qualitative methods that fit, applying that knowledge independently in their own work with little or no supervision; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to use the strengths, and judge the limits, of the quantitative or qualitative methods that fit, applying that knowledge independently in your own work with little or no supervision.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on strengths and limits of quantitative and qualitative methods, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 12). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b13 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and Annex D's qaa/fheq-2024/annex-d/practical/r2/1st (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on strengths and limits of quantitative and qualitative methods looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'Which methodological choice did you make on your own, and what was it based on?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b13
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students design, research and present an extended project, written or practical, to an outstanding standard and with insight; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to design, research and present an extended project, written or practical, to an outstanding standard and with insight.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on an extended research or practical project, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 13). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b14 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r2/1st (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on an extended research or practical project looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'What would make your project stand out to an expert reader?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b14
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students show and apply theoretical understanding consistently and convincingly when engaging critically with cultural and production practice, as the programme's focus allows; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to show and apply theoretical understanding consistently and convincingly when engaging critically with cultural and production practice, as the programme's focus allows.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on theory in cultural and production practice, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 14). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b15 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r1/1st (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on theory in cultural and production practice looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'Where does your theory and your practice argue the same case throughout?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b15
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students show creative expression and flair of an outstanding standard in practice, as the programme's focus allows; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to show creative expression and flair of an outstanding standard in practice, as the programme's focus allows.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on creative expression through practice, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 15). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b16 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r3/1st (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on creative expression through practice looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'What in your work would an audience remember, and why?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b16
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students bring new knowledge and understanding together creatively and critically, and reflect critically on their own learning and performance; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to bring new knowledge and understanding together creatively and critically, and reflect critically on your own learning and performance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on reflecting on learning and performance, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 16). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b17 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3 and Annex D's qaa/fheq-2024/annex-d/transferable/r5/1st (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on reflecting on learning and performance looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'What would you now do differently in your learning, and why?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b17
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students understand and reflect critically on the different traditions and paths by which media, communication or film studies grew, and what they mean for the discipline and its cultural setting now; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to understand and reflect critically on the different traditions and paths by which media, communication or film studies grew, and what they mean for the discipline and its cultural setting now.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on how the subject developed, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 17). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b18 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's qaa/fheq-2024/annex-d/knowledge/r1/1st (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on how the subject developed looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'How would you place your own work among the subject's traditions?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b18
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students understand why the discipline needs to be inclusive, and show respect to diverse people inside and outside the subject; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to understand why the discipline needs to be inclusive, and show respect to diverse people inside and outside the subject.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on an inclusive discipline and respect for others, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 18). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b19 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r2/1st (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on an inclusive discipline and respect for others looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'Where could you help the subject become more inclusive?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b19
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students take an active part, to an outstanding degree, in varied discussion and debate in which others may challenge their own views; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to take an active part, to an outstanding degree, in varied discussion and debate in which others may challenge your own views.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on openness in discussion and debate, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 19). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b20 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r1/1st (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on openness in discussion and debate looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'When has your part in a debate changed its direction?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.9.b20
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students use communication, media, film and cultural forms and technologies ethically and with cultural responsibility, at work and in daily life, to an outstanding standard; this describes the top of the range, not the pass standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you should be able to use communication, media, film and cultural forms and technologies ethically and with cultural responsibility, at work and in daily life, to an outstanding standard.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (should): the top of the range for honours graduates on ethical, responsible use of media forms, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.9 (excellent level, subject knowledge and skills, item 20). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.7.b21 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r1/1st (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on ethical, responsible use of media forms looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'How would your work stand as an example of ethical practice to others?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.10.b1
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students consistently choose, weigh, judge, comment on and combine a wide range of research, primary sources, views and information to an outstanding degree, working references in smoothly; this describes the top of the range, not the pass standard.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you will be able to consistently choose, weigh, judge, comment on and combine a wide range of research, primary sources, views and information to an outstanding degree, working references in smoothly.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (will): the top of the range for honours graduates on selecting and referencing sources, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.10 (excellent level, generic skills, item 1). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b1 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and Annex D's qaa/fheq-2024/annex-d/cognitive/r1/1st (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on selecting and referencing sources looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'Where does your use of sources build a view nobody else has put together?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.10.b2
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students build, hold and criticise an argument to an outstanding degree, weighing other views; this describes the top of the range, not the pass standard.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you will be able to build, hold and criticise an argument to an outstanding degree, weighing other views.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (will): the top of the range for honours graduates on building and testing an argument, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.10 (excellent level, generic skills, item 2). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b2 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and Annex D's qaa/fheq-2024/annex-d/cognitive/r2/1st (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on building and testing an argument looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'Where does your argument answer its critics before they speak?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.10.b3
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students explain complex concepts, theories and debates with sophistication and critical insight; this describes the top of the range, not the pass standard.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you will be able to explain complex concepts, theories and debates with sophistication and critical insight.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (will): the top of the range for honours graduates on explaining complex ideas, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.10 (excellent level, generic skills, item 3). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b3 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r1/1st (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on explaining complex ideas looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'What does your explanation add that the textbook does not?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.10.b4
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students solve problems with outstanding creativity, using a range of methods; this describes the top of the range, not the pass standard.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you will be able to solve problems with outstanding creativity, using a range of methods.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (will): the top of the range for honours graduates on solving problems creatively, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.10 (excellent level, generic skills, item 4). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b4 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.2 and Annex D's qaa/fheq-2024/annex-d/cognitive/r3/1st (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on solving problems creatively looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'Which of your solutions surprised you or others?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.10.b5
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students show research findings through a range of methods for visualising and presenting data; this describes the top of the range, not the pass standard.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you will be able to show research findings through a range of methods for visualising and presenting data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (will): the top of the range for honours graduates on presenting research findings, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.10 (excellent level, generic skills, item 5). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b5 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/practical/r4/1st (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on presenting research findings looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'How would you present the same findings to two very different audiences?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.10.b6
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students analyse, judge critically, combine and interpret information and ideas to a consistently outstanding level, drawing on the field's literature; this describes the top of the range, not the pass standard.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you will be able to analyse, judge critically, combine and interpret information and ideas to a consistently outstanding level, drawing on the field's literature.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (will): the top of the range for honours graduates on analysing and interpreting information, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.10 (excellent level, generic skills, item 6). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b6 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's qaa/fheq-2024/annex-d/knowledge/r3/1st (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on analysing and interpreting information looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'Where does your interpretation go beyond the literature you used?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.10.b7
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students get information, ideas, problems and solutions across to an accomplished level in speech or other non-written forms, online and in writing, with clear expression and style, and with sensitivity and openness to other ideas and approaches; this describes the top of the range, not the pass standard.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you will be able to get information, ideas, problems and solutions across to an accomplished level in speech or other non-written forms, online and in writing, with clear expression and style, and with sensitivity and openness to other ideas and approaches.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (will): the top of the range for honours graduates on communicating in many forms, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.10 (excellent level, generic skills, item 7). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b7 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r1/1st (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on communicating in many forms looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'Which piece of your communication would you hold up as a model?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.10.b8
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students show outstanding numeracy and digital literacy; this describes the top of the range, not the pass standard.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you will be able to show outstanding numeracy and digital literacy.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (will): the top of the range for honours graduates on numeracy and digital literacy, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.10 (excellent level, generic skills, item 8). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b8 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's qaa/fheq-2024/annex-d/transferable/r1/1st (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on numeracy and digital literacy looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'Where have your numeric or digital skills shaped a project's outcome?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.10.b9
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students lead and take part in group discussion and make clear, authoritative and valuable contributions to shared projects, listening to others with outstanding care; this describes the top of the range, not the pass standard.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you will be able to lead and take part in group discussion and make clear, authoritative and valuable contributions to shared projects, listening to others with outstanding care.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (will): the top of the range for honours graduates on group work, listening and leadership, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.10 (excellent level, generic skills, item 9). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b9 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and Annex D's qaa/fheq-2024/annex-d/transferable/r2/1st (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on group work, listening and leadership looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'When have you led a group, and how did you make sure everyone was heard?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.10.b10
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students manage their own learning and work consistently and independently, meeting set briefs and deadlines; this describes the top of the range, not the pass standard.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you will be able to manage your own learning and work consistently and independently, meeting set briefs and deadlines.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (will): the top of the range for honours graduates on managing own learning to brief and deadline, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.10 (excellent level, generic skills, item 10). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b10 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and Annex D's qaa/fheq-2024/annex-d/transferable/r3/1st (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on managing own learning to brief and deadline looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'How have you kept independent work on track across a whole year?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.10.b11
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students show outstanding initiative and personal responsibility, and work autonomously; this describes the top of the range, not the pass standard.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you will be able to show outstanding initiative and personal responsibility, and work autonomously.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (will): the top of the range for honours graduates on flexibility, initiative and responsibility, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.10 (excellent level, generic skills, item 11). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b11 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and Annex D's qaa/fheq-2024/annex-d/transferable/r4/1st (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on flexibility, initiative and responsibility looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'What have you started and carried through entirely on your own?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.10.b12
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students reflect on their own work with outstanding ability; this describes the top of the range, not the pass standard.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you will be able to reflect on your own work with outstanding ability.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (will): the top of the range for honours graduates on reflecting on own work, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.10 (excellent level, generic skills, item 12). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b12 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3 and Annex D's qaa/fheq-2024/annex-d/transferable/r5/1st (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on reflecting on own work looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'How has your reflection changed what you do next?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.10.b13
  forPractitioner: { text: "Excellent level: set tasks that let the strongest students use entrepreneurial skills of an outstanding level, where they fit, with audiences, users, clients, consumers, markets and sources; this describes the top of the range, not the pass standard.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level in your honours degree, you will be able to use entrepreneurial skills of an outstanding level, where they fit, with audiences, users, clients, consumers, markets and sources.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an excellent-level standard (will): the top of the range for honours graduates on entrepreneurial skills, at FHEQ Level 6 (FQHEIS Level 10), not a requirement for the award. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.10 (excellent level, generic skills, item 13). Do not present it as the pass standard or as a master's outcome. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.8.b13 at the typical level, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's qaa/fheq-2024/annex-d/practical/r1/1st (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a strong student asks what outstanding work on entrepreneurial skills looks like, or when staff write criteria for the top marks. Present it as an aim, never a requirement: in plain words to a student and as a stretch goal to staff. Ask: 'What venture or project could you take to market from your work?' Avoid implying that a student fails without it."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.13
  forPractitioner: { text: "As a condition of the master's award, look for systematic subject knowledge, understanding and skills and outstanding command of the undergraduate generic skills, plus the four further expectations in 4.13.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a master's in the subject, you show systematic subject knowledge, understanding and skills, an outstanding command of the general skills set for undergraduates and the four further expectations listed with them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as the condition of the master's award (force threshold) at FHEQ Level 7 and FQHEIS Level 11. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.13. Do not read it as an honours rung: its general skills match the excellent level, qaa/communication-media-film-and-cultural-studies-2024/4.10.b1 to qaa/communication-media-film-and-cultural-studies-2024/4.10.b13. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.13.b1 to qaa/communication-media-film-and-cultural-studies-2024/4.13.b4, qaa/communication-media-film-and-cultural-studies-2024/1.7 and the FHEQ master's descriptor qaa/fheq-2024/4.17.b1 (spine:7)."
  author-agent-dialogue: "Raise it when a master's team sets its outcomes or a student asks what the master's award requires. Ask: 'Which of the excellent-level general skills do you already show, and which do you need to build?' Avoid presenting the excellent level as the honours minimum."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.13.b1
  forPractitioner: { text: "For the master's award, plan for and assess understanding and awareness that reach, or draw on, the leading edge of academic research or professional practice in the field.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a master's in the subject you show understanding and awareness that reach, or draw on, the leading edge of academic research or professional practice in the field.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as one of four further expectations attached to the master's award (force threshold, from the lead-in) at FHEQ Level 7 and FQHEIS Level 11. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.13. Do not apply it to honours graduates. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.13, qaa/communication-media-film-and-cultural-studies-2024/1.7 and the FHEQ master's descriptor qaa/fheq-2024/4.17.b1 (spine:7)."
  author-agent-dialogue: "Raise it when a master's student reviews progress or a team writes master's outcomes. Ask: 'Which recent research or practice in your area are you building on, and how current is it?' Put it to staff as an award condition and to a student in plain words; do not use it to judge undergraduate work."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.13.b2
  forPractitioner: { text: "For the master's award, plan for and assess originality in applying knowledge, with a practical grasp of how research pushes the discipline's knowledge forward.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a master's in the subject you show originality in applying knowledge, with a practical grasp of how research pushes the discipline's knowledge forward.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as one of four further expectations attached to the master's award (force threshold, from the lead-in) at FHEQ Level 7 and FQHEIS Level 11. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.13. Do not apply it to honours graduates. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.13, qaa/communication-media-film-and-cultural-studies-2024/1.7 and the FHEQ master's descriptor qaa/fheq-2024/4.17.b3 (spine:7)."
  author-agent-dialogue: "Raise it when a master's student reviews progress or a team writes master's outcomes. Ask: 'Where is your own work original, and how does research move the field on?' Put it to staff as an award condition and to a student in plain words; do not use it to judge undergraduate work."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.13.b3
  forPractitioner: { text: "For the master's award, plan for and assess understanding that allows critical evaluation of current research, research methods and advanced scholarship in the discipline.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a master's in the subject you show understanding that allows critical evaluation of current research, research methods and advanced scholarship in the discipline.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as one of four further expectations attached to the master's award (force threshold, from the lead-in) at FHEQ Level 7 and FQHEIS Level 11. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.13. Do not apply it to honours graduates. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.13, qaa/communication-media-film-and-cultural-studies-2024/1.7 and the FHEQ master's descriptor qaa/fheq-2024/4.17.b4.1 (spine:7)."
  author-agent-dialogue: "Raise it when a master's student reviews progress or a team writes master's outcomes. Ask: 'How would you judge a recent study's method in your area?' Put it to staff as an award condition and to a student in plain words; do not use it to judge undergraduate work."
- statement: qaa/communication-media-film-and-cultural-studies-2024/4.13.b4
  forPractitioner: { text: "For the master's award, plan for and assess growth in disciplinary knowledge and understanding, and new skills built to a high level.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a master's in the subject you show growth in disciplinary knowledge and understanding, and new skills built to a high level.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as one of four further expectations attached to the master's award (force threshold, from the lead-in) at FHEQ Level 7 and FQHEIS Level 11. Cite it as QAA (2024), Communication, Media, Film and Cultural Studies Subject Benchmark Statement, para 4.13. Do not apply it to honours graduates. Set it beside qaa/communication-media-film-and-cultural-studies-2024/4.13, qaa/communication-media-film-and-cultural-studies-2024/1.7 and the FHEQ master's descriptor qaa/fheq-2024/4.17.b7 (spine:7)."
  author-agent-dialogue: "Raise it when a master's student reviews progress or a team writes master's outcomes. Ask: 'Which new skill has your master's study taken to a high level?' Put it to staff as an award condition and to a student in plain words; do not use it to judge undergraduate work."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:4", role: "cites", locator: "D1, 1.6 (\"FHEQ Levels 4-6\")" }
  - { id: "fheq:5", role: "cites", locator: "D1, 1.6" }
  - { id: "fheq:6", role: "cites", locator: "D1, 1.6; 2.11" }
  - { id: "fheq:7", role: "cites", locator: "D1, 1.7; 4.2" }
  - { id: "fqheis:7", role: "cites", locator: "D1, 1.6 (\"FQHEIS Levels 7-10\")" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 1.6" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 1.6" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 1.6; 2.11" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 1.7; 4.2" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.11: \"FHEQ Level 6; FQHEIS Level 10\" for the honours degree); matches std:doc:qaa-fheq-2024-framework Table 1" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 1.7; 4.2: \"FHEQ Level 7 and FQHEIS Level 11\"); matches std:doc:qaa-fheq-2024-framework S5 (shared descriptor 4.17)" }
  - { from: "fheq:4 to fheq:6", to: "fqheis:7 to fqheis:10", relation: "corresponds", basis: "stated as a range for the bachelor's course (D1, 1.6); the FHEQ document pairs them per qualification, not level by level" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "3.7", "3.8", "3.9", "3.10", "3.11", "3.12", "3.16"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.19", "1.20", "1.21", "3.10"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "1.28", "1.29", "1.30", "3.17"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.31", "1.32", "1.33", "2.15", "3.13", "3.14", "3.15", "3.16", "3.17"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["3.21"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-communication-media-film-and-cultural-studies-2019-benchmarks (not ingested)", note: "section 6 names the fourth edition of 2019 and earlier editions of 2016, 2008 and 2002; the closing line names this the fifth edition" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the four honours classifications, for achievement above threshold (D1, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ Levels 4 to 7 (D1, 1.6, 1.7, 2.11, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS Levels 7 to 11 (D1, 1.6, 1.7, 2.11, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "\"Guidance on Education for Sustainable Development (ESD) published by QAA and Advance HE\" (D1, 1.23)" }
- { rel: "refersTo", target: "std:doc:qaa-enterprise-2018-guidance", note: "listed in section 5 only (twice); the enterprise theme paragraphs do not cite it" }
- { rel: "refersTo", target: "QAA guidance on generative AI (not ingested)", note: "D1, 3.21; section 5 lists QAA (2023) Reconsidering assessment for the ChatGPT era" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance (not ingested)", note: "front matter" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2024-04"
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
- The fields study cultural and communicative activity as a central force in economic, political, psychological and social life, and how people make, share and read meaning (D1, 1.1, 2.1).
- They draw on the arts, humanities and social sciences and on creative and professional practice in the cultural, film and communication industries, with links to design, business, marketing and computing (D1, 1.2, 1.8).
- A broad family of courses with varied emphases, from theory and history to production and professional practice, under many titles; the statement is a framework, not a prescription (D1, 1.3, 2.1 to 2.7).
- Eleven shared propositions bind the courses: culture and media shape lives, identities and power, are major employers, are unequally open to participation and call for informed debate on their politics, law and ethics (D1, 2.8).
- Courses combine understanding and skills in different measures, often with practice used to inform critique or critique to inform practice (D1, 2.9, 2.10).
- The fields have a long record of critiquing inherited hierarchies of power and representation, and the statement casts teaching staff as agents of change (D1, 1.14, 3.12).
- Courses commonly engage students in the three Cs of media literacy: cultural access, critical understanding and creative activity (D1, 2.2).
- The fields are agile, responding quickly to new technologies and practices, generative AI among them (D1, 1.4, 3.21).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "the fields' long critique of power and representation makes EDI part of the subject itself; the statement asks for EDI in every course and process, active recruitment, a diverse curriculum beyond tokenism, critical dialogue on gender, race, class, disability and colonialism, and an inclusive discipline as a student outcome at every rung (D1, 1.13 to 1.18, 3.7 to 3.12, 3.16)"
  statements: ["qaa/communication-media-film-and-cultural-studies-2024/1.16", "qaa/communication-media-film-and-cultural-studies-2024/1.17", "qaa/communication-media-film-and-cultural-studies-2024/1.18", "qaa/communication-media-film-and-cultural-studies-2024/3.7", "qaa/communication-media-film-and-cultural-studies-2024/3.8", "qaa/communication-media-film-and-cultural-studies-2024/3.9", "qaa/communication-media-film-and-cultural-studies-2024/3.10", "qaa/communication-media-film-and-cultural-studies-2024/1.10.b9", "qaa/communication-media-film-and-cultural-studies-2024/4.4.b18", "qaa/communication-media-film-and-cultural-studies-2024/4.7.b19", "qaa/communication-media-film-and-cultural-studies-2024/4.9.b18"]
- theme: theme:accessibility
  inThisSubject: "headed Accessibility: emotional, functional and technical access built into design, delivery and assessment; reasonable adjustments, attainment gaps, accessible resources and a pedagogy of care, repeated in the EDI section (D1, 1.19 to 1.21, 3.10)"
  statements: ["qaa/communication-media-film-and-cultural-studies-2024/1.19", "qaa/communication-media-film-and-cultural-studies-2024/1.20", "qaa/communication-media-film-and-cultural-studies-2024/1.21", "qaa/communication-media-film-and-cultural-studies-2024/3.10"]
- theme: theme:esd
  inThisSubject: "headed Sustainability: sustainability as a lens for course design, UNESCO's eight competencies, media representation of sustainability and the industry's own climate impact, ESD across the curriculum, the SDGs, BAFTA albert and sustainable studios and equipment; global issues and sustainable practice appear as student outcomes (D1, 1.22 to 1.30, 3.17)"
  statements: ["qaa/communication-media-film-and-cultural-studies-2024/1.23", "qaa/communication-media-film-and-cultural-studies-2024/1.27", "qaa/communication-media-film-and-cultural-studies-2024/1.28", "qaa/communication-media-film-and-cultural-studies-2024/1.29", "qaa/communication-media-film-and-cultural-studies-2024/3.17", "qaa/communication-media-film-and-cultural-studies-2024/1.10.b11", "qaa/communication-media-film-and-cultural-studies-2024/1.11.b8", "qaa/communication-media-film-and-cultural-studies-2024/4.4.b6", "qaa/communication-media-film-and-cultural-studies-2024/4.7.b7", "qaa/communication-media-film-and-cultural-studies-2024/4.9.b6"]
- theme: theme:enterprise
  inThisSubject: "headed Employability, enterprise and entrepreneurship education, and again Developing entrepreneurship and enterprise skills: careers in fast-changing creative industries, the economic weight of the sector, enterprise content such as intellectual property and production finance, enterprise for inclusion and sustainability, and entrepreneurial skills at every rung (D1, 1.31 to 1.33, 2.15, 3.13 to 3.17)"
  statements: ["qaa/communication-media-film-and-cultural-studies-2024/3.17", "qaa/communication-media-film-and-cultural-studies-2024/1.12.b8", "qaa/communication-media-film-and-cultural-studies-2024/1.12.b12", "qaa/communication-media-film-and-cultural-studies-2024/4.5.b13", "qaa/communication-media-film-and-cultural-studies-2024/4.8.b13", "qaa/communication-media-film-and-cultural-studies-2024/4.10.b13"]
- theme: theme:generative-ai
  inThisSubject: "one paragraph in the assessment section: students learn to use emerging technologies and AI effectively and ethically, and assessment responds while protecting academic integrity, with a pointer to QAA's generative AI guidance (D1, 3.21)"
  statements: ["qaa/communication-media-film-and-cultural-studies-2024/3.21"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "2.3", gloss: "practical, technological, business, environmental, industrial, audience and aesthetic emphases" }
  - { component: "2.4", gloss: "historical or contemporary emphasis" }
  - { component: "2.5", gloss: "fundamental modes of human communication, or specific media and systems" }
  - { component: "2.6", gloss: "professional practice and its management, including intellectual property; or critical and activist approaches" }
  - { component: "2.7", gloss: "artistic qualities of media, film and cultural forms" }
  - { component: "2.8", gloss: "eleven propositions that link all courses" }
  - { component: "3.15", gloss: "enterprise content: intellectual property, financial and legal literacy, production finance" }
practices:
  - { component: "2.16", kind: "learning", gloss: "work-based learning: live briefs, mentors, placements, sandwich year" }
  - { component: "3.2", kind: "learning", gloss: "a wide range of academic and non-academic materials" }
  - { component: "3.4", kind: "learning", gloss: "six learning processes: awareness, critical understanding, practice, creativity, literacies, reflection" }
  - { component: "3.5", kind: "teaching", gloss: "online, in-person, blended and flipped delivery; group and individual learning" }
  - { component: "3.6", kind: "learning", gloss: "active engagement with forms and practices; outside speakers and organisations" }
  - { component: "3.19", kind: "assessment", gloss: "students as participants: group critiques, co-produced assessment" }
  - { component: "3.20", kind: "assessment", gloss: "assessment matched to aims; varied to aid inclusion and deter essay mills" }
  - { component: "3.22", kind: "assessment", gloss: "sixteen kinds of assessment, from essays to festivals, pitches and authentic tasks" }
  - { component: "3.23", kind: "assessment", gloss: "constructive feedback by many means" }
  - { component: "3.24", kind: "assessment", gloss: "formative, summative and feedforward" }
  - { component: "3.25", kind: "assessment", gloss: "an extended final-year project, production, portfolio or work-based learning" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.3", lists: ["4.4", "4.5"], award: "bachelor's with honours", items: 33 }
  - { rung: "typical", leadIn: "4.6", lists: ["4.7", "4.8"], award: "bachelor's with honours", items: 34 }
  - { rung: "excellent", leadIn: "4.10", lists: ["4.9", "4.10"], award: "bachelor's with honours", items: 33 }
rungBases: "4.1: the statement sets out the minimum threshold and the typical and excellent standards a student will have shown at the award of the honours degree, and the master's standards; 4.2: most students do significantly better than the threshold, judged by each provider with Annex D; 4.3 and 4.6 are the threshold and typical lead-ins ('are able to demonstrate'); the excellent rung has no lead-in before its subject list (4.9), and its lead-in sentence opens the generic list (4.10). The six rung lists themselves open 'students should typically be able to', the excellent generic list excepted. Master's: 1.7 and 4.13, recorded outside the rungs (rung none)."
outcomeLists:
  - { leadIn: "1.9", gloss: "skills graduates show depending on the course (will)", items: 4, award: ["bachelor's with honours"] }
  - { leadIn: "1.10", gloss: "research, critical analysis, production and professional practice (will typically)", items: 12, award: ["bachelor's with honours"] }
  - { leadIn: "1.11", gloss: "citizenship (may)", items: 9, award: ["bachelor's with honours"] }
  - { leadIn: "1.12", gloss: "transferable skills (may)", items: 12, award: ["bachelor's with honours"] }
outcomes:
  - { outcome: "key debates and theories of the field", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b1", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b1", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b1", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "analysing media texts with theory", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b2", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b2", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b2", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "why texts and contexts matter (interrogate)", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b3", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b3", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b3", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "why texts and contexts matter (critique)", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b3", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b4", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b3", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "communities shaping media and cultural policy", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b4", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b6", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b5", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "media forms, debate and power", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b5", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b5", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b4", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "global issues and sustainability", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b6", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b7", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b6", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "technologies and products are not neutral", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b7", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b8", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b7", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "cultural value and how it is formed", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b8", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b10", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b9", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "how social groups use media", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b9", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b9", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b8", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "choosing and using research methods", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b10", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b11", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b10", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "finding and judging sources and frameworks", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b11", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b12", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b11", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "strengths and limits of quantitative and qualitative methods", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b12", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b13", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b12", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "an extended research or practical project", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b13", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b14", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b13", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "theory in cultural and production practice", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b14", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b15", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b14", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "creative expression through practice", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b15", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b16", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b15", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "reflecting on learning and performance", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b16", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b17", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b16", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "how the subject developed", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b17", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b18", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b17", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "an inclusive discipline and respect for others", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b18", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b19", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b18", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "openness in discussion and debate", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b19", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b20", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b19", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "ethical, responsible use of media forms", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.4.b20", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.7.b21", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.9.b20", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "selecting and referencing sources", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.5.b1", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.8.b1", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.10.b1", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "building and testing an argument", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.5.b2", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.8.b2", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.10.b2", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "explaining complex ideas", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.5.b3", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.8.b3", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.10.b3", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "solving problems creatively", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.5.b4", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.8.b4", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.10.b4", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "presenting research findings", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.5.b5", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.8.b5", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.10.b5", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "analysing and interpreting information", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.5.b6", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.8.b6", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.10.b6", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "communicating in many forms", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.5.b7", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.8.b7", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.10.b7", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "numeracy and digital literacy", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.5.b8", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.8.b8", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.10.b8", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "group work, listening and leadership", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.5.b9", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.8.b9", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.10.b9", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "managing own learning to brief and deadline", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.5.b10", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.8.b10", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.10.b10", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "flexibility, initiative and responsibility", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.5.b11", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.8.b11", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.10.b11", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "reflecting on own work", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.5.b12", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.8.b12", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.10.b12", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "entrepreneurial skills", threshold: "qaa/communication-media-film-and-cultural-studies-2024/4.5.b13", typical: "qaa/communication-media-film-and-cultural-studies-2024/4.8.b13", excellent: "qaa/communication-media-film-and-cultural-studies-2024/4.10.b13", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
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
- { body: "professional, statutory and regulatory bodies (PSRBs), unnamed", says: "the statement supports them on academic standards; their requirements are further reference points; courses may be developed with them and courses with professional outcomes may need their accreditation (D1, front matter, 2.15, 2.21)", requirements: "not-applicable-by-design: no body named (Part E)" }
- { body: "BAFTA albert Education Partnership", says: "an external framework that can bring recognition for sustainable production and screen skills (D1, 1.29)", requirements: "not yet ingested (Part E)" }
- { body: "The Alliance for Sustainability Leadership in Education (EAUC)", says: "its resources give general higher education frameworks and guidelines for sustainable facilities and practice (D1, 1.30)", requirements: "not yet ingested (Part E)" }
- { body: "UNESCO", says: "its resources on learning objectives for sustainable development set out eight core competencies (D1, 1.24)", requirements: "not yet ingested (Part E)" }
- { body: "Department for Culture, Media and Sport", says: "the source of the figures on jobs and growth in the creative industries (D1, 1.32)", requirements: "not-applicable: cited as a data source" }
- { body: "Office for Students", says: "England's regulator; under its framework the statement is not a sector-recognised standard (D1, front matter)", requirements: "not-applicable: a regulator, named for the statement's status" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion; Embedding equality, diversity and inclusion", carriedIn: ["1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "3.7", "3.8", "3.9", "3.10", "3.11", "3.12", "3.16"], statements: ["1.16", "1.17", "1.18", "3.7", "3.8", "3.9", "3.10", "1.10.b9", "4.4.b18", "4.7.b19", "4.9.b18"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["1.19", "1.20", "1.21", "3.10"], statements: ["1.19", "1.20", "1.21", "3.10"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "1.28", "1.29", "1.30", "3.17"], statements: ["1.23", "1.27", "1.28", "1.29", "3.17", "1.10.b11", "1.11.b8", "4.4.b6", "4.7.b7", "4.9.b6"] }
  - { id: "theme:enterprise", named: "Employability, enterprise and entrepreneurship education; Developing entrepreneurship and enterprise skills", carriedIn: ["1.31", "1.32", "1.33", "2.15", "3.13", "3.14", "3.15", "3.16", "3.17"], statements: ["3.17", "1.12.b8", "1.12.b12", "4.5.b13", "4.8.b13", "4.10.b13"] }
  - { id: "theme:generative-ai", named: "emerging technologies, machine learning and artificial intelligence; QAA guidance on generative AI", carriedIn: ["3.21"], statements: ["3.21"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["1.6", "1.7", "2.11", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:7", "fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["1.6", "1.7", "2.11", "4.2"] }
bodies:
  - { body: "PSRBs (unnamed)", citedIn: ["front matter", "2.15", "2.21"] }
  - { body: "BAFTA albert Education Partnership", citedIn: ["1.29"] }
  - { body: "The Alliance for Sustainability Leadership in Education (EAUC)", citedIn: ["1.30"] }
  - { body: "UNESCO", citedIn: ["1.24"] }
  - { body: "Department for Culture, Media and Sport", citedIn: ["1.32"] }
  - { body: "Advance HE (co-publisher of the ESD guidance)", citedIn: ["1.23"] }
  - { body: "Office for Students (regulator, England)", citedIn: ["front matter"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "descriptions of the four honours classifications (1st, 2.1, 2.2, 3rd), for achievement above threshold, and a reference for Level 7/11 awards" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Guidance on Education for Sustainable Development (ESD) published by QAA and Advance HE", citedIn: ["1.23"], role: "the context in which the statement should be read for sustainability" }
  - { document: "QAA guidance on generative AI (not yet ingested: Part E)", named: "QAA guidance on generative AI", citedIn: ["3.21"], role: "further guidance on AI and academic integrity" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (QAA, 2018)", citedIn: ["section 5"], role: "listed in the references only (Part E)" }
  - { document: "UN Sustainable Development Goals (external)", named: "United Nations' Sustainable Development Goals (SDGs)", citedIn: ["1.22", "1.28", "3.17"], role: "an external reference point for sustainability in the curriculum" }
  - { document: "UNESCO, Education for Sustainable Development Goals: learning objectives (external)", named: "resources for educators developing learning objectives around sustainable development", citedIn: ["1.24"], role: "the eight core sustainability competencies" }
  - { document: "European Charter for Media Literacy (external)", named: "the European Charter for Media Literacy", citedIn: ["2.2"], role: "source of the three Cs: cultural access, critical understanding, creative activity" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code for Higher Education", citedIn: ["front matter"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "Quality Assessment Framework for Wales; Quality Enhancement Framework (Scotland) (not ingested)", named: "the same", citedIn: ["front matter"], role: "where the statement is a key reference point" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "threshold-level", definition: "the minimum standard a student will have shown when awarded the honours degree (D1, 4.1, 4.3)", beneficiaryDefinition: "the least you must have shown by the end of your honours degree", scopeNote: "lists 4.4 and 4.5", category: "unknown", practices: ["education"] }
- { slug: "typical-level", definition: "systematic subject knowledge, understanding and skills with competent command of general skills, above the threshold (D1, 4.6)", beneficiaryDefinition: "what most students show, above the minimum", scopeNote: "lists 4.7 and 4.8", category: "unknown", practices: ["education"] }
- { slug: "excellent-level", definition: "systematic subject knowledge, understanding and skills with outstanding command of general skills (D1, 4.10)", beneficiaryDefinition: "the top of the range for your degree", scopeNote: "lists 4.9 and 4.10; also the general-skills base for the master's award (4.13)", category: "unknown", practices: ["education"] }
- { slug: "three-cs-media-literacy", definition: "cultural access, critical understanding and creative activity, from the European Charter for Media Literacy, as the basis many courses build on (D1, 2.2)", category: "unknown", practices: ["education"] }
- { slug: "pedagogy-of-care", definition: "teaching built on trust, inclusion, respect and support so that everyone feels included and able to take part (D1, 1.21, 3.10)", category: "unknown", practices: ["education"] }
- { slug: "feedforward", definition: "feedback aimed at how a student can improve future work, in the task and in wider skills and knowledge (D1, 3.24)", category: "unknown", practices: ["education"] }
- { slug: "authentic-assessment", definition: "assessment through real-world tasks such as client projects, policy documents, briefs or job simulations (D1, 3.22)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "threshold-level", form: "Threshold level", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "typical-level", form: "Typical level", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "excellent-level", form: "Excellent level", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "three-cs-media-literacy", form: "the 3c's", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "pedagogy-of-care", form: "pedagogy of care", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "feedforward", form: "feedforward", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "authentic-assessment", form: "authentic assessment", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Communication, Media, Film and Cultural Studies"
  edition: "April 2024 (fifth edition)"
  year: 2024
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/communication-media-film-and-cultural-studies-2024/communication-media-film-and-cultural-studies-2024.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: de1b3b0e48d4a85ac72b6e16d89f18d4d196b3570aff52d242f707c1358dbe67
  heldFiles: ["wkspc2601-library/txt/qaa-2024-communication-media-film-cultural-studies-subject-standard.txt", "wkspc2601-library/txt/qaa-2024-communication-media-film-cultural-studies-subject-standard.norm.txt", "wkspc2601-library/records/qaa-2024-communication-media-film-cultural-studies-subject-standard.chunks.json", "wkspc2601-library/records/qaa-2024-communication-media-film-cultural-studies-subject-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0044", title: "QAA guidance on generative AI (and QAA (2023) Reconsidering assessment for the ChatGPT era)", why: "cited in 3.21 for AI and academic integrity; not yet held" }
- { w: "W-std-0045", title: "Subject Benchmark Statement: Communication, Media, Film and Cultural Studies, fourth edition (2019)", why: "the superseded edition, for S7 and change tracking" }
```

## Part E Gaps and questions
- SB4, rung shape: three rungs, each split into subject knowledge, understanding and skills and generic skills (six lists): threshold 4.4 (20) and 4.5 (13); typical 4.7 (21) and 4.8 (13); excellent 4.9 (20) and 4.10 (13). The skeleton found only the excellent rung (13, from 4.10's lead-in); judged here.
- SB4, lead-ins: threshold and typical have lead-in paragraphs (4.3, 4.6: 'are able to demonstrate'); the excellent rung has none before its subject list 4.9, and its lead-in sentence opens the generic list 4.10. Every rung list but 4.10 opens 'students should typically be able to', even at threshold: a new wording.
- S4, force: threshold items take `threshold` from 4.1 ('the minimum threshold', forceFrom 4.1); typical and excellent items take the list's own 'should' (4.7, 4.8, 4.9), and 4.10's items 'will' ('are able to'). The 'typically' in the threshold lists' lead-in is not read as weakening the threshold; for Abbott at P3.
- S4, gradeOf: the lists run nearly parallel, so each typical item links to the threshold item and each excellent item to the typical item with the same content, all inferred (67 links; SB4 outcomes 34 rows). Typical 4.7.b3 and 4.7.b4 both match threshold 4.4.b3; 4.9.b3 links to 4.7.b4. The typical subject list orders some items differently (4.7.b5/b6, b9/b10 against 4.4.b4/b5, b8/b9) and the excellent list again (4.9.b4/b5, b8/b9); links follow content, not position.
- S4, identical wording across rungs (the issuer's, kept): 4.7.b7 = 4.9.b6 (global issues); 4.7.b11 = 4.9.b10 (research methods); 4.7.b12 = 4.9.b11 (sources); 4.7.b18 = 4.9.b17 (traditions of the subject); 4.4.b18 = 4.7.b19 = 4.9.b18 (inclusive discipline); 4.5.b5 = 4.8.b5 and 4.5.b8 = 4.8.b8 (generic). The excellent 4.10.b5 drops 'clearly' from the lower rungs' wording.
- S4, section 1 outcome lists recorded with rung none: 1.9 (will, 'some of', by course), 1.10 (will typically), 1.11 and 1.12 (may). Several items repeat rung items nearly word for word (1.10.b6 and 4.4.b11; 1.10.b7 and 4.4.b12; 1.11.b6 and 4.4.b4; 1.11.b9 and 4.4.b19; 1.12.b8 and 4.5.b13; 1.12.b11 and 4.4.b7); kept as separate records, linked in `aaw`.
- S4, master's: 1.7 ('require', recorded as must) and 4.13 with its four items, recorded with rung none, force threshold as a condition of award ('are awarded to students who demonstrate'), level fheq:7. 4.13's stem is cut as its own record (find) because it carries the base expectation (excellent-level general skills); the items are noun phrases, so most carry no verb.
- S4, skeleton corrections by `find`: 4.4.b8 runs across a page break (the skeleton stopped at 'maintained and'); paragraph records 1.7, 1.18, 1.21, 3.17 and 4.2 end before the sub-heading the extraction joined to them; 4.13 is the stem sentence only.
- S4, D-std-0002 (a) judgements, not taken as statements: 1.4 and 1.15 ('should be viewed': how to read the statement); 1.24's list (UNESCO's competencies, quoted, not standards); 1.25 and 3.1 to 3.6 (plain present); 2.10 ('require' describing many courses); 2.11 ('it is expected', 'would be expected': progression and postgraduate readiness, an obliging word outside the five, for Abbott); 2.19 and 2.20 (descriptive 'will' about review and examiners); 3.11 ('is crucial', 'a need for'); 3.15 (optional content, 'may'; its 'will allow' predictive); 3.25 ('are likely to require').
- S4, plain-present provider norms (template open point 5), listed not taken: 3.1 (teaching and assessment 'are designed'; students 'are made aware'), 3.4 ('strategies promote'), 3.6, 3.20 ('assessment strategies follow'), 3.23's last sentence ('Feedback is provided').
- S4, 1.17: 'must' sits inside a relative clause ('policies, practices and systems that must strive for fairness') after 'EDI is not optional'; recorded as must. 3.8 and 3.10 open with provider 'will'; 3.10 then repeats 1.21's sentences on resources, support and a pedagogy of care word for word.
- S4, 3.21 recorded as addressee both: 'Students should learn' (learner) and 'Assessment strategies should be responsive' (provider); domain generic-skill, level fheq:6, theme:generative-ai (Conventions from batch 1).
- S4, 3.18 cites 'paragraphs 1.8-1.12': a cross-reference (DPN-1), not cut.
- S4, domain: subject-list items split between knowledge, understanding and subject-skill by our reading; the issuer heads them only 'Subject knowledge, understanding and skills'. Reflection on learning (4.4.b16 and its rungs) is kept as subject-skill because the issuer places it in the subject list, though its generic twin is 4.5.b12.
- S4a and aaw: Annex D rows are paired with rungs as 3rd for threshold, 2.1 for typical and 1st for excellent; the statement makes no such match (4.2 points to Annex D only for performance above threshold): inferred, for P3. The FHEQ descriptor and Annex D row named for each item are our reading.
- S2, subjects: HECoS 100444, 100058 and 101233 and CAH24-01-05 and CAH15-01-06 follow the statement's own title words (stated). CAH24-01 (media, journalism and communications) is the parent group, inferred. Course titles in 1.3: broadcasting (100439 broadcast journalism), interactive media (100636) and games studies (101267 computer games) are nearest matches, inferred; political communication and lobbying, content creation, cultural management and subject histories have no HECoS code. 'publishing' appears twice in 1.3's list.
- SB6, frameworks: FHEQ and FQHEIS cited in 1.6, 1.7, 2.11 and 4.2; 1.6 cites ranges (FHEQ 4-6, FQHEIS 7-10), recorded as level by level in S5. CQFW not cited. Scottish four-year honours (2.13) names no framework.
- SB6, themes: TH tags in S4 the statements inside a theme's own paragraphs and the rung items whose content is the theme (sustainability 4.4.b6 rows; inclusive discipline 4.4.b18 rows; entrepreneurial skills 4.5.b13 rows). 1.9 to 1.12 sit between the context and the EDI sections, not inside a theme section.
- SB6, shared documents: the QAA Enterprise and Entrepreneurship Education guidance (2018) is listed twice in section 5 and not cited in the text; the British Academy (2024) report is in section 5 only. QAA guidance on generative AI is cited in 3.21 and listed in D3.
- SB5: no PSRB is named; BAFTA albert, the EAUC and UNESCO are named as sustainability resources, the DCMS as a data source and the Office for Students as England's regulator. Section 6 names subject associations (MeCCSA, the Association for Journalism Education, BAFSS, BJTC, BKSTS) only as affiliations of 2016 advisory group members; not recorded as bodies.
- S7, supersedes: the 2019 fourth edition, from section 6; the 2016, 2008 and 2002 editions appear only as advisory group lists.
- Patterns differing from Psychology: six rung lists (subject and generic at each rung) with a lead-in 'should typically be able to' even at threshold; no excellent lead-in paragraph before its subject list; section 1 outcome lists in 'will', 'will typically' and 'may'; master's expectations added to the excellent-level general skills (4.13); a generative AI paragraph inside assessment; provider obligations in must (1.17) and require (1.7).
- S9: not researched in P1.
- S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are still to check.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:52: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0094 (P1); built by tools/bm_build.py.
