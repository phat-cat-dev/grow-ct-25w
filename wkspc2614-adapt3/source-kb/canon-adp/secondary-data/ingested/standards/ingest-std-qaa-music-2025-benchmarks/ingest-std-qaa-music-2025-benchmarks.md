---
id: std:doc:qaa-music-2025-benchmarks
title: "Subject Benchmark Statement Music"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100070", label: "music", basis: "stated" }
  - { scheme: "cah", code: "CAH25-02-02", label: "music", basis: "stated" }
  - { scheme: "hecos", code: "100223", label: "music production", basis: "stated" }
  - { scheme: "hecos", code: "101241", label: "music therapy", basis: "stated" }
  - { scheme: "hecos", code: "100035", label: "musical theatre", basis: "stated" }
  - { scheme: "hecos", code: "100674", label: "ethnomusicology and world music", basis: "stated" }
  - { scheme: "hecos", code: "100667", label: "musicology", basis: "stated" }
  - { scheme: "hecos", code: "100695", label: "music composition", basis: "stated" }
  - { scheme: "hecos", code: "100841", label: "popular music", basis: "stated" }
  - { scheme: "hecos", code: "100221", label: "music technology", basis: "stated" }
  - { scheme: "hecos", code: "100427", label: "acoustics", basis: "stated" }
  - { scheme: "hecos", code: "100637", label: "musicianship and performance studies", basis: "inferred" }
  - { scheme: "hecos", code: "100643", label: "music and arts management", basis: "inferred" }
edition: "April 2025 (fifth edition)"
published: 2025-04
status: current
supersedes: "the 2019 minor update (and the 2016, 2008 and 2002 editions), named in the membership section (section 6)"
heldText: { method: sha256-bytes, raw: 0411d7548d143e9a8973b70047b56db3f0d07cb097b820d589c1655cf95494f8, normalised: 71c6014b2e3220bc2dd867a250ed439d728034cbf7ea7c66ab701adfef61b3f7 }
heldTextStan: { method: sha256-stan, raw: 0411d7548d143e9a8973b70047b56db3f0d07cb097b820d589c1655cf95494f8, normalised: 0992211d8cb046d603ac64b54e598d14620f4e8549eaaa397f2e9d4ee73de03b }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, the 2022 onward revision with cross-cutting themes (fifth edition of this statement)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0121 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:00"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Music (QAA, April 2025)

> Run 0121, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2025-music-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in music should know, understand and be able to do, set out for the honours degree as a two-column table (a minimum threshold and a typical level) under three headings, knowledge and understanding, technical skills and professional skills, with a short list added for master's study. Reach for it when designing, approving, reviewing or describing a music course, its outcomes or its marking. It is not a curriculum and not a regulatory requirement; in England it is not a sector-recognised standard.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2025 as the fifth edition, the statement covers undergraduate and taught postgraduate degrees in music, including cognate and specialised degrees such as music production, music therapy, musical theatre, ethnomusicology and performance. It sets out the subject's context and purposes, five cross-cutting themes (equity, diversity and inclusion; accessibility; education for sustainable development; employability, enterprise and entrepreneurship education; generative AI), the distinctive features of a music degree (design, progression, flexibility, partnership, monitoring and review), its content, teaching, learning and assessment, and benchmark standards for the honours degree at two rungs, threshold (22 items) and typical (22 items), paired row by row, with excellence described only in prose, plus five master's outcomes at FHEQ level 7. It points to Annex D for the degree classes and names three accrediting bodies (JAMES, CDMT, HCPC) and the Equality and Human Rights Commission.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Music"
edition: "April 2025 (fifth edition)"
dates:
  published: 2025-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; part of the current quality arrangements in Scotland, Wales and Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2025", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate in music is expected to know, understand and be able to do at honours, at threshold and typical levels, and the added outcomes for master's study"
