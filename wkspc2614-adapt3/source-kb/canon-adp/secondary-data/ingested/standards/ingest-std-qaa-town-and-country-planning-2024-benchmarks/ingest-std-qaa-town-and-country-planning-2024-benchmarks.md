---
id: std:doc:qaa-town-and-country-planning-2024-benchmarks
title: "Subject Benchmark Statement Town and Country Planning"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100197", label: "planning", basis: "stated" }
  - { scheme: "hecos", code: "100199", label: "urban and regional planning", basis: "stated" }
  - { scheme: "cah", code: "CAH13-01-04", label: "planning (urban, rural and regional)", basis: "stated" }
  - { scheme: "hecos", code: "100593", label: "rural planning", basis: "inferred" }
edition: "April 2024 (fifth edition)"
published: 2024-04
status: current
supersedes: "the fourth edition, 2019 (D1, back matter)"
heldText: { method: sha256-bytes, raw: 893eac1731a05f2d243fb07f2028b42e794d3c3c776f5b1a68143faa5fe3cffe, normalised: 318a41db76e9f43a7fc379c5cbdee993c1f1bee8f2e30a74dcb8ea8a476bce11 }
heldTextStan: { method: sha256-stan, raw: 893eac1731a05f2d243fb07f2028b42e794d3c3c776f5b1a68143faa5fe3cffe, normalised: 4a116f1ec4df0a3de77b578722dcfe52f0abaadcd5ad9471c3e654d9403fb2ee }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, fifth edition of this statement (April 2024), with the cross-cutting themes"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0133 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:42"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Town and Country Planning (QAA, April 2024)

> Run 0133, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2024-town-country-planning-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in town and country planning (spatial, urban and regional, land-use, city, environmental or community planning) should know and be able to do at the end of an honours degree, with three standards (threshold, typical, excellent) and an added list for the integrated master's (MPlan). Reach for it when designing, reviewing or describing a planning course or its outcomes. It is not a curriculum, not the RTPI's accreditation requirements and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2024 as the fifth edition, the statement covers undergraduate and taught postgraduate planning courses, with standards for bachelor's degrees with honours (FHEQ level 6, FQHEIS level 10) and integrated master's degrees (FHEQ level 7, FQHEIS level 11). Its threshold list has 13 items, each tagged by the issuer with one or two of five themes (knowledge and understanding, cognitive, practical and transferable skills, professional competencies); the typical and excellent standards are two broad items each, building on the threshold, and the integrated master's adds four. It treats the four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability; enterprise and entrepreneurship), points to Annex D of the qualifications frameworks for the honours classes, names the RTPI as the body conferring Chartered Town Planner status, and sets out content in five thematic groupings rather than a prescribed list.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Town and Country Planning"
edition: "April 2024 (fifth edition)"
dates:
  published: 2024-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point and not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of the quality arrangements in Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2024", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a town and country planning graduate can be expected to know, do and understand at the end of an honours degree or an integrated master's, and the nature of planning courses (D1, front matter: About this Statement; 1.7; 1.19; 4.1; 4.10)"
