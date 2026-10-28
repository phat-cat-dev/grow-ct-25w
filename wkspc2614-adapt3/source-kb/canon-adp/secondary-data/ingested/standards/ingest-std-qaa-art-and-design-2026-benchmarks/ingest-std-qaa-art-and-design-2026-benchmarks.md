---
id: std:doc:qaa-art-and-design-2026-benchmarks
title: "Subject Benchmark Statement Art and Design"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "101361", label: "creative arts and design", basis: "inferred" }
  - { scheme: "hecos", code: "100059", label: "fine art", basis: "inferred" }
  - { scheme: "hecos", code: "100048", label: "design", basis: "inferred" }
  - { scheme: "cah", code: "CAH25-01-01", label: "creative arts and design (non-specific)", basis: "inferred" }
  - { scheme: "cah", code: "CAH25-01-02", label: "art", basis: "inferred" }
  - { scheme: "cah", code: "CAH25-01-03", label: "design studies", basis: "inferred" }
edition: "April 2026 (fifth edition)"
published: 2026-04
status: current
supersedes: "the fourth edition, 2019 (a minor update of the 2016 statement) (D1, back matter)"
heldText: { method: sha256-bytes, raw: a36e11f8640452d59e5810ec755b4f3983e7014f7267c29ad88ae2c91eb89193, normalised: 71c3b33d7aecfc984db8915dbc3c47c840cb344f40eb9c25c3692a700ee0c816 }
heldTextStan: { method: sha256-stan, raw: a36e11f8640452d59e5810ec755b4f3983e7014f7267c29ad88ae2c91eb89193, normalised: ccd11de5896cc0f854ccc0b489393901ea4689afaf33eb0a10b12d7578ac5eef }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2026 revision (fifth edition for Art and Design)"
awardsCovered: ["bachelor's with honours", "master's", "integrated master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing (front matter; 1.2; 3.31)"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0088 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:31"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Art and Design (QAA, April 2026)

> Run 0088, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2026-art-design-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in Art and Design should know, do and understand at the end of an honours degree, with a short set of master's outcomes: one table of fourteen attributes, each described at three rungs (threshold, typical, excellent), and twelve outcomes master's graduates typically reach. Reach for it when designing, reviewing or describing an art or design course, its modules or its outcomes. It is not a curriculum, not a professional body's accreditation standard and, in England, not a sector-recognised standard.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2026 as the fifth edition, the statement describes Art and Design as a practice-based, student-centred subject of making and creative inquiry; sets out five cross-cutting themes (equity, diversity and inclusion; accessibility and the needs of disabled students; education for sustainable development; employability, entrepreneurship and enterprise education; generative AI); covers course design, progression, flexibility, partnership and review, and the content, teaching, assessment and feedback of a course; and gives benchmark standards as one table (Table 1) of fourteen attributes at threshold, typical and excellent for bachelor's degrees with honours, a master's list in 4.7 and a note on integrated master's. It points to Annex D of the 2024 Frameworks for the degree classes, cites the FHEQ and FQHEIS levels, and names PSRBs, two accrediting bodies and three non-accrediting professional bodies.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Art and Design"
edition: "April 2026 (fifth edition)"
dates:
  published: 2026-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector-owned reference point, not a regulatory requirement; in England not a sector-recognised standard under the OfS framework; part of the quality arrangements in Scotland, Wales and Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2026", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what an Art and Design graduate can be expected to know, do and understand at the end of their studies, and the nature and characteristics of awards in the subject (D1, front matter: About this Statement; 4.1)"
appliesTo:
  awards: ["bachelor's degrees with honours (single honours, joint and combined)", "master's degrees (taught postgraduate)", "integrated master's degrees (4.8)"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This QAA Subject Benchmark Statement for Art and Design defines what can be expected of a graduate in terms of what they might know, do and understand at the end of their studies.\" (D1, front matter: About this Statement)"
statedSubjects:
  - { name: "Art and Design", locator: "(D1, title; 1.2)", kind: "subject", codes: [{ scheme: "hecos", code: "101361", label: "creative arts and design" }, { scheme: "cah", code: "CAH25-01-01", label: "creative arts and design (non-specific)" }] }
  - { name: "single honours award or part of a broader interdisciplinary degree", locator: "(D1, 2.10)", kind: "programme title", codes: [{ scheme: "hecos", code: "101361", label: "creative arts and design" }] }
  - { name: "combined or joint degree, including major and minor options", locator: "(D1, 2.14)", kind: "programme title", codes: [{ scheme: "hecos", code: "101361", label: "creative arts and design" }] }
  - { name: "product design", locator: "(D1, 2.23)", kind: "specialism", codes: [{ scheme: "hecos", code: "100050", label: "product design" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of an Art and Design degree", gloss: "the subject amid technological and cultural change" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of an Art and Design degree", gloss: "'subject' and 'disciplines' defined" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context and purposes of an Art and Design degree", gloss: "room for providers to weight the subject locally" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Art and Design degree", gloss: "breadth of disciplines; practice-based pedagogy" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Art and Design degree", gloss: "conceiving, testing, making and sharing work" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Art and Design degree", gloss: "visual, spatial and sensory languages; wider value" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Art and Design degree", gloss: "studios, workshops and flexible study modes" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Art and Design degree", gloss: "links with other subjects and sectors" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Art and Design degree", gloss: "graduate resourcefulness and careers" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "diverse practices; reflexivity and individual voice" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "national access and equality policies by nation" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "values of an inclusive learning community" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "legacies of exclusion and how they are countered" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "inclusion across the student life cycle" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "inclusive practice as a source of innovation" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "dialogue and co-created curriculum" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessibility as a core value; disabled and neurodiverse students" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "open admissions; portfolio entry" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "reasonable and anticipatory adjustments" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessible live learning activities" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessible studios; quiet areas" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "hybrid learning and its limits for access" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "making as evidence of learning" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "flexible assessment formats" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainable development and its reference points" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "core skills for sustainability; climate literacy" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "creative pedagogies for linked global challenges" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "regenerative creative practice" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "industry partnerships for sustainability" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "working with STEM and other fields on global issues" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "tools for sustainability awareness" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainability, inclusion and ethics in curricula" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "responsible digital practice" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "the value graduates create through careers" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "technical, entrepreneurial and emotional capacities" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "enterprise education and IP-led businesses" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "agility for changing creative careers" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "practice-based and experiential learning" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "interpersonal and leadership competences" }
  - { number: "1.40", order: 42, componentType: stem, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "skills for creative economies (a list of thirteen)" }
  - { number: "1.41", order: 43, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "the subject and emerging technologies" }
  - { number: "1.42", order: 44, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "GenAI literacies and ethics" }
  - { number: "1.43", order: 45, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "a spectrum of GenAI use; own position" }
  - { number: "1.44", order: 46, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "GenAI as one tool among many" }
  - { number: "1.45", order: 47, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "authentic assessment including GenAI" }
  - { number: "1.46", order: 48, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "agency and authorship with GenAI" }
  - { number: "1.47", order: 49, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "GenAI and creative labour" }
  - { number: "1.48", order: 50, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "bias in GenAI and cultural visibility" }
  - { number: "1.49", order: 51, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "environmental cost of GenAI" }
  - { number: "1.50", order: 52, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI)", gloss: "intellectual property and GenAI" }
  - { number: "2.1", order: 54, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "a spectrum of practices and theories" }
  - { number: "2.2", order: 55, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "course design models and reference points" }
  - { number: "2.3", order: 56, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "disciplinary or flexible curricula" }
  - { number: "2.4", order: 57, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "interdisciplinary and specialist courses" }
  - { number: "2.5", order: 58, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "learning through making and change-making" }
  - { number: "2.6", order: 59, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "student-centred experiential learning" }
  - { number: "2.7", order: 60, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "live and inquiry-led learning" }
  - { number: "2.8", order: 61, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "varied assessment" }
  - { number: "2.9", order: 62, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "contextual and critical awareness" }
  - { number: "2.10", order: 63, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "undergraduate study: single and combined" }
  - { number: "2.11", order: 64, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "diverse postgraduate provision" }
  - { number: "2.12", order: 65, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression across levels to the threshold" }
  - { number: "2.13", order: 66, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "readiness for postgraduate study" }
  - { number: "2.14", order: 67, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined degrees" }
  - { number: "2.15", order: 68, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards" }
  - { number: "2.16", order: 69, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "duration in England, Wales and Northern Ireland" }
  - { number: "2.17", order: 70, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "Scottish degrees and levels" }
  - { number: "2.18", order: 71, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "integrated master's length and levels" }
  - { number: "2.19", order: 72, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "part-time routes" }
  - { number: "2.20", order: 73, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes, formats and credit" }
  - { number: "2.21", order: 74, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "validation, franchising and apprenticeships" }
  - { number: "2.22", order: 75, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "commercial practice through partnership" }
  - { number: "2.23", order: 76, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "accreditation and professional bodies" }
  - { number: "2.24", order: 77, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.25", order: 78, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "externality in review" }
  - { number: "2.26", order: 79, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners in studios" }
  - { number: "2.27", order: 80, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners' role and reports" }
  - { number: "2.28", order: 81, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "professional and regulatory accreditation" }
  - { number: "3.1", order: 83, componentType: paragraph, parent: "section 3", heading: "Content, structure and delivery", gloss: "what the section covers" }
  - { number: "3.2", order: 84, componentType: area, parent: "section 3", heading: "Content", gloss: "curricula responding to change" }
  - { number: "3.3", order: 85, componentType: area, parent: "section 3", heading: "Content", gloss: "four typical areas of study" }
  - { number: "3.4", order: 86, componentType: area, parent: "section 3", heading: "Content", gloss: "aims of courses" }
  - { number: "3.5", order: 87, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "range of teaching and learning methods" }
  - { number: "3.6", order: 88, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "studio, lecture and project learning" }
  - { number: "3.7", order: 89, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "learning resources and technical staff" }
  - { number: "3.8", order: 90, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "scheduled and independent learning" }
  - { number: "3.9", order: 91, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "module outcomes building across levels" }
  - { number: "3.10", order: 92, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "student-centred pedagogy" }
  - { number: "3.11", order: 93, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "discursive subject learning" }
  - { number: "3.12", order: 94, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "staff practice, scholarship and CPD" }
  - { number: "3.13", order: 95, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "in-person and online delivery" }
  - { number: "3.14", order: 96, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "group work and employability" }
  - { number: "3.15", order: 97, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "interdisciplinary collaboration" }
  - { number: "3.16", order: 98, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "industry and enterprise activities" }
  - { number: "3.17", order: 99, componentType: paragraph, parent: "section 3", heading: "Assessment and feedback", gloss: "why assessment and feedback matter" }
  - { number: "3.18", order: 100, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "diverse, inclusive assessment" }
  - { number: "3.19", order: 101, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "holistic assessment of a submission" }
  - { number: "3.20", order: 102, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "co-designed assessment" }
  - { number: "3.21", order: 103, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessing process and product" }
  - { number: "3.22", order: 104, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment in professional settings" }
  - { number: "3.23", order: 105, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "self and peer assessment" }
  - { number: "3.24", order: 106, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "new forms of assessment; integrity" }
  - { number: "3.25", order: 107, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment methods (a list of fourteen)" }
  - { number: "3.26", order: 108, componentType: practice, parent: "section 3", heading: "Feedback", gloss: "feedback as part of learning" }
  - { number: "3.27", order: 109, componentType: practice, parent: "section 3", heading: "Feedback", gloss: "continuous feedback" }
  - { number: "3.28", order: 110, componentType: practice, parent: "section 3", heading: "Feedback", gloss: "formal and informal feedback settings" }
  - { number: "3.29", order: 111, componentType: practice, parent: "section 3", heading: "Feedback", gloss: "situational feedback" }
  - { number: "3.30", order: 112, componentType: practice, parent: "section 3", heading: "Feedback", gloss: "feedback co-constructed with students" }
  - { number: "3.31", order: 113, componentType: practice, parent: "section 3", heading: "Feedback", gloss: "the 'crit' and inclusive review" }
  - { number: "3.32", order: 114, componentType: practice, parent: "section 3", heading: "Feedback", gloss: "formats of feedback" }
  - { number: "4.1", order: 116, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "what the standards are" }
  - { number: "4.2", order: 117, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed threshold; Annex D" }
  - { number: "4.3", order: 118, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "competence standards and the Equality Act" }
  - { number: "4.4", order: 119, componentType: paragraph, parent: "section 4", heading: "Undergraduate degrees: threshold, typical and excellent standards", gloss: "Table 1: fourteen attributes at three rungs" }
  - { number: "4.5", order: 120, componentType: paragraph, parent: "section 4", heading: "Postgraduate degrees", gloss: "master's beyond the honours standards" }
  - { number: "4.6", order: 121, componentType: paragraph, parent: "section 4", heading: "Postgraduate degrees", gloss: "kinds of postgraduate course" }
  - { number: "4.7", order: 122, componentType: stem, parent: "section 4", heading: "Postgraduate degrees", gloss: "outcomes for master's graduates (a list of twelve)" }
  - { number: "4.8", order: 123, componentType: paragraph, parent: "section 4", heading: "Integrated master's", gloss: "integrated master's at level 7" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of an Art and Design degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of Art and Design", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and Part B" }
  - { number: "none", heading: "section heading lines 1 to 4", kind: "other: headings, recorded in S3 as sections" }
  - { number: "5", heading: "Membership of the Advisory Group (2026, 2019, 2016, 2008, 2002)", kind: "other: back matter, read for S8 and supersedes" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 62 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/art-and-design-2026/1.19
  locator: { number: "1.19", headingPath: ["Context and purposes of an Art and Design degree", "Accessibility and the needs of disabled students"] }
  span: { start: 17789, end: 18566 }
  source: "1.19 Under the Equality Act 2010, higher education providers must make reasonable adjustments to support disabled students and ensure they can fully participate in academic life. Designing accessible courses benefits all students and helps create an inclusive learning environment. In Art and Design, this means building flexibility into teaching materials and structures, and making anticipatory adjustments. This may include sharing briefing materials in advance, offering alternative formats for lectures or course content, and providing support such as one-to-one assistance, or specialist equipment. Collaborative practice and group work are a common feature in Art and Design courses, and this is also an area where reasonable adjustments are required for some students.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "higher education providers offering the subject"
  addressee: provider
  verbs: ["make", "support", "ensure", "required"]
  about: "reasonable and anticipatory adjustments for disabled students"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Under the Equality Act 2010 providers must adjust reasonably so disabled students take a full part in academic life; in this subject that means flexible materials and structures, adjustments made in advance, and adjustments in group and collaborative work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/art-and-design-2026/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of Art and Design", "Progression"] }
  span: { start: 41468, end: 42215 }
  source: "2.12 Over the course of a standard undergraduate degree with honours (FHEQ Level 6; FQHEIS Level 10) or, if available, an integrated master's degree (FHEQ Level 7; FQHEIS Level 11), an Art and Design student will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the attainment of knowledge, expertise and experience that builds towards the final achievement of meeting the threshold (and, if specified, higher-level) subject- specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on an honours or integrated master's course"
  addressee: learner
  verbs: ["progress"]
  about: "progression across levels towards the threshold skills"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "An Art and Design student will move from level to level under each institution's rules, each level adding knowledge, expertise and experience towards meeting the threshold (and any higher) subject and generic skills, usually by passing and gaining credit for all learning and assessment, practical work included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of Art and Design", "Progression"] }
  span: { start: 42628, end: 43114 }
  source: "2.14 Undergraduates studying Art and Design courses as part of a combined or joint degree with other subjects (including courses that specify major and minor options) will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the areas covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study.\n\n13\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students taking the subject in a joint or combined degree"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "joint and combined degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students who take Art and Design within a joint or combined degree, major and minor included, will reach the core of the subject and generic skills set out here and will add others from their other subject; they may also work where the disciplines overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/2.24
  locator: { number: "2.24", headingPath: ["Distinctive features of Art and Design", "Monitoring and review"] }
  span: { start: 47276, end: 47920 }
  source: "2.24 Degree-awarding bodies, and their collaborative partnerships, routinely collect and analyse information and undertake periodic course review according to their own needs. Considering the student voice will form part of this. They draw on a range of external reference points, including this Statement, to ensure that their provision aligns with sector norms. Monitoring and evaluation are a periodic assessment of a course, conducted internally or by external independent evaluators. Evaluation uses information from both current and historic monitoring to develop an understanding of student achievement or inform future course planning.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "degree-awarding bodies and their partners"
  addressee: provider
  verbs: ["form"]
  about: "student voice in monitoring and review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Degree-awarding bodies and their partners collect and analyse information and review courses periodically to their own needs; taking account of what students say will form part of this, alongside external reference points such as this statement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/art-and-design-2026/2.25
  locator: { number: "2.25", headingPath: ["Distinctive features of Art and Design", "Monitoring and review"] }
  span: { start: 47920, end: 48218 }
  source: "2.25 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers as part of periodic review to gain an independent perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Externality is essential to UK quality assurance: providers will bring in external reviewers in periodic review, for an independent view of proposed changes and to make sure threshold standards are met and the content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/art-and-design-2026/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65943, end: 66428 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers awarding honours"
  addressee: provider
  verbs: ["refer"]
  about: "Annex D for evidence of classification"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will perform well above the minimum; each provider decides what counts as evidence of that and should consult Annex D of the 2024 Frameworks, which describes the four honours classes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/art-and-design-2026/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 66428, end: 66904 }
  source: "4.3 Please note that minimum threshold standards are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards (as defined by the Equality Act 2010) as part of a programme specification, these can be informed by the relevant Subject Benchmark Statement along with any PSRB requirements. In these circumstances, providers should follow the most recent guidance from the Equality and Human Rights Commission.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "providers who develop competence standards"
  addressee: provider
  verbs: ["follow"]
  about: "competence standards and Equality and Human Rights Commission guidance"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Threshold standards are not universal competence standards; a provider that sets competence standards under the Equality Act 2010 may draw on this statement and any PSRB requirements, and should follow the latest guidance from the Equality and Human Rights Commission."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 67454, end: 67572 }
  source: "Demonstrates the ability to gather and synthesise information from contextual sources and materials, to generate ideas"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["demonstrates", "gather", "synthesise", "generate"]
  about: "gathering sources to generate ideas"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Collects information from contextual sources and materials and pulls it together to produce ideas (Research and inquiry)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b1.excellent
  locator: { number: "4.4.b1.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 67658, end: 67776 }
  source: "Engages critically with diverse sources, synthesising insight and demonstrating how this supports creative development"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["engages", "synthesising", "demonstrating", "supports"]
  about: "critical synthesis of sources for creative development"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b1.typical, basis: stated }
  paraphrase: "Excellent descriptor: Works critically with varied sources, draws insight from them and shows how that insight drives creative development (Research and inquiry)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b1.typical
  locator: { number: "4.4.b1.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 67573, end: 67657 }
  source: "Undertakes research employing appropriate methods across a broad spectrum of sources"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["undertakes", "employing"]
  about: "research with fitting methods across many sources"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b1, basis: stated }
  paraphrase: "Typical descriptor: Carries out research with fitting methods across a wide range of sources (Research and inquiry)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 67796, end: 67857 }
  source: "Applies use of materials and processes appropriate to context"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["applies"]
  about: "materials and processes suited to context"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Uses materials and processes that suit the context of the work (Material knowledge)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b2.excellent
  locator: { number: "4.4.b2.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 67926, end: 68053 }
  source: "Engages with materials in a purposeful, explorative and imaginative way, applying them confidently to produce creative outcomes"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["engages", "applying", "produce"]
  about: "purposeful, imaginative and confident use of materials"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b2.typical, basis: stated }
  paraphrase: "Excellent descriptor: Handles materials with purpose, exploration and imagination, and uses them with confidence to make creative work (Material knowledge)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b2.typical
  locator: { number: "4.4.b2.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 67858, end: 67925 }
  source: "Experiments with materials and processes to generate creative ideas"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["experiments", "generate"]
  about: "experimenting with materials to spark ideas"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b2, basis: stated }
  paraphrase: "Typical descriptor: Experiments with materials and processes as a way of producing creative ideas (Material knowledge)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 68075, end: 68146 }
  source: "Recognises key historical and current theoretical and cultural contexts"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["recognises"]
  about: "main historical, theoretical and cultural contexts"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Recognises the main historical contexts of the field and the theoretical and cultural ones that matter now (Contextual awareness)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b3.excellent
  locator: { number: "4.4.b3.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 68223, end: 68311 }
  source: "Integrates contextual understanding, factors and behaviours to support creative ambition"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["integrates", "support"]
  about: "context integrated in support of ambition"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b3.typical, basis: stated }
  paraphrase: "Excellent descriptor: Brings contextual understanding, its factors and behaviours together in the service of ambitious creative work (Contextual awareness)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b3.typical
  locator: { number: "4.4.b3.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 68147, end: 68222 }
  source: "Applies contextual understanding and key factors to shape creative practice"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["applies", "shape"]
  about: "context shaping creative practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b3, basis: stated }
  paraphrase: "Typical descriptor: Uses an understanding of context and its main factors to shape creative practice (Contextual awareness)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 68366, end: 68457 }
  source: "Identifies current debates and conversation relevant to art, design and cultural production"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["identifies"]
  about: "current debates in art, design and culture"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Identifies the debates and conversations now under way in art, design and cultural production (Engagement with contemporary discourse and debate)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b4.excellent
  locator: { number: "4.4.b4.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 68551, end: 68642 }
  source: "Applies critical understanding of discourse to contribute to current disciplinary dialogues"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["applies", "contribute"]
  about: "contributing to the discipline's conversations"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b4.typical, basis: stated }
  paraphrase: "Excellent descriptor: Brings a critical grasp of the discourse to bear and adds to the conversations the discipline is having now (Engagement with contemporary discourse and debate)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b4.typical
  locator: { number: "4.4.b4.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 68458, end: 68550 }
  source: "Engages with relevant debates and ideas to inform thinking, practice and critical reflection"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["engages", "inform"]
  about: "debates feeding thinking and practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b4, basis: stated }
  paraphrase: "Typical descriptor: Takes part in relevant debates and ideas and lets them feed thinking, practice and critical reflection (Engagement with contemporary discourse and debate)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 68677, end: 68772 }
  source: "Recognises and interprets ideas and practices within cultural, creative and conceptual contexts"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["recognises", "interprets"]
  about: "interpreting ideas and practices in context"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Recognises and interprets ideas and practices in their cultural, creative and conceptual settings (Analysis)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b5.excellent
  locator: { number: "4.4.b5.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 68853, end: 68940 }
  source: "Interrogates and experiments with creative possibilities through analysis and synthesis"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["interrogates", "experiments"]
  about: "questioning and testing creative possibilities"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b5.typical, basis: stated }
  paraphrase: "Excellent descriptor: Questions and tests creative possibilities by analysing and combining ideas (Analysis)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b5.typical
  locator: { number: "4.4.b5.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 68773, end: 68852 }
  source: "Systematically applies analysis to inform creative practice and decision-making"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["applies", "inform"]
  about: "systematic analysis guiding decisions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b5, basis: stated }
  paraphrase: "Typical descriptor: Analyses systematically and uses the results to guide creative practice and decisions (Analysis)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 68953, end: 69031 }
  source: "Identifies and uses suitable methods to develop and complete creative outcomes"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["identifies", "uses", "develop", "complete"]
  about: "methods to develop and finish work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Finds and uses suitable methods to develop creative work and see it through to completion (Realisation)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b6.excellent
  locator: { number: "4.4.b6.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 69111, end: 69240 }
  source: "Consolidates and generates understanding to realise imaginative and creative outcomes that express intent and innovative thinking"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["consolidates", "generates", "realise", "express"]
  about: "work that conveys intent and new thinking"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b6.typical, basis: stated }
  paraphrase: "Excellent descriptor: Draws together and builds understanding to make imaginative creative work that conveys clear intent and innovative thinking (Realisation)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b6.typical
  locator: { number: "4.4.b6.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 69032, end: 69110 }
  source: "Uses effective methods and techniques to realise imaginative creative outcomes"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["uses", "realise"]
  about: "effective methods for imaginative work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b6, basis: stated }
  paraphrase: "Typical descriptor: Uses effective methods and techniques to produce imaginative creative work (Realisation)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 69279, end: 69389 }
  source: "Reflects on creative decisions and outcomes to develop self-reflection and understand strengths and weaknesses"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["reflects", "develop", "understand"]
  about: "reflecting on decisions, strengths and weaknesses"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Reflects on creative decisions and results to grow self-awareness and know their own strengths and weaknesses (Reflection)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b7.excellent
  locator: { number: "4.4.b7.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 69459, end: 69541 }
  source: "Applies critical evaluation, self- awareness and reflection to improve future work"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["applies", "improve"]
  about: "evaluation used to improve later work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b7.typical, basis: stated }
  paraphrase: "Excellent descriptor: Uses critical evaluation, self-awareness and reflection to make later work better (Reflection)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b7.typical
  locator: { number: "4.4.b7.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 69390, end: 69458 }
  source: "Critically evaluates the impact of process, development and outcomes"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["evaluates"]
  about: "critical evaluation of process and outcomes"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b7, basis: stated }
  paraphrase: "Typical descriptor: Judges critically what the process, the development of the work and its results have achieved (Reflection)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 69575, end: 69649 }
  source: "Recognises how creative work conveys meaning and is open to interpretation"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["recognises", "conveys"]
  about: "how work carries meaning"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Recognises that creative work carries meaning and can be read in more than one way (Awareness of audience and impact)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b8.excellent
  locator: { number: "4.4.b8.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 69722, end: 69857 }
  source: "Communicates work to ensure relevance to diverse audiences or contexts, sensitively demonstrating awareness of complexity and ambiguity"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["communicates", "ensure", "demonstrating"]
  about: "relevance to diverse audiences; handling ambiguity"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b8.typical, basis: stated }
  paraphrase: "Excellent descriptor: Communicates work so it speaks to diverse audiences or settings, with a sensitive awareness of complexity and ambiguity (Awareness of audience and impact)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b8.typical
  locator: { number: "4.4.b8.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 69650, end: 69721 }
  source: "Considers audiences when conceiving, developing and presenting outcomes"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["considers", "conceiving", "developing", "presenting"]
  about: "audiences throughout the making of work"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b8, basis: stated }
  paraphrase: "Typical descriptor: Keeps audiences in mind while conceiving, developing and presenting work (Awareness of audience and impact)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 69970, end: 70008 }
  source: "Plans time and tasks to meet deadlines"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["plans", "meet"]
  about: "planning time and tasks for deadlines"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Plans time and tasks so that deadlines are met (Independence and management)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b9.excellent
  locator: { number: "4.4.b9.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 70088, end: 70170 }
  source: "Works independently with initiative and resilience in sometimes uncertain contexts"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["works"]
  about: "independent work with initiative and resilience"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b9.typical, basis: stated }
  paraphrase: "Excellent descriptor: Works alone with initiative and resilience where the setting is at times uncertain (Independence and management)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b9.typical
  locator: { number: "4.4.b9.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 70009, end: 70087 }
  source: "Organises time and resources effectively to solve problems and manage projects"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["organises", "solve", "manage"]
  about: "organising resources to run projects"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b9, basis: stated }
  paraphrase: "Typical descriptor: Organises time and resources well to solve problems and run projects (Independence and management)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b10
  locator: { number: "4.4.b10", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 70185, end: 70250 }
  source: "Describes ideas, intent or experience through appropriate formats"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["describes"]
  about: "describing ideas in suitable formats"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Describes ideas, intentions or experience in formats that suit them (Communication)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b10.excellent
  locator: { number: "4.4.b10.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 70350, end: 70470 }
  source: "Integrates critical and experimental approaches to purposefully communicate ideas with conviction, coherence and purpose"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["integrates", "communicate"]
  about: "communicating with conviction and coherence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b10.typical, basis: stated }
  paraphrase: "Excellent descriptor: Combines critical and experimental approaches to put ideas across with conviction, coherence and purpose (Communication)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b10.typical
  locator: { number: "4.4.b10.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 70251, end: 70349 }
  source: "Selects and uses appropriate communication methods to develop and share creative ideas effectively"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["selects", "uses", "develop", "share"]
  about: "choosing ways to communicate ideas"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b10, basis: stated }
  paraphrase: "Typical descriptor: Chooses and uses suitable ways of communicating to develop and share creative ideas well (Communication)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b11
  locator: { number: "4.4.b11", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 70505, end: 70609 }
  source: "Shows awareness of the creative sector's ethical and social responsibilities, and empathy towards others"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["shows"]
  about: "awareness of the sector's ethical duties; empathy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Shows awareness of the ethical and social responsibilities of the creative sector, and empathy for other people (Ethics and social responsibility)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b11.excellent
  locator: { number: "4.4.b11.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 70709, end: 70841 }
  source: "Applies critical practice to address inequalities of representation in the contexts in which art and design is produced and consumed"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["applies", "address"]
  about: "tackling unequal representation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b11.typical, basis: stated }
  paraphrase: "Excellent descriptor: Uses critical practice to tackle unequal representation where art and design are made and consumed (Ethics and social responsibility)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b11.typical
  locator: { number: "4.4.b11.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 70611, end: 70708 }
  source: "Engages with ethical principles, inclusivity, access and social considerations in decision-making"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["engages"]
  about: "ethics, inclusivity and access in decisions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b11, basis: stated }
  paraphrase: "Typical descriptor: Takes ethical principles, inclusivity, access and social factors into account when deciding (Ethics and social responsibility)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b12
  locator: { number: "4.4.b12", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 70866, end: 71007 }
  source: "Evidences an understanding of sustainability and acknowledges the creative sector's role in responding to environmental and social challenges"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["evidences", "acknowledges", "responding"]
  about: "understanding sustainability and the sector's part"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Shows an understanding of sustainability and accepts the part the creative sector plays in meeting environmental and social challenges (Sustainability literacy)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b12.excellent
  locator: { number: "4.4.b12.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 71122, end: 71251 }
  source: "Integrates sustainability as a core value in creative work, showing awareness of circularity, resource impact and long-term value"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["integrates", "showing"]
  about: "sustainability as a core value"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b12.typical, basis: stated }
  paraphrase: "Excellent descriptor: Makes sustainability a core value of creative work, aware of circularity, resource use and lasting value (Sustainability literacy)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b12.typical
  locator: { number: "4.4.b12.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 71008, end: 71121 }
  source: "Actively considers environmental, social and economic sustainability in proposed decisions and production methods"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["considers"]
  about: "sustainability in decisions and production"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b12, basis: stated }
  paraphrase: "Typical descriptor: Actively weighs environmental, social and economic sustainability in planned decisions and ways of producing work (Sustainability literacy)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b13
  locator: { number: "4.4.b13", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 71288, end: 71352 }
  source: "Recognises the potential for work to be professionally presented"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["recognises", "presented"]
  about: "seeing how work could be presented professionally"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Sees how work could be presented in a professional way (Enterprise and entrepreneurship)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b13.excellent
  locator: { number: "4.4.b13.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 71430, end: 71523 }
  source: "Devises opportunities to publicly present, exhibit, commercialise or publish creative outputs"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["devises", "present", "exhibit", "commercialise", "publish"]
  about: "creating chances to exhibit, sell or publish"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b13.typical, basis: stated }
  paraphrase: "Excellent descriptor: Creates their own openings to present, exhibit, sell or publish creative work in public (Enterprise and entrepreneurship)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b13.typical
  locator: { number: "4.4.b13.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 71354, end: 71429 }
  source: "Develops innovative creative outputs within professional or public contexts"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["develops"]
  about: "innovative work in professional or public settings"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b13, basis: stated }
  paraphrase: "Typical descriptor: Develops new and inventive creative work in professional or public settings (Enterprise and entrepreneurship)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b14
  locator: { number: "4.4.b14", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 71538, end: 71698 }
  source: "Recognises and articulates personal strengths and areas for development, in order to engage in collaboration and establish an awareness of professional networks"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["recognises", "articulates", "engage", "establish"]
  about: "own strengths, collaboration and networks"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold descriptor: Recognises and explains their strengths and development needs so that they can collaborate and become aware of professional networks (Employability)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b14.excellent
  locator: { number: "4.4.b14.excellent", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 71786, end: 71922 }
  source: "Actively seeks and capitalises on opportunities to build professional networks, demonstrate initiative, adaptability and professionalism"
  stem: "4.4"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["seeks", "capitalises", "build", "demonstrate"]
  about: "seizing networking chances with initiative"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b14.typical, basis: stated }
  paraphrase: "Excellent descriptor: Actively looks for and makes the most of chances to grow professional networks, showing initiative, adaptability and professionalism (Employability)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.4.b14.typical
  locator: { number: "4.4.b14.typical", headingPath: ["Benchmark standards", "Undergraduate degrees: threshold, typical and excellent standards"] }
  span: { start: 71699, end: 71785 }
  source: "Demonstrates commitment to personal development and to building a professional network"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["demonstrates", "building"]
  about: "commitment to growth and professional contacts"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/art-and-design-2026/4.4.b14, basis: stated }
  paraphrase: "Typical descriptor: Shows they are committed to growing personally and to building professional contacts (Employability)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.5
  locator: { number: "4.5", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 71945, end: 72148 }
  source: "4.5 Master's level degrees require higher levels of technical, critical, conceptual and contextual understanding, in addition to meeting the benchmark standards at undergraduate level listed in Table 1.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["require", "meeting"]
  about: "master's understanding beyond the honours standards"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's degree calls for greater technical, critical, conceptual and contextual understanding, on top of meeting the honours standards in Table 1."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 72482, end: 72642 }
  source: "systematically and rigorously apply theoretical, practical, technical and contextual knowledge in the development of creative, academic or professional outcomes"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["apply"]
  about: "systematic, rigorous use of knowledge in outcomes"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are typically able to apply theoretical, practical, technical and contextual knowledge with system and rigour as creative, academic or professional work develops."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 72645, end: 72765 }
  source: "apply materials extensively and inventively to expand making processes and introduce new approaches to creative practice"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["apply", "expand", "introduce"]
  about: "inventive use of materials"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are typically able to use materials widely and inventively, extending how things are made and bringing new approaches into creative practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 72768, end: 72854 }
  source: "systematically develop and apply methods and methodologies to support advanced inquiry"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["develop", "apply", "support"]
  about: "methods for advanced inquiry"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are typically able to build and use methods and methodologies systematically to carry advanced inquiry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 72857, end: 72976 }
  source: "critically and comprehensively analyse research, iteration and contextual factors to inform the advancement of practice"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["analyse", "inform"]
  about: "critical analysis to advance practice"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are typically able to analyse research, iteration and contextual factors critically and thoroughly so that practice moves forward."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 72979, end: 73138 }
  source: "professionally realise practice, research, ideas and knowledge in visual, verbal and/or written forms applied within varied, complex and unpredictable contexts"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["realise"]
  about: "realising work in complex, unpredictable settings"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are typically able to realise practice, research, ideas and knowledge to a professional standard in visual, spoken or written form across varied, complex and unpredictable settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.7.b6
  locator: { number: "4.7.b6", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 73141, end: 73268 }
  source: "undertake critical reflection upon practice in a systematic and purposeful manner to support intellectual growth and innovation"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["undertake", "support"]
  about: "systematic critical reflection"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are typically able to reflect critically on practice in a systematic and purposeful way, supporting intellectual growth and innovation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.7.b7
  locator: { number: "4.7.b7", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 73271, end: 73354 }
  source: "confidently apply professional working methods within a range of complex situations"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["apply"]
  about: "professional working methods in complex situations"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are typically able to use professional working methods with confidence across a range of complex situations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.7.b8
  locator: { number: "4.7.b8", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 73357, end: 73479 }
  source: "deploy flexible and agile working methods to support project development and enable a creative approach to problem-solving"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["deploy", "support", "enable"]
  about: "flexible, agile working"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are typically able to use flexible and agile methods of working to move projects on and take a creative approach to problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.7.b9
  locator: { number: "4.7.b9", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 73482, end: 73647 }
  source: "situate practice in a clearly defined and critically informed context, interrogating its relationship to ethical working practices, responsibilities and implications"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["situate", "interrogating"]
  about: "ethically situated practice"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are typically able to place practice in a clearly defined, critically informed context and question how it relates to ethical working practices, responsibilities and implications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.7.b10
  locator: { number: "4.7.b10", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 73650, end: 73778 }
  source: "interpret knowledge within a clearly defined context that is sensitive to cultural, environmental, social and political contexts"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["interpret"]
  about: "knowledge read in sensitive context"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are typically able to interpret knowledge within a clearly bounded context that is alert to cultural, environmental, social and political matters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.7.b11
  locator: { number: "4.7.b11", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 73781, end: 73916 }
  source: "apply creative strategies that centre equity and inclusion, responding to structural injustices through design or artistic intervention"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["apply", "centre", "responding"]
  about: "equity and inclusion in creative strategy"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are typically able to use creative strategies that put equity and inclusion at their centre, answering structural injustice through design or artistic intervention."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/art-and-design-2026/4.7.b12
  locator: { number: "4.7.b12", headingPath: ["Benchmark standards", "Postgraduate degrees"] }
  span: { start: 73919, end: 74060 }
  source: "apply collaborative working methods with initiative, responsiveness and leadership to realise shared goals and contribute to positive change."
  stem: "4.7"
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's graduates of the subject"
  addressee: learner
  verbs: ["apply", "realise", "contribute"]
  about: "collaboration and leadership for change"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are typically able to work collaboratively with initiative, responsiveness and leadership to reach shared goals and add to positive change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/art-and-design-2026/1.19
  forPractitioner: { text: "Plan adjustments before they are asked for: providers must make reasonable adjustments under the Equality Act 2010, and here that means briefs shared early, other formats for lectures and content, one-to-one help or specialist kit, and adjustments for group work.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a legal duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a legal duty on the provider under the Equality Act 2010, carried in the accessibility theme, not as a learning outcome or a level-bound standard. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 1.19) and name the Act as the source of the duty. Do not present the statement itself as the regulation, and do not turn it into a student outcome. Set it beside paras 1.17 to 1.24 and the inclusive-assessment practices in 3.18 to 3.20 (qaa/art-and-design-2026/1.19 is the only obliging record in the theme)."
  author-agent-dialogue: "Raise it with a programme team planning studios, group projects or assessment, or with a teacher asked about a disabled student's access. Frame it for staff as an anticipatory duty: what is in place before anyone asks. Ask: 'Which adjustments for group and studio work are ready now, and which wait for a request?' Do not put this duty to a student as something they must show."
- statement: qaa/art-and-design-2026/2.12
  forPractitioner: { text: "Map each level so that it builds towards the threshold skills in Table 1: students will progress level by level under your regulations, normally by passing and earning credit for every part of the course, practical components included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will move up one level at a time, each year adding knowledge, expertise and experience that build towards the subject and general skills expected at the end; usually that means passing and earning credit for all your learning and assessment, practical work included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation of progression (force: will) across an honours degree at FHEQ Level 6 (FQHEIS Level 10) or an integrated master's at FHEQ Level 7 (FQHEIS Level 11). Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 2.12). Do not claim it fixes progression rules, which stay with each institution. Set it beside Table 1's threshold cells (for example qaa/art-and-design-2026/4.4.b1) and the FHEQ descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1, with spine:6 and spine:7."
  author-agent-dialogue: "Raise it when a student asks what each year is for or a team is mapping modules across levels. Tell a student plainly that each level builds towards the skills expected at the end; frame it for staff as a check on level-by-level design. Ask: 'What does this year add that you will need by the final year?' Avoid presenting the higher rungs as what every student must reach."
- statement: qaa/art-and-design-2026/2.14
  forPractitioner: { text: "In a joint or combined course, students will meet the core subject and generic skills of this statement and add skills from the partner subject; design the course so the overlap between the two can be explored.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study the subject alongside another in a joint or combined degree, you will reach the core subject and general skills and add others from your second subject, with chances to explore where the two meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation (force: will) for joint and combined honours at FHEQ Level 6 (FQHEIS Level 10): the core of the subject and generic skills is met, not the whole. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 2.14). Do not claim a joint student meets every cell of Table 1 in full, or that the statement says which cells are core. Set it beside Table 1 (para 4.4), para 2.10 and the FHEQ honours descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it with a student on a joint or major and minor route, or a team designing one. Tell the student plainly that they cover the core of this subject and gain other skills from the second; with staff, ask which cells the course treats as core. Ask: 'Where do your two subjects meet in your own work?' Avoid suggesting the student is held to the full single honours set."
- statement: qaa/art-and-design-2026/2.24
  forPractitioner: { text: "In monitoring and periodic review, students' views will form part of the evidence, read with external reference points including this statement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the awarding body in its review process", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider expectation (force: will) about course review, holding at every level. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 2.24). Do not present it as a learning outcome or as a regulatory rule. Set it beside para 2.25 (externality, qaa/art-and-design-2026/2.25) and the review role of external examiners in paras 2.26 and 2.27."
  author-agent-dialogue: "Raise it with a programme team preparing a periodic review or annual monitoring. Frame it for staff: how students' views enter the evidence. Ask: 'Where in the review do students' own accounts change a decision?' Do not give this to a student as a standard; with a student, at most explain that their views count in review."
- statement: qaa/art-and-design-2026/2.25
  forPractitioner: { text: "Bring external reviewers into periodic review: they will give an independent view of changes and check that threshold standards are reached and content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in periodic review", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider expectation (force: will) about externality in periodic review. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 2.25). Do not claim it sets the threshold standards themselves, which are in Table 1. Set it beside para 2.24 (qaa/art-and-design-2026/2.24), paras 2.26 and 2.27 on external examiners, and Table 1's threshold cells."
  author-agent-dialogue: "Raise it with a team planning a periodic review or choosing reviewers. Frame it for staff as the independent check on threshold standards and fit with the subject. Ask: 'Who outside the provider will look at this change, and what will they test it against?' Do not present it to a student as their responsibility."
- statement: qaa/art-and-design-2026/4.2
  forPractitioner: { text: "Most students will go well beyond threshold. When deciding what evidence shows achievement, providers should use Annex D's descriptions of the first, upper second, lower second and third classes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in classifying degrees", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider recommendation (force: should) to use Annex D when judging achievement above threshold, at FHEQ Level 6 (FQHEIS Level 10) for honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.2) and Annex D as std:doc:qaa-fheq-2024-framework. Do not map Table 1's typical or excellent rungs onto a degree class: the statement does not. Set it beside qaa/fheq-2024/annex-d/summary/r1/3rd and the other Annex D summary rows."
  author-agent-dialogue: "Raise it with a team writing marking criteria or a classification policy. Frame it for staff: the subject's rungs describe attainment, while Annex D describes the classes. Ask: 'How do your criteria for a 2.1 relate to the typical cells?' Do not put this to a student as a rule they follow."
- statement: qaa/art-and-design-2026/4.3
  forPractitioner: { text: "Do not treat Table 1's threshold as a competence standard. If you write competence standards for a programme specification, draw on this statement and PSRB requirements and follow the Equality and Human Rights Commission's current guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in writing competence standards", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider recommendation (force: should) about competence standards in the Equality Act 2010 sense, holding at any level. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.3). Do not call the threshold cells competence standards, and do not claim the statement sets any. Set it beside para 1.19 (qaa/art-and-design-2026/1.19) and Table 1's threshold cells."
  author-agent-dialogue: "Raise it when a team proposes making a skill compulsory for every student or writes a programme specification with competence standards. Frame it for staff as a caution about inclusion law. Ask: 'Is this a genuine competence standard, and have you read the current Commission guidance?' Do not present it to a student as a requirement on them."
- statement: qaa/art-and-design-2026/4.4.b1
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate collects information from contextual sources and materials and pulls it together to produce ideas; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you collect information from the sources and materials around your work and pull it together to come up with ideas.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Research and inquiry' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Research and inquiry, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b3) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b1.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b5, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/knowledge/r3/3rd."
  author-agent-dialogue: "Bring this up when a student is starting the research for a project or a team is reviewing how research is taught. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'Where did the ideas in your last project come from, and how did you gather them?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b1.excellent
  forPractitioner: { text: "At the excellent rung, the graduate works critically with varied sources, draws insight from them and shows how that insight drives creative development; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you work critically with varied sources, draw your own insight from them and show how it moves your creative work forward.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Research and inquiry' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Research and inquiry, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b3) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b1.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b5, spine:6 and Annex D row qaa/fheq-2024/annex-d/knowledge/r3 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is starting the research for a project or a team is reviewing how research is taught. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'Where did the ideas in your last project come from, and how did you gather them?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b1.typical
  forPractitioner: { text: "At the typical rung, the graduate carries out research with fitting methods across a wide range of sources; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you research with methods that suit the task, drawing on a wide range of sources.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Research and inquiry' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Research and inquiry, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b3) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b1 and the excellent cell qaa/art-and-design-2026/4.4.b1.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b5, spine:6 and Annex D row qaa/fheq-2024/annex-d/knowledge/r3 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is starting the research for a project or a team is reviewing how research is taught. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'Where did the ideas in your last project come from, and how did you gather them?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b2
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate uses materials and processes that suit the context of the work; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you use materials and processes that suit the setting of your work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Material knowledge' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Material knowledge, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b2) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b2.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Bring this up when a student is choosing materials or processes, or a teacher is planning workshop inductions. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'Why did you pick these materials, and what did you try before settling on them?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b2.excellent
  forPractitioner: { text: "At the excellent rung, the graduate handles materials with purpose, exploration and imagination, and uses them with confidence to make creative work; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you handle materials with purpose and imagination, exploring what they can do and using them confidently in your work.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Material knowledge' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Material knowledge, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b2) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b2.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2, spine:6 and Annex D row qaa/fheq-2024/annex-d/practical/r1 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is choosing materials or processes, or a teacher is planning workshop inductions. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'Why did you pick these materials, and what did you try before settling on them?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b2.typical
  forPractitioner: { text: "At the typical rung, the graduate experiments with materials and processes as a way of producing creative ideas; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you experiment with materials and processes to spark creative ideas.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Material knowledge' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Material knowledge, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b2) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b2 and the excellent cell qaa/art-and-design-2026/4.4.b2.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2, spine:6 and Annex D row qaa/fheq-2024/annex-d/practical/r1 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is choosing materials or processes, or a teacher is planning workshop inductions. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'Why did you pick these materials, and what did you try before settling on them?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b3
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate recognises the main historical contexts of the field and the theoretical and cultural ones that matter now; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you recognise the main historical, theoretical and cultural contexts your field sits in, past and present.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Contextual awareness' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Contextual awareness, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b10) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b3.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Bring this up when a student is placing their work in history or theory, or a team is linking contextual studies to studio modules. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'Which artists, designers or ideas, past or present, does your work answer to?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b3.excellent
  forPractitioner: { text: "At the excellent rung, the graduate brings contextual understanding, its factors and behaviours together in the service of ambitious creative work; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you bring your grasp of context fully into your work so that it backs up your creative ambitions.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Contextual awareness' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Contextual awareness, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b10) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b3.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1, spine:6 and Annex D row qaa/fheq-2024/annex-d/knowledge/r2 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is placing their work in history or theory, or a team is linking contextual studies to studio modules. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'Which artists, designers or ideas, past or present, does your work answer to?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b3.typical
  forPractitioner: { text: "At the typical rung, the graduate uses an understanding of context and its main factors to shape creative practice; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you use what you understand about context to shape your creative practice.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Contextual awareness' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Contextual awareness, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b10) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b3 and the excellent cell qaa/art-and-design-2026/4.4.b3.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1, spine:6 and Annex D row qaa/fheq-2024/annex-d/knowledge/r2 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is placing their work in history or theory, or a team is linking contextual studies to studio modules. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'Which artists, designers or ideas, past or present, does your work answer to?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b4
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate identifies the debates and conversations now under way in art, design and cultural production; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you can name the debates going on now in art, design and cultural production.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Engagement with contemporary discourse and debate' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Engagement with contemporary discourse and debate, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b4) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b4.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.2, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Bring this up when a student is asked about current debates in their field or a team is planning seminars and critical writing. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'What argument going on in your field right now matters to your work, and where do you stand on it?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b4.excellent
  forPractitioner: { text: "At the excellent rung, the graduate brings a critical grasp of the discourse to bear and adds to the conversations the discipline is having now; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you use a critical grasp of the discussion in your field to add your own voice to it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Engagement with contemporary discourse and debate' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Engagement with contemporary discourse and debate, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b4) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b4.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.2, spine:6 and Annex D row qaa/fheq-2024/annex-d/cognitive/r1 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is asked about current debates in their field or a team is planning seminars and critical writing. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'What argument going on in your field right now matters to your work, and where do you stand on it?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b4.typical
  forPractitioner: { text: "At the typical rung, the graduate takes part in relevant debates and ideas and lets them feed thinking, practice and critical reflection; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you engage with relevant debates and ideas and let them feed your thinking, your practice and your reflection.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Engagement with contemporary discourse and debate' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Engagement with contemporary discourse and debate, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b4) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b4 and the excellent cell qaa/art-and-design-2026/4.4.b4.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.2, spine:6 and Annex D row qaa/fheq-2024/annex-d/cognitive/r1 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is asked about current debates in their field or a team is planning seminars and critical writing. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'What argument going on in your field right now matters to your work, and where do you stand on it?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b5
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate recognises and interprets ideas and practices in their cultural, creative and conceptual settings; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you recognise and interpret ideas and practices in their cultural, creative and conceptual settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Analysis' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Analysis, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b4) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b5.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Bring this up when a student is analysing their own or others' work, or a teacher is setting an analytical task. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'What does this piece do, and how did your analysis of it change what you made next?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b5.excellent
  forPractitioner: { text: "At the excellent rung, the graduate questions and tests creative possibilities by analysing and combining ideas; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you question and test creative possibilities by analysing ideas and combining them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Analysis' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Analysis, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b4) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b5.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7, spine:6 and Annex D row qaa/fheq-2024/annex-d/cognitive/r2 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is analysing their own or others' work, or a teacher is setting an analytical task. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'What does this piece do, and how did your analysis of it change what you made next?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b5.typical
  forPractitioner: { text: "At the typical rung, the graduate analyses systematically and uses the results to guide creative practice and decisions; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you analyse systematically and use what you find to guide your creative choices.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Analysis' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Analysis, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b4) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b5 and the excellent cell qaa/art-and-design-2026/4.4.b5.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7, spine:6 and Annex D row qaa/fheq-2024/annex-d/cognitive/r2 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is analysing their own or others' work, or a teacher is setting an analytical task. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'What does this piece do, and how did your analysis of it change what you made next?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b6
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate finds and uses suitable methods to develop creative work and see it through to completion; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you find and use suitable methods to develop your creative work and finish it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Realisation' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Realisation, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b5) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b6.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/practical/r3/3rd."
  author-agent-dialogue: "Bring this up when a student is turning ideas into finished work or a team is planning a final major project. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'What methods took this from idea to finished piece, and what would you change?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b6.excellent
  forPractitioner: { text: "At the excellent rung, the graduate draws together and builds understanding to make imaginative creative work that conveys clear intent and innovative thinking; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you build and draw together your understanding to make imaginative work that shows clear intent and new thinking.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Realisation' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Realisation, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b5) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b6.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6, spine:6 and Annex D row qaa/fheq-2024/annex-d/practical/r3 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is turning ideas into finished work or a team is planning a final major project. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'What methods took this from idea to finished piece, and what would you change?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b6.typical
  forPractitioner: { text: "At the typical rung, the graduate uses effective methods and techniques to produce imaginative creative work; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you use effective methods and techniques to make imaginative creative work.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Realisation' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Realisation, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b5) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b6 and the excellent cell qaa/art-and-design-2026/4.4.b6.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6, spine:6 and Annex D row qaa/fheq-2024/annex-d/practical/r3 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is turning ideas into finished work or a team is planning a final major project. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'What methods took this from idea to finished piece, and what would you change?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b7
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate reflects on creative decisions and results to grow self-awareness and know their own strengths and weaknesses; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you look back on your creative decisions and results to understand yourself, your strengths and your weaknesses.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Reflection' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Reflection, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b6) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b7.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Bring this up when a student is writing a reflective statement or process journal, or a teacher is designing reflective assessment. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'Looking back at this project, what worked, what did not, and what will you do differently?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b7.excellent
  forPractitioner: { text: "At the excellent rung, the graduate uses critical evaluation, self-awareness and reflection to make later work better; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you use critical evaluation, self-awareness and reflection to make your next piece of work better.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Reflection' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Reflection, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b6) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b7.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4, spine:6 and Annex D row qaa/fheq-2024/annex-d/transferable/r5 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is writing a reflective statement or process journal, or a teacher is designing reflective assessment. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'Looking back at this project, what worked, what did not, and what will you do differently?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b7.typical
  forPractitioner: { text: "At the typical rung, the graduate judges critically what the process, the development of the work and its results have achieved; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you judge critically what your process, development and results have achieved.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Reflection' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Reflection, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b6) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b7 and the excellent cell qaa/art-and-design-2026/4.4.b7.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4, spine:6 and Annex D row qaa/fheq-2024/annex-d/transferable/r5 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is writing a reflective statement or process journal, or a teacher is designing reflective assessment. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'Looking back at this project, what worked, what did not, and what will you do differently?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b8
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate recognises that creative work carries meaning and can be read in more than one way; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you recognise that creative work carries meaning and that people may read it differently.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Awareness of audience and impact' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Awareness of audience and impact, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b5) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b8.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Bring this up when a student is planning how work will be shown or a team is setting exhibition or presentation tasks. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'Who is this work for, and how might they read it differently from you?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b8.excellent
  forPractitioner: { text: "At the excellent rung, the graduate communicates work so it speaks to diverse audiences or settings, with a sensitive awareness of complexity and ambiguity; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you communicate your work so it speaks to many audiences and settings, handling complexity and ambiguity with care.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Awareness of audience and impact' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Awareness of audience and impact, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b5) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b8.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8, spine:6 and Annex D row qaa/fheq-2024/annex-d/transferable/r1 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is planning how work will be shown or a team is setting exhibition or presentation tasks. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'Who is this work for, and how might they read it differently from you?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b8.typical
  forPractitioner: { text: "At the typical rung, the graduate keeps audiences in mind while conceiving, developing and presenting work; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you keep your audiences in mind as you conceive, develop and present your work.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Awareness of audience and impact' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Awareness of audience and impact, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b5) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b8 and the excellent cell qaa/art-and-design-2026/4.4.b8.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8, spine:6 and Annex D row qaa/fheq-2024/annex-d/transferable/r1 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is planning how work will be shown or a team is setting exhibition or presentation tasks. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'Who is this work for, and how might they read it differently from you?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b9
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate plans time and tasks so that deadlines are met; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you plan your time and tasks so you meet deadlines.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Independence and management' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Independence and management, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b8) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b9.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.15.b9.2, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Bring this up when a student is struggling with deadlines or workload, or a team is staging independence across the levels. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'How did you plan this project, and where did the plan slip?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b9.excellent
  forPractitioner: { text: "At the excellent rung, the graduate works alone with initiative and resilience where the setting is at times uncertain; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you work on your own, taking the initiative and staying resilient when things are uncertain.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Independence and management' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Independence and management, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b8) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b9.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.15.b9.2, spine:6 and Annex D row qaa/fheq-2024/annex-d/transferable/r3 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is struggling with deadlines or workload, or a team is staging independence across the levels. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'How did you plan this project, and where did the plan slip?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b9.typical
  forPractitioner: { text: "At the typical rung, the graduate organises time and resources well to solve problems and run projects; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you organise your time and resources well to solve problems and run projects.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Independence and management' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Independence and management, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b8) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b9 and the excellent cell qaa/art-and-design-2026/4.4.b9.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.15.b9.2, spine:6 and Annex D row qaa/fheq-2024/annex-d/transferable/r3 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is struggling with deadlines or workload, or a team is staging independence across the levels. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'How did you plan this project, and where did the plan slip?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b10
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate describes ideas, intentions or experience in formats that suit them; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you describe your ideas, intentions or experience in suitable formats.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Communication' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Communication, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b5) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b10.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Bring this up when a student is preparing a pitch, statement or presentation, or a teacher is setting communication tasks. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'How would you explain this idea to someone who has not seen the work?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b10.excellent
  forPractitioner: { text: "At the excellent rung, the graduate combines critical and experimental approaches to put ideas across with conviction, coherence and purpose; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you combine critical and experimental approaches to put your ideas across with conviction and coherence.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Communication' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Communication, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b5) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b10.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8, spine:6 and Annex D row qaa/fheq-2024/annex-d/transferable/r1 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is preparing a pitch, statement or presentation, or a teacher is setting communication tasks. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'How would you explain this idea to someone who has not seen the work?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b10.typical
  forPractitioner: { text: "At the typical rung, the graduate chooses and uses suitable ways of communicating to develop and share creative ideas well; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you choose and use suitable ways of communicating to develop and share your creative ideas well.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Communication' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Communication, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b5) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b10 and the excellent cell qaa/art-and-design-2026/4.4.b10.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8, spine:6 and Annex D row qaa/fheq-2024/annex-d/transferable/r1 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is preparing a pitch, statement or presentation, or a teacher is setting communication tasks. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'How would you explain this idea to someone who has not seen the work?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b11
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate shows awareness of the ethical and social responsibilities of the creative sector, and empathy for other people; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you show you understand the ethical and social responsibilities of the creative sector, and you show empathy for others.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Ethics and social responsibility' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Ethics and social responsibility, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b11) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b11.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.2, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Bring this up when a student is weighing an ethical question in their work or a team is placing ethics and inclusion in the curriculum. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'Who could be affected by this work, and whose voices are missing from it?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b11.excellent
  forPractitioner: { text: "At the excellent rung, the graduate uses critical practice to tackle unequal representation where art and design are made and consumed; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you use critical practice to tackle unequal representation in the places where art and design are made and used.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Ethics and social responsibility' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Ethics and social responsibility, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b11) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b11.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.2, spine:6 and Annex D row qaa/fheq-2024/annex-d/professional/r2/3rd-1st for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is weighing an ethical question in their work or a team is placing ethics and inclusion in the curriculum. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'Who could be affected by this work, and whose voices are missing from it?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b11.typical
  forPractitioner: { text: "At the typical rung, the graduate takes ethical principles, inclusivity, access and social factors into account when deciding; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you take ethics, inclusivity, access and social factors into account when you make decisions.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Ethics and social responsibility' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Ethics and social responsibility, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b11) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b11 and the excellent cell qaa/art-and-design-2026/4.4.b11.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.2, spine:6 and Annex D row qaa/fheq-2024/annex-d/professional/r2/3rd-1st for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is weighing an ethical question in their work or a team is placing ethics and inclusion in the curriculum. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'Who could be affected by this work, and whose voices are missing from it?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b12
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate shows an understanding of sustainability and accepts the part the creative sector plays in meeting environmental and social challenges; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you show you understand sustainability and the part the creative sector plays in meeting environmental and social challenges.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Sustainability literacy' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Sustainability literacy, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b10) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b12.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.2, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/summary/r4/3rd."
  author-agent-dialogue: "Bring this up when a student is choosing materials, production methods or digital tools, or a team is embedding sustainability. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'What is the environmental and social cost of how you made this, and what would lower it?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b12.excellent
  forPractitioner: { text: "At the excellent rung, the graduate makes sustainability a core value of creative work, aware of circularity, resource use and lasting value; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you make sustainability central to your creative work, aware of circularity, resource use and lasting value.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Sustainability literacy' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Sustainability literacy, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b10) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b12.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.2, spine:6 and Annex D row qaa/fheq-2024/annex-d/summary/r4 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is choosing materials, production methods or digital tools, or a team is embedding sustainability. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'What is the environmental and social cost of how you made this, and what would lower it?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b12.typical
  forPractitioner: { text: "At the typical rung, the graduate actively weighs environmental, social and economic sustainability in planned decisions and ways of producing work; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you actively weigh environmental, social and economic sustainability in your decisions and in how you produce work.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Sustainability literacy' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Sustainability literacy, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b10) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b12 and the excellent cell qaa/art-and-design-2026/4.4.b12.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.2, spine:6 and Annex D row qaa/fheq-2024/annex-d/summary/r4 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is choosing materials, production methods or digital tools, or a team is embedding sustainability. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'What is the environmental and social cost of how you made this, and what would lower it?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b13
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate sees how work could be presented in a professional way; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you see how your work could be presented professionally.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Enterprise and entrepreneurship' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Enterprise and entrepreneurship, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b7) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b13.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/transferable/r4/3rd."
  author-agent-dialogue: "Bring this up when a student is thinking about exhibiting, selling or publishing, or a team is planning professional practice modules. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'Where could this work be shown, sold or published, and what would it take to get it there?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b13.excellent
  forPractitioner: { text: "At the excellent rung, the graduate creates their own openings to present, exhibit, sell or publish creative work in public; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you create your own chances to show, exhibit, sell or publish your creative work in public.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Enterprise and entrepreneurship' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Enterprise and entrepreneurship, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b7) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b13.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1, spine:6 and Annex D row qaa/fheq-2024/annex-d/transferable/r4 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is thinking about exhibiting, selling or publishing, or a team is planning professional practice modules. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'Where could this work be shown, sold or published, and what would it take to get it there?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b13.typical
  forPractitioner: { text: "At the typical rung, the graduate develops new and inventive creative work in professional or public settings; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you develop innovative creative work in professional or public settings.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Enterprise and entrepreneurship' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Enterprise and entrepreneurship, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b7) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b13 and the excellent cell qaa/art-and-design-2026/4.4.b13.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1, spine:6 and Annex D row qaa/fheq-2024/annex-d/transferable/r4 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is thinking about exhibiting, selling or publishing, or a team is planning professional practice modules. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'Where could this work be shown, sold or published, and what would it take to get it there?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b14
  forPractitioner: { text: "At threshold (the minimum for the honours award), the graduate recognises and explains their strengths and development needs so that they can collaborate and become aware of professional networks; set and assess level 6 work so that this can be seen.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you recognise and explain your strengths and what you need to develop, so you can collaborate and get to know professional networks.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold) for 'Employability' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Employability, threshold column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b12) holds the nearest outcome, and do not equate it with any one degree class. Set it beside the typical cell qaa/art-and-design-2026/4.4.b14.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3, spine:6 and Annex D's third-class description qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Bring this up when a student is planning placements, networks or a career, or a team is reviewing employability provision. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the threshold rung. Ask: 'What are you good at, what do you need to develop, and who in your field do you already know?' Do not read the table out at length."
- statement: qaa/art-and-design-2026/4.4.b14.excellent
  forPractitioner: { text: "At the excellent rung, the graduate actively looks for and makes the most of chances to grow professional networks, showing initiative, adaptability and professionalism; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you actively look for and make the most of chances to grow your professional networks, showing initiative, adaptability and professionalism.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes) for 'Employability' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Employability, excellent column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b12) holds the nearest outcome, and never present it as the pass requirement. Set it beside the typical cell qaa/art-and-design-2026/4.4.b14.typical, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3, spine:6 and Annex D row qaa/fheq-2024/annex-d/transferable/r2 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is planning placements, networks or a career, or a team is reviewing employability provision. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the excellent rung. Ask: 'What are you good at, what do you need to develop, and who in your field do you already know?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.4.b14.typical
  forPractitioner: { text: "At the typical rung, the graduate shows they are committed to growing personally and to building professional contacts; set and assess level 6 work so that this can be seen.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you show you are committed to your own growth and to building professional contacts.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes) for 'Employability' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree with honours. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.4, Table 1: Employability, typical column). Do not call it a regulatory requirement or apply it to master's study, where para 4.7 (qaa/art-and-design-2026/4.7.b12) holds the nearest outcome, and never present it as the pass requirement. Set it beside the threshold cell qaa/art-and-design-2026/4.4.b14 and the excellent cell qaa/art-and-design-2026/4.4.b14.excellent, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3, spine:6 and Annex D row qaa/fheq-2024/annex-d/transferable/r2 for comparison only, since the statement ties no rung to a degree class."
  author-agent-dialogue: "Bring this up when a student is planning placements, networks or a career, or a team is reviewing employability provision. With a student, put it in plain second-person words about their own work; with staff, frame it as what level 6 work in this area lets a graduate show at the typical rung. Ask: 'What are you good at, what do you need to develop, and who in your field do you already know?' Do not read the table out at length, and do not present this cell as the minimum a student must reach."
- statement: qaa/art-and-design-2026/4.5
  forPractitioner: { text: "Design master's study so that students reach deeper technical, critical, conceptual and contextual understanding, and also meet the honours standards of Table 1 (read as required, force must).", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level you must reach a deeper technical, critical, conceptual and contextual understanding, while also meeting everything expected at honours level.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as the master's requirement (force: must, from the issuer's 'require') at FHEQ Level 7 (FQHEIS Level 11): honours standards plus deeper understanding. Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.5). Do not claim it applies to honours study or that it is a regulatory rule. Set it beside the list in para 4.7 (qaa/art-and-design-2026/4.7.b1 to 4.7.b12), Table 1, the FHEQ master's descriptor qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it with a master's applicant or student asking how the level differs from their degree, or a team writing level 7 outcomes. Say plainly to a student that the honours skills are the floor and the master's adds depth in four kinds of understanding. Ask: 'Which of technical, critical, conceptual or contextual understanding has grown most in your work?' Avoid reading the master's list out in full."
- statement: qaa/art-and-design-2026/4.7.b1
  forPractitioner: { text: "Master's graduates will typically be able to apply theoretical, practical, technical and contextual knowledge with system and rigour as creative, academic or professional work develops; give level 7 modules and the major project room for this.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to bring theory, practice, technique and context to your work with rigour and method, whether the result is creative, academic or professional.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the outcomes master's graduates are typically able to show (force: will, framed by the issuer as typical), at FHEQ Level 7 (FQHEIS Level 11), resting on the honours standards (para 4.5). Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.7, item 1). Do not present it as a regulatory requirement, a pass threshold or an honours-level outcome. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b3, spine:7, para 4.5 (qaa/art-and-design-2026/4.5) and the honours row qaa/art-and-design-2026/4.4.b3."
  author-agent-dialogue: "Raise it when a student is shaping a major project or a team is writing level 7 project outcomes. With a master's student, say it plainly in the second person; with a programme team, frame it as what level 7 study gives room to show. Ask: 'Which kinds of knowledge does this project lean on, and how do you test that you have used them rigorously?' Avoid reading the whole list aloud and avoid treating it as a pass rule."
- statement: qaa/art-and-design-2026/4.7.b2
  forPractitioner: { text: "Master's graduates will typically be able to use materials widely and inventively, extending how things are made and bringing new approaches into creative practice; give level 7 modules and the major project room for this.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to use materials widely and inventively, pushing how things are made and bringing new approaches into your practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the outcomes master's graduates are typically able to show (force: will, framed by the issuer as typical), at FHEQ Level 7 (FQHEIS Level 11), resting on the honours standards (para 4.5). Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.7, item 2). Do not present it as a regulatory requirement, a pass threshold or an honours-level outcome. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b3, spine:7, para 4.5 (qaa/art-and-design-2026/4.5) and the honours row qaa/art-and-design-2026/4.4.b2."
  author-agent-dialogue: "Raise it when a student is pushing a material or process further or a team is planning studio and workshop access at level 7. With a master's student, say it plainly in the second person; with a programme team, frame it as what level 7 study gives room to show. Ask: 'What have you done with this material that you had not seen done before?' Avoid reading the whole list aloud and avoid treating it as a pass rule."
- statement: qaa/art-and-design-2026/4.7.b3
  forPractitioner: { text: "Master's graduates will typically be able to build and use methods and methodologies systematically to carry advanced inquiry; give level 7 modules and the major project room for this.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to build and use research methods and methodologies systematically to carry advanced inquiry.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the outcomes master's graduates are typically able to show (force: will, framed by the issuer as typical), at FHEQ Level 7 (FQHEIS Level 11), resting on the honours standards (para 4.5). Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.7, item 3). Do not present it as a regulatory requirement, a pass threshold or an honours-level outcome. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b2, spine:7, para 4.5 (qaa/art-and-design-2026/4.5) and the honours row qaa/art-and-design-2026/4.4.b1."
  author-agent-dialogue: "Raise it when a student is designing the method for a research-led project or a team is planning research training. With a master's student, say it plainly in the second person; with a programme team, frame it as what level 7 study gives room to show. Ask: 'Why is this the right method for your question, and what would another method show?' Avoid reading the whole list aloud and avoid treating it as a pass rule."
- statement: qaa/art-and-design-2026/4.7.b4
  forPractitioner: { text: "Master's graduates will typically be able to analyse research, iteration and contextual factors critically and thoroughly so that practice moves forward; give level 7 modules and the major project room for this.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to analyse research, your iterations and the context of your work critically and thoroughly, so your practice moves forward.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the outcomes master's graduates are typically able to show (force: will, framed by the issuer as typical), at FHEQ Level 7 (FQHEIS Level 11), resting on the honours standards (para 4.5). Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.7, item 4). Do not present it as a regulatory requirement, a pass threshold or an honours-level outcome. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b4.1, spine:7, para 4.5 (qaa/art-and-design-2026/4.5) and the honours row qaa/art-and-design-2026/4.4.b5."
  author-agent-dialogue: "Raise it when a student is reviewing iterations of their work or a team is setting critical writing at level 7. With a master's student, say it plainly in the second person; with a programme team, frame it as what level 7 study gives room to show. Ask: 'What did your analysis of the last round of work change in the next?' Avoid reading the whole list aloud and avoid treating it as a pass rule."
- statement: qaa/art-and-design-2026/4.7.b5
  forPractitioner: { text: "Master's graduates will typically be able to realise practice, research, ideas and knowledge to a professional standard in visual, spoken or written form across varied, complex and unpredictable settings; give level 7 modules and the major project room for this.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to bring practice, research, ideas and knowledge to a professional finish in visual, spoken or written form, in varied, complex and unpredictable settings.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the outcomes master's graduates are typically able to show (force: will, framed by the issuer as typical), at FHEQ Level 7 (FQHEIS Level 11), resting on the honours standards (para 4.5). Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.7, item 5). Do not present it as a regulatory requirement, a pass threshold or an honours-level outcome. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b5 and qaa/fheq-2024/4.17.b8.2, spine:7, para 4.5 (qaa/art-and-design-2026/4.5) and the honours row qaa/art-and-design-2026/4.4.b6."
  author-agent-dialogue: "Raise it when a student is preparing work for a public or professional setting or a team is designing a final show or viva. With a master's student, say it plainly in the second person; with a programme team, frame it as what level 7 study gives room to show. Ask: 'Which form suits this work best, and how will it hold up in a setting you do not control?' Avoid reading the whole list aloud and avoid treating it as a pass rule."
- statement: qaa/art-and-design-2026/4.7.b6
  forPractitioner: { text: "Master's graduates will typically be able to reflect critically on practice in a systematic and purposeful way, supporting intellectual growth and innovation; give level 7 modules and the major project room for this.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to reflect critically on your practice in a planned, purposeful way that helps you grow and innovate.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the outcomes master's graduates are typically able to show (force: will, framed by the issuer as typical), at FHEQ Level 7 (FQHEIS Level 11), resting on the honours standards (para 4.5). Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.7, item 6). Do not present it as a regulatory requirement, a pass threshold or an honours-level outcome. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b6 and qaa/fheq-2024/4.17.b7, spine:7, para 4.5 (qaa/art-and-design-2026/4.5) and the honours row qaa/art-and-design-2026/4.4.b7."
  author-agent-dialogue: "Raise it when a student is writing a reflective account or a team is assessing reflection at level 7. With a master's student, say it plainly in the second person; with a programme team, frame it as what level 7 study gives room to show. Ask: 'What is your method for reflecting, and what has it led you to change?' Avoid reading the whole list aloud and avoid treating it as a pass rule."
- statement: qaa/art-and-design-2026/4.7.b7
  forPractitioner: { text: "Master's graduates will typically be able to use professional working methods with confidence across a range of complex situations; give level 7 modules and the major project room for this.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to use professional ways of working with confidence in a range of complex situations.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the outcomes master's graduates are typically able to show (force: will, framed by the issuer as typical), at FHEQ Level 7 (FQHEIS Level 11), resting on the honours standards (para 4.5). Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.7, item 7). Do not present it as a regulatory requirement, a pass threshold or an honours-level outcome. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b8.2, spine:7, para 4.5 (qaa/art-and-design-2026/4.5) and the honours row qaa/art-and-design-2026/4.4.b13."
  author-agent-dialogue: "Raise it when a student is on a placement or live brief or a team is planning professional practice at level 7. With a master's student, say it plainly in the second person; with a programme team, frame it as what level 7 study gives room to show. Ask: 'In your last complex brief, which professional methods held up and which did not?' Avoid reading the whole list aloud and avoid treating it as a pass rule."
- statement: qaa/art-and-design-2026/4.7.b8
  forPractitioner: { text: "Master's graduates will typically be able to use flexible and agile methods of working to move projects on and take a creative approach to problems; give level 7 modules and the major project room for this.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to work flexibly and with agility to move projects on and take a creative approach to problems.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the outcomes master's graduates are typically able to show (force: will, framed by the issuer as typical), at FHEQ Level 7 (FQHEIS Level 11), resting on the honours standards (para 4.5). Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.7, item 8). Do not present it as a regulatory requirement, a pass threshold or an honours-level outcome. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b5, spine:7, para 4.5 (qaa/art-and-design-2026/4.5) and the honours row qaa/art-and-design-2026/4.4.b9."
  author-agent-dialogue: "Raise it when a project has changed course or a team is planning collaborative or live work. With a master's student, say it plainly in the second person; with a programme team, frame it as what level 7 study gives room to show. Ask: 'When the brief changed, how did you adapt your way of working?' Avoid reading the whole list aloud and avoid treating it as a pass rule."
- statement: qaa/art-and-design-2026/4.7.b9
  forPractitioner: { text: "Master's graduates will typically be able to place practice in a clearly defined, critically informed context and question how it relates to ethical working practices, responsibilities and implications; give level 7 modules and the major project room for this.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to place your practice in a clear, critically informed context and question its ethics, responsibilities and consequences.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the outcomes master's graduates are typically able to show (force: will, framed by the issuer as typical), at FHEQ Level 7 (FQHEIS Level 11), resting on the honours standards (para 4.5). Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.7, item 9). Do not present it as a regulatory requirement, a pass threshold or an honours-level outcome. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b1, spine:7, para 4.5 (qaa/art-and-design-2026/4.5) and the honours row qaa/art-and-design-2026/4.4.b11."
  author-agent-dialogue: "Raise it when a student is framing a major project or a team is placing ethics in level 7 study. With a master's student, say it plainly in the second person; with a programme team, frame it as what level 7 study gives room to show. Ask: 'What context does your practice belong to, and what ethical questions does that raise?' Avoid reading the whole list aloud and avoid treating it as a pass rule."
- statement: qaa/art-and-design-2026/4.7.b10
  forPractitioner: { text: "Master's graduates will typically be able to interpret knowledge within a clearly bounded context that is alert to cultural, environmental, social and political matters; give level 7 modules and the major project room for this.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to interpret knowledge within a clearly bounded context, alert to cultural, environmental, social and political matters.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the outcomes master's graduates are typically able to show (force: will, framed by the issuer as typical), at FHEQ Level 7 (FQHEIS Level 11), resting on the honours standards (para 4.5). Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.7, item 10). Do not present it as a regulatory requirement, a pass threshold or an honours-level outcome. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b1, spine:7, para 4.5 (qaa/art-and-design-2026/4.5) and the honours row qaa/art-and-design-2026/4.4.b3."
  author-agent-dialogue: "Raise it when a student is building the context for a thesis or project or a team is planning critical studies at level 7. With a master's student, say it plainly in the second person; with a programme team, frame it as what level 7 study gives room to show. Ask: 'Which cultural, environmental, social or political factors shape how your work should be read?' Avoid reading the whole list aloud and avoid treating it as a pass rule."
- statement: qaa/art-and-design-2026/4.7.b11
  forPractitioner: { text: "Master's graduates will typically be able to use creative strategies that put equity and inclusion at their centre, answering structural injustice through design or artistic intervention; give level 7 modules and the major project room for this.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to use creative strategies built around equity and inclusion, answering structural injustice through design or art.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the outcomes master's graduates are typically able to show (force: will, framed by the issuer as typical), at FHEQ Level 7 (FQHEIS Level 11), resting on the honours standards (para 4.5). Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.7, item 11). Do not present it as a regulatory requirement, a pass threshold or an honours-level outcome. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b8.1, spine:7, para 4.5 (qaa/art-and-design-2026/4.5) and the honours row qaa/art-and-design-2026/4.4.b11."
  author-agent-dialogue: "Raise it when a student is working on a project about injustice or a team is embedding equity in level 7 briefs. With a master's student, say it plainly in the second person; with a programme team, frame it as what level 7 study gives room to show. Ask: 'What injustice does this work respond to, and who shaped the response with you?' Avoid reading the whole list aloud and avoid treating it as a pass rule."
- statement: qaa/art-and-design-2026/4.7.b12
  forPractitioner: { text: "Master's graduates will typically be able to work collaboratively with initiative, responsiveness and leadership to reach shared goals and add to positive change; give level 7 modules and the major project room for this.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to work with others, taking the initiative, responding and leading, to reach shared goals and make a positive difference.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the outcomes master's graduates are typically able to show (force: will, framed by the issuer as typical), at FHEQ Level 7 (FQHEIS Level 11), resting on the honours standards (para 4.5). Cite it as (QAA, 2026, Art and Design Subject Benchmark Statement, para 4.7, item 12). Do not present it as a regulatory requirement, a pass threshold or an honours-level outcome. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b8.1, spine:7, para 4.5 (qaa/art-and-design-2026/4.5) and the honours row qaa/art-and-design-2026/4.4.b14."
  author-agent-dialogue: "Raise it when a student is leading or joining a team project or a team is assessing collaboration at level 7. With a master's student, say it plainly in the second person; with a programme team, frame it as what level 7 study gives room to show. Ask: 'What part did you play in the group, and what changed because of it?' Avoid reading the whole list aloud and avoid treating it as a pass rule."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:4", role: "cites", locator: "D1, 2.15" }
  - { id: "fheq:5", role: "cites", locator: "D1, 2.15" }
  - { id: "fheq:6", role: "cites", locator: "D1, 2.12; 2.16; 2.18" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.12; 2.18; 4.8" }
  - { id: "fqheis:7", role: "cites", locator: "D1, 2.15" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 2.15" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.17" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.12; 2.17; 2.18" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.12; 2.18; 4.8" }
  - { id: "spine:6", role: "refers", locator: "std:ref:uk-framework, R2 and R8 (inferred: Table 1 and the generic skills sit at this step)" }
  - { id: "spine:7", role: "refers", locator: "std:ref:uk-framework, R2 and R8 (inferred: the master's outcomes in 4.7)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.12; 2.18: honours degree, FHEQ Level 6, FQHEIS Level 10)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.12; 2.18; 4.8: integrated master's)" }
  - { from: "fheq:4", to: "fqheis:7", relation: "equivalent", basis: "stated (D1, 2.15: Certificate of Higher Education)" }
  - { from: "fheq:5", to: "fqheis:8", relation: "equivalent", basis: "stated (D1, 2.15: Diploma of Higher Education)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.10", "1.11", "1.12", "1.13", "1.14", "1.15", "1.16", "1.19", "1.21", "1.32", "1.38", "1.40", "3.17", "3.18", "3.19", "4.3", "4.4", "4.7"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "3.13", "3.20", "4.4"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.6", "1.25", "1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "1.49", "4.4"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.9", "1.29", "1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "3.14", "3.16", "4.4"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["1.33", "1.37", "1.41", "1.42", "1.43", "1.44", "1.45", "1.46", "1.47", "1.48", "1.49", "1.50"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-art-and-design-2019-benchmarks (not yet ingested)", note: "the fourth edition, 2019, a minor update of 2016 (D1, back matter): Part E" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree classification descriptions for honours, named in 4.2" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ Levels 4 to 7 (2.12, 2.15, 2.16, 2.18, 4.8)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS/SCQF Levels 7 to 11 (2.12, 2.15, 2.17, 2.18, 4.8)" }
- { rel: "cites", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "Education for Sustainable Development (QAA and Advance HE, 2021), 1.26" }
- { rel: "refersTo", target: "QAA Quality Code 2024 and QAA Glossary (not yet ingested)", note: "front matter" }
- { rel: "refersTo", target: "PSRB requirements: Institution of Engineering Designers; Chartered Society of Designers (not yet ingested)", note: "2.23; Part E" }
- { rel: "relatedTo", target: "std:doc:qaa-history-of-art-architecture-and-design-2026-benchmarks", note: "inferred: a neighbouring subject in the same series; not named in the text" }
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
- A broad subject of many disciplines, practice-based and student-centred, in which making and creative inquiry are both how students learn and how they show their learning (D1, 1.4, 2.5, 2.6).
- Its practices conceive, test, make and share work that shapes visual and material culture, drawing on visual, spatial and sensory languages (D1, 1.5, 1.6).
- Studios and workshops shape learning; flexible and online modes now sit beside them (D1, 1.7, 2.10, 3.13).
- It is increasingly interdisciplinary, crossing into the humanities, business, engineering, computing, health and the built environment (D1, 1.8, 2.1, 2.4, 3.15).
- Contextual and critical study (history, theory, discourse) runs through practice rather than beside it (D1, 2.9, 3.3, 3.11).
- Assessment looks at process as well as product, often holistically, with feedback through reviews or crits (D1, 2.8, 3.19, 3.21, 3.31).
- Live briefs, exhibitions, placements and partnerships tie learning to creative careers (D1, 1.38, 2.7, 2.22, 3.16).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "headed equity, diversity and inclusion: diverse practices and student voices as a driver of creativity, decolonial attention to the subject's knowledge traditions, studio culture as an inclusive community, inclusive assessment; at the rungs, ethics and unequal representation; at master's, equity-centred creative strategy (D1, 1.10 to 1.16; 3.17 to 3.19; 4.4; 4.7)"
  statements: ["qaa/art-and-design-2026/4.4.b11", "qaa/art-and-design-2026/4.4.b11.typical", "qaa/art-and-design-2026/4.4.b11.excellent", "qaa/art-and-design-2026/4.7.b11"]
- theme: theme:accessibility
  inThisSubject: "the Equality Act duty of reasonable and anticipatory adjustment applied to studios, live projects, group work, hybrid learning and flexible assessment formats, with making itself accepted as evidence (D1, 1.17 to 1.24; 3.13; 3.20)"
  statements: ["qaa/art-and-design-2026/1.19", "qaa/art-and-design-2026/4.4.b11.typical"]
- theme: theme:esd
  inThisSubject: "sustainability as an ethical frame for creative practice: regenerative design, circularity, responsible digital practice and the cost of GenAI, with a sustainability literacy row in Table 1 (D1, 1.25 to 1.33; 1.49; 4.4)"
  statements: ["qaa/art-and-design-2026/4.4.b12", "qaa/art-and-design-2026/4.4.b12.typical", "qaa/art-and-design-2026/4.4.b12.excellent", "qaa/art-and-design-2026/4.7.b10"]
- theme: theme:enterprise
  inThisSubject: "named employability, entrepreneurship and enterprise education: resilient, self-employed and IP-led creative careers, live projects and placements, a skills list in 1.40, and two rows of Table 1 (D1, 1.34 to 1.40; 3.16; 4.4)"
  statements: ["qaa/art-and-design-2026/4.4.b13", "qaa/art-and-design-2026/4.4.b13.typical", "qaa/art-and-design-2026/4.4.b13.excellent", "qaa/art-and-design-2026/4.4.b14", "qaa/art-and-design-2026/4.4.b14.typical", "qaa/art-and-design-2026/4.4.b14.excellent", "qaa/art-and-design-2026/4.7.b7", "qaa/art-and-design-2026/4.7.b12"]
- theme: theme:generative-ai
  inThisSubject: "GenAI as one tool in creative workflows: a spectrum from automation to refusal, students taking their own position, authentic assessment with process documentation, bias and cultural visibility, environmental cost and intellectual property (D1, 1.41 to 1.50)"
  statements: []
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.3", gloss: "four typical areas: art and design practices; historical, theoretical and critical studies; research-led practice and methods; professional skills development" }
  - { component: "3.2", gloss: "curricula answering technology, planetary concerns, global views and industry change" }
  - { component: "3.4", gloss: "aims: independent thinking, creative innovation, professional engagement" }
practices:
  - { component: "3.5", kind: "teaching", gloss: "studio learning, workshops, tutorials, reviews, peer learning, study visits, lectures, seminars" }
  - { component: "3.6", kind: "teaching", gloss: "studio, lecture and project-based teaching and what each develops" }
  - { component: "3.8", kind: "learning", gloss: "scheduled and independent learning, becoming more self-directed" }
  - { component: "3.11", kind: "learning", gloss: "discursive learning with texts, discussion and presentation" }
  - { component: "3.14", kind: "learning", gloss: "group work and projects" }
  - { component: "3.15", kind: "learning", gloss: "interdisciplinary collaborative projects" }
  - { component: "3.16", kind: "teaching", gloss: "industry, enterprise and employability activities; placements; competitions" }
  - { component: "3.21", kind: "assessment", gloss: "assessing both process and product" }
  - { component: "3.23", kind: "assessment", gloss: "self and peer assessment" }
  - { component: "3.25", kind: "assessment", gloss: "fourteen methods, from portfolios and exhibitions to pitches, sketchbooks and timed practicals" }
  - { component: "3.27", kind: "assessment", gloss: "continuous formative feedback" }
  - { component: "3.31", kind: "assessment", gloss: "the crit, or review, run inclusively" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.4", award: "bachelor's with honours", items: 14 }
  - { rung: "typical", leadIn: "4.4", award: "bachelor's with honours", items: 14 }
  - { rung: "excellent", leadIn: "4.4", award: "bachelor's with honours", items: 14 }
rungBases: "4.1 frames the three as minimum (threshold), typical and excellent standards shown at the honours award; 4.2 says most students exceed threshold and points to Annex D; 4.4 says the descriptors build on each other incrementally and gives Table 1, fourteen attributes in two groups (subject knowledge and understanding; professional and transferable skills), each with a threshold, typical and excellent cell"
outcomeLists:
  - { leadIn: "4.7", gloss: "master's graduates are typically able to", items: 12, award: ["master's"] }
outcomes:
  - { outcome: "research and inquiry", threshold: "qaa/art-and-design-2026/4.4.b1", typical: "qaa/art-and-design-2026/4.4.b1.typical", excellent: "qaa/art-and-design-2026/4.4.b1.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "material knowledge", threshold: "qaa/art-and-design-2026/4.4.b2", typical: "qaa/art-and-design-2026/4.4.b2.typical", excellent: "qaa/art-and-design-2026/4.4.b2.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "contextual awareness", threshold: "qaa/art-and-design-2026/4.4.b3", typical: "qaa/art-and-design-2026/4.4.b3.typical", excellent: "qaa/art-and-design-2026/4.4.b3.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "engagement with contemporary discourse and debate", threshold: "qaa/art-and-design-2026/4.4.b4", typical: "qaa/art-and-design-2026/4.4.b4.typical", excellent: "qaa/art-and-design-2026/4.4.b4.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "analysis", threshold: "qaa/art-and-design-2026/4.4.b5", typical: "qaa/art-and-design-2026/4.4.b5.typical", excellent: "qaa/art-and-design-2026/4.4.b5.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "realisation", threshold: "qaa/art-and-design-2026/4.4.b6", typical: "qaa/art-and-design-2026/4.4.b6.typical", excellent: "qaa/art-and-design-2026/4.4.b6.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "reflection", threshold: "qaa/art-and-design-2026/4.4.b7", typical: "qaa/art-and-design-2026/4.4.b7.typical", excellent: "qaa/art-and-design-2026/4.4.b7.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "awareness of audience and impact", threshold: "qaa/art-and-design-2026/4.4.b8", typical: "qaa/art-and-design-2026/4.4.b8.typical", excellent: "qaa/art-and-design-2026/4.4.b8.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "independence and management", threshold: "qaa/art-and-design-2026/4.4.b9", typical: "qaa/art-and-design-2026/4.4.b9.typical", excellent: "qaa/art-and-design-2026/4.4.b9.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "communication", threshold: "qaa/art-and-design-2026/4.4.b10", typical: "qaa/art-and-design-2026/4.4.b10.typical", excellent: "qaa/art-and-design-2026/4.4.b10.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "ethics and social responsibility", threshold: "qaa/art-and-design-2026/4.4.b11", typical: "qaa/art-and-design-2026/4.4.b11.typical", excellent: "qaa/art-and-design-2026/4.4.b11.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "sustainability literacy", threshold: "qaa/art-and-design-2026/4.4.b12", typical: "qaa/art-and-design-2026/4.4.b12.typical", excellent: "qaa/art-and-design-2026/4.4.b12.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "enterprise and entrepreneurship", threshold: "qaa/art-and-design-2026/4.4.b13", typical: "qaa/art-and-design-2026/4.4.b13.typical", excellent: "qaa/art-and-design-2026/4.4.b13.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "employability", threshold: "qaa/art-and-design-2026/4.4.b14", typical: "qaa/art-and-design-2026/4.4.b14.typical", excellent: "qaa/art-and-design-2026/4.4.b14.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
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
- { body: "professional, statutory and regulatory bodies (PSRBs), as a class", says: "consulted in course design where relevant; may accredit courses through review of curriculum, facilities, staffing, assessment and partnerships; their requirements inform competence standards (D1, front matter; 2.2; 2.23; 2.28; 4.3)", requirements: "not yet ingested (Part E)" }
- { body: "Institution of Engineering Designers", says: "an industry-led skills body that accredits courses, for example in product design (D1, 2.23)", requirements: "not yet ingested (Part E)" }
- { body: "Chartered Society of Designers", says: "an industry-led skills body that accredits courses (D1, 2.23)", requirements: "not yet ingested (Part E)" }
- { body: "The Association of Photographers", says: "a professional body that does not accredit; affiliated courses gain industry insight and opportunities (D1, 2.23)", requirements: "not yet ingested (Part E)" }
- { body: "the Association of Illustrators", says: "a professional body that does not accredit; affiliation gives access to insight and opportunities (D1, 2.23)", requirements: "not yet ingested (Part E)" }
- { body: "Interior Educators", says: "a professional body that does not accredit; affiliation gives access to insight and opportunities (D1, 2.23)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equity, diversity and inclusion (EDI)", carriedIn: ["1.10", "1.11", "1.12", "1.13", "1.14", "1.15", "1.16", "1.19", "1.21", "1.32", "1.38", "1.40", "3.17", "3.18", "3.19", "4.3", "4.4", "4.7"], statements: ["4.4.b11", "4.4.b11.typical", "4.4.b11.excellent", "4.7.b11"] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "3.13", "3.20", "4.4"], statements: ["1.19", "4.4.b11.typical"] }
  - { id: "theme:esd", named: "Education for sustainable development (ESD)", carriedIn: ["1.6", "1.25", "1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "1.49", "4.4"], statements: ["4.4.b12", "4.4.b12.typical", "4.4.b12.excellent", "4.7.b10"] }
  - { id: "theme:enterprise", named: "Employability, entrepreneurship and enterprise education (EEE)", carriedIn: ["1.9", "1.29", "1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "3.14", "3.16", "4.4"], statements: ["4.4.b13", "4.4.b13.typical", "4.4.b13.excellent", "4.4.b14", "4.4.b14.typical", "4.4.b14.excellent", "4.7.b7", "4.7.b12"] }
  - { id: "theme:generative-ai", named: "Generative artificial intelligence (GenAI)", carriedIn: ["1.33", "1.37", "1.41", "1.42", "1.43", "1.44", "1.45", "1.46", "1.47", "1.48", "1.49", "1.50"], statements: [] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["2.12", "2.15", "2.16", "2.18", "4.2", "4.8"] }
  - { framework: "scqf", levels: ["fqheis:7", "fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.12", "2.15", "2.17", "2.18", "4.8"] }
bodies:
  - { body: "PSRBs", citedIn: ["2.2", "2.23", "2.28", "4.3"] }
  - { body: "Institution of Engineering Designers", citedIn: ["2.23"] }
  - { body: "Chartered Society of Designers", citedIn: ["2.23"] }
  - { body: "The Association of Photographers", citedIn: ["2.23"] }
  - { body: "the Association of Illustrators", citedIn: ["2.23"] }
  - { body: "Interior Educators", citedIn: ["2.23"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "descriptions of the four honours classes, for evidence of achievement above threshold" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Education for Sustainable Development (QAA and Advance HE, 2021)", citedIn: ["1.26"], role: "learning outcomes for sustainability" }
  - { document: "not yet ingested: listed in Part E", named: "Quality Code (2024 update); QAA Glossary", citedIn: ["front matter"], role: "companion reference points" }
  - { document: "not yet ingested: listed in Part E", named: "Equality Act 2010", citedIn: ["1.10", "1.19", "4.3"], role: "legal basis for EDI, adjustments and competence standards" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "discipline-art-and-design", definition: "a distinct area of activity within the subject of Art and Design, some still evolving; the statement keeps 'subject' for Art and Design as a whole (D1, 1.2)", beneficiaryDefinition: "one of the separate areas of art and design you might specialise in, such as illustration or product design", scopeNote: "used throughout for specialisms", category: "unknown", practices: ["art and design"] }
- { slug: "course", definition: "an approved pathway of study giving a coherent learning experience that normally leads to a qualification; used interchangeably with programme (D1, front matter)", beneficiaryDefinition: "the whole set of study you sign up for that leads to your award", scopeNote: "also called programme", category: "unknown", practices: ["education"] }
- { slug: "module", definition: "a self-contained, formally structured unit of study with its own learning outcomes and assessment criteria; used interchangeably with unit (D1, front matter)", beneficiaryDefinition: "one self-contained block of your course with its own outcomes and assessment", scopeNote: "also called unit", category: "unknown", practices: ["education"] }
- { slug: "review-crit", definition: "the studio practice of critical discussion of student work, historically the 'crit'; some providers now say 'review' because of associations with power imbalance (D1, 3.31)", beneficiaryDefinition: "a session where your work is discussed critically with tutors, peers or outside guests", scopeNote: "crit, critique and review name the same practice", category: "unknown", practices: ["art and design"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "discipline-art-and-design", form: "disciplines", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "course", form: "course", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "course", form: "programme", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "formal" }
- { concept: "module", form: "module", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "module", form: "unit", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "formal" }
- { concept: "review-crit", form: "review", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "review-crit", form: "Crit", lang: "en", partOfSpeech: "noun", termStatus: "deprecated", register: "informal" }
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
  title: "Subject Benchmark Statement Art and Design"
  edition: "April 2026 (fifth edition)"
  year: 2026
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/art-and-design-2026/art-and-design-2026.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: a36e11f8640452d59e5810ec755b4f3983e7014f7267c29ad88ae2c91eb89193
  heldFiles: ["wkspc2601-library/txt/qaa-2026-art-design-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2026-art-design-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2026-art-design-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2026-art-design-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0033", title: "Subject Benchmark Statement: Art and Design (QAA, 2019, fourth edition)", why: "the superseded edition, for supersedes and a comparison of the standards" }
```

## Part E Gaps and questions
- Skeleton: bm-skel.json was absent from run-src at the start of run 0088; generated with tools/std_prep.py art-and-design-2026 (no judgement fields). Its rung counts were 0 because Table 1 is linearised into paragraph 4.4.
- Pattern (differs from Psychology): the rungs are one table (Table 1, in 4.4) of fourteen attributes, each with a threshold, typical and excellent cell, in two groups (subject knowledge and understanding; professional and transferable skills). Recorded per the batch-1 table convention: ids 4.4.b<n>, 4.4.b<n>.typical, 4.4.b<n>.excellent; each cell has its own span (cut by `find`), since every cell carries its own wording.
- gradeOf for all 28 typical and excellent cells is stated (the issuer pairs the cells in one row), not inferred.
- Force on the rungs: the cells carry no modal. The threshold cells take force threshold (4.1, "minimum (threshold)"); the typical and excellent cells are recorded as describes. 4.1's "will have demonstrated" covers all three, but sits too far from the cells for the builder's force check; for Abbott: whether typical and excellent should read will, as in Psychology.
- Pattern: no master's rungs; 4.7 is a list of twelve outcomes with the lead-in "are typically able to" (recorded as rung none, force will, award master's, fheq:7). The word 'typically' may mark it as a typical-level list; for Abbott.
- 4.5: "Master's level degrees require" recorded as force must (required is must, batch-1 convention); for Abbott.
- 4.8: integrated master's "meets FHEQ Level 7/FQHEIS Level 11 standards", plain present with no modal: not a statement; S3 component only.
- Plain-present provider norms (not statements, template open point 5): 1.10 and 1.16 (courses aim, enable); 1.21 (studios designed or adapted to be accessible); 1.45 (courses use authentic assessments including GenAI); 2.18 (integrated master's designed to meet the descriptors in full); 3.7 (students are able to access resources: a provision, not an outcome); 3.16 (courses include industry activities); 4.6 (postgraduate courses include all three elements).
- Obliging words outside the five, left as components: 1.14 and 1.38 ("essential"); 1.37 ("there is a need for graduates", "Graduates ... require"); 1.39 ("are essential professional competencies"); 3.18 ("requiring diverse and inclusive modes of assessment"); 2.13 ("it would be expected", "may require"). Recorded as describes in effect (no statement); for Abbott.
- 2.27: "They will consider" describes the external examiner's role, an actor neither learner nor provider; not cut as a statement. 2.24 and 2.25 were cut as provider expectations (will).
- 1.40: a list of thirteen skills under "Art and Design education provides opportunities for students to develop ... The skills include"; a provision list, not an outcome list ("are able to"), so not cut; the skeleton's 1.40.b1 to b13 are left as candidates. For Abbott: it reads like an employability outcome list.
- 3.3 and 3.25 lists (areas of study; assessment methods) are descriptive, recorded in SB3, not cut.
- Section headings run on at the end of the paragraph before them in the held text (1.9, 1.16, 1.24, 1.33, 1.40.b13, 2.11, 2.15, 2.20, 2.23, 2.28, 3.1, 3.4, 3.16, 3.17, 3.25.b14); the skeleton's theme hits on those headings (1.9 EDI, 1.24 ESD, 1.33 enterprise) are not counted in SB6 unless the paragraph also treats the theme.
- SB6: the theme names in the front matter (key changes list) are excluded matter. 3.13 and 3.20 (accessibility) and 3.14 and 3.16 (employability) carry the theme by cross-reference ("see Accessibility, paragraphs 1.17-1.24"); the numbers after "paragraphs" are references, not statements (DPN-1).
- Generative AI is a cross-cutting theme here (theme:generative-ai, 1.41 to 1.50; also named in 1.33 and 1.37); no statement is cut from it.
- Theme name variant: the statement says "Equity, diversity and inclusion", not equality; mapped to theme:edi.
- Levels: 1.18 names "Level 3 qualifications" (entry, outside the HE frameworks; RQF or CQFW not named): not recorded in S5.
- CQFW is not cited. FQHEIS is cited as "SCQF/FQHEIS" (2.17, 2.18) and as FQHEIS (2.12, 2.15, 4.8); FHEQ also in 4.2 as the Frameworks document.
- Inferred codes, held back from lookup until P3: hecos 101361 creative arts and design, 100059 fine art, 100048 design; cah CAH25-01-01, CAH25-01-02, CAH25-01-03. The text names the subject "Art and Design" but no code; 100050 product design is a specialism named in 2.23 (statedSubjects only).
- S5: spine:6 and spine:7 are inferred from the reference framework (R2, R8); generic-skill records carry fheq:6 (Table 1) or fheq:7 (4.7).
- Bodies: the PSRBs and five named bodies (2.23) have no ingested requirements; named but not bodies of the subject: Office for Students (front matter), Equality and Human Rights Commission (4.3), Design Council (1.25), UNESCO (1.26), Advance HE (1.26), DCMS and Arts Council England (1.35).
- Shared documents not ingested: QAA Quality Code 2024 and Glossary (front matter); Equality Act 2010 (1.10, 1.19, 4.3); UN Sustainable Development Goals and the Design Council's Skills for Planet (1.25); UNESCO key competencies for sustainability (1.26); national access plans by nation (1.11).
- Table 1 cell text has stray spaces from extraction ("self- awareness"); sources keep the held text as it is.
- supersedes: the fourth edition (2019) is named in back matter only; its document id is a placeholder.
- S9 commentary not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:31: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0088 (P1); built by tools/bm_build.py.