appliesTo:
  awards: ["bachelor's with honours", "master's (taught postgraduate and integrated master's)"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This Subject Benchmark Statement is relevant to all kinds of undergraduate and taught postgraduate degrees in Music, including broad-ranging Music degrees, cognate degrees such as Sound Studies and Music Production, degrees that intersect closely with other fields, such as Music Therapy and Musical Theatre, and specialised degrees within Music such as Ethnomusicology and Music Performance.\" (D1, 1.10)"
statedSubjects:
  - { name: "Music", locator: "(D1, title; 1.1; 1.10)", kind: "subject", codes: [{ scheme: "hecos", code: "100070", label: "music" }, { scheme: "cah", code: "CAH25-02-02", label: "music" }] }
  - { name: "Sound Studies", locator: "(D1, 1.10; 1.24)", kind: "programme title", codes: [] }
  - { name: "Music Production", locator: "(D1, 1.10; 2.5; 2.14)", kind: "programme title", codes: [{ scheme: "hecos", code: "100223", label: "music production" }] }
  - { name: "Music Therapy", locator: "(D1, 1.10; 2.5; 2.14; 3.4)", kind: "programme title", codes: [{ scheme: "hecos", code: "101241", label: "music therapy" }] }
  - { name: "Musical Theatre", locator: "(D1, 1.10; 2.14)", kind: "programme title", codes: [{ scheme: "hecos", code: "100035", label: "musical theatre" }] }
  - { name: "Ethnomusicology", locator: "(D1, 1.10; 2.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100674", label: "ethnomusicology and world music" }] }
  - { name: "Music Performance", locator: "(D1, 1.10; 2.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100637", label: "musicianship and performance studies" }] }
  - { name: "Musicology", locator: "(D1, 1.16; 2.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100667", label: "musicology" }] }
  - { name: "Composition", locator: "(D1, 2.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100695", label: "music composition" }] }
  - { name: "Popular Music studies", locator: "(D1, 2.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100841", label: "popular music" }] }
  - { name: "Music Technology", locator: "(D1, 1.24)", kind: "specialism", codes: [{ scheme: "hecos", code: "100221", label: "music technology" }] }
  - { name: "Acoustics", locator: "(D1, 1.24)", kind: "specialism", codes: [{ scheme: "hecos", code: "100427", label: "acoustics" }] }
  - { name: "Music Business", locator: "(D1, 2.4; 3.4)", kind: "programme title", codes: [{ scheme: "hecos", code: "100643", label: "music and arts management" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Music degree", gloss: "the field's breadth and the value of its graduates to society" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Music degree", gloss: "degrees vary widely; the key elements are listed in 2.2" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Music degree", gloss: "the subject keeps changing with the needs of its users" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Music degree", gloss: "the range of traditions reflects a diverse society" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Music degree", gloss: "branches studied alone, combined or beside other disciplines" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Music degree", gloss: "distinctive elements of the subject and the resources they need" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Music degree", gloss: "a range of providers, conservatoires among them" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Music degree", gloss: "learners arrive by academic, vocational and self-taught routes" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Music degree", gloss: "where graduates work; self-employment and portfolio careers" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Music degree", gloss: "the degrees the statement covers" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Music degree", gloss: "examples are illustrative, not complete" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "inclusive curricula and the critique of privilege" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "problems in inherited scholarship; inclusive perspectives" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "gatekeeping in admission and unequal access to resources" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "choice, self-direction and identity in creative work" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "global musics, collaboration and overlooked material" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "decolonising history and redressing unequal representation" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "the Equality Act duty and disabilities that bear on music study" }
  - { number: "1.19", order: 21, componentType: stem, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "specialist support and examples of reasonable adjustments" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessible, flexible design of teaching and assessment" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "access to music-specific activities, with alternatives" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessible synchronous and online provision" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainability as part of understanding music's value" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "the role of ESD; an interdisciplinary lens; the SDGs" }
  - { number: "1.25", order: 27, componentType: stem, parent: "section 1", heading: "Education for sustainable development", gloss: "teaching for sustainability, with SDG-linked examples" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "the environmental impact of music-making and responses to it" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "what enterprise education supports; links with employers" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "entrepreneurship beyond paid employment" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "roles across the music ecosystem; portfolio careers" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "resilience and adaptability; careers started before study" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "professional readiness at graduation" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "enterprise built into curriculum and assessment" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "teaching and assessing enterprise directly" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "industry involvement in enterprise education" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "learning from staff who are practitioners" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "transferable qualities; support for freelance and business careers" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "what generative AI offers music" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "staff understanding; critical and ethical student use of AI" }
  - { number: "1.39", order: 41, componentType: stem, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "adapting teaching to use generative AI" }
  - { number: "1.40", order: 42, componentType: stem, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "adapting assessment to use generative AI" }
  - { number: "1.41", order: 43, componentType: stem, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "ethical, legal and environmental guidance on generative AI" }
  - { number: "2.1", order: 45, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "the variety of programme designs" }
  - { number: "2.2", order: 46, componentType: area, parent: "section 2", heading: "Design", gloss: "connected activities that shape every programme" }
  - { number: "2.3", order: 47, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "interdisciplinary, global and multicultural by nature" }
  - { number: "2.4", order: 48, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "single honours or part of another degree" }
  - { number: "2.5", order: 49, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "the variety of taught postgraduate provision" }
  - { number: "2.6", order: 50, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression across levels towards the threshold" }
  - { number: "2.7", order: 51, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "readiness for postgraduate study" }
  - { number: "2.8", order: 52, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined degrees" }
  - { number: "2.9", order: 53, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards below honours" }
  - { number: "2.10", order: 54, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "course length across the UK nations" }
  - { number: "2.11", order: 55, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes of delivery and ways of gaining credit" }
  - { number: "2.12", order: 56, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership delivery and the statement's part in it" }
  - { number: "2.13", order: 57, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnerships that build employability" }
  - { number: "2.14", order: 58, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "accreditation by professional bodies" }
  - { number: "2.15", order: 59, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnerships with schools and colleges; the national plans" }
  - { number: "2.16", order: 60, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic course review" }
  - { number: "2.17", order: 61, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.18", order: 62, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "the external examining system" }
  - { number: "2.19", order: 63, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners, live and recorded assessment, annual reports" }
  - { number: "2.20", order: 64, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation of professional and vocational courses" }
  - { number: "3.1", order: 66, componentType: paragraph, parent: "section 3", heading: "Content, structure and delivery", gloss: "how content shapes teaching and assessment" }
  - { number: "3.2", order: 67, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "key content points back to 2.2" }
  - { number: "3.3", order: 68, componentType: area, parent: "section 3", heading: "Content", gloss: "diversity of design, focus and approach" }
  - { number: "3.4", order: 69, componentType: area, parent: "section 3", heading: "Content", gloss: "interdisciplinary and music-adjacent study" }
  - { number: "3.5", order: 70, componentType: area, parent: "section 3", heading: "Content", gloss: "skills and attributes common to graduates" }
  - { number: "3.6", order: 71, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "a range of teaching styles; inclusive and practical" }
  - { number: "3.7", order: 72, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "lectures and seminars" }
  - { number: "3.8", order: 73, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "learning environments, equipment and collections" }
  - { number: "3.9", order: 74, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "individual tuition in performance or composition" }
  - { number: "3.10", order: 75, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "ensemble tuition" }
  - { number: "3.11", order: 76, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "teaching across levels with differentiated criteria" }
  - { number: "3.12", order: 77, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "formal and extracurricular performing activity" }
  - { number: "3.13", order: 78, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "industry-related teaching and placements" }
  - { number: "3.14", order: 79, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "links with support services" }
  - { number: "3.15", order: 80, componentType: paragraph, parent: "section 3", heading: "Assessment and feedback", gloss: "the purpose of assessment and feedback" }
  - { number: "3.16", order: 81, componentType: paragraph, parent: "section 3", heading: "Assessment and feedback", gloss: "assessment across practice and theory; process and product" }
  - { number: "3.17", order: 82, componentType: paragraph, parent: "section 3", heading: "Assessment and feedback", gloss: "authentic assessment" }
  - { number: "3.18", order: 83, componentType: paragraph, parent: "section 3", heading: "Assessment and feedback", gloss: "choice of assessment and submission methods" }
  - { number: "3.19", order: 84, componentType: practice, parent: "section 3", heading: "Assessment methods", gloss: "indicative assessment methods" }
  - { number: "3.20", order: 85, componentType: practice, parent: "section 3", heading: "Assessment methods", gloss: "projects and portfolios" }
  - { number: "3.21", order: 86, componentType: practice, parent: "section 3", heading: "Feedback", gloss: "clarity about assessment and marking" }
  - { number: "3.22", order: 87, componentType: paragraph, parent: "section 3", heading: "Feedback", gloss: "formats of feedback" }
  - { number: "3.23", order: 88, componentType: practice, parent: "section 3", heading: "Feedback", gloss: "continuous feedback and feed forward" }
  - { number: "3.24", order: 89, componentType: paragraph, parent: "section 3", heading: "Feedback", gloss: "discussing and using feedback" }
  - { number: "3.25", order: 90, componentType: practice, parent: "section 3", heading: "Feedback", gloss: "peer feedback networks" }
  - { number: "4.1", order: 92, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the two rungs set: minimum threshold and typical" }
  - { number: "4.2", order: 93, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most students exceed the threshold; Annex D" }
  - { number: "4.3", order: 94, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "not competence standards; Equality Act guidance" }
  - { number: "4.4", order: 95, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "how excellence may be shown" }
  - { number: "4.5", order: 96, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "no common curriculum implied" }
  - { number: "4.6", order: 97, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the standards are shown together" }
  - { number: "4.7", order: 98, componentType: stem, parent: "section 4", heading: "Knowledge and understanding", gloss: "knowledge and understanding: threshold and typical columns" }
  - { number: "4.8", order: 99, componentType: stem, parent: "section 4", heading: "Technical skills", gloss: "technical skills: threshold and typical columns" }
  - { number: "4.9", order: 100, componentType: stem, parent: "section 4", heading: "Professional skills", gloss: "professional skills: threshold and typical columns" }
  - { number: "4.10", order: 101, componentType: stem, parent: "section 4", heading: "Master's level", gloss: "outcomes added for master's study" }
  - { number: "4.11", order: 102, componentType: paragraph, parent: "section 4", heading: "Master's level", gloss: "master's as a route to doctoral work" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Music degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Music degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "none", heading: "section headings (1 to 4)", kind: "other: heading lines" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for S7 and SB6" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: membership, read for S7 (earlier editions 2019, 2016, 2008, 2002)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 61 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/music-2025/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of a Music degree", "Accessibility and the needs of disabled students"] }
  span: { start: 15881, end: 16906 }
  source: "1.18 All Music courses have a responsibility to consider the needs of students with disabilities under the Equality Act (2010) and take proactive steps to ensure disabled students do not experience direct or indirect discrimination, harassment or victimisation. Disabilities particularly pertinent to the study of Music might include physical impairments (including repetitive strain injuries), sensory conditions (particularly visual and hearing impairments and D/deafness), mental health conditions (including debilitating performance anxiety), neurodiversity (including dyslexia and autism), long-term medical conditions (including myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS) and epilepsy), and specific learning difficulties. Access to degrees for all students is proactively and flexibly considered, including processes of recruitment and selection. Music course teams also ensure that all students are able to access performance spaces and facilities, teaching rooms, studios and audiovisual equipment.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "a responsibility to" read as must
  level: none
  appliesTo: "music courses and course teams"
  addressee: provider
  verbs: ["consider", "take", "ensure"]
  about: "the Equality Act duty towards disabled students"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Every music course carries a responsibility under the Equality Act 2010 to weigh the needs of disabled students and act ahead of time so they meet no discrimination, harassment or victimisation; the paragraph lists conditions that bear on music study and says teams make spaces and equipment reachable for all."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/music-2025/1.31
  locator: { number: "1.31", headingPath: ["Context and purposes of a Music degree", "Employability, enterprise and entrepreneurship education"] }
  span: { start: 25113, end: 25534 }
  source: "1.31 Music programmes support students on their professional journeys, while preparing them for challenges and opportunities. Transferable skills are relevant here, as well as education for professional life. At the point of graduating, students will have started building their professional networks, begun developing their own personal brand, solved complex problems in challenging situations, and built up resilience.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students at the point of graduating"
  addressee: learner
  verbs: ["support", "started", "begun", "solved", "built"]
  about: "professional readiness at graduation"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses back students on their way into professional life; by graduation students will have begun professional networks and a personal brand, met hard problems in testing settings and grown resilient."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of a Music degree", "Progression"] }
  span: { start: 35219, end: 36038 }
  source: "2.6 Over the course of a standard undergraduate degree with honours (FHEQ Level 6; FQHEIS Level 10) or, if available, an integrated master’s degree (FHEQ Level 7; FQHEIS Level 11), a Music student will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level sees the attainment of knowledge, expertise and experience that builds towards the final achievement of meeting at least the threshold-level of subject-specific and generic skills listed in this Statement. The knowledge, expertise and experience acquired throughout a Music degree are often cumulative. Examples include performance/compositional output of increasing duration and technical complexity, or critical/historical/contextual engagement at a deeper level.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on honours and integrated master's courses in music"
  addressee: learner
  verbs: ["progress", "expected", "builds"]
  about: "progression across levels towards the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "On an honours degree (FHEQ 6; FQHEIS 10) or integrated master's (FHEQ 7; FQHEIS 11) a student will move up level by level under the institution's rules, each level adding knowledge, expertise and experience towards at least the threshold in subject and generic skills; much of this builds cumulatively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of a Music degree", "Progression"] }
  span: { start: 36038, end: 36490 }
  source: "2.7 Upon graduation from an undergraduate degree in Music, it is expected that a student who has achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in Music or a related discipline. Entry requirements to postgraduate programmes are, however, determined by individual providers and may require the acquisition of specified skills and/or specified levels of achievement at undergraduate level.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "requirements" read as must
  level: fheq:6
  appliesTo: "honours graduates with a second-class degree or higher"
  addressee: learner
  verbs: ["expected", "achieved", "determined"]
  about: "readiness for postgraduate study"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A music graduate with at least a second-class degree is expected to be able and ready to take on postgraduate study in music or a related field, though each provider sets its own entry requirements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of a Music degree", "Progression"] }
  span: { start: 36490, end: 36947 }
  source: "2.8 Undergraduates studying Music as part of a combined or joint degree with other subjects (including courses that specify major and minor options) will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the areas covered in the other subject(s) of their degree. Additionally, overlaps between different disciplines may enable students to explore opportunities for interdisciplinary study.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduates studying music in a joint or combined degree"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "joint and combined degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students taking music within a joint or combined degree, including major and minor routes, will reach the core of the subject and generic skills set out here and gain others from their other subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/2.16
  locator: { number: "2.16", headingPath: ["Distinctive features of a Music degree", "Monitoring and review"] }
  span: { start: 40995, end: 41644 }
  source: "2.16 Degree-awarding bodies, and their collaborative partnerships, routinely collect and analyse information and undertake periodic course review according to their own needs. Considering the student voice will form part of this. They draw on a range of external reference points, including this Statement, to ensure that their provision aligns with sector norms. Monitoring and evaluation facilitate periodic assessment of a course, conducted internally or by external independent evaluators. Evaluation uses information from both current and historic monitoring to develop an understanding of student achievement or inform future course planning.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "degree-awarding bodies and their partners"
  addressee: provider
  verbs: ["collect", "analyse", "undertake", "form", "draw"]
  about: "monitoring, review and the student voice"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Degree-awarding bodies and their partners gather and study information and review courses on their own cycle; the student voice will be part of this, and they use external reference points, this statement among them, to check alignment with sector norms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/music-2025/2.17
  locator: { number: "2.17", headingPath: ["Distinctive features of a Music degree", "Monitoring and review"] }
  span: { start: 41644, end: 42017 }
  source: "2.17 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers from other higher education institutions, professional bodies or employers as part of periodic review to gain an independent perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "providers conducting periodic review"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "External scrutiny is a core part of UK quality assurance; providers will bring in reviewers from other institutions, professional bodies or employers during periodic review to gain an outside view and confirm that threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/music-2025/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of a Music degree", "Monitoring and review"] }
  span: { start: 42844, end: 42990 }
  source: "External examiners are required to produce a report each year and make recommendations for changes to modules and assessments (where appropriate)."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "external examiners"
  addressee: provider
  verbs: ["required", "produce", "make"]
  about: "external examiners' annual report"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "External examiners must write a report every year and suggest changes to modules and assessments where they see a need."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/music-2025/3.21
  locator: { number: "3.21", headingPath: ["Content, structure and delivery", "Feedback"] }
  span: { start: 57730, end: 58197 }
  source: "3.21 As assessments are central to a student’s learning experience and professional skills, it is essential within assessment and feedback practices that students are provided with clarity on the assessment process, and how their mark will be calculated. Clearly articulated assessment criteria aligned to learning outcomes and curriculum enable students to contextualise their mark and understand how they can improve their future submissions and professional work.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "it is essential" read as must
  level: none
  appliesTo: "assessment and feedback practice in music courses"
  addressee: provider
  verbs: ["provided", "enable"]
  about: "clarity about assessment and marking"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Because assessment is central to learning and professional skill, students are to be told clearly how assessment works and how marks are reached; criteria tied to outcomes and curriculum let them read their mark and see how to improve."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/3.24
  locator: { number: "3.24", headingPath: ["Content, structure and delivery", "Feedback"] }
  span: { start: 59218, end: 59573 }
  source: "3.24 Creative and performance assessments in Music can include personal expression, dependent on artistic practices. Therefore, typically, students will have opportunities to\n\n19\ndiscuss and seek clarification on feedback received and be given the tools to interpret and use it, equipping them with the skills required to work in the creative industries.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students receiving feedback on creative and performance work"
  addressee: both
  verbs: ["include", "have", "discuss", "seek", "interpret", "use"]
  about: "discussing and using feedback"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Since creative and performance assessment can turn on personal artistic expression, students will typically be able to talk through and query their feedback and be given ways to read and act on it, a skill the creative industries need."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60264, end: 60749 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers awarding honours degrees in music"
  addressee: provider
  verbs: ["perform", "refer"]
  about: "going beyond the threshold; Annex D"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do well above the minimum threshold; each provider decides what evidence shows such achievement and should consult Annex D of the national qualifications Frameworks, which describes the four main honours classes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/music-2025/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60749, end: 61242 }
  source: "4.3 Please note that the minimum threshold and typical standards are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards (as defined by the Equality Act 2010) as part of a programme specification, these can be informed by the relevant Subject Benchmark Statement along with any PSRB requirements. In these circumstances, providers should follow the most recent guidance from the Equality and Human Rights Commission .\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers developing competence standards"
  addressee: provider
  verbs: ["note", "intended", "develop", "informed", "follow"]
  about: "competence standards and the Equality Act"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The threshold and typical standards are not universal competence standards; a provider that sets competence standards under the Equality Act 2010 in a programme specification may draw on the statement and any PSRB requirements and should follow the latest guidance from the Equality and Human Rights Commission."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/music-2025/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Knowledge and understanding"] }
  span: { start: 62043, end: 62231 }
  source: "demonstrate knowledge and understanding of a body of music and of musical materials, artefacts, texts, discourses, resources and concepts associated with it appropriate to their discipline"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "a body of music and its materials"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least know and understand a body of music, together with the materials, texts, discourses and concepts that go with it in their discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.7.b1.typical
  locator: { number: "4.7.b1.typical", headingPath: ["Benchmark standards", "Knowledge and understanding"] }
  span: { start: 62232, end: 62377 }
  source: "in addition, show the ability to explore, evaluate, apply or challenge associated scholarship and research relating to musical materials in depth"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["show", "explore", "evaluate", "apply", "challenge"]
  about: "engaging in depth with scholarship on musical materials"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.7.b1, basis: stated }
  paraphrase: "Will typically also be able to explore, assess, use or contest the scholarship and research on musical materials in depth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Knowledge and understanding"] }
  span: { start: 62378, end: 62561 }
  source: "demonstrate knowledge and understanding of musical contexts, including the relationship of Music to historical, philosophical, cultural, educational and social practices and phenomena"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "musical contexts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least show knowledge and understanding of the contexts of music, including how it relates to historical, philosophical, cultural, educational and social practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.7.b2.typical
  locator: { number: "4.7.b2.typical", headingPath: ["Benchmark standards", "Knowledge and understanding"] }
  span: { start: 62562, end: 62672 }
  source: "in addition, demonstrate awareness of the critical debates arising from the placing of Music in wider contexts"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "critical debates about music in its contexts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.7.b2, basis: stated }
  paraphrase: "Will typically also be aware of the critical debates that arise when music is set in wider contexts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Knowledge and understanding"] }
  span: { start: 62707, end: 62870 }
  source: "demonstrate knowledge and understanding of how Music interconnects with other disciplines in the arts, humanities, and social and physical sciences, as appropriate"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "music and other disciplines"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least show knowledge and understanding of how music connects with other fields in the arts, humanities and the social and physical sciences, where relevant."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.7.b3.typical
  locator: { number: "4.7.b3.typical", headingPath: ["Benchmark standards", "Knowledge and understanding"] }
  span: { start: 62871, end: 63001 }
  source: "in addition, show an awareness of the implications of an interdisciplinary approach to Music for creation, innovation and research"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["show"]
  about: "what interdisciplinary work means for creation and research"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.7.b3, basis: stated }
  paraphrase: "Will typically also be aware of what an interdisciplinary approach to music implies for making, innovating and researching."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Knowledge and understanding"] }
  span: { start: 63002, end: 63137 }
  source: "analyse and interrogate musical materials and artefacts appropriate to their discipline and communicate the findings in a coherent form"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["analyse", "interrogate", "communicate"]
  about: "analysing musical materials and reporting findings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least be able to analyse and question musical materials and artefacts in their discipline and report what they find coherently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.7.b4.typical
  locator: { number: "4.7.b4.typical", headingPath: ["Benchmark standards", "Knowledge and understanding"] }
  span: { start: 63138, end: 63263 }
  source: "in addition, show critical awareness of issues of debate or uncertainty raised from analysing musical materials and artefacts"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["show", "raised", "analysing"]
  about: "debate and uncertainty raised by analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.7.b4, basis: stated }
  paraphrase: "Will typically also be critically aware of the questions of debate or uncertainty that analysing musical materials raises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Knowledge and understanding"] }
  span: { start: 63264, end: 63414 }
  source: "demonstrate an understanding of relationships between artistic practice and theoretical aspects of Music, as applicable to the particular area studied"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "practice and theory in music"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least show an understanding of how artistic practice relates to the theory of music, as it applies to their area."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.7.b5.typical
  locator: { number: "4.7.b5.typical", headingPath: ["Benchmark standards", "Knowledge and understanding"] }
  span: { start: 63415, end: 63519 }
  source: "in addition, critique the nature, relevance, purpose and consequences of theoretical constructs in Music"
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["critique"]
  about: "critiquing theoretical constructs"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.7.b5, basis: stated }
  paraphrase: "Will typically also critique the nature, relevance, purpose and effects of theoretical constructs in music."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.7.b6
  locator: { number: "4.7.b6", headingPath: ["Benchmark standards", "Knowledge and understanding"] }
  span: { start: 63520, end: 63599 }
  source: "demonstrate an understanding of the relationships between Music and technology."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "music and technology"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least show an understanding of how music and technology relate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.7.b6.typical
  locator: { number: "4.7.b6.typical", headingPath: ["Benchmark standards", "Knowledge and understanding"] }
  span: { start: 63600, end: 63733 }
  source: "in addition, show in-depth awareness of current discourse in and on Music technologies through critical work or practice-as-research."
  stem: "4.7"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["show"]
  about: "current discourse on music technologies"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.7.b6, basis: stated }
  paraphrase: "Will typically also show deep awareness of current discussion in and about music technologies, shown through critical writing or research through practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Technical skills"] }
  span: { start: 63874, end: 64007 }
  source: "convey personal expression and imagination in practical music-making through employing appropriate technical and interpretative means"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["convey", "employing"]
  about: "personal expression in practical music-making"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least convey personal expression and imagination when making music, using suitable technical and interpretative means."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.8.b1.typical
  locator: { number: "4.8.b1.typical", headingPath: ["Benchmark standards", "Technical skills"] }
  span: { start: 64008, end: 64143 }
  source: "demonstrate an individual musical personality or ‘voice’, through advanced technical skills and deeper levels of interpretative insight"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "an individual musical voice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.8.b1, basis: stated }
  paraphrase: "Will typically show an individual musical personality or voice, through advanced technique and deeper interpretative insight."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Technical skills"] }
  span: { start: 64144, end: 64245 }
  source: "recognise and use essential components of musical language appropriate to the discipline and practice"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["recognise", "use"]
  about: "the components of musical language"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least recognise and use the essential components of musical language suited to their discipline and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.8.b2.typical
  locator: { number: "4.8.b2.typical", headingPath: ["Benchmark standards", "Technical skills"] }
  span: { start: 64246, end: 64351 }
  source: "in addition, interrogate the use of musical language within different cultural or genre-specific settings"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["interrogate"]
  about: "musical language across cultures and genres"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.8.b2, basis: stated }
  paraphrase: "Will typically also question how musical language is used in different cultural or genre settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Technical skills"] }
  span: { start: 64352, end: 64441 }
  source: "recognise and respond to aspects of musical organisation as appropriate to the discipline"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["recognise", "respond"]
  about: "musical organisation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least recognise and respond to how music is organised, as their discipline requires."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.8.b3.typical
  locator: { number: "4.8.b3.typical", headingPath: ["Benchmark standards", "Technical skills"] }
  span: { start: 64442, end: 64533 }
  source: "in addition, internalise and reconstruct musical materials as appropriate to the discipline"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["internalise", "reconstruct"]
  about: "internalising and rebuilding musical materials"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.8.b3, basis: stated }
  paraphrase: "Will typically also internalise musical materials and rebuild them, as suits the discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Technical skills"] }
  span: { start: 64534, end: 64657 }
  source: "collaborate in music-making, whether through ensemble performance, co-creation, improvisatory work, or analogous activities"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["collaborate"]
  about: "collaborative music-making"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least collaborate in making music, through ensembles, co-creation, improvisation or similar work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.8.b4.typical
  locator: { number: "4.8.b4.typical", headingPath: ["Benchmark standards", "Technical skills"] }
  span: { start: 64658, end: 64729 }
  source: "in addition, demonstrate qualities of leadership within a creative team"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "leadership in a creative team"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.8.b4, basis: stated }
  paraphrase: "Will typically also show leadership within a creative team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Technical skills"] }
  span: { start: 64764, end: 64960 }
  source: "employ music technologies as appropriate to the discipline; this could include recording, producing, composition, sound design, instrument creation, live events, or use of generative technologies."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["employ", "include"]
  about: "using music technologies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least use music technologies as the discipline needs, from recording and production to composition, sound design, instrument making, live events or generative tools."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.8.b5.typical
  locator: { number: "4.8.b5.typical", headingPath: ["Benchmark standards", "Technical skills"] }
  span: { start: 64961, end: 65084 }
  source: "in addition, demonstrate nuance, creative flair and professionalism with the technology in a stylistically appropriate way."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "nuance and flair with technology"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.8.b5, basis: stated }
  paraphrase: "Will typically also use the technology with nuance, creative flair and professionalism, in a way that suits the style."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b1
  locator: { number: "4.9.b1", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 65231, end: 65337 }
  source: "demonstrate independent research skills and the potential for continuing artistic and creative development"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "independent research and creative growth"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least show independent research skills and the potential to keep developing artistically and creatively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b1.typical
  locator: { number: "4.9.b1.typical", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 65338, end: 65428 }
  source: "in addition, demonstrate the potential for artistic and creative leadership and innovation"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "potential for creative leadership and innovation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.9.b1, basis: stated }
  paraphrase: "Will typically also show the potential to lead and innovate artistically and creatively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b2
  locator: { number: "4.9.b2", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 65429, end: 65502 }
  source: "work independently, and show self- motivation and critical self-awareness"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["work", "show"]
  about: "independent work, self-motivation and self-awareness"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least work on their own and show self-motivation and critical awareness of themselves."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b2.typical
  locator: { number: "4.9.b2.typical", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 65503, end: 65600 }
  source: "in addition, produce independent work of high quality (rigorous, defensible, robust, imaginative)"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["produce"]
  about: "high-quality independent work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.9.b2, basis: stated }
  paraphrase: "Will typically also produce strong work on their own that is rigorous, defensible, robust and imaginative."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b3
  locator: { number: "4.9.b3", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 65601, end: 65674 }
  source: "work with others in diverse teams addressing joint projects or activities"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["work", "addressing"]
  about: "working in diverse teams"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least work with others in diverse teams on shared projects or activities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b3.typical
  locator: { number: "4.9.b3.typical", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 65675, end: 65774 }
  source: "in addition, demonstrate advanced skills of teamwork, negotiation, organisation and decision-making"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "teamwork, negotiation and decision-making"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.9.b3, basis: stated }
  paraphrase: "Will typically also show advanced teamwork, negotiation, organisation and decision-making."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b4
  locator: { number: "4.9.b4", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 65775, end: 65855 }
  source: "organise and manage a schedule of work effectively in the execution of a project"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["organise", "manage"]
  about: "scheduling and managing a project"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least plan and manage a schedule of work well when carrying out a project."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b4.typical
  locator: { number: "4.9.b4.typical", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 65856, end: 65943 }
  source: "in addition, demonstrate confidence and adaptability in project planning and management"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "confident, adaptable project planning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.9.b4, basis: stated }
  paraphrase: "Will typically also plan and manage projects with confidence and adaptability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b5
  locator: { number: "4.9.b5", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 65944, end: 66025 }
  source: "demonstrate awareness and respect of different professional and cultural contexts"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "respect for professional and cultural contexts"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least show awareness of, and respect for, different professional and cultural contexts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b5.typical
  locator: { number: "4.9.b5.typical", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 66026, end: 66236 }
  source: "in addition, adapt and respond creatively to different professional and cultural environments, and articulate the value of musical, intellectual and creative skills and associated practices within such contexts"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["adapt", "respond", "articulate"]
  about: "adapting to settings and voicing the value of music skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.9.b5, basis: stated }
  paraphrase: "Will typically also adjust creatively to varied professional and cultural environments and explain the value of musical, intellectual and creative skills there."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b6
  locator: { number: "4.9.b6", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 66237, end: 66413 }
  source: "present work in accessible form, intelligible to both expert and non-expert audiences (readers, listeners, consumers) through sonic, verbal and/or written forms of presentation"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["present"]
  about: "presenting work to expert and general audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least present work accessibly, so that expert and non-expert audiences alike can follow it, in sound, speech or writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b6.typical
  locator: { number: "4.9.b6.typical", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 66414, end: 66503 }
  source: "in addition, demonstrate and articulate imaginative and persuasive powers of presentation"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["demonstrate", "articulate"]
  about: "imaginative, persuasive presentation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.9.b6, basis: stated }
  paraphrase: "Will typically also show imaginative and persuasive presentation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b7
  locator: { number: "4.9.b7", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 66504, end: 66575 }
  source: "demonstrate awareness of appropriate technological and technical skills"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "awareness of technical and technological skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least show awareness of the technological and technical skills that suit their work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b7.typical
  locator: { number: "4.9.b7.typical", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 66576, end: 66692 }
  source: "demonstrate advanced knowledge of the application of technical and technological skills relative to the area studied"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "applying technical skills, advanced"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.9.b7, basis: stated }
  paraphrase: "Will typically show advanced knowledge of how technical and technological skills are applied in their area."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b8
  locator: { number: "4.9.b8", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 66693, end: 66796 }
  source: "demonstrate an awareness of the legal and ethical frameworks relating to Music practices and procedures"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "legal and ethical frameworks in music"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least show awareness of the legal and ethical frameworks that apply to music practice and procedure."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b8.typical
  locator: { number: "4.9.b8.typical", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 66797, end: 66909 }
  source: "identify ethical and political challenges within Music and take steps to ensure ethical practices are undertaken"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["identify", "take", "ensure"]
  about: "ethical and political challenges and ethical practice"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.9.b8, basis: stated }
  paraphrase: "Will typically identify ethical and political challenges in music and act to make sure practice is ethical."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b9
  locator: { number: "4.9.b9", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 66910, end: 66995 }
  source: "communicate musical and creative ideas effectively with others within a creative team"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating ideas in a creative team"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least communicate musical and creative ideas well to others in a creative team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b9.typical
  locator: { number: "4.9.b9.typical", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 66996, end: 67089 }
  source: "in addition, adapt language and terminology when communicating with a variety of stakeholders"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["adapt", "communicating"]
  about: "adapting language for different stakeholders"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.9.b9, basis: stated }
  paraphrase: "Will typically also adjust language and terms when communicating with a range of stakeholders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b10
  locator: { number: "4.9.b10", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 67090, end: 67162 }
  source: "demonstrate an awareness of how Music relates to wider societal concerns"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["demonstrate", "relates"]
  about: "music and wider societal concerns"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least show awareness of how music bears on wider concerns in society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b10.typical
  locator: { number: "4.9.b10.typical", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 67163, end: 67261 }
  source: "in addition, identify ways in which Music can contribute to solving global and societal challenges"
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["identify", "contribute"]
  about: "music and global and societal challenges"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.9.b10, basis: stated }
  paraphrase: "Will typically also identify ways music can help to address global and societal challenges."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b11
  locator: { number: "4.9.b11", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 67262, end: 67317 }
  source: "demonstrate the ability to adapt and continue to learn."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in music at the threshold"
  addressee: learner
  verbs: ["demonstrate", "adapt", "continue"]
  about: "adapting and continuing to learn"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will at least show they can adapt and go on learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.9.b11.typical
  locator: { number: "4.9.b11.typical", headingPath: ["Benchmark standards", "Professional skills"] }
  span: { start: 67318, end: 67399 }
  source: "in addition, demonstrate an ability to contribute to shaping the future of Music."
  stem: "4.9"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates in music at the typical level"
  addressee: learner
  verbs: ["demonstrate", "contribute", "shaping"]
  about: "shaping the future of music"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/music-2025/4.9.b11, basis: stated }
  paraphrase: "Will typically also show they can help shape the future of music."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.10.b1.masters
  locator: { number: "4.10.b1.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 67657, end: 67808 }
  source: "demonstrate both a systematic and comprehensive understanding and a critical awareness of current and emerging trends in Music research and/or practice"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in music"
  addressee: learner
  verbs: ["demonstrate"]
  about: "systematic, critical grasp of current and emerging trends"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to show a systematic, comprehensive and critically aware grasp of current and emerging directions in music research or practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.10.b2.masters
  locator: { number: "4.10.b2.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 67811, end: 67937 }
  source: "evaluate current research and advanced scholarship to apply knowledge in original ways in an area of Music studies or practice"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in music"
  addressee: learner
  verbs: ["evaluate", "apply"]
  about: "evaluating research to apply knowledge originally"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to assess current research and advanced scholarship and use knowledge in original ways in a field of music study or practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.10.b3.masters
  locator: { number: "4.10.b3.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 67940, end: 68082 }
  source: "evaluate appropriate methodologies and demonstrate self-direction and originality in dealing with complex problems in practice and/or research"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in music"
  addressee: learner
  verbs: ["evaluate", "demonstrate", "dealing"]
  about: "method, self-direction and originality with complex problems"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to weigh suitable methodologies and show self-direction and originality in handling complex problems in practice or research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.10.b4.masters
  locator: { number: "4.10.b4.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 68085, end: 68207 }
  source: "create new insight in their field of study, and communicate conclusions clearly to specialist and non-specialist audiences"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in music"
  addressee: learner
  verbs: ["create", "communicate"]
  about: "new insight, communicated to specialists and others"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to generate new insight in their field and convey conclusions clearly to specialist and general audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/music-2025/4.10.b5.masters
  locator: { number: "4.10.b5.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 68210, end: 68335 }
  source: "complete a major piece of practice, or a substantial research project, informed by thorough understandings of the discipline."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in music"
  addressee: learner
  verbs: ["complete", "informed"]
  about: "a major practice project or substantial research project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to complete a major practice project or a substantial research project grounded in a thorough understanding of the discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/music-2025/1.18
  forPractitioner: { text: "Plan for disabled students before anyone asks: consider the conditions that matter in music (strain injuries, hearing and sight, performance anxiety, neurodiversity, long-term illness), admit flexibly and make sure every student can reach studios, rooms, performance spaces and equipment.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty the statement places on music courses through the Equality Act 2010, worded as a responsibility rather than with must or should; it holds at every level and is not an outcome for students. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 1.18) and set it beside paras 1.19 to 1.22 and the caution on competence standards in para 4.3. Do not claim the statement itself creates the legal duty; the duty comes from the Act."
  author-agent-dialogue: "Raise it with a programme team reviewing access to practical teaching, studios or ensembles, or with staff planning admissions. Frame it for staff as a planning duty, never as something a student must do. Ask: which practical activities on this course could a disabled student not yet reach, and what is in place before they arrive? Avoid quoting the list of conditions at length or speaking of a student's condition for them."
- statement: qaa/music-2025/1.31
  forPractitioner: { text: "Design the course so that, by graduation, students will have begun a professional network and a personal brand, tackled complex problems under pressure and built resilience; transferable skills and preparation for working life sit behind this.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you will have started a professional network and your own personal brand, worked through hard problems in demanding situations and grown more resilient.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected outcome (will) for students graduating with honours in music, at FHEQ level 6, placed in the statement's employability, enterprise and entrepreneurship section rather than in the benchmark table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 1.31) and set it beside the professional-skills rows 4.9.b4 and 4.9.b11, the honours descriptor qaa/fheq-2024/4.15.b9.1 and spine:6. Do not claim it is a threshold standard; the table in para 4.9 holds those."
  author-agent-dialogue: "Raise it when a student asks what they should have in place for work by the end of the degree, or a team plans careers provision. Put it in the second person for a student. Ask: who is in your professional network now, and how do you describe your work to someone who might hire you? Avoid making it sound like a marked requirement."
- statement: qaa/music-2025/2.6
  forPractitioner: { text: "Map each level so that it adds knowledge, expertise and experience that lead towards at least the threshold standards at the end, for example longer and more complex performance or composition, or deeper critical and contextual work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Each year of your course will build on the last, adding knowledge, skill and experience, so that by the end you reach at least the minimum standard for the degree; expect your work to grow longer, more complex or more searching as you go.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the statement's account of progression (will, with an expectation) through an honours degree at FHEQ level 6 or an integrated master's at FHEQ level 7, building towards the threshold standards in paras 4.7 to 4.9. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 2.6). Set it beside the level-by-level progression the FHEQ describes (qaa/fheq-2024/4.10, 4.12 and 4.15 descriptors; spine:4 to spine:6). Do not claim it fixes what each level must contain; it leaves the rules to each institution."
  author-agent-dialogue: "Raise it when a student asks how the years of a course fit together, or a team designs level outcomes. Put it plainly; for staff, frame it as the build towards the final threshold. Ask: what in this level's work is longer, harder or deeper than the level before? Avoid treating earlier levels as if they had to meet the final threshold already."
- statement: qaa/music-2025/2.7
  forPractitioner: { text: "Treat a second-class honours result or better as the point at which graduates are expected to be ready for postgraduate study; note that postgraduate entry rules are each provider's own and may ask for particular skills or marks.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you finish with a second-class degree or higher, you can expect to be ready for postgraduate study in music or a related subject, though each course sets its own entry rules.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an expectation (worded as expected and would, not as a requirement) about honours graduates in music at FHEQ level 6 with a second-class result or above. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 2.7) and set it beside the master's outcomes 4.10.b1.masters to 4.10.b5.masters and the Annex D classes (qaa/fheq-2024/annex-d/summary/r1/2.2). Do not claim it entitles anyone to a postgraduate place; entry is set by each provider."
  author-agent-dialogue: "Raise it when a student asks whether their degree result opens the way to a master's. Put it in the second person and plainly. Ask: what result are you working towards, and which skills would the course you have in mind ask for? Avoid promising admission."
- statement: qaa/music-2025/2.8
  forPractitioner: { text: "In a joint or combined degree, make sure the music part delivers the core subject-specific and generic skills, while the partner subject adds its own; look for interdisciplinary openings where the two meet.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study music alongside another subject, you will reach the core music and general skills, and pick up further skills from your other subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected outcome (will) for joint and combined honours students at FHEQ level 6: they meet core elements, not every item, of the standards in paras 4.7 to 4.9. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 2.8). Set it beside para 2.4 on music within other degrees and the honours descriptor qaa/fheq-2024/4.15.b1. Do not claim the statement says which elements are core; it leaves that open."
  author-agent-dialogue: "Raise it when a joint-honours student or a combined-degree team asks how much of the music standards applies to them. Ask: which of the music outcomes does your half of the degree cover in full, and which does the other subject supply instead? Avoid suggesting a joint student must meet every single-honours item."
- statement: qaa/music-2025/2.16
  forPractitioner: { text: "Build the student voice into routine monitoring and periodic review, and use external reference points such as this statement to check that provision sits within sector norms.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider about review; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider expectation (will) for monitoring and review: the student voice forms part of course review. It holds for the course as a whole, not for a level. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 2.16) and set it beside the external review and examining paragraphs 2.17 and 2.19. Do not claim it prescribes a review cycle; it leaves the cycle to each body."
  author-agent-dialogue: "Raise it with a programme team preparing a periodic review or an annual monitoring report. Ask: how have students' views shaped the last round of changes, and where is that recorded? Do not put it to a student as something they must do."
- statement: qaa/music-2025/2.17
  forPractitioner: { text: "Include external reviewers, from other universities, professional bodies or employers, in periodic review to give an independent view on proposed changes and to confirm the threshold standards and the subject content.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider expectation (will) on periodic review, holding for the course as a whole. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 2.17) and set it beside paras 2.16, 2.18 and 2.19 and the threshold columns of paras 4.7 to 4.9 that reviewers check against. Do not claim it is a regulatory rule; the statement is a reference point."
  author-agent-dialogue: "Raise it with a programme team choosing reviewers or planning a review panel. Ask: who outside the institution will look at the proposed changes, and does the panel include someone from practice or industry? Do not present it to students as their concern."
- statement: qaa/music-2025/2.19
  forPractitioner: { text: "Expect an annual report from each external examiner, with recommendations on modules and assessment where needed; arrange live attendance or recordings of recitals and event-based assessment so they can judge.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on external examiners and the provider; not a standard for the student", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement (required) on external examiners: one report a year, with recommendations where needed. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 2.19), and set it beside the rest of para 2.19 on attending or reviewing recorded performances and para 2.18 on the examining system. Do not claim the statement sets the report's content beyond recommendations on modules and assessment."
  author-agent-dialogue: "Raise it with a programme team or a new external examiner planning the year's work. Ask: how will the examiner see live or recorded performances, and how will their recommendations be answered? Do not raise it with students as a duty of theirs."
- statement: qaa/music-2025/3.21
  forPractitioner: { text: "Tell students plainly how each assessment runs and how the mark is worked out, and publish criteria aligned to the learning outcomes and curriculum so they can place their mark and see how to do better next time.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to be told clearly how each assessment works and how your mark is worked out, with criteria that show you how to improve your next piece of work.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation on assessment practice, worded as essential rather than with must or should, holding at every level. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 3.21) and set it beside the feedback paragraphs 3.22 to 3.25 and the reference assessment criteria (std:ref:uk-assesscriteria). Do not claim it prescribes a marking scheme; it asks for clarity and alignment."
  author-agent-dialogue: "Raise it when a student is unsure how a mark was reached, or a team reviews its assessment briefs. For a student, put it as what they can expect to be told; for staff, as what each brief must make plain. Ask: could a student explain from the brief alone how this work will be marked? Avoid turning it into a complaint about a particular marker."
- statement: qaa/music-2025/3.24
  forPractitioner: { text: "Give students room to talk through and question feedback on creative and performance work, and teach them how to interpret and act on it, as preparation for the creative industries.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Because creative and performance work is personal, you will usually get the chance to talk through your feedback, ask what it means and learn how to use it, which is a skill you will need at work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical expectation (will) on feedback for creative and performance work, holding at every level. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 3.24) and set it beside paras 3.21 to 3.23 and 3.25 on feedback and peer feedback. Do not claim it guarantees a meeting for every assessment; the statement says typically."
  author-agent-dialogue: "Raise it when a student is puzzled or upset by feedback on a performance or composition. Put it in the second person: they can ask what the feedback means. Ask: which comment do you least understand, and what would you try differently next time? Avoid defending or overturning the mark yourself."
- statement: qaa/music-2025/4.2
  forPractitioner: { text: "When deciding what evidence shows achievement above the threshold, you should consult Annex D of the UK qualifications Frameworks, which describes the first, upper second, lower second and third classes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to the provider about how it sets evidence for degree classes", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on providers awarding honours in music at FHEQ level 6: they refer to Annex D when judging achievement above the threshold. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.2) and set it beside the threshold and typical columns of paras 4.7 to 4.9 and the Annex D classes in std:doc:qaa-fheq-2024-framework (qaa/fheq-2024/annex-d/summary/r1/3rd to qaa/fheq-2024/annex-d/summary/r1/1st). Do not claim the statement maps its typical level onto a particular class."
  author-agent-dialogue: "Raise it with a programme team writing marking criteria or classification rules. Ask: where do your criteria for the upper bands come from, and do they match the Annex D descriptions? Do not put it to a student as a duty; for a student, talk about the class descriptions instead."
- statement: qaa/music-2025/4.3
  forPractitioner: { text: "Do not treat the benchmark table as a list of competence standards; if you set competence standards in a programme specification, base them on this statement and any PSRB requirements and follow the Equality and Human Rights Commission's current guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to the provider about competence standards; not a standard for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on providers that write competence standards in the Equality Act 2010 sense, holding for the programme as a whole. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.3) and set it beside the accessibility paragraphs 1.18 to 1.22 and the bodies in para 2.14. Do not claim that the threshold or typical items are competence standards; the statement says they are not."
  author-agent-dialogue: "Raise it with a programme team writing a programme specification for an accredited or practice-based course. Ask: does the specification set any competence standards, and has the current Equality and Human Rights Commission guidance been checked against them? Do not put it to a student."
- statement: qaa/music-2025/4.7.b1
  forPractitioner: { text: "Make sure every student can show what they know and understand of a body of music and of the artefacts, texts, resources and ideas attached to it in their field.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to show that you know and understand a body of music and the materials, texts and ideas that go with it in your area.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the knowledge and understanding table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.7, threshold column, row 1). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.7.b1.typical, the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: Which body of music could you talk about with confidence, and what materials and ideas come with it? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.7.b1.typical
  forPractitioner: { text: "Expect most students to go further and engage in depth with the scholarship and research on their musical materials, exploring, testing, applying or challenging it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will be able to explore, weigh up, use or argue against the research and scholarship on the music you study, in depth.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the knowledge and understanding table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.7, typical column, row 1). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.7.b1, the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: Which piece of scholarship on your music have you questioned or put to work in your own writing or practice? Avoid presenting it as the minimum; the threshold item 4.7.b1 is the floor."
- statement: qaa/music-2025/4.7.b2
  forPractitioner: { text: "Make sure every student can show knowledge of the contexts music sits in: history, philosophy, culture, education and society.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to show that you understand the settings music belongs to, such as its history, culture, philosophy, education and social life.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the knowledge and understanding table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.7, threshold column, row 2). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.7.b2.typical, the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: Which historical, cultural or social setting helps you explain the music you work on? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.7.b2.typical
  forPractitioner: { text: "Expect most students to also know the critical arguments that arise when music is read within its wider contexts.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also know the critical arguments that come up when music is placed in its wider setting.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the knowledge and understanding table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.7, typical column, row 2). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.7.b2, the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: Which debate about music and its setting could you outline both sides of? Avoid presenting it as the minimum; the threshold item 4.7.b2 is the floor."
- statement: qaa/music-2025/4.7.b3
  forPractitioner: { text: "Make sure every student can show how music links with other disciplines across the arts, humanities and the social and physical sciences, as suits their course.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to show how music connects with other subjects, such as other arts, the humanities and the social or physical sciences.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the knowledge and understanding table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.7, threshold column, row 3). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.7.b3.typical, the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: Which other subject has changed how you think about music, and how? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.7.b3.typical
  forPractitioner: { text: "Expect most students to also see what working across disciplines means for creative work, innovation and research in music.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also see what working across subjects means for how music is made, renewed and researched.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the knowledge and understanding table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.7, typical column, row 3). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.7.b3, the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: How did drawing on another discipline change a piece of your creative or research work? Avoid presenting it as the minimum; the threshold item 4.7.b3 is the floor."
- statement: qaa/music-2025/4.7.b4
  forPractitioner: { text: "Make sure every student can analyse and probe the musical materials and artefacts of their field and present the results in a coherent form.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to analyse and question musical materials in your area and explain what you find clearly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the knowledge and understanding table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.7, threshold column, row 4). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.7.b4.typical, the honours descriptor qaa/fheq-2024/4.15.b3.1 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: Can you walk through an analysis you have done and say what it showed? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.7.b4.typical
  forPractitioner: { text: "Expect most students to also recognise, critically, where analysis of musical materials leaves matters open or contested.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also be critically aware of where analysing music leaves questions open or in dispute.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the knowledge and understanding table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.7, typical column, row 4). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.7.b4, the honours descriptor qaa/fheq-2024/4.15.b3.1 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/cognitive/r1/2.2 and qaa/fheq-2024/annex-d/cognitive/r1/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: Where did your analysis leave a question open, and how did you deal with that? Avoid presenting it as the minimum; the threshold item 4.7.b4 is the floor."
- statement: qaa/music-2025/4.7.b5
  forPractitioner: { text: "Make sure every student can show how artistic practice and theoretical thinking in music relate, in the area they study.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to show how making music and thinking about it in theory relate to each other in your area.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the knowledge and understanding table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.7, threshold column, row 5). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.7.b5.typical, the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: How does a theory you have learned show up in the music you make or study? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.7.b5.typical
  forPractitioner: { text: "Expect most students to also critique the theories and frameworks used in music: what they are, why they matter, what they do and what follows from them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also be able to critique the theories used in music: what they are, what they are for and what they lead to.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the knowledge and understanding table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.7, typical column, row 5). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.7.b5, the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: Which theoretical idea in music would you challenge, and on what grounds? Avoid presenting it as the minimum; the threshold item 4.7.b5 is the floor."
- statement: qaa/music-2025/4.7.b6
  forPractitioner: { text: "Make sure every student can show how music and technology shape each other.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to show how music and technology are connected.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the knowledge and understanding table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.7, threshold column, row 6). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.7.b6.typical, the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: How has technology changed the music you work with? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.7.b6.typical
  forPractitioner: { text: "Expect most students to also show in-depth awareness of present debate on music technologies, through critical writing or practice-as-research.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also show a deep awareness of current thinking about music technology, through critical work or research through practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the knowledge and understanding table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.7, typical column, row 6). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.7.b6, the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: Which current debate about music technology have you engaged with in your own work? Avoid presenting it as the minimum; the threshold item 4.7.b6 is the floor."
- statement: qaa/music-2025/4.8.b1
  forPractitioner: { text: "Make sure every student can bring personal expression and imagination to practical music-making through apt technique and interpretation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to put your own expression and imagination into making music, using the right technique and interpretation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the technical skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.8, threshold column, row 1). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.8.b1.typical, the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/practical/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: In your last performance or piece, what was yours rather than copied? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.8.b1.typical
  forPractitioner: { text: "Expect most students to show a distinct musical personality, with advanced technique and deeper interpretative insight.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will show a musical voice of your own, backed by advanced technique and deeper insight into interpretation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the technical skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.8, typical column, row 1). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.8.b1, the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/practical/r3/2.2 and qaa/fheq-2024/annex-d/practical/r3/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: What would a listener recognise as your own voice in your music? Avoid presenting it as the minimum; the threshold item 4.8.b1 is the floor."
- statement: qaa/music-2025/4.8.b2
  forPractitioner: { text: "Make sure every student can recognise and use the core elements of musical language that their field and practice need.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to recognise and use the basic building blocks of musical language in your area.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the technical skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.8, threshold column, row 2). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.8.b2.typical, the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: Which elements of musical language do you rely on most in your practice? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.8.b2.typical
  forPractitioner: { text: "Expect most students to also examine how musical language works differently across cultures and genres.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also be able to question how musical language works in different cultures or genres.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the technical skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.8, typical column, row 2). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.8.b2, the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: How does the same musical device work differently in two genres or traditions you know? Avoid presenting it as the minimum; the threshold item 4.8.b2 is the floor."
- statement: qaa/music-2025/4.8.b3
  forPractitioner: { text: "Make sure every student can recognise and respond to the organisation of music in the ways their field needs.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to recognise how music is put together and respond to it, as your area needs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the technical skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.8, threshold column, row 3). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.8.b3.typical, the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: Can you hear or read how a piece is organised and say what you noticed? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.8.b3.typical
  forPractitioner: { text: "Expect most students to also absorb musical materials and reconstruct them, in the way their field calls for.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also be able to take music in so fully that you can rebuild it yourself.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the technical skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.8, typical column, row 3). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.8.b3, the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: Could you reconstruct a passage you have learned from memory or by ear? Avoid presenting it as the minimum; the threshold item 4.8.b3 is the floor."
- statement: qaa/music-2025/4.8.b4
  forPractitioner: { text: "Make sure every student can make music with others, whether in ensembles, joint creation, improvisation or comparable activity.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to make music with other people, in ensembles, by creating together, improvising or in similar ways.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the technical skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.8, threshold column, row 4). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.8.b4.typical, the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: What was your part in the last group you made music with? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.8.b4.typical
  forPractitioner: { text: "Expect most students to also lead within a creative team.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also show that you can lead within a creative team.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the technical skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.8, typical column, row 4). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.8.b4, the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/transferable/r2/2.2 and qaa/fheq-2024/annex-d/transferable/r2/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: When have you led a group of musicians, and what did you do to make it work? Avoid presenting it as the minimum; the threshold item 4.8.b4 is the floor."
- statement: qaa/music-2025/4.8.b5
  forPractitioner: { text: "Make sure every student can work with the music technologies their field needs, such as recording, production, composition, sound design, instrument building, live events or generative tools.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to use the music technology your area needs, such as recording, production, sound design, live events or generative tools.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the technical skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.8, threshold column, row 5). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.8.b5.typical, the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/practical/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: Which music technology do you use, and what do you use it for? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.8.b5.typical
  forPractitioner: { text: "Expect most students to also handle technology with nuance, creative flair and professional polish, in keeping with the style.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also use technology with subtlety, flair and professional polish, in a way that suits the style of the music.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the technical skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.8, typical column, row 5). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.8.b5, the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/practical/r3/2.2 and qaa/fheq-2024/annex-d/practical/r3/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: Where in your recent work did your use of technology show style and polish rather than only function? Avoid presenting it as the minimum; the threshold item 4.8.b5 is the floor."
- statement: qaa/music-2025/4.9.b1
  forPractitioner: { text: "Make sure every student can show research skills of their own and promise of continued artistic and creative growth.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to show that you can research on your own and that you can keep growing as an artist.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, threshold column, row 1). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.9.b1.typical, the honours descriptor qaa/fheq-2024/4.15.b5 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: What have you found out through your own research recently? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.9.b1.typical
  forPractitioner: { text: "Expect most students to also show promise as artistic and creative leaders and innovators.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also show that you have it in you to lead and break new ground creatively.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, typical column, row 1). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.9.b1, the honours descriptor qaa/fheq-2024/4.15.b5 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/transferable/r3/2.2 and qaa/fheq-2024/annex-d/transferable/r3/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: Where have you tried something new that others could follow? Avoid presenting it as the minimum; the threshold item 4.9.b1 is the floor."
- statement: qaa/music-2025/4.9.b2
  forPractitioner: { text: "Make sure every student can work independently and shows drive and critical self-awareness.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to work on your own, keep yourself going and look critically at your own work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, threshold column, row 2). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.9.b2.typical, the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: How do you keep a long project moving when no one is checking on you? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.9.b2.typical
  forPractitioner: { text: "Expect most students to also produce independent work of a high standard that is rigorous, defensible, robust and imaginative.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also produce strong work of your own that is careful, well argued, sturdy and imaginative.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, typical column, row 2). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.9.b2, the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/transferable/r3/2.2 and qaa/fheq-2024/annex-d/transferable/r3/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: Which piece of your own work would you defend as rigorous and imaginative, and why? Avoid presenting it as the minimum; the threshold item 4.9.b2 is the floor."
- statement: qaa/music-2025/4.9.b3
  forPractitioner: { text: "Make sure every student can work with others in mixed teams on joint projects or activities.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to work with a mix of people in teams on shared projects.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, threshold column, row 3). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.9.b3.typical, the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: What did you contribute to the last team project you were part of? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.9.b3.typical
  forPractitioner: { text: "Expect most students to also show advanced skill in teamwork, negotiating, organising and making decisions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also show advanced skill in working in a team, negotiating, organising and deciding.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, typical column, row 3). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.9.b3, the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/transferable/r2/2.2 and qaa/fheq-2024/annex-d/transferable/r2/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: When did you help a team reach a decision it was stuck on? Avoid presenting it as the minimum; the threshold item 4.9.b3 is the floor."
- statement: qaa/music-2025/4.9.b4
  forPractitioner: { text: "Make sure every student can organise and run a work schedule effectively while delivering a project.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to plan and keep to a schedule of work when you carry out a project.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, threshold column, row 4). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.9.b4.typical, the honours descriptor qaa/fheq-2024/4.15.b9.2 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: How did you plan the time for your last project, and did it hold? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.9.b4.typical
  forPractitioner: { text: "Expect most students to also plan and manage projects confidently and adapt when things change.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also plan and run projects with confidence and adjust when plans change.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, typical column, row 4). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.9.b4, the honours descriptor qaa/fheq-2024/4.15.b9.2 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/transferable/r3/2.2 and qaa/fheq-2024/annex-d/transferable/r3/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: When a project plan went wrong, how did you change it? Avoid presenting it as the minimum; the threshold item 4.9.b4 is the floor."
- statement: qaa/music-2025/4.9.b5
  forPractitioner: { text: "Make sure every student can show awareness of and respect for varied professional and cultural settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to show that you know about, and respect, different professional and cultural settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, threshold column, row 5). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.9.b5.typical, the honours descriptor qaa/fheq-2024/4.15.b9.2 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/transferable/r4/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: Which professional or cultural setting outside your usual one have you worked in? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.9.b5.typical
  forPractitioner: { text: "Expect most students to also adapt creatively to different professional and cultural environments and make the case for musical, intellectual and creative skills within them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also adapt creatively to different working and cultural settings and explain what musical and creative skills bring to them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, typical column, row 5). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.9.b5, the honours descriptor qaa/fheq-2024/4.15.b9.2 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/transferable/r4/2.2 and qaa/fheq-2024/annex-d/transferable/r4/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: How would you explain the value of your musical skills to an employer outside music? Avoid presenting it as the minimum; the threshold item 4.9.b5 is the floor."
- statement: qaa/music-2025/4.9.b6
  forPractitioner: { text: "Make sure every student can present work in a form both specialists and non-specialists can follow, through sound, speech or writing.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to present your work so that both experts and people new to it can follow, in sound, speech or writing.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, threshold column, row 6). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.9.b6.typical, the honours descriptor qaa/fheq-2024/4.15.b8 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: Could someone with no music training follow your last presentation or programme note? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.9.b6.typical
  forPractitioner: { text: "Expect most students to also present imaginatively and persuasively.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also present your work in imaginative and persuasive ways.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, typical column, row 6). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.9.b6, the honours descriptor qaa/fheq-2024/4.15.b8 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/transferable/r1/2.2 and qaa/fheq-2024/annex-d/transferable/r1/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: What did you do in a recent presentation to win the audience over? Avoid presenting it as the minimum; the threshold item 4.9.b6 is the floor."
- statement: qaa/music-2025/4.9.b7
  forPractitioner: { text: "Make sure every student can show awareness of the technical and technological skills their work calls for.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to show that you know which technical and technological skills your work needs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, threshold column, row 7). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.9.b7.typical, the honours descriptor qaa/fheq-2024/4.15.b9.3 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: Which technical skills does your kind of music work depend on? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.9.b7.typical
  forPractitioner: { text: "Expect most students to show advanced knowledge of applying technical and technological skills in the area they study.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will show advanced knowledge of how to apply technical and technological skills in your area.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, typical column, row 7). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.9.b7, the honours descriptor qaa/fheq-2024/4.15.b9.3 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: Where have you applied a technical skill in a way a beginner would not? Avoid presenting it as the minimum; the threshold item 4.9.b7 is the floor."
- statement: qaa/music-2025/4.9.b8
  forPractitioner: { text: "Make sure every student can show awareness of the legal and ethical rules that govern music practice and procedure, such as rights and consent.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to show that you know the legal and ethical rules that apply to working in music.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, threshold column, row 8). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.9.b8.typical, the honours descriptor qaa/fheq-2024/4.15.b4 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/professional/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: Which legal or ethical rules have applied to music you have made, recorded or shared? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.9.b8.typical
  forPractitioner: { text: "Expect most students to spot ethical and political challenges in music and take steps so that practice stays ethical.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will spot ethical and political problems in music and take action so that the work is done ethically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, typical column, row 8). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.9.b8, the honours descriptor qaa/fheq-2024/4.15.b4 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/professional/r2/2.2 and qaa/fheq-2024/annex-d/professional/r2/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: When did you notice an ethical problem in a music project, and what did you do? Avoid presenting it as the minimum; the threshold item 4.9.b8 is the floor."
- statement: qaa/music-2025/4.9.b9
  forPractitioner: { text: "Make sure every student can get musical and creative ideas across to others in a creative team.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to get your musical and creative ideas across to others in a creative team.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, threshold column, row 9). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.9.b9.typical, the honours descriptor qaa/fheq-2024/4.15.b8 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: How do you explain a musical idea to the rest of a band or team? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.9.b9.typical
  forPractitioner: { text: "Expect most students to also adjust their language and terms for the different people they deal with.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also change your language and terms to suit the different people you work with.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, typical column, row 9). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.9.b9, the honours descriptor qaa/fheq-2024/4.15.b8 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/transferable/r1/2.2 and qaa/fheq-2024/annex-d/transferable/r1/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: How would you describe the same project to a fellow musician, a funder and an audience? Avoid presenting it as the minimum; the threshold item 4.9.b9 is the floor."
- statement: qaa/music-2025/4.9.b10
  forPractitioner: { text: "Make sure every student can show awareness of how music connects with wider questions in society.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to show that you understand how music connects with wider issues in society.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, threshold column, row 10). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.9.b10.typical, the honours descriptor qaa/fheq-2024/4.15.b4 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: Which issue in society does the music you study speak to? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.9.b10.typical
  forPractitioner: { text: "Expect most students to also identify ways music can help meet global and social challenges.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also be able to name ways music can help with global and social challenges.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, typical column, row 10). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.9.b10, the honours descriptor qaa/fheq-2024/4.15.b4 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/transferable/r5/2.2 and qaa/fheq-2024/annex-d/transferable/r5/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: How could music help with a problem in your community or beyond? Avoid presenting it as the minimum; the threshold item 4.9.b10 is the floor."
- statement: qaa/music-2025/4.9.b11
  forPractitioner: { text: "Make sure every student can show adaptability and the capacity to keep learning.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the minimum for your honours degree, you will be able to show that you can adapt and keep learning.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum every student shows for a bachelor's degree with honours in music, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, threshold column, row 11). Do not claim it is a regulatory requirement or that it describes master's study. Set it beside its typical partner 4.9.b11.typical, the honours descriptor qaa/fheq-2024/4.15.b9.3 with spine:6, and the third-class cell qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. Put it plainly: second person for a student, and for staff as what assessment lets every student show. Ask: What have you had to learn quickly or change how you work recently? Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."
- statement: qaa/music-2025/4.9.b11.typical
  forPractitioner: { text: "Expect most students to also show they can contribute to where music goes next.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Going beyond the minimum, as most students do, you will also show that you can help shape where music goes next.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a typical standard (will): what most honours graduates in music show, above the minimum, at FHEQ level 6 (FQHEIS level 10), in the professional skills table. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.9, typical column, row 11). Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). Set it beside the threshold item 4.9.b11, the honours descriptor qaa/fheq-2024/4.15.b9.3 with spine:6, and the Annex D cells qaa/fheq-2024/annex-d/transferable/r3/2.2 and qaa/fheq-2024/annex-d/transferable/r3/2.1."
  author-agent-dialogue: "Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. Ask: What change in music would you like to be part of, and what are you doing towards it? Avoid presenting it as the minimum; the threshold item 4.9.b11 is the floor."
- statement: qaa/music-2025/4.10.b1.masters
  forPractitioner: { text: "Expect master's students to show a systematic and thorough understanding of current and emerging directions in music research or practice, with critical awareness.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your master's degree, you will be able to show a systematic, thorough and critical grasp of where music research or practice is now and where it is heading.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's outcome (will) at FHEQ level 7 (FQHEIS level 11), recorded at the threshold rung, which adds to the honours standards in paras 4.7 to 4.9 for master's study in music. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.10). Set it beside the honours item 4.7.b1.typical and the master's descriptor qaa/fheq-2024/4.17.b1 with spine:7. Do not claim it applies to honours graduates or that the statement grades master's work into threshold and typical levels."
  author-agent-dialogue: "Raise it when a master's student or a postgraduate team asks how master's work differs from honours. Put it in plain words, second person for a student. Ask: Which current development in your area of music could you explain and critique to a specialist? Avoid presenting it as an honours expectation."
- statement: qaa/music-2025/4.10.b2.masters
  forPractitioner: { text: "Expect master's students to evaluate current research and advanced scholarship and apply what they know with originality.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your master's degree, you will be able to judge current research and advanced scholarship and use what you know in original ways.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's outcome (will) at FHEQ level 7 (FQHEIS level 11), recorded at the threshold rung, which adds to the honours standards in paras 4.7 to 4.9 for master's study in music. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.10). Set it beside the honours item 4.7.b1.typical and the master's descriptor qaa/fheq-2024/4.17.b3 with spine:7. Do not claim it applies to honours graduates or that the statement grades master's work into threshold and typical levels."
  author-agent-dialogue: "Raise it when a master's student or a postgraduate team asks how master's work differs from honours. Put it in plain words, second person for a student. Ask: Where has your reading of recent research changed what you made or argued? Avoid presenting it as an honours expectation."
- statement: qaa/music-2025/4.10.b3.masters
  forPractitioner: { text: "Expect master's students to choose and justify methods and to tackle complex problems with self-direction and originality.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your master's degree, you will be able to weigh up methods and tackle complex problems in practice or research on your own initiative and in original ways.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's outcome (will) at FHEQ level 7 (FQHEIS level 11), recorded at the threshold rung, which adds to the honours standards in paras 4.7 to 4.9 for master's study in music. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.10). Set it beside the honours item 4.9.b2.typical and the master's descriptor qaa/fheq-2024/4.17.b6 with spine:7. Do not claim it applies to honours graduates or that the statement grades master's work into threshold and typical levels."
  author-agent-dialogue: "Raise it when a master's student or a postgraduate team asks how master's work differs from honours. Put it in plain words, second person for a student. Ask: Which method did you choose for your current project, and what made it the right one? Avoid presenting it as an honours expectation."
- statement: qaa/music-2025/4.10.b4.masters
  forPractitioner: { text: "Expect master's students to produce new insight in their field and communicate their conclusions clearly to both specialists and non-specialists.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your master's degree, you will be able to come up with new insight in your field and explain your conclusions clearly to experts and to people outside it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's outcome (will) at FHEQ level 7 (FQHEIS level 11), recorded at the threshold rung, which adds to the honours standards in paras 4.7 to 4.9 for master's study in music. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.10). Set it beside the honours item 4.9.b6.typical and the master's descriptor qaa/fheq-2024/4.17.b5 with spine:7. Do not claim it applies to honours graduates or that the statement grades master's work into threshold and typical levels."
  author-agent-dialogue: "Raise it when a master's student or a postgraduate team asks how master's work differs from honours. Put it in plain words, second person for a student. Ask: What new insight has your work produced, and how would you explain it to someone outside music? Avoid presenting it as an honours expectation."
- statement: qaa/music-2025/4.10.b5.masters
  forPractitioner: { text: "Expect master's students to carry through a major practice-based project or a sizeable research project, grounded in thorough understanding of the discipline.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your master's degree, you will be able to complete a major practical project or a substantial piece of research, built on a thorough understanding of your field.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's outcome (will) at FHEQ level 7 (FQHEIS level 11), recorded at the threshold rung, which adds to the honours standards in paras 4.7 to 4.9 for master's study in music. Cite it as (QAA, 2025, Music Subject Benchmark Statement, para 4.10). Set it beside the honours item 4.9.b4.typical and the master's descriptor qaa/fheq-2024/4.17.b2 with spine:7. Do not claim it applies to honours graduates or that the statement grades master's work into threshold and typical levels."
  author-agent-dialogue: "Raise it when a master's student or a postgraduate team asks how master's work differs from honours. Put it in plain words, second person for a student. Ask: What is your major project, and how does it draw on your understanding of the field? Avoid presenting it as an honours expectation."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.6 (honours: FHEQ Level 6)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.6 (honours: FQHEIS Level 10)" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.6 (integrated master's: FHEQ Level 7); 4.10 (master's list, level inferred)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.6 (integrated master's: FQHEIS Level 11)" }
  - { id: "fheq:4", role: "cites", locator: "D1, 2.9 (CertHE)" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 2.9 (CertHE, as the statement gives it)" }
  - { id: "fheq:5", role: "cites", locator: "D1, 2.9 (DipHE)" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.9 (DipHE, as the statement gives it)" }
  - { id: "spine:6", role: "refers", locator: "std:ref:uk-framework R2 (inferred)" }
  - { id: "spine:7", role: "refers", locator: "std:ref:uk-framework R2 (inferred)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.6); agrees with std:doc:qaa-fheq-2024-framework Table 1" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.6); agrees with std:doc:qaa-fheq-2024-framework Table 1" }
  - { from: "fheq:4", to: "fqheis:8", relation: "equivalent", basis: "stated (D1, 2.9) for the CertHE; differs from std:doc:qaa-fheq-2024-framework Table 1 (CertHE at fqheis:7): Part E" }
  - { from: "fheq:5", to: "fqheis:9", relation: "equivalent", basis: "stated (D1, 2.9) for the DipHE; differs from std:doc:qaa-fheq-2024-framework Table 1 (DipHE at fqheis:8): Part E" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "2.3", "3.6", "3.18"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.18", "1.19", "1.20", "1.21", "1.22", "3.6", "3.14", "4.3"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.23", "1.24", "1.25", "1.26", "1.41"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "1.35", "1.36", "2.2", "2.13", "3.5", "3.13"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["1.37", "1.38", "1.39", "1.40", "1.41", "4.8"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "4.2: providers refer to the degree classification descriptions" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "2.6, 2.9: FHEQ levels 4 to 7 named" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "2.6, 2.9: FQHEIS levels 8 to 11 named" }
- { rel: "refersTo", target: "Equality and Human Rights Commission guidance on competence standards (not yet ingested)", note: "4.3; Part E" }
- { rel: "refersTo", target: "Equality Act 2010 (legislation; not a standards document)", note: "1.18, 4.3" }
- { rel: "refersTo", target: "National Plans for Music Education, England and Wales (2022; not yet ingested)", note: "2.15" }
- { rel: "refersTo", target: "United Nations Sustainable Development Goals (not yet ingested)", note: "1.24, 1.25" }
- { rel: "refersTo", target: "JAMES, CDMT and HCPC accreditation requirements (not yet ingested)", note: "2.14; Part E" }
- { rel: "overlaps", target: "std:doc:qaa-dance-drama-and-performance-2024-benchmarks", note: "inferred: musical theatre and performance (1.10, 2.14); Part E" }
- { rel: "relatedTo", target: "other Subject Benchmark Statements for music-adjacent subjects", note: "3.4 says Music Business and Music Therapy may reference other statements; inferred, not named" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2025-04"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "none-stated; an advisory group of academics, students and sector members (D1, section 6)"
replacedBy: "none"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- Music in higher education is a wide field of intellectual and creative activity that builds specialist and general skills and opens many careers inside and outside music (D1, 1.1)
- Degrees differ greatly in content, method and approach; some keep to one tradition while others are plural, reflecting cultural diversity (D1, 1.2, 1.4)
- Its distinctive elements are practice, creative invention, sensory skill, collaboration and special literacies such as notation and programming, which need space, instruments, technology, collections and practitioner staff (D1, 1.6)
- It can be arts- or science-based and meets many other subjects, from the humanities and business to engineering, physics, psychology, medicine and education (D1, 1.5, 2.3)
- Every programme draws on linked activities: reading musical texts, creative and re-creative practice, analysis and criticism, repertories and their contexts, the social value of music, teaching music, aesthetics and reception, theory and practice, and vocational skills (D1, 2.2)
- It is offered by universities and specialist conservatoires, each with its own mission, to learners who arrive by academic, vocational or self-taught routes (D1, 1.7, 1.8)
- Graduates often work for themselves in portfolio careers across music, education, broadcasting, healthcare and the wider cultural sector (D1, 1.9, 1.29)

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "music study questions inherited canons and privilege, opens to global, decolonial, disability-centred and gender-focused perspectives, and tackles unequal access to instruments, tuition and admission (D1, 1.12 to 1.17)"
  statements: []
- theme: theme:accessibility
  inThisSubject: "courses plan for disabilities that bear on music study (strain injuries, hearing and sight, performance anxiety, neurodiversity) and make lessons, ensembles, studios, placements and online material reachable (D1, 1.18 to 1.22)"
  statements: ["qaa/music-2025/1.18", "qaa/music-2025/4.3"]
- theme: theme:esd
  inThisSubject: "students weigh the environmental and social footprint of music-making, from instrument materials and touring to the global music economy, and music is framed against the UN goals (D1, 1.23 to 1.26)"
  statements: []
- theme: theme:enterprise
  inThisSubject: "enterprise is built into the curriculum through events, commissions, briefs, microbusinesses, placements and practitioner staff, preparing students for freelance portfolio careers (D1, 1.27 to 1.36)"
  statements: ["qaa/music-2025/1.31"]
- theme: theme:generative-ai
  inThisSubject: "generative AI is used in teaching and assessed projects as a creative collaborator, with guidance on rights, plagiarism, labour, environmental cost and bias (D1, 1.37 to 1.41; 4.8)"
  statements: ["qaa/music-2025/4.8.b5"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "2.2", gloss: "the linked activities every programme draws on, from musical texts and practice to aesthetics and vocational skills" }
  - { component: "3.3", gloss: "specialist or generalist; arts or science; vocational or liberal" }
  - { component: "3.4", gloss: "joint study and music-adjacent subjects such as music business and music therapy" }
  - { component: "3.5", gloss: "the skills and attributes graduates share, set out further in section 4" }
  - { component: "1.6", gloss: "the subject's distinctive elements and their resource needs" }
practices:
  - { component: "3.6", kind: "teaching", gloss: "varied, inclusive teaching with practical learning, in person, online or hybrid" }
  - { component: "3.7", kind: "teaching", gloss: "lectures and seminars for history, analysis and criticism" }
  - { component: "3.9", kind: "teaching", gloss: "one-to-one tuition in performance or composition" }
  - { component: "3.10", kind: "teaching", gloss: "ensemble tuition, workshops and masterclasses" }
  - { component: "3.12", kind: "learning", gloss: "formal and extracurricular performing, often student-led" }
  - { component: "3.13", kind: "learning", gloss: "industry-linked learning, placements and mentoring" }
  - { component: "1.39", kind: "teaching", gloss: "teaching adapted to use generative AI" }
  - { component: "1.40", kind: "assessment", gloss: "assessment adapted to use generative AI" }
  - { component: "3.19", kind: "assessment", gloss: "indicative methods: written, presented and performed work, and artefacts" }
  - { component: "3.20", kind: "assessment", gloss: "projects and portfolios, peer and self-assessment" }
  - { component: "3.21", kind: "assessment", gloss: "clear criteria and marking" }
  - { component: "3.23", kind: "assessment", gloss: "continuous feedback and feed forward" }
  - { component: "3.25", kind: "assessment", gloss: "peer feedback networks" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.7; 4.8; 4.9; 4.10", award: ["bachelor's with honours", "master's"], items: 27 }
  - { rung: "typical", leadIn: "4.7; 4.8; 4.9", award: "bachelor's with honours", items: 22 }
  - { rung: "excellent", leadIn: "none", award: "bachelor's with honours", items: 0 }
rungBases: "4.1 names two rungs, the minimum threshold and the typical standard, for the honours degree; each of 4.7 to 4.9 is a two-column table (Threshold level, Typical level) under one lead-in, flattened in the held text and read row by row: 22 rows, 22 threshold and 22 typical cells, each typical cell paired with the threshold cell in its row (gradeOf stated). The threshold count of 27 is 22 honours cells and 5 master's outcomes (4.10), recorded at the threshold rung with award master's by the brief's convention. Excellence is described only in prose (4.4), with no list, so the excellent rung has no items."
outcomeLists:
  - { leadIn: "4.10", gloss: "outcomes added for master's study, beyond the honours standards", items: 5, award: ["master's"] }
outcomes:
  - { outcome: "a body of music and its materials", threshold: "qaa/music-2025/4.7.b1", typical: "qaa/music-2025/4.7.b1.typical", excellent: "none", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "musical contexts", threshold: "qaa/music-2025/4.7.b2", typical: "qaa/music-2025/4.7.b2.typical", excellent: "none", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "music and other disciplines", threshold: "qaa/music-2025/4.7.b3", typical: "qaa/music-2025/4.7.b3.typical", excellent: "none", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "analysing musical materials and reporting findings", threshold: "qaa/music-2025/4.7.b4", typical: "qaa/music-2025/4.7.b4.typical", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "practice and theory in music", threshold: "qaa/music-2025/4.7.b5", typical: "qaa/music-2025/4.7.b5.typical", excellent: "none", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "music and technology", threshold: "qaa/music-2025/4.7.b6", typical: "qaa/music-2025/4.7.b6.typical", excellent: "none", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "personal expression in practical music-making", threshold: "qaa/music-2025/4.8.b1", typical: "qaa/music-2025/4.8.b1.typical", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "the components of musical language", threshold: "qaa/music-2025/4.8.b2", typical: "qaa/music-2025/4.8.b2.typical", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "musical organisation", threshold: "qaa/music-2025/4.8.b3", typical: "qaa/music-2025/4.8.b3.typical", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "collaborative music-making", threshold: "qaa/music-2025/4.8.b4", typical: "qaa/music-2025/4.8.b4.typical", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "using music technologies", threshold: "qaa/music-2025/4.8.b5", typical: "qaa/music-2025/4.8.b5.typical", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "independent research and creative growth", threshold: "qaa/music-2025/4.9.b1", typical: "qaa/music-2025/4.9.b1.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "independent work, self-motivation and self-awareness", threshold: "qaa/music-2025/4.9.b2", typical: "qaa/music-2025/4.9.b2.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "working in diverse teams", threshold: "qaa/music-2025/4.9.b3", typical: "qaa/music-2025/4.9.b3.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "scheduling and managing a project", threshold: "qaa/music-2025/4.9.b4", typical: "qaa/music-2025/4.9.b4.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "respect for professional and cultural contexts", threshold: "qaa/music-2025/4.9.b5", typical: "qaa/music-2025/4.9.b5.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "presenting work to expert and general audiences", threshold: "qaa/music-2025/4.9.b6", typical: "qaa/music-2025/4.9.b6.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "awareness of technical and technological skills", threshold: "qaa/music-2025/4.9.b7", typical: "qaa/music-2025/4.9.b7.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "legal and ethical frameworks in music", threshold: "qaa/music-2025/4.9.b8", typical: "qaa/music-2025/4.9.b8.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "communicating ideas in a creative team", threshold: "qaa/music-2025/4.9.b9", typical: "qaa/music-2025/4.9.b9.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "music and wider societal concerns", threshold: "qaa/music-2025/4.9.b10", typical: "qaa/music-2025/4.9.b10.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "adapting and continuing to learn", threshold: "qaa/music-2025/4.9.b11", typical: "qaa/music-2025/4.9.b11.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
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
- { body: "Professional, statutory and regulatory bodies (PSRBs) in general", says: "may use the statement in defining academic standards; accredit some music courses by reviewing curriculum, facilities, staffing, assessment and partnerships; their requirements may inform competence standards (D1, front matter; 2.14; 2.20; 4.3)", requirements: "not yet ingested (Part E)" }
- { body: "JAMES (Joint Audio Media Education Services)", says: "named as an accreditor for areas such as music production (D1, 2.14)", requirements: "not yet ingested (Part E)" }
- { body: "CDMT (Council for Dance, Drama and Musical Theatre)", says: "named as an accreditor for areas such as musical theatre (D1, 2.14)", requirements: "not yet ingested (Part E)" }
- { body: "HCPC (Health and Care Professions Council)", says: "named as an accreditor for areas such as music therapy (D1, 2.14)", requirements: "not yet ingested (Part E)" }
- { body: "Equality and Human Rights Commission", says: "its latest guidance is to be followed by providers that set competence standards (D1, 4.3)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equity, diversity and inclusion", carriedIn: ["1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "2.3", "3.6", "3.18"], statements: [] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["1.18", "1.19", "1.20", "1.21", "1.22", "3.6", "3.14", "4.3"], statements: ["1.18", "4.3"] }
  - { id: "theme:esd", named: "Education for sustainable development", carriedIn: ["1.23", "1.24", "1.25", "1.26", "1.41"], statements: [] }
  - { id: "theme:enterprise", named: "Employability, enterprise and entrepreneurship education", carriedIn: ["1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "1.35", "1.36", "2.2", "2.13", "3.5", "3.13"], statements: ["1.31"] }
  - { id: "theme:generative-ai", named: "Generative artificial intelligence (GenAI)", carriedIn: ["1.37", "1.38", "1.39", "1.40", "1.41", "4.8"], statements: ["4.8.b5"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["2.6", "2.9", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.6", "2.9"] }
bodies:
  - { body: "PSRBs (in general)", citedIn: ["2.14", "2.20", "4.3"] }
  - { body: "JAMES", citedIn: ["2.14"] }
  - { body: "CDMT", citedIn: ["2.14"] }
  - { body: "HCPC", citedIn: ["2.14"] }
  - { body: "Equality and Human Rights Commission", citedIn: ["4.3"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "the common descriptions of the four honours classes, for judging achievement above the threshold" }
  - { document: "not yet ingested: listed in Part E", named: "Equality Act (2010)", citedIn: ["1.18", "4.3"], role: "the legal basis for duties to disabled students and for competence standards" }
  - { document: "not yet ingested: listed in Part E", named: "United Nations Sustainable Development Goals (SDGs)", citedIn: ["1.24", "1.25"], role: "a frame for sustainability in the curriculum" }
  - { document: "not yet ingested: listed in Part E", named: "National Plans for Music Education in Wales and England (both 2022)", citedIn: ["2.15"], role: "context for partnerships with schools and colleges" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "continuous-feedback", definition: "information given to students throughout a course in order to improve their learning and attainment (D1, 3.23)", beneficiaryDefinition: "ongoing comments on your work meant to help you improve", scopeNote: "said to be a strength of many music courses", category: "unknown", practices: ["education"] }
- { slug: "feed-forward", definition: "feedback framed so that students can carry what they learned into later projects (D1, 3.23)", beneficiaryDefinition: "feedback that tells you what to do next time", scopeNote: "given in quotation marks in the text", category: "unknown", practices: ["education"] }
- { slug: "enterprise-and-entrepreneurship-education", definition: "education that builds the behaviours, attributes and competencies that shape career choice and success, abbreviated EEE (D1, 1.27)", beneficiaryDefinition: "learning that prepares you to make your own opportunities and work", scopeNote: "paired with employability in the section heading", category: "unknown", practices: ["education"] }
- { slug: "education-for-sustainable-development", definition: "a holistic approach across the curriculum to linked questions of climate change, social justice and global inequality, abbreviated ESD (D1, 1.23)", beneficiaryDefinition: "learning that helps you act for a sustainable future", scopeNote: "framed with the UN SDGs", category: "unknown", practices: ["education"] }
- { slug: "threshold-and-typical", definition: "the two rungs of benchmark standards: the minimum shown at award and what most students show (D1, 4.1, 4.2)", beneficiaryDefinition: "the minimum and the usual standard for your honours degree", scopeNote: "excellence is described in prose only (4.4)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "continuous-feedback", form: "continuous feedback", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "feed-forward", form: "feed forward", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "enterprise-and-entrepreneurship-education", form: "Enterprise and entrepreneurship education (EEE)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "education-for-sustainable-development", form: "Education for Sustainable Development (ESD)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-and-typical", form: "minimum threshold and typical standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Music"
  edition: "April 2025 (fifth edition)"
  year: 2025
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/music-2025/music-2025.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 0411d7548d143e9a8973b70047b56db3f0d07cb097b820d589c1655cf95494f8
  heldFiles: ["wkspc2601-library/txt/qaa-2025-music-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2025-music-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2025-music-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2025-music-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0082", source: "QAA Subject Benchmark Statement: Music (2019, minor update)", why: "the edition this one supersedes, for the change comparison" }
- { w: "W-std-0083", source: "Equality and Human Rights Commission guidance on competence standards", why: "cited in 4.3 for providers setting competence standards" }
- { w: "W-std-0084", source: "Accreditation requirements of JAMES, CDMT and HCPC", why: "the bodies named in 2.14; their requirements are their own standards documents" }
- { w: "W-std-0085", source: "National Plans for Music Education, England (HM Government, 2022) and Wales (Welsh Government, 2022)", why: "cited in 2.15 and in section 5" }
```

## Part E Gaps and questions
- Rungs: two, threshold and typical, set as one two-column table (Threshold level | Typical level) in each of 4.7, 4.8 and 4.9 under the lead-in 'students are able to'; 6, 5 and 11 rows. Psychology has a separate list per rung. The table is flattened in the held text and was read row by row: each typical cell normally opens 'in addition,', which marks the row boundary.
- Placements to confirm at P3 (no 'in addition' marker): 4.8.b1.typical (the individual 'voice' cell), 4.9.b7.typical (advanced technical knowledge) and 4.9.b8.typical (ethical and political challenges). Each sits between two threshold cells in the text and is read as its row's typical cell.
- gradeOf is recorded as stated for all 22 typical cells: the issuer pairs the columns by row, and most typical cells say 'in addition' to their threshold partner. The three rows above rest on the row reading alone; if P3 treats them as inferred, change GRADE for those three ids.
- No excellent rung: 4.4 describes excellence in prose (professionalism in presentation; innovative scholarly or creative approaches) with 'may', and gives no list. SB4 records the excellent rung with leadIn none and 0 items.
- Master's: 4.10 lists five outcomes under 'Through completing a master's degree, students are able to', after a stem saying master's study 'requires' critical and conceptual understanding beyond the honours standards. Recorded at the threshold rung with award master's, level fheq:7 (inferred: 4.10 names no level; 2.6 names FHEQ 7 only for the integrated master's) and ids 4.10.b<k>.masters, per the brief. The stem's 'requires' is read as the lead-in, not a statement of its own.
- Force words outside the five: 1.18 'have a responsibility to' (force describes); 2.7 'it is expected that ... would be capable of' (describes); 3.21 'it is essential ... that students are provided with clarity' (describes); 2.6 'it is expected that each level sees' sits beside 'will progress' (force will, from the latter). For Abbott.
- Threshold cells take force threshold: 4.1 calls them the 'minimum threshold' standards for the honours award. Typical cells take the lead-in's 'are able to' (will), via forceFrom on the table's paragraph.
- Plain-present provider norms, not statements (template open point 5): 1.19 to 1.22 (course teams ensure access, adjustments and accessible materials), 1.32 ('will often involve' organising events), 1.38 and 1.41 (students work to build a critical understanding of AI; students are provided with guidance), 2.18 (external examiners will typically be asked), 2.20 (courses may require accreditation), 3.6 to 3.14 and 3.22 to 3.23 (teaching and feedback norms).
- Not statements by judgement: 4.1 (the rung definition, kept as the lead-in component); 2.5 ('some programmes will allow' is descriptive); 3.17 ('skills that will be used' is descriptive); 4.11 ('may equip').
- 2.19 is cut to its obliging sentence ('External examiners are required to produce a report each year ...'); the rest of the paragraph is descriptive (may).
- 2.9 states the CertHE at FQHEIS Level 8 and the DipHE at FQHEIS Level 9, where std:doc:qaa-fheq-2024-framework Table 1 and std:doc:qaa-fqheis-2024-framework S5 put them at fqheis:7 and fqheis:8. Recorded as the statement states it in S5; the conflict is for Abbott at P3.
- 2.14 expands PSRB as 'professional, statutory or professional body'; the front matter has 'professional, statutory and regulatory bodies'. Recorded as PSRBs; the expansion in 2.14 looks like an issuer slip.
- Inferred subject codes: hecos 100637 musicianship and performance studies (for 'Music Performance', 1.10) and hecos 100643 music and arts management (for 'Music Business', 2.4 and 3.4). 'Sound Studies' (1.10) has no HECoS term; left uncoded. Acoustics (100427) sits in CAH07 physics though the statement names it within music (1.24).
- Inferred relations: overlaps with std:doc:qaa-dance-drama-and-performance-2024-benchmarks (musical theatre, performance); music-adjacent statements in 3.4 are unnamed.
- SB6 bodies and documents not yet ingested: JAMES, CDMT, HCPC requirements; Equality and Human Rights Commission guidance; Equality Act 2010; UN SDGs; National Plans for Music Education (England and Wales, 2022); the Quality Code (front matter only, excluded matter).
- Cross-cutting themes are five, all with their own sub-headings in section 1, including generative AI (1.37 to 1.41) and employability joined with enterprise. The front matter's list of key changes names them too (excluded matter).
- Section 5 (references) names the EDIMS report, ISM's Dignity at Work 2, the Keychange manifesto and the UK Parliament inquiry on misogyny in music: EDI sources, not cited by paragraph; not recorded in SB6.
- Pattern differences from Psychology: one two-column table per heading instead of lists per rung; no excellent rung; three headings (knowledge and understanding, technical skills, professional skills); a separate master's list; generative AI as a theme; four 'will' and 'should' provider paragraphs in sections 2 to 4.
- CQFW is not named in the text; Wales is named only for course length (2.10) and the Welsh national plan (2.15). No CQFW level recorded.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:00: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0121 (P1); built by tools/bm_build.py.