appliesTo:
  awards: ["bachelor's degrees with honours, single, joint or combined (1.17, 2.3, 2.6)", "integrated master's degrees, MPlan (1.17, 2.7, 4.10)", "taught master's, including conversion courses: the statement informs them (1.7, 1.17, 1.19), but section 4's standards are set for the two awards above"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"The Statement addresses Town and Country Planning degree courses at both undergraduate and taught postgraduate levels, as well as helping to inform those designing other degree courses which have a substantial Planning content.\" (D1, 1.7)"
statedSubjects:
  - { name: "Town and Country Planning (Planning as shorthand)", locator: "(D1, 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100197", label: "planning" }, { scheme: "cah", code: "CAH13-01-04", label: "planning (urban, rural and regional)" }] }
  - { name: "Urban and Regional Planning", locator: "(D1, 1.1)", kind: "programme title", codes: [{ scheme: "hecos", code: "100199", label: "urban and regional planning" }] }
  - { name: "Spatial Planning; Land-Use Planning; City Planning; Environmental Planning; Community Planning", locator: "(D1, 1.1)", kind: "programme title", codes: [] }
  - { name: "Planning combined with Real Estate, Architecture, Design or Geography", locator: "(D1, 2.3)", kind: "programme title", codes: [] }
  - { name: "specialist master's in a particular area of planning", locator: "(D1, 1.17)", kind: "specialism", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Town and Country Planning", gloss: "the field and its many course names" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Town and Country Planning", gloss: "planning serves what societies value" }
  - { number: "1.3", order: 5, componentType: stem, parent: "section 1", heading: "Context and purposes of a Town and Country Planning", gloss: "issues planning is linked to (list)" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Town and Country Planning", gloss: "contested causes; contexts may change sharply" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Town and Country Planning", gloss: "an inter- and multi-disciplinary subject" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Town and Country Planning", gloss: "vocational aims; accreditation optional" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Town and Country Planning", gloss: "a broad reference, beyond accreditation outcomes" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Town and Country Planning", gloss: "international setting and devolved governance" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Town and Country Planning", gloss: "the four cross-cutting themes introduced" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Town and Country Planning degree", gloss: "creative proposals amid competing interests" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Town and Country Planning degree", gloss: "kinds of knowledge and the skills they build" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Town and Country Planning degree", gloss: "scholarship, practice and wider skills" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Town and Country Planning degree", gloss: "agile, curious planners for changing careers" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Town and Country Planning degree", gloss: "standards as a broad frame; harm and benefit" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Town and Country Planning degree", gloss: "planning as the study of managed change" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Town and Country Planning degree", gloss: "the academic core: why and how planning is done" }
  - { number: "1.17", order: 19, componentType: stem, parent: "section 1", heading: "Characteristics of a Town and Country Planning degree", gloss: "forms a degree course may take (list)" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Town and Country Planning degree", gloss: "one-year master's, placements, apprenticeships" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Town and Country Planning degree", gloss: "section 4 aimed at honours and integrated master's" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Town and Country Planning degree", gloss: "scholarship with practice; survey and data" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Town and Country Planning degree", gloss: "modes of study; fieldwork always included" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Town and Country Planning degree", gloss: "a frame for courses, not a method" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive curriculum and belonging" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "uneven growth and equitable places" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusion at different spatial scales" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive design and co-creation" }
  - { number: "1.27", order: 29, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "principles for embedding inclusivity (list)" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "diverse teaching methods and materials" }
  - { number: "1.29", order: 31, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive behaviours to foster (list)" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "inclusive design for every learner need" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "accessible environments and reasonable adjustments" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "accessible settings beyond the campus" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "varied methods; clear expectations" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "flexible recruitment; seeing oneself in the curriculum" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainability throughout; critical view of the SDGs" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainability in policy and regulation" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainability defined broadly, over time and scale" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "the four Ps" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "critical debate on what sustainability means" }
  - { number: "1.40", order: 42, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "tensions between the three pillars" }
  - { number: "1.41", order: 43, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "interdisciplinary learning for sustainability" }
  - { number: "1.42", order: 44, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "embedding the SDGs in modules" }
  - { number: "1.43", order: 45, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise education and careers" }
  - { number: "1.44", order: 46, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "entrepreneurship and the values of planning" }
  - { number: "1.45", order: 47, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "modules on development business and climate" }
  - { number: "1.46", order: 48, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise in existing modules; digital tools" }
  - { number: "1.47", order: 49, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "case studies, problem-based learning, real projects" }
  - { number: "2.1", order: 51, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "theory balanced with practice" }
  - { number: "2.2", order: 52, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "professional bodies shape course design" }
  - { number: "2.3", order: 53, componentType: stem, parent: "section 2", heading: "Design", gloss: "common features of structure (list)" }
  - { number: "2.4", order: 54, componentType: practice, parent: "section 2", heading: "Design", gloss: "distinctive course features (list)" }
  - { number: "2.5", order: 55, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression towards the honours threshold" }
  - { number: "2.6", order: 56, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined degrees" }
  - { number: "2.7", order: 57, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "the integrated master's (MPlan)" }
  - { number: "2.8", order: 58, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards and course length by nation" }
  - { number: "2.9", order: 59, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "specialising as students progress" }
  - { number: "2.10", order: 60, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "growing complexity, judgement and independence" }
  - { number: "2.11", order: 61, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "doctoral study and researcher networks" }
  - { number: "2.12", order: 62, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible structures and modes" }
  - { number: "2.13", order: 63, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "delivery modes and learning tools" }
  - { number: "2.14", order: 64, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "part-time, apprenticeship and sandwich routes" }
  - { number: "2.15", order: 65, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "accredited outcomes and room to specialise" }
  - { number: "2.16", order: 66, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership at many scales" }
  - { number: "2.17", order: 67, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnerships with practitioners and employers" }
  - { number: "2.18", order: 68, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "employer input from every sector" }
  - { number: "2.19", order: 69, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "community and campaign groups" }
  - { number: "2.20", order: 70, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "kinds of partner contribution; study visits" }
  - { number: "2.21", order: 71, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "study abroad partnerships" }
  - { number: "2.22", order: 72, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "placements of varying length" }
  - { number: "2.23", order: 73, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "degree apprenticeship partnerships" }
  - { number: "2.24", order: 74, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "ethics and fairness in partnerships" }
  - { number: "2.25", order: 75, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "networks and learned societies" }
  - { number: "2.26", order: 76, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring, review and the student voice" }
  - { number: "2.27", order: 77, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.28", order: 78, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners" }
  - { number: "2.29", order: 79, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "practitioners as external examiners" }
  - { number: "2.30", order: 80, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation review by the professional body" }
  - { number: "3.1", order: 82, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "the planner as broker, visionary and advocate" }
  - { number: "3.2", order: 83, componentType: practice, parent: "section 3", heading: "Content", gloss: "place-based learning; individual and group work" }
  - { number: "3.3", order: 84, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "thematic groupings, not a fixed list; the SDGs" }
  - { number: "3.4", order: 85, componentType: area, parent: "section 3", heading: "Content", gloss: "five themes of content (list)" }
  - { number: "3.5", order: 86, componentType: area, parent: "section 3", heading: "Content", gloss: "causes and processes of environmental change" }
  - { number: "3.6", order: 87, componentType: area, parent: "section 3", heading: "Content", gloss: "the practice of planning" }
  - { number: "3.7", order: 88, componentType: area, parent: "section 3", heading: "Content", gloss: "debates in planning" }
  - { number: "3.8", order: 89, componentType: area, parent: "section 3", heading: "Content", gloss: "key planning skills" }
  - { number: "3.9", order: 90, componentType: area, parent: "section 3", heading: "Content", gloss: "specialist skills and knowledge" }
  - { number: "3.10", order: 91, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "teaching informed by research and practice" }
  - { number: "3.11", order: 92, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "education strategies; lifelong learning" }
  - { number: "3.12", order: 93, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "strategies designed with practitioners" }
  - { number: "3.13", order: 94, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "what teaching covers; practitioner input" }
  - { number: "3.14", order: 95, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "learning defined; varied approaches" }
  - { number: "3.15", order: 96, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "learning with stakeholders" }
  - { number: "3.16", order: 97, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "research skills and the student-led project" }
  - { number: "3.17", order: 98, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "authentic assessment" }
  - { number: "3.18", order: 99, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "range of assessment types (list)" }
  - { number: "4.1", order: 101, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the three standards introduced" }
  - { number: "4.2", order: 102, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed threshold; Annex D" }
  - { number: "4.3", order: 103, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "standards apply to all of section 3" }
  - { number: "4.4", order: 104, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the standards students are expected to reach" }
  - { number: "4.5", order: 105, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "the three standards defined" }
  - { number: "4.6", order: 106, componentType: stem, parent: "section 4", heading: "Threshold level", gloss: "threshold: five core themes" }
  - { number: "4.7", order: 107, componentType: stem, parent: "section 4", heading: "Threshold level", gloss: "threshold standards (list)" }
  - { number: "4.8", order: 108, componentType: stem, parent: "section 4", heading: "Typical level", gloss: "typical standard" }
  - { number: "4.9", order: 109, componentType: stem, parent: "section 4", heading: "Excellent level", gloss: "excellent standard" }
  - { number: "4.10", order: 110, componentType: stem, parent: "section 4", heading: "Integrated master's degrees", gloss: "integrated master's standards" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Town and Country Planning degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of the Town and Country Planning degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2, S7 and SB6" }
  - { number: "none", heading: "section heading lines (1 to 4)", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for SB6 and Part E" }
  - { number: "6", heading: "Membership of the Advisory Group (2024, 2019, 2016, 2008, 2002); employer representation; copyright", kind: "other: back matter, read for S8 and supersedes" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 44 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/town-and-country-planning-2024/1.8
  locator: { number: "1.8", headingPath: ["Context and purposes of a Town and Country Planning degree", ""] }
  span: { start: 15773, end: 16432 }
  source: "1.8 Planning education in the UK increasingly takes place in an internationalised context, with growing awareness of the varied contexts for Planning practice and varied origins of Planning knowledge, as well as increasing numbers of international students on Planning programmes. The Planning movement has a long history of policy mobility and a desire to learn from elsewhere while critically understanding specific contexts for application. Elements of Planning education will reflect global, national and devolved governance structures and courses should take account of differences in governance, law, policy and practice as appropriate for their focus.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "planning courses"
  addressee: provider
  verbs: ["reflect", "take"]
  about: "governance differences across nations and abroad"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Planning education reflects global, national and devolved systems of government, and courses should allow for how law, policy, governance and practice differ, to suit their focus, in an increasingly international setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of a Town and Country Planning degree", "Purposes and characteristics of a Town and Country Planning degree"] }
  span: { start: 16849, end: 17524 }
  source: "1.10 Town and Country Planning generates creative proposals for change, by means of analysis, public participation and cooperative working within a complex web of competing interests. Positive action is at the heart of Planning, and it operates within a wide context of environmental, political, social, economic, legal and governance constraints and power dynamics. A Planning degree should seek to develop students’ knowledge and critical understanding of these contexts, giving consideration to changing social, economic, environmental, legal, cultural, political, policy, administrative and ethical frameworks for Planning in a local, national and international context.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "planning degrees"
  addressee: both
  verbs: ["seek", "develop"]
  about: "critical understanding of the contexts of planning"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "A planning degree should aim to build students' knowledge and critical grasp of the environmental, political, social, economic, legal and governance settings in which planning works, and of how its frameworks change at local, national and international scales."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of a Town and Country Planning degree", "Purposes and characteristics of a Town and Country Planning degree"] }
  span: { start: 18543, end: 19584 }
  source: "1.12 Town and Country Planning degrees provide students with opportunities to engage with academic research and critical scholarship, as well as vocational and professional development. This includes seeking to develop planners who understand the communities that Planning serves and are able to act as creative problem-solvers, developing appropriate responses to spatial, development and design challenges and opportunities. Planning should be understood in relation to its consequences for diverse publics, including those relating to people’s health and well-being, the quality of their environment, inequalities, and the vitality of local economies. Town and Country Planning degrees will also develop broader skills, including negotiation, leadership, teamworking, communication, a capacity for independent research and critical reflection. An emphasis should be placed on allowing students to become reflective and reflexive practitioners, able to understand and act within the ethical contexts and imperatives for Planning practice.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "planning degrees"
  addressee: both
  verbs: ["develop", "placed", "allowing"]
  about: "wider skills and reflective, reflexive practice"
  themes: [none]
  domain: generic-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Planning degrees offer research and scholarship alongside professional growth and will build wider skills, among them negotiation, leadership, teamwork, communication, independent research and critical reflection; they should stress students becoming reflective and reflexive practitioners who grasp and act on the ethical demands of planning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/1.20
  locator: { number: "1.20", headingPath: ["Context and purposes of a Town and Country Planning degree", "Characteristics of a Town and Country Planning degree"] }
  span: { start: 23305, end: 24147 }
  source: "1.20 The mix between different types of knowledge and paradigms will vary between courses, and a diversity of approaches to knowing and understanding places and processes in the environment is to be encouraged. Planning courses should ordinarily involve a mix of scholarship and practical application of knowledge and skills. Planning has long been understood to involve survey – the collection of data – and the analysis of data before plan- making and decision-making processes. Planning courses should consider a variety of sources and approaches to data analysis, including the use of technologies utilised with appropriate methodological rigour and in an ethical framework. In general, a student would normally develop core Planning knowledge and skills before focusing on a more specialist area of Planning subject matter and practice.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "planning courses"
  addressee: provider
  verbs: ["involve", "consider", "develop"]
  about: "scholarship with practice; survey and data analysis"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should normally combine scholarship with putting knowledge and skills to practical use, and should consider varied data sources and methods of analysis, with technology used rigorously and ethically, since planning rests on survey and analysis before plans and decisions; core learning usually comes before specialism."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/1.21
  locator: { number: "1.21", headingPath: ["Context and purposes of a Town and Country Planning degree", "Characteristics of a Town and Country Planning degree"] }
  span: { start: 24147, end: 24772 }
  source: "1.21 Town and Country Planning courses may be delivered full or part-time and will involve varying mixes of in-person and remote (distance) learning. Flexibility to meet the diverse needs of Planning students is encouraged. However courses are delivered, students should\n\n7\nbe offered opportunities to develop the interpersonal skills required for meaningful cross- professional teamwork, and be exposed to real-world places in all their richness and complexity. Given the real-world focus of Planning as a discipline, fieldwork, site and study visits and experiential learning should always form part of Planning education.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "planning courses in every mode"
  addressee: provider
  verbs: ["offered", "develop", "exposed", "form"]
  about: "interpersonal skills, real places and fieldwork"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Whatever the mode, full or part-time, in person or at a distance, students should get chances to build the interpersonal skills for work across professions and should meet real places in their full complexity; fieldwork, visits to sites and experiential learning should always feature in planning education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of a Town and Country Planning degree", "Equality, diversity and inclusion"] }
  span: { start: 25319, end: 26293 }
  source: "1.23 Given that Town and Country Planning graduates will be practising Planning in societies with diverse populations, it is essential that courses are underpinned by an inclusive curriculum where students are attentive to the challenges and opportunities of creating equitable places. The term ‘inclusivity’ is intended to mean an approach that embeds a barrier-free educational environment, with which underrepresented groups can fully engage. An inclusive curriculum therefore not only integrates employability to support career opportunities for diverse student groups, but also permits the development of a learning community both during and after studies. Through the latter, students will be challenged to think about ways to promote a greater sense of belonging for underrepresented groups. When underrepresented groups feel included, there is a greater sense of belonging within the wider cohort, not only in an educational setting but also later in the workplace.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "it is essential" read as must
  level: none
  appliesTo: "planning courses and their students"
  addressee: both
  verbs: ["underpinned", "challenged", "promote"]
  about: "an inclusive curriculum and belonging"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Because graduates will practise in diverse societies, a barrier-free, inclusive curriculum is called essential, one that links employability to the careers of diverse groups and builds a learning community; students will be challenged to consider how to strengthen belonging for underrepresented groups."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/1.25
  locator: { number: "1.25", headingPath: ["Context and purposes of a Town and Country Planning degree", "Equality, diversity and inclusion"] }
  span: { start: 26709, end: 27330 }
  source: "1.25 Consideration of knowledge gained by students through an inclusivity lens therefore needs to be undertaken at various spatial scales. This might be in the form of questions that will be specific to a site or neighbourhood but that have equitable implications for the wider community. In other instances, students will need to draw on knowledge that is specific to certain groups in society; for example how to tackle barriers to accessing green spaces, especially for underrepresented groups (including those with health conditions, those of lower socio-economic status, and those from minority ethnic backgrounds).\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["draw"]
  about: "knowledge of particular groups at every scale"
  themes: [theme:edi]
  domain: knowledge
  award: ["none"]
  gradeOf: none
  paraphrase: "Students apply an inclusion lens at several spatial scales, from a site to the wider community, and will need to use knowledge particular to certain groups, such as how to remove barriers that keep underrepresented people from green space."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/1.30
  locator: { number: "1.30", headingPath: ["Context and purposes of a Town and Country Planning degree", "Accessibility"] }
  span: { start: 29575, end: 30118 }
  source: "1.30 Town and Country Planning courses should be designed to be inclusive, recognising a full range of learner needs to ensure equitable access to learning. This requires recognition that what access looks like will vary for different groups and individual learners. Care should be taken to consider how all areas of programme design (learning environments, course materials, assessment methods and wider support structures) may affect learners in respect of protected characteristics (including neurodiversity) and socio-economic background.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course design"
  addressee: provider
  verbs: ["designed", "recognising", "taken", "consider"]
  about: "inclusive design for the full range of learner needs"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should be designed inclusively for the whole range of learner needs, recognising that access differs between groups and people, and care should be taken over how environments, materials, assessment and support affect learners with protected characteristics, neurodivergent learners among them, and from different socio-economic backgrounds."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/1.31
  locator: { number: "1.31", headingPath: ["Context and purposes of a Town and Country Planning degree", "Accessibility"] }
  span: { start: 30118, end: 30698 }
  source: "1.31 All learning environments and course materials should be accessible to learners with particular mobility and learning needs, or those with lived experience of disadvantage – including structural inequalities that impact on access to learning opportunities. Where appropriate, following national and institutional guidelines, students should benefit from reasonable adjustments that reflect particular assessed needs. Programmes should also seek to ensure that all students have access to the facilities and resources they require to learn effectively both on and off campus.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "learning environments and programmes"
  addressee: both
  verbs: ["benefit", "seek", "ensure"]
  about: "accessible environments, adjustments and resources"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Every learning environment and set of materials should be open to learners with mobility or learning needs or with lived experience of disadvantage; students should receive reasonable adjustments for assessed needs, following national and institutional guidance, and programmes should try to give all students the facilities and resources to learn on and off campus."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/1.32
  locator: { number: "1.32", headingPath: ["Context and purposes of a Town and Country Planning degree", "Accessibility"] }
  span: { start: 30698, end: 31152 }
  source: "1.32 Town and Country Planning courses are taught across a variety of learning environments, including campus teaching spaces, site visits, field trips and placements. They can include group project work, live projects and blended and digital learning technologies. Particular care should be taken to ensure that these environments are inclusive and fully accessible to all students, considering a full range of physical, social and financial issues.\n\n9\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "all settings of planning teaching"
  addressee: provider
  verbs: ["taken", "ensure"]
  about: "accessible settings beyond the classroom"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Planning is taught in many settings, from campus rooms to site visits, field trips, placements, group and live projects and digital learning, and particular care should be taken that each is inclusive and fully accessible, physically, socially and financially."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/1.34
  locator: { number: "1.34", headingPath: ["Context and purposes of a Town and Country Planning degree", "Accessibility"] }
  span: { start: 31626, end: 32277 }
  source: "1.34 Recruitment to Town and Country Planning courses, including degree apprenticeship routes where appropriate, should be sufficiently flexible to enable learners with non-standard academic backgrounds or from groups underrepresented in higher education to flourish. In keeping with wider goals of diversifying professional practice in the built environment, course content should be designed to ensure that all members of the learning community can see themselves in the curriculum, have opportunities to learn about and from the diverse experiences of others, and are supported to explore the range of future career opportunities available to them."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "recruitment and course content"
  addressee: provider
  verbs: ["enable", "designed", "ensure", "explore"]
  about: "flexible recruitment and a curriculum students see themselves in"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Recruitment, apprenticeship routes included, should be flexible enough for learners from non-standard backgrounds or underrepresented groups to thrive, and content should be designed so that everyone recognises themselves in it, learns from others' varied experiences and is helped to explore future careers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/1.35
  locator: { number: "1.35", headingPath: ["Context and purposes of a Town and Country Planning degree", "Sustainability"] }
  span: { start: 32293, end: 32656 }
  source: "1.35 Issues of sustainability underpin, and are woven throughout, the pedagogy and content of Planning education. In a similar vein, higher education providers delivering Planning degrees should engage with and promote critical thinking regarding the UN Sustainable Development Goals (SDGs) (see also section 3), other frameworks and sustainability more broadly.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers delivering planning degrees"
  addressee: provider
  verbs: ["underpin", "engage", "promote"]
  about: "sustainability and critical thinking on the SDGs"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Sustainability runs through the teaching and content of planning education, and those delivering planning degrees should engage with, and encourage critical thinking about, the UN SDGs, other frameworks and sustainability in general."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/1.42
  locator: { number: "1.42", headingPath: ["Context and purposes of a Town and Country Planning degree", "Sustainability"] }
  span: { start: 35079, end: 35468 }
  source: "1.42 Planning courses should consider how to embed approaches to teaching and learning that are linked to the UN SDGs across modules, working towards the SDGs and associated frameworks, including the QAA and Advance HE’s Education for Sustainable Development Guidance. Case studies, practical examples, live projects and placements can be used to embed sustainability practice in learning."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "planning courses"
  addressee: provider
  verbs: ["consider", "embed", "linked", "used"]
  about: "embedding the SDGs across modules"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should consider how to build teaching and learning tied to the UN SDGs into modules, working towards the goals and related frameworks such as the joint ESD guidance, with live projects, placements, case studies and practical examples as means."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of the Town and Country Planning degree", "Progression"] }
  span: { start: 44744, end: 45181 }
  source: "2.6 Undergraduates studying Town and Country Planning courses as part of a combined or joint degree with other subjects will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the topics covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study.\n\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of joint or combined degrees"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "joint and combined honours"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students on joint or combined degrees will gain the core subject-specific and generic skills set out in the statement and add others from their second subject, and may explore where the disciplines meet."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of the Town and Country Planning degree", "Progression"] }
  span: { start: 46539, end: 47912 }
  source: "2.10 As students progress through their course, their knowledge and expertise in understanding places, drawing on different methods of information gathering, moves through increased levels of complexity/critical thinking and greater acknowledgement of roles/influences of various stakeholders. They will also demonstrate a greater appreciation of the sophistication needed for making ‘situated and evidenced judgements’ on matters that are both ‘spatial’ (such as relating to a site, neighbourhood, urban/rural communities) and ‘non-spatial’ (for example on topics such as young people and climate change, ageing-in- place, the role of AI in future practice, interdisciplinary/professional working, and reflective practice). As they progress, students develop a greater depth of knowledge and gain an understanding of the vital contribution made by research in their subject. Students will demonstrate an increasing ability to undertake fieldwork or projects independently, using primary and/or secondary data. They will also need to be able to acknowledge that the theory and practice of Planning are not separate, but rather a continuum that commences by inquiring about the possibilities of improving a place, that pauses in order to reflect on the interventions made so far, and that then recommences by raising new questions on how best to improve the place further.\n\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students progressing through the degree"
  addressee: learner
  verbs: ["demonstrate", "acknowledge"]
  about: "progression in judgement, independence and theory with practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As they progress, students' understanding of places grows more complex and critical and takes more account of stakeholders; they will show a growing grasp of the subtlety needed for situated, evidenced judgements on spatial and non-spatial questions, increasing independence in fieldwork and projects and an understanding that planning theory and practice form one continuing cycle of inquiry, reflection and improvement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/2.27
  locator: { number: "2.27", headingPath: ["Distinctive features of the Town and Country Planning degree", "Monitoring and review"] }
  span: { start: 55959, end: 56255 }
  source: "2.27 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "providers in periodic review"
  addressee: provider
  verbs: ["use", "ensure", "achieved"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Externality is central to UK quality assurance: providers will bring in external reviewers during periodic review for an outside view on proposed changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/3.12
  locator: { number: "3.12", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 66987, end: 67480 }
  source: "3.12 To emphasise the essential interaction of theory with practice, these strategies should be designed through the collaboration of Planning academics and practitioners, combining the application of theoretical concepts with the processes of real-life scenarios to create a student-centred, inclusive pedagogy. Sustainability in its broadest sense underpins all pedagogic considerations, being fundamental to the study and practice of Town and Country Planning as a place-making profession.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "learning, teaching and assessment strategies"
  addressee: provider
  verbs: ["designed", "combining", "underpins"]
  about: "teaching designed with practitioners"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "To bring theory and practice together, teaching and learning strategies should be designed jointly by planning academics and practitioners, joining theoretical ideas to real-life processes in an inclusive pedagogy centred on the student, with sustainability underpinning every pedagogic choice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/3.13
  locator: { number: "3.13", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 67480, end: 67800 }
  source: "3.13 Teaching includes curriculum design, the selection and delivery of content, the method and type of assessment, moderation and reflection. This process, especially the delivery of content, should encourage the active involvement of professional practitioners, thereby enabling real-world challenges to be addressed.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "teaching"
  addressee: provider
  verbs: ["encourage", "enabling"]
  about: "practitioner involvement in teaching"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching spans curriculum design, content, assessment, moderation and reflection, and the process, above all the delivery of content, should draw professional practitioners in actively so that real-world problems are tackled."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/3.14
  locator: { number: "3.14", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 67800, end: 68145 }
  source: "3.14 Learning is the process of change in the individual brought about by the acquisition of information, understanding, skills, attitude and behaviour. Consequently, a variety of pedagogical approaches are to be used to accommodate the diversity of student learning styles and the evolving modes of hybrid, analogue and digital engagement.\n\n22\n"
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "teaching approaches"
  addressee: provider
  verbs: ["used", "accommodate"]
  about: "varied pedagogies for diverse learners"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Learning is change in a person through new information, understanding, skills, attitudes and behaviour, so varied teaching approaches are called for, suited to different learning styles and to hybrid, analogue and digital modes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 68145, end: 68777 }
  source: "3.15 Learning opportunities should actively involve interaction with a range of stakeholders and have the potential to include students co-creating with academics and/or practitioners, interdisciplinary collaboration, work-based environments, scenario-based projects, real-life simulations, situations for problem identification and resolution, and community participation. These opportunities would allow for both individual student study and group work to be undertaken. A strong combination of these would help broaden understanding of social, attitudinal and physical barriers, and should be encouraged within Planning courses.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "learning opportunities"
  addressee: provider
  verbs: ["involve", "encouraged"]
  about: "learning with stakeholders"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Learning opportunities should involve students actively with a range of stakeholders and may take in co-creation with academics or practitioners, interdisciplinary work, workplaces, scenario projects, simulations, problem-solving and community participation, alone and in groups; such a mix, which widens understanding of social, attitudinal and physical barriers, should be encouraged."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/3.16
  locator: { number: "3.16", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 68777, end: 69595 }
  source: "3.16 Research skills are an important part of the educational journey across a programme of study. They are also important for Planning practice, given the need to understand the built and natural environments and their socio-economic contexts before considering any interventions. Students can develop their investigative skills to demonstrate independence through a student-led research or design project. They are challenged to think in critical, creative and applied ways and may devise research questions, design and conduct a research methodology, and potentially produce original knowledge which will be important to the discipline. As well as conducting their own project, students will communicate their research to academic and/or professional communities using professional communication skills and methods."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["communicate", "develop", "devise", "design", "conduct"]
  about: "research skills and communicating research"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Research skills matter throughout the course and in practice, since places and their contexts need understanding before any intervention; through a research or design project they lead, students show independence and may frame questions and design a method; they will present their research to academic or professional audiences in a professional manner."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 72657, end: 73142 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["refer", "perform"]
  about: "evidence of achievement and Annex D"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do considerably better than the minimum threshold; each provider decides what counts as evidence of achievement and should refer to Annex D of the qualifications frameworks, which describes the four honours classifications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.4
  locator: { number: "4.4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 73621, end: 73823 }
  source: "4.4 These are the standards that it is expected students will achieve in a Town and Country Planning degree, and students should demonstrate an understanding and ability to apply these, as appropriate.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["achieve", "demonstrate", "apply"]
  about: "the standards students are expected to reach"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students are expected to reach these standards in a planning degree and should show that they understand them and can apply them as fits their work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 74768, end: 74910 }
  source: "an appreciation of the interconnected nature of Planning interventions and the bearing these have upon the built and natural environments (KU)"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold standard"
  addressee: learner
  verbs: []
  about: "interlinked interventions and environments"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates understand how planning interventions connect with one another and how they act on built and natural environments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 74917, end: 75005 }
  source: "an ability to identify and resolve problems through Planning tools and processes (CS/PS)"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold standard"
  addressee: learner
  verbs: ["identify", "resolve"]
  about: "solving problems with planning tools and processes"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates can find and settle problems using the tools and processes of planning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 75008, end: 75169 }
  source: "theories of Planning, its role in society, the underpinning arguments for the activity of Planning, and how best to relate theories to Planning practices (KU/CS)"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold standard"
  addressee: learner
  verbs: ["relate"]
  about: "planning theory and its link to practice"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates know the theories of planning and the case made for its role in society, and how best to link theory to practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 75172, end: 75390 }
  source: "the political, economic, social, legal and institutional contexts in which Planning is carried out, the relative powers of actors involved, and the respective means by which planners might act within such contexts (KU)"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold standard"
  addressee: learner
  verbs: ["act"]
  about: "the contexts and actors of planning"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates know the legal, political, economic, social and institutional settings of planning, the relative power of those involved and how planners can act within them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 75393, end: 75547 }
  source: "policy, its role in framing action at different scales, the processes by which Planning policy is made, and the potential of policy to shape outcomes (KU)"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold standard"
  addressee: learner
  verbs: ["framing", "made", "shape"]
  about: "policy and how it is made"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates know what policy is, how it frames action at different scales, how planning policy comes about and how far it can shape outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.7.b6
  locator: { number: "4.7.b6", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 75550, end: 75720 }
  source: "the role of Planning in making sustainable and inclusive places, the contribution of design and finance to this process, and the need to consider different groups (KU/PS)"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold standard"
  addressee: learner
  verbs: ["making", "consider"]
  about: "sustainable, inclusive places; design and finance"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates understand planning's part in creating sustainable and inclusive places, what design and finance add to that and why the needs of different groups count."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.7.b7
  locator: { number: "4.7.b7", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 75723, end: 75878 }
  source: "the relationship between Planning and communities, the impact of Planning on people and places, and how best to work with diverse groups in society (KU/PS)"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold standard"
  addressee: learner
  verbs: ["work"]
  about: "planning, communities and diverse groups"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates understand how planning relates to communities and affects people and places, and how to work well with varied groups."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.7.b8
  locator: { number: "4.7.b8", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 75881, end: 76035 }
  source: "the potential of Town and Country Planning to tackle the climate and biodiversity crises, such as the role of infrastructure in meeting climate goals (KU)"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold standard"
  addressee: learner
  verbs: ["tackle", "meeting"]
  about: "planning, climate and biodiversity"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates know how planning can address the climate and biodiversity crises, for instance through infrastructure that helps reach climate goals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.7.b9
  locator: { number: "4.7.b9", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 76038, end: 76167 }
  source: "the use of technology in Planning, including an appreciation of the digital environments in which Planning is carried out (PS/TS)"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold standard"
  addressee: learner
  verbs: ["carried"]
  about: "technology and digital settings in planning"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates can use technology in planning and appreciate the digital settings in which planning now takes place."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.7.b10
  locator: { number: "4.7.b10", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 76170, end: 76313 }
  source: "the significance of values and ethics to the practice of Planning and an understanding of the role of the profession in upholding these (CS/PC)"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold standard"
  addressee: learner
  verbs: ["upholding"]
  about: "values, ethics and the profession"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates understand why values and ethics matter to planning practice and the profession's part in upholding them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.7.b11
  locator: { number: "4.7.b11", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 76316, end: 76475 }
  source: "the relationship of Planning to other professional and disciplinary fields, including the importance of working effectively across disciplinary boundaries (PC)"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold standard"
  addressee: learner
  verbs: ["working"]
  about: "working across disciplines and professions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates understand how planning relates to other professions and disciplines and why working well across their boundaries matters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.7.b12
  locator: { number: "4.7.b12", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 76478, end: 76665 }
  source: "the importance of research to effective Planning, including the use of evidence drawing on a range of information sources, and the evaluation of alternative policies and arguments (CS/PS)"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold standard"
  addressee: learner
  verbs: ["drawing"]
  about: "research, evidence and weighing alternatives"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates understand why research matters to good planning, use evidence from varied sources and judge alternative policies and arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.7.b13
  locator: { number: "4.7.b13", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 76668, end: 76769 }
  source: "the ability to effectively communicate through written, graphic, numerical and digital means (PS/TS)."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold standard"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating in written, graphic, numerical and digital forms"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates communicate well in writing, graphics, numbers and digital media."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 76928, end: 77065 }
  source: "development beyond the minimum threshold of knowledge and understanding, cognitive skills, practical skills and professional competencies"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical standard"
  addressee: learner
  verbs: []
  about: "going beyond the threshold across the core themes"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the typical standard, graduates meet every threshold criterion and will also go further than the minimum in what they know and understand, in thinking and practical skills and in professional competence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 77068, end: 77202 }
  source: "some critical discernment, insight, initiative, creativity and autonomy through effective and appropriate application of the criteria."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical standard"
  addressee: learner
  verbs: []
  about: "some critical judgement, initiative, creativity and autonomy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the typical standard, graduates will also show some critical judgement, insight, initiative, creativity and independence in applying the criteria well and fittingly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.9.b1
  locator: { number: "4.9.b1", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 77336, end: 77568 }
  source: "an understanding and application of all criteria listed, with additional development beyond the typical threshold of knowledge and understanding, cognitive skills, practical skills and professional competencies to an excellent level"
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent standard"
  addressee: learner
  verbs: ["listed"]
  about: "excellence across all criteria"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/town-and-country-planning-2024/4.8.b1, basis: inferred }
  paraphrase: "At the excellent standard, graduates, having met the threshold and typical standards, understand and apply every criterion and will have taken their knowledge, thinking, practical skills and professional competence further than the typical level, to an excellent degree."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.9.b2
  locator: { number: "4.9.b2", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 77571, end: 77702 }
  source: "through effective, fluent, sophisticated application, an excellent level of critical discernment, insight, creativity and autonomy."
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent standard"
  addressee: learner
  verbs: []
  about: "excellent critical judgement, insight, creativity and autonomy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/town-and-country-planning-2024/4.8.b2, basis: inferred }
  paraphrase: "At the excellent standard, graduates apply the criteria fluently and with sophistication and will show excellent critical judgement, insight, creativity and independence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.10.b1
  locator: { number: "4.10.b1", headingPath: ["Benchmark standards", "Integrated master's degrees"] }
  span: { start: 78169, end: 78254 }
  source: "in-depth knowledge in one or more specialised areas of Planning activity and practice"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "graduates of integrated master's degrees"
  addressee: learner
  verbs: []
  about: "in-depth specialist knowledge"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Integrated master's graduates will, beyond the typical bachelor's standard, show deep knowledge of at least one specialist field of planning activity and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.10.b2
  locator: { number: "4.10.b2", headingPath: ["Benchmark standards", "Integrated master's degrees"] }
  span: { start: 78257, end: 78359 }
  source: "a good awareness and understanding of professional working, roles, responsibilities, ethics and values"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "graduates of integrated master's degrees"
  addressee: learner
  verbs: []
  about: "professional working, roles, ethics and values"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Integrated master's graduates will show a good grasp of how professionals work and the roles and responsibilities they hold, along with professional ethics and values."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.10.b3
  locator: { number: "4.10.b3", headingPath: ["Benchmark standards", "Integrated master's degrees"] }
  span: { start: 78362, end: 78446 }
  source: "a high degree of professionalism in undertaking assignments and/or working in groups"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "graduates of integrated master's degrees"
  addressee: learner
  verbs: ["undertaking", "working"]
  about: "professionalism in assignments and group work"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Integrated master's graduates will show a high level of professionalism in carrying out assignments and in group work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/town-and-country-planning-2024/4.10.b4
  locator: { number: "4.10.b4", headingPath: ["Benchmark standards", "Integrated master's degrees"] }
  span: { start: 78449, end: 78567 }
  source: "the effective use of data collection and analysis, and an ability to conduct independent research in Planning studies."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "graduates of integrated master's degrees"
  addressee: learner
  verbs: ["conduct"]
  about: "data and independent research"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Integrated master's graduates will use data collection and analysis effectively and be able to carry out independent research in planning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/town-and-country-planning-2024/1.8
  forPractitioner: { text: "Courses should take account of how the UK nations and other countries differ in law, policy, governance and practice, as fits the course's focus, and reflect structures at global, national and devolved scales.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) on how a course handles differences between the UK nations and other countries, not as a learning outcome. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 1.8). Do not present it as a regulatory requirement or as tied to one award or level. Set it beside qaa/town-and-country-planning-2024/4.7.b4 on the contexts of planning and qaa/town-and-country-planning-2024/4.7.b5 on policy at different scales."
  author-agent-dialogue: "Raise it with a programme team when a course recruits from several jurisdictions or teaches one nation's system alone. Put it in practitioner terms: the course should say which systems it covers and how it treats the rest. Ask which jurisdictions the core modules assume, and where students meet the differences. Avoid putting it to a student as something they must do."
- statement: qaa/town-and-country-planning-2024/1.10
  forPractitioner: { text: "The course should set out to develop students' knowledge and critical understanding of the changing settings of planning, from law, policy and administration to ethics, culture and power, at every scale from local to international.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you build knowledge and a critical understanding of the political, social, economic, legal, environmental and ethical settings that planning works in, from local to international.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) of what a planning degree sets out to develop, framed as the course's aim rather than a measured outcome. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 1.10). Do not present it as a threshold standard or as a regulatory requirement. Set it beside qaa/town-and-country-planning-2024/4.7.b4, the threshold item on the contexts of planning, and qaa/fheq-2024/4.15.b1 for the honours level of understanding."
  author-agent-dialogue: "Raise it when a student asks why the course spends time on law, politics or economics, or when a team reviews how context is taught. With a student, say plainly that the course should help them understand the settings planning works in; with staff, frame it as a design aim. Ask which setting, legal, political or economic, the person finds hardest to read in a real case. Avoid reading the paragraph aloud or treating it as a test the student must pass."
- statement: qaa/town-and-country-planning-2024/1.12
  forPractitioner: { text: "Courses will develop negotiation, leadership, teamwork, communication, independent research and critical reflection, and should give weight to students growing into reflective and reflexive practitioners alert to the ethics of planning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course will help you build skills in negotiating, leading, working in teams, communicating, researching on your own and reflecting critically, and it should help you become a practitioner who questions your own part in planning and its ethics.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (will, then should) of the wider skills and reflective practice a planning degree builds, not as one of the rung standards. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 1.12). Do not present it as a regulatory requirement or as a list a module must cover in full. Set it beside qaa/town-and-country-planning-2024/4.7.b10 and qaa/town-and-country-planning-2024/4.7.b11, and beside qaa/fheq-2024/annex-d/transferable/r5/3rd for reflection at honours level."
  author-agent-dialogue: "Raise it when a student is preparing a reflective account or a team plans skills development across the years. With a student, talk about negotiating, leading, teamwork and reflection in their own experience; with staff, frame it as what the course should foster. Ask when the person last changed their mind about their own role in a planning decision, and why. Avoid presenting the whole list as a checklist every student must already meet."
- statement: qaa/town-and-country-planning-2024/1.20
  forPractitioner: { text: "Courses should combine scholarship with practical application, and should teach survey and data analysis from varied sources, using technology with sound method and ethics; core knowledge and skills normally come before a specialism.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) about the balance of scholarship and practice and the teaching of data analysis. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 1.20). Do not present it as a learning outcome or as fixing a particular order of modules. Set it beside qaa/town-and-country-planning-2024/4.7.b12 on research and evidence and qaa/town-and-country-planning-2024/3.16 on research skills."
  author-agent-dialogue: "Raise it with a programme team reviewing the balance of theory and practice or how survey and data methods are taught. Put it in practitioner terms: what mix of scholarship and application the course offers, and where data analysis is learned. Ask where students first collect and analyse their own data, and how its ethics are taught. Avoid giving it to a student as a duty of theirs."
- statement: qaa/town-and-country-planning-2024/1.21
  forPractitioner: { text: "However the course is delivered, it should give students chances to develop interpersonal skills for cross-professional teamwork and to encounter real places, and fieldwork, visits and experiential learning should always be included.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) that every planning course, in any mode, includes fieldwork, visits and experiential learning and builds interpersonal skills. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 1.21). Do not present it as a regulatory requirement or as excusing distance courses from fieldwork. Set it beside qaa/town-and-country-planning-2024/2.4 on distinctive features and qaa/town-and-country-planning-2024/4.7.b11 on working across disciplines."
  author-agent-dialogue: "Raise it when a team plans a distance or part-time route, or when fieldwork is under budget pressure. Put it in practitioner terms: the course should always offer fieldwork and real places, whatever the mode. Ask how a student on the most remote route meets real places and works with other professions. Avoid giving it to a student as something they must arrange."
- statement: qaa/town-and-country-planning-2024/1.23
  forPractitioner: { text: "The text calls an inclusive curriculum essential: remove barriers so underrepresented groups can take full part, link employability to diverse students' careers and build a learning community in which students will be challenged to think about belonging.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will be asked to think about how places and professions can help people from underrepresented groups feel they belong, and to learn in a community that welcomes everyone.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as the statement's case for an inclusive curriculum; its word is 'essential', outside the usual modal words, so record it as described and do not turn it into a must. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 1.23). Do not present it as a regulatory or legal duty. Set it beside qaa/town-and-country-planning-2024/1.25, qaa/town-and-country-planning-2024/4.7.b7 on working with diverse groups and the theme record theme:edi."
  author-agent-dialogue: "Raise it when a team reviews inclusion in the curriculum or a student asks how the course treats diversity. With a student, talk about belonging and about the communities they will plan for; with staff, frame it as a curriculum principle. Ask whose experience is missing from the case studies the course uses. Avoid reading the paragraph aloud or telling a student the course is failing them."
- statement: qaa/town-and-country-planning-2024/1.25
  forPractitioner: { text: "Students will need to consider inclusion at different scales and draw on knowledge about particular groups, for example the barriers that people on low incomes, with health conditions or from minority ethnic backgrounds face in reaching green space.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will need to think about inclusion at every scale, from one site to a whole community, and use what is known about particular groups, such as what stops some people using green spaces.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation (will) that students apply knowledge of particular groups when judging inclusion at different scales. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 1.25). Do not present it as a threshold standard or as naming every group a course must cover. Set it beside qaa/town-and-country-planning-2024/4.7.b7 and qaa/town-and-country-planning-2024/4.7.b6, and beside qaa/fheq-2024/annex-d/knowledge/r1/3rd for knowledge at honours level."
  author-agent-dialogue: "Raise it when a student is assessing a site or neighbourhood proposal. Put it in plain words and the second person: who might be shut out of this place, and what do you know about why. Ask which groups a proposal the student is working on would serve least well. Avoid lecturing on groups in general or reading the issuer's examples aloud as a fixed list."
- statement: qaa/town-and-country-planning-2024/1.30
  forPractitioner: { text: "Courses should be designed for the whole range of learner needs: accept that access looks different for different people, and check how environments, materials, assessment and support affect students with protected characteristics or from different socio-economic backgrounds.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) on inclusive course design. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 1.30). Do not present it as stating the provider's legal duties in full or as a student outcome. Set it beside qaa/town-and-country-planning-2024/1.31 and qaa/town-and-country-planning-2024/1.32 and the theme record theme:accessibility."
  author-agent-dialogue: "Raise it with a programme team at design or review, especially when assessment methods change. Put it in practitioner terms: each part of the design should be checked for who it might exclude. Ask which assessment or setting in the course is hardest for a disabled or low-income student, and what has been done about it. Avoid putting it to a student as their responsibility."
- statement: qaa/town-and-country-planning-2024/1.31
  forPractitioner: { text: "Learning spaces and materials should be accessible to learners with mobility or learning needs or lived experience of disadvantage; students should receive reasonable adjustments for assessed needs, and the programme should seek to give everyone the resources to learn on and off campus.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you have assessed needs, you should receive reasonable adjustments, and your learning spaces, materials and resources, on campus and off, should be open to you.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on accessible environments, adjustments and resources. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 1.31). Do not present it as a statement of the law on adjustments or as a learning outcome. Set it beside qaa/town-and-country-planning-2024/1.30 and qaa/town-and-country-planning-2024/1.32 and the theme record theme:accessibility."
  author-agent-dialogue: "Raise it when a student mentions a barrier to learning, or a team plans materials or field trips. With a student, say plainly that they should get reasonable adjustments for assessed needs and point them to the service that arranges them; with staff, frame it as a design check. Ask what, if anything, stops the person using the course's spaces, materials or resources. Avoid deciding what adjustment a student needs."
- statement: qaa/town-and-country-planning-2024/1.32
  forPractitioner: { text: "Particular care should be taken that site visits, field trips, placements, group and live projects and digital learning are inclusive and fully accessible, with physical, social and financial barriers all considered.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) that field, placement and digital settings are fully accessible. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 1.32). Do not present it as a student outcome or as forbidding any particular setting. Set it beside qaa/town-and-country-planning-2024/1.21 on fieldwork and qaa/town-and-country-planning-2024/1.31."
  author-agent-dialogue: "Raise it when a team plans a field trip, placement or live project. Put it in practitioner terms: check the physical, social and financial barriers of each setting. Ask what a field trip costs a student and who might be unable to take part. Avoid giving it to a student as their duty."
- statement: qaa/town-and-country-planning-2024/1.34
  forPractitioner: { text: "Recruitment should be flexible for learners from non-standard or underrepresented backgrounds, and course content should be designed so that every student can recognise themselves in it, learn from others' experience and explore their career options.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) on flexible recruitment and a curriculum that reflects its students, in the service of a more diverse built environment profession. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 1.34). Do not present it as an admissions rule or a quota. Set it beside qaa/town-and-country-planning-2024/1.23 and qaa/town-and-country-planning-2024/2.23 on apprenticeships, and the theme records theme:accessibility and theme:edi."
  author-agent-dialogue: "Raise it with a programme team reviewing admissions, case studies or careers support. Put it in practitioner terms: who gets in, who sees themselves in the content and who is helped towards which careers. Ask whether students from non-standard routes progress and find planning jobs as often as others. Avoid presenting it to a student as their responsibility."
- statement: qaa/town-and-country-planning-2024/1.35
  forPractitioner: { text: "Weave sustainability through the course: it should engage with the UN SDGs and other frameworks and encourage students to think critically about them and about sustainability in general.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) that a planning degree engages critically with the SDGs and sustainability. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 1.35). Do not present it as requiring uncritical adoption of the SDGs; the text asks for critical thinking. Set it beside qaa/town-and-country-planning-2024/1.42, qaa/town-and-country-planning-2024/4.7.b8 and std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise it when a team maps sustainability across modules or a student questions the SDGs. Put it in practitioner terms: the course should both use the goals and invite critique of them. Ask where students are asked to challenge, not only apply, a sustainability framework. Avoid giving it to a student as an obligation."
- statement: qaa/town-and-country-planning-2024/1.42
  forPractitioner: { text: "Courses should consider how to embed SDG-linked teaching and learning across modules, drawing on the joint ESD guidance and using live projects, placements, case studies and practical examples.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should consider) on embedding the SDGs, which leaves the means to the course. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 1.42). Do not present it as requiring a dedicated sustainability module. Set it beside qaa/town-and-country-planning-2024/1.35 and std:doc:qaa-advancehe-esd-2021-guidance, which it names."
  author-agent-dialogue: "Raise it when a team reviews modules for sustainability content. Put it in practitioner terms: which modules link to which goals, and through what activities. Ask which live project or placement in the course carries sustainability practice most directly. Avoid presenting it to a student as a duty."
- statement: qaa/town-and-country-planning-2024/2.6
  forPractitioner: { text: "Joint and combined honours students will reach the core planning skills, specific and generic, and add skills from their other subject, with scope to work where the disciplines overlap.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study planning with another subject, you will gain the core planning skills, both those particular to planning and the wider ones, add skills from your other subject and can explore where the two meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation (will) for joint and combined honours students at FHEQ level 6: they reach the core planning skills, not every specialist one. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 2.6). Do not claim that joint honours students meet the full single honours range. Set it beside the threshold list qaa/town-and-country-planning-2024/4.7.b1 to qaa/town-and-country-planning-2024/4.7.b13 and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a joint honours student worries they are learning less planning than single honours peers, or a team designs a combined route. With a student, say they will gain the core planning skills and others from their second subject; with staff, frame it as what the core must protect. Ask which core planning skills the student's route covers fully, and which it covers lightly. Avoid implying a joint degree is a lesser award."
- statement: qaa/town-and-country-planning-2024/2.10
  forPractitioner: { text: "Plan progression so that students will show more complex and critical understanding of places and stakeholders, finer situated and evidence-based judgement on spatial and non-spatial matters, more independence in fieldwork and projects using primary or secondary data and a sense of theory and practice as one cycle.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As you move through your course, you will make more careful judgements about places, grounded in evidence and context, carry out fieldwork and projects more independently and come to see planning theory and practice as one cycle of asking, acting and reflecting.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation (will) of how students progress across an honours degree towards FHEQ level 6, not as a threshold item. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 2.10). Do not present the topics it gives as examples (young people and climate change, ageing in place, AI) as required content. Set it beside qaa/town-and-country-planning-2024/4.7.b2 and qaa/town-and-country-planning-2024/4.7.b12, qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise it when a student reflects on how their work has changed between years, or a team plans progression in fieldwork and projects. With a student, ask them to compare an early judgement with a recent one; with staff, frame it as the shape of progression. Ask how much of the student's latest fieldwork they planned themselves. Avoid treating the end of the progression as expected in the first year."
- statement: qaa/town-and-country-planning-2024/2.27
  forPractitioner: { text: "In periodic review, the provider will use external reviewers to give an outside view on changes and to confirm that threshold standards are met and content suits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider expectation (will) about external review in periodic course review. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 2.27). Do not present it as a regulator's rule or a student outcome. Set it beside qaa/town-and-country-planning-2024/2.28 on external examiners and qaa/town-and-country-planning-2024/4.2 on evidence of achievement."
  author-agent-dialogue: "Raise it with a programme team preparing for periodic review. Put it in practitioner terms: who the external reviewers are and what they are asked to confirm. Ask whether the review panel includes a practitioner as well as an academic. Avoid putting it to a student."
- statement: qaa/town-and-country-planning-2024/3.12
  forPractitioner: { text: "Teaching and learning strategies should be designed by academics and practitioners together, linking theory to real-life processes in an inclusive, student-centred way, with sustainability behind every choice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) that teaching strategies are co-designed with practitioners. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 3.12). Do not present it as requiring practitioners in every module. Set it beside qaa/town-and-country-planning-2024/3.13, qaa/town-and-country-planning-2024/3.15 and qaa/town-and-country-planning-2024/1.35."
  author-agent-dialogue: "Raise it with a programme team reviewing who designs teaching. Put it in practitioner terms: where practitioners shape the strategy, not only deliver guest sessions. Ask which module was last redesigned with a practitioner, and what changed. Avoid giving it to a student as a duty."
- statement: qaa/town-and-country-planning-2024/3.13
  forPractitioner: { text: "Teaching, especially the delivery of content, should actively involve professional practitioners so that real-world problems are addressed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) that practitioners take an active part in teaching. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 3.13). Do not present it as a student outcome. Set it beside qaa/town-and-country-planning-2024/3.12 and qaa/town-and-country-planning-2024/2.4."
  author-agent-dialogue: "Raise it when a team plans guest contributors, live briefs or studio teaching. Put it in practitioner terms: how practitioners bring real problems into the course. Ask which real-world problem from practice the students tackled this year. Avoid putting it to a student as their duty."
- statement: qaa/town-and-country-planning-2024/3.14
  forPractitioner: { text: "Use a variety of teaching approaches to suit different learning styles and hybrid, analogue and digital modes; the text's wording ('are to be used') is obliging but not one of the usual modals.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the statement's call for varied pedagogy; its wording 'are to be used' is recorded as described, not as must or should. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 3.14). Do not present it as a regulatory requirement. Set it beside qaa/town-and-country-planning-2024/1.33 and qaa/town-and-country-planning-2024/3.15."
  author-agent-dialogue: "Raise it when a team relies on one teaching format or moves between in-person and online delivery. Put it in practitioner terms: which approaches the course uses for which learners. Ask which students the current mix of formats suits least. Avoid giving it to a student as a duty."
- statement: qaa/town-and-country-planning-2024/3.15
  forPractitioner: { text: "Learning should actively involve stakeholders, through co-creation, interdisciplinary work, workplaces, scenarios, simulations and community participation, individually and in groups, and that mix should be encouraged.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) that learning involves stakeholders, with the forms listed as options (may). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 3.15). Do not present every listed form as required. Set it beside qaa/town-and-country-planning-2024/3.12, qaa/town-and-country-planning-2024/2.4 and qaa/town-and-country-planning-2024/4.7.b7."
  author-agent-dialogue: "Raise it when a team designs projects or simulations. Put it in practitioner terms: which stakeholders students meet, and in what roles. Ask when students last worked with a community group rather than only studying one. Avoid treating the list of forms as a checklist."
- statement: qaa/town-and-country-planning-2024/3.16
  forPractitioner: { text: "Give students a student-led research or design project in which they can frame questions and choose a method; they will communicate their research to academic or professional audiences with professional skills.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop research skills, often through a research or design project you lead yourself, and you will present your findings to academic or professional audiences in a professional way.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation (will) that students communicate their own research to academic or professional audiences; framing questions and producing original knowledge are possibilities (may, potentially), not requirements. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 3.16). Do not claim that every student produces original knowledge. Set it beside qaa/town-and-country-planning-2024/4.7.b12, qaa/town-and-country-planning-2024/4.10.b4 and qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise it when a student is choosing or planning a dissertation or design project. With a student, talk plainly about their own question, method and who will hear the results; with staff, frame it as what the project should lead to. Ask who outside the university would want to hear the student's findings, and in what form. Avoid suggesting the project must produce new knowledge to pass."
- statement: qaa/town-and-country-planning-2024/4.2
  forPractitioner: { text: "Decide your own evidence of achievement, referring as you should to Annex D, which describes the four honours classifications; expect most students to exceed the threshold.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) to refer to Annex D when deciding evidence of achievement for honours classes. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.2). Do not present Annex D as part of this statement or the threshold as the usual result. Set it beside std:doc:qaa-fheq-2024-framework, Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd to qaa/fheq-2024/annex-d/summary/r1/1st) and qaa/town-and-country-planning-2024/4.5."
  author-agent-dialogue: "Raise it with a programme team aligning marking criteria with honours classes. Put it in practitioner terms: how the course's criteria read against Annex D. Ask how the course tells a 2.1 from a 2.2 in a planning report. Avoid putting it to a student as their duty."
- statement: qaa/town-and-country-planning-2024/4.4
  forPractitioner: { text: "Students should show that they understand the standards and can apply them as fits; these are the standards a planning degree expects them to reach.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You are expected to reach these standards in your degree, and you should be able to show you understand them and can put them to use where they apply.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) that students understand and can apply the section 4 standards. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.4). Do not present it as a further standard in its own right. Set it beside the threshold list qaa/town-and-country-planning-2024/4.7.b1 to qaa/town-and-country-planning-2024/4.7.b13 and qaa/town-and-country-planning-2024/4.5."
  author-agent-dialogue: "Raise it when a student asks what the course expects of them by graduation. With a student, say plainly that they should understand the standards and be able to use them; with staff, frame it as the purpose of sharing the standards with students. Ask which of the standards the student could show evidence for today. Avoid reading the whole of section 4 aloud."
- statement: qaa/town-and-country-planning-2024/4.7.b1
  forPractitioner: { text: "At the minimum, graduates grasp that planning interventions are interlinked and affect both built and natural environments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will understand how planning interventions link together and how they affect built and natural environments.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.7). Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside qaa/town-and-country-planning-2024/4.8.b1 and qaa/town-and-country-planning-2024/4.9.b1, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what joined-up thinking about interventions means, or a team maps a first module on the environment. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. Ask can the person trace how one intervention they have studied changed both the built and the natural environment? Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum."
- statement: qaa/town-and-country-planning-2024/4.7.b2
  forPractitioner: { text: "At the minimum, graduates identify problems and resolve them with planning tools and processes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will be able to spot problems and resolve them with planning's tools and processes.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.7). Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside qaa/town-and-country-planning-2024/4.8.b2, qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise it when a student is working on a problem-based or live project, or a team writes a studio brief. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. Ask which planning tool or process did the person use on the last problem they tackled, and why that one? Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum."
- statement: qaa/town-and-country-planning-2024/4.7.b3
  forPractitioner: { text: "At the minimum, graduates know planning theory, why planning exists and how theory bears on practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will know the main theories of planning, why societies plan and how theory connects to what planners do.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.7). Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside qaa/town-and-country-planning-2024/4.7.b10, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student finds theory remote from practice, or a team reviews a theory module. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. Ask for one theory of planning, what case does it make, and how would it change what a planner does? Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum."
- statement: qaa/town-and-country-planning-2024/4.7.b4
  forPractitioner: { text: "At the minimum, graduates know the legal, political, economic, social and institutional contexts of planning, who holds power in them and how planners can work within them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will know the legal, political, economic, social and institutional settings planning works in, who holds power there and how planners can act.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.7). Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside qaa/town-and-country-planning-2024/4.7.b5 and qaa/town-and-country-planning-2024/1.10, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks why the same proposal fares differently in different places, or a team plans teaching on governance. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. Ask who held most power in a planning decision the person has studied, and what room did the planner have? Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum."
- statement: qaa/town-and-country-planning-2024/4.7.b5
  forPractitioner: { text: "At the minimum, graduates know how policy frames action across scales, how planning policy is made and what it can achieve.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will know how planning policy is made, how it guides action at different scales and how much difference it can make.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.7). Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside qaa/town-and-country-planning-2024/4.7.b4, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student is writing about a local plan or national policy, or a team plans a policy module. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. Ask how was a policy the person has studied made, and what difference did it make on the ground? Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum."
- statement: qaa/town-and-country-planning-2024/4.7.b6
  forPractitioner: { text: "At the minimum, graduates understand how planning, with design and finance, makes sustainable and inclusive places for different groups.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will understand how planning, helped by design and finance, creates places that are sustainable and work for different groups of people.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.7). Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside qaa/town-and-country-planning-2024/4.7.b7 and qaa/town-and-country-planning-2024/4.7.b8, qaa/fheq-2024/annex-d/knowledge/r1/3rd, and the theme records theme:esd and theme:edi."
  author-agent-dialogue: "Raise it when a student works on a design or development project, or a team reviews how sustainability and inclusion run through the course. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. Ask in a scheme the person has studied, how did design and finance help or hinder a place that works for different groups? Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum."
- statement: qaa/town-and-country-planning-2024/4.7.b7
  forPractitioner: { text: "At the minimum, graduates understand planning's relationship with communities and its effects, and how to work with diverse groups.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will understand how planning affects people and places and how to work well with the many different groups in a community.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.7). Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside qaa/town-and-country-planning-2024/4.7.b6 and qaa/town-and-country-planning-2024/1.25, and qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student prepares for consultation or community engagement work. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. Ask whose voices were missing from an engagement exercise the person has seen, and how would they reach them? Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum."
- statement: qaa/town-and-country-planning-2024/4.7.b8
  forPractitioner: { text: "At the minimum, graduates know what planning can do about climate change and biodiversity loss, including through infrastructure.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will know how planning can help deal with climate change and the loss of nature, for example through the infrastructure it plans.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.7). Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside qaa/town-and-country-planning-2024/4.7.b6 and qaa/town-and-country-planning-2024/1.35, std:doc:qaa-advancehe-esd-2021-guidance and qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student studies climate adaptation, green infrastructure or nature recovery. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. Ask what could a plan the person knows do differently to cut emissions or restore nature? Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum."
- statement: qaa/town-and-country-planning-2024/4.7.b9
  forPractitioner: { text: "At the minimum, graduates use planning technology and understand the digital environments planning works in.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will be able to use technology in planning and understand the digital settings planning now works in.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.7). Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside qaa/fheq-2024/annex-d/practical/r1/3rd and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student learns mapping, digital engagement or other planning software, or a team reviews digital skills. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. Ask which digital tools has the person used in planning work, and where did those tools help or mislead? Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum."
- statement: qaa/town-and-country-planning-2024/4.7.b10
  forPractitioner: { text: "At the minimum, graduates understand the place of values and ethics in planning and the profession's role in keeping them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will understand why values and ethics matter in planning and how the profession keeps to them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.7). Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside qaa/town-and-country-planning-2024/1.12 and qaa/town-and-country-planning-2024/4.10.b2, and qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Raise it when a student meets an ethical dilemma in a project or placement, or a team plans teaching on professional ethics. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. Ask what would the person do if a client's interest clashed with the public interest in a scheme? Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum."
- statement: qaa/town-and-country-planning-2024/4.7.b11
  forPractitioner: { text: "At the minimum, graduates understand planning's ties to other fields and the value of effective work across disciplines.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will understand how planning connects with other professions and why working well with them matters.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.7). Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside qaa/town-and-country-planning-2024/4.10.b3, qaa/fheq-2024/annex-d/transferable/r2/3rd, qaa/fheq-2024/4.15.b9.2 and spine:6."
  author-agent-dialogue: "Raise it when a student works with architecture, surveying or engineering students, or a team plans an interdisciplinary project. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. Ask what did another profession bring to a project the person worked on that planning could not? Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum."
- statement: qaa/town-and-country-planning-2024/4.7.b12
  forPractitioner: { text: "At the minimum, graduates value research in planning, use evidence from a range of sources and evaluate competing policies and arguments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will understand why research matters in planning, use evidence from many sources and weigh up different policies and arguments.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.7). Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside qaa/town-and-country-planning-2024/4.10.b4 and qaa/town-and-country-planning-2024/3.16, qaa/fheq-2024/4.15.b3.2, qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/knowledge/r3/3rd."
  author-agent-dialogue: "Raise it when a student plans a dissertation or an evidence base, or a team reviews research teaching. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. Ask what evidence would change the person's mind about the policy option they favour? Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum."
- statement: qaa/town-and-country-planning-2024/4.7.b13
  forPractitioner: { text: "At the minimum, graduates communicate effectively in writing, visually, numerically and digitally.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will be able to get your ideas across clearly in writing, drawings and graphics, numbers and digital media.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.7). Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/transferable/r1/3rd and qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Raise it when a student prepares a report, plan, presentation or poster. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. Ask which of writing, graphics, numbers and digital media does the person find hardest, and what would strengthen it? Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum."
- statement: qaa/town-and-country-planning-2024/4.8.b1
  forPractitioner: { text: "Typical graduates will meet all threshold criteria and go further in knowledge, cognitive and practical skills and professional competence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the standard most students reach, you will meet every minimum criterion and go further in what you know, how you think, your practical skills and your professional competence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in planning reach, beyond the threshold; an expectation, not a requirement, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.8). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside the threshold list qaa/town-and-country-planning-2024/4.7.b1 to qaa/town-and-country-planning-2024/4.7.b13, qaa/town-and-country-planning-2024/4.9.b1, and qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise it when a student asks what a good degree looks like beyond a pass, or a team writes criteria for the middle classes. With a student, put it in plain words and the second person as what most graduates reach; with staff, frame it as the level above the threshold. Ask where in one recent piece of work did the person go further than simply meeting the criteria? Avoid presenting it as the minimum a student must reach."
- statement: qaa/town-and-country-planning-2024/4.8.b2
  forPractitioner: { text: "Typical graduates will show some critical discernment, insight, initiative, creativity and autonomy in how they apply the criteria.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the standard most students reach, you will show some critical judgement, insight, initiative, creativity and independence in how you apply what you have learned.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in planning reach, beyond the threshold; an expectation, not a requirement, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.8). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/town-and-country-planning-2024/4.9.b2, qaa/fheq-2024/4.15.b9.1, qaa/fheq-2024/annex-d/cognitive/r4/2.2 and qaa/fheq-2024/annex-d/transferable/r4/2.2."
  author-agent-dialogue: "Raise it when a student wants to move from competent to good work. With a student, put it in plain words and the second person as what most graduates reach; with staff, frame it as the level above the threshold. Ask where did the person take the initiative or try a creative approach in their last project? Avoid presenting it as the minimum a student must reach."
- statement: qaa/town-and-country-planning-2024/4.9.b1
  forPractitioner: { text: "Excellent graduates will understand and apply all the criteria and develop knowledge, cognitive and practical skills and professional competence to an excellent level, beyond the typical.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the highest standard, you will understand and use every criterion and take your knowledge, thinking, practical skills and professional competence well beyond the usual level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in planning show, beyond the typical; an aspiration, not a requirement, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.9). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/town-and-country-planning-2024/4.8.b1, qaa/fheq-2024/annex-d/knowledge/r1/1st and qaa/fheq-2024/annex-d/cognitive/r1/1st."
  author-agent-dialogue: "Raise it when a student aims for a first or asks what marks out the best work. With a student, put it in plain words and the second person as what the best work shows; with staff, frame it as the level above the typical. Ask which criterion does the person's strongest work already exceed, and which holds them back? Avoid presenting it as the minimum a student must reach."
- statement: qaa/town-and-country-planning-2024/4.9.b2
  forPractitioner: { text: "Excellent graduates will apply the criteria fluently and with sophistication, and their critical discernment, insight, creativity and autonomy will be of a high order.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the highest standard, you will apply what you have learned fluently and with sophistication, showing outstanding critical judgement, insight, creativity and independence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in planning show, beyond the typical; an aspiration, not a requirement, at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.9). Do not present it as the minimum for the award or as a regulatory requirement. Set it beside qaa/town-and-country-planning-2024/4.8.b2, qaa/fheq-2024/annex-d/cognitive/r4/1st, qaa/fheq-2024/annex-d/cognitive/r3/1st and qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Raise it when a student is ready to stretch beyond good work, or a team writes criteria for a first. With a student, put it in plain words and the second person as what the best work shows; with staff, frame it as the level above the typical. Ask where has the person made an independent judgement that went beyond what they were taught? Avoid presenting it as the minimum a student must reach."
- statement: qaa/town-and-country-planning-2024/4.10.b1
  forPractitioner: { text: "Integrated master's graduates will show in-depth knowledge of at least one specialist field of planning activity and practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On an integrated master's, you will build deep knowledge of at least one specialist area of planning and its practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an added standard for the integrated master's in planning (MPlan) at FHEQ level 7 (FQHEIS level 11): graduates will show it on top of the typical bachelor's standard. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.10). Do not present it as a regulatory requirement, as a standard for one-year taught master's courses or as part of the bachelor's standards. Set it beside qaa/town-and-country-planning-2024/3.9 and qaa/town-and-country-planning-2024/4.8.b1, qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it when a student chooses a specialism in the master's year. With a student, say in plain words and the second person what the extra master's year should add; with staff, frame it as what lifts the award above the honours degree. Ask which specialist area does the person want to know in depth, and what would show that depth? Avoid treating it as expected of bachelor's students."
- statement: qaa/town-and-country-planning-2024/4.10.b2
  forPractitioner: { text: "Integrated master's graduates will understand well how planners work and the roles and responsibilities they hold, along with the ethics and values of the profession.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On an integrated master's, you will gain a good understanding of how planners work and the roles and responsibilities they carry, along with the ethics and values of the profession.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an added standard for the integrated master's in planning (MPlan) at FHEQ level 7 (FQHEIS level 11): graduates will show it on top of the typical bachelor's standard. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.10). Do not present it as a regulatory requirement, as a standard for one-year taught master's courses or as part of the bachelor's standards. Set it beside qaa/town-and-country-planning-2024/4.7.b10, qaa/fheq-2024/4.17.b8.1 and qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student prepares for placement or professional membership. With a student, say in plain words and the second person what the extra master's year should add; with staff, frame it as what lifts the award above the honours degree. Ask what responsibilities would the person carry in a first planning post, and which ethical tension would they expect to meet? Avoid treating it as expected of bachelor's students."
- statement: qaa/town-and-country-planning-2024/4.10.b3
  forPractitioner: { text: "Integrated master's graduates will work with a high degree of professionalism on assignments and in groups.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On an integrated master's, you will handle assignments and group work with a high level of professionalism.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an added standard for the integrated master's in planning (MPlan) at FHEQ level 7 (FQHEIS level 11): graduates will show it on top of the typical bachelor's standard. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.10). Do not present it as a regulatory requirement, as a standard for one-year taught master's courses or as part of the bachelor's standards. Set it beside qaa/town-and-country-planning-2024/4.7.b11, qaa/fheq-2024/4.17.b6 and qaa/fheq-2024/4.17.b8.2."
  author-agent-dialogue: "Raise it when a group project runs into difficulty or a team designs master's-level group work. With a student, say in plain words and the second person what the extra master's year should add; with staff, frame it as what lifts the award above the honours degree. Ask what would a client notice about how the person's group worked? Avoid treating it as expected of bachelor's students."
- statement: qaa/town-and-country-planning-2024/4.10.b4
  forPractitioner: { text: "Integrated master's graduates will collect and analyse data effectively and conduct independent research in planning studies.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On an integrated master's, you will collect and analyse data effectively and carry out your own research in planning.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an added standard for the integrated master's in planning (MPlan) at FHEQ level 7 (FQHEIS level 11): graduates will show it on top of the typical bachelor's standard. Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para 4.10). Do not present it as a regulatory requirement, as a standard for one-year taught master's courses or as part of the bachelor's standards. Set it beside qaa/town-and-country-planning-2024/4.7.b12 and qaa/town-and-country-planning-2024/3.16, qaa/fheq-2024/4.17.b2 and qaa/fheq-2024/4.17.b4.2."
  author-agent-dialogue: "Raise it when a student plans the master's dissertation. With a student, say in plain words and the second person what the extra master's year should add; with staff, frame it as what lifts the award above the honours degree. Ask what data will the person collect, and how will they know their analysis is sound? Avoid treating it as expected of bachelor's students."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.5" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.5" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.7" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.7" }
  - { id: "fheq:4", role: "inferred", locator: "D1, 2.8: CertHE named as an exit award; level from std:doc:qaa-fheq-2024-framework, Table 1 (Part E)" }
  - { id: "fheq:5", role: "inferred", locator: "D1, 2.8: DipHE named as an exit award; level from std:doc:qaa-fheq-2024-framework, Table 1 (Part E)" }
  - { id: "spine:6", role: "inferred", locator: "std:ref:uk-framework R2, for the honours standards" }
  - { id: "spine:7", role: "inferred", locator: "std:ref:uk-framework R2, for the integrated master's standards" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.5: \"FHEQ Level 6; FQHEIS Level 10\", for the degree with honours)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.7, for the integrated master's); the shared descriptor per std:doc:qaa-fheq-2024-framework S5" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["front matter", "1.9", "1.23", "1.24", "1.25", "1.26", "1.27", "1.28", "1.29", "1.34", "2.23", "4.7"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["front matter", "1.9", "1.27", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "3.6"] }
- { id: "theme:esd", role: "carries", carriedIn: ["front matter", "1.9", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "1.41", "1.42", "3.3", "3.12", "4.7"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["front matter", "1.9", "1.43", "1.44", "1.45", "1.46", "1.47"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-town-and-country-planning-2019-benchmarks (not held)", note: "the fourth edition, 2019; this is the fifth (D1, back matter)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree classification descriptions (4.2); FHEQ levels 6 and 7 (2.5, 2.7)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS levels 10 and 11 (2.5, 2.7)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "named at 1.42" }
- { rel: "readWith", target: "std:doc:qaa-housing-studies-2022-benchmarks", note: "front matter: other relevant statements to reference" }
- { rel: "readWith", target: "std:doc:qaa-land-construction-real-estate-and-surveying-2024-benchmarks", note: "front matter: other relevant statements to reference" }
- { rel: "refersTo", target: "RTPI learning outcomes for initial planning education and accreditation (not yet ingested: Part E)", note: "2.2, 2.15, 2.30" }
- { rel: "refersTo", target: "Chartered Town Planner Degree Apprenticeship Standard (not yet ingested: Part E)", note: "1.18, 2.23" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance (not yet ingested)", note: "front matter" }
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
- Planning is the study of how societies plan, design, manage and regulate change in built and natural environments, and of why and how they intervene and with what effects (D1, 1.15, 1.16).
- Its academic core is the rationale for planning and how it is practised, taking in land and property markets, design and place-making, ecology and geography (D1, 1.16).
- It is inter- and multi-disciplinary and holistic, drawing on the social sciences and on environmental and design disciplines (D1, 1.5, 1.11).
- It is about positive action: creative proposals reached through analysis, public participation and cooperation among competing interests (D1, 1.10).
- It is vocational and often professionally accredited, though it need not be; the RTPI alone confers Chartered Town Planner status in the UK (D1, front matter, 1.6, 2.2).
- Learning is place-based and real-world: fieldwork, site visits, live projects and practitioners in the curriculum (D1, 1.21, 2.4, 3.2).
- Theory and practice form one continuing cycle, and the planner works as broker, visionary and advocate (D1, 2.10, 3.1).
- Planning is devolved across the four UK nations, which share values and knowledge through professional and academic networks (D1, front matter, 1.8).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "planners shape equitable places for diverse societies, so the curriculum is inclusive, builds belonging for underrepresented groups and uses knowledge of particular groups at every spatial scale (D1, 1.23 to 1.29)"
  statements: ["qaa/town-and-country-planning-2024/1.23", "qaa/town-and-country-planning-2024/1.25", "qaa/town-and-country-planning-2024/4.7.b6", "qaa/town-and-country-planning-2024/4.7.b7"]
- theme: theme:accessibility
  inThisSubject: "inclusive design for every learner need, reasonable adjustments and accessible field trips, placements and live projects, physically, socially and financially; flexible recruitment (D1, 1.30 to 1.34)"
  statements: ["qaa/town-and-country-planning-2024/1.30", "qaa/town-and-country-planning-2024/1.31", "qaa/town-and-country-planning-2024/1.32", "qaa/town-and-country-planning-2024/1.34"]
- theme: theme:esd
  inThisSubject: "headed Sustainability: it underpins all of planning education; critical debate on its meaning, the four Ps, tensions between the pillars and the SDGs embedded across modules (D1, 1.35 to 1.42, 3.3, 3.12)"
  statements: ["qaa/town-and-country-planning-2024/1.35", "qaa/town-and-country-planning-2024/1.42", "qaa/town-and-country-planning-2024/4.7.b6", "qaa/town-and-country-planning-2024/4.7.b8"]
- theme: theme:enterprise
  inThisSubject: "enterprise linked to the values of planning and place-based leadership; modules on development business, land markets and climate enterprise; real-world projects with local authorities and communities (D1, 1.43 to 1.47)"
  statements: []
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.4", gloss: "five thematic groupings of content, described as non-prescriptive (3.3)" }
  - { component: "3.5", gloss: "causes and processes of change: socio-economic, political, land markets, environmental change, built and natural interaction" }
  - { component: "3.6", gloss: "practice of planning: impacts, institutions and law, plan-making, design, delivery and viability, ethics, digital technology including generative AI" }
  - { component: "3.7", gloss: "debates in planning: history of thought, theory, state and market, ethics, power, scale" }
  - { component: "3.8", gloss: "key planning skills: data, appraisal, problem-solving, numeracy, design, presentation, negotiation, digital planning, teamwork" }
  - { component: "3.9", gloss: "specialist knowledge and skills; usual in the integrated master's" }
practices:
  - { component: "2.4", kind: "teaching", gloss: "practitioners and community groups in the curriculum, placements, field visits, live projects, varied assessment, specialist software" }
  - { component: "3.2", kind: "learning", gloss: "place-based learning through site visits and field study; individual and group work" }
  - { component: "3.13", kind: "teaching", gloss: "practitioners actively involved in delivery" }
  - { component: "3.14", kind: "learning", gloss: "varied approaches for hybrid, analogue and digital modes" }
  - { component: "3.15", kind: "learning", gloss: "co-creation, scenarios, simulations, community participation" }
  - { component: "3.16", kind: "learning", gloss: "student-led research or design project" }
  - { component: "3.17", kind: "assessment", gloss: "authentic assessment reflecting professional pathways" }
  - { component: "3.18", kind: "assessment", gloss: "essays, design projects, examinations, graphics, portfolios, presentations, placement reports, role-play such as mock committees" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.6", award: "bachelor's with honours", items: 13 }
  - { rung: "typical", leadIn: "4.8", award: "bachelor's with honours", items: 2 }
  - { rung: "excellent", leadIn: "4.9", award: "bachelor's with honours", items: 2 }
  - { rung: "threshold", leadIn: "4.10", award: "master's", items: 4 }
rungBases: "4.5 defines the three: threshold, the minimum for an honours degree; typical, the attainment of most honours graduates; excellent, competencies and skills at an enhanced level. The typical and excellent items build on the whole threshold list rather than restating it item by item. 4.10's list is added to the bachelor's typical standard for the integrated master's (recorded as threshold for master's, batch 1 convention)."
outcomeLists: []
outcomes:
  - { outcome: "development beyond the threshold across the core themes", threshold: "none", typical: "qaa/town-and-country-planning-2024/4.8.b1", excellent: "qaa/town-and-country-planning-2024/4.9.b1", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "critical judgement, creativity and autonomy", threshold: "none", typical: "qaa/town-and-country-planning-2024/4.8.b2", excellent: "qaa/town-and-country-planning-2024/4.9.b2", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
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
- { body: "Royal Town Planning Institute (RTPI)", says: "uniquely confers Chartered Town Planner status in the UK; its learning outcomes for initial planning education often shape course design; it accredits courses with scrutiny and annual review; it supports early career researchers; its accredited schools meet in the Planning Schools Forum (D1, front matter, 2.2, 2.11, 2.25, 2.30)", requirements: "not yet ingested (Part E)" }
- { body: "Royal Institute of British Architects (RIBA)", says: "named as a professional body of an aligned discipline and an informal partner to planning education (D1, 2.25)", requirements: "not yet ingested (Part E): named only as a partner" }
- { body: "Royal Institution of Chartered Surveyors (RICS)", says: "named as a professional body of an aligned discipline and an informal partner to planning education (D1, 2.25)", requirements: "not yet ingested (Part E): named only as a partner" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["front matter", "1.9", "1.23", "1.24", "1.25", "1.26", "1.27", "1.28", "1.29", "1.34", "2.23", "4.7"], statements: ["1.23", "1.25", "4.7.b6", "4.7.b7"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["front matter", "1.9", "1.27", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "3.6"], statements: ["1.30", "1.31", "1.32", "1.34"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development; 1.9: education for sustainability)", carriedIn: ["front matter", "1.9", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "1.41", "1.42", "3.3", "3.12", "4.7"], statements: ["1.35", "1.42", "4.7.b6", "4.7.b8"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education; 1.9: employability and education)", carriedIn: ["front matter", "1.9", "1.43", "1.44", "1.45", "1.46", "1.47"], statements: [] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.5", "2.7"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.5", "2.7"] }
bodies:
  - { body: "Royal Town Planning Institute", citedIn: ["front matter", "2.2", "2.11", "2.25", "2.30"] }
  - { body: "Urban Studies Foundation", citedIn: ["2.11"] }
  - { body: "Planning Schools Forum", citedIn: ["2.25"] }
  - { body: "Association of European Schools of Planning", citedIn: ["2.25"] }
  - { body: "Town and Country Planning Association", citedIn: ["2.25"] }
  - { body: "Regional Studies Association", citedIn: ["2.25"] }
  - { body: "Commonwealth Association of Planners", citedIn: ["2.25"] }
  - { body: "Royal Institute of British Architects", citedIn: ["2.25"] }
  - { body: "Royal Institution of Chartered Surveyors", citedIn: ["2.25"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "descriptions of the four honours classifications, to which providers should refer when deciding evidence of achievement" }
  - { document: "std:doc:qaa-fheq-2024-framework and std:doc:qaa-fqheis-2024-framework", named: "FHEQ Level 6 and 7; FQHEIS Level 10 and 11", citedIn: ["2.5", "2.7"], role: "levels of the honours degree and the integrated master's" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "the QAA and Advance HE's Education for Sustainable Development Guidance", citedIn: ["1.42"], role: "a framework for embedding the SDGs" }
  - { document: "UN Sustainable Development Goals (external)", named: "UN Sustainable Development Goals (SDGs)", citedIn: ["1.35", "1.42", "3.3"], role: "the frame of the sustainability theme and of content design" }
  - { document: "std:doc:qaa-housing-studies-2022-benchmarks; std:doc:qaa-land-construction-real-estate-and-surveying-2024-benchmarks", named: "Housing Studies; Land, Construction, Real Estate and Surveying", citedIn: ["front matter"], role: "other statements to reference" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code", citedIn: ["front matter"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "Chartered Town Planner Degree Apprenticeship Standard (not yet ingested: Part E)", named: "Chartered Town Planner Degree Apprenticeship Standard", citedIn: ["1.18", "2.23"], role: "the apprenticeship route in England" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "town-and-country-planning", definition: "the name used for the field and, shortened to Planning, for the range of closely related courses under other titles such as spatial, urban and regional or community planning (D1, 1.1)", beneficiaryDefinition: "the subject you study, whatever your course is called", scopeNote: "the statement uses Planning throughout as shorthand", category: "unknown", practices: ["education"] }
- { slug: "inclusivity", definition: "an approach that builds an educational setting free of barriers, in which underrepresented groups can take full part (D1, 1.23)", beneficiaryDefinition: "learning set up so that nothing stops anyone taking full part", scopeNote: "the basis of the inclusive curriculum (1.23 to 1.29)", category: "unknown", practices: ["education"] }
- { slug: "four-ps", definition: "the four concerns planning is often said to balance: people, place, prosperity in more than the economic sense, and the planet (D1, 1.38)", beneficiaryDefinition: "people, place, prosperity and planet", scopeNote: "framed under sustainability", category: "unknown", practices: ["education", "planning"] }
- { slug: "threshold-standard", definition: "the minimum needed for an honours degree (D1, 4.5)", scopeNote: "with typical and excellent above it", category: "unknown", practices: ["education"] }
- { slug: "typical-standard", definition: "the attainment most honours graduates reach (D1, 4.5)", scopeNote: "builds on the threshold (4.8)", category: "unknown", practices: ["education"] }
- { slug: "excellent-standard", definition: "competencies and skills at an enhanced level (D1, 4.5)", scopeNote: "builds on the typical (4.9)", category: "unknown", practices: ["education"] }
- { slug: "integrated-masters-planning", definition: "a four-year full-time (or longer part-time) integrated master's in planning at FHEQ level 7, FQHEIS level 11 (D1, 2.7)", beneficiaryDefinition: "a degree that runs undergraduate and master's study together", scopeNote: "often called the MPlan; standards in 4.10", category: "unknown", practices: ["education"] }
- { slug: "learning", definition: "change in a person brought about by gaining information, understanding, skills, attitudes and behaviour (D1, 3.14)", scopeNote: "the basis for varied pedagogy", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "town-and-country-planning", form: "Town and Country Planning", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "town-and-country-planning", form: "Planning", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "formal" }
- { concept: "inclusivity", form: "inclusivity", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "four-ps", form: "four 'Ps'", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "threshold-standard", form: "threshold standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "typical-standard", form: "typical standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "excellent-standard", form: "excellent standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "integrated-masters-planning", form: "MPlan", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "discipline-specific" }
- { concept: "learning", form: "learning", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "broader", from: "excellent-standard", to: "typical-standard", note: "4.9: in addition to the threshold and typical standards" }
- { rel: "broader", from: "typical-standard", to: "threshold-standard", note: "4.8: in addition to the threshold criteria" }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement Town and Country Planning"
  edition: "April 2024 (fifth edition)"
  year: 2024
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/town-and-country-planning-2024/town-and-country-planning-2024.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 893eac1731a05f2d243fb07f2028b42e794d3c3c776f5b1a68143faa5fe3cffe
  heldFiles: ["wkspc2601-library/txt/qaa-2024-town-country-planning-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2024-town-country-planning-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2024-town-country-planning-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2024-town-country-planning-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0102", source: "RTPI learning outcomes for initial planning education and its accreditation policy", why: "the requirements of the body named in SB5; cited at 2.2, 2.15 and 2.30", tier: "primary" }
- { w: "W-std-0103", source: "Chartered Town Planner Degree Apprenticeship Standard (Institute for Apprenticeships and Technical Education)", why: "the apprenticeship route named at 1.18 and 2.23", tier: "primary" }
```

## Part E Gaps and questions
- Rungs: three rungs, defined in 4.5 and listed at 4.6 and 4.7 (threshold, 13 items), 4.8 (typical, 2) and 4.9 (excellent, 2); 4.10 adds 4 items for the integrated master's. Differs from Psychology: the typical and excellent standards are two broad items each that build on the whole threshold list, not parallel lists.
- Skeleton corrections: 4.5.b1 to b3 were marked threshold rung items; they are the definitions of the three rungs (rungBases), not statements. 4.9.b1 and b2 were marked threshold; they are excellent. 4.10.b1 to b4 were marked typical; they are the integrated master's list.
- Integrated master's (4.10): its lead-in sets the baseline at the bachelor's typical standard, not the threshold, then adds four items. Recorded as rung threshold, award master's (meaning the integrated master's, MPlan, 2.7), level fheq:7 stated (2.7), by the batch 1 convention; for P3 whether a rung value should say it starts from typical.
- 4.6.b1 to b5 are the five core themes for standards (KU, CS, PS, TS, PC), labels, not statements. Each 4.7 item carries the issuer's theme codes; the five map one to one onto Annex D's knowledge, cognitive, practical, transferable and professional categories, so each aaw points to the Annex D 3rd cells. Our domain for each item is read from its codes and content (inferred): KU as knowledge or understanding, CS and PS as subject-skill, TS as generic-skill, PC by content (4.7.b10 understanding, 4.7.b11 generic-skill).
- Threshold items are noun phrases completing the 4.7 lead-in; several items (4.7.b1, 4.8.b1, 4.8.b2, 4.9.b2, 4.10.b1, 4.10.b2) have no verb of their own, so verbs is empty.
- Threshold force is threshold, from 4.6 ("the minimum requirement") and 4.5; forceFrom 4.6. The excellent lead-in 4.9 has no modal ("excellent graduates also demonstrate"): force will taken from 4.1 ("will have demonstrated"), forceFrom 4.1, for P3. The integrated master's lead-in has "will" and "can be expected to": recorded will.
- gradeOf, inferred: 4.9.b1 to 4.8.b1 and 4.9.b2 to 4.8.b2 (content plainly matches, same order); no typical item links to a single threshold item. 4.9.b2 drops "initiative", which 4.8.b2 has; 4.9.b1 says "beyond the typical threshold", read as beyond the typical standard.
- Domain for the aggregate items is a forced single choice: 4.8.b1 and 4.9.b1 knowledge (they span all the core themes), 4.8.b2 and 4.9.b2 generic-skill.
- Section 3's lists (3.5 to 3.8, 38 items) are in the plain present ("Planning students demonstrate ... knowledge and understanding of"), with 3.8 "might include"; 3.3 says they are thematic groupings, not a prescriptive list. Recorded as SB3 areas, not statements; 4.3 says the standards apply to all of them. For P3 alongside template open point 5.
- Obliging words outside the five, for Abbott: "it is essential" (1.23, recorded as a describes statement; 2.27, recorded will from its own "will"); "are to be used" (3.14, describes); "needs to be", "requires" (1.25 first sentence, 1.26); "need to" (1.14, of planners; 1.25 "will need to", recorded will); "have to meet" (2.15, accredited courses); "it is important" (1.33, 2.24, 3.17); "it is expected that", "would be expected" (2.5, 4.4); "would be anticipated", "will need to adapt" (3.18). Only 1.23, 1.25, 2.27, 3.14 and 4.4 are taken as statements.
- Plain-present provider norms not taken as statements (template open point 5): 1.22, 1.28, 2.1, 2.3, 2.12, 2.13, 2.26, 3.10, 3.11 (for example "Education strategies incorporate ...").
- Mixed modals in one paragraph, recorded by the main obliging word: 1.12 (will and should: should), 1.21 (may, should, will: should), 3.15 (should, may: should), 3.16 (can, may, will: will), 4.2 (will, should: should).
- Front matter "consideration should be given to referencing other relevant Subject Benchmark Statements" and "Joint courses ... should also note" are in excluded matter; not statements; recorded as readWith in S7.
- 1.9 names the themes as "education for sustainability" and "employability and education"; the second appears to mean enterprise and entrepreneurship education (the front matter names "employability, entrepreneurship and enterprise education"); tagged theme:enterprise, for P3.
- Generative AI and AI are mentioned (1.46, 2.10, 3.6, 3.8, 3.18) but there is no generative AI section, so theme:generative-ai is not used.
- Statements with a student version though addressed partly to the provider (addressee both): 1.10, 1.12, 1.23, 1.31.
- Codes: hecos 100197 planning, hecos 100199 urban and regional planning and cah CAH13-01-04 are stated (1.1 names Town and Country Planning and Urban and Regional Planning). hecos 100593 rural planning is inferred (the "country" in the title; not named) and held back from any lookup until P3. Spatial, land-use, city, environmental and community planning (1.1) have no HECoS term of their own.
- Frameworks: FHEQ and FQHEIS are cited at 2.5 and 2.7 only; CQFW is not cited. The front matter names the Quality Assessment Framework for Wales, the Quality Enhancement Framework (Scotland) and the OfS regulatory framework: quality frameworks, not qualification frameworks. S5 fheq:4 and fheq:5 are inferred from 2.8's exit awards (CertHE, DipHE) by the FHEQ's Table 1; spine:6 and spine:7 from the reference framework's R2.
- Bodies: the RTPI's requirements (learning outcomes for initial planning education, accreditation) are not yet ingested (D3). RIBA and RICS are named only as aligned partners (2.25); their requirements are out of scope. The Planning Officers Society appears only in the Advisory Group list (excluded).
- Shared documents: the Chartered Town Planner Degree Apprenticeship Standard (1.18, 2.23) is not ingested (D3). QAA's 2018 Enterprise and Entrepreneurship Education guidance (std:doc:qaa-enterprise-2018-guidance) is in the reference list (section 5, excluded) but not cited in the body, so it is not in SB6.
- 1.35 "(see also section 3)" and 1.47 "As noted in section 3" are references, not statements (DPN-1).
- supersedes: the back matter says this is the fifth edition (April 2024) and names the fourth (2019); the 2019 statement is not held.
- Patterns that differ from Psychology: rung items carry the issuer's theme codes; typical and excellent are two broad items each; no "are able to" outcome lists; an integrated master's add-on list; the excellent lead-in has no modal.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:42: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0133 (P1); built by tools/bm_build.py.
