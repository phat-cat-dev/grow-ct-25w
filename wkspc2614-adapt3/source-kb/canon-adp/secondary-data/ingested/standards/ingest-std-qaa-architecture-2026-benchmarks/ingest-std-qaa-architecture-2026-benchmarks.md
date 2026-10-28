---
id: std:doc:qaa-architecture-2026-benchmarks
title: "Subject Benchmark Statement Architecture"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100122", label: "architecture", basis: "stated" }
  - { scheme: "cah", code: "CAH13-01-01", label: "architecture", basis: "stated" }
  - { scheme: "cah", code: "CAH13-01", label: "architecture, building and planning", basis: "stated" }
  - { scheme: "hecos", code: "100583", label: "architectural design", basis: "inferred" }
edition: "April 2026 (Fourth Edition)"
published: 2026-04
status: current
supersedes: "the previous Architecture statement (the text names key changes from it and lists a 2020 advisory group; its edition is not given: Part E)"
heldText: { method: sha256-bytes, raw: d7d10b2df272f178173603ea94e1ebc61b68cd5871662b75073433129c920b9a, normalised: 4a602dcbb103a41bfceec2881f111d777ce309dbf7162b816f82209512b3ca32 }
heldTextStan: { method: sha256-stan, raw: d7d10b2df272f178173603ea94e1ebc61b68cd5871662b75073433129c920b9a, normalised: 9bb98a3c0c206815206c84f28ef8a2e1cc29de90d68d9d7482aed08e3ab9cb36 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, the revision series with cross-cutting themes (this the fourth edition for Architecture)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0087 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:15"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Architecture (QAA, April 2026)

> Run 0087, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2026-architecture-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a student of Architecture will have shown at the end of an honours degree and of a master's, set out as twelve named literacies stated twice, once as the honours minimum and once as the master's minimum. Reach for it when designing, approving, reviewing or describing an architecture course, its outcomes or its studio teaching and reviews. It is not the ARB's accreditation criteria or RIBA's validation criteria, it states no typical or excellent rung and in England it is not a regulatory requirement.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2026 as the fourth edition for the subject, the statement places architecture between the arts, sciences and humanities with design as its defining skill, and describes the context of a degree under five cross-cutting themes: equity, diversity and inclusion; accessibility and the needs of disabled students; education for sustainable development; employability, entrepreneurship and enterprise education; and generative artificial intelligence, the fifth new to the series. It describes curriculum design, progression, flexibility, partnerships and review, then content, structure and the studio, reviews and assessment. Its standards are minimum standards only, a taxonomy of twelve literacies defined for the bachelor's degree with honours (4.6) and again for the master's, including the integrated master's (4.7); performance above the minimum is left to the degree classification descriptions (Annex D). It names two professional bodies, the Architects Registration Board and the Royal Institute of British Architects, whose own outcomes apply to recognised degrees.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Architecture"
edition: "April 2026 (Fourth Edition)"
dates:
  published: 2026-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector-owned reference point; not a sector-recognised standard in England, part of the quality arrangements in Scotland, Wales and Northern Ireland (D1, front matter, Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2026", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate in Architecture can be expected to know, do and understand at the end of an honours degree and of a master's, and the context, features, content and delivery of courses in the subject"
appliesTo:
  awards: ["bachelor's with honours", "master's"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs' definitions of academic standards; information for prospective students and employers; student-facing articulation in handbooks and briefs"]
doesNot: "it does not prescribe approaches to teaching, learning or assessment, does not repeat the learning outcomes of the accrediting bodies and does not interpret legislation or carry statutory or regulatory requirements (D1, front matter)"
beneficiary: the student
statedScope: "\"The Statement addresses Architecture courses at both undergraduate and taught postgraduate levels, as well as helping to inform those designing other degree courses, including apprenticeship degrees, which have a substantial architectural content or are a cognate discipline.\" (D1, front matter, How can I use this document?)"
statedSubjects:
  - { name: "Architecture", locator: "(D1, title; front matter)", kind: "subject", codes: [{ scheme: "hecos", code: "100122", label: "architecture" }, { scheme: "cah", code: "CAH13-01-01", label: "architecture" }] }
  - { name: "Architect (integrated degree) L7 and Architectural Assistant (Integrated Degree) L6 Apprenticeships", locator: "(D1, 2.10)", kind: "programme title", codes: [{ scheme: "hecos", code: "100122", label: "architecture" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Architecture degree", gloss: "an interdisciplinary field joining arts, sciences and humanities" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Architecture degree", gloss: "design as the architect's core skill and its wider value" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Architecture degree", gloss: "contested design as a spur to debate and openness to uncertainty" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Architecture degree", gloss: "collaboration, team leadership and shared authorship" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Architecture degree", gloss: "professional orientation, wider careers and differing governance" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "a more representative profession and a lasting provider commitment to EDI" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "inclusive settings, reflective processes and fair access" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "inclusive curricula and a decolonising rereading of the discipline" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "respectful studio culture and a range of voices" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "hidden costs of study and their effect on access" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "managing the pressures of presenting in studio and reviews" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "legal duties on adjustments and the subject's design expertise" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessibility as person and setting together" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "holistic approaches beyond basic compliance" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "neurodivergent needs in studio and lecture settings" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "flexible curriculum and assessment for diverse needs" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "oversight frameworks where needs in a group conflict" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "the physical studio and neurodivergent students" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "the climate and ecological emergency and the architect's part" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ESD aims and the guidance to draw on" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "critical engagement with sustainability" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "themes students may meet within sustainability" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "climate literacy built across the course and predictive tools" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "interdisciplinary co-design and ethical reflection" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "providers modelling sustainable practice" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "what enterprise education offers careers" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "enterprise and entrepreneurship education defined" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Career readiness for EEE", gloss: "career readiness in and alongside the curriculum" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Career readiness for EEE", gloss: "career events, international links and mobility" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Career readiness for EEE", gloss: "careers beyond the title of architect" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Situated learning for EEE", gloss: "placements and fair support to find one" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Situated learning for EEE", gloss: "alternative routes to professional experience" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Situated learning for EEE", gloss: "what work placements give students" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Situated learning for EEE", gloss: "extracurricular links to practice and alumni" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Situated learning for EEE", gloss: "live projects in the core curriculum" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "the effect of GenAI on education and practice" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "teaching about GenAI and its implications" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "reflective assessment of authorship and process" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "authorship, attribution and use policies for GenAI" }
  - { number: "1.40", order: 42, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "inclusive and affordable use of GenAI" }
  - { number: "2.1", order: 44, componentType: paragraph, parent: "section 2", heading: "Curriculum design", gloss: "a curriculum open to new knowledge and techniques" }
  - { number: "2.2", order: 45, componentType: paragraph, parent: "section 2", heading: "Curriculum design", gloss: "lifelong learning and routes beyond registration" }
  - { number: "2.3", order: 46, componentType: paragraph, parent: "section 2", heading: "Curriculum design", gloss: "combined and joint honours students" }
  - { number: "2.4", order: 47, componentType: paragraph, parent: "section 2", heading: "Curriculum design", gloss: "PSRB content requirements and going beyond them" }
  - { number: "2.5", order: 48, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression across levels towards the minimum standards" }
  - { number: "2.6", order: 49, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "readiness for postgraduate study" }
  - { number: "2.7", order: 50, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards at lower levels" }
  - { number: "2.8", order: 51, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "practice periods and study abroad within progression" }
  - { number: "2.9", order: 52, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "monitoring time away and adjustments in progression" }
  - { number: "2.10", order: 53, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "apprenticeship routes at Levels 6 and 7" }
  - { number: "2.11", order: 54, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "course length outside Scotland" }
  - { number: "2.12", order: 55, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "Scottish degree structure and titles" }
  - { number: "2.13", order: 56, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "integrated master's length and levels" }
  - { number: "2.14", order: 57, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "part-time study and credit" }
  - { number: "2.15", order: 58, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "inclusive and accessible delivery modes" }
  - { number: "2.16", order: 59, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "studio culture, digital tools and release structures" }
  - { number: "2.17", order: 60, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "electives with coherence kept" }
  - { number: "2.18", order: 61, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "delivery with partners" }
  - { number: "2.19", order: 62, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "strategic and transnational partnerships" }
  - { number: "2.20", order: 63, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "applying the standards across partnered awards" }
  - { number: "2.21", order: 64, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "live projects and activities with external partners" }
  - { number: "2.22", order: 65, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "partnerships that widen participation" }
  - { number: "2.23", order: 66, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "course monitoring, evaluation and the student voice" }
  - { number: "2.24", order: 67, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "externality in periodic review" }
  - { number: "2.25", order: 68, componentType: paragraph, parent: "section 2", heading: "Professional, statutory and regulatory bodies (PSRBs)", gloss: "ARB and RIBA as partners in course design" }
  - { number: "2.26", order: 69, componentType: paragraph, parent: "section 2", heading: "Professional, statutory and regulatory bodies (PSRBs)", gloss: "RIBA validation of Parts 1 to 3" }
  - { number: "2.27", order: 70, componentType: paragraph, parent: "section 2", heading: "Professional, statutory and regulatory bodies (PSRBs)", gloss: "ARB accreditation from January 2028" }
  - { number: "2.28", order: 71, componentType: paragraph, parent: "section 2", heading: "Professional, statutory and regulatory bodies (PSRBs)", gloss: "professional body monitoring and visits" }
  - { number: "2.29", order: 72, componentType: paragraph, parent: "section 2", heading: "External examiners", gloss: "who external examiners are and what they judge" }
  - { number: "2.30", order: 73, componentType: paragraph, parent: "section 2", heading: "External examiners", gloss: "examiners' reports and threshold comparisons" }
  - { number: "2.31", order: 74, componentType: paragraph, parent: "section 2", heading: "External examiners", gloss: "advisory boards" }
  - { number: "2.32", order: 75, componentType: paragraph, parent: "section 2", heading: "External examiners", gloss: "the cross-cutting themes in review" }
  - { number: "3.1", order: 77, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "activities seen through the idea of literacies" }
  - { number: "3.2", order: 78, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "the taxonomy as an overlapping framework" }
  - { number: "3.3", order: 79, componentType: area, parent: "section 3", heading: "Content", gloss: "the twelve literacies named" }
  - { number: "3.4", order: 80, componentType: practice, parent: "section 3", heading: "Content", gloss: "integrated design studio projects and their assessment" }
  - { number: "3.5", order: 81, componentType: area, parent: "section 3", heading: "Content", gloss: "three core subject areas around design" }
  - { number: "3.6", order: 82, componentType: practice, parent: "section 3", heading: "Content", gloss: "delivery methods for subject modules" }
  - { number: "3.7", order: 83, componentType: area, parent: "section 3", heading: "Content", gloss: "architectural humanities as critical enquiry" }
  - { number: "3.8", order: 84, componentType: area, parent: "section 3", heading: "Content", gloss: "technology as a subject area" }
  - { number: "3.9", order: 85, componentType: area, parent: "section 3", heading: "Content", gloss: "professional practice as a subject area" }
  - { number: "3.10", order: 86, componentType: paragraph, parent: "section 3", heading: "Structure", gloss: "foundations in the early stages" }
  - { number: "3.11", order: 87, componentType: paragraph, parent: "section 3", heading: "Structure", gloss: "rising complexity and synthesis" }
  - { number: "3.12", order: 88, componentType: paragraph, parent: "section 3", heading: "Structure", gloss: "specialist enquiry and master's level investigation" }
  - { number: "3.13", order: 89, componentType: area, parent: "section 3", heading: "Structure", gloss: "postgraduate specialisms" }
  - { number: "3.14", order: 90, componentType: practice, parent: "section 3", heading: "Learning and teaching", gloss: "modes of learning and teaching" }
  - { number: "3.15", order: 91, componentType: practice, parent: "section 3", heading: "Learning and teaching", gloss: "studio as space, method and culture" }
  - { number: "3.16", order: 92, componentType: practice, parent: "section 3", heading: "Studio pedagogy", gloss: "studio as shared physical workspace" }
  - { number: "3.17", order: 93, componentType: paragraph, parent: "section 3", heading: "Studio pedagogy", gloss: "design studio as transformative pedagogy" }
  - { number: "3.18", order: 94, componentType: paragraph, parent: "section 3", heading: "Studio pedagogy", gloss: "the pattern of studio projects" }
  - { number: "3.19", order: 95, componentType: practice, parent: "section 3", heading: "Studio pedagogy", gloss: "co-authored group projects" }
  - { number: "3.20", order: 96, componentType: paragraph, parent: "section 3", heading: "Studio pedagogy", gloss: "vertical and interdisciplinary studio groups" }
  - { number: "3.21", order: 97, componentType: practice, parent: "section 3", heading: "Studio pedagogy", gloss: "tutorials and practitioners in studio" }
  - { number: "3.22", order: 98, componentType: paragraph, parent: "section 3", heading: "Studio pedagogy", gloss: "iteration in studio and portfolios showing process" }
  - { number: "3.23", order: 99, componentType: paragraph, parent: "section 3", heading: "Resources", gloss: "studio facilities students need" }
  - { number: "3.24", order: 100, componentType: paragraph, parent: "section 3", heading: "Resources", gloss: "specialist workshops and model storage" }
  - { number: "3.25", order: 101, componentType: paragraph, parent: "section 3", heading: "Resources", gloss: "communication and space to display work" }
  - { number: "3.26", order: 102, componentType: paragraph, parent: "section 3", heading: "Resources", gloss: "digital hardware, software and equitable access" }
  - { number: "3.27", order: 103, componentType: paragraph, parent: "section 3", heading: "Resources", gloss: "library and technical literature" }
  - { number: "3.28", order: 104, componentType: paragraph, parent: "section 3", heading: "Resources", gloss: "lecture and seminar spaces" }
  - { number: "3.29", order: 105, componentType: practice, parent: "section 3", heading: "Specialist, research and practice-informed teaching", gloss: "specialist teaching tested through studio" }
  - { number: "3.30", order: 106, componentType: paragraph, parent: "section 3", heading: "Specialist, research and practice-informed teaching", gloss: "research- and practice-informed teaching and thematic studios" }
  - { number: "3.31", order: 107, componentType: practice, parent: "section 3", heading: "Specialist, research and practice-informed teaching", gloss: "practice experience and routes to registration" }
  - { number: "3.32", order: 108, componentType: practice, parent: "section 3", heading: "Specialist, research and practice-informed teaching", gloss: "live projects with clients" }
  - { number: "3.33", order: 109, componentType: practice, parent: "section 3", heading: "Specialist, research and practice-informed teaching", gloss: "learning in context, site and study visits" }
  - { number: "3.34", order: 110, componentType: practice, parent: "section 3", heading: "Reviews", gloss: "reviews as feedback and presentation practice" }
  - { number: "3.35", order: 111, componentType: paragraph, parent: "section 3", heading: "Reviews", gloss: "stress and power in review formats" }
  - { number: "3.36", order: 112, componentType: paragraph, parent: "section 3", heading: "Reviews", gloss: "student-centred and inclusive review formats" }
  - { number: "3.37", order: 113, componentType: paragraph, parent: "section 3", heading: "Reviews", gloss: "reviews in summative assessment" }
  - { number: "3.38", order: 114, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "scaffolded assessment and self and peer evaluation" }
  - { number: "3.39", order: 115, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formative and summative feedback" }
  - { number: "3.40", order: 116, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment types and capturing process" }
  - { number: "3.41", order: 117, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "the culminating portfolio and thesis" }
  - { number: "3.42", order: 118, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "the portfolio as synoptic assessment" }
  - { number: "3.43", order: 119, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "criteria for design work and visual rubrics" }
  - { number: "3.44", order: 120, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "assessment spaces and alternatives" }
  - { number: "3.45", order: 121, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "group work and its assessment" }
  - { number: "3.46", order: 122, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "flexible and experimental assessment" }
  - { number: "3.47", order: 123, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "students in feedback and assessment" }
  - { number: "4.1", order: 125, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the minimum standards and the integrated master's" }
  - { number: "4.2", order: 126, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "achievement above the minimum and Annex D" }
  - { number: "4.3", order: 127, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "competence standards and the Equality Act" }
  - { number: "4.4", order: 128, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "how the literacies are applied and assessed" }
  - { number: "4.5", order: 129, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "PSRB outcomes for recognised degrees" }
  - { number: "4.6", order: 130, componentType: stem, parent: "section 4", heading: "Bachelor's level minimum standards", gloss: "stem: the honours minimum, twelve literacies" }
  - { number: "4.7", order: 131, componentType: stem, parent: "section 4", heading: "Master's level minimum standards", gloss: "stem: the master's minimum, twelve literacies" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of an Architecture degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of the Architecture course", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2, SB5 and SB6" }
  - { number: "none", heading: "section heading lines (sections 1 to 4)", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "Membership of the Advisory Group (2026, 2020, 2010, 2000)", kind: "other: back matter; names of people, read only for the edition history" }
  - { number: "none", heading: "Fourth Edition; Published 16 April 2026; copyright and address", kind: "other: colophon, read for S1 and S8" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 68 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/architecture-2026/1.5
  locator: { number: "1.5", headingPath: ["Context and purposes of an Architecture degree", "Purposes and characteristics of an Architecture degree"] }
  span: { start: 13499, end: 14614 }
  source: "1.5 Architecture education is professionally oriented, with most courses being validated or accredited by PRSBs, providing a recognised pathway to chartered status or to registration and the title of Architect. Many students who choose to study Architecture do so with the intention of becoming a professional architect. However, the knowledge, understanding, skills and attributes gained through an Architecture education are transferable to a wide range of other occupations and students often choose to go on to pursue a related career, or work in different fields. This reflects the success of the broad learning opportunities that architectural education can offer, which may also inform the design of a course. Architecture is a global and mobile profession while Architecture education in the UK takes place in an internationalised context. To support Architecture students in preparing for this, elements of architectural education reflect global, national and devolved governance structures. Courses should take account of differences in governance, law, policy and practice as appropriate for their focus."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["take"]
  about: "governance differences across the nations"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Architecture is a professionally oriented, global field that most students enter hoping to become architects, though many move to other careers; courses should allow for how governance, law, policy and practice vary, as fits each course's focus."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.6
  locator: { number: "1.6", headingPath: ["Context and purposes of an Architecture degree", "Equity, diversity and inclusion"] }
  span: { start: 14647, end: 15179 }
  source: "1.6 The profession of architecture relies on building a graduate community that is more diverse, inclusive and representative of the wider society it designs for and with. Barriers into the profession have been and continue to be well researched and articulated but are yet to\n\n5\nbe surmounted. Providers must continue to develop sustained and reflective commitment to equity, diversity and inclusion (EDI) which should be meaningfully embedded within the culture and practice of Architecture education and professional engagement.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["continue", "develop", "embedded"]
  about: "a sustained provider commitment to EDI"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The profession needs a graduate body that better reflects the society it designs for, and barriers to entry persist; providers must keep developing a sustained, reflective commitment to equity, diversity and inclusion, which should be built into the culture and practice of architectural education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.7
  locator: { number: "1.7", headingPath: ["Context and purposes of an Architecture degree", "Equity, diversity and inclusion"] }
  span: { start: 15179, end: 15889 }
  source: "1.7 Equitable, diverse and inclusive learning environments promote fairness, acceptance and respect. They recognise that each individual brings unique lived experiences and acknowledge the benefits that comes from diversity , individual differences, and the varied knowledge and practices that emerge from these. Schools of Architecture should establish ongoing reflective processes to address emerging equity and diversity challenges and collaborate with students to develop more inclusive curricula and pedagogies. Providers have a responsibility to continuously advance equitable access and opportunities for students from all backgrounds to ensure students can progress successfully through their studies.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "schools of architecture"
  addressee: provider
  verbs: ["establish", "address", "collaborate", "develop"]
  about: "reflective processes for equity and inclusive curricula"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Inclusive settings value what each person brings; schools should set up continuing reflective processes to tackle new equity and diversity issues and work with students on more inclusive curricula and teaching, and providers carry a duty to keep widening fair access and opportunity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.9
  locator: { number: "1.9", headingPath: ["Context and purposes of an Architecture degree", "Equity, diversity and inclusion"] }
  span: { start: 16739, end: 17423 }
  source: "1.9 Schools should ensure an inclusive, supportive and respectful learning environment which promotes opportunities to engage in and inform critical discourse, exploring, challenging, critiquing, deconstructing and building on established approaches and worldviews within the discipline. Wherever possible, schools should look to expose students to diverse voices and perspectives. This may include staff, but also guest speakers, reviewers and consultants who can share viewpoints from across and outside the field. This variety of voices and pedagogies broadens and enriches the educational experience by giving students access to a wide range of ideas, approaches and role models.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "schools"
  addressee: provider
  verbs: ["ensure", "look", "expose"]
  about: "a respectful studio culture with diverse voices"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Schools should keep the learning environment inclusive, supportive and respectful, open to critique of established approaches, and where they can should bring students into contact with a wide range of voices and perspectives, from staff, guest speakers, reviewers and consultants."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of an Architecture degree", "Equity, diversity and inclusion"] }
  span: { start: 17423, end: 18409 }
  source: "1.10 Schools should recognise the implications of the additional explicit and hidden costs involved in studying Architecture and the potential for these to disadvantage and exclude potential learners. Expenses incurred for materials, digital resources (hardware and software) and study visits may prevent students from fully participating in their studies and from realising their potential. An expectation to spend long hours working in studio can also place those with external commitments, such as caring responsibilities or those working to support their studies, at a disadvantage. Schools should aim to minimise additional costs incurred by students wherever possible, supporting equitable access to resources, and being mindful of the challenges many students can face. They should also recognise the specific challenges of access to work-based learning and/or professional practice experience faced by some student groups, and the potential for this to exacerbate inequalities.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "schools"
  addressee: provider
  verbs: ["recognise", "aim", "minimise"]
  about: "the hidden costs of study"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Extra visible and hidden costs, such as materials, hardware, software, study visits and long studio hours, can exclude students; schools should recognise these effects, try to keep extra costs down and support fair access to resources and should also recognise unequal access to work-based learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.11
  locator: { number: "1.11", headingPath: ["Context and purposes of an Architecture degree", "Equity, diversity and inclusion"] }
  span: { start: 18409, end: 19158 }
  source: "1.11 Architecture education is centred on 'the studio' (as defined in paragraph 3.15). Students regularly present and discuss their work in front of others, a format which can be difficult for some students and therefore needs to be carefully managed. Schools should recognise the specific challenges that reviews (as defined in paragraph 3.32) may present for some students. Within and beyond established studio pedagogy, programmes can utilise a variety of modes and methods in both the delivery and assessment of courses to support inclusive learning, recognising different learning styles to support individual needs. Programmes may benefit from using inclusive curriculum toolkits or checklists to support their pedagogic and curriculum design."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "schools"
  addressee: provider
  verbs: ["recognise"]
  about: "the strain of presenting work in reviews"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Studio learning means students often present work to others, which some find hard; schools should recognise the particular difficulties reviews can bring, and programmes can use a variety of modes and methods to support inclusive learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of an Architecture degree", "Accessibility and the needs of disabled students"] }
  span: { start: 19212, end: 19665 }
  source: "1.12 Educational institutions are legally required to comply with the Disability Discrimination Act 1995, the Education Act 1996, and the Equality Act 2010, which mandate the provision of 'reasonable adjustments' for students, academic staff and professional services staff. Architecture schools, often engaged at the forefront of research and teaching in accessible design, are uniquely positioned to embed accessibility beyond reasonable adjustments.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must
  level: none
  appliesTo: "educational institutions"
  addressee: provider
  verbs: ["comply"]
  about: "legal duties to make reasonable adjustments"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Institutions are bound by law, under the Equality Act 2010 and the earlier Disability Discrimination Act 1995 and Education Act 1996, to provide reasonable adjustments for students and staff; schools of architecture, often expert in accessible design, are well placed to go further."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.14
  locator: { number: "1.14", headingPath: ["Context and purposes of an Architecture degree", "Accessibility and the needs of disabled students"] }
  span: { start: 20513, end: 21008 }
  source: "1.14 Institutions should adopt integrated, holistic approaches to meeting accessibility needs that value and enhance potential for success. This may move beyond basic compliance to creating genuinely inclusive educational environments in which all students and staff can thrive. Given the discipline's commitment to designing inclusive and equitable spaces, Architecture education has a particular responsibility to exemplify these principles in its own educational environments and curriculum.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "institutions"
  addressee: provider
  verbs: ["adopt"]
  about: "holistic approaches to accessibility"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Institutions should take integrated, whole approaches to accessibility that support success, moving past basic compliance towards environments where all students and staff thrive, a duty the subject carries with special weight given its commitment to inclusive design."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of an Architecture degree", "Accessibility and the needs of disabled students"] }
  span: { start: 21911, end: 22225 }
  source: "1.17 Managing individual needs within group settings can create conflicting requirements. Providers should therefore develop clear oversight frameworks to support equitable and transparent decision making in such scenarios, thereby contributing to the teaching of emotional literacy to students of all neurotypes.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["develop"]
  about: "oversight frameworks for conflicting needs in groups"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Different individual needs in a group can conflict; providers should therefore develop clear oversight frameworks for fair, open decisions in such cases, which also helps teach emotional literacy to students of every neurotype."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of an Architecture degree", "Accessibility and the needs of disabled students"] }
  span: { start: 22225, end: 22674 }
  source: "1.18 The physical environment also plays a critical role in supporting neurodivergent students. Environmental aspects, such as lighting, acoustics, visual clutter and breakout spaces, might be particularly disabling for neurodivergent students who spend significant time in studio spaces during their studies. Course teams should take into consideration making reasonable adjustments to physical environments that adversely affect disabled students."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course teams"
  addressee: provider
  verbs: ["take"]
  about: "reasonable adjustments to the physical studio"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The physical setting matters for neurodivergent students, who spend long periods in studio, where lighting, acoustics, clutter and a lack of breakout space can be disabling; course teams should consider reasonable adjustments to physical settings that harm disabled students."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.21
  locator: { number: "1.21", headingPath: ["Context and purposes of an Architecture degree", "Education for sustainable development"] }
  span: { start: 24060, end: 24882 }
  source: "1.21 Sustainability in Architecture encompasses a broad, complex and interconnected set of concerns. It is a field that is constantly evolving, and curricula should make space for students to critically engage with the concept of sustainability, its limitations and emergent alternative approaches. Education for Sustainable Development enables learners to think critically and take informed decisions, building confidence with complexity and promoting a culture of ongoing learning. This enables students to question and explore the challenges, complexities and contradictions of sustainability, to both local and global scenarios and their crossovers. It invites critical reflection about long-term practices and evolving approaches that meet the needs of current and future life while respecting ecological boundaries.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "curricula"
  addressee: provider
  verbs: ["make"]
  about: "critical engagement with sustainability"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Sustainability in architecture is broad, complex and changing, so curricula should give students room to examine the idea critically, including its limits and new alternative approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of an Architecture degree", "Education for sustainable development"] }
  span: { start: 25407, end: 26047 }
  source: "1.23 A firm foundation for knowledge about climate literacy, competence and capability will be holistically nurtured across the creative, cultural, technical and professional dimensions of the discipline. Tailoring pedagogy and course content toward real-world applications through opportunities within the curricula enables holistic integration of regenerative practice and can encourage innovative and experimental approaches. Schools can consider how predictive tools such as environmental or energy modelling, building performance evaluation and whole life carbon assessment can be integrated to test and inform design decision-making.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses in the subject and their students"
  addressee: both
  verbs: ["nurtured"]
  about: "climate literacy built across the course"
  themes: [theme:esd]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Grounding in climate literacy, competence and capability will be developed across the creative, cultural, technical and professional sides of the subject, helped by real-world applications and by predictive tools that test design decisions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/1.25
  locator: { number: "1.25", headingPath: ["Context and purposes of an Architecture degree", "Education for sustainable development"] }
  span: { start: 26732, end: 27020 }
  source: "1.25 Providers should strive to lead by example, working with their student bodies to continuously review and refine their ESD practices. By modelling environmental and ethical practices, schools can inspire students to adopt similar applications in their professional and personal lives."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["strive", "lead"]
  about: "providers modelling sustainable practice"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Providers should try to lead by example, reviewing and improving their sustainability education practice with their students; modelling environmental and ethical practice lets schools encourage students to do the same at work and at home."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.31
  locator: { number: "1.31", headingPath: ["Context and purposes of an Architecture degree", "Situated learning for EEE"] }
  span: { start: 30571, end: 31193 }
  source: "1.31 Where placements are offered, providers' career teams and services connect students with job opportunities, while Architecture schools value leverage of alumni and practitioner networks for more targeted placements. Here, we define a placement as a period of credit- rated practice work that is undertaken during an undergraduate or master's programme. During a placement, schools have an ethical responsibility to ensure that students are not exposed to poor working practices. Additionally, providers should strive to ensure all students receive equal support in finding a placement, to create inclusive practices.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers and schools"
  addressee: provider
  verbs: ["strive", "ensure"]
  about: "fair support in finding placements"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Placements, defined as credit-rated periods of practice work within an undergraduate or master's course, carry an ethical duty on schools to protect students from poor working practice, and providers should try to give every student equal support in finding one."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.35
  locator: { number: "1.35", headingPath: ["Context and purposes of an Architecture degree", "Situated learning for EEE"] }
  span: { start: 33044, end: 33810 }
  source: "1.35 Architecture education is well placed to embed live projects within the core curriculum, grounding student learning in authentic, real-world challenges and scenarios and preparing them for practice. It enables students to develop professional competencies while within education, and bridge academic learning with practical application. Innovation often emerges during these projects through material testing, prototype building and virtual simulation, all supporting enterprise and entrepreneurship education. Live projects involving field trips and community engagement will need to address risk, ethical implications and student accessibility concerns. When appropriate, engaging students in these processes supports authentic learning and employment skills."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "live projects"
  addressee: provider
  verbs: ["address"]
  about: "risk and ethics in live projects"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Live projects in the core curriculum ground learning in real challenges and support enterprise; those involving field trips and community work will need to deal with risk, ethical implications and accessibility for students."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.37
  locator: { number: "1.37", headingPath: ["Context and purposes of an Architecture degree", "Generative artificial intelligence"] }
  span: { start: 34296, end: 35016 }
  source: "1.37 Architecture education will need to include knowledge and understanding on GenAI use in industry. This should cover the ethical, sustainable, intellectual property (IP) and\n\n10\nGeneral Data Protection Regulation (GDPR) implications of its use, the potential for bias and discrimination in models trained on historical or synthetic datasets, and the potential means to mitigate these issues. In this context, careful consideration should be given by providers to the development of students' critical thinking skills when evaluating the reliability of GenAI outputs, and to clearly articulate the processes, reasoning and methodologies underpinning the prompting and refinement of the tools that contribute to them.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["include", "cover"]
  about: "teaching about GenAI and its implications"
  themes: [theme:genai]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Architecture education will need to cover how GenAI is used in industry, which should include its ethical, sustainability, intellectual property and data protection implications, bias in models and ways to reduce it; providers should attend to students' critical judgement of GenAI outputs and their ability to explain how they prompted and refined the tools."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.38
  locator: { number: "1.38", headingPath: ["Context and purposes of an Architecture degree", "Generative artificial intelligence"] }
  span: { start: 35016, end: 35644 }
  source: "1.38 Critical and reflective forms of assessment can refocus pedagogic practice, enabling examination of design authorship and process transparency. These include verbal and non- verbal critical reasoning, integration of technical problem-solving exercises within real-world contexts, and evaluation of experiential learning activities. GenAI may be employed as a facilitative tool within these processes, enabling exploration and iteration rather than serving as an end in itself. Courses should continue to promote speculative, analytical, research- informed and novel working methodologies in studio-based design assessment.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses"
  addressee: provider
  verbs: ["continue", "promote"]
  about: "research-informed methods in studio assessment"
  themes: [theme:genai]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Critical and reflective assessment can expose design authorship and process, with GenAI used as an aid to exploration rather than an end; courses should keep encouraging speculative, analytical, research-informed and novel ways of working in studio design assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/1.40
  locator: { number: "1.40", headingPath: ["Context and purposes of an Architecture degree", "Generative artificial intelligence"] }
  span: { start: 36533, end: 36840 }
  source: "1.40 Providers should ensure that GenAI technology is implemented to promote inclusivity, rather than amplify privilege, and so careful thought over the teaching of and cost impact for students using specialist GenAI tools for compulsory work need to be considered before establishing briefing requirements."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["ensure"]
  about: "inclusive and affordable use of GenAI"
  themes: [theme:genai]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Providers should make sure GenAI is introduced in a way that promotes inclusion rather than amplifying privilege, weighing the teaching needed and the cost to students before requiring specialist tools for compulsory work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of the Architecture course", "Curriculum design"] }
  span: { start: 36913, end: 37248 }
  source: "2.1 Curriculum design should remain sufficiently flexible to incorporate emerging knowledge and techniques (such as regulatory changes, digital fabrication, sustainable design methods and artificial intelligence) so that students engage with the nature of Architecture as both an academic discipline and as a fast-evolving profession.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "curriculum design"
  addressee: provider
  verbs: ["remain", "incorporate"]
  about: "a curriculum open to emerging knowledge"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Curriculum design should stay flexible enough to take in new knowledge and techniques, such as regulatory change, digital fabrication, sustainable methods and artificial intelligence, so students meet the subject as both an academic discipline and a fast-changing profession."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/2.2
  locator: { number: "2.2", headingPath: ["Distinctive features of the Architecture course", "Curriculum design"] }
  span: { start: 37248, end: 37865 }
  source: "2.2 An architectural education incorporates lifelong learning and continuous professional development. While many students aim to become registered architects, programmes are typically designed to enable graduates to pursue a range of career paths or further study – course design should therefore instil research and creativity that underpins progression to these routes and emerging career paths. Evolving, enhancing and enabling transferable skills support students to be ready for these emerging opportunities or changes in career choice. This includes hard and soft skills being transparent to the student body.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course design"
  addressee: provider
  verbs: ["instil", "underpins"]
  about: "research and creativity for varied careers"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The education builds in lifelong learning and professional development, and since courses often prepare students for varied careers or further study, course design should instil the research and creativity that support those and new routes, with transferable skills made visible to students."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of the Architecture course", "Curriculum design"] }
  span: { start: 37865, end: 38430 }
  source: "2.3 Undergraduates studying Architecture courses as part of a combined or joint degree with other subjects (including courses that specify major and minor options) will achieve core elements of the threshold standards outlined in this Statement and will add others according to the areas covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating opportunities for interdisciplinary study. Inter, trans and cross-disciplinary experience in education support transferability in career choice.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduates on combined or joint degrees"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "core threshold standards in joint and combined degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Undergraduates taking architecture in a combined or joint degree will reach the core elements of the threshold standards here and will add others from the areas their other subject covers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of the Architecture course", "Curriculum design"] }
  span: { start: 38430, end: 38795 }
  source: "2.4 In designing Architecture courses, providers should take account of PSRB requirements (notably ARB and RIBA) for minimum expected content within and across modules. Provision should ensure a wide educational experience that encourages experimentation, critical investigation and intellectual development beyond compliance with threshold regulatory requirements."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers designing courses"
  addressee: provider
  verbs: ["take"]
  about: "PSRB content requirements and wider experience"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "In designing courses, providers should take account of what the professional bodies, chiefly ARB and RIBA, require as minimum content, while giving a broad education that encourages experiment, critical investigation and intellectual growth past mere compliance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of the Architecture course", "Progression"] }
  span: { start: 40760, end: 41160 }
  source: "2.9 Practical experience or study abroad opportunities that take place in the duration of a course should be suitably monitored by the provider. Progression pathways should consider individual student needs. Where appropriate, reasonable adjustments should be put in place to align a student's experience and learning with equitable, diverse and inclusive measures (as noted in paragraphs 1.12-1 8).\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["monitored", "consider", "put"]
  about: "monitoring practice and study abroad; adjustments"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Practical experience or study abroad within a course should be properly monitored by the provider, progression routes should consider individual needs and reasonable adjustments should, where fitting, align each student's experience with equitable and inclusive measures."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of the Architecture course", "Progression"] }
  span: { start: 41160, end: 41554 }
  source: "2.10 Increasingly, alternative pathways such as Architect (integrated degree) L7 and Architectural Assistant (Integrated Degree) L6 Apprenticeships offer an integrated route to studying a RIBA validated Part 2 and 3 combined or Part 1 undergraduate course respectively. Providers should refer to requirements from the relevant national apprenticeship trailblazer groups to explore these routes."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["refer", "explore"]
  about: "apprenticeship routes to the subject"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Apprenticeships at Level 7 (Architect) and Level 6 (Architectural Assistant) now offer integrated routes to RIBA-validated Part 2 and 3 or Part 1 courses; providers should consult the national trailblazer groups' requirements when exploring them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/2.15
  locator: { number: "2.15", headingPath: ["Distinctive features of the Architecture course", "Flexibility"] }
  span: { start: 43112, end: 43467 }
  source: "2.15 Courses should be designed with inclusivity and accessibility in mind. Institutions may offer a range of delivery modes and pathways to suit different student circumstances. Courses that are offered full-time or part-time, in-person through campus-based studio teaching, or via blended and online learning components can improve access for students.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses"
  addressee: provider
  verbs: ["designed"]
  about: "inclusive and accessible course design"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses should be designed with inclusion and accessibility in mind, and institutions may offer varied modes and routes, full-time, part-time, in-person or blended, to widen access."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of the Architecture course", "Partnerships"] }
  span: { start: 44802, end: 45773 }
  source: "2.19 Providers may engage in national or international strategic partnerships for delivering their courses. This can include franchised or validated provision, where Architecture is delivered at a partner institution under the oversight of the degree-awarding body. Partnerships can be accompanied by articulation agreements that allow students from another institution (in the UK or abroad) advanced entry into a specified programme. They can also be characterised by transnational education arrangements, such as offshore campuses, exchanges, placements or joint degrees with international higher education providers. In developing such partnership models, providers must ensure that the quality and standards of an Architecture degree remain consistent and that students, regardless of location or context, achieve the benchmarks set out in this Statement. Providers may benefit from consulting the Quality Code Advice and Guidance on Partnerships for further detail.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must
  level: none
  appliesTo: "providers in partnerships"
  addressee: provider
  verbs: ["ensure", "achieve"]
  about: "consistent quality and standards in partnerships"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Providers may deliver through national or international partnerships, including franchise, validation, articulation and transnational arrangements; when they do they must ensure the quality and standards of the degree stay consistent and that every student, wherever based, reaches the standards this statement sets."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/2.20
  locator: { number: "2.20", headingPath: ["Distinctive features of the Architecture course", "Partnerships"] }
  span: { start: 45773, end: 46294 }
  source: "2.20 Partnerships can take several forms, from formal collaborative delivery of a course (for example, another academic institution, community organisation or industry), through to less formal arrangements (that bring in placement opportunities and external expertise for reciprocal learning). In all cases, this Statement and its standards should be applied to ensure that a qualification involving partnerships is designed and managed such that the benchmark academic outcomes are achieved across the entire programme.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "partnered qualifications"
  addressee: provider
  verbs: ["applied"]
  about: "applying the standards across partnered awards"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Partnerships range from formal joint delivery to looser arrangements; in all of them the statement and its standards should be applied so that a partnered award reaches the expected outcomes across the whole programme."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/2.24
  locator: { number: "2.24", headingPath: ["Distinctive features of the Architecture course", "Monitoring and review"] }
  span: { start: 48328, end: 48960 }
  source: "2.24 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers as part of periodic review to gain an independent perspective on any proposed changes and ensure threshold standards are achieved, and content is appropriate for the subject. Periodic reviews and annual monitoring reports support an in-depth evaluation of the course, often involving external panel members and independent advisers to provide objective perspectives. Outcomes are used to inform future planning to ensure that programmes continue to deliver positive outcomes aligned with benchmark standards."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["use", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Externality is central to UK quality assurance: providers will use external reviewers in periodic review for an independent view on changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/2.32
  locator: { number: "2.32", headingPath: ["Distinctive features of the Architecture course", "External examiners"] }
  span: { start: 52402, end: 52739 }
  source: "2.32 Monitoring and review processes can ensure that important cross-cutting themes are embedded throughout the curriculum. Architecture programmes should reflect these themes in design, content and delivery. Programme reviews provide the opportunity to evaluate how successfully themes are interwoven in the student learning experience."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "programmes"
  addressee: provider
  verbs: ["reflect"]
  about: "the cross-cutting themes in design, content and delivery"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Monitoring and review can make sure the cross-cutting themes run through the curriculum; programmes should reflect them in design, content and delivery, and reviews are the chance to judge how well they are woven in."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/3.2
  locator: { number: "3.2", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 53140, end: 53742 }
  source: "3.2 The taxonomy of literacies provides a thematic framework through which the diverse subjects and components that make up the curriculum can be organised and understood. This provides a framework connecting professional body requirements to learning, teaching and assessment strategies. The literacies should not be seen as discrete or isolated but as interdependent and overlapping, reflecting the integrative nature of architectural thinking and practice. Literacies can also provide a tool for meaningful engagement with non-specialist audiences to support good communication with diverse voices.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the taxonomy of literacies and those who use it"
  addressee: both
  verbs: ["seen"]
  about: "reading the literacies as overlapping"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The taxonomy offers a thematic frame linking professional body requirements to learning, teaching and assessment; the literacies should be read as interdependent and overlapping rather than discrete, and they help communication with non-specialists."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 53742, end: 54237 }
  source: "3.3 On completing a course in Architecture, a graduate is expected to have acquired the following literacies: 1) design literacy 2) visual and spatial literacy 3) cultural and contextual literacy 4) climate and ecological literacy 5) technical and building environment literacy 6) digital literacy 7) research and enquiry-based literacy 8) ethical and professional literacy 9) practice and business literacy 10) financial and economic literacy 11) emotional literacy 12) communication literacy.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: none
  appliesTo: "graduates of a course in the subject"
  addressee: learner
  verbs: ["acquired"]
  about: "the twelve literacies named"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "On completing a course, a graduate is expected to have gained twelve literacies: design; visual and spatial; cultural and contextual; climate and ecological; technical and building environment; digital; research and enquiry; ethical and professional; practice and business; financial and economic; emotional; and communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/3.22
  locator: { number: "3.22", headingPath: ["Content, structure and delivery", "Studio pedagogy"] }
  span: { start: 65585, end: 65946 }
  source: "3.22 The studio supports an iterative and reflective process of drawing/sketching and modelling. Students hone their skills through experimentation, testing ideas, risk-taking and failure as part of a design and a pedagogical process. Portfolios for assessment should reflect both the process and outcomes of studio design projects as set out in paragraph 3.40."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "portfolios for assessment"
  addressee: provider
  verbs: ["reflect"]
  about: "portfolios showing process and outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Studio supports an iterative, reflective cycle of drawing and modelling in which experiment, risk and failure belong to the process; portfolios for assessment should show both the process and the results of studio projects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/3.23
  locator: { number: "3.23", headingPath: ["Content, structure and delivery", "Resources"] }
  span: { start: 65957, end: 66983 }
  source: "3.23 As a space for drawing and making, a studio needs to be well-lit and provide adequate space for students to work on large models. In addition to accessing equipment that supports traditional processes and production, students also require access to the digital tools now integral to design processes and employed across industry. Access to power supply and to Wi-Fi networks are standard in studios, and, ideally, students should be able to easily access large format printing and specialist making facilities. Students should be able to store their belongings and work-in-progress securely. Ideally, students will be provided with a dedicated space sufficient to allow them to work within the studio environment for the duration of their design projects. Where access to a physical studio is not possible, programmes may employ tactics designed to replicate some or all of its characteristics, including the use of digital platforms which enable students to collaborate and share their work with their peers and tutors.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "studio provision"
  addressee: provider
  verbs: ["access", "store"]
  about: "studio facilities students need"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A studio needs good light and room for large models, and students need digital tools used across industry; ideally they should easily reach large-format printing and making facilities, and they should be able to store belongings and work securely, with digital substitutes where a physical studio is impossible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/3.33
  locator: { number: "3.33", headingPath: ["Content, structure and delivery", "Specialist, research and practice-informed teaching"] }
  span: { start: 71874, end: 72675 }
  source: "3.33 An understanding of context, including, but not limited to, the physical environment, is fundamental to the study (and production) of architecture. Learning-in-context through study and site visits – which may be local, within the UK, or further afield – can offer students an invaluable opportunity to experience a wide range of contrasting cultural contexts. This includes observing and studying buildings in progress on construction sites, and engagement with broader professional contexts. While study visits are advantageous, programmes should be mindful of both the potential environmental impacts around air transport and EDI impacts where extended study visits may be unaffordable for some and may disadvantage students with external commitments and responsibilities (see paragraph 1.10)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "programmes"
  addressee: provider
  verbs: ["mindful"]
  about: "environmental and EDI effects of study visits"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Context is fundamental to studying architecture, and site and study visits offer contrasting settings, but programmes should keep in mind the environmental impact of flying and that long visits may be unaffordable or exclude students with outside commitments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/3.34
  locator: { number: "3.34", headingPath: ["Content, structure and delivery", "Reviews"] }
  span: { start: 72684, end: 74009 }
  source: "3.34 A review is an opportunity for immediate and direct feedback and supports students in gaining confidence and skills to present work to new audiences – a standard activity in industry. Students commonly present their design work (finished or ongoing) for wider discussion. This usually takes the form of digital or physical drawings and models accompanied by a verbal or pre-recorded project explanation and followed by a discussion between a mix of students, peers, educators and practitioners. Students can benefit from the insight of both their peers, tutors and visiting specialists or professional practitioners. They learn how to listen and respond to critical feedback – a form of critical reflection with others which may enable them to progress their work in new and unexpected directions. The requirement to present work succinctly supports the development of visual as well as verbal communication skills and literacy. Providers will need to ensure non-visual and non-verbal alternatives are offered as alternative forms of learning and assessment where required. Reviews can also punctuate what may be an extended design process. This supports stretched feedback and formative assessment at key stages of a project, helping students manage their workload and creating structured opportunities for reflection.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["ensure", "offered"]
  about: "non-visual and non-verbal alternatives to reviews"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Reviews give immediate feedback and build students' confidence to present to new audiences; providers will need to make sure non-visual and non-verbal alternatives are available as other forms of learning and assessment where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/3.36
  locator: { number: "3.36", headingPath: ["Content, structure and delivery", "Reviews"] }
  span: { start: 74867, end: 75836 }
  source: "3.36 Best practice case studies include more student-centred review formats which can incorporate methods and procedures which respect diversity and accessibility concerns. These include grouping student presentations; changing the methods used for presentation and for giving feedback to prioritise peer discourse (supplemented by written feedback) and changing the spatial layout. The use of online platforms for the presentation and discussion of student work can also provide more accessibility for disadvantaged learners, allowing for remote participation and minimising the additional costs usually faced by students. In all these examples, the dynamics of interaction may vary while the principle of open,\n\n22\nconstructive discourse centred around students' ideas remains core. Schools should ensure that staff have carefully considered the format and scope of reviews and been given appropriate guidance to design and support an inclusive learning environment.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "schools"
  addressee: provider
  verbs: ["ensure"]
  about: "staff preparation for inclusive reviews"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Student-centred review formats, such as grouped presentations, peer-led discussion with written feedback, changed layouts and online platforms, can respect diversity and access; schools should make sure staff have thought through review format and scope and been guided to support an inclusive environment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/3.37
  locator: { number: "3.37", headingPath: ["Content, structure and delivery", "Reviews"] }
  span: { start: 75836, end: 76521 }
  source: "3.37 Where reviews are used as part of a summative assessment, particular care should be taken to ensure that individuals or student groups are not subject to specific disadvantage. A combination of visual and verbal presentation has some parallels in professional practice and may therefore be appropriate in some instances; however, students may be disadvantaged by differential conditions and unduly impacted by the stress associated with an in-person presentation for examination. Alternative forms of assessment will need to be considered in these circumstances. It is recommended that providers offer guidance to educators on giving appropriate inclusive and supportive feedback."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "summative assessment by review"
  addressee: provider
  verbs: ["taken", "considered"]
  about: "reviews in summative assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Where reviews count towards summative assessment, care should be taken that no individual or group is disadvantaged; since in-person presentation can unduly affect some students, alternative assessment will need to be considered, and providers are recommended to guide educators on inclusive feedback."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/3.40
  locator: { number: "3.40", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 77773, end: 78695 }
  source: "3.40 Courses can use multiple types of assessment tasks depending on the learning being assessed. For example, portfolios, presentations, exhibitions, illustrated reports, live builds, physical models, essays and exams. It is important for a learner to capture their design process to show their critical thinking and reflection. This will be increasingly important with the increased use of Generative AI. Examples of assessment tasks that support this are iteration logbooks, decision rationales, reflective commentary and critique-response narratives. Presentations can take the form of tabletop reviews or open panels. Both can include external panel members from other providers, professional practices, project stakeholders and peers. Care should be taken to ensure that external panel members have been given guidance on appropriate conduct and feedback during reviews to support an inclusive learning environment.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment with external panels"
  addressee: provider
  verbs: ["taken", "ensure"]
  about: "guidance for external panel members"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses can use many kinds of assessment task, and capturing the design process matters more as Generative AI spreads; care should be taken that external panel members are guided on conduct and feedback in reviews so the environment stays inclusive."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/3.44
  locator: { number: "3.44", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 80321, end: 80845 }
  source: "3.44 Consideration of the space and set-up of any assessment should be appropriate for the nature of architectural work and suitable for all, whether for an exam or live presentation. Alternative spaces should be offered where required to support students with different learning needs – such as a prerecorded presentation or quiet classroom. Most courses will require studio space to be set aside for collective assessment practice to allow physical submissions, such as model making, hand drawings and exhibition formats.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment arrangements"
  addressee: provider
  verbs: ["offered"]
  about: "alternative assessment spaces"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The space and set-up for any assessment should suit architectural work and all students; alternative spaces, such as a recorded presentation or a quiet room, should be offered where needed, and most courses will need studio space for collective assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/3.45
  locator: { number: "3.45", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 80845, end: 81360 }
  source: "3.45 Group and team working is an integral part of work within architectural practice and inclusion within the curriculum can offer a valuable teaching and learning experience. Students should be encouraged to take advantage of group working opportunities when they are made available. Assessment tasks can include collective and individual contributions and offer the chance for each student to reflect or interpret feedback gathered through group work to demonstrate an understanding from collaborative learning.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "students and those who teach them"
  addressee: both
  verbs: ["encouraged"]
  about: "taking up group working"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Group working is integral to architectural practice and valuable in the curriculum; students should be encouraged to use group work when offered, and assessment can combine collective and individual contributions with reflection on feedback from group work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.1
  locator: { number: "4.1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 82290, end: 82974 }
  source: "4.1 This Subject Benchmark Statement sets out the minimum standards (in this case, literacies) that a student will have demonstrated when they are awarded an honours degree in Architecture and a master's degree in Architecture. For a student to be awarded an integrated master's degree in Architecture they will have met the requirements for an honours degree before completing a year of study or equivalent credit at Level 7 FHEQ/Level 11 FQHEIS in order to fulfil the requirements for an integrated master's award. Demonstrating these literacies over time will show that a student has achieved the range of knowledge, understanding and skills expected of graduates in Architecture.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "students awarded the degrees covered"
  addressee: learner
  verbs: ["demonstrated", "met", "completing"]
  about: "the minimum standards and the integrated master's route"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The statement sets minimum standards, as literacies, that a student will have shown when awarded an honours or a master's degree in architecture; an integrated master's student will have met the honours requirements before completing a year or its credit at FHEQ Level 7 or FQHEIS Level 11."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 82974, end: 83449 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["refer"]
  about: "evidence of achievement above the minimum"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Most students will perform well above the minimum; each provider sets its own way of judging evidence of this and should refer to Annex D of the Frameworks, which describes the four honours classifications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 83449, end: 83918 }
  source: "4.3 Please note that the minimum standards are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards (as defined by the Equality Act 2010) as part of a programme specification, these can be informed by the relevant Subject Benchmark Statement along with any PSRB requirements. In these circumstances providers should follow the most recent guidance from the Equality and Human Rights Commission.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["follow"]
  about: "competence standards and EHRC guidance"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The minimum standards are not universal competence standards; a provider that develops competence standards under the Equality Act 2010 may draw on the statement and PSRB requirements and should follow the latest Equality and Human Rights Commission guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/4.5
  locator: { number: "4.5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 84497, end: 84951 }
  source: "4.5 As noted in section 1 and under 'Partnerships' in section 2 (paragraphs 2.18-2.22) many Architecture degrees are recognised by two UK PSRBs – the Architects Registration Board (ARB) and the Royal Institute of British Architects (RIBA). For degrees that are recognised by a PSRB, themes, values, attributes and/or outcomes, as defined by the professional bodies to support development of competences required for professional registration, will apply."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "degrees recognised by a PSRB"
  addressee: provider
  verbs: ["apply"]
  about: "PSRB outcomes for recognised degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Many architecture degrees are recognised by ARB and RIBA; for those degrees, the themes, values, attributes and outcomes the bodies define for professional registration will apply."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architecture-2026/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Bachelor's level minimum standards"] }
  span: { start: 85276, end: 85724 }
  source: "1) Design literacy: the ability to conceive and develop architectural design proposals of moderate complexity, evidencing a process that integrate spatial, artistic, aesthetic, environmental and technical considerations. This encompasses critical and creative thinking, theoretical and practical responses and iterative design processes. Design\n\n25\nliteracy enables students to respond to briefs with contextual sensitivity and technical coherence."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the bachelor's degree with honours"
  addressee: learner
  verbs: ["conceive", "develop", "respond"]
  about: "conceiving and developing design proposals"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to conceive and develop architectural proposals of moderate complexity through an iterative process that brings together spatial, artistic, aesthetic, environmental and technical concerns, thinking critically and creatively and answering a brief with sensitivity to context and technical coherence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Bachelor's level minimum standards"] }
  span: { start: 85725, end: 85996 }
  source: "2) Visual and spatial literacy: the ability to conceive, interpret, manipulate and communicate spatial and visual information through drawings and models, to support the evolution of coherent design proposals that encompass spatial relationships and material assemblages."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the bachelor's degree with honours"
  addressee: learner
  verbs: ["conceive", "interpret", "manipulate", "communicate", "support"]
  about: "working with spatial and visual information"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to conceive, read, shape and convey spatial and visual information in drawings and models so that a coherent design develops, covering spatial relationships and how materials come together."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Bachelor's level minimum standards"] }
  span: { start: 85997, end: 86397 }
  source: "3) Cultural and contextual literacy: the ability to understand and critically engage with the cultural, historical, theoretical, artistic and social contexts that shape architecture. This includes analysing precedents to inform design thinking and pedagogy. Contextual literacy is underpinned with historical and theoretical knowledge from a mixture of global cultures, places and periods of history."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the bachelor's degree with honours"
  addressee: learner
  verbs: ["understand", "engage", "analysing", "inform"]
  about: "the cultural and historical contexts of architecture"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to understand and engage critically with the cultural, historical, theoretical, artistic and social settings that shape architecture, analysing precedents to inform design, grounded in history and theory drawn from many cultures, places and periods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Bachelor's level minimum standards"] }
  span: { start: 86398, end: 86679 }
  source: "4) Climate and ecological literacy: knowledge of the principles of climate change, biodiversity loss, environmental impact, and regenerative design strategies. This includes knowledge of the importance of responsible material specification, energy efficiency, and ethical sourcing."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the bachelor's degree with honours"
  addressee: learner
  verbs: []
  about: "principles of climate change and regenerative design"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know the principles of climate change, loss of biodiversity, environmental impact and regenerative design strategies, including why responsible specification of materials, energy efficiency and ethical sourcing matter."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Bachelor's level minimum standards"] }
  span: { start: 86680, end: 87209 }
  source: "5) Technical and building environment literacy: knowledge of construction systems, building physics, building pathology, materials, environmental technologies and their application in quantitative and qualitative design processes. Technical literacy includes knowledge of the principles of life safety, fire safety, accessibility and inclusive design. This enables students to integrate strategies that meet appropriate performance standards. These skills can be applicable to conservation, adaptive reuse and new build projects."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the bachelor's degree with honours"
  addressee: learner
  verbs: ["integrate", "meet"]
  about: "construction, building physics and life safety"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know construction systems, building physics and pathology, materials and environmental technologies and how to use them in quantitative and qualitative design work, including the principles of protecting life, fire safety, access and inclusive design, so as to integrate strategies that meet suitable performance standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Bachelor's level minimum standards"] }
  span: { start: 87210, end: 87422 }
  source: "6) Digital literacy: the ability to use digital tools and technologies in architectural design, evaluation and communication, and an awareness of how Generative artificial intelligence can be applied in practice."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the bachelor's degree with honours"
  addressee: learner
  verbs: ["use", "applied"]
  about: "digital tools and awareness of GenAI"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to use digital tools and technologies to design, evaluate and communicate architecture, and will be aware of how Generative artificial intelligence can be used in practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.6.b7
  locator: { number: "4.6.b7", headingPath: ["Benchmark standards", "Bachelor's level minimum standards"] }
  span: { start: 87423, end: 87626 }
  source: "7) Research and enquiry-based literacy: an understanding of architectural research methods and their role in supporting innovation-informed decision-making and the advancement of architectural knowledge."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the bachelor's degree with honours"
  addressee: learner
  verbs: ["supporting"]
  about: "research methods in architecture"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will understand the research methods of architecture and how they support decisions informed by innovation and the growth of the discipline's knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.6.b8
  locator: { number: "4.6.b8", headingPath: ["Benchmark standards", "Bachelor's level minimum standards"] }
  span: { start: 87627, end: 87917 }
  source: "8) Ethical and professional literacy: knowledge about codes of conduct, and the principles associated with equity, diversity, inclusion and accessibility. This includes an understanding of the ethical implications of architectural decisions on society, the environment and social wellbeing."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the bachelor's degree with honours"
  addressee: learner
  verbs: []
  about: "codes of conduct and the ethics of design decisions"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know professional codes of conduct and the principles of equity, diversity, inclusion and accessibility, and understand the ethical effects of design decisions on society, the environment and wellbeing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.6.b9
  locator: { number: "4.6.b9", headingPath: ["Benchmark standards", "Bachelor's level minimum standards"] }
  span: { start: 87918, end: 88261 }
  source: "9) Practice and business literacy: knowledge of the principles of the professional, legal, and business contexts of architecture. This includes the principles of project management, procurement, contracts, policy, financial planning and cost management. It also includes knowledge of planning systems, building codes and regulatory compliance."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the bachelor's degree with honours"
  addressee: learner
  verbs: []
  about: "the professional, legal and business context"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know the principles of the professional, legal and business setting of architecture, including managing projects, procurement and contracts, policy, financial planning and cost control, planning systems, building codes and compliance with regulation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.6.b10
  locator: { number: "4.6.b10", headingPath: ["Benchmark standards", "Bachelor's level minimum standards"] }
  span: { start: 88262, end: 88456 }
  source: "10) Financial and economic literacy: awareness of how the design proposals and longevity of a project are influenced and impacted by financial and economic mechanisms, both locally and globally."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the bachelor's degree with honours"
  addressee: learner
  verbs: ["influenced", "impacted"]
  about: "financial and economic forces on projects"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be aware of how financial and economic mechanisms, local and global, shape and affect design proposals and how long a project lasts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.6.b11
  locator: { number: "4.6.b11", headingPath: ["Benchmark standards", "Bachelor's level minimum standards"] }
  span: { start: 88457, end: 88597 }
  source: "11) Emotional literacy: the ability to understand, interpret and collaborate with others for the purpose of designing for another person(s)."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the bachelor's degree with honours"
  addressee: learner
  verbs: ["understand", "interpret", "collaborate"]
  about: "understanding and working with others when designing for them"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to understand, read and work with other people in order to design for someone else."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.6.b12
  locator: { number: "4.6.b12", headingPath: ["Benchmark standards", "Bachelor's level minimum standards"] }
  span: { start: 88598, end: 88968 }
  source: "12) Communication literacy: the ability to clearly and effectively convey architectural ideas through verbal and/or non-verbal, written and visual means. This includes presenting concepts to diverse audiences (for example, discussions with stakeholders,\n\n26\ncollaborators and peers) and producing coherent documentation that supports critical thinking and design intent."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the bachelor's degree with honours"
  addressee: learner
  verbs: ["convey", "presenting", "producing"]
  about: "communicating ideas to varied audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to put architectural ideas across clearly and effectively by spoken or other means, in writing and visually, presenting to varied audiences and producing coherent documents that support critical thinking and design intent."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Master's level minimum standards"] }
  span: { start: 89276, end: 89884 }
  source: "1) Design literacy: the ability to conceive, develop and resolve complex architectural design proposals, evidencing a process and methodology that integrate spatial, artistic, aesthetic, environmental and technical considerations. This encompasses critical and creative thinking, strategic thinking, theoretical and practical responses, iterative design processes and the synthesis of diverse knowledge domains through studio-based learning. Design literacy enables students to respond to briefs with originality, contextual sensitivity and technical coherence, applying systems thinking to design questions."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's degree"
  addressee: learner
  verbs: ["conceive", "develop", "resolve", "respond", "applying"]
  about: "resolving complex design proposals"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to conceive, develop and resolve complex architectural proposals through a deliberate process and method that brings together spatial, artistic, aesthetic, environmental and technical concerns, thinking strategically as well as critically and creatively, synthesising varied knowledge in studio and answering a brief with originality and systems thinking."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Master's level minimum standards"] }
  span: { start: 89885, end: 90286 }
  source: "2) Visual and spatial literacy: the ability to conceive, develop and articulate sophisticated spatial relationships and material expressions through drawing, modelling and making. This literacy encompasses the evolution of a considered architectural language which enables students to craft coherent, inhabitable spaces and spatial and material assemblages that demonstrate conceptual rigor and skill."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's degree"
  addressee: learner
  verbs: ["conceive", "develop", "articulate", "craft", "demonstrate"]
  about: "sophisticated spatial and material expression"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to conceive, develop and express sophisticated spatial relationships and material qualities through drawing, modelling and making, evolving a considered architectural language that produces coherent, habitable spaces showing rigour and skill."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Master's level minimum standards"] }
  span: { start: 90287, end: 90762 }
  source: "3) Cultural and contextual literacy: the ability to understand and critically engage with the cultural, historical, theoretical, artistic and social contexts that shape architecture. This includes analysing narratives, values and precedents to inform design thinking and pedagogy. Contextual literacy is underpinned with historical and theoretical knowledge from a mixture of global cultures, places and periods of history, and an understanding of social and climate justice."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's degree"
  addressee: learner
  verbs: ["understand", "engage", "analysing", "inform"]
  about: "cultural contexts, narratives and social and climate justice"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to understand and engage critically with the cultural, historical, theoretical, artistic and social settings of architecture, analysing narratives, values and precedents to inform design, grounded in global history and theory and in an understanding of social and climate justice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Master's level minimum standards"] }
  span: { start: 90763, end: 91127 }
  source: "4) Climate and ecological literacy: understanding of the principles of climate change, biodiversity loss, global environmental impact and regenerative design strategies. This includes understanding the importance of responsible material specification, energy efficiency, waste reduction, ethical sourcing and the application of these principles to design projects."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's degree"
  addressee: learner
  verbs: []
  about: "understanding and applying climate principles in design"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will understand the principles behind climate change, the loss of biodiversity, environmental impact at global scale and regenerative design, why responsible materials, energy efficiency, waste reduction and ethical sourcing matter and how to apply these principles to design projects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Master's level minimum standards"] }
  span: { start: 91128, end: 91665 }
  source: "5) Technical and building environment literacy: understanding of construction systems, building physics, building pathology, materials, environmental technologies and their application in quantitative and qualitative design processes. Technical literacy includes understanding of the principles of life safety, fire safety, accessibility and inclusive design. This enables students to integrate strategies that meet appropriate performance standards. These skills can be applicable to conservation, adaptive reuse and new build projects."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's degree"
  addressee: learner
  verbs: ["integrate", "meet"]
  about: "understanding construction, building physics and life safety"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will understand construction systems, building physics and pathology, materials and environmental technologies and their use in quantitative and qualitative design work, including the principles of protecting life, fire safety, access and inclusive design, so as to integrate strategies meeting suitable performance standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.7.b6
  locator: { number: "4.7.b6", headingPath: ["Benchmark standards", "Master's level minimum standards"] }
  span: { start: 91666, end: 92002 }
  source: "6) Digital literacy: the ability to effectively apply and instrumentalise digital tools and technologies in architectural design, evaluation and communication. This includes knowledge of how BIM, computational design, digital fabrication, virtual reality, data security and Generative artificial intelligence can be applied in practice."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's degree"
  addressee: learner
  verbs: ["apply", "instrumentalise", "applied"]
  about: "applying digital tools, BIM and GenAI"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to apply digital tools and technologies effectively, and put them to work, in design, evaluation and communication, knowing how practice uses BIM, computational design, digital fabrication, virtual reality, generative AI and data security."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.7.b7
  locator: { number: "4.7.b7", headingPath: ["Benchmark standards", "Master's level minimum standards"] }
  span: { start: 92003, end: 92315 }
  source: "7) Research and enquiry-based literacy: an understanding of architectural research methods and their role in supporting innovation-informed decision-making and the\n\n27\nadvancement of architectural knowledge. This includes the ability to apply appropriate methods of research or enquiry-based working to projects."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's degree"
  addressee: learner
  verbs: ["apply"]
  about: "applying research methods to projects"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will understand the research methods of architecture and their part in innovation-informed decisions and the growth of knowledge, and will be able to apply suitable research or enquiry methods to projects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.7.b8
  locator: { number: "4.7.b8", headingPath: ["Benchmark standards", "Master's level minimum standards"] }
  span: { start: 92316, end: 92675 }
  source: "8) Ethical and professional literacy: understanding codes of conduct and the principles associated with equity, diversity, inclusion and accessibility. This includes the principles of advocacy, civic responsibility, climate justice, community engagement and the ethical implications of architectural decisions on society, the environment and social wellbeing."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's degree"
  addressee: learner
  verbs: []
  about: "advocacy, civic responsibility and ethics"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will understand professional codes of conduct and the principles of equity, diversity, inclusion and accessibility, together with advocacy, civic duty, climate justice, community engagement and the ethical effects of design decisions on society, environment and wellbeing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.7.b9
  locator: { number: "4.7.b9", headingPath: ["Benchmark standards", "Master's level minimum standards"] }
  span: { start: 92676, end: 93023 }
  source: "9) Practice and business literacy: understanding of the principles of professional, legal, and business contexts of architecture. This includes the principles of project management, procurement, contracts, policy, financial planning and cost management. It also includes understanding of planning systems, building codes and regulatory compliance."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's degree"
  addressee: learner
  verbs: []
  about: "understanding the professional, legal and business context"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will understand the principles of the professional, legal and business setting of architecture, including managing projects, procurement and contracts, policy, financial planning and cost control, planning systems, building codes and compliance with regulation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.7.b10
  locator: { number: "4.7.b10", headingPath: ["Benchmark standards", "Master's level minimum standards"] }
  span: { start: 93024, end: 93376 }
  source: "10) Financial and economic literacy: understanding of how design proposals and longevity of a project are influenced and impacted by financial and economic mechanisms, both locally and globally. This includes knowledge of core economic principles, and the numeracy skills required to inform decisions on business sustainability and project feasibility."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's degree"
  addressee: learner
  verbs: ["influenced", "impacted", "inform"]
  about: "economics, numeracy and project feasibility"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will understand how financial and economic mechanisms, local and global, shape design proposals and the life of a project, with knowledge of core economic principles and the numeracy needed to judge business sustainability and feasibility."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.7.b11
  locator: { number: "4.7.b11", headingPath: ["Benchmark standards", "Master's level minimum standards"] }
  span: { start: 93377, end: 93762 }
  source: "11) Emotional literacy: the social ability to understand, interpret and collaborate with others for the purpose of designing for another person(s). It encompasses self- awareness, self-regulation and skilled responsiveness within a creative process. The intent is to learn to advocate for others, build teams and improve collective wellbeing through collaborative community engagement."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's degree"
  addressee: learner
  verbs: ["understand", "interpret", "collaborate", "advocate", "build", "improve"]
  about: "emotional and social skills in collaborative design"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have the social ability to understand, read and work with others in order to design for them, including self-awareness, self-regulation and responsive skill in creative work, aiming to speak for others, build teams and improve shared wellbeing through community engagement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architecture-2026/4.7.b12
  locator: { number: "4.7.b12", headingPath: ["Benchmark standards", "Master's level minimum standards"] }
  span: { start: 93763, end: 94188 }
  source: "12) Communication literacy: the ability to clearly and effectively convey complex architectural ideas through verbal and/or non-verbal, written and visual means. This includes presenting concepts to diverse audiences (for example, discussions with stakeholders, collaborators and peers) and producing coherent and critically informed documentation that supports critical thinking, design intent and professional practice.\n\n28"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's degree"
  addressee: learner
  verbs: ["convey", "presenting", "producing"]
  about: "communicating complex ideas and critical documentation"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to put complex architectural ideas across clearly and effectively by spoken or other means, in writing and visually, presenting to varied audiences and producing coherent, critically informed documents that support critical thinking, design intent and professional practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/architecture-2026/1.5
  forPractitioner: { text: "Build the national and devolved differences in governance, law, policy and practice that suit your course's focus into what students learn, since many will work across borders.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.5 as an expectation the statement puts with 'should': courses should reflect how governance, law, policy and practice differ between the UK nations and beyond, to suit their focus. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.5) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.29 on international collaboration, 2.12 on Scottish degree structures and the professional-context items 4.6.b9 and 4.7.b9."
  author-agent-dialogue: "Raise paragraph 1.5 with a programme team or teacher when a team is deciding how much of the curriculum treats regulation and practice across different jurisdictions, framing it as something the course is expected to do. Ask: Which governance and legal settings does your course prepare students to work in, and where in the modules do they meet the differences? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.6
  forPractitioner: { text: "Treat equity, diversity and inclusion as a standing commitment of the provider, reviewed and renewed over time, and make it part of how the school teaches, assesses and engages with the profession, not a separate initiative.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe paragraph 1.6 as a requirement the statement puts with 'must': providers must sustain a reflective commitment to equity, diversity and inclusion, and that commitment should run through the culture and practice of the school. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.6) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.7 to 1.11 on inclusive environments and costs, the ethical and professional literacy items 4.6.b8 and 4.7.b8 and the EDI theme record theme:edi."
  author-agent-dialogue: "Raise paragraph 1.6 with a programme team or teacher when a team reviews how the school addresses who enters and succeeds in the subject, framing it as something the course is expected to do. Ask: Where can you show that your commitment to equity, diversity and inclusion has changed practice in the studio, in assessment or in links with the profession? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.7
  forPractitioner: { text: "Set up a standing, reflective process for spotting and acting on equity and diversity issues, co-design more inclusive curricula and teaching with students and keep improving fair access so every student can progress.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.7 as an expectation the statement puts with 'should': schools should run ongoing reflective processes on equity and diversity and develop more inclusive curricula with students. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.7) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.6 on the provider's commitment, 1.9 on diverse voices and 2.32 on reviewing the themes."
  author-agent-dialogue: "Raise paragraph 1.7 with a programme team or teacher when a team is planning curriculum review or student partnership work, framing it as something the course is expected to do. Ask: How do students take part in shaping a more inclusive curriculum, and how often does the school look again at equity issues? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.9
  forPractitioner: { text: "Keep the studio and wider learning environment inclusive and respectful while open to challenging established views, and widen the range of people students hear from: staff, visiting speakers, reviewers and consultants from inside and outside the field.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.9 as an expectation the statement puts with 'should': schools should keep the environment inclusive and respectful and, where possible, expose students to a wide range of voices. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.9) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.7, 3.21 on practitioners in studio and 3.34 to 3.36 on reviews."
  author-agent-dialogue: "Raise paragraph 1.9 with a programme team or teacher when a team plans visiting critics, guest lectures or review panels, framing it as something the course is expected to do. Ask: Whose voices do your students hear across a year, and who is missing from your reviewers and visiting speakers? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.10
  forPractitioner: { text: "Audit what students pay beyond fees (materials, kit, software, trips) and the time studio culture demands, cut those costs where you can, back fair access to resources and watch for students shut out of work-based learning or practice experience.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.10 as an expectation the statement puts with 'should': schools should recognise and reduce the extra costs of studying the subject and the unequal access some groups have to work-based learning. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.10) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.40 on the cost of GenAI tools, 3.26 on equitable access to hardware and software and 3.33 on study visits."
  author-agent-dialogue: "Raise paragraph 1.10 with a programme team or teacher when a team sets project briefs, model-making demands, software requirements or study trips, framing it as something the course is expected to do. Ask: What does a student spend beyond fees to complete your briefs, and which students cannot take part fully because of cost or outside commitments? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.11
  forPractitioner: { text: "Recognise that presenting in reviews is hard for some students, and use varied modes and methods of delivery and assessment, perhaps with an inclusive curriculum toolkit, so the studio supports different learners.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.11 as an expectation the statement puts with 'should': schools should recognise the challenges that reviews and public presentation in studio can pose for some students. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.11) and do not call it a regulatory or legal requirement in its own right. Set it beside 3.34 to 3.37 on reviews and 3.44 on alternative assessment spaces."
  author-agent-dialogue: "Raise paragraph 1.11 with a programme team or teacher when a team designs review formats or presentation-based assessment, framing it as something the course is expected to do. Ask: Which students find your review format hardest, and what alternative do you offer them without losing the learning? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.12
  forPractitioner: { text: "Meet the legal duty to make reasonable adjustments (the Equality Act 2010, with the 1995 and 1996 Acts the paragraph also names), and use the school's own expertise in accessible design to go beyond those adjustments.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe paragraph 1.12 as a requirement the statement puts with 'must': institutions are legally required to make reasonable adjustments under the Acts it names (the issuer's word is 'required', recorded as must). It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.12) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.13 to 1.18 on accessibility, 4.3 on competence standards and the Equality Act 2010 and theme:accessibility."
  author-agent-dialogue: "Raise paragraph 1.12 with a programme team or teacher when a team asks what the law requires of the school for disabled students, framing it as something the course is expected to do. Ask: How does the school move from making individual adjustments to designing access in from the start? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.14
  forPractitioner: { text: "Take an integrated, whole-school approach to accessibility that goes past compliance; because the discipline teaches inclusive design, its own spaces and curriculum should model it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.14 as an expectation the statement puts with 'should': institutions should adopt integrated approaches to accessibility that go beyond basic compliance. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.14) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.12, 1.16 on flexible curriculum design and the inclusive design content in 4.6.b5 and 4.7.b5."
  author-agent-dialogue: "Raise paragraph 1.14 with a programme team or teacher when a team reviews its accessibility arrangements or its own building and studio spaces, framing it as something the course is expected to do. Ask: Would a visitor see the inclusive design you teach reflected in your own studios and course arrangements? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.17
  forPractitioner: { text: "Set up a clear framework for deciding fairly and openly when students' needs clash within group work, and use it as a chance to build emotional literacy across the cohort.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.17 as an expectation the statement puts with 'should': providers should develop clear oversight frameworks for fair decisions when individual needs conflict in group settings. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.17) and do not call it a regulatory or legal requirement in its own right. Set it beside 3.45 on group work and the emotional literacy items 4.6.b11 and 4.7.b11."
  author-agent-dialogue: "Raise paragraph 1.17 with a programme team or teacher when a team runs group projects and needs a way to resolve clashing adjustments, framing it as something the course is expected to do. Ask: When two students' needs pull a group project in different directions, who decides and on what basis? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.18
  forPractitioner: { text: "Look at the studio as a working environment for neurodivergent and disabled students (light, sound, clutter, places to step away) and consider reasonable adjustments where it disadvantages them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.18 as an expectation the statement puts with 'should': course teams should consider adjusting physical settings that put disabled students at a disadvantage. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.18) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.12, 1.15 on neurodivergent conditions and 3.23 on studio facilities."
  author-agent-dialogue: "Raise paragraph 1.18 with a programme team or teacher when a team plans studio space or responds to a student's access needs, framing it as something the course is expected to do. Ask: What in your studio environment makes long working hours harder for neurodivergent students, and what could be changed? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.21
  forPractitioner: { text: "Give students room in the curriculum to question sustainability itself, its limits and emerging alternatives, rather than presenting it as a settled checklist.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.21 as an expectation the statement puts with 'should': curricula should leave space for students to engage critically with sustainability, its limits and emerging alternatives. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.21) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.23 on climate literacy, the climate and ecological literacy items 4.6.b4 and 4.7.b4 and std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise paragraph 1.21 with a programme team or teacher when a team designs or reviews its sustainability teaching, framing it as something the course is expected to do. Ask: Where do students get to challenge the idea of sustainability, not only apply it? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.23
  forPractitioner: { text: "Develop climate literacy across every strand of the course, not in one module: tie it to real-world application and bring in predictive tools, for example energy or performance modelling and whole life carbon checks, to test design choices.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will build a solid grounding in climate literacy across every part of your studies, from design and culture to technology and practice, and you may use tools such as energy modelling to test your design choices.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe paragraph 1.23 as an expectation the statement puts with 'will': climate literacy is developed across the whole course rather than in one place. It underpins the climate and ecological literacy minimum at honours (4.6.b4, FHEQ Level 6) and at master's (4.7.b4, FHEQ Level 7) but is not itself a rung. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.23), do not present the tools it mentions as required; set it beside 1.21, 1.24 and the honours descriptor item qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Bring paragraph 1.23 up when a student asks how sustainability fits their studies, or when a team maps climate content across the years. With a student, say in plain words that climate understanding runs through design, history, technology and practice; with staff, ask where each strand carries it. Ask: In which of your projects did climate questions shape a design decision, and how did you test that decision? Avoid presenting the predictive tools as a requirement, and do not read the paragraph aloud."
- statement: qaa/architecture-2026/1.25
  forPractitioner: { text: "Model the environmental and ethical practice you teach, and review and refine your sustainability education with your students on a continuing basis.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.25 as an expectation the statement puts with 'should': providers should lead by example and keep reviewing their sustainability education practice together with students. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.25) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.21, 1.23 and theme:esd."
  author-agent-dialogue: "Raise paragraph 1.25 with a programme team or teacher when a team considers how the school's own operations and practices match what it teaches on sustainability, framing it as something the course is expected to do. Ask: Where does the school's own practice contradict what it asks of students on sustainability, and how do students help review that? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.31
  forPractitioner: { text: "Where placements are offered, protect students from poor working practices during them, and make sure every student gets the same level of help in securing a placement.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.31 as an expectation the statement puts with 'should': providers should strive to give all students equal support in finding a placement, and schools carry an ethical duty during placements. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.31) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.32 to 1.34 on routes to experience and 2.9 on monitoring practical experience."
  author-agent-dialogue: "Raise paragraph 1.31 with a programme team or teacher when a team runs or reviews placement support, framing it as something the course is expected to do. Ask: Do all students, whatever their networks or background, get the same help to find a placement, and how do you check working conditions? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.35
  forPractitioner: { text: "When you run live projects with field trips or community engagement, plan for risk, ethics and student accessibility from the outset.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe paragraph 1.35 as an expectation the statement puts with 'will': live projects with trips or community work have to deal with risk, ethics and access for students. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.35) and do not call it a regulatory or legal requirement in its own right. Set it beside 3.32 on live project work, 2.21 on external partners and 1.27 on enterprise education."
  author-agent-dialogue: "Raise paragraph 1.35 with a programme team or teacher when a team plans a live project with a community or client, framing it as something the course is expected to do. Ask: What risk, ethical and access questions does this live project raise, and who has signed them off? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.37
  forPractitioner: { text: "Teach how industry uses GenAI and its ethical, environmental, intellectual property and data protection implications, including bias and its mitigation, and build students' critical judgement of outputs and their ability to account for how they used the tools.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the curriculum; the student-facing outcome is in the digital literacy items 4.6.b6 and 4.7.b6", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe paragraph 1.37 as an expectation the statement puts with 'will': courses will need to teach knowledge and understanding of GenAI use in industry, and this should cover its ethical, IP, data and bias issues. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.37) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.38 to 1.40, the digital literacy items 4.6.b6 and 4.7.b6 and the GenAI theme (theme:genai, proposed)."
  author-agent-dialogue: "Raise paragraph 1.37 with a programme team or teacher when a team decides where GenAI is taught and how students should account for their use of it, framing it as something the course is expected to do. Ask: Where do students learn the ethical and legal issues of GenAI, and how do they show the reasoning behind their prompts? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.38
  forPractitioner: { text: "Use critical and reflective assessment to make authorship and process visible, treat GenAI as a facilitating tool and keep valuing speculative, analytical and research-informed methods in design assessment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.38 as an expectation the statement puts with 'should': courses should keep encouraging speculative, analytical, research-led and new methods when studio design is assessed. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.38) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.37, 1.39 and 3.40 on capturing the design process."
  author-agent-dialogue: "Raise paragraph 1.38 with a programme team or teacher when a team revises studio assessment in response to GenAI, framing it as something the course is expected to do. Ask: How does your assessment show who authored a design and how it developed, whatever tools were used? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/1.40
  forPractitioner: { text: "Before a brief requires a specialist GenAI tool, consider what teaching students need to use it and what it costs them, so the tool widens inclusion rather than rewarding those who can pay.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 1.40 as an expectation the statement puts with 'should': providers should ensure GenAI is implemented to promote inclusion, weighing teaching and cost before setting briefs that require it. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 1.40) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.10 on hidden costs, 1.37 and 3.26 on equitable access to software."
  author-agent-dialogue: "Raise paragraph 1.40 with a programme team or teacher when a team considers requiring a paid GenAI tool in a brief, framing it as something the course is expected to do. Ask: If a brief needs a specialist GenAI tool, who pays for it and who teaches students to use it? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/2.1
  forPractitioner: { text: "Keep the curriculum flexible enough to absorb new knowledge and techniques (regulation, fabrication, sustainable methods, AI) so students see the field as an academic discipline and as a profession in rapid change.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 2.1 as an expectation the statement puts with 'should': curriculum design should remain flexible enough to take in emerging knowledge and techniques. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 2.1) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.37 on GenAI, 2.2 and 2.4."
  author-agent-dialogue: "Raise paragraph 2.1 with a programme team or teacher when a team plans how new regulation or technology enters the curriculum, framing it as something the course is expected to do. Ask: How quickly can a change in regulation or practice reach your modules, and who decides? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/2.2
  forPractitioner: { text: "Design the course to build research and creativity that serve registration and other careers or further study alike, and make the hard and soft transferable skills explicit to students.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 2.2 as an expectation the statement puts with 'should': course design should instil research and creativity that underpin progression into registration, other careers or further study. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 2.2) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.30 on careers beyond the title, 2.6 and the research literacy items 4.6.b7 and 4.7.b7."
  author-agent-dialogue: "Raise paragraph 2.2 with a programme team or teacher when a team considers students who will not become registered architects, framing it as something the course is expected to do. Ask: How visible to students are the transferable skills your course builds, and where are they named? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/2.3
  forPractitioner: { text: "In a joint or combined degree, students will meet the core elements of the threshold literacies and add others drawn from their second subject; design the joint curriculum so both hold.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study architecture as part of a joint or combined degree, you will reach the core parts of the minimum literacies for the subject and add others from your second subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe paragraph 2.3 as an expectation, put with 'will', that joint and combined honours students reach the core of the threshold literacies, not all of them. It holds for the bachelor's degree with honours at FHEQ Level 6 and FQHEIS Level 10. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 2.3); do not claim it names which literacies are core, since it does not; set it beside the honours minimum list 4.6.b1 to 4.6.b12 and the descriptor item qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise paragraph 2.3 when a joint or combined honours student asks whether they must meet every architecture standard, or when a team designs a joint programme. Tell the student in plain words that they reach the core of the subject's minimum and add strengths from their other subject; with staff, ask how the core is chosen. Ask: Which of the twelve literacies does your architecture side cover fully, and which does your other subject add? Avoid implying the student is held to less than a minimum without saying what the core is."
- statement: qaa/architecture-2026/2.4
  forPractitioner: { text: "Map the ARB and RIBA minimum content requirements into the modules, then design beyond them so students experiment, investigate critically and grow intellectually rather than just comply.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 2.4 as an expectation the statement puts with 'should': providers should take account of PSRB requirements for minimum content, notably ARB and RIBA, while going beyond compliance. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 2.4) and do not call it a regulatory or legal requirement in its own right. Set it beside 4.5, 2.25 to 2.28 on the PSRBs and SB5."
  author-agent-dialogue: "Raise paragraph 2.4 with a programme team or teacher when a team maps PSRB content into modules, framing it as something the course is expected to do. Ask: Where does your course go beyond ARB and RIBA minimum content, and how do you show it? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/2.9
  forPractitioner: { text: "Monitor placements and study abroad that sit within the course, shape progression routes around individual needs and put reasonable adjustments in place so time away is equitable and inclusive.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 2.9 as an expectation the statement puts with 'should': practical experience and study abroad should be monitored by the provider, with reasonable adjustments where appropriate. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 2.9) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.31, 2.8 and 1.12 to 1.18 on accessibility."
  author-agent-dialogue: "Raise paragraph 2.9 with a programme team or teacher when a team oversees placements, years out or study abroad, framing it as something the course is expected to do. Ask: How do you monitor a student's experience while they are away, and how are adjustments carried into a placement? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/2.10
  forPractitioner: { text: "If you offer or plan the Level 6 or Level 7 architecture apprenticeships, work from the relevant national trailblazer groups' requirements alongside RIBA validation.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 2.10 as an expectation the statement puts with 'should': providers should refer to the national apprenticeship trailblazer groups' requirements when exploring the apprenticeship routes. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 2.10) and do not call it a regulatory or legal requirement in its own right. Set it beside 2.16 on release structures, 2.26 on RIBA validation and SB5."
  author-agent-dialogue: "Raise paragraph 2.10 with a programme team or teacher when a team considers an apprenticeship route, framing it as something the course is expected to do. Ask: Which trailblazer requirements apply to your apprenticeship, and how do they sit with the validation you hold? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/2.15
  forPractitioner: { text: "Design every course for inclusion and accessibility from the start, and consider whether full-time, part-time, campus studio or blended and online modes would widen access.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 2.15 as an expectation the statement puts with 'should': courses should be designed from the start for inclusion and access. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 2.15) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.14, 1.16 and 2.16 on hybrid teaching."
  author-agent-dialogue: "Raise paragraph 2.15 with a programme team or teacher when a team designs a new course or delivery mode, framing it as something the course is expected to do. Ask: Which students could not take your course as currently delivered, and which mode would change that? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/2.19
  forPractitioner: { text: "In any franchise, validation, articulation or transnational partnership, make sure the quality and standards of the architecture degree are the same everywhere and that every student, wherever they study, meets these standards.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe paragraph 2.19 as a requirement the statement puts with 'must': in developing partnership models, providers must ensure consistent quality and standards and that all students achieve the standards set out. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 2.19) and do not call it a regulatory or legal requirement in its own right. Set it beside 2.18, 2.20 and the Quality Code's Advice and Guidance on Partnerships (not yet ingested)."
  author-agent-dialogue: "Raise paragraph 2.19 with a programme team or teacher when a team plans or reviews a partnership or transnational delivery, framing it as something the course is expected to do. Ask: How do you know students at a partner site reach the same literacies as students at home? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/2.20
  forPractitioner: { text: "Apply these standards to the whole of any qualification involving partners, formal or informal, so the outcomes hold across every part of the programme.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 2.20 as an expectation the statement puts with 'should': the statement and its standards should be applied so a qualification involving partnerships reaches the outcomes across the whole programme. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 2.20) and do not call it a regulatory or legal requirement in its own right. Set it beside 2.19 and 2.21."
  author-agent-dialogue: "Raise paragraph 2.20 with a programme team or teacher when a team designs an award with parts delivered by others, framing it as something the course is expected to do. Ask: Which parts of the award do partners deliver, and how do those parts contribute to the literacies? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/2.24
  forPractitioner: { text: "Bring in external reviewers for periodic review to test proposed changes independently and confirm that threshold standards are met and content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe paragraph 2.24 as an expectation the statement puts with 'will': providers will use external reviewers in periodic review to secure threshold standards and suitable content. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 2.24) and do not call it a regulatory or legal requirement in its own right. Set it beside 2.23, 2.29 to 2.30 on external examiners and 2.32."
  author-agent-dialogue: "Raise paragraph 2.24 with a programme team or teacher when a team prepares for periodic review, framing it as something the course is expected to do. Ask: Who is your external reviewer, and how will they judge whether threshold standards are met? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/2.32
  forPractitioner: { text: "Reflect the cross-cutting themes (equity and inclusion, accessibility, sustainability, enterprise, GenAI) in course design, content and delivery, and use programme review to test how well they are woven through.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 2.32 as an expectation the statement puts with 'should': programmes should reflect the cross-cutting themes in design, content and delivery. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 2.32) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.6 to 1.40 (which set out the five themes) and SB6."
  author-agent-dialogue: "Raise paragraph 2.32 with a programme team or teacher when a team prepares a programme review or annual monitoring, framing it as something the course is expected to do. Ask: For each of the five themes, where would a reviewer find it in your modules and assessments? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/3.2
  forPractitioner: { text: "Use the twelve literacies as an overlapping frame that links professional requirements to teaching and assessment, not as separate boxes to tick module by module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You will meet the twelve literacies as overlapping parts of one way of thinking about architecture, not as separate subjects, and they give you words to explain your work to people outside the field.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 3.2 as guidance, put with 'should', on how to read the taxonomy: the literacies are interdependent, not discrete. It applies to both the honours (FHEQ Level 6) and the master's (FHEQ Level 7) minimum lists. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 3.2); do not write the literacies up as twelve separate modules or a checklist; set it beside 3.3, 4.4 and the two lists 4.6 and 4.7."
  author-agent-dialogue: "Bring paragraph 3.2 in when a student or teacher treats the literacies as separate boxes, or a team wants to map them one per module. With a student, say plainly that a single project usually draws on several literacies at once; with staff, frame it as a reason to foreground one literacy per assessment without isolating it. Ask: In your last project, which literacies were you using together, and which was the main focus? Avoid reading the paragraph aloud."
- statement: qaa/architecture-2026/3.3
  forPractitioner: { text: "Plan the course so graduates acquire all twelve literacies, which 4.6 defines for honours and 4.7 for the master's; this paragraph only names them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your course you will have built twelve literacies: design, visual and spatial, cultural and contextual, climate and ecological, technical, digital, research, ethical and professional, practice and business, financial, emotional and communication.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe paragraph 3.3 as the list of the twelve literacies every graduate is expected to have acquired; the issuer's wording is 'is expected to', recorded here as will. It names the literacies only; their content and level are in 4.6 (honours, FHEQ Level 6) and 4.7 (master's, FHEQ Level 7). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 3.3) and do not write outcomes from the names alone; set it beside 4.6.b1 to 4.6.b12 and 4.7.b1 to 4.7.b12."
  author-agent-dialogue: "Raise paragraph 3.3 when a student or team first asks what the subject's literacies are. Name them in plain words and point on to the honours or master's definitions for what each asks; with staff, frame the list as the spine of the course's outcomes. Ask: Which of these twelve do you feel strongest in, and which have you had least chance to build? Avoid treating the bare names as the standard."
- statement: qaa/architecture-2026/3.22
  forPractitioner: { text: "Ask for portfolios that show how a design developed, including tests and failures, as well as the finished outcome.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 3.22 as an expectation the statement puts with 'should': portfolios submitted for assessment should show how a studio design developed as well as where it ended. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 3.22) and do not call it a regulatory or legal requirement in its own right. Set it beside 3.40 to 3.42 on assessment tasks and the portfolio and 1.38."
  author-agent-dialogue: "Raise paragraph 3.22 with a programme team or teacher when a team writes portfolio requirements or marking criteria, framing it as something the course is expected to do. Ask: Does your portfolio brief reward evidence of process and failed attempts, or only the final scheme? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/3.23
  forPractitioner: { text: "Provide a well-lit studio with space for large models, the digital tools industry uses, power and Wi-Fi, ready access to large-format printing and making facilities and secure storage; where physical studio space is not possible, replicate its features digitally.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 3.23 as an expectation the statement puts with 'should': students should be able to reach printing and making facilities and store their belongings and work securely. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 3.23) and do not call it a regulatory or legal requirement in its own right. Set it beside 3.24 to 3.28 on resources, 1.18 on the physical environment and 3.26."
  author-agent-dialogue: "Raise paragraph 3.23 with a programme team or teacher when a team plans studio space or resources, framing it as something the course is expected to do. Ask: Can every student store work securely and reach printing and workshops when they need them? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/3.33
  forPractitioner: { text: "Plan site and study visits with their environmental cost, especially air travel, and their affordability and fit with caring or work commitments in mind.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 3.33 as an expectation the statement puts with 'should': programmes should be mindful of the environmental and EDI impacts of study visits. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 3.33) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.10 on costs, 1.21 and 1.25 on sustainability."
  author-agent-dialogue: "Raise paragraph 3.33 with a programme team or teacher when a team plans a study trip, framing it as something the course is expected to do. Ask: Who cannot come on this trip, and what is its carbon cost against the learning? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/3.34
  forPractitioner: { text: "Run reviews as feedback and practice in presenting, and make sure non-visual and non-verbal alternatives exist for students who need them, both in learning and in assessment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe paragraph 3.34 as an expectation the statement puts with 'will': providers will need to make sure students who need them have alternatives to visual and spoken presentation. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 3.34) and do not call it a regulatory or legal requirement in its own right. Set it beside 3.35 to 3.37 on review formats, 1.11 and the communication literacy items 4.6.b12 and 4.7.b12."
  author-agent-dialogue: "Raise paragraph 3.34 with a programme team or teacher when a team designs reviews or responds to a student who cannot present in the usual way, framing it as something the course is expected to do. Ask: What does a student who cannot present visually or verbally do instead, and is it equally valued? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/3.36
  forPractitioner: { text: "Brief and guide staff so they have considered the format and scope of each review, and try student-centred formats such as grouped presentations, peer discussion with written feedback and online reviews.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 3.36 as an expectation the statement puts with 'should': schools should ensure staff have considered review format and scope and have guidance for an inclusive environment. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 3.36) and do not call it a regulatory or legal requirement in its own right. Set it beside 3.35, 3.37 and 3.40 on guidance for external panel members."
  author-agent-dialogue: "Raise paragraph 3.36 with a programme team or teacher when a team prepares tutors and visiting critics for reviews, framing it as something the course is expected to do. Ask: What guidance do your tutors and visiting critics receive before a review, and who checks the format is inclusive? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/3.37
  forPractitioner: { text: "If a review is summative, check that no student or group is disadvantaged, offer an alternative where in-person presentation would unfairly affect someone, and give staff guidance on inclusive, supportive feedback.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 3.37 as an expectation the statement puts with 'should': particular care should be taken that summative reviews do not disadvantage individuals or groups. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 3.37) and do not call it a regulatory or legal requirement in its own right. Set it beside 3.34, 3.36 and 3.44 on assessment spaces."
  author-agent-dialogue: "Raise paragraph 3.37 with a programme team or teacher when a team uses a review as part of a final mark, framing it as something the course is expected to do. Ask: If a review counts towards the mark, what would a fair alternative look like for a student affected by presenting in person? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/3.40
  forPractitioner: { text: "Use a range of assessment tasks that capture the design process (logbooks, decision rationales, reflective commentary), and brief external panel members on how to conduct reviews and give feedback inclusively.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 3.40 as an expectation the statement puts with 'should': care should be taken that external panel members have guidance on conduct and feedback during reviews. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 3.40) and do not call it a regulatory or legal requirement in its own right. Set it beside 3.22, 3.36, 1.38 and 1.39 on GenAI and authorship."
  author-agent-dialogue: "Raise paragraph 3.40 with a programme team or teacher when a team invites external panel members to reviews or adapts assessment for GenAI, framing it as something the course is expected to do. Ask: How do your assessment tasks show the student's own design process, and what are visiting panel members told before they comment? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/3.44
  forPractitioner: { text: "Set up assessment spaces that suit architectural work and every student, offer alternatives such as a recorded presentation or quiet room where needed and reserve studio space for physical submissions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 3.44 as an expectation the statement puts with 'should': assessment spaces should be appropriate and suitable for all, with alternative spaces offered where required. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 3.44) and do not call it a regulatory or legal requirement in its own right. Set it beside 3.37, 1.16 and 1.18."
  author-agent-dialogue: "Raise paragraph 3.44 with a programme team or teacher when a team plans assessment logistics, framing it as something the course is expected to do. Ask: What alternative space or format can a student ask for, and how do they know it is available? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/3.45
  forPractitioner: { text: "Encourage students to take up group projects when offered, and assess both the collective and the individual contribution, including the student's reflection on group feedback.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You will be encouraged to take part in group projects when they are on offer, because team working is central to architectural practice, and you may be assessed on both your shared and your own contribution.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 3.45 as an expectation, put with 'should', that students are encouraged into group working; the duty to encourage sits with the course. It applies at honours (FHEQ Level 6) and master's (FHEQ Level 7), and the group skills it builds sit beside the honours descriptor item qaa/fheq-2024/4.15.b9.1 and the master's item qaa/fheq-2024/4.17.b8.1. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 3.45); do not claim group work is compulsory; set it beside 1.4, 1.17, 3.19 and the emotional literacy items 4.6.b11 and 4.7.b11."
  author-agent-dialogue: "Raise paragraph 3.45 when a student is unsure about joining a group project or a team designs group assessment. With a student, explain in plain words why team working matters in practice; with staff, ask how individual contributions are seen within the group mark. Ask: What did you learn from the feedback on your last group project that you could not have learned alone? Avoid presenting group work as mandatory."
- statement: qaa/architecture-2026/4.1
  forPractitioner: { text: "Treat the literacies as the minimum every student will have demonstrated at award; for an integrated master's, students meet the honours minimum first, then complete a further year (or equivalent credit) at Level 7 or SCQF Level 11.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "When you are awarded your degree, you will have shown at least the minimum level in each of the subject's literacies; on an integrated master's, you first reach the honours minimum and then complete a further year at master's level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe paragraph 4.1 as the statement's definition of its standards: minimum standards, the threshold a student will have demonstrated at award, for the honours degree (FHEQ Level 6, FQHEIS Level 10) and the master's (FHEQ Level 7, FQHEIS Level 11). State that the integrated master's requires the honours minimum first and then a year or equivalent credit at Level 7. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.1); do not imply typical or excellent rungs, which the statement does not set; set it beside 4.2, the lists 4.6 and 4.7 and the descriptors qaa/fheq-2024/4.15.i1 and qaa/fheq-2024/4.17.i1."
  author-agent-dialogue: "Raise paragraph 4.1 when a student asks what they must show to be awarded the degree, or how the integrated master's is built. Tell a student plainly that the literacies are the floor everyone reaches; with staff, frame them as the threshold the award rests on. Ask: Which literacy are you least sure you have shown yet, and what evidence would settle it? Do not describe the minimum as the expected level of a typical student."
- statement: qaa/architecture-2026/4.2
  forPractitioner: { text: "Judge achievement above the minimum by your own method, but anchor it to Annex D's descriptions of first, upper second, lower second and third-class honours.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 4.2 as an expectation the statement puts with 'should': providers should refer to Annex D of the Frameworks for Higher Education Qualifications when judging achievement above the minimum. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.2) and do not call it a regulatory or legal requirement in its own right. Set it beside 4.1, Annex D in std:doc:qaa-fheq-2024-framework (qaa/fheq-2024/annex-d/summary/r1/3rd to qaa/fheq-2024/annex-d/summary/r1/1st) and its SL6 classification bands."
  author-agent-dialogue: "Raise paragraph 4.2 with a programme team or teacher when a team sets classification criteria or marking descriptors, framing it as something the course is expected to do. Ask: How do your marking criteria for a first, a 2.1 and a 2.2 relate to Annex D's descriptions? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/4.3
  forPractitioner: { text: "Do not treat the literacies as competence standards in the Equality Act sense; if you write competence standards for a programme specification, draw on the statement and PSRB requirements and follow current Equality and Human Rights Commission guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe paragraph 4.3 as an expectation the statement puts with 'should': providers that develop competence standards should follow the most recent Equality and Human Rights Commission guidance. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.3) and do not call it a regulatory or legal requirement in its own right. Set it beside 1.12, 4.5 and SB5."
  author-agent-dialogue: "Raise paragraph 4.3 with a programme team or teacher when a team writes competence standards or considers adjustments to assessment, framing it as something the course is expected to do. Ask: Which of your requirements are true competence standards, and have you checked them against current EHRC guidance? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/4.5
  forPractitioner: { text: "If your degree is recognised by ARB or RIBA, their themes, values, attributes and outcomes apply alongside these literacies; plan for both.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe paragraph 4.5 as an expectation the statement puts with 'will': for PSRB-recognised degrees, the bodies' own themes, values, attributes and outcomes will apply. It applies to courses at both awards the statement covers, the honours degree (FHEQ Level 6) and the master's (FHEQ Level 7), and is a duty on the course, not an outcome a student demonstrates. Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.5) and do not call it a regulatory or legal requirement in its own right. Set it beside 2.4, 2.25 to 2.28 and SB5 (the ARB and RIBA requirements are not yet ingested)."
  author-agent-dialogue: "Raise paragraph 4.5 with a programme team or teacher when a team aligns the course with ARB or RIBA requirements, framing it as something the course is expected to do. Ask: Where do the ARB or RIBA outcomes ask for more than these literacies, and how does the course show both? Do not put it to a student as a target they have to meet, and summarise it rather than reading the issuer's wording aloud."
- statement: qaa/architecture-2026/4.6.b1
  forPractitioner: { text: "Every honours graduate will be able to take a design proposal of moderate complexity from idea to developed scheme, iterating and combining spatial, aesthetic, environmental and technical concerns, and answer a brief with technical coherence and regard for context.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, at minimum, you will be able to come up with and develop a design of moderate complexity, working through it in cycles and pulling together space, art, environment and technical needs, so that it answers the brief and fits its setting.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for design literacy at the end of an honours degree in architecture: a threshold every graduate of the award will have reached, at FHEQ Level 6 and FQHEIS Level 10 (spine:6). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.6, literacy 1). Do not present it as an ARB or RIBA criterion or as the typical standard of an honours graduate, or the master's minimum. Set it beside the master's item 4.7.b1 and 3.4 on studio projects and the honours descriptor items qaa/fheq-2024/4.15.b6 and qaa/fheq-2024/4.15.b7 and the third-class column of Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd)."
  author-agent-dialogue: "Bring this up when a student asks what design literacy asks of them by the end of the honours degree, or when a team maps design project briefs across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Looking at your latest design, how did you balance the spatial, environmental and technical demands, and how did it change through your iterations? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.6.b2
  forPractitioner: { text: "Every honours graduate will be able to create, interpret, manipulate and communicate spatial and visual information in drawings and models to develop a coherent proposal, including spatial relationships and material assemblies.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, at minimum, you will be able to imagine, read, work on and share spatial and visual ideas through drawings and models, using them to develop a coherent design that shows how spaces relate and how materials fit together.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for visual and spatial literacy at the end of an honours degree in architecture: a threshold every graduate of the award will have reached, at FHEQ Level 6 and FQHEIS Level 10 (spine:6). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.6, literacy 2). Do not present it as an ARB or RIBA criterion or as the typical standard of an honours graduate, or the master's minimum. Set it beside the master's item 4.7.b2 and 3.22 on drawing and modelling in studio and the honours descriptor items qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b8 and the third-class column of Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd)."
  author-agent-dialogue: "Bring this up when a student asks what visual and spatial literacy asks of them by the end of the honours degree, or when a team maps drawing and modelling across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Which of your drawings or models best shows how the spaces in your scheme relate to each other, and why? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.6.b3
  forPractitioner: { text: "Every honours graduate will understand, and engage critically with, the settings that shape architecture (cultural, historical, theoretical, artistic and social), analyse precedents to inform design and draw on history and theory from a range of global cultures and periods.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, at minimum, you will understand and think critically about the cultural, historical, theoretical, artistic and social forces that shape buildings and use precedents from many cultures and periods to inform your designs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for cultural and contextual literacy at the end of an honours degree in architecture: a threshold every graduate of the award will have reached, at FHEQ Level 6 and FQHEIS Level 10 (spine:6). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.6, literacy 3). Do not present it as an ARB or RIBA criterion or as the typical standard of an honours graduate, or the master's minimum. Set it beside the master's item 4.7.b3, 3.7 on architectural humanities and 1.8 on decolonising the curriculum and the honours descriptor items qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b7 and the third-class column of Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd)."
  author-agent-dialogue: "Bring this up when a student asks what cultural and contextual literacy asks of them by the end of the honours degree, or when a team maps history and theory teaching across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Which precedent most shaped your last design, and what did you take from its cultural or historical setting? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.6.b4
  forPractitioner: { text: "Every honours graduate will know the principles behind climate change, the loss of biodiversity, environmental impact and regenerative design, and why responsible material specification, energy efficiency and ethical sourcing matter.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, at minimum, you will know the main principles of climate change, biodiversity loss and environmental impact, the strategies of regenerative design and why choosing materials responsibly, saving energy and sourcing ethically matter.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for climate and ecological literacy at the end of an honours degree in architecture: a threshold every graduate of the award will have reached, at FHEQ Level 6 and FQHEIS Level 10 (spine:6). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.6, literacy 4). Do not present it as an ARB or RIBA criterion or as the typical standard of an honours graduate, or the master's minimum. Set it beside the master's item 4.7.b4, 1.21 and 1.23 on climate literacy, and theme:esd and the honours descriptor items qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b4 and the third-class column of Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd)."
  author-agent-dialogue: "Bring this up when a student asks what climate and ecological literacy asks of them by the end of the honours degree, or when a team maps sustainability and climate content across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Can you explain how one material choice in your project affects its carbon and ecological impact? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.6.b5
  forPractitioner: { text: "Every honours graduate will know construction systems, building physics, pathology, materials and environmental technologies, as well as the principles of life and fire safety, accessibility and inclusive design; they will integrate strategies that meet suitable performance standards in new build, reuse or conservation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, at minimum, you will know how buildings are built and how they perform (structure, materials, physics, decay and environmental systems), the basics of life safety, fire safety, access and inclusive design and how to build these into a design that performs as it should.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for technical and building environment literacy at the end of an honours degree in architecture: a threshold every graduate of the award will have reached, at FHEQ Level 6 and FQHEIS Level 10 (spine:6). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.6, literacy 5). Do not present it as an ARB or RIBA criterion or as the typical standard of an honours graduate, or the master's minimum. Set it beside the master's item 4.7.b5 and 3.8 on technology as a subject area and the honours descriptor items qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b2 and the third-class column of Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd)."
  author-agent-dialogue: "Bring this up when a student asks what technical and building environment literacy asks of them by the end of the honours degree, or when a team maps technology and environmental science teaching across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Where in your last scheme did fire safety or accessibility change a design decision? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.6.b6
  forPractitioner: { text: "Every honours graduate will be able to use digital tools in design, evaluation and communication and will be aware of the uses of generative AI in practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, at minimum, you will be able to use digital tools to design, test and present your work, and you will know how generative AI can be used in architectural practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for digital literacy at the end of an honours degree in architecture: a threshold every graduate of the award will have reached, at FHEQ Level 6 and FQHEIS Level 10 (spine:6). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.6, literacy 6). Do not present it as an ARB or RIBA criterion or as the typical standard of an honours graduate, or the master's minimum. Set it beside the master's item 4.7.b6, 1.37 on GenAI and 3.26 on digital access and the honours descriptor items qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b8 and the third-class column of Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd)."
  author-agent-dialogue: "Bring this up when a student asks what digital literacy asks of them by the end of the honours degree, or when a team maps software and GenAI teaching across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Which digital tools did you use to test your last design, and where did you choose not to use generative AI? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.6.b7
  forPractitioner: { text: "Every honours graduate will understand architectural research methods and how they support innovation-led decisions and advance knowledge in the field.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, at minimum, you will understand how research is done in architecture and how it helps you make well-founded, innovative design decisions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for research and enquiry-based literacy at the end of an honours degree in architecture: a threshold every graduate of the award will have reached, at FHEQ Level 6 and FQHEIS Level 10 (spine:6). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.6, literacy 7). Do not present it as an ARB or RIBA criterion or as the typical standard of an honours graduate, or the master's minimum. Set it beside the master's item 4.7.b7 and 3.11 on research-led enquiry and the honours descriptor items qaa/fheq-2024/4.15.b3.2 and qaa/fheq-2024/4.15.b6 and the third-class column of Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd)."
  author-agent-dialogue: "Bring this up when a student asks what research and enquiry-based literacy asks of them by the end of the honours degree, or when a team maps research methods teaching across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: What research did you do for your last project, and how did it change the design? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.6.b8
  forPractitioner: { text: "Every honours graduate will know the profession's codes of conduct and the principles of equity, diversity, inclusion and accessibility, and understand how design decisions bear ethically on people, environment and wellbeing.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, at minimum, you will know the codes of conduct architects follow and the principles of fairness, inclusion and access, and you will understand how design choices affect society, the environment and people's wellbeing.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for ethical and professional literacy at the end of an honours degree in architecture: a threshold every graduate of the award will have reached, at FHEQ Level 6 and FQHEIS Level 10 (spine:6). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.6, literacy 8). Do not present it as an ARB or RIBA criterion or as the typical standard of an honours graduate, or the master's minimum. Set it beside the master's item 4.7.b8, 1.8 and theme:edi and the honours descriptor items qaa/fheq-2024/4.15.b9.2 and qaa/fheq-2024/4.15.b9.1 and the third-class column of Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd)."
  author-agent-dialogue: "Bring this up when a student asks what ethical and professional literacy asks of them by the end of the honours degree, or when a team maps professional ethics and EDI content across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Which ethical question did your last project raise for the people who would use it, and how did you respond? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.6.b9
  forPractitioner: { text: "Every honours graduate will know the principles of architecture's professional, legal and business context: project management, procurement, contracts, policy, financial planning, cost management, planning, building codes and regulation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, at minimum, you will know the basics of how architecture works as a profession and a business, including managing projects, procurement, contracts, policy, budgets, the planning system, building regulations and compliance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for practice and business literacy at the end of an honours degree in architecture: a threshold every graduate of the award will have reached, at FHEQ Level 6 and FQHEIS Level 10 (spine:6). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.6, literacy 9). Do not present it as an ARB or RIBA criterion or as the typical standard of an honours graduate, or the master's minimum. Set it beside the master's item 4.7.b9 and 3.9 on professional practice and the honours descriptor items qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b9.3 and the third-class column of Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd)."
  author-agent-dialogue: "Bring this up when a student asks what practice and business literacy asks of them by the end of the honours degree, or when a team maps professional practice teaching across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: If a client asked how your design would get planning approval and meet building regulations, what would you tell them? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.6.b10
  forPractitioner: { text: "Every honours graduate will be aware of how local and global financial and economic forces influence design proposals and the longevity of projects.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, at minimum, you will be aware of how money and economics, close to home and worldwide, shape design proposals and how long buildings last.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for financial and economic literacy at the end of an honours degree in architecture: a threshold every graduate of the award will have reached, at FHEQ Level 6 and FQHEIS Level 10 (spine:6). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.6, literacy 10). Do not present it as an ARB or RIBA criterion or as the typical standard of an honours graduate, or the master's minimum. Set it beside the master's item 4.7.b10 and 4.6.b9 and the honours descriptor items qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/4.15.b9.2 and the third-class column of Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd)."
  author-agent-dialogue: "Bring this up when a student asks what financial and economic literacy asks of them by the end of the honours degree, or when a team maps cost and economic content across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: How might the budget or the wider economy change what gets built from your design, and how long it lasts? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.6.b11
  forPractitioner: { text: "Every honours graduate will be able to understand, interpret and collaborate with others in order to design for other people.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, at minimum, you will be able to understand other people, read what they need and work with them so that you can design for them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for emotional literacy at the end of an honours degree in architecture: a threshold every graduate of the award will have reached, at FHEQ Level 6 and FQHEIS Level 10 (spine:6). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.6, literacy 11). Do not present it as an ARB or RIBA criterion or as the typical standard of an honours graduate, or the master's minimum. Set it beside the master's item 4.7.b11, 1.4 on collaboration and 1.17 and the honours descriptor items qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.15.b8 and the third-class column of Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd)."
  author-agent-dialogue: "Bring this up when a student asks what emotional literacy asks of them by the end of the honours degree, or when a team maps collaborative and user-centred work across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: How did you find out what the people you were designing for needed, and how did that change your proposal? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.6.b12
  forPractitioner: { text: "Every honours graduate will be able to communicate architectural ideas clearly and effectively in verbal or non-verbal, written and visual forms, present to diverse audiences and produce coherent documentation of design intent.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, at minimum, you will be able to explain your architectural ideas clearly in speech or other forms, in writing and visually, present to different audiences such as clients and collaborators and produce clear documents that show your thinking and design intent.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for communication literacy at the end of an honours degree in architecture: a threshold every graduate of the award will have reached, at FHEQ Level 6 and FQHEIS Level 10 (spine:6). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.6, literacy 12). Do not present it as an ARB or RIBA criterion or as the typical standard of an honours graduate, or the master's minimum. Set it beside the master's item 4.7.b12 and 3.34 on reviews and the honours descriptor items qaa/fheq-2024/4.15.b8 and the third-class column of Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd)."
  author-agent-dialogue: "Bring this up when a student asks what communication literacy asks of them by the end of the honours degree, or when a team maps presentation and documentation across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Who was the hardest audience you presented to, and how did you change the way you explained your design? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.7.b1
  forPractitioner: { text: "Every master's graduate will be able to take complex proposals through to resolution with a clear method, synthesising diverse knowledge in studio, thinking strategically and in systems and answering briefs with originality as well as technical coherence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your master's, at minimum, you will be able to take a complex design from first idea to a resolved scheme, with a clear method, drawing together many kinds of knowledge, thinking strategically and in systems and answering the brief with originality.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for design literacy at the end of a master's in architecture, including the integrated master's: a threshold every graduate of the award will have reached, at FHEQ Level 7 and FQHEIS Level 11 (spine:7). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.7, literacy 1). Do not present it as an ARB or RIBA criterion or as the typical standard of a master's graduate, or the honours minimum. Set it beside the honours item 4.6.b1 and 3.12 on master's level investigation and the master's descriptor items qaa/fheq-2024/4.17.b3 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Bring this up when a student asks what design literacy asks of them by the end of the master's, or when a team maps design thesis and studio projects across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: What makes your thesis project resolved rather than developed, and where is the original move in it? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.7.b2
  forPractitioner: { text: "Every master's graduate will be able to develop and articulate sophisticated spatial and material relationships through drawing, modelling and making, with a considered architectural language that yields coherent, habitable space.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your master's, at minimum, you will be able to develop and express rich spatial and material ideas through drawing, models and making, with an architectural language of your own that creates coherent spaces people can live in.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for visual and spatial literacy at the end of a master's in architecture, including the integrated master's: a threshold every graduate of the award will have reached, at FHEQ Level 7 and FQHEIS Level 11 (spine:7). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.7, literacy 2). Do not present it as an ARB or RIBA criterion or as the typical standard of a master's graduate, or the honours minimum. Set it beside the honours item 4.6.b2 and the master's descriptor items qaa/fheq-2024/4.17.b3 and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Bring this up when a student asks what visual and spatial literacy asks of them by the end of the master's, or when a team maps drawing, modelling and making across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: How would you describe the architectural language of your recent work, and where does it show most clearly? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.7.b3
  forPractitioner: { text: "Every master's graduate will critically engage with architecture's cultural, historical, theoretical, artistic and social contexts, analyse narratives, values and precedents for design and understand social and climate justice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your master's, at minimum, you will think critically about the cultural, historical, theoretical, artistic and social forces behind architecture, use stories, values and precedents from many cultures to inform your work and understand social and climate justice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for cultural and contextual literacy at the end of a master's in architecture, including the integrated master's: a threshold every graduate of the award will have reached, at FHEQ Level 7 and FQHEIS Level 11 (spine:7). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.7, literacy 3). Do not present it as an ARB or RIBA criterion or as the typical standard of a master's graduate, or the honours minimum. Set it beside the honours item 4.6.b3 and 1.8 and the master's descriptor items qaa/fheq-2024/4.17.b1 and qaa/fheq-2024/4.17.b4.1."
  author-agent-dialogue: "Bring this up when a student asks what cultural and contextual literacy asks of them by the end of the master's, or when a team maps history, theory and justice content across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Whose story or values did your project take seriously, and whose might it have left out? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.7.b4
  forPractitioner: { text: "Every master's graduate will understand climate change, the loss of biodiversity, worldwide environmental impact and regenerative design and the importance of responsible materials, energy efficiency, waste reduction and ethical sourcing; they will apply these principles in design.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your master's, at minimum, you will understand climate change, biodiversity loss and global environmental impact, the strategies of regenerative design and why responsible materials, saving energy, cutting waste and ethical sourcing matter; you will apply them in your designs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for climate and ecological literacy at the end of a master's in architecture, including the integrated master's: a threshold every graduate of the award will have reached, at FHEQ Level 7 and FQHEIS Level 11 (spine:7). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.7, literacy 4). Do not present it as an ARB or RIBA criterion or as the typical standard of a master's graduate, or the honours minimum. Set it beside the honours item 4.6.b4, 1.21 to 1.23 and theme:esd and the master's descriptor items qaa/fheq-2024/4.17.b1 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Bring this up when a student asks what climate and ecological literacy asks of them by the end of the master's, or when a team maps sustainability and climate content across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Which regenerative principle did you apply in your thesis, and how did you test whether it worked? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.7.b5
  forPractitioner: { text: "Every master's graduate will understand construction systems, building physics, pathology, materials and environmental technologies, as well as the principles of life and fire safety, accessibility and inclusive design; they will integrate strategies that meet performance standards.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your master's, at minimum, you will understand how buildings are built and perform, the principles of life safety, fire safety, access and inclusive design and how to build these into designs that perform as they should, whether new, reused or conserved.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for technical and building environment literacy at the end of a master's in architecture, including the integrated master's: a threshold every graduate of the award will have reached, at FHEQ Level 7 and FQHEIS Level 11 (spine:7). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.7, literacy 5). Do not present it as an ARB or RIBA criterion or as the typical standard of a master's graduate, or the honours minimum. Set it beside the honours item 4.6.b5 and 3.8 and the master's descriptor items qaa/fheq-2024/4.17.b1 and qaa/fheq-2024/4.17.b2."
  author-agent-dialogue: "Bring this up when a student asks what technical and building environment literacy asks of them by the end of the master's, or when a team maps technology and environmental teaching across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: How did you test the environmental performance of your scheme, and what did the result change? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.7.b6
  forPractitioner: { text: "Every master's graduate will apply digital tools effectively and put them to purposeful use in design, evaluation and communication, knowing how practice uses BIM, computation, digital fabrication, virtual reality, generative AI and data security.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your master's, at minimum, you will be able to use digital tools effectively and purposefully in designing, testing and presenting, and you will know how architects use BIM, computational design, digital fabrication, virtual reality and generative AI, and how they keep data secure.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for digital literacy at the end of a master's in architecture, including the integrated master's: a threshold every graduate of the award will have reached, at FHEQ Level 7 and FQHEIS Level 11 (spine:7). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.7, literacy 6). Do not present it as an ARB or RIBA criterion or as the typical standard of a master's graduate, or the honours minimum. Set it beside the honours item 4.6.b6, 1.37 to 1.39 and 3.8 and the master's descriptor items qaa/fheq-2024/4.17.b2 and qaa/fheq-2024/4.17.b3."
  author-agent-dialogue: "Bring this up when a student asks what digital literacy asks of them by the end of the master's, or when a team maps digital and computational teaching across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Which digital method did you put to real work in your thesis, and what would the project have lost without it? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.7.b7
  forPractitioner: { text: "Every master's graduate will understand architectural research methods and their role in innovation-led decisions and advancing knowledge, and will apply suitable research or enquiry methods to projects.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your master's, at minimum, you will understand how research works in architecture and be able to choose and use the right research or enquiry methods in your own projects.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for research and enquiry-based literacy at the end of a master's in architecture, including the integrated master's: a threshold every graduate of the award will have reached, at FHEQ Level 7 and FQHEIS Level 11 (spine:7). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.7, literacy 7). Do not present it as an ARB or RIBA criterion or as the typical standard of a master's graduate, or the honours minimum. Set it beside the honours item 4.6.b7, 3.12 and 3.41 on the thesis and the master's descriptor items qaa/fheq-2024/4.17.b2 and qaa/fheq-2024/4.17.b4.2."
  author-agent-dialogue: "Bring this up when a student asks what research and enquiry-based literacy asks of them by the end of the master's, or when a team maps research methods and the thesis across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Which research method did your thesis rely on, and why was it the right one for your question? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.7.b8
  forPractitioner: { text: "Every master's graduate will understand codes of conduct, the principles of equity, diversity, inclusion and accessibility, the principles of advocacy, civic responsibility, climate justice and community engagement and the ethical effects of design decisions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your master's, at minimum, you will understand architects' codes of conduct and the principles of fairness, inclusion and access; you will also understand advocacy, civic responsibility, climate justice and community engagement and how design choices affect society, the environment and wellbeing.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for ethical and professional literacy at the end of a master's in architecture, including the integrated master's: a threshold every graduate of the award will have reached, at FHEQ Level 7 and FQHEIS Level 11 (spine:7). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.7, literacy 8). Do not present it as an ARB or RIBA criterion or as the typical standard of a master's graduate, or the honours minimum. Set it beside the honours item 4.6.b8 and theme:edi and the master's descriptor items qaa/fheq-2024/4.17.b8.2 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Bring this up when a student asks what ethical and professional literacy asks of them by the end of the master's, or when a team maps professional ethics and community engagement across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Who did your project speak up for, and how did you engage the community it affects? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.7.b9
  forPractitioner: { text: "Every master's graduate will understand the principles of architecture's professional, legal and business context: project management, procurement, contracts, policy, financial planning, cost management, planning, building codes and regulation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your master's, at minimum, you will understand how architecture works as a profession and a business, including managing projects, procurement, contracts, policy, budgets, the planning system, building regulations and compliance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for practice and business literacy at the end of a master's in architecture, including the integrated master's: a threshold every graduate of the award will have reached, at FHEQ Level 7 and FQHEIS Level 11 (spine:7). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.7, literacy 9). Do not present it as an ARB or RIBA criterion or as the typical standard of a master's graduate, or the honours minimum. Set it beside the honours item 4.6.b9, 3.9 and 2.27 on ARB's Academic Outcomes and the master's descriptor items qaa/fheq-2024/4.17.b1 and qaa/fheq-2024/4.17.b8.1."
  author-agent-dialogue: "Bring this up when a student asks what practice and business literacy asks of them by the end of the master's, or when a team maps professional practice teaching across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: How would the procurement route change the way your thesis project is delivered? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.7.b10
  forPractitioner: { text: "Every master's graduate will understand how local and global financial and economic forces shape proposals and project longevity, know core economic principles and have the numeracy to inform decisions on feasibility and business sustainability.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your master's, at minimum, you will understand how money and economics shape designs and how long projects last, know the core principles of economics and have the number skills to judge whether a project or practice is viable.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for financial and economic literacy at the end of a master's in architecture, including the integrated master's: a threshold every graduate of the award will have reached, at FHEQ Level 7 and FQHEIS Level 11 (spine:7). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.7, literacy 10). Do not present it as an ARB or RIBA criterion or as the typical standard of a master's graduate, or the honours minimum. Set it beside the honours item 4.6.b10 and 4.7.b9 and the master's descriptor items qaa/fheq-2024/4.17.b5 and qaa/fheq-2024/4.17.b8.2."
  author-agent-dialogue: "Bring this up when a student asks what financial and economic literacy asks of them by the end of the master's, or when a team maps cost, feasibility and practice management across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: Could you show, with figures, whether your scheme is feasible, and what would make it fail? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.7.b11
  forPractitioner: { text: "Every master's graduate will understand, interpret and collaborate with others to design for them, with self-awareness, self-regulation and skilled responsiveness, and will learn to speak up for others, form teams and raise shared wellbeing.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your master's, at minimum, you will be able to understand and work with others to design for them, knowing and managing yourself in creative work, standing up for others, building teams and improving wellbeing through work with communities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for emotional literacy at the end of a master's in architecture, including the integrated master's: a threshold every graduate of the award will have reached, at FHEQ Level 7 and FQHEIS Level 11 (spine:7). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.7, literacy 11). Do not present it as an ARB or RIBA criterion or as the typical standard of a master's graduate, or the honours minimum. Set it beside the honours item 4.6.b11, 1.4 and 1.17 and the master's descriptor items qaa/fheq-2024/4.17.b6 and qaa/fheq-2024/4.17.b8.1."
  author-agent-dialogue: "Bring this up when a student asks what emotional literacy asks of them by the end of the master's, or when a team maps teamwork and community engagement across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: When a team you were in hit conflict, what did you do, and what did it teach you about yourself? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
- statement: qaa/architecture-2026/4.7.b12
  forPractitioner: { text: "Every master's graduate will communicate complex architectural ideas clearly and effectively in verbal or non-verbal, written and visual forms, present to diverse audiences and produce coherent, critically informed documentation that serves design intent and practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your master's, at minimum, you will be able to explain complex architectural ideas clearly in speech or other forms, in writing and visually, present to different audiences and produce clear, critical documents that show your thinking, design intent and professional approach.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the minimum the statement sets for communication literacy at the end of a master's in architecture, including the integrated master's: a threshold every graduate of the award will have reached, at FHEQ Level 7 and FQHEIS Level 11 (spine:7). Cite it as (QAA, 2026, Architecture Subject Benchmark Statement, para 4.7, literacy 12). Do not present it as an ARB or RIBA criterion or as the typical standard of a master's graduate, or the honours minimum. Set it beside the honours item 4.6.b12 and 3.34 and the master's descriptor items qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Bring this up when a student asks what communication literacy asks of them by the end of the master's, or when a team maps presentation, writing and documentation across the course. Tell a student in plain words what they will be able to do at minimum; with staff, frame it as what every graduate of the award must be able to show. Ask: How did you explain your thesis differently to a client, a fellow designer and a member of the public? Make clear it is the floor, not the mark of a strong result, and do not read the definition out word for word."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.5; 2.11; 2.13" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.5; 2.13; 4.1" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.5; 2.12; 2.13" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.5; 2.13; 4.1" }
  - { id: "fheq:4", role: "cites", locator: "D1, 2.7 (exit award)" }
  - { id: "fheq:5", role: "cites", locator: "D1, 2.7 (exit award)" }
  - { id: "fqheis:7", role: "cites", locator: "D1, 2.7 (exit award)" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 2.7 (exit award)" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.12 (Scottish ordinary degree)" }
  - { id: "spine:6", role: "refers", locator: "std:ref:uk-framework R2, R8 (inferred: the honours minimum sits at this step)" }
  - { id: "spine:7", role: "refers", locator: "std:ref:uk-framework R2, R8 (inferred: the master's minimum sits at this step)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.5: honours degree \"(FHEQ Level 6; FQHEIS Level 10)\"; 2.13)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.5; 2.13; 4.1: \"Level 7 FHEQ/Level 11 FQHEIS\")" }
  - { from: "fheq:4", to: "fqheis:7", relation: "equivalent", basis: "stated (D1, 2.7: Certificate of Higher Education)" }
  - { from: "fheq:5", to: "fqheis:8", relation: "equivalent", basis: "stated (D1, 2.7: Diploma of Higher Education)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.6", "1.7", "1.8", "1.9", "1.10", "1.11", "2.9", "2.22", "3.33", "3.36", "3.37", "4.6", "4.7"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "2.15", "3.34", "3.36", "4.6", "4.7"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "3.33", "4.6", "4.7"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "1.35", "3.41"] }
- { id: "theme:genai", role: "carries", carriedIn: ["1.36", "1.37", "1.38", "1.39", "1.40", "2.1", "3.40", "4.6", "4.7"], note: "new theme id, proposed (Part E)" }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-architecture-<previous year>-benchmarks (not yet ingested)", note: "the front matter lists key changes from the previous statement and the back matter a 2020 advisory group; edition not stated (Part E)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree classification descriptions, cited for achievement above the minimum (4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ Levels 4 to 7 (2.5, 2.7, 2.11, 2.13, 4.1)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS and SCQF Levels 7 to 11 (2.5, 2.7, 2.12, 2.13, 4.1)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "the QAA / Advance HE ESD guidance, named without a date (1.20; edition inferred, Part E)" }
- { rel: "refersTo", target: "ARB accreditation requirements and Academic and Practice Outcomes (not yet ingested)", note: "front matter, 2.4, 2.25, 2.27, 2.28, 4.5" }
- { rel: "refersTo", target: "RIBA validation procedures and criteria (not yet ingested)", note: "front matter, 2.4, 2.10, 2.12, 2.25, 2.26, 2.28, 3.4, 4.5" }
- { rel: "refersTo", target: "QAA Quality Code (2024) and its Advice and Guidance on Partnerships (not yet ingested)", note: "front matter, 2.19" }
- { rel: "refersTo", target: "Equality and Human Rights Commission guidance on competence standards (not yet ingested)", note: "4.3" }
- { rel: "relatedTo", target: "std:doc:qaa-architectural-technology-2022-benchmarks; std:doc:qaa-landscape-architecture-2024-benchmarks; std:doc:qaa-history-of-art-architecture-and-design-2026-benchmarks", note: "neighbouring statements in the built environment and art history (inferred: not cited by the text)" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2026-04"
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
- Architecture joins the arts, sciences and humanities, combining creative and analytical approaches to the challenges of built and natural environments; architects act as communicators, coordinators and advocates (D1, 1.1).
- Design, broadly understood, is the defining skill: a method, a creative act, a technical discipline and a cultural practice (D1, 1.2).
- Design is contested, so the discipline advances by critique and asks students to live with the unknown and the unfinished (D1, 1.3).
- Work is collaborative and leads towards shared authorship and leadership of mixed teams (D1, 1.4, 3.19, 3.45).
- It is professionally oriented, with most courses validated or accredited, yet its learning transfers to many other careers (D1, 1.5, 1.30).
- Teaching centres on the studio as space, method and culture, with project-based learning and reviews (D1, 3.4, 3.15 to 3.22, 3.34).
- The statement frames the subject through twelve overlapping literacies that support an ethos of intelligent generalism (D1, front matter, 3.1 to 3.3).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "a profession seeking a more representative graduate body; inclusive studio culture and diverse voices; a decolonising rereading of history and theory; the hidden costs of materials, kit, trips and long studio hours; the strain of reviews (D1, 1.6 to 1.11, 3.33, 3.36, 3.37)"
  statements: ["qaa/architecture-2026/1.6", "qaa/architecture-2026/1.7", "qaa/architecture-2026/1.9", "qaa/architecture-2026/1.10", "qaa/architecture-2026/1.11", "qaa/architecture-2026/4.6.b8", "qaa/architecture-2026/4.7.b8"]
- theme: theme:accessibility
  inThisSubject: "legal duties for adjustments, with the subject's own expertise in accessible design as a reason to go further; neurodivergent students in the studio environment; flexible assessment and alternatives to in-person review (D1, 1.12 to 1.18, 2.15, 3.34)"
  statements: ["qaa/architecture-2026/1.12", "qaa/architecture-2026/1.14", "qaa/architecture-2026/1.17", "qaa/architecture-2026/1.18", "qaa/architecture-2026/3.34", "qaa/architecture-2026/4.6.b5", "qaa/architecture-2026/4.7.b5"]
- theme: theme:esd
  inThisSubject: "the climate and ecological emergency as a call for rapid change; climate literacy built across the course; regenerative design, whole life carbon and predictive tools; a critical stance on sustainability itself; providers leading by example (D1, 1.19 to 1.25, 3.33)"
  statements: ["qaa/architecture-2026/1.21", "qaa/architecture-2026/1.23", "qaa/architecture-2026/1.25", "qaa/architecture-2026/4.6.b4", "qaa/architecture-2026/4.7.b4"]
- theme: theme:enterprise
  inThisSubject: "named as employability, entrepreneurship and enterprise education: career readiness, placements, live projects, alumni networks and careers beyond the title of architect (D1, 1.26 to 1.35, 3.41)"
  statements: ["qaa/architecture-2026/1.31", "qaa/architecture-2026/1.35"]
- theme: theme:genai
  inThisSubject: "a fifth cross-cutting theme in this statement: GenAI in industry and its ethical, IP, data and bias issues; authorship and process in assessment; use policies; inclusive and affordable use (D1, 1.36 to 1.40, 3.40)"
  statements: ["qaa/architecture-2026/1.37", "qaa/architecture-2026/1.38", "qaa/architecture-2026/1.40", "qaa/architecture-2026/4.6.b6", "qaa/architecture-2026/4.7.b6"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.3", gloss: "the twelve literacies as the frame for content" }
  - { component: "3.5", gloss: "around design: technology and environmental science, history and theory, professional practice" }
  - { component: "3.7", gloss: "architectural humanities: critical, historical and theoretical enquiry" }
  - { component: "3.8", gloss: "technology: construction, structure, physics, materials and circular systems, environmental technologies, BIM and computation" }
  - { component: "3.9", gloss: "professional practice: ethics, law, business, finance, procurement, planning, policy and regulation" }
  - { component: "3.13", gloss: "postgraduate specialisms: conservation, reuse and retrofit, computation, net zero design, housing and urbanism" }
practices:
  - { component: "3.4", kind: "assessment", gloss: "integrated design studio projects, at least half the assessed work in RIBA-validated courses" }
  - { component: "3.6", kind: "teaching", gloss: "lectures, seminars, workshops, site visits and specialist facilities" }
  - { component: "3.14", kind: "teaching", gloss: "direct instruction, tutorials and independent study" }
  - { component: "3.15", kind: "teaching", gloss: "studio as space, method and community of practice, with remote and block variants" }
  - { component: "3.16", kind: "learning", gloss: "socialised and peer learning in the studio" }
  - { component: "3.19", kind: "learning", gloss: "co-authored group design projects" }
  - { component: "3.21", kind: "teaching", gloss: "one-to-one and small group tutorials with practitioners" }
  - { component: "3.29", kind: "teaching", gloss: "specialist teaching applied and tested in studio" }
  - { component: "3.31", kind: "learning", gloss: "practice experience, placements and mentoring" }
  - { component: "3.32", kind: "learning", gloss: "live projects and fabrication builds with clients" }
  - { component: "3.33", kind: "learning", gloss: "site and study visits" }
  - { component: "3.34", kind: "assessment", gloss: "reviews for feedback and formative assessment" }
  - { component: "3.38", kind: "assessment", gloss: "scaffolded assessment with self and peer evaluation" }
  - { component: "3.39", kind: "assessment", gloss: "continual formative and summative feedback" }
  - { component: "3.40", kind: "assessment", gloss: "varied tasks that capture the design process" }
  - { component: "3.42", kind: "assessment", gloss: "the portfolio as synoptic assessment" }
  - { component: "3.45", kind: "assessment", gloss: "group work with collective and individual contributions" }
  - { component: "3.47", kind: "assessment", gloss: "peer, student-led and self-assessment" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.6", award: "bachelor's with honours", items: 12, wording: "minimum standards: 'the minimum requirement that graduates ... can be expected to reach'" }
  - { rung: "threshold", leadIn: "4.7", award: "master's", items: 12, wording: "minimum standards, the same lead-in for the master's" }
  - { rung: "typical", leadIn: "none", award: "none", items: 0 }
  - { rung: "excellent", leadIn: "none", award: "none", items: 0 }
rungBases: "threshold only, stated as 'minimum standards' (4.1, 4.6, 4.7); performance above it is left to Annex D (4.2). Records with rung threshold: 24, the two lists; 2.3 and 4.1 speak of the threshold but are not list items and carry rung none"
outcomeLists:
  - { leadIn: "3.3", gloss: "the twelve literacies named, one record (3.3); defined in 4.6 and 4.7", items: 1, award: ["honours", "master's"] }
outcomes:
  - { outcome: "design literacy (honours)", threshold: "qaa/architecture-2026/4.6.b1", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "visual and spatial literacy (honours)", threshold: "qaa/architecture-2026/4.6.b2", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "cultural and contextual literacy (honours)", threshold: "qaa/architecture-2026/4.6.b3", typical: "none", excellent: "none", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "climate and ecological literacy (honours)", threshold: "qaa/architecture-2026/4.6.b4", typical: "none", excellent: "none", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "technical and building environment literacy (honours)", threshold: "qaa/architecture-2026/4.6.b5", typical: "none", excellent: "none", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "digital literacy (honours)", threshold: "qaa/architecture-2026/4.6.b6", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "research and enquiry-based literacy (honours)", threshold: "qaa/architecture-2026/4.6.b7", typical: "none", excellent: "none", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "ethical and professional literacy (honours)", threshold: "qaa/architecture-2026/4.6.b8", typical: "none", excellent: "none", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "practice and business literacy (honours)", threshold: "qaa/architecture-2026/4.6.b9", typical: "none", excellent: "none", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "financial and economic literacy (honours)", threshold: "qaa/architecture-2026/4.6.b10", typical: "none", excellent: "none", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "emotional literacy (honours)", threshold: "qaa/architecture-2026/4.6.b11", typical: "none", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "communication literacy (honours)", threshold: "qaa/architecture-2026/4.6.b12", typical: "none", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "design literacy (master's)", threshold: "qaa/architecture-2026/4.7.b1", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "master's" }
  - { outcome: "visual and spatial literacy (master's)", threshold: "qaa/architecture-2026/4.7.b2", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "master's" }
  - { outcome: "cultural and contextual literacy (master's)", threshold: "qaa/architecture-2026/4.7.b3", typical: "none", excellent: "none", basis: "stated", domain: "understanding", award: "master's" }
  - { outcome: "climate and ecological literacy (master's)", threshold: "qaa/architecture-2026/4.7.b4", typical: "none", excellent: "none", basis: "stated", domain: "understanding", award: "master's" }
  - { outcome: "technical and building environment literacy (master's)", threshold: "qaa/architecture-2026/4.7.b5", typical: "none", excellent: "none", basis: "stated", domain: "understanding", award: "master's" }
  - { outcome: "digital literacy (master's)", threshold: "qaa/architecture-2026/4.7.b6", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "master's" }
  - { outcome: "research and enquiry-based literacy (master's)", threshold: "qaa/architecture-2026/4.7.b7", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "master's" }
  - { outcome: "ethical and professional literacy (master's)", threshold: "qaa/architecture-2026/4.7.b8", typical: "none", excellent: "none", basis: "stated", domain: "understanding", award: "master's" }
  - { outcome: "practice and business literacy (master's)", threshold: "qaa/architecture-2026/4.7.b9", typical: "none", excellent: "none", basis: "stated", domain: "understanding", award: "master's" }
  - { outcome: "financial and economic literacy (master's)", threshold: "qaa/architecture-2026/4.7.b10", typical: "none", excellent: "none", basis: "stated", domain: "understanding", award: "master's" }
  - { outcome: "emotional literacy (master's)", threshold: "qaa/architecture-2026/4.7.b11", typical: "none", excellent: "none", basis: "stated", domain: "generic-skill", award: "master's" }
  - { outcome: "communication literacy (master's)", threshold: "qaa/architecture-2026/4.7.b12", typical: "none", excellent: "none", basis: "stated", domain: "generic-skill", award: "master's" }
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
- { body: "Architects Registration Board (ARB)", says: "the statutory regulator under the Architects Act 1997: protects the title of architect, keeps the register and accredits courses; from January 2028 accredits only UK master's-level qualifications with the Academic Outcomes and practice qualifications with the Practice Outcomes, or combined ones; its outcomes apply to recognised degrees (D1, front matter, 2.4, 2.25, 2.27, 2.28, 4.5)", requirements: "not yet ingested (Part E)" }
- { body: "Royal Institute of British Architects (RIBA)", says: "a professional membership body that validates qualifications worldwide at Parts 1, 2 and 3, all needed for Chartered Membership, which is separate from the title of architect and not a legal requirement; validated courses give at least half the assessed work to integrated design studio projects (D1, front matter, 2.4, 2.10, 2.12, 2.25, 2.26, 2.28, 3.4, 4.5)", requirements: "not yet ingested (Part E)" }
- { body: "national apprenticeship trailblazer groups", says: "set requirements for the Level 6 and Level 7 architecture apprenticeships, which providers should consult (D1, 2.10)", requirements: "not yet ingested (Part E)" }
- { body: "Equality and Human Rights Commission", says: "its latest guidance is to be followed where a provider develops competence standards (D1, 4.3)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equity, diversity and inclusion (EDI)", carriedIn: ["front matter", "1.6", "1.7", "1.8", "1.9", "1.10", "1.11", "2.9", "2.22", "3.33", "3.36", "3.37", "4.6", "4.7"], statements: ["1.6", "1.7", "1.9", "1.10", "1.11", "2.9", "3.33", "3.36", "3.37", "4.6.b8", "4.7.b8"] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["front matter", "1.11", "1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "2.15", "3.34", "3.36", "4.6", "4.7"], statements: ["1.12", "1.14", "1.17", "1.18", "2.15", "3.34", "3.44", "4.6.b5", "4.7.b5"] }
  - { id: "theme:esd", named: "Education for sustainable development (ESD)", carriedIn: ["front matter", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "2.1", "3.33", "4.6", "4.7"], statements: ["1.21", "1.23", "1.25", "3.33", "4.6.b4", "4.7.b4"] }
  - { id: "theme:enterprise", named: "Employability, entrepreneurship and enterprise education (EEE)", carriedIn: ["front matter", "1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "1.35", "3.41"], statements: ["1.31", "1.35"] }
  - { id: "theme:genai", named: "Generative artificial intelligence (GenAI)", carriedIn: ["front matter", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "2.1", "3.40", "4.6", "4.7"], statements: ["1.37", "1.38", "1.40", "3.40", "4.6.b6", "4.7.b6"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["2.5", "2.7", "2.11", "2.13", "4.1"] }
  - { framework: "scqf", levels: ["fqheis:7", "fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.5", "2.7", "2.12", "2.13", "4.1"], note: "cited as FQHEIS (2.5, 2.7, 4.1) and as SCQF/FQHEIS (2.12, 2.13)" }
  - { framework: "other: apprenticeship levels L6 and L7", levels: ["fheq:6", "fheq:7"], citedIn: ["2.10", "2.16"], note: "level read as FHEQ (inferred)" }
bodies:
  - { body: "Architects Registration Board", citedIn: ["front matter", "2.4", "2.25", "2.27", "2.28", "4.5"] }
  - { body: "Royal Institute of British Architects", citedIn: ["front matter", "2.4", "2.10", "2.12", "2.25", "2.26", "2.28", "3.4", "4.5"] }
  - { body: "PSRBs, unnamed", citedIn: ["front matter", "1.5", "1.32", "2.4", "2.24", "2.25", "2.28", "2.30", "3.2", "3.9", "3.31", "4.3", "4.5"] }
  - { body: "national apprenticeship trailblazer groups", citedIn: ["2.10"] }
  - { body: "Equality and Human Rights Commission", citedIn: ["4.3"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
  - { body: "UNESCO", citedIn: ["1.20"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "descriptions of the four honours classifications, for achievement above the minimum" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "the QAA / Advance HE Education for Sustainable Development guidance", citedIn: ["1.20"], role: "a source for curriculum design and pedagogy in sustainability (edition not stated: Part E)" }
  - { document: "QAA Quality Code, 2024 update (not yet ingested: Part E)", named: "an update to the Quality Code", citedIn: ["front matter"], role: "a further reference point when using the statement" }
  - { document: "QAA Quality Code Advice and Guidance on Partnerships (not yet ingested: Part E)", named: "the Quality Code Advice and Guidance on Partnerships", citedIn: ["2.19"], role: "further detail for partnership delivery" }
  - { document: "QAA Glossary (not ingested: Part E)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "UN Sustainable Development Goals and competences (not ingested)", named: "the UN Sustainable Development Goals (SDGs)", citedIn: ["front matter", "1.20"], role: "a holistic model for the literacies and a possible frame for ESD" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "literacy", definition: "the ability to find, read, judge and use information within a particular field of knowledge or practice; the statement frames its standards as twelve of them (D1, 3.1, 3.3)", beneficiaryDefinition: "being able to find, understand, judge and use what matters in one area of architecture", scopeNote: "twelve named; defined for honours in 4.6 and master's in 4.7", category: "unknown", practices: ["education"] }
- { slug: "studio", definition: "both the physical workspace for design and the teaching methods and culture around it, a community of practice (D1, 3.15, 3.16)", beneficiaryDefinition: "the shared space where you design, and the way of learning that goes on there", scopeNote: "now includes digital and remote formats (3.15)", category: "unknown", practices: ["education"] }
- { slug: "review", definition: "a session in which students present design work, finished or in progress, for discussion and immediate feedback from peers, tutors and practitioners (D1, 3.34)", beneficiaryDefinition: "a session where you show your design and get feedback from others", scopeNote: "also called crits in practice (recall, not in the text)", category: "unknown", practices: ["education"] }
- { slug: "placement", definition: "a period of credit-rated practice work taken during an undergraduate or master's course (D1, 1.31)", beneficiaryDefinition: "time spent working in practice for credit during your course", scopeNote: "distinct from a year out in practice (2.8)", category: "unknown", practices: ["education"] }
- { slug: "school", definition: "an organisational group holding several courses; may be called a department, programme or subject elsewhere (D1, front matter)", scopeNote: "the statement uses provider for the awarding organisation", category: "unknown", practices: ["education"] }
- { slug: "course", definition: "an approved route of study made of modules leading to an undergraduate or postgraduate qualification (D1, front matter)", scopeNote: "used for what other statements call a programme", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "literacy", form: "literacies", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "studio", form: "studio", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "review", form: "review", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "placement", form: "placement", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "school", form: "school", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "course", form: "course", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", from: "studio", to: "review", note: "reviews are a studio practice (3.25, 3.34)" }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement Architecture"
  edition: "April 2026 (Fourth Edition)"
  year: 2026
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/architecture-2026/architecture-2026.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: d7d10b2df272f178173603ea94e1ebc61b68cd5871662b75073433129c920b9a
  heldFiles: ["wkspc2601-library/txt/qaa-2026-architecture-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2026-architecture-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2026-architecture-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2026-architecture-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0030", citation: "ARB accreditation handbook and the Academic and Practice Outcomes (from January 2028)", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0031", citation: "RIBA validation procedures and criteria", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0032", citation: "the previous QAA Subject Benchmark Statement for Architecture (2020, recall)", settles: ["S7", "S8"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- Rungs: no typical or excellent rung. The statement sets minimum standards only, with lead-ins in 4.6 (honours) and 4.7 (master's): "the minimum requirement that graduates ... can be expected to reach". Recorded as rung threshold, force threshold, 12 items each. A new lead-in wording against Psychology ("minimum requirement ... can be expected to reach", no modal verb in the list).
- Two awards on one threshold rung: the honours minimum (FHEQ 6, FQHEIS 10) and the master's minimum, including the integrated master's (FHEQ 7, FQHEIS 11), each a full list of the same twelve literacies. No gradeOf link: SB-3 links one rung below within the same award, and the master's list is a different award, not a rung. The honours and master's items with the same number are the same named literacy (stated by name), recorded side by side in SB4 outcomes.
- The SB4 rung count: 24 records carry rung threshold, 12 per list. 2.3 (joint honours students reach the core of the threshold standards) and 4.1 (the definition of the minimum standards) speak of the threshold but are not rung list items, so they carry rung none and type expectation. For P3.
- The list items are cut from running text with find= (no line breaks in the held text): the skeleton gave 4.6 and 4.7 as single paragraphs with no stems. 4.6.b1 spans a page break ("Design\n\n25\nliteracy"), kept as held. The heading "Subject knowledge, understanding, skills and abilities" sits in each lead-in, not in the items. The skeleton's rung counts (0) were wrong for this text.
- 3.3 names the twelve literacies with "a graduate is expected to have acquired": one record, not twelve, since the names alone carry no standard and 4.6 and 4.7 define them. The issuer's word is "is expected to", not one of the five; recorded as force will, for P3.
- 1.12: the issuer's word is "legally required" (the Acts named), recorded as force must, for P3. 1.35, 1.37 and 3.34: "will need to", recorded as will.
- Obliging paragraphs not recorded, because their obliging word is not one of the five: 1.36 ("needs to adapt"), 1.39 ("It is the responsibility of schools and providers"), 2.17 ("it is important that ... continue to meet the academic threshold standards"), 3.24 ("Careful consideration needs to be"), 3.26 ("courses need to"). 3.38's "must" describes what deep learning involves, not a duty: not recorded. 2.5 and 2.6 ("it is expected that", "it would be expected that") describe progression: not recorded. For P3.
- Paragraphs with only "may", "can" or "are encouraged" are descriptive and kept as S3 components (D-std-0002 (a)).
- A fifth cross-cutting theme, Generative artificial intelligence, is named in the front matter as one of the statement's themes: new theme id theme:genai proposed (no shared record yet). The theme is new to the series against Psychology.
- Theme naming differs from Psychology: "equity, diversity and inclusion" (not equality); "employability, entrepreneurship and enterprise education (EEE)", with sub-headings "Career readiness for EEE" and "Situated learning for EEE" (1.28, 1.31).
- Subject codes: hecos 100122 and CAH13-01-01 match the subject named; CAH13-01 is its parent. hecos 100583 architectural design is inferred (the text does not name it as a subject) and held back from lookup until P3.
- Edition: "Fourth Edition", published 16 April 2026; advisory groups listed for 2026, 2020, 2010 and 2000. The previous statement is not named or dated in the text; supersedes recorded generically.
- S7 relatedTo the architectural technology, landscape architecture and history of art statements is inferred from subject proximity; the text cites none of them.
- ESD guidance: 1.20 names "the QAA / Advance HE Education for Sustainable Development guidance" without a year; linked to std:doc:qaa-advancehe-esd-2021-guidance (inferred edition).
- The level ids spine:6 and spine:7 in S5 and each aaw are inferred from std:ref:uk-framework R2 and R8; the FHEQ descriptor ids each aaw names (qaa/fheq-2024/4.15.* for honours, 4.17.* for master's) are our pairing by content, inferred.
- Apprenticeship levels "L6" and "L7" (2.10, 2.16) are read as FHEQ levels (inferred; the text does not name the framework).
- Issuer typos and extraction noise kept in the held text: "PRSBs" for PSRBs (1.5); "paragraphs 1.12-1 8" (2.9, meaning 1.12 to 1.18); "s chool" (front matter); "rigor" (4.7.b2); "Well -equipped" (3.24). The line "3.16 and 3.45." is the end of a cross-reference in 3.19 ("as described in paragraph"), not paragraphs 3.16 or 3.45 (DPN-1); the skeleton kept it inside 3.19 correctly.
- Cross-references read as references, never statements (DPN-1): 1.11 (3.15, 3.32; note 3.32 is live projects, and reviews are defined in 3.34, an issuer cross-reference error), 2.9, 2.16, 3.19, 3.22, 3.25 (3.34, 3.42), 3.31 (2.25 to 2.28; 1.30 to 1.34), 3.33 (1.10), 4.5 (2.18 to 2.22), front matter (2.25 to 2.28).
- Most S4 records are provider duties (38 of 68 have no student version); the statement states its learner standards almost entirely in the two literacy lists.
- P2: no trigger beyond the inferred codes, theme id and edition links, which P3 settles; S9 not researched.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:15: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0087 (P1); built by tools/bm_build.py.
