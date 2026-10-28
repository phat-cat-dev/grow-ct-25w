---
id: std:doc:qaa-geography-2022-benchmarks
title: "Subject Benchmark Statement: Geography"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100409", label: "geography", basis: "inferred" }
  - { scheme: "cah", code: "CAH26-01-01", label: "geography (non-specific)", basis: "inferred" }
edition: "March 2022 (fifth edition)"
published: 2022-03
status: current
supersedes: "the fourth edition, 2019 (D1, back matter): std:doc:qaa-geography-2019-benchmarks, not held"
heldText: { method: sha256-bytes, raw: c19bcde6392a92c322294fbd4a0d50c50206840eebc546fe98395c3c7e2e9488, normalised: 8c49f8340affa36201c9bf9075dec04dbe517d79b1bb23e4cb1cd67dfcaae576 }
heldTextStan: { method: sha256-stan, raw: c19bcde6392a92c322294fbd4a0d50c50206840eebc546fe98395c3c7e2e9488, normalised: 7f6c0400d46774cc9aea7e608a76909ccac3459e76fac0a3f96517af25ca7605 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2022 revision (fifth edition for Geography)"
awardsCovered: ["bachelor's with honours", "integrated master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document; two terms it defines in passing (geocapabilities, 3.22; reproducibility, 3.27)"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0108 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:32"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Geography (QAA, March 2022)

> Run 0108, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2022-geography-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
An agent reading this document can tell what a Geography honours graduate (and an integrated master's graduate, held to the same table) is expected to know and do at three rungs, threshold, typical and excellent, across knowledge and understanding, subject-specific skills and generic skills; which skills and attributes the subject lists as outcomes; and what the statement asks of courses, above all inclusive, safe, low-carbon fieldwork. Each statement carries the issuer's text, our paraphrase, a practitioner and a student version and two instructions to AI agents, one for writing about the statement and one for using it in dialogue.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
The QAA Geography statement (March 2022, fifth edition) covers single honours degrees and integrated master's degrees in Geography across the four UK nations, at FHEQ Level 6 (FQHEIS Level 10), with the integrated master's at FHEQ Level 7 (FQHEIS Level 11). It states its standards in one flattened table under 4.8 with three columns, threshold, typical and excellent, and 22 rows (8 knowledge and understanding, 7 subject-specific skills, 7 generic skills), summarised in prose at 4.5 to 4.7; four further outcomes that successful graduates should have developed sit above the table. Section 3 lists subject-specific skills, generic intellectual skills, generic skills and personal attributes, most of which graduates are able to show (3.23). Its obligations fall mostly on courses: values and critical theory across the curriculum, fieldwork throughout the degree, and ethics, risk, inclusivity and carbon assessments before taught fieldwork. Themes: equity, equality, diversity and inclusion; accessibility; sustainability (ESD); employability, entrepreneurship and enterprise. Body: the Royal Geographical Society (with IBG). Shared documents: Annex D of the FHEQ, the ESD guidance and the enterprise guidance.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement: Geography"
edition: "March 2022 (fifth edition)"
dates:
  published: 2022-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement; not sector-recognised standards in England, a key reference point in Wales and Scotland, part of quality requirements in Northern Ireland (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2022", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a Geography honours or integrated master's graduate is expected to know, understand and be able to do, and the distinctive features, content and delivery of courses in the subject"
appliesTo:
  awards: ["bachelor's with honours", "integrated master's"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This document is a QAA Subject Benchmark Statement for Geography that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies.\" (D1, front matter)"
statedSubjects:
  - { name: "Geography", locator: "(D1, front matter; 1.1; 3.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100409", label: "geography" }, { scheme: "cah", code: "CAH26-01-01", label: "geography (non-specific)" }] }
  - { name: "BA and BSc degree courses (and MA in Scotland), integrated master's programmes", locator: "(D1, 1.2)", kind: "programme title", codes: [{ scheme: "hecos", code: "100409", label: "geography" }] }
  - { name: "physical and human geography (named as the natural and social sides of the subject, not as titles)", locator: "(D1, 3.3; 4.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100410", label: "physical geography" }, { scheme: "hecos", code: "100478", label: "human geography" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "geography as integrated study of society and environment through scale, place, space and time" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "an established subject with many routes in; BA, BSc, Scottish MA and integrated master's" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Purposes of a Geography degree", gloss: "purposes: holistic thinking across sciences and humanities; STEM and SHAPE; graduates for real challenges" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Geography degree", gloss: "breadth, plural ways of knowing, fieldwork and spatial technologies as defining traits" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "a shared community duty to build equity and inclusion, beyond legal minimums" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "colonial roots of the discipline and the duty to counter their legacies" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "core values of the inclusive community, to run through the whole curriculum" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "critical theory across the discipline; anticipatory design of learning sites" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "supportive settings, working with discomfort, care for wellbeing" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainable development in geography and three ESD principles" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "behaviours and capabilities for civic life, careers and economic change" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "graduates' data skills and their value for enterprise of many kinds" }
  - { number: "2.1", order: 16, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "progressive, aligned course design led by experts with student co-production" }
  - { number: "2.2", order: 17, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "experiential and theoretical design; overarching concepts that bound the subject" }
  - { number: "2.3", order: 18, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "inclusive, equitable design in every part of teaching and assessment" }
  - { number: "2.4", order: 19, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "live experiential learning, blended options and accessible resources" }
  - { number: "2.5", order: 20, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "students seeing themselves in the curriculum; barriers for some groups" }
  - { number: "2.6", order: 21, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "inclusive, affordable fieldwork as a duty on leaders and designers" }
  - { number: "2.7", order: 22, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "breadth first, then specialism, placed within the whole discipline" }
  - { number: "2.8", order: 23, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "growing critical judgement and independence as students progress" }
  - { number: "2.9", order: 24, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "how data collection shapes understanding of the world" }
  - { number: "2.10", order: 25, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "course lengths, exit awards and the Scottish four-year honours degree" }
  - { number: "2.11", order: 26, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexibility as part of an accessible, inclusive course" }
  - { number: "2.12", order: 27, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "what a flexible course accommodates and integrates" }
  - { number: "2.13", order: 28, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "resourcing flexible material; unequal access to technology" }
  - { number: "2.14", order: 29, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "internal and external partnerships and what they give students" }
  - { number: "2.15", order: 30, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "equal access to partnerships; partners share equity duties" }
  - { number: "2.16", order: 31, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "scales and sectors of partnership; student-centred design" }
  - { number: "2.17", order: 32, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "what employers value beyond core geographical skills" }
  - { number: "2.18", order: 33, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "learned societies and Chartered Geographer accreditation" }
  - { number: "2.19", order: 34, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review by degree-awarding bodies" }
  - { number: "2.20", order: 35, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.21", order: 36, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "3.1", order: 38, componentType: paragraph, parent: "section 3", heading: "Content: subject knowledge and understanding", gloss: "single honours courses cover the knowledge areas that follow; others proportionally" }
  - { number: "3.2", order: 39, componentType: area, parent: "section 3", heading: "Content: subject knowledge and understanding", gloss: "what characterises the discipline; four strands of concepts" }
  - { number: "3.3", order: 40, componentType: area, parent: "section 3", heading: "Content: subject knowledge and understanding", gloss: "spatial distributions, change across scales and the effect of scale" }
  - { number: "3.4", order: 41, componentType: area, parent: "section 3", heading: "Content: subject knowledge and understanding", gloss: "how places are made and remade; fieldwork in familiar and unfamiliar places" }
  - { number: "3.5", order: 42, componentType: area, parent: "section 3", heading: "Content: subject knowledge and understanding", gloss: "systems thinking about human and natural worlds" }
  - { number: "3.6", order: 43, componentType: area, parent: "section 3", heading: "Content: subject knowledge and understanding", gloss: "economic, social, cultural, political and environmental patterns; contested scales" }
  - { number: "3.7", order: 44, componentType: area, parent: "section 3", heading: "Content: subject knowledge and understanding", gloss: "drivers of environmental change; energy and matter fluxes" }
  - { number: "3.8", order: 45, componentType: area, parent: "section 3", heading: "Content: subject knowledge and understanding", gloss: "the history of the discipline, colonialism and decolonial practice" }
  - { number: "3.9", order: 46, componentType: area, parent: "section 3", heading: "Content: subject knowledge and understanding", gloss: "representation, mapping and the politics of spatial data" }
  - { number: "3.10", order: 47, componentType: area, parent: "section 3", heading: "Content: subject knowledge and understanding", gloss: "research design, ethics, safety and a range of methodologies" }
  - { number: "3.11", order: 48, componentType: area, parent: "section 3", heading: "Content: subject knowledge and understanding", gloss: "GISci, GIS, remote sensing and statistics" }
  - { number: "3.12", order: 49, componentType: area, parent: "section 3", heading: "Content: subject knowledge and understanding", gloss: "global and local perspectives applied to real problems, with their limits" }
  - { number: "3.13", order: 50, componentType: practice, parent: "section 3", heading: "Fieldwork", gloss: "fieldwork integral to every course" }
  - { number: "3.14", order: 51, componentType: practice, parent: "section 3", heading: "Fieldwork", gloss: "an expansive idea of the field and access to varied fields" }
  - { number: "3.15", order: 52, componentType: practice, parent: "section 3", heading: "Fieldwork", gloss: "fieldwork required throughout the degree and what it develops" }
  - { number: "3.16", order: 53, componentType: practice, parent: "section 3", heading: "Fieldwork", gloss: "collecting and analysing field data; resources needed" }
  - { number: "3.17", order: 54, componentType: practice, parent: "section 3", heading: "Fieldwork", gloss: "virtual fieldwork and its limits" }
  - { number: "3.18", order: 55, componentType: practice, parent: "section 3", heading: "Fieldwork", gloss: "ethical, safe fieldwork; ethics and risk assessments first" }
  - { number: "3.19", order: 56, componentType: practice, parent: "section 3", heading: "Fieldwork", gloss: "inclusive, accessible, fair fieldwork; inclusivity impact assessment" }
  - { number: "3.20", order: 57, componentType: practice, parent: "section 3", heading: "Fieldwork", gloss: "carbon audit and justified destinations" }
  - { number: "3.21", order: 58, componentType: practice, parent: "section 3", heading: "Fieldwork", gloss: "staff training and capacity for fieldwork" }
  - { number: "3.22", order: 59, componentType: paragraph, parent: "section 3", heading: "Skills, attributes and geocapabilities", gloss: "learning through geography; geocapabilities defined" }
  - { number: "3.23", order: 60, componentType: paragraph, parent: "section 3", heading: "Skills, attributes and geocapabilities", gloss: "graduates show competence in most listed skills and attributes" }
  - { number: "3.24", order: 61, componentType: paragraph, parent: "section 3", heading: "Skills, attributes and geocapabilities", gloss: "principles for building skills alongside knowledge" }
  - { number: "3.25", order: 62, componentType: paragraph, parent: "section 3", heading: "Subject-specific skills", gloss: "intellectual skills and working across disciplines" }
  - { number: "3.26", order: 63, componentType: paragraph, parent: "section 3", heading: "Subject-specific skills", gloss: "evidence, mixed analysis and choice of scale" }
  - { number: "3.27", order: 64, componentType: paragraph, parent: "section 3", heading: "Subject-specific skills", gloss: "techniques, data ethics and reproducibility" }
  - { number: "3.28", order: 65, componentType: paragraph, parent: "section 3", heading: "Subject-specific skills", gloss: "graduates' research and data skills and their wider value" }
  - { number: "3.29", order: 66, componentType: paragraph, parent: "section 3", heading: "Subject-specific skills", gloss: "resources for spatial data; critical spatial data science" }
  - { number: "3.30", order: 67, componentType: stem, parent: "section 3", heading: "Subject-specific skills", gloss: "list: subject-specific skills" }
  - { number: "3.31", order: 68, componentType: paragraph, parent: "section 3", heading: "Generic skills and personal attributes", gloss: "lead-in to generic skills and attributes" }
  - { number: "3.32", order: 69, componentType: stem, parent: "section 3", heading: "Generic skills and personal attributes", gloss: "list: generic intellectual skills" }
  - { number: "3.33", order: 70, componentType: stem, parent: "section 3", heading: "Generic skills and personal attributes", gloss: "list: generic skills" }
  - { number: "3.34", order: 71, componentType: stem, parent: "section 3", heading: "Generic skills and personal attributes", gloss: "list: personal attributes" }
  - { number: "3.35", order: 72, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "innovative and changing teaching contexts" }
  - { number: "3.36", order: 73, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "the range of teaching approaches courses use" }
  - { number: "3.37", order: 74, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "roles of fieldwork and experiential learning" }
  - { number: "3.38", order: 75, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "independent research throughout the degree, often a dissertation" }
  - { number: "3.39", order: 76, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "a wide mix of teaching and learning styles" }
  - { number: "3.40", order: 77, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "an assessment and feedback strategy" }
  - { number: "3.41", order: 78, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment methods students are likely to meet" }
  - { number: "4.1", order: 80, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the threshold as the minimum for honours" }
  - { number: "4.2", order: 81, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed the threshold; refer to Annex D" }
  - { number: "4.3", order: 82, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "areas of achievement: knowledge and three kinds of skill" }
  - { number: "4.4", order: 83, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the table covers honours and integrated master's; not prescriptive" }
  - { number: "4.5", order: 84, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the threshold graduate in summary" }
  - { number: "4.6", order: 85, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the typical graduate in summary" }
  - { number: "4.7", order: 86, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the excellent graduate in summary" }
  - { number: "4.8", order: 87, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "four outcomes for successful graduates, then the rung table" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Geography degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Geography degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and S8" }
  - { number: "section headings 1 to 4", heading: "section heading lines", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for S7, SB5 and SB6" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for Geography", kind: "other: back matter, read for S8 (edition history)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 138 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/geography-2022/1.5
  locator: { number: "1.5", headingPath: ["Context and purposes of a Geography degree", "Equity, equality, diversity and inclusion"] }
  span: { start: 12104, end: 13162 }
  source: "1.5 Geography, as an inclusive learning community, has a collective responsibility to embed equity, equality, diversity and inclusion within all institutions, processes, curricula, and pedagogies. This responsibility to go beyond the minimum expectations of equality ensures an equitable community that recognises learners' difference in prior experience and opportunity and can help to remedy systemic disadvantages in the subject, for example: through widening participation agendas to ensure economic disadvantage does not hinder a student's access, experience or outcome; countering the under-representation of marginalised groups inclusive of, and beyond, those with protected characteristics as defined by the Equality Act 2010; adopting a zero-tolerance approach to discrimination and harassment, including everyday microaggressions; anticipating access for neurodiverse community members; and closing structural awarding gaps. All participants in the community will need to engage, reflect and change in order to uphold this responsibility and duty.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "everyone in the geography learning community"
  addressee: both
  verbs: ["engage", "reflect", "change"]
  about: "a shared duty to embed equity and inclusion"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The subject community has a shared duty, going past legal minimums, to build equity, equality, diversity and inclusion into its institutions, curricula and teaching, for example by widening participation, countering under-representation, refusing discrimination and closing awarding gaps; everyone in it will need to engage, reflect and change to meet that duty."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/1.6
  locator: { number: "1.6", headingPath: ["Context and purposes of a Geography degree", "Equity, equality, diversity and inclusion"] }
  span: { start: 13162, end: 13842 }
  source: "1.6 Contemporary geography draws from knowledge traditions formed through colonial enlightenment science. Geographical concepts and techniques contributed to the overseas expansion of British and European empires, which was justified using narratives of white, able and heteronormative superiority. Colonial and imperial geographies, and their contemporary legacies of systemic disadvantage, for example, racism, classism, ablism, homophobia and patriarchy, must therefore be acknowledged and countered by fostering an inclusive learning community encompassing a range of participants, such as students, academics, technicians, professional staff, visitors and external partners.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the geography learning community"
  addressee: both
  verbs: ["acknowledged", "countered"]
  about: "acknowledging and countering colonial legacies"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Because the discipline's knowledge grew partly out of colonial science that helped justify empire, its colonial and imperial legacies of systemic disadvantage, such as racism, classism, ableism, homophobia and patriarchy, must be acknowledged and countered through a learning community that includes everyone involved."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/1.7
  locator: { number: "1.7", headingPath: ["Context and purposes of a Geography degree", "Equity, equality, diversity and inclusion"] }
  span: { start: 13842, end: 14517 }
  source: "1.7 The following core values underpin geography's inclusive learning community: an ethics of care towards inhabitants and environments embracing and valuing plurality of knowledges and experiences; respect for alternative perspectives and lifestyles; attentiveness to the opportunities and challenges raised by decolonial imperatives; and solidarity in recognising and addressing injustice. These values should be integrated throughout the curriculum and not be siloed within individual modules and/or sub-disciplines. This will enhance the contribution that studying geography can make to realising transformative justice across our human, biodiverse and geodiverse world.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the geography curriculum"
  addressee: provider
  verbs: ["integrated"]
  about: "core values across the whole curriculum"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The inclusive community rests on care for people and places, respect for other views and ways of life, attention to decolonial demands and solidarity against injustice; these values should run through the whole curriculum rather than sit in single modules or sub-fields."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/1.8
  locator: { number: "1.8", headingPath: ["Context and purposes of a Geography degree", "Equity, equality, diversity and inclusion"] }
  span: { start: 14517, end: 15388 }
  source: "1.8 The core values underpinning geography's inclusive learning community aligns with, and encourages, curricula design principles that stimulate critical thinking informed by a variety of progressive theoretical perspectives. These include, but are not limited to, theoretical perspectives from critical theory, critical race theory, decoloniality , disability studies, feminist, queer, and science and technology studies. The application of critical theory is relevant to, and should be applied across, the geographical discipline. The core values also promote anticipatory design and practices, which are considerate of the particularities associated with sites of learning, for example, online, face-to-face, in the field or in the laboratory, paying close attention to those that may have historically been less inclusive, such as fieldwork sites and laboratori es.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the geography curriculum"
  addressee: provider
  verbs: ["applied"]
  about: "critical theory across the discipline"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The core values favour curricula that build critical thinking from progressive theory, among them critical race theory, decoloniality, disability, feminist and queer studies and science and technology studies; critical theory should be applied across geography, and the values also favour design that anticipates the barriers of each learning site, fieldwork and laboratories above all."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of a Geography degree", "Entrepreneurship and enterprise education"] }
  span: { start: 18609, end: 19878 }
  source: "1.12 Geography graduates are able to collect, analyse and manipulate a range of quantitative and qualitative data. Their approach to spatial analytics is distinctive, and highly valued in the private, public and third sectors, because of their ability to transcend scales and integrate knowledge and geocapabilities across multiple disciplines, not only in the natural and social sciences, but also in the humanities and arts. Consequently, Geography graduates use their geospatial awareness and practical experience to understand and solve complex societal and economic challenges, and know how to gather and evaluate evidence to inform innovation and decision-making. Geography graduates also understand the intrinsic value of a range of alternative economies and entrepreneurial approaches, including, but not limited to, green entrepreneurship, social entrepreneurship and digital entrepreneurship. As such, enterprise and entrepreneurship education in geography encompasses and goes beyond facilitating the creation of surplus economic value through an allied focus on social, cultural and environmental value. A deeper generic analysis can be\n\n6\nfound in the QAA document, Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers.\n\n7\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["collect", "analyse", "manipulate", "solve", "gather", "evaluate"]
  about: "data skills for innovation and enterprise"
  themes: [theme:enterprise]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will be able to gather, analyse and handle varied numerical and qualitative data; their spatial analysis, crossing scales and disciplines, lets them tackle complex social and economic problems and use evidence for innovation and decisions, and they see the worth of alternative economies and of green, social and digital entrepreneurship."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of a Geography degree", "Design"] }
  span: { start: 19930, end: 20442 }
  source: "2.1 Geography degrees are designed to give students an integrative education in the discipline of geography. Courses should be built on progressively more complex learning outcomes which are aligned with teaching methods and assessment. Course design is led by experts and practitioners of the discipline, while also acknowledging the role of student engagement and co-production in evolving and reflective course design. Geography courses in the UK increasingly utilise mechanisms for student-centred learning.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Geography courses"
  addressee: provider
  verbs: ["built"]
  about: "progressive, aligned course design"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Geography degrees aim at an integrative education; courses should rest on learning outcomes that grow in complexity and match teaching and assessment, with design led by subject experts and shaped by student engagement and co-creation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of a Geography degree", "Accessibility"] }
  span: { start: 22103, end: 22899 }
  source: "2.6 Geographers employ an expansive understanding of the field and require access to a variety of types of fields for fieldwork. While fieldwork is an essential part of the discipline, an awareness of the individual needs of the student body during fieldwork should also be recognised. Leaders and coordinators of fieldwork are responsible for implementing anticipatory design to ensure field spaces are not exclusionary on the basis of all protected characteristics, class, gender identity and neurodiversity, and that sufficient facilities and resources exist for all individuals present. Equally, course designers need to take care to ensure learning experiences are not prohibitive on the basis of additional costs associated with fieldwork and specialist clothing and equipment. Progression\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "fieldwork leaders and course designers"
  addressee: provider
  verbs: ["recognised", "implementing", "ensure"]
  about: "inclusive and affordable fieldwork"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Fieldwork needs access to many kinds of field; essential as it is, students' individual needs during fieldwork should be recognised, fieldwork leaders are responsible for anticipatory design so that no field site excludes anyone on any protected characteristic, class, gender identity or neurodiversity and facilities suffice, and designers need to stop the extra costs of travel, clothing and kit from barring anyone."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of a Geography degree", "Progression"] }
  span: { start: 22899, end: 23707 }
  source: "2.7 Progression within higher-level study of a subject such as geography is likely to involve some measure of specialisation. In the initial stages of a degree course, students achieve a basic knowledge and understanding of a range of different approaches across the breadth of the subject. Thereafter, progression and specialisation in a particular branch of the discipline informs critical reflection about both the subject's diversity and its unifying themes. By the end of a course, students are able to situate their chosen specialisms within\n\n8\na wider understanding of geography, its approach, history and theoretical underpinnings. Given the emphasis on diversity of programmes, it is important that potential students are fully informed of the particular nature and strengths of individual courses.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students at the end of the course"
  addressee: learner
  verbs: ["situate"]
  about: "placing a specialism within the wider discipline"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Study grows more specialised as the degree goes on, after a broad first grounding; by the end, students will be able to place their chosen specialisms within a wider grasp of geography, its approach, history and theory, and applicants need clear information on what each course offers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of a Geography degree", "Progression"] }
  span: { start: 23707, end: 24167 }
  source: "2.8 As students progress, they are able to evaluate evidence and knowledge critically and make value judgements about the sources of information with increasing sophistication. Students will have opportunities to demonstrate increasing levels of critical reflection and understanding as they progress through their studies. They will also demonstrate an increasing ability to undertake fieldwork or projects independently, using primary and/or secondary data.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students as they progress"
  addressee: learner
  verbs: ["evaluate", "make", "demonstrate", "undertake"]
  about: "growing critical judgement and independence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As they progress, students are able to judge evidence and the value of their sources with growing sophistication; they will have chances to show deeper critical reflection and will show a growing capacity to carry out fieldwork or projects on their own with primary or secondary data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of a Geography degree", "Progression"] }
  span: { start: 24167, end: 24549 }
  source: "2.9 As they progress, students should develop an increased understanding of the impacts of the epistemology of primary data collection, and its impacts on the ontological understanding we have of the world. Thus, they should have opportunities to develop an increased understanding of the nature of data as it pertains to the real world, and geographic knowledge as outlined below.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students as they progress, and their courses"
  addressee: both
  verbs: ["develop"]
  about: "how collecting data shapes knowledge of the world"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As they progress, students should come to understand more fully how the epistemology of collecting primary data affects what we take the world to be, and should have chances to grasp better how data relate to the real world and to geographical knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/2.13
  locator: { number: "2.13", headingPath: ["Distinctive features of a Geography degree", "Flexibility"] }
  span: { start: 25995, end: 26307 }
  source: "2.13 The provision of accessible, inclusive and flexible material requires additional resources to ensure high-quality content and delivery. The design should also reflect diversity in students' access to technology, ensuring that the flexibility of design does not lead to unintended consequences. Partnerships\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course design and resourcing"
  addressee: provider
  verbs: ["reflect", "ensuring"]
  about: "resourcing flexible material and unequal access to technology"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Accessible, inclusive and flexible material needs extra resources to keep quality high, and design should allow for students' unequal access to technology so that flexibility does not cause harm nobody planned."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/2.15
  locator: { number: "2.15", headingPath: ["Distinctive features of a Geography degree", "Partnerships"] }
  span: { start: 26861, end: 27567 }
  source: "2.15 Institutions should ensure that equality of experience is given to all students in their ability to engage in partnerships, where appropriate. The facilitation of partnerships within institutions, such as student societies or interdepartmental working, are of equal value, giving students the opportunity to communicate, build networks and understand the context in which geography as a discipline operates. Partners become part of the geography learning community and have the responsibility to attend to the same principles of equity, equality, diversity and inclusion in their interactions. Partners offer important opportunities to enhance the learning community's engagement with equity agendas.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "institutions"
  addressee: provider
  verbs: ["ensure"]
  about: "equal access to partnerships"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Institutions should make sure every student has an equal chance to take part in partnerships where relevant; partnerships inside the institution, such as societies and work across departments, count as much as external ones, and partners take on the same equity duties."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/2.16
  locator: { number: "2.16", headingPath: ["Distinctive features of a Geography degree", "Partnerships"] }
  span: { start: 27567, end: 27969 }
  source: "2.16 Partnership activities can be at a variety of scales and sectors, for example cross- disciplinary, cross-institutional, non-governmental organisations, industry, research, private and public. The activities may range from short-term activities to a long-term relationship and should be designed to be student centred and to support the understanding of the subject beyond the academic experience.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "partnership activities"
  addressee: provider
  verbs: ["designed"]
  about: "student-centred partnership activities"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Partnerships may cross disciplines, institutions and sectors and may be brief or lasting; they should be designed around students and help them understand the subject beyond their studies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/2.20
  locator: { number: "2.20", headingPath: ["Distinctive features of a Geography degree", "Monitoring and review"] }
  span: { start: 29526, end: 29838 }
  source: "2.20 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "providers in periodic review"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Externality is essential to UK quality assurance; providers will use external reviewers in periodic review to get an outside view of proposed changes and to check that threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Content: subject knowledge and understanding"] }
  span: { start: 32255, end: 32958 }
  source: "3.3 Geography graduates are able to demonstrate knowledge and explanations of spatial distributions in both physical and human phenomena. Geographers understand the dynamics and rates of change at different temporal and spatial scales and can evaluate the processes shaping the geographies of the past, present and future. Geographers have a critical awareness of the significance of spatial and temporal scale for natural processes, human processes and their interactions and analysis. They comprehend how such processes operate across local, regional and global scales to produce particular geographies. They are also aware of how the scale of study can impact upon the conclusions that may be drawn.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "evaluate"]
  about: "spatial distributions and change across scales"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will be able to show knowledge and explanation of how physical and human phenomena are distributed in space; they grasp change at different scales of time and space, judge the processes shaping past, present and future geographies, and see how the chosen scale affects conclusions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.5
  locator: { number: "3.5", headingPath: ["Content, structure and delivery", "Content: subject knowledge and understanding"] }
  span: { start: 33717, end: 34094 }
  source: "3.5 Geographers are able to use a systems framework to critically conceptualise patterns, processes, interactions and change in the context of a human, biodiverse and geodiverse world. This acknowledges environmental impacts on human activity; human impacts on biophysical systems and on components of the climate system; and the management of environments and landscapes.\n\n11\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["use", "conceptualise"]
  about: "systems thinking about human and natural worlds"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will be able to use systems thinking to frame patterns, processes, interactions and change critically in a world of people, biodiversity and geodiversity, taking in environmental effects on people, human effects on natural and climate systems, and environmental management."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Fieldwork"] }
  span: { start: 41206, end: 42381 }
  source: "3.15 Fieldwork encompasses directed learning, peer-assisted learning and self-directed student learning and requires extended and in-depth time in the field, including multi-day trips and residential trips. Fieldwork is required throughout a Geography degree to enable progression in core skills and capabilities, often resulting in self-directed fieldwork by the end of a Geography degree. Fieldwork provides geographers with a unique opportunity for experiential learning; teamwork; problem-based learning; research design, planning and implementation; data collection, management and analysis; resilience, flexibility and coping with uncertainty and unfamiliar situations; and understanding and managing risks. It is a key means of delivery for specific skills that cannot readily be obtained in the classroom. Fieldwork also helps hone skills in group work, planning, sampling, research design and problem-solving. Finally, as nearly all data are spatial (they are collected somewhere), only fieldwork gives students experience and critical understanding of the link between the real world and measurement as captured in spatial data and place-based representations.\n\n13\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Geography degrees and their students"
  addressee: both
  verbs: ["required"]
  about: "fieldwork through the whole degree"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Fieldwork, mixing directed, peer and self-directed learning with extended time in the field including multi-day and residential trips, is required across the whole degree so that core skills can progress, often ending in self-directed fieldwork; it builds teamwork, problem-based learning, research design, data handling, resilience and the handling of risk, and it alone links the real world to its measurement in spatial data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.18
  locator: { number: "3.18", headingPath: ["Content, structure and delivery", "Fieldwork"] }
  span: { start: 43344, end: 43774 }
  source: "3.18 Fieldwork is an opportunity to reflect on sensibilities, such as the positionalities, responsibilities and relationalities of students and staff. Consequently, all fieldwork should be planned and conducted in a way that is ethical, responsible, careful and safe, for students, staff, visited communities and all other stakeholders. An ethics assessment and risk assessment should be undertaken prior to all taught fieldwork.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who plan and run taught fieldwork"
  addressee: provider
  verbs: ["planned", "conducted", "undertaken"]
  about: "ethics and risk assessment before fieldwork"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Fieldwork invites reflection on positionality, responsibility and relationships, so all fieldwork should be planned and run ethically, responsibly, carefully and safely for everyone involved, with an ethics assessment and a risk assessment before any taught fieldwork."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/3.19
  locator: { number: "3.19", headingPath: ["Content, structure and delivery", "Fieldwork"] }
  span: { start: 43774, end: 44303 }
  source: "3.19 Fieldwork should be planned and conducted in such a way as to be inclusive and accessible, considering the well-being of students and staff, including their mental and physical health, and all other protected characteristics. Fieldwork opportunities should be fair and providers, to the extent possible, should consider the resourcing needed to overcome costs and other barriers that might impact a student's ability to participate fully. An inclusivity impact assessment should be undertaken prior to all taught fieldwork.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who plan fieldwork, and providers"
  addressee: provider
  verbs: ["planned", "conducted", "consider", "undertaken"]
  about: "inclusive, accessible and fair fieldwork"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Fieldwork should be planned and run to be inclusive and accessible, minding students' and staff's wellbeing and all protected characteristics; opportunities should be fair, providers should, as far as they can, fund their way round cost and other barriers, and an inclusivity impact assessment should come before all taught fieldwork."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/3.20
  locator: { number: "3.20", headingPath: ["Content, structure and delivery", "Fieldwork"] }
  span: { start: 44303, end: 44858 }
  source: "3.20 The environmental impact of fieldwork, its sustainability and its carbon footprint should be considered by conducting a carbon audit prior to all taught fieldwork. The choice of destination(s) visited and the mode of transport should be clearly justified by the programme learning outcomes. This justification should balance the environmental costs involved with the geographical learning, transferable skills, development of social and cultural capital and other educational benefits derived by learning experientially within specific environments.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who plan taught fieldwork"
  addressee: provider
  verbs: ["considered", "justified", "balance"]
  about: "carbon audit and justified destinations"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The environmental impact and carbon footprint of fieldwork should be weighed through a carbon audit before all taught fieldwork; destinations and transport should be justified by programme outcomes, setting environmental cost against the learning and other gains of studying in a place."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/3.21
  locator: { number: "3.21", headingPath: ["Content, structure and delivery", "Fieldwork"] }
  span: { start: 44858, end: 45231 }
  source: "3.21 Staff take on significant responsibilities in delivering taught fieldwork. Appropriate resourcing by the provider should ensure that staff are fully trained and supported to deliver high-quality field learning. Employers must also recognise that staff have differing capacities to lead and/or participate in geography fieldwork. Skills, attributes and geocapabilities\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the provider as employer of fieldwork staff"
  addressee: provider
  verbs: ["ensure", "recognise"]
  about: "training and capacity of fieldwork staff"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Staff carry heavy responsibility in taught fieldwork; the provider's resourcing should make sure they are fully trained and supported, and employers must recognise that staff differ in their capacity to lead or join fieldwork."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/3.26
  locator: { number: "3.26", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 47966, end: 48293 }
  source: "3.26 Geographers use a variety of sources of evidence and are able to apply appropriate forms of both quantitative and qualitative analysis, making informed judgements based on the evidence available. Geographers are numerate and able to establish the appropriate spatial and temporal scales for the purpose of their analysis.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["use", "apply", "making", "establish"]
  about: "mixed analysis of evidence and choice of scale"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will be able to draw on varied evidence and apply suitable quantitative and qualitative analysis, judging soundly from what the evidence shows; they are numerate and can set the right space and time scales for their analysis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.30.b1
  locator: { number: "3.30.b1", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 50344, end: 50377 }
  source: "spatial awareness and observation"
  stem: "3.30"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "spatial awareness and observation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show spatial awareness and careful observation, one of the subject-specific skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.30.b2
  locator: { number: "3.30.b2", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 50380, end: 50476 }
  source: "recognising the moral, ethical and safety issues involved in all aspects of geographical enquiry"
  stem: "3.30"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["recognising"]
  about: "ethics and safety in enquiry"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show the ability to spot the moral, ethical and safety questions in every part of geographical enquiry, one of the subject-specific skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.30.b3
  locator: { number: "3.30.b3", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 50479, end: 50557 }
  source: "conducting fieldwork and data collection, assessing risks and their mitigation"
  stem: "3.30"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["conducting", "assessing"]
  about: "fieldwork, data collection and risk"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show skill in carrying out fieldwork and collecting data while judging risks and how to reduce them, one of the subject-specific skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.30.b4
  locator: { number: "3.30.b4", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 50560, end: 50690 }
  source: "employing a variety of interpretative methods, for example, participant observation, ethnographic interviews, and auto-ethnography"
  stem: "3.30"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["employing"]
  about: "interpretative methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show skill with interpretative methods such as participant observation, ethnographic interviews and auto-ethnography, one of the subject-specific skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.30.b5
  locator: { number: "3.30.b5", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 50693, end: 50804 }
  source: "employing a variety of social survey methods, for example, questionnaire surveys and semi-structured interviews"
  stem: "3.30"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["employing"]
  about: "social survey methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show skill with social survey methods such as questionnaires and semi-structured interviews, one of the subject-specific skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.30.b6
  locator: { number: "3.30.b6", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 50807, end: 50938 }
  source: "employing a variety of science laboratory skills and methods, for example, soil, water and sediment sample preparation and analysis"
  stem: "3.30"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["employing"]
  about: "laboratory skills and methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show laboratory skills such as preparing and analysing soil, water and sediment samples, one of the subject-specific skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.30.b7
  locator: { number: "3.30.b7", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 50941, end: 51061 }
  source: "primary data generation, collection and recording, and the use of secondary data sets, both quantitative and qualitative"
  stem: "3.30"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "primary and secondary data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show skill in generating, collecting and recording primary data and using secondary data sets, numerical and qualitative, one of the subject-specific skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.30.b8
  locator: { number: "3.30.b8", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 51064, end: 51255 }
  source: "critically evaluating, interpreting and combining different types of geographical evidence, for example, texts, visual and material culture, archival data, maps, digitised and laboratory data"
  stem: "3.30"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["evaluating", "interpreting", "combining"]
  about: "evaluating and combining kinds of evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show critical judgement, interpretation and combination of kinds of geographical evidence, from texts and archives to maps and laboratory data, one of the subject-specific skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.30.b9
  locator: { number: "3.30.b9", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 51258, end: 51331 }
  source: "analysis and problem-solving through quantitative and qualitative methods"
  stem: "3.30"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "analysis and problem-solving"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show analysis and problem-solving with numerical and qualitative methods, one of the subject-specific skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.30.b10
  locator: { number: "3.30.b10", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 51334, end: 51506 }
  source: "applying methods for the collection and analysis of spatial and environmental information, for example, by using GIS, remote sensing, statistical and mathematical modelling"
  stem: "3.30"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["applying", "using"]
  about: "spatial and environmental information methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show collecting and analysing spatial and environmental information with tools such as GIS, remote sensing and statistical or mathematical models, one of the subject-specific skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.30.b11
  locator: { number: "3.30.b11", headingPath: ["Content, structure and delivery", "Subject-specific skills"] }
  span: { start: 51509, end: 51602 }
  source: "preparing effective maps, diagrams and visualisations. Generic skills and personal attributes"
  stem: "3.30"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["preparing"]
  about: "maps, diagrams and visualisations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show skill in making clear, effective maps, diagrams and visualisations, one of the subject-specific skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.32.b1
  locator: { number: "3.32.b1", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 51769, end: 51830 }
  source: "assessing the merits of contrasting theories and explanations"
  stem: "3.32"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["assessing"]
  about: "weighing contrasting theories"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show skill in weighing up contrasting theories and explanations, one of the generic intellectual skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.32.b2
  locator: { number: "3.32.b2", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 51833, end: 52064 }
  source: "an awareness of the social, cultural and political context in which knowledge is produced (epistemological hegemonies), the positionalities of the researcher and the researched alike, and the democratisation of knowledge production"
  stem: "3.32"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "the politics and positionality of knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show awareness of the social, cultural and political settings in which knowledge is made, of the positions of researcher and researched, and of widening who makes knowledge, one of the generic intellectual skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.32.b3
  locator: { number: "3.32.b3", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52068, end: 52134 }
  source: "understanding the appropriate and ethical use of evidence and data"
  stem: "3.32"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["understanding"]
  about: "ethical use of evidence and data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show an understanding of how to use evidence and data properly and ethically, one of the generic intellectual skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.32.b4
  locator: { number: "3.32.b4", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52137, end: 52288 }
  source: "planning, designing and executing a piece of rigorous research or enquiry, both independently and in groups, including the production of a final report"
  stem: "3.32"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["planning", "designing", "executing"]
  about: "planning and carrying out research"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show skill in planning, designing and carrying out rigorous research alone and in groups, through to a final report, one of the generic intellectual skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.32.b5
  locator: { number: "3.32.b5", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52292, end: 52325 }
  source: "numeracy and statistical literacy"
  stem: "3.32"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "numeracy and statistical literacy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show numeracy and statistical literacy, one of the generic intellectual skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.32.b6
  locator: { number: "3.32.b6", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52328, end: 52368 }
  source: "abstraction and synthesis of information"
  stem: "3.32"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "abstraction and synthesis"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show skill in abstracting and synthesising information, one of the generic intellectual skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.32.b7
  locator: { number: "3.32.b7", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52371, end: 52401 }
  source: "developing a reasoned argument"
  stem: "3.32"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["developing"]
  about: "reasoned argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show skill in building a reasoned argument, one of the generic intellectual skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.32.b8
  locator: { number: "3.32.b8", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52404, end: 52473 }
  source: "taking responsibility for learning and reflection upon that learning."
  stem: "3.32"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["taking"]
  about: "responsibility for and reflection on learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show responsibility for learning and reflection on that learning, one of the generic intellectual skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.33.b1
  locator: { number: "3.33.b1", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52505, end: 52576 }
  source: "learning and studying, developing autonomous learning and metacognition"
  stem: "3.33"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["developing"]
  about: "study, autonomy and metacognition"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show effective study, autonomous learning and awareness of how learning works, one of the generic skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.33.b2
  locator: { number: "3.33.b2", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52579, end: 52634 }
  source: "decision-making, time management and prioritising tasks"
  stem: "3.33"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["prioritising"]
  about: "decisions, time and priorities"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show decision-making, time management and setting priorities among tasks, one of the generic skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.33.b3
  locator: { number: "3.33.b3", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52637, end: 52665 }
  source: "record-keeping and archiving"
  stem: "3.33"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "record-keeping and archiving"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show skill in keeping and archiving records, one of the generic skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.33.b4
  locator: { number: "3.33.b4", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52668, end: 52782 }
  source: "synthesising, contextualising and critically evaluating information of different styles and from different sources"
  stem: "3.33"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["synthesising", "contextualising", "evaluating"]
  about: "synthesising and evaluating information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show skill in synthesising, placing in context and critically judging information of varied styles and sources, one of the generic skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.33.b5
  locator: { number: "3.33.b5", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52785, end: 52826 }
  source: "oral, written and graphical communication"
  stem: "3.33"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "oral, written and graphical communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show communication in speech, writing and graphics, one of the generic skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.33.b6
  locator: { number: "3.33.b6", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52829, end: 52874 }
  source: "retrieval, handling and archiving of datasets"
  stem: "3.33"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "retrieving and handling datasets"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show skill in finding, handling and archiving datasets, one of the generic skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.33.b7
  locator: { number: "3.33.b7", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52881, end: 52939 }
  source: "an understanding of intellectual property and data privacy"
  stem: "3.33"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "intellectual property and data privacy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show an understanding of intellectual property and data privacy, one of the generic skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.33.b8
  locator: { number: "3.33.b8", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 52942, end: 53030 }
  source: "communication with a variety of audiences, employing formats appropriate to the audience"
  stem: "3.33"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["employing"]
  about: "communicating to varied audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show communication with varied audiences in formats that suit them, one of the generic skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.33.b9
  locator: { number: "3.33.b9", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 53033, end: 53126 }
  source: "the ability to work in groups and teams and to recognise and respect the viewpoints of others"
  stem: "3.33"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["work", "recognise", "respect"]
  about: "group work and respect for others"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show teamwork in groups while recognising and respecting others' viewpoints, one of the generic skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.33.b10
  locator: { number: "3.33.b10", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 53129, end: 53188 }
  source: "the ability to take creative approaches to problem-solving."
  stem: "3.33"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["take"]
  about: "creative problem-solving"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show creative approaches to solving problems, one of the generic skills listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.34.b1
  locator: { number: "3.34.b1", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 53225, end: 53235 }
  source: "motivation"
  stem: "3.34"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "motivation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show the attribute of motivation, one of the personal attributes listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.34.b2
  locator: { number: "3.34.b2", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 53238, end: 53248 }
  source: "innovation"
  stem: "3.34"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "innovation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show the attribute of innovation, one of the personal attributes listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.34.b3
  locator: { number: "3.34.b3", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 53251, end: 53269 }
  source: "entrepreneurialism"
  stem: "3.34"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "entrepreneurialism"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show an entrepreneurial outlook, one of the personal attributes listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.34.b4
  locator: { number: "3.34.b4", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 53272, end: 53329 }
  source: "ability to work responsibly, autonomously and with others"
  stem: "3.34"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["work"]
  about: "responsible, autonomous and shared work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show the ability to work responsibly, on your own and with others, one of the personal attributes listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.34.b5
  locator: { number: "3.34.b5", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 53332, end: 53407 }
  source: "self-awareness, reflection, resilience, self-management and self-confidence"
  stem: "3.34"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "self-awareness and resilience"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show self-awareness, reflection, resilience, self-management and confidence in yourself, one of the personal attributes listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.34.b6
  locator: { number: "3.34.b6", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 53410, end: 53429 }
  source: "empathy and insight"
  stem: "3.34"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "empathy and insight"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show the attribute of empathy and insight, one of the personal attributes listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.34.b7
  locator: { number: "3.34.b7", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 53432, end: 53476 }
  source: "intellectual integrity and ethical behaviour"
  stem: "3.34"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "integrity and ethical behaviour"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show intellectual integrity and ethical conduct, one of the personal attributes listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.34.b8
  locator: { number: "3.34.b8", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 53479, end: 53579 }
  source: "awareness of responsibility as a local, national and international citizen with a global perspective"
  stem: "3.34"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "responsible global citizenship"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show a sense of responsibility as a citizen at local, national and international scale, with a global outlook, one of the personal attributes listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.34.b9
  locator: { number: "3.34.b9", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 53582, end: 53623 }
  source: "the skills to engage in lifelong learning"
  stem: "3.34"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["engage"]
  about: "lifelong learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show the skills to keep learning throughout life, one of the personal attributes listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.34.b10
  locator: { number: "3.34.b10", headingPath: ["Content, structure and delivery", "Generic skills and personal attributes"] }
  span: { start: 53626, end: 53677 }
  source: "flexibility and adaptability. Teaching and learning"
  stem: "3.34"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "flexibility and adaptability"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show the attribute of flexibility and adaptability, one of the personal attributes listed, most of which graduates are able to show."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/3.39
  locator: { number: "3.39", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 56377, end: 56904 }
  source: "3.39 The balance within a degree course of these teaching and learning styles and of the associated assessment methods will clearly vary from one higher education provider to another, consistent with the overall mission, aims and objectives of both the provider and the course. However, honours degree courses in Geography will characteristically have recourse to a wide range of learning and teaching styles, as befits the intellectual heritage of a discipline whose concerns are with both environment and society. Assessment\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "honours degree courses in Geography"
  addressee: provider
  verbs: ["vary", "have"]
  about: "a wide range of teaching and learning styles"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The mix of teaching, learning and assessment differs between providers with their missions and aims, but geography honours courses will typically use a wide range of learning and teaching styles, fitting a subject that spans environment and society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/3.40
  locator: { number: "3.40", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 56904, end: 58003 }
  source: "3.40 An assessment and feedback for learning strategy will allow all students to demonstrate their level of attainment, and reflect upon and discuss their progress. For each method of assessment, the aims, requirements and marking criteria are clearly defined and aligned, allowing appropriate progression throughout the degree course. Such a strategy reflects the variety of abilities and skills developed within the curriculum, the types of teaching methods and learning contexts used, and the learning outcomes of the degree course. Moreover, it recognises the value of formative assessment for promoting deep reflective learning. Students are given opportunities to take part in self-assessment and peer review, authentic assessments, and to work individually and in groups. Students are encouraged to demonstrate their full range of abilities, with providers offering a mix of assessment methods that are accessible to students from varying educational backgrounds and in different learning situations, in some cases offering a choice of assessment formats and authentic public-facing outputs.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "the course's assessment and feedback strategy"
  addressee: provider
  verbs: ["allow", "demonstrate", "reflect", "discuss"]
  about: "an assessment and feedback strategy for every student"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "An assessment and feedback strategy will let every student show what they have attained and reflect on and talk about their progress; each method has clear, aligned aims, requirements and criteria, formative work, self and peer review and authentic tasks are valued, and a mix of accessible methods is offered, sometimes with a choice of format."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/4.1
  locator: { number: "4.1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58815, end: 59148 }
  source: "4.1 This Subject Benchmark Statement sets out the minimum threshold standards that a student will have demonstrated when they are awarded an honours degree in Geography. Demonstrating these standards over time will show that a student has achieved the range of knowledge, understanding and skills expected of graduates in Geography.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students awarded honours in Geography"
  addressee: learner
  verbs: ["demonstrated"]
  about: "the threshold as the minimum for honours"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The section sets out the minimum threshold that a student will have shown on being awarded honours in Geography; meeting these standards over time shows they have the knowledge, understanding and skills expected of graduates."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 59148, end: 59632 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "each higher education provider"
  addressee: provider
  verbs: ["perform", "refer"]
  about: "Annex D for performance above the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do far better than the minimum; each provider decides what evidence shows this and should refer to Annex D, which describes the four honours classes, first, upper second, lower second and third, at FHEQ Level 6 (FQHEIS Level 10)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/geography-2022/4.5
  locator: { number: "4.5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60467, end: 60960 }
  source: "4.5 Threshold graduates possess a basic knowledge and understanding of change within human and physical environments, of interrelationships between these environments, of sustainability and sustainable development, and of the interdependence of places at various scales. Their view of the subject and its methodologies is strongly influenced by formal teaching and has a limited critical perspective. Competence in essential subject- specific, intellectual and generic skills is demonstrated.\n"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates"
  addressee: learner
  verbs: ["possess", "demonstrated"]
  about: "the threshold graduate in summary"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "A threshold graduate has basic knowledge of change in human and physical environments, of the links between them, of sustainability and of how places at different scales depend on each other; their view leans on formal teaching with limited criticality, and they show competence in the essential subject, intellectual and generic skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.6
  locator: { number: "4.6", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60960, end: 61419 }
  source: "4.6 Typical graduates display a critical awareness of the scope and methodologies of the subject, based on a solid foundation of knowledge, consistently demonstrating a command of appropriate subject-specific and generic skills as well as proficiency in most of the higher-level intellectual skills. Typical graduates are also distinguished from the threshold level by a capacity for developing and applying personal perspectives critically to their studies.\n"
  stem: none
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates"
  addressee: learner
  verbs: ["display", "demonstrating"]
  about: "the typical graduate in summary"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.5, basis: stated }
  paraphrase: "A typical graduate shows critical awareness of the subject's scope and methods on a solid base of knowledge, commands subject and generic skills consistently with proficiency in most higher intellectual skills, and stands above the threshold by applying their own perspectives critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.7
  locator: { number: "4.7", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 61419, end: 62259 }
  source: "4.7 Geography graduates that achieve excellence beyond the typical standard are distinguished primarily by superior intellectual skills, which are deployed in the context of wide-ranging knowledge of the various aspects of the subject. The strength of geography's methodological breadth is most clearly demonstrated in its best graduates, who bring originality, insight and superior critical and reflective abilities to bear upon this knowledge and have the capacity to link theory and practice in identifying and tackling research problems. This quality is evident across the spectrum of assessed work, but is perhaps most clearly demonstrated in independent work, especially dissertations, which may produce outcomes that are at or close to the levels of publishable research, and which represent an advance within subject knowledge.\n\n19\n"
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "graduates who reach excellence"
  addressee: learner
  verbs: ["distinguished", "deployed", "bring", "link"]
  about: "the excellent graduate in summary"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.6, basis: stated }
  paraphrase: "Excellent graduates stand out mainly through superior intellectual skills used across wide knowledge; they bring originality, insight and strong critical reflection, link theory and practice in research, and show this most in independent work such as dissertations, which may approach publishable quality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 62518, end: 62610 }
  source: "collaborate equitably, and empathise and respect the views, perspectives and needs of others"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "successful graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["collaborate", "empathise", "respect"]
  about: "equitable, empathetic collaboration"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Should have built the ability to work with others fairly, with empathy and respect for their views, perspectives and needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 62613, end: 62731 }
  source: "understand and reflect critically on the norms and values that underlie one's own and others' perspectives and actions"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "successful graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["understand", "reflect"]
  about: "critical reflection on norms and values"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Should have built the ability to grasp, and think critically about, the norms and values behind their own and others' views and actions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 62734, end: 62818 }
  source: "work collaboratively with others offering different knowledge, views and experiences"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "successful graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["work"]
  about: "collaborating across difference"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Should have built the ability to work with people who bring different knowledge, views and experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 62821, end: 62935 }
  source: "be aware of, and have an understanding of, the impact of their own, and others' emotional response and well-being."
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "successful graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["have"]
  about: "awareness of emotions and wellbeing"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Should have built awareness and understanding of how their own and others' emotional responses and wellbeing affect them and their work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 62992, end: 63086 }
  source: "Describe and exemplify the nature of change and variability within societies and environments."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["describe", "exemplify"]
  about: "change and variability in societies and environments (threshold)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can describe, with examples, how societies and environments change and vary."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b5.excellent
  locator: { number: "4.8.b5.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 63188, end: 63304 }
  source: "Demonstrate critical insight into the nature and causes of change and variability within societies and environments."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["demonstrate"]
  about: "change and variability in societies and environments (excellent)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b5.typical, basis: stated }
  paraphrase: "An excellent graduate can show critical insight into why and how societies and environments change and vary."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b5.typical
  locator: { number: "4.8.b5.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 63087, end: 63187 }
  source: "Demonstrate comprehension of the nature of change and variability within societies and environments."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["demonstrate"]
  about: "change and variability in societies and environments (typical)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b5, basis: stated }
  paraphrase: "A typical graduate can show a sound grasp of how societies and environments change and vary."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b6
  locator: { number: "4.8.b6", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 63305, end: 63432 }
  source: "Describe and exemplify the reciprocal relationships between societies and environments at multiple spatial and temporal scales."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["describe", "exemplify"]
  about: "the two-way relationships between societies and environments (threshold)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can describe, with examples, the two-way links between societies and environments across scales of space and time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b6.excellent
  locator: { number: "4.8.b6.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 63567, end: 63721 }
  source: "Demonstrate critical insight of the complexity of the reciprocal relationships between societies and environments at multiple spatial and temporal scales."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the two-way relationships between societies and environments (excellent)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b6.typical, basis: stated }
  paraphrase: "An excellent graduate can show critical insight into how complex the two-way links between societies and environments are, across scales of space and time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b6.typical
  locator: { number: "4.8.b6.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 63433, end: 63566 }
  source: "Demonstrate comprehension of the reciprocal relationships between societies and environments at multiple spatial and temporal scales."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the two-way relationships between societies and environments (typical)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b6, basis: stated }
  paraphrase: "A typical graduate can show a sound grasp of the two-way links between societies and environments across scales of space and time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b7
  locator: { number: "4.8.b7", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 63722, end: 63863 }
  source: "Describe approaches to sustainability and sustainable development in relation to the complex interactions between societies and environments."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["describe"]
  about: "sustainability and sustainable development (threshold)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can describe ways of approaching sustainability and sustainable development as they bear on how societies and environments interact."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b7.excellent
  locator: { number: "4.8.b7.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 64022, end: 64184 }
  source: "Demonstrate critical insight into sustainability and sustainable development practices in relation to the complex interactions between societies and environments."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["demonstrate"]
  about: "sustainability and sustainable development (excellent)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b7.typical, basis: stated }
  paraphrase: "An excellent graduate can show critical insight into sustainability and sustainable development practice as it bears on how societies and environments interact."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b7.typical
  locator: { number: "4.8.b7.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 63864, end: 64021 }
  source: "Demonstrate comprehension of sustainability and sustainable development practices in relation to the complex interactions between societies and environments."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["demonstrate"]
  about: "sustainability and sustainable development (typical)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b7, basis: stated }
  paraphrase: "A typical graduate can show a sound grasp of sustainability and sustainable development practice as it bears on how societies and environments interact."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b8
  locator: { number: "4.8.b8", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 64185, end: 64362 }
  source: "Describe the history of geography as a discipline and the relevant contexts of past and present geographical knowledge production, and contemporary implications of this history."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["describe"]
  about: "the history of geography and its making of knowledge (threshold)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can describe how geography grew as a discipline, the settings in which its knowledge was and is made, and what that history means now."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b8.excellent
  locator: { number: "4.8.b8.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 64561, end: 64769 }
  source: "Demonstrate a critical understanding of the history of geography as a discipline and the relevant contexts of past and present geographical knowledge production, and contemporary implications of this history."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the history of geography and its making of knowledge (excellent)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b8.typical, basis: stated }
  paraphrase: "An excellent graduate can show a critical understanding of the discipline's history, the settings of its knowledge-making then and now, and their present-day consequences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b8.typical
  locator: { number: "4.8.b8.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 64363, end: 64560 }
  source: "Demonstrate comprehension of the history of geography as a discipline and the relevant contexts of past and present geographical knowledge production, and contemporary implications of this history."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the history of geography and its making of knowledge (typical)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b8, basis: stated }
  paraphrase: "A typical graduate can show a sound grasp of the discipline's history, the settings of its knowledge-making then and now, and their present-day consequences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b9
  locator: { number: "4.8.b9", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 64770, end: 64837 }
  source: "Describe and exemplify the diversity and interdependency of places."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["describe", "exemplify"]
  about: "the diversity and interdependence of places (threshold)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can describe, with examples, how places differ and depend on one another."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b9.excellent
  locator: { number: "4.8.b9.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 64904, end: 64980 }
  source: "Reflect on and appraise the reasons for the diversity and interdependency of"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["reflect", "appraise"]
  about: "the diversity and interdependence of places (excellent)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b9.typical, basis: stated }
  paraphrase: "An excellent graduate can reflect on and judge the reasons why places at different scales differ and depend on one another."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b9.typical
  locator: { number: "4.8.b9.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 64838, end: 64903 }
  source: "Demonstrate comprehension of the diversity and interdependency of"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the diversity and interdependence of places (typical)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b9, basis: stated }
  paraphrase: "A typical graduate can show a sound grasp of how places at different scales differ and depend on one another."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b10
  locator: { number: "4.8.b10", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65053, end: 65246 }
  source: "Describe and exemplify the diversity of approaches to generation of knowledge and understanding deriving from experience of the epistemologies of the natural and social sciences and humanities."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["describe", "exemplify"]
  about: "ways of producing geographical knowledge (threshold)"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can describe, with examples, the different ways knowledge is produced across the natural sciences, social sciences and humanities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b10.excellent
  locator: { number: "4.8.b10.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65431, end: 65625 }
  source: "Critically appraise the diversity of approaches to the generation of knowledge and understanding deriving from experience of the epistemologies of the natural and social sciences and humanities."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["appraise"]
  about: "ways of producing geographical knowledge (excellent)"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b10.typical, basis: stated }
  paraphrase: "An excellent graduate can critically appraise the different ways knowledge is produced across the natural sciences, social sciences and humanities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b10.typical
  locator: { number: "4.8.b10.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65247, end: 65430 }
  source: "Evaluate the diversity of approaches to the generation of knowledge and understanding deriving from experience of the epistemologies of the natural and social sciences and humanities."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["evaluate"]
  about: "ways of producing geographical knowledge (typical)"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b10, basis: stated }
  paraphrase: "A typical graduate can evaluate the different ways knowledge is produced across the natural sciences, social sciences and humanities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b11
  locator: { number: "4.8.b11", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65626, end: 65673 }
  source: "Carry out routine investigations as instructed."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["carry"]
  about: "applying geographical concepts (threshold)"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can carry out routine investigations when told how."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b11.excellent
  locator: { number: "4.8.b11.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65744, end: 65826 }
  source: "Apply a reflective understanding of geographical concepts in different situations."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["apply"]
  about: "applying geographical concepts (excellent)"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b11.typical, basis: stated }
  paraphrase: "An excellent graduate can apply geographical concepts to varied situations with reflection."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b11.typical
  locator: { number: "4.8.b11.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65674, end: 65743 }
  source: "Apply understanding of geographical concepts in different situations."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["apply"]
  about: "applying geographical concepts (typical)"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b11, basis: stated }
  paraphrase: "A typical graduate can use their grasp of geographical concepts in varied situations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b12
  locator: { number: "4.8.b12", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65827, end: 65878 }
  source: "Know the difference between accuracy and precision."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["know"]
  about: "accuracy, precision and uncertainty in data (threshold)"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can tell accuracy apart from precision."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b12.excellent
  locator: { number: "4.8.b12.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65947, end: 66026 }
  source: "Critically reflect on the accuracy, precision and uncertainty of research data."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["reflect"]
  about: "accuracy, precision and uncertainty in data (excellent)"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b12.typical, basis: stated }
  paraphrase: "An excellent graduate can reflect critically on how accurate, precise and uncertain research data are."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b12.typical
  locator: { number: "4.8.b12.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65879, end: 65946 }
  source: "Apply a systematic approach to accuracy, precision and uncertainty."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["apply"]
  about: "accuracy, precision and uncertainty in data (typical)"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b12, basis: stated }
  paraphrase: "A typical graduate can handle accuracy, precision and uncertainty systematically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b13
  locator: { number: "4.8.b13", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 66081, end: 66214 }
  source: "Illustrate the issues involved in applying research design and execution skills within the specific context of field- based research."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["illustrate"]
  about: "research design and execution in field research (threshold)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can illustrate the issues that arise in designing and carrying out research in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b13.excellent
  locator: { number: "4.8.b13.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 66346, end: 66554 }
  source: "Formulate a sophisticated and comprehensive analysis of the issues involved in applying research design and execution skills within the specific context of field-based research, including alternative options."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["formulate"]
  about: "research design and execution in field research (excellent)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b13.typical, basis: stated }
  paraphrase: "An excellent graduate can formulate a thorough, sophisticated analysis of the issues in designing and carrying out field research, with alternative options."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b13.typical
  locator: { number: "4.8.b13.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 66215, end: 66345 }
  source: "Evaluate the issues involved in applying research design and execution skills within the specific context of field-based research."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["evaluate"]
  about: "research design and execution in field research (typical)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b13, basis: stated }
  paraphrase: "A typical graduate can evaluate the issues that arise in designing and carrying out research in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b14
  locator: { number: "4.8.b14", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 66555, end: 66796 }
  source: "Illustrate diversity of techniques and approaches involved in collecting geographical information (for example, instrumentation, remote sensing, cartographic surveying, social survey, observation and the use of textual and archival sources)."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["illustrate"]
  about: "techniques for collecting geographical information (threshold)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can illustrate the range of techniques for collecting geographical information, such as instruments, remote sensing, surveys, observation and archives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b14.excellent
  locator: { number: "4.8.b14.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 67041, end: 67317 }
  source: "Critically appraise and reflect on use of the diversity of techniques and approaches involved in collecting geographical information (for example, instrumentation, remote sensing, cartographic surveying, social survey, observation and the use of textual and archival sources)."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["appraise", "reflect"]
  about: "techniques for collecting geographical information (excellent)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b14.typical, basis: stated }
  paraphrase: "An excellent graduate can critically appraise and reflect on their own use of the range of techniques for collecting geographical information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b14.typical
  locator: { number: "4.8.b14.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 66797, end: 67040 }
  source: "Evaluate the diversity of techniques and approaches involved in collecting geographical information (for example, instrumentation, remote sensing, cartographic surveying, social survey, observation and the use of textual and archival sources)."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["evaluate"]
  about: "techniques for collecting geographical information (typical)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b14, basis: stated }
  paraphrase: "A typical graduate can evaluate the range of techniques for collecting geographical information, such as instruments, remote sensing, surveys, observation and archives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b15
  locator: { number: "4.8.b15", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 67318, end: 67455 }
  source: "Illustrate both quantitative and qualitative approaches for analysis of geographical information and data and perform basic applications."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["illustrate", "perform"]
  about: "quantitative and qualitative analysis (threshold)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can illustrate quantitative and qualitative ways of analysing geographical data and carry out basic applications of them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b15.excellent
  locator: { number: "4.8.b15.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 67582, end: 67734 }
  source: "Critically appraise and reflect on the application of quantitative and qualitative approaches for analysis of geographical data, including excellent and"
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["appraise", "reflect"]
  about: "quantitative and qualitative analysis (excellent)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b15.typical, basis: stated }
  paraphrase: "An excellent graduate can critically appraise and reflect on using quantitative and qualitative analysis, applying a range of approaches with excellence and sophistication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b15.typical
  locator: { number: "4.8.b15.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 67456, end: 67581 }
  source: "Evaluate both quantitative and qualitative approaches for analysis of geographical information and data, including competence"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["evaluate"]
  about: "quantitative and qualitative analysis (typical)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b15, basis: stated }
  paraphrase: "A typical graduate can evaluate quantitative and qualitative ways of analysing geographical data, applying a range of them competently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b16
  locator: { number: "4.8.b16", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 67848, end: 68100 }
  source: "Illustrate diversity of specialised techniques and approaches involved in analysing geographical information (for example, special techniques for the analysis of spatial information, GIS, laboratory techniques, qualitative and quantitative techniques)."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["illustrate"]
  about: "specialised techniques of analysis (threshold)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can illustrate the range of specialised techniques for analysing geographical information, such as spatial analysis, GIS and laboratory methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b16.excellent
  locator: { number: "4.8.b16.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 68356, end: 68644 }
  source: "Demonstrate a mastery of techniques and approaches involved in analysing geographical information (for example, special techniques for the analysis of spatial information, GIS, laboratory techniques, qualitative and quantitative techniques) and very good judgement of their effectiveness."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["demonstrate"]
  about: "specialised techniques of analysis (excellent)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b16.typical, basis: stated }
  paraphrase: "An excellent graduate can show mastery of specialised analytical techniques and very good judgement of how well they work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b16.typical
  locator: { number: "4.8.b16.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 68101, end: 68355 }
  source: "Evaluate the diversity of specialised techniques and approaches involved in analysing geographical information (for example, special techniques for the analysis of spatial information, GIS, laboratory techniques, qualitative and quantitative techniques)."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["evaluate"]
  about: "specialised techniques of analysis (typical)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b16, basis: stated }
  paraphrase: "A typical graduate can evaluate the range of specialised techniques for analysing geographical information, such as spatial analysis, GIS and laboratory methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b17
  locator: { number: "4.8.b17", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 68645, end: 68710 }
  source: "Summarise information and data and make accurate interpretations."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["summarise", "make"]
  about: "synthesising and interpreting information (threshold)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can summarise information and data and interpret them accurately."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b17.excellent
  locator: { number: "4.8.b17.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 68827, end: 68968 }
  source: "Synthesize information and data and make accurate and critically reflective interpretations in the context of current geographical knowledge."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["synthesize", "make"]
  about: "synthesising and interpreting information (excellent)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b17.typical, basis: stated }
  paraphrase: "An excellent graduate can bring information and data together and interpret them accurately and with critical reflection in light of current geographical knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b17.typical
  locator: { number: "4.8.b17.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 68711, end: 68826 }
  source: "Synthesize information and data and make accurate interpretations in the context of current geographical knowledge."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["synthesize", "make"]
  about: "synthesising and interpreting information (typical)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b17, basis: stated }
  paraphrase: "A typical graduate can bring information and data together and interpret them accurately in light of current geographical knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b18
  locator: { number: "4.8.b18", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 68969, end: 69158 }
  source: "Illustrate diversity of specialised techniques and approaches involved in presenting geographical knowledge and information (for example, GIS, cartography and different textual strategies)."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["illustrate"]
  about: "presenting geographical information (threshold)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can illustrate the range of specialised ways of presenting geographical knowledge, such as GIS, cartography and textual strategies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b18.excellent
  locator: { number: "4.8.b18.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 69338, end: 69472 }
  source: "Critically evaluate and reflect on the appropriate application of the diversity of specialised geographical techniques and approaches."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["evaluate", "reflect"]
  about: "presenting geographical information (excellent)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b18.typical, basis: stated }
  paraphrase: "An excellent graduate can critically evaluate and reflect on how suitably specialised geographical techniques are applied."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b18.typical
  locator: { number: "4.8.b18.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 69159, end: 69337 }
  source: "Evaluate the diversity of specialised techniques and approaches involved in presenting geographical information (for example, GIS, cartography and dif ferent textual strategies)."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["evaluate"]
  about: "presenting geographical information (typical)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b18, basis: stated }
  paraphrase: "A typical graduate can evaluate the range of specialised ways of presenting geographical information, such as GIS, cartography and textual strategies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b19
  locator: { number: "4.8.b19", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 69473, end: 69566 }
  source: "Communicate geographical ideas, principles and theories by written, oral and graphical means."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating geographical ideas (threshold)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can put across geographical ideas, principles and theories in writing, speech and graphics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b19.excellent
  locator: { number: "4.8.b19.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 69686, end: 69819 }
  source: "Communicate geographical ideas, principles and theories with flair, accuracy and sophistication by written, oral and graphical means."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating geographical ideas (excellent)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b19.typical, basis: stated }
  paraphrase: "An excellent graduate can put across geographical ideas, principles and theories with flair, precision and sophistication in writing, speech and graphics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b19.typical
  locator: { number: "4.8.b19.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 69567, end: 69685 }
  source: "Communicate geographical ideas, principles and theories effectively and fluently by written, oral and graphical means."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating geographical ideas (typical)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b19, basis: stated }
  paraphrase: "A typical graduate can put across geographical ideas, principles and theories well and fluently in writing, speech and graphics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b20
  locator: { number: "4.8.b20", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 69864, end: 69917 }
  source: "Communicate personal views about geographical issues."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["communicate"]
  about: "views on geographical issues (threshold)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can express their own views on geographical issues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b20.excellent
  locator: { number: "4.8.b20.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 69985, end: 70084 }
  source: "Critically reflect on a range of views about geographical issues and come to a reasoned evaluation."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["reflect", "come"]
  about: "views on geographical issues (excellent)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b20.typical, basis: stated }
  paraphrase: "An excellent graduate can reflect critically on a range of views on geographical issues and reach a reasoned judgement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b20.typical
  locator: { number: "4.8.b20.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 69918, end: 69984 }
  source: "Communicate and compare different views about geographical issues."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["communicate", "compare"]
  about: "views on geographical issues (typical)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b20, basis: stated }
  paraphrase: "A typical graduate can express and compare differing views on geographical issues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b21
  locator: { number: "4.8.b21", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 70089, end: 70209 }
  source: "Demonstrate an awareness of their positionality and assumptions and the potential implications and consequences of them."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["demonstrate"]
  about: "positionality and assumptions (threshold)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can show awareness of their own positionality and assumptions and of what these may lead to."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b21.excellent
  locator: { number: "4.8.b21.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 70322, end: 70444 }
  source: "Recognise their positionality and assumptions and critically evaluate the potential implications and consequences of them."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["recognise", "evaluate"]
  about: "positionality and assumptions (excellent)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b21.typical, basis: stated }
  paraphrase: "An excellent graduate can recognise their positionality and assumptions and critically evaluate what these may lead to."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b21.typical
  locator: { number: "4.8.b21.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 70210, end: 70321 }
  source: "Recognise their positionality and assumptions and evaluate the potential implications and consequences of them."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["recognise", "evaluate"]
  about: "positionality and assumptions (typical)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b21, basis: stated }
  paraphrase: "A typical graduate can recognise their positionality and assumptions and evaluate what these may lead to."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b22
  locator: { number: "4.8.b22", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 70445, end: 70493 }
  source: "Present material to support a reasoned argument."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["present"]
  about: "reasoned argument (threshold)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can present material in support of a reasoned argument."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b22.excellent
  locator: { number: "4.8.b22.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 70605, end: 70736 }
  source: "Synthesize complex information to support the presentation of a reasoned argument to both specialist and non- specialist audiences."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["synthesize"]
  about: "reasoned argument (excellent)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b22.typical, basis: stated }
  paraphrase: "An excellent graduate can draw complex information together to put a reasoned argument to specialists and non-specialists alike."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b22.typical
  locator: { number: "4.8.b22.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 70494, end: 70604 }
  source: "Synthesize material appropriately to support the presentation of a reasoned argument to the intended audience."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["synthesize"]
  about: "reasoned argument (typical)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b22, basis: stated }
  paraphrase: "A typical graduate can draw material together suitably to put a reasoned argument to its intended audience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b23
  locator: { number: "4.8.b23", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 70737, end: 70833 }
  source: "Use communications and ICT to select, analyse, present and communicate geographical information."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["use"]
  about: "communications technology and ICT (threshold)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can use communication technologies and ICT to select, analyse, present and share geographical information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b23.excellent
  locator: { number: "4.8.b23.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 70961, end: 71089 }
  source: "Use communications and ICT with a high level of competence to select, analyse, present and communicate geographical information."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["use"]
  about: "communications technology and ICT (excellent)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b23.typical, basis: stated }
  paraphrase: "An excellent graduate can use communication technologies and ICT highly competently to select, analyse, present and share geographical information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b23.typical
  locator: { number: "4.8.b23.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 70834, end: 70960 }
  source: "Use communications and ICT effectively and appropriately to select, analyse, present and communicate geographical information."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["use"]
  about: "communications technology and ICT (typical)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b23, basis: stated }
  paraphrase: "A typical graduate can use communication technologies and ICT well and suitably to select, analyse, present and share geographical information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b24
  locator: { number: "4.8.b24", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 71090, end: 71201 }
  source: "Undertake independent/ self-directed study/ learning (including time management) within a supportive framework."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["undertake"]
  about: "independent study and time management (threshold)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can study independently and manage their time within a supportive structure."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b24.excellent
  locator: { number: "4.8.b24.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 71343, end: 71485 }
  source: "Undertake highly autonomous and well organised study/ learning and time management to achieve consistent, proficient and sustained attainment."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["undertake", "achieve"]
  about: "independent study and time management (excellent)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b24.typical, basis: stated }
  paraphrase: "An excellent graduate can study with high autonomy and good organisation, managing their time to attain consistently, proficiently and steadily."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b24.typical
  locator: { number: "4.8.b24.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 71202, end: 71342 }
  source: "Undertake independent/ self-directed study/ learning (including time management) to achieve consistent, proficient and sustained attainment."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["undertake", "achieve"]
  about: "independent study and time management (typical)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b24, basis: stated }
  paraphrase: "A typical graduate can study independently and manage their time so as to attain consistently, proficiently and steadily."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b25
  locator: { number: "4.8.b25", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 71486, end: 71567 }
  source: "Perform assigned tasks within a group setting and take part in group discussions."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["perform", "take"]
  about: "group work and leadership (threshold)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can carry out tasks given to them in a group and join in its discussions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b25.excellent
  locator: { number: "4.8.b25.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 71672, end: 71785 }
  source: "Demonstrate group leadership and supportive participation of others within a group setting to achieve objectives."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["demonstrate"]
  about: "group work and leadership (excellent)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b25.typical, basis: stated }
  paraphrase: "An excellent graduate can lead a group and support others' participation so that it meets its aims."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b25.typical
  locator: { number: "4.8.b25.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 71568, end: 71671 }
  source: "Work as a participant or leader of a group and contribute effectively to the achievement of objectives."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["work", "contribute"]
  about: "group work and leadership (typical)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b25, basis: stated }
  paraphrase: "A typical graduate can work as a member or leader of a group and help it meet its aims."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b26
  locator: { number: "4.8.b26", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 71786, end: 71887 }
  source: "Describe the process of learning and present a basic assessment of personal strengths and weaknesses."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "threshold graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["describe", "present"]
  about: "reflecting on one's own learning (threshold)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As the minimum for the award, the graduate can describe how they learn and give a basic account of their own strengths and weaknesses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b26.excellent
  locator: { number: "4.8.b26.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 71968, end: 72121 }
  source: "Critically reflect on the process of learning, evaluating personal strengths and weaknesses and demonstrating an understanding of alternative strategies."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "excellent graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["reflect", "evaluating", "demonstrating"]
  about: "reflecting on one's own learning (excellent)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b26.typical, basis: stated }
  paraphrase: "An excellent graduate can reflect critically on how they learn, weighing their strengths and weaknesses and showing they understand other strategies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/geography-2022/4.8.b26.typical
  locator: { number: "4.8.b26.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 71888, end: 71967 }
  source: "Analyse the process of learning and evaluate personal strengths and weaknesses."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "typical graduates of honours and integrated master's degrees"
  addressee: learner
  verbs: ["analyse", "evaluate"]
  about: "reflecting on one's own learning (typical)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: { statement: qaa/geography-2022/4.8.b26, basis: stated }
  paraphrase: "A typical graduate can analyse how they learn and evaluate their own strengths and weaknesses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/geography-2022/1.5
  forPractitioner: { text: "Treat inclusion as a task for the whole community: staff, students and partners will need to engage, reflect and change, with concrete work on widening participation, under-represented groups, zero tolerance of harassment, neurodiverse access and awarding gaps.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As a member of the geography learning community you will be asked to help make it fair and inclusive: to take part, reflect on your own assumptions and be ready to change.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a shared expectation on the whole learning community, carried by \"will need to\", that everyone engages, reflects and changes to embed equity and inclusion. It carries no level: it concerns the course or the community, not one stage of study. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 1.5, and do not claim that it is a legal duty under the Equality Act or a measurable student outcome. Set it beside 1.6 to 1.9, the inclusion statements 2.6, 2.15 and 3.19, and the collaboration outcome 4.8.b1."
  author-agent-dialogue: "Bring this up when a student or colleague asks what inclusion means in geography, or a programme team reviews its equity work. Put it in plain words, as something everyone shares rather than a rule for students alone, and ask: What have you changed in how you work or study after thinking about who is included? Where do you see gaps in access or awarding on your course? Avoid reading the paragraph aloud, or presenting it to a student as a test they must pass."
- statement: qaa/geography-2022/1.6
  forPractitioner: { text: "Course teams must name and actively work against the colonial roots of geographical knowledge and their present-day legacies of disadvantage, building a community that includes students, academics, technicians, professional staff, visitors and partners.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will look at how geography's colonial past still shapes disadvantage today, and you belong to a community that must recognise and work against those legacies.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation (must) on the subject community to acknowledge and counter the colonial and imperial legacies in geography. It carries no level: it binds the subject community at every stage of the degree. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 1.6, and do not claim that it prescribes one decolonial curriculum, or that it is a regulatory condition. Set it beside 1.7, 1.8, the knowledge paragraph 3.8 and the history-of-geography row 4.8.b8 with its typical and excellent cells."
  author-agent-dialogue: "Bring this up when a student asks why the course examines geography's colonial history, or a team plans decolonising work. Put it plainly and without blame, in the second person for a student and as a curriculum obligation for staff, and ask: Where in your modules do you meet the colonial history of the discipline? What would countering its legacies look like in your own work? Avoid lecturing at length from the text or treating it as an optional extra."
- statement: qaa/geography-2022/1.7
  forPractitioner: { text: "Thread care, plural knowledges, respect, decolonial attention and solidarity through every part of the curriculum; they should not be confined to particular modules or sub-fields.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design; the student meets its effect across modules", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a curriculum expectation (should) that the subject's core values run through every module. It sets no level and applies to course design across all years. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 1.7, and do not claim that students are assessed on holding these values, or that it is a regulatory rule. Set it beside 1.6, 1.8 and the reflection outcome 4.8.b2."
  author-agent-dialogue: "Bring this up when a programme team maps where values such as care and solidarity appear in its curriculum. Put it as a design or planning question for the programme team, and ask: Which modules carry these values, and which leave them out? Would a student meet them in every year? Avoid giving it to a student as a requirement on them."
- statement: qaa/geography-2022/1.8
  forPractitioner: { text: "Apply critical theory across every branch of the course, not only in human geography, and plan each learning site, whether online, in a classroom, outdoors or in a laboratory, with its likely barriers anticipated.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a curriculum expectation (should) that critical theory is applied across the whole discipline. It sets no level; it shapes design throughout the degree. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 1.8, and do not claim that its list of theories is closed, since the issuer says it is not limited. Set it beside 1.7, 1.9 and the fieldwork access statements 2.6 and 3.19."
  author-agent-dialogue: "Bring this up when a team asks whether physical geography modules need critical theory too, or plans inclusive laboratory or field teaching. Put it as a design or planning question for the programme team, and ask: Where does critical theory appear in your physical and quantitative modules? Which learning sites have you checked for barriers? Avoid putting it to a student as an obligation."
- statement: qaa/geography-2022/1.12
  forPractitioner: { text: "Graduates will collect, analyse and work with quantitative and qualitative data, bring spatial analysis across scales and disciplines to complex social and economic problems, and use evidence to inform innovation and decisions, understanding green, social and digital enterprise.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to collect, analyse and work with both numerical and qualitative data, use your spatial thinking to help solve complex social and economic problems, and understand different kinds of enterprise, including green, social and digital ones.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome graduates will reach (\"are able to\"), placed in the enterprise and entrepreneurship section. Hold it at FHEQ Level 6 (FQHEIS Level 10), the honours degree. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 1.12, and do not claim that every graduate must be an entrepreneur, or that it adds a separate enterprise requirement. Set it beside the attribute 3.34.b3, the analysis row 4.8.b15, qaa/fheq-2024/4.15.b9.2 and spine:6."
  author-agent-dialogue: "Bring this up when a student asks how geography skills lead to work or enterprise, or a team plans employability content. Put it in plain words, in the second person to a student and as a course-design point to staff, and ask: Which data have you collected and analysed yourself? Where could that work help a business, charity or public body decide something? Avoid implying that only commercial enterprise counts, since social and environmental value count too."
- statement: qaa/geography-2022/2.1
  forPractitioner: { text: "Design the course so its outcomes rise in complexity year on year and line up with how you teach and assess, and involve students in reviewing and co-producing the design.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a course-design expectation (should): outcomes of rising complexity aligned with teaching and assessment. It spans the whole degree, up to FHEQ Level 6 (FQHEIS Level 10), or Level 7 for the integrated master's. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 2.1, and do not claim that it fixes outcomes for any one year. Set it beside 2.7 and 2.8 on progression, 3.40 on assessment, and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Bring this up when a programme team plans outcomes across the years or checks alignment. Put it as a design or planning question for the programme team, and ask: Do your outcomes get harder each year? Does each assessment test the outcome it claims to? Avoid giving it to a student as a duty."
- statement: qaa/geography-2022/2.6
  forPractitioner: { text: "Recognise students' individual needs in the field; fieldwork leaders are responsible for anticipating barriers of any protected characteristic, class, gender identity or neurodiversity and for adequate facilities, and course designers need to keep extra fieldwork, clothing or equipment costs from excluding anyone.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on fieldwork leaders and course designers; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider duty (should, with \"responsible for\" and \"need to\" beside it) to make fieldwork inclusive and affordable. It sets no level and applies to all fieldwork in the degree. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 2.6, and do not claim that it lets a course drop fieldwork, which the issuer calls essential. Set it beside 3.15, 3.18, 3.19, 3.20 and 1.8 on anticipatory design."
  author-agent-dialogue: "Bring this up when a team plans a field trip or a student raises a barrier to taking part. Put it with staff as a planning duty, and with a student only to reassure them that removing barriers falls to the course, and ask: What barriers of cost, access or identity could this trip create? Who would carry the extra cost? Avoid presenting it to a student as their duty."
- statement: qaa/geography-2022/2.7
  forPractitioner: { text: "Build breadth early and specialism later, so that by the end students will situate their specialism within geography's wider approach, history and theory; tell applicants clearly what is distinctive about your course.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your degree will start broad and let you specialise later; by the end you will be able to show how your specialism fits into geography as a whole, including its history and theory.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an end-of-course outcome (\"are able to\") about placing a specialism within the discipline. Hold it at FHEQ Level 6 (FQHEIS Level 10), and for the integrated master's at the end of that course. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 2.7, and do not claim that it fixes which specialism a student must choose. Set it beside 2.8, the history row 4.8.b8, qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Bring this up when a student is choosing options or a final-year project, or a team reviews breadth against specialism. Put it in plain words, in the second person to a student and as a course-design point to staff, and ask: How does your chosen specialism connect to the rest of geography? Which wider debates does it draw on? Avoid treating specialisation as a reason to drop breadth."
- statement: qaa/geography-2022/2.8
  forPractitioner: { text: "Plan for growth: students will evaluate evidence and sources with rising sophistication, will be given chances to show deeper critical reflection, and will take on fieldwork or projects with increasing independence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As you move through your degree you will judge evidence and sources more critically, and you will be able to plan and carry out fieldwork or projects more and more on your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a progression outcome (\"are able to\", \"will\"): rising critical evaluation and independence in fieldwork or projects. Read it across the years of the degree up to FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 2.8, and do not claim that full independence is expected from the first year. Set it beside 2.7, 2.9, the independent study row 4.8.b24 and qaa/fheq-2024/4.15.b5."
  author-agent-dialogue: "Bring this up when a student asks how expectations change between years, or a team checks progression in fieldwork. Put it in plain words, in the second person to a student and as a course-design point to staff, and ask: How much of your last fieldwork or project did you plan yourself? How do you now judge whether a source is reliable? Avoid expecting final-year independence from a first-year student."
- statement: qaa/geography-2022/2.9
  forPractitioner: { text: "Give students chances, as they progress, to see how collecting primary data shapes knowledge of the world and how data relate to reality; students should deepen this understanding over the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "As you progress, you should come to understand how the way data are collected shapes what we think we know about the world.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a progression expectation (should) on students' understanding of data and knowledge, with a matching duty on the course to give chances. Read it across the degree up to FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 2.9, and do not claim that it is a rung standard or that it concerns quantitative work alone. Set it beside 2.8, 3.15, the epistemology row 4.8.b10 and the accuracy row 4.8.b12."
  author-agent-dialogue: "Bring this up when a student reflects on fieldwork data or a team plans a methods module. Put it in plain words, in the second person to a student and as a course-design point to staff, and ask: How did the way you collected your data shape what you concluded? What could a different method have shown? Avoid heavy philosophical terms without examples."
- statement: qaa/geography-2022/2.13
  forPractitioner: { text: "Resource flexible and accessible materials properly, and design them to work for students with limited devices or connectivity, so that flexibility does not backfire.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design and resourcing", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) on resourcing flexible delivery and allowing for unequal access to technology. It sets no level and applies across the course. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 2.13, and do not claim that it requires any particular platform. Set it beside 2.3, 2.11, 2.12 and 3.40."
  author-agent-dialogue: "Bring this up when a team moves teaching online or blends delivery. Put it as a design or planning question for the programme team, and ask: Which students lack reliable devices or internet? What happens to them if a task is online only? Avoid putting the duty on students."
- statement: qaa/geography-2022/2.15
  forPractitioner: { text: "Make partnership opportunities, from placements and projects to student societies, equally open to all students, and brief partners on the equity, equality, diversity and inclusion principles they share with you.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the institution", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an institutional expectation (should) of equal access to partnerships. It sets no level. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 2.15, and do not claim that every student is guaranteed a placement. Set it beside 2.14, 2.16, 2.17 and 1.5."
  author-agent-dialogue: "Bring this up when a team plans placements or partner projects, or a student asks why they could not join one. Put it as a duty on the institution, and to a student as what they may fairly expect, and ask: Who has taken up partnership opportunities so far, and who has not? What stops some students taking part? Avoid telling a student they must find their own partnership."
- statement: qaa/geography-2022/2.16
  forPractitioner: { text: "Design every partnership activity, brief or lasting, around the student and around understanding geography outside the university.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a design expectation (should) for partnership activities. It sets no level. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 2.16, and do not claim that partnerships are compulsory. Set it beside 2.14, 2.15 and 2.17."
  author-agent-dialogue: "Bring this up when a team designs a placement or partner project. Put it as a design or planning question for the programme team, and ask: Who gains most from this partnership as designed? What will students learn about geography outside academia? Avoid giving it to a student as a requirement."
- statement: qaa/geography-2022/2.20
  forPractitioner: { text: "Bring external reviewers into periodic review to test proposed changes, confirm threshold standards are met and check the content fits geography.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in quality assurance", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider expectation (will) to use external reviewers in periodic review. It sets no level; it concerns review of the whole course. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 2.20, and do not claim that it sets the review cycle or replaces external examining. Set it beside 2.19, 2.21 and the threshold definition 4.1."
  author-agent-dialogue: "Bring this up when a team prepares for periodic review. Put it as a design or planning question for the programme team, and ask: Who will act as external reviewer, and what will they check against? Which threshold standards might they question? Avoid raising it with students as their duty."
- statement: qaa/geography-2022/3.3
  forPractitioner: { text: "Graduates will show knowledge and explanation of spatial distributions in physical and human phenomena, understand rates of change across scales, evaluate the processes behind past, present and future geographies, and recognise how scale shapes conclusions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to explain where physical and human things are found and why, how they change over time and space, and how the scale you study at affects what you conclude.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a knowledge outcome (\"are able to\") on spatial distributions and scale. Hold it at FHEQ Level 6 (FQHEIS Level 10), the honours degree. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.3, and do not claim that it lists every topic a course must teach. Set it beside 3.5, the rows 4.8.b5 and 4.8.b6 with their typical and excellent cells, and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Bring this up when a student revises core ideas or asks what scale means in geography. Put it in plain words, in the second person to a student and as a course-design point to staff, and ask: Can you explain why something you studied is found where it is? Would your conclusion change at a different scale? Avoid a list of definitions without an example."
- statement: qaa/geography-2022/3.5
  forPractitioner: { text: "Graduates will apply a systems framework to think critically about patterns, processes and change, taking in environmental impacts on people, human impacts on biophysical and climate systems, and the management of environments.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to use systems thinking to understand how people and the natural world affect each other, climate included, and how environments are managed.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome (\"are able to\") on systems thinking. Hold it at FHEQ Level 6 (FQHEIS Level 10), the honours degree. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.5, and do not claim that it belongs to physical geography alone. Set it beside 3.3, the reciprocal relationships row 4.8.b6 and qaa/fheq-2024/4.15.b3.1."
  author-agent-dialogue: "Bring this up when a student links human and physical topics, or plans an integrated project. Put it in plain words, in the second person to a student and as a course-design point to staff, and ask: What are the parts of the system you studied, and how do they affect each other? Where do people fit in it? Avoid systems jargon without a real case."
- statement: qaa/geography-2022/3.15
  forPractitioner: { text: "Include fieldwork at every stage of the degree, with extended and residential time in the field, so that core skills progress, typically to self-directed fieldwork by the end; this is a requirement, not an option.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will do fieldwork throughout your degree, including longer and residential trips, building up to planning your own fieldwork by the end.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a course requirement (\"required\", read as must) that fieldwork runs through the whole degree. It holds across all years of the honours degree and the integrated master's. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.15, and do not claim that virtual fieldwork can fully replace it, since the issuer says many kinds cannot be replicated (3.17). Set it beside 3.13, 3.14, 3.16 to 3.21 and the field research row 4.8.b13."
  author-agent-dialogue: "Bring this up when a student asks why fieldwork is compulsory, or a team considers cutting field days. Put it plainly to a student and as a firm requirement to staff, and ask: What skills did your last fieldwork build that a classroom could not? How does your fieldwork get more independent each year? Avoid suggesting a course may drop fieldwork."
- statement: qaa/geography-2022/3.18
  forPractitioner: { text: "Complete an ethics assessment and a risk assessment before every taught field trip, and plan it to be ethical, responsible, careful and safe for students, staff, the communities visited and other stakeholders.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who plan fieldwork; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) that every taught field trip has ethics and risk assessments first. It sets no level. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.18, and do not claim that students carry this duty on taught trips. Set it beside 3.19, 3.20, 2.6 and the subject skill 3.30.b2."
  author-agent-dialogue: "Bring this up when a team plans a trip, or a student asks how fieldwork safety is handled. Put it as a design or planning question for the programme team, and ask: Has the ethics assessment considered the communities you will visit? Who signs off the risk assessment? Avoid giving the assessment duty to students on taught trips."
- statement: qaa/geography-2022/3.19
  forPractitioner: { text: "Plan every field trip for inclusion and access, mental and physical health included; fund ways round cost barriers where you can, and complete an inclusivity impact assessment beforehand.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider and fieldwork planners", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) of inclusive, accessible and fair fieldwork, with an inclusivity impact assessment. It sets no level. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.19, and do not claim that the provider must meet every cost, since the issuer says to the extent possible. Set it beside 2.6, 3.18, 3.20 and 1.5."
  author-agent-dialogue: "Bring this up when a team plans fieldwork or a student cannot afford or reach a trip. Put it as a planning duty, and to a student as what they can fairly ask the course for, and ask: What would stop a student joining this trip? What did the inclusivity assessment find? Avoid implying the student must solve access barriers alone."
- statement: qaa/geography-2022/3.20
  forPractitioner: { text: "Run a carbon audit before each taught trip and justify the destination and travel by the outcomes they serve, weighing carbon cost against learning gains.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on fieldwork planners", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) to audit and justify the carbon cost of fieldwork. It sets no level. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.20, and do not claim that distant fieldwork is ruled out. Set it beside 3.17 on virtual fieldwork, 3.18, 3.19 and std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Bring this up when a team chooses a field destination or a student asks about the environmental cost of trips. Put it as a design or planning question for the programme team, and ask: What did the carbon audit show? Which outcomes need this destination rather than a nearer one? Avoid putting the audit on students."
- statement: qaa/geography-2022/3.21
  forPractitioner: { text: "Resource and train fieldwork staff fully; as employer you must recognise that colleagues differ in how far they can lead or take part in fieldwork.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider as employer", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty on the provider as employer: training and support (should) and recognition of staff capacity (must). It sets no level. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.21, and do not claim that it sets staffing ratios. Set it beside 3.18, 3.19 and 2.6."
  author-agent-dialogue: "Bring this up when a department plans fieldwork staffing. Put it as an employer and workload question for staff, and ask: Who is trained to lead this trip? Have colleagues been able to say what they can take on? Avoid raising it with students as their concern."
- statement: qaa/geography-2022/3.26
  forPractitioner: { text: "Graduates will use varied evidence, apply suitable quantitative and qualitative analysis, make informed judgements from it and choose suitable scales in space and time; they are numerate.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to use many kinds of evidence, analyse it with numbers and with qualitative methods, judge soundly from it, and choose the right scale in space and time for your analysis.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome (\"are able to\") on evidence, mixed analysis and scale. Hold it at FHEQ Level 6 (FQHEIS Level 10), the honours degree. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.26, and do not claim that it fixes particular techniques. Set it beside 3.27, 3.28, the analysis row 4.8.b15 and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Bring this up when a student plans an analysis or a dissertation method. Put it in plain words, in the second person to a student and as a course-design point to staff, and ask: Why did you choose that method and that scale? What would the evidence not let you conclude? Avoid presenting one method as always right."
- statement: qaa/geography-2022/3.30.b1
  forPractitioner: { text: "Graduates will show spatial awareness and careful observation; this is one of the subject-specific skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop spatial awareness and careful observation; you are expected to show most, though not necessarily all, of the subject-specific skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of subject-specific skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.30, and do not claim that every graduate must show it. Set it beside the field research row 4.8.b13 and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Bring this up when a student plans fieldwork, a methods module or a dissertation. Put it plainly, in the second person for a student, and ask: What did you notice on your last field visit that a map would not show? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.30.b2
  forPractitioner: { text: "Graduates will show the ability to spot the moral, ethical and safety questions in every part of geographical enquiry; this is one of the subject-specific skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop the ability to spot the moral, ethical and safety questions in every part of geographical enquiry; you are expected to show most, though not necessarily all, of the subject-specific skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of subject-specific skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.30, and do not claim that every graduate must show it. Set it beside 3.18, the positionality row 4.8.b21 and qaa/fheq-2024/4.15.b4."
  author-agent-dialogue: "Bring this up when a student plans fieldwork, a methods module or a dissertation. Put it plainly, in the second person for a student, and ask: What ethical or safety question did your last project raise, and how did you handle it? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.30.b3
  forPractitioner: { text: "Graduates will show skill in carrying out fieldwork and collecting data while judging risks and how to reduce them; this is one of the subject-specific skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop skill in carrying out fieldwork and collecting data while judging risks and how to reduce them; you are expected to show most, though not necessarily all, of the subject-specific skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of subject-specific skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.30, and do not claim that every graduate must show it. Set it beside 3.15, the row 4.8.b13 and qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Bring this up when a student plans fieldwork, a methods module or a dissertation. Put it plainly, in the second person for a student, and ask: What risks did you identify before your fieldwork, and what did you do about them? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.30.b4
  forPractitioner: { text: "Graduates will show skill with interpretative methods such as participant observation, ethnographic interviews and auto-ethnography; this is one of the subject-specific skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop skill with interpretative methods such as participant observation, ethnographic interviews and auto-ethnography; you are expected to show most, though not necessarily all, of the subject-specific skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of subject-specific skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.30, and do not claim that every graduate must show it. Set it beside the collection row 4.8.b14 and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Bring this up when a student plans fieldwork, a methods module or a dissertation. Put it plainly, in the second person for a student, and ask: Which interpretative method have you used, and what did it let you see? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.30.b5
  forPractitioner: { text: "Graduates will show skill with social survey methods such as questionnaires and semi-structured interviews; this is one of the subject-specific skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop skill with social survey methods such as questionnaires and semi-structured interviews; you are expected to show most, though not necessarily all, of the subject-specific skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of subject-specific skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.30, and do not claim that every graduate must show it. Set it beside the collection row 4.8.b14 and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Bring this up when a student plans fieldwork, a methods module or a dissertation. Put it plainly, in the second person for a student, and ask: How did you design your questions, and what would you change next time? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.30.b6
  forPractitioner: { text: "Graduates will show laboratory skills such as preparing and analysing soil, water and sediment samples; this is one of the subject-specific skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop laboratory skills such as preparing and analysing soil, water and sediment samples; you are expected to show most, though not necessarily all, of the subject-specific skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of subject-specific skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.30, and do not claim that every graduate must show it. Set it beside the analysis row 4.8.b16 and qaa/fheq-2024/annex-d/practical/r3/3rd."
  author-agent-dialogue: "Bring this up when a student plans fieldwork, a methods module or a dissertation. Put it plainly, in the second person for a student, and ask: Which laboratory procedure can you run without help, and how do you check your results? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.30.b7
  forPractitioner: { text: "Graduates will show skill in generating, collecting and recording primary data and using secondary data sets, numerical and qualitative; this is one of the subject-specific skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop skill in generating, collecting and recording primary data and using secondary data sets, numerical and qualitative; you are expected to show most, though not necessarily all, of the subject-specific skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of subject-specific skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.30, and do not claim that every graduate must show it. Set it beside the collection row 4.8.b14 and qaa/fheq-2024/4.15.b5."
  author-agent-dialogue: "Bring this up when a student plans fieldwork, a methods module or a dissertation. Put it plainly, in the second person for a student, and ask: When did you choose existing data over collecting your own, and why? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.30.b8
  forPractitioner: { text: "Graduates will show critical judgement, interpretation and combination of kinds of geographical evidence, from texts and archives to maps and laboratory data; this is one of the subject-specific skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop critical judgement, interpretation and combination of kinds of geographical evidence, from texts and archives to maps and laboratory data; you are expected to show most, though not necessarily all, of the subject-specific skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of subject-specific skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.30, and do not claim that every graduate must show it. Set it beside the synthesis row 4.8.b17 and qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Bring this up when a student plans fieldwork, a methods module or a dissertation. Put it plainly, in the second person for a student, and ask: How did you weigh two sources that pointed different ways? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.30.b9
  forPractitioner: { text: "Graduates will show analysis and problem-solving with numerical and qualitative methods; this is one of the subject-specific skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop analysis and problem-solving with numerical and qualitative methods; you are expected to show most, though not necessarily all, of the subject-specific skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of subject-specific skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.30, and do not claim that every graduate must show it. Set it beside the analysis row 4.8.b15 and qaa/fheq-2024/4.15.b3.1."
  author-agent-dialogue: "Bring this up when a student plans fieldwork, a methods module or a dissertation. Put it plainly, in the second person for a student, and ask: Which problem have you solved with data, and which method did you use? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.30.b10
  forPractitioner: { text: "Graduates will show collecting and analysing spatial and environmental information with tools such as GIS, remote sensing and statistical or mathematical models; this is one of the subject-specific skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop collecting and analysing spatial and environmental information with tools such as GIS, remote sensing and statistical or mathematical models; you are expected to show most, though not necessarily all, of the subject-specific skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of subject-specific skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.30, and do not claim that every graduate must show it. Set it beside the rows 4.8.b16 and 4.8.b23 and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Bring this up when a student plans fieldwork, a methods module or a dissertation. Put it plainly, in the second person for a student, and ask: Which spatial tool are you most confident with, and what are its limits? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.30.b11
  forPractitioner: { text: "Graduates will show skill in making clear, effective maps, diagrams and visualisations; this is one of the subject-specific skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop skill in making clear, effective maps, diagrams and visualisations; you are expected to show most, though not necessarily all, of the subject-specific skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of subject-specific skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.30, and do not claim that every graduate must show it. Set it beside the presentation row 4.8.b18 and qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Bring this up when a student plans fieldwork, a methods module or a dissertation. Put it plainly, in the second person for a student, and ask: Who was your last map for, and did it work for them? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.32.b1
  forPractitioner: { text: "Graduates will show skill in weighing up contrasting theories and explanations; this is one of the generic intellectual skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop skill in weighing up contrasting theories and explanations; you are expected to show most, though not necessarily all, of the generic intellectual skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic intellectual skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.32, and do not claim that every graduate must show it. Set it beside the views row 4.8.b20 and qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Bring this up when a student reflects on how they think and argue, or a team maps intellectual skills. Put it plainly, in the second person for a student, and ask: Which two explanations of the same thing have you compared, and which convinced you? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.32.b2
  forPractitioner: { text: "Graduates will show awareness of the social, cultural and political settings in which knowledge is made, of the positions of researcher and researched, and of widening who makes knowledge; this is one of the generic intellectual skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop awareness of the social, cultural and political settings in which knowledge is made, of the positions of researcher and researched, and of widening who makes knowledge; you are expected to show most, though not necessarily all, of the generic intellectual skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic intellectual skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.32, and do not claim that every graduate must show it. Set it beside the positionality row 4.8.b21, 3.8 and qaa/fheq-2024/4.15.b4."
  author-agent-dialogue: "Bring this up when a student reflects on how they think and argue, or a team maps intellectual skills. Put it plainly, in the second person for a student, and ask: Whose knowledge counted in your last project, and whose was missing? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.32.b3
  forPractitioner: { text: "Graduates will show an understanding of how to use evidence and data properly and ethically; this is one of the generic intellectual skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop an understanding of how to use evidence and data properly and ethically; you are expected to show most, though not necessarily all, of the generic intellectual skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic intellectual skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.32, and do not claim that every graduate must show it. Set it beside 3.27, the accuracy row 4.8.b12 and qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Bring this up when a student reflects on how they think and argue, or a team maps intellectual skills. Put it plainly, in the second person for a student, and ask: When might using a data set be legal but still unethical? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.32.b4
  forPractitioner: { text: "Graduates will show skill in planning, designing and carrying out rigorous research alone and in groups, through to a final report; this is one of the generic intellectual skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop skill in planning, designing and carrying out rigorous research alone and in groups, through to a final report; you are expected to show most, though not necessarily all, of the generic intellectual skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic intellectual skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.32, and do not claim that every graduate must show it. Set it beside 3.38, the field research row 4.8.b13 and qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Bring this up when a student reflects on how they think and argue, or a team maps intellectual skills. Put it plainly, in the second person for a student, and ask: Which part of your research did you plan alone, and which with others? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.32.b5
  forPractitioner: { text: "Graduates will show numeracy and statistical literacy; this is one of the generic intellectual skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop numeracy and statistical literacy; you are expected to show most, though not necessarily all, of the generic intellectual skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic intellectual skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.32, and do not claim that every graduate must show it. Set it beside the analysis row 4.8.b15 and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Bring this up when a student reflects on how they think and argue, or a team maps intellectual skills. Put it plainly, in the second person for a student, and ask: Can you explain what a statistical result in your work means in plain words? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.32.b6
  forPractitioner: { text: "Graduates will show skill in abstracting and synthesising information; this is one of the generic intellectual skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop skill in abstracting and synthesising information; you are expected to show most, though not necessarily all, of the generic intellectual skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic intellectual skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.32, and do not claim that every graduate must show it. Set it beside the synthesis row 4.8.b17 and qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Bring this up when a student reflects on how they think and argue, or a team maps intellectual skills. Put it plainly, in the second person for a student, and ask: Can you sum up a long reading in three points of your own? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.32.b7
  forPractitioner: { text: "Graduates will show skill in building a reasoned argument; this is one of the generic intellectual skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop skill in building a reasoned argument; you are expected to show most, though not necessarily all, of the generic intellectual skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic intellectual skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.32, and do not claim that every graduate must show it. Set it beside the argument row 4.8.b22 and qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Bring this up when a student reflects on how they think and argue, or a team maps intellectual skills. Put it plainly, in the second person for a student, and ask: What is the main claim of your current essay, and what evidence carries it? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.32.b8
  forPractitioner: { text: "Graduates will show responsibility for learning and reflection on that learning; this is one of the generic intellectual skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop responsibility for learning and reflection on that learning; you are expected to show most, though not necessarily all, of the generic intellectual skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic intellectual skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.32, and do not claim that every graduate must show it. Set it beside the reflection row 4.8.b26 and qaa/fheq-2024/4.15.b5."
  author-agent-dialogue: "Bring this up when a student reflects on how they think and argue, or a team maps intellectual skills. Put it plainly, in the second person for a student, and ask: What did you learn from your last piece of feedback, and what did you change? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.33.b1
  forPractitioner: { text: "Graduates will show effective study, autonomous learning and awareness of how learning works; this is one of the generic skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop effective study, autonomous learning and awareness of how learning works; you are expected to show most, though not necessarily all, of the generic skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.33, and do not claim that every graduate must show it. Set it beside the independent study row 4.8.b24 and qaa/fheq-2024/4.15.b9.3."
  author-agent-dialogue: "Bring this up when a student prepares for work or reviews their study skills. Put it plainly, in the second person for a student, and ask: How do you know when you have really understood something? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.33.b2
  forPractitioner: { text: "Graduates will show decision-making, time management and setting priorities among tasks; this is one of the generic skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop decision-making, time management and setting priorities among tasks; you are expected to show most, though not necessarily all, of the generic skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.33, and do not claim that every graduate must show it. Set it beside the row 4.8.b24 and qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Bring this up when a student prepares for work or reviews their study skills. Put it plainly, in the second person for a student, and ask: How did you decide what to do first last week? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.33.b3
  forPractitioner: { text: "Graduates will show skill in keeping and archiving records; this is one of the generic skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop skill in keeping and archiving records; you are expected to show most, though not necessarily all, of the generic skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.33, and do not claim that every graduate must show it. Set it beside 3.27 on reproducibility and qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Bring this up when a student prepares for work or reviews their study skills. Put it plainly, in the second person for a student, and ask: Could someone else follow your field notebook or data folder? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.33.b4
  forPractitioner: { text: "Graduates will show skill in synthesising, placing in context and critically judging information of varied styles and sources; this is one of the generic skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop skill in synthesising, placing in context and critically judging information of varied styles and sources; you are expected to show most, though not necessarily all, of the generic skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.33, and do not claim that every graduate must show it. Set it beside the synthesis row 4.8.b17 and qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Bring this up when a student prepares for work or reviews their study skills. Put it plainly, in the second person for a student, and ask: How did you judge a source that was not academic? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.33.b5
  forPractitioner: { text: "Graduates will show communication in speech, writing and graphics; this is one of the generic skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop communication in speech, writing and graphics; you are expected to show most, though not necessarily all, of the generic skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.33, and do not claim that every graduate must show it. Set it beside the row 4.8.b19 and qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Bring this up when a student prepares for work or reviews their study skills. Put it plainly, in the second person for a student, and ask: Which form of communication do you find hardest, and why? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.33.b6
  forPractitioner: { text: "Graduates will show skill in finding, handling and archiving datasets; this is one of the generic skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop skill in finding, handling and archiving datasets; you are expected to show most, though not necessarily all, of the generic skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.33, and do not claim that every graduate must show it. Set it beside the row 4.8.b23 and qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Bring this up when a student prepares for work or reviews their study skills. Put it plainly, in the second person for a student, and ask: Where did your last data set come from, and how did you store it? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.33.b7
  forPractitioner: { text: "Graduates will show an understanding of intellectual property and data privacy; this is one of the generic skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop an understanding of intellectual property and data privacy; you are expected to show most, though not necessarily all, of the generic skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.33, and do not claim that every graduate must show it. Set it beside 3.27 and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Bring this up when a student prepares for work or reviews their study skills. Put it plainly, in the second person for a student, and ask: Whose permission did you need to use the images or data in your work? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.33.b8
  forPractitioner: { text: "Graduates will show communication with varied audiences in formats that suit them; this is one of the generic skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop communication with varied audiences in formats that suit them; you are expected to show most, though not necessarily all, of the generic skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.33, and do not claim that every graduate must show it. Set it beside the argument row 4.8.b22 and qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Bring this up when a student prepares for work or reviews their study skills. Put it plainly, in the second person for a student, and ask: How would you explain your project to a local council rather than a tutor? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.33.b9
  forPractitioner: { text: "Graduates will show teamwork in groups while recognising and respecting others' viewpoints; this is one of the generic skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop teamwork in groups while recognising and respecting others' viewpoints; you are expected to show most, though not necessarily all, of the generic skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.33, and do not claim that every graduate must show it. Set it beside the group row 4.8.b25, 4.8.b1 and qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Bring this up when a student prepares for work or reviews their study skills. Put it plainly, in the second person for a student, and ask: When did a teammate change your mind? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.33.b10
  forPractitioner: { text: "Graduates will show creative approaches to solving problems; this is one of the generic skills listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop creative approaches to solving problems; you are expected to show most, though not necessarily all, of the generic skills in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of generic skills, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.33, and do not claim that every graduate must show it. Set it beside qaa/fheq-2024/annex-d/cognitive/r4/3rd and qaa/fheq-2024/4.15.b9.2."
  author-agent-dialogue: "Bring this up when a student prepares for work or reviews their study skills. Put it plainly, in the second person for a student, and ask: What unusual approach have you tried on a problem, and did it work? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.34.b1
  forPractitioner: { text: "Graduates will show motivation; this is one of the personal attributes listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop motivation; you are expected to show most, though not necessarily all, of the personal attributes in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of personal attributes, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.34, and do not claim that every graduate must show it. Set it beside the row 4.8.b24 and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Bring this up when a student reflects on personal development or prepares for applications. Put it plainly, in the second person for a student, and ask: What keeps you going when a task is hard? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.34.b2
  forPractitioner: { text: "Graduates will show innovation; this is one of the personal attributes listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop innovation; you are expected to show most, though not necessarily all, of the personal attributes in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of personal attributes, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.34, and do not claim that every graduate must show it. Set it beside qaa/fheq-2024/annex-d/cognitive/r4/3rd."
  author-agent-dialogue: "Bring this up when a student reflects on personal development or prepares for applications. Put it plainly, in the second person for a student, and ask: What have you done differently from the usual way, and why? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.34.b3
  forPractitioner: { text: "Graduates will show an entrepreneurial outlook; this is one of the personal attributes listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop an entrepreneurial outlook; you are expected to show most, though not necessarily all, of the personal attributes in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of personal attributes, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.34, and do not claim that every graduate must show it. Set it beside 1.12 and std:doc:qaa-enterprise-2018-guidance."
  author-agent-dialogue: "Bring this up when a student reflects on personal development or prepares for applications. Put it plainly, in the second person for a student, and ask: Where could your geography skills create value for others, social or economic? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.34.b4
  forPractitioner: { text: "Graduates will show the ability to work responsibly, on your own and with others; this is one of the personal attributes listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop the ability to work responsibly, on your own and with others; you are expected to show most, though not necessarily all, of the personal attributes in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of personal attributes, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.34, and do not claim that every graduate must show it. Set it beside the group row 4.8.b25 and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Bring this up when a student reflects on personal development or prepares for applications. Put it plainly, in the second person for a student, and ask: When did you take responsibility for something that went wrong in a group? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.34.b5
  forPractitioner: { text: "Graduates will show self-awareness, reflection, resilience, self-management and confidence in yourself; this is one of the personal attributes listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop self-awareness, reflection, resilience, self-management and confidence in yourself; you are expected to show most, though not necessarily all, of the personal attributes in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of personal attributes, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.34, and do not claim that every graduate must show it. Set it beside the reflection row 4.8.b26 and qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Bring this up when a student reflects on personal development or prepares for applications. Put it plainly, in the second person for a student, and ask: How did you recover after a setback in your studies? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.34.b6
  forPractitioner: { text: "Graduates will show empathy and insight; this is one of the personal attributes listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop empathy and insight; you are expected to show most, though not necessarily all, of the personal attributes in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of personal attributes, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.34, and do not claim that every graduate must show it. Set it beside 4.8.b1 and 4.8.b3."
  author-agent-dialogue: "Bring this up when a student reflects on personal development or prepares for applications. Put it plainly, in the second person for a student, and ask: How did someone else's experience change how you saw a place? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.34.b7
  forPractitioner: { text: "Graduates will show intellectual integrity and ethical conduct; this is one of the personal attributes listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop intellectual integrity and ethical conduct; you are expected to show most, though not necessarily all, of the personal attributes in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of personal attributes, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.34, and do not claim that every graduate must show it. Set it beside 3.30.b2 and qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Bring this up when a student reflects on personal development or prepares for applications. Put it plainly, in the second person for a student, and ask: How do you make sure your work is honestly your own and fairly uses others'? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.34.b8
  forPractitioner: { text: "Graduates will show a sense of responsibility as a citizen at local, national and international scale, with a global outlook; this is one of the personal attributes listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop a sense of responsibility as a citizen at local, national and international scale, with a global outlook; you are expected to show most, though not necessarily all, of the personal attributes in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of personal attributes, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.34, and do not claim that every graduate must show it. Set it beside 1.10, 3.12 and std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Bring this up when a student reflects on personal development or prepares for applications. Put it plainly, in the second person for a student, and ask: What responsibility do you feel towards a place you have studied? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.34.b9
  forPractitioner: { text: "Graduates will show the skills to keep learning throughout life; this is one of the personal attributes listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop the skills to keep learning throughout life; you are expected to show most, though not necessarily all, of the personal attributes in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of personal attributes, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.34, and do not claim that every graduate must show it. Set it beside qaa/fheq-2024/4.15.b9.3 and spine:6."
  author-agent-dialogue: "Bring this up when a student reflects on personal development or prepares for applications. Put it plainly, in the second person for a student, and ask: What will you need to keep learning after your degree, and how? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.34.b10
  forPractitioner: { text: "Graduates will show flexibility and adaptability; this is one of the personal attributes listed, and graduates are expected to show most of them, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop flexibility and adaptability; you are expected to show most, though not necessarily all, of the personal attributes in this list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one item in a list of personal attributes, most of which graduates are able to show (3.23), so treat it as a broad expectation rather than a rule for each item. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (3.1), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.34, and do not claim that every graduate must show it. Set it beside 3.15 and qaa/fheq-2024/4.15.b9.2."
  author-agent-dialogue: "Bring this up when a student reflects on personal development or prepares for applications. Put it plainly, in the second person for a student, and ask: When did a plan fail in the field, and how did you adapt? Avoid reading the whole list aloud or implying that every item must be mastered."
- statement: qaa/geography-2022/3.39
  forPractitioner: { text: "Use a wide range of teaching and learning styles, fitted to your mission and aims, as a subject spanning environment and society calls for.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a statement about course design", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation (will, \"characteristically\") that honours courses use a wide range of teaching and learning styles. It sets no level. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.39, and do not claim that it prescribes particular methods. Set it beside 3.35 to 3.38 and 3.40."
  author-agent-dialogue: "Bring this up when a team reviews its teaching mix. Put it as a design or planning question for the programme team, and ask: Which styles does the course rely on most? Which learners might that leave behind? Avoid giving it to a student as a duty."
- statement: qaa/geography-2022/3.40
  forPractitioner: { text: "Build an assessment and feedback strategy that lets every student show their attainment and reflect on their progress, with clearly aligned aims and criteria for each method, formative and authentic tasks, self and peer review, and a mix of accessible formats.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design; the student meets it as varied, clearly explained assessment", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation (will) on the course's assessment and feedback strategy. It spans the whole degree. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 3.40, and do not claim that it fixes assessment types or weightings. Set it beside 3.41, 2.1 and the classification descriptions qaa/fheq-2024/annex-d."
  author-agent-dialogue: "Bring this up when a team redesigns assessment or a student asks why formats vary. Put it as a design or planning question for the programme team, and ask: Can every student show what they know in at least one format that suits them? Are criteria clear before the task starts? Avoid presenting it to a student as their obligation."
- statement: qaa/geography-2022/4.1
  forPractitioner: { text: "Treat the threshold cells as the least every student awarded honours will have demonstrated, shown through assessment over the course.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To be awarded an honours degree in geography, you will have shown at least the minimum standards in knowledge, understanding and skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the issuer's definition of the threshold: the least a student will have demonstrated for honours. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same table to integrated master's degrees (4.4). Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.1, and do not claim that the threshold is the expected or typical result, since 4.2 says most do far better. Set it beside 4.2, 4.5, the threshold cells 4.8.b5 to 4.8.b26 and qaa/fheq-2024/annex-d/summary/r1/3rd."
  author-agent-dialogue: "Bring this up when a student asks what they must show to pass, or a team sets pass criteria. Put it in plain words, in the second person to a student and as a course-design point to staff, and ask: Which of the minimum standards are you confident you meet? Where do you need more evidence? Avoid presenting the threshold as the goal, since most students exceed it."
- statement: qaa/geography-2022/4.2
  forPractitioner: { text: "Most of your students will exceed the threshold; decide what evidence shows this, and refer to Annex D of the qualifications frameworks, which describes the four honours classes at FHEQ Level 6 (FQHEIS Level 10).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in setting classification evidence", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) to judge performance above the threshold against Annex D. It concerns honours classification at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.2, and do not claim that the issuer sets marks or class boundaries. Set it beside 4.1, 4.5 to 4.7, std:doc:qaa-fheq-2024-framework Annex D (qaa/fheq-2024/annex-d) and std:ref:uk-assesscriteria."
  author-agent-dialogue: "Bring this up when a team writes classification criteria or marking descriptors. Put it as a design or planning question for the programme team, and ask: How do your criteria for a first differ from those for an upper second? Do they match the Annex D descriptions? Avoid putting it to a student as their duty."
- statement: qaa/geography-2022/4.5
  forPractitioner: { text: "At threshold, graduates hold a basic grasp of environmental and social change, its interrelations, sustainability and the interdependence of places, see the subject largely through what they were taught with little critique, and show competence in the essential skills.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will have a basic grasp of how human and physical environments change and connect, of sustainability and of how places depend on each other, and you will show you can use the essential skills.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the issuer's summary of the threshold rung, the least a graduate shows for the award. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.5, and do not claim that it describes a typical graduate. Set it beside 4.6, 4.7, the threshold cells in 4.8, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/summary/r1/3rd."
  author-agent-dialogue: "Bring this up when a student fears failing or asks what the minimum looks like. Put it plainly, in the second person, as the floor and not the aim, and ask: Can you explain change and sustainability in your own words with an example? Which essential skills could you show evidence for now? Avoid presenting the threshold as what most students achieve."
- statement: qaa/geography-2022/4.6
  forPractitioner: { text: "At the typical level, graduates show critical awareness of geography's scope and methods, consistent command of subject and generic skills, proficiency in most higher-level thinking skills, and critical use of their own perspectives.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you show critical awareness of the subject and its methods, use your skills consistently, and bring your own view to your work critically.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the issuer's summary of the typical rung, described with no modal, which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.6, and do not claim that it is the minimum for the award. Set it beside 4.5, 4.7, the typical cells in 4.8 and qaa/fheq-2024/annex-d/summary/r1/2.2 and r1/2.1."
  author-agent-dialogue: "Bring this up when a student asks what a good degree looks like. Put it plainly, in the second person, and ask: Where in your work do you bring your own perspective critically? Do you use your skills consistently or only sometimes? Avoid presenting the typical rung as the pass standard."
- statement: qaa/geography-2022/4.7
  forPractitioner: { text: "At the excellent level, graduates show superior intellectual skills across broad knowledge, originality and insight, and join theory to practice in research problems, most visibly in dissertations that may come near publishable standard.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you bring originality and insight to wide knowledge, join theory and practice in your research, and may produce independent work, such as a dissertation, close to publishable quality.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the issuer's summary of the excellent rung, described with no modal, an aspiration above the typical. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.7, and do not claim that it is expected of every graduate or that publishable work is required. Set it beside 4.6, the excellent cells in 4.8, qaa/fheq-2024/annex-d/summary/r1/1st and spine:6."
  author-agent-dialogue: "Bring this up when a strong student asks how to reach a first, or a team designs dissertation criteria. Put it plainly, in the second person, and ask: Where does your work go beyond what you were taught? How does your dissertation connect theory and practice? Avoid making a student feel this is the minimum."
- statement: qaa/geography-2022/4.8.b1
  forPractitioner: { text: "Graduates should have developed fair collaboration, empathy and respect for the views, perspectives and needs of others.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should have learned to work fairly with others, with empathy and respect for their views and needs.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an outcome that successful graduates should have developed, listed above the rung table. Hold it at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8 (first bullet), and do not claim that it is graded by rung, since the issuer lists it outside the table. Set it beside the group row 4.8.b25, 1.5, 3.33.b9 and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Bring this up when a student reflects on working with others or a team designs collaborative or reflective tasks. Put it in plain words, in the second person to a student and as a course-design point to staff, and ask: When did you last change your view after listening to someone? How did you make sure everyone in your group was heard? Avoid reading the list aloud or turning it into a checklist of feelings."
- statement: qaa/geography-2022/4.8.b2
  forPractitioner: { text: "Graduates should have developed a critical understanding of the norms and values that shape their own and others' views and actions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should have learned to notice and question the values behind what you and others think and do.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an outcome that successful graduates should have developed, listed above the rung table. Hold it at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8 (second bullet), and do not claim that it is graded by rung, since the issuer lists it outside the table. Set it beside the positionality row 4.8.b21, 1.7 and qaa/fheq-2024/4.15.b4."
  author-agent-dialogue: "Bring this up when a student reflects on working with others or a team designs collaborative or reflective tasks. Put it in plain words, in the second person to a student and as a course-design point to staff, and ask: Which of your own assumptions have you questioned this year? What values sit behind a view you disagree with? Avoid reading the list aloud or turning it into a checklist of feelings."
- statement: qaa/geography-2022/4.8.b3
  forPractitioner: { text: "Graduates should have developed the ability to collaborate with people whose knowledge, views and experience differ from theirs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should have learned to work well with people whose knowledge, views and experience differ from yours.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an outcome that successful graduates should have developed, listed above the rung table. Hold it at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8 (third bullet), and do not claim that it is graded by rung, since the issuer lists it outside the table. Set it beside the group row 4.8.b25, 2.15 and qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Bring this up when a student reflects on working with others or a team designs collaborative or reflective tasks. Put it in plain words, in the second person to a student and as a course-design point to staff, and ask: Who in your last group saw things most differently from you, and what did you gain from that? Avoid reading the list aloud or turning it into a checklist of feelings."
- statement: qaa/geography-2022/4.8.b4
  forPractitioner: { text: "Graduates should have developed an awareness and understanding of the effect of their own and others' emotions and wellbeing.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should have learned to notice how your own and other people's feelings and wellbeing affect you and your work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an outcome that successful graduates should have developed, listed above the rung table. Hold it at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8 (fourth bullet), and do not claim that it is graded by rung, since the issuer lists it outside the table. Set it beside 1.9, 3.34.b5 and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Bring this up when a student reflects on working with others or a team designs collaborative or reflective tasks. Put it in plain words, in the second person to a student and as a course-design point to staff, and ask: How do your feelings about a place or a task affect your work? How do you notice when a teammate is struggling? Avoid reading the list aloud or turning it into a checklist of feelings."
- statement: qaa/geography-2022/4.8.b5
  forPractitioner: { text: "At threshold, every graduate can describe, with examples, how societies and environments change and vary; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to describe, with examples, how societies and environments change and vary.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for change and variability in societies and environments: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b5.typical, 4.8.b5.excellent, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Bring this up when a student revises how societies and environments change, or a team writes outcomes on change. Put it plainly, in the second person to a student or as a design point to staff, and ask: Can you give an example of change in a society or environment and say what drove it? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b5.excellent
  forPractitioner: { text: "At the excellent level, graduates can show critical insight into why and how societies and environments change and vary.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to show critical insight into why and how societies and environments change and vary.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for change and variability in societies and environments, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b5, 4.8.b5.typical, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Bring this up when a student revises how societies and environments change, or a team writes outcomes on change. Put it plainly, in the second person to a student or as a design point to staff, and ask: Can you give an example of change in a society or environment and say what drove it? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b5.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can show a sound grasp of how societies and environments change and vary.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to show a sound grasp of how societies and environments change and vary.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for change and variability in societies and environments, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b5, 4.8.b5.excellent, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r1/2.1 (with .../knowledge/r1/2.2)."
  author-agent-dialogue: "Bring this up when a student revises how societies and environments change, or a team writes outcomes on change. Put it plainly, in the second person to a student or as a design point to staff, and ask: Can you give an example of change in a society or environment and say what drove it? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b6
  forPractitioner: { text: "At threshold, every graduate can describe, with examples, the two-way links between societies and environments across scales of space and time; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to describe, with examples, the two-way links between societies and environments across scales of space and time.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for the two-way relationships between societies and environments: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b6.typical, 4.8.b6.excellent, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Bring this up when a student links human and physical topics. Put it plainly, in the second person to a student or as a design point to staff, and ask: How does the environment you studied shape the people there, and how do they shape it, at more than one scale? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b6.excellent
  forPractitioner: { text: "At the excellent level, graduates can show critical insight into how complex the two-way links between societies and environments are, across scales of space and time.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to show critical insight into how complex the two-way links between societies and environments are, across scales of space and time.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for the two-way relationships between societies and environments, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b6, 4.8.b6.typical, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Bring this up when a student links human and physical topics. Put it plainly, in the second person to a student or as a design point to staff, and ask: How does the environment you studied shape the people there, and how do they shape it, at more than one scale? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b6.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can show a sound grasp of the two-way links between societies and environments across scales of space and time.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to show a sound grasp of the two-way links between societies and environments across scales of space and time.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for the two-way relationships between societies and environments, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b6, 4.8.b6.excellent, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r2/2.1 (with .../knowledge/r2/2.2)."
  author-agent-dialogue: "Bring this up when a student links human and physical topics. Put it plainly, in the second person to a student or as a design point to staff, and ask: How does the environment you studied shape the people there, and how do they shape it, at more than one scale? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b7
  forPractitioner: { text: "At threshold, every graduate can describe ways of approaching sustainability and sustainable development as they bear on how societies and environments interact; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to describe ways of approaching sustainability and sustainable development as you bear on how societies and environments interact.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for sustainability and sustainable development: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b7.typical, 4.8.b7.excellent, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Bring this up when a student discusses sustainability or a team maps education for sustainable development. Put it plainly, in the second person to a student or as a design point to staff, and ask: What does sustainable development mean in a case you know, and who gains or loses from it? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b7.excellent
  forPractitioner: { text: "At the excellent level, graduates can show critical insight into sustainability and sustainable development practice as it bears on how societies and environments interact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to show critical insight into sustainability and sustainable development practice as it bears on how societies and environments interact.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for sustainability and sustainable development, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b7, 4.8.b7.typical, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Bring this up when a student discusses sustainability or a team maps education for sustainable development. Put it plainly, in the second person to a student or as a design point to staff, and ask: What does sustainable development mean in a case you know, and who gains or loses from it? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b7.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can show a sound grasp of sustainability and sustainable development practice as it bears on how societies and environments interact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to show a sound grasp of sustainability and sustainable development practice as it bears on how societies and environments interact.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for sustainability and sustainable development, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b7, 4.8.b7.excellent, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r2/2.1 (with .../knowledge/r2/2.2)."
  author-agent-dialogue: "Bring this up when a student discusses sustainability or a team maps education for sustainable development. Put it plainly, in the second person to a student or as a design point to staff, and ask: What does sustainable development mean in a case you know, and who gains or loses from it? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b8
  forPractitioner: { text: "At threshold, every graduate can describe how geography grew as a discipline, the settings in which its knowledge was and is made, and what that history means now; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to describe how geography grew as a discipline, the settings in which its knowledge was and is made, and what that history means now.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for the history of geography and its making of knowledge: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b8.typical, 4.8.b8.excellent, qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Bring this up when a student studies the history of the discipline or its colonial past. Put it plainly, in the second person to a student or as a design point to staff, and ask: Whose knowledge has geography included and left out, and what follows from that today? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b8.excellent
  forPractitioner: { text: "At the excellent level, graduates can show a critical understanding of the discipline's history, the settings of its knowledge-making then and now, and their present-day consequences.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to show a critical understanding of the discipline's history, the settings of its knowledge-making then and now, and your present-day consequences.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for the history of geography and its making of knowledge, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b8, 4.8.b8.typical, qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Bring this up when a student studies the history of the discipline or its colonial past. Put it plainly, in the second person to a student or as a design point to staff, and ask: Whose knowledge has geography included and left out, and what follows from that today? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b8.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can show a sound grasp of the discipline's history, the settings of its knowledge-making then and now, and their present-day consequences.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to show a sound grasp of the discipline's history, the settings of its knowledge-making then and now, and your present-day consequences.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for the history of geography and its making of knowledge, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b8, 4.8.b8.excellent, qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/annex-d/knowledge/r2/2.1 (with .../knowledge/r2/2.2)."
  author-agent-dialogue: "Bring this up when a student studies the history of the discipline or its colonial past. Put it plainly, in the second person to a student or as a design point to staff, and ask: Whose knowledge has geography included and left out, and what follows from that today? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b9
  forPractitioner: { text: "At threshold, every graduate can describe, with examples, how places differ and depend on one another; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to describe, with examples, how places differ and depend on one another.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for the diversity and interdependence of places: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b9.typical, 4.8.b9.excellent, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Bring this up when a student compares places or scales. Put it plainly, in the second person to a student or as a design point to staff, and ask: How does the place you studied depend on places elsewhere? Why do places differ? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b9.excellent
  forPractitioner: { text: "At the excellent level, graduates can reflect on and judge the reasons why places at different scales differ and depend on one another.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to reflect on and judge the reasons why places at different scales differ and depend on one another.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for the diversity and interdependence of places, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b9, 4.8.b9.typical, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Bring this up when a student compares places or scales. Put it plainly, in the second person to a student or as a design point to staff, and ask: How does the place you studied depend on places elsewhere? Why do places differ? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b9.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can show a sound grasp of how places at different scales differ and depend on one another.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to show a sound grasp of how places at different scales differ and depend on one another.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for the diversity and interdependence of places, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b9, 4.8.b9.excellent, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r1/2.1 (with .../knowledge/r1/2.2)."
  author-agent-dialogue: "Bring this up when a student compares places or scales. Put it plainly, in the second person to a student or as a design point to staff, and ask: How does the place you studied depend on places elsewhere? Why do places differ? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b10
  forPractitioner: { text: "At threshold, every graduate can describe, with examples, the different ways knowledge is produced across the natural sciences, social sciences and humanities; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to describe, with examples, the different ways knowledge is produced across the natural sciences, social sciences and humanities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for ways of producing geographical knowledge: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b10.typical, 4.8.b10.excellent, qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Bring this up when a student meets different research traditions in human and physical geography. Put it plainly, in the second person to a student or as a design point to staff, and ask: How would a natural scientist and a humanities scholar each come to know your topic? What does each approach miss? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b10.excellent
  forPractitioner: { text: "At the excellent level, graduates can critically appraise the different ways knowledge is produced across the natural sciences, social sciences and humanities.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to critically appraise the different ways knowledge is produced across the natural sciences, social sciences and humanities.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for ways of producing geographical knowledge, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b10, 4.8.b10.typical, qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Bring this up when a student meets different research traditions in human and physical geography. Put it plainly, in the second person to a student or as a design point to staff, and ask: How would a natural scientist and a humanities scholar each come to know your topic? What does each approach miss? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b10.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can evaluate the different ways knowledge is produced across the natural sciences, social sciences and humanities.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to evaluate the different ways knowledge is produced across the natural sciences, social sciences and humanities.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for ways of producing geographical knowledge, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b10, 4.8.b10.excellent, qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/annex-d/cognitive/r2/2.1 (with .../cognitive/r2/2.2)."
  author-agent-dialogue: "Bring this up when a student meets different research traditions in human and physical geography. Put it plainly, in the second person to a student or as a design point to staff, and ask: How would a natural scientist and a humanities scholar each come to know your topic? What does each approach miss? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b11
  forPractitioner: { text: "At threshold, every graduate can carry out routine investigations when told how; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to carry out routine investigations when told how.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for applying geographical concepts: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b11.typical, 4.8.b11.excellent, qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Bring this up when a student applies ideas from class to a new case. Put it plainly, in the second person to a student or as a design point to staff, and ask: Can you take a concept from one module and use it to explain a new situation? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b11.excellent
  forPractitioner: { text: "At the excellent level, graduates can apply geographical concepts to varied situations with reflection.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to apply geographical concepts to varied situations with reflection.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for applying geographical concepts, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b11, 4.8.b11.typical, qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/annex-d/cognitive/r3/1st."
  author-agent-dialogue: "Bring this up when a student applies ideas from class to a new case. Put it plainly, in the second person to a student or as a design point to staff, and ask: Can you take a concept from one module and use it to explain a new situation? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b11.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can use their grasp of geographical concepts in varied situations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to use your grasp of geographical concepts in varied situations.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for applying geographical concepts, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b11, 4.8.b11.excellent, qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/annex-d/cognitive/r3/2.1 (with .../cognitive/r3/2.2)."
  author-agent-dialogue: "Bring this up when a student applies ideas from class to a new case. Put it plainly, in the second person to a student or as a design point to staff, and ask: Can you take a concept from one module and use it to explain a new situation? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b12
  forPractitioner: { text: "At threshold, every graduate can tell accuracy apart from precision; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to tell accuracy apart from precision.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for accuracy, precision and uncertainty in data: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b12.typical, 4.8.b12.excellent, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Bring this up when a student handles measurements or questions of data quality. Put it plainly, in the second person to a student or as a design point to staff, and ask: What is the difference between how accurate and how precise your data are? How sure can you be of your result? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b12.excellent
  forPractitioner: { text: "At the excellent level, graduates can reflect critically on how accurate, precise and uncertain research data are.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to reflect critically on how accurate, precise and uncertain research data are.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for accuracy, precision and uncertainty in data, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b12, 4.8.b12.typical, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r4/1st."
  author-agent-dialogue: "Bring this up when a student handles measurements or questions of data quality. Put it plainly, in the second person to a student or as a design point to staff, and ask: What is the difference between how accurate and how precise your data are? How sure can you be of your result? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b12.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can handle accuracy, precision and uncertainty systematically.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to handle accuracy, precision and uncertainty systematically.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for accuracy, precision and uncertainty in data, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, knowledge and understanding, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b12, 4.8.b12.excellent, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r4/2.1 (with .../practical/r4/2.2)."
  author-agent-dialogue: "Bring this up when a student handles measurements or questions of data quality. Put it plainly, in the second person to a student or as a design point to staff, and ask: What is the difference between how accurate and how precise your data are? How sure can you be of your result? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b13
  forPractitioner: { text: "At threshold, every graduate can illustrate the issues that arise in designing and carrying out research in the field; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to illustrate the issues that arise in designing and carrying out research in the field.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for research design and execution in field research: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b13.typical, 4.8.b13.excellent, qaa/fheq-2024/4.15.b6 and qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Bring this up when a student plans fieldwork or a dissertation. Put it plainly, in the second person to a student or as a design point to staff, and ask: What went wrong or nearly wrong in your field research design, and how would you change it? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b13.excellent
  forPractitioner: { text: "At the excellent level, graduates can formulate a thorough, sophisticated analysis of the issues in designing and carrying out field research, with alternative options.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to formulate a thorough, sophisticated analysis of the issues in designing and carrying out field research, with alternative options.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for research design and execution in field research, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b13, 4.8.b13.typical, qaa/fheq-2024/4.15.b6 and qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Bring this up when a student plans fieldwork or a dissertation. Put it plainly, in the second person to a student or as a design point to staff, and ask: What went wrong or nearly wrong in your field research design, and how would you change it? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b13.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can evaluate the issues that arise in designing and carrying out research in the field.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to evaluate the issues that arise in designing and carrying out research in the field.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for research design and execution in field research, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b13, 4.8.b13.excellent, qaa/fheq-2024/4.15.b6 and qaa/fheq-2024/annex-d/practical/r1/2.1 (with .../practical/r1/2.2)."
  author-agent-dialogue: "Bring this up when a student plans fieldwork or a dissertation. Put it plainly, in the second person to a student or as a design point to staff, and ask: What went wrong or nearly wrong in your field research design, and how would you change it? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b14
  forPractitioner: { text: "At threshold, every graduate can illustrate the range of techniques for collecting geographical information, such as instruments, remote sensing, surveys, observation and archives; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to illustrate the range of techniques for collecting geographical information, such as instruments, remote sensing, surveys, observation and archives.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for techniques for collecting geographical information: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b14.typical, 4.8.b14.excellent, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Bring this up when a student chooses data-collection methods. Put it plainly, in the second person to a student or as a design point to staff, and ask: Which collection methods have you used, and why that one for your question? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b14.excellent
  forPractitioner: { text: "At the excellent level, graduates can critically appraise and reflect on their own use of the range of techniques for collecting geographical information.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to critically appraise and reflect on your own use of the range of techniques for collecting geographical information.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for techniques for collecting geographical information, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b14, 4.8.b14.typical, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Bring this up when a student chooses data-collection methods. Put it plainly, in the second person to a student or as a design point to staff, and ask: Which collection methods have you used, and why that one for your question? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b14.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can evaluate the range of techniques for collecting geographical information, such as instruments, remote sensing, surveys, observation and archives.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to evaluate the range of techniques for collecting geographical information, such as instruments, remote sensing, surveys, observation and archives.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for techniques for collecting geographical information, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b14, 4.8.b14.excellent, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r1/2.1 (with .../practical/r1/2.2)."
  author-agent-dialogue: "Bring this up when a student chooses data-collection methods. Put it plainly, in the second person to a student or as a design point to staff, and ask: Which collection methods have you used, and why that one for your question? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b15
  forPractitioner: { text: "At threshold, every graduate can illustrate quantitative and qualitative ways of analysing geographical data and carry out basic applications of them; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to illustrate quantitative and qualitative ways of analysing geographical data and carry out basic applications of them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for quantitative and qualitative analysis: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b15.typical, 4.8.b15.excellent, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Bring this up when a student analyses data. Put it plainly, in the second person to a student or as a design point to staff, and ask: Why did you use numbers, words or both to analyse this? What would the other approach add? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b15.excellent
  forPractitioner: { text: "At the excellent level, graduates can critically appraise and reflect on using quantitative and qualitative analysis, applying a range of approaches with excellence and sophistication.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to critically appraise and reflect on using quantitative and qualitative analysis, applying a range of approaches with excellence and sophistication.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for quantitative and qualitative analysis, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b15, 4.8.b15.typical, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r4/1st."
  author-agent-dialogue: "Bring this up when a student analyses data. Put it plainly, in the second person to a student or as a design point to staff, and ask: Why did you use numbers, words or both to analyse this? What would the other approach add? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b15.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can evaluate quantitative and qualitative ways of analysing geographical data, applying a range of them competently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to evaluate quantitative and qualitative ways of analysing geographical data, applying a range of them competently.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for quantitative and qualitative analysis, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b15, 4.8.b15.excellent, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r4/2.1 (with .../practical/r4/2.2)."
  author-agent-dialogue: "Bring this up when a student analyses data. Put it plainly, in the second person to a student or as a design point to staff, and ask: Why did you use numbers, words or both to analyse this? What would the other approach add? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b16
  forPractitioner: { text: "At threshold, every graduate can illustrate the range of specialised techniques for analysing geographical information, such as spatial analysis, GIS and laboratory methods; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to illustrate the range of specialised techniques for analysing geographical information, such as spatial analysis, GIS and laboratory methods.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for specialised techniques of analysis: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b16.typical, 4.8.b16.excellent, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r3/3rd."
  author-agent-dialogue: "Bring this up when a student learns GIS, laboratory or other specialist analysis. Put it plainly, in the second person to a student or as a design point to staff, and ask: Which specialist technique do you trust most, and how do you know it worked? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b16.excellent
  forPractitioner: { text: "At the excellent level, graduates can show mastery of specialised analytical techniques and very good judgement of how well they work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to show mastery of specialised analytical techniques and very good judgement of how well you work.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for specialised techniques of analysis, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b16, 4.8.b16.typical, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r3/1st."
  author-agent-dialogue: "Bring this up when a student learns GIS, laboratory or other specialist analysis. Put it plainly, in the second person to a student or as a design point to staff, and ask: Which specialist technique do you trust most, and how do you know it worked? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b16.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can evaluate the range of specialised techniques for analysing geographical information, such as spatial analysis, GIS and laboratory methods.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to evaluate the range of specialised techniques for analysing geographical information, such as spatial analysis, GIS and laboratory methods.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for specialised techniques of analysis, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b16, 4.8.b16.excellent, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r3/2.1 (with .../practical/r3/2.2)."
  author-agent-dialogue: "Bring this up when a student learns GIS, laboratory or other specialist analysis. Put it plainly, in the second person to a student or as a design point to staff, and ask: Which specialist technique do you trust most, and how do you know it worked? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b17
  forPractitioner: { text: "At threshold, every graduate can summarise information and data and interpret them accurately; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to summarise information and data and interpret them accurately.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for synthesising and interpreting information: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b17.typical, 4.8.b17.excellent, qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Bring this up when a student writes up results. Put it plainly, in the second person to a student or as a design point to staff, and ask: What does your evidence add up to, and how does it fit what is already known? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b17.excellent
  forPractitioner: { text: "At the excellent level, graduates can bring information and data together and interpret them accurately and with critical reflection in light of current geographical knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to bring information and data together and interpret them accurately and with critical reflection in light of current geographical knowledge.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for synthesising and interpreting information, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b17, 4.8.b17.typical, qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r1/1st."
  author-agent-dialogue: "Bring this up when a student writes up results. Put it plainly, in the second person to a student or as a design point to staff, and ask: What does your evidence add up to, and how does it fit what is already known? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b17.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can bring information and data together and interpret them accurately in light of current geographical knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to bring information and data together and interpret them accurately in light of current geographical knowledge.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for synthesising and interpreting information, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b17, 4.8.b17.excellent, qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r1/2.1 (with .../cognitive/r1/2.2)."
  author-agent-dialogue: "Bring this up when a student writes up results. Put it plainly, in the second person to a student or as a design point to staff, and ask: What does your evidence add up to, and how does it fit what is already known? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b18
  forPractitioner: { text: "At threshold, every graduate can illustrate the range of specialised ways of presenting geographical knowledge, such as GIS, cartography and textual strategies; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to illustrate the range of specialised ways of presenting geographical knowledge, such as GIS, cartography and textual strategies.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for presenting geographical information: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b18.typical, 4.8.b18.excellent, qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Bring this up when a student prepares maps, figures or presentations. Put it plainly, in the second person to a student or as a design point to staff, and ask: Why did you choose this map or format for this audience? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b18.excellent
  forPractitioner: { text: "At the excellent level, graduates can critically evaluate and reflect on how suitably specialised geographical techniques are applied.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to critically evaluate and reflect on how suitably specialised geographical techniques are applied.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for presenting geographical information, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b18, 4.8.b18.typical, qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/practical/r4/1st."
  author-agent-dialogue: "Bring this up when a student prepares maps, figures or presentations. Put it plainly, in the second person to a student or as a design point to staff, and ask: Why did you choose this map or format for this audience? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b18.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can evaluate the range of specialised ways of presenting geographical information, such as GIS, cartography and textual strategies.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to evaluate the range of specialised ways of presenting geographical information, such as GIS, cartography and textual strategies.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for presenting geographical information, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b18, 4.8.b18.excellent, qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/practical/r4/2.1 (with .../practical/r4/2.2)."
  author-agent-dialogue: "Bring this up when a student prepares maps, figures or presentations. Put it plainly, in the second person to a student or as a design point to staff, and ask: Why did you choose this map or format for this audience? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b19
  forPractitioner: { text: "At threshold, every graduate can put across geographical ideas, principles and theories in writing, speech and graphics; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to put across geographical ideas, principles and theories in writing, speech and graphics.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for communicating geographical ideas: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b19.typical, 4.8.b19.excellent, qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Bring this up when a student prepares any written, spoken or visual work. Put it plainly, in the second person to a student or as a design point to staff, and ask: Who is your audience, and how did you adapt your writing, talk or graphics for them? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b19.excellent
  forPractitioner: { text: "At the excellent level, graduates can put across geographical ideas, principles and theories with flair, precision and sophistication in writing, speech and graphics.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to put across geographical ideas, principles and theories with flair, precision and sophistication in writing, speech and graphics.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for communicating geographical ideas, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b19, 4.8.b19.typical, qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Bring this up when a student prepares any written, spoken or visual work. Put it plainly, in the second person to a student or as a design point to staff, and ask: Who is your audience, and how did you adapt your writing, talk or graphics for them? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b19.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can put across geographical ideas, principles and theories well and fluently in writing, speech and graphics.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to put across geographical ideas, principles and theories well and fluently in writing, speech and graphics.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for communicating geographical ideas, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, subject-specific skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b19, 4.8.b19.excellent, qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/transferable/r1/2.1 (with .../transferable/r1/2.2)."
  author-agent-dialogue: "Bring this up when a student prepares any written, spoken or visual work. Put it plainly, in the second person to a student or as a design point to staff, and ask: Who is your audience, and how did you adapt your writing, talk or graphics for them? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b20
  forPractitioner: { text: "At threshold, every graduate can express their own views on geographical issues; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to express your own views on geographical issues.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for views on geographical issues: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b20.typical, 4.8.b20.excellent, qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Bring this up when a student discusses a contested issue. Put it plainly, in the second person to a student or as a design point to staff, and ask: What do you think about this issue, and what would someone who disagrees say? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b20.excellent
  forPractitioner: { text: "At the excellent level, graduates can reflect critically on a range of views on geographical issues and reach a reasoned judgement.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to reflect critically on a range of views on geographical issues and reach a reasoned judgement.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for views on geographical issues, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b20, 4.8.b20.typical, qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Bring this up when a student discusses a contested issue. Put it plainly, in the second person to a student or as a design point to staff, and ask: What do you think about this issue, and what would someone who disagrees say? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b20.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can express and compare differing views on geographical issues.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to express and compare differing views on geographical issues.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for views on geographical issues, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b20, 4.8.b20.excellent, qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r2/2.1 (with .../cognitive/r2/2.2)."
  author-agent-dialogue: "Bring this up when a student discusses a contested issue. Put it plainly, in the second person to a student or as a design point to staff, and ask: What do you think about this issue, and what would someone who disagrees say? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b21
  forPractitioner: { text: "At threshold, every graduate can show awareness of their own positionality and assumptions and of what these may lead to; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to show awareness of your own positionality and assumptions and of what these may lead to.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for positionality and assumptions: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b21.typical, 4.8.b21.excellent, qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Bring this up when a student reflects on fieldwork, research ethics or their own viewpoint. Put it plainly, in the second person to a student or as a design point to staff, and ask: How might your own background shape what you noticed or concluded? What follows from that? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b21.excellent
  forPractitioner: { text: "At the excellent level, graduates can recognise their positionality and assumptions and critically evaluate what these may lead to.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to recognise your positionality and assumptions and critically evaluate what these may lead to.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for positionality and assumptions, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b21, 4.8.b21.typical, qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/annex-d/transferable/r5/1st."
  author-agent-dialogue: "Bring this up when a student reflects on fieldwork, research ethics or their own viewpoint. Put it plainly, in the second person to a student or as a design point to staff, and ask: How might your own background shape what you noticed or concluded? What follows from that? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b21.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can recognise their positionality and assumptions and evaluate what these may lead to.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to recognise your positionality and assumptions and evaluate what these may lead to.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for positionality and assumptions, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b21, 4.8.b21.excellent, qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/annex-d/transferable/r5/2.1 (with .../transferable/r5/2.2)."
  author-agent-dialogue: "Bring this up when a student reflects on fieldwork, research ethics or their own viewpoint. Put it plainly, in the second person to a student or as a design point to staff, and ask: How might your own background shape what you noticed or concluded? What follows from that? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b22
  forPractitioner: { text: "At threshold, every graduate can present material in support of a reasoned argument; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to present material in support of a reasoned argument.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for reasoned argument: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b22.typical, 4.8.b22.excellent, qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Bring this up when a student plans an essay or presentation. Put it plainly, in the second person to a student or as a design point to staff, and ask: What is your main claim, and which evidence carries it? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b22.excellent
  forPractitioner: { text: "At the excellent level, graduates can draw complex information together to put a reasoned argument to specialists and non-specialists alike.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to draw complex information together to put a reasoned argument to specialists and non-specialists alike.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for reasoned argument, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b22, 4.8.b22.typical, qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Bring this up when a student plans an essay or presentation. Put it plainly, in the second person to a student or as a design point to staff, and ask: What is your main claim, and which evidence carries it? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b22.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can draw material together suitably to put a reasoned argument to its intended audience.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to draw material together suitably to put a reasoned argument to its intended audience.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for reasoned argument, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b22, 4.8.b22.excellent, qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/annex-d/cognitive/r2/2.1 (with .../cognitive/r2/2.2)."
  author-agent-dialogue: "Bring this up when a student plans an essay or presentation. Put it plainly, in the second person to a student or as a design point to staff, and ask: What is your main claim, and which evidence carries it? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b23
  forPractitioner: { text: "At threshold, every graduate can use communication technologies and ICT to select, analyse, present and share geographical information; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to use communication technologies and ICT to select, analyse, present and share geographical information.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for communications technology and ICT: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b23.typical, 4.8.b23.excellent, qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Bring this up when a student uses digital tools for analysis or presentation. Put it plainly, in the second person to a student or as a design point to staff, and ask: Which digital tools do you use to analyse and present information, and how well do they serve you? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b23.excellent
  forPractitioner: { text: "At the excellent level, graduates can use communication technologies and ICT highly competently to select, analyse, present and share geographical information.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to use communication technologies and ICT highly competently to select, analyse, present and share geographical information.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for communications technology and ICT, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b23, 4.8.b23.typical, qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Bring this up when a student uses digital tools for analysis or presentation. Put it plainly, in the second person to a student or as a design point to staff, and ask: Which digital tools do you use to analyse and present information, and how well do they serve you? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b23.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can use communication technologies and ICT well and suitably to select, analyse, present and share geographical information.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to use communication technologies and ICT well and suitably to select, analyse, present and share geographical information.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for communications technology and ICT, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b23, 4.8.b23.excellent, qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/transferable/r1/2.1 (with .../transferable/r1/2.2)."
  author-agent-dialogue: "Bring this up when a student uses digital tools for analysis or presentation. Put it plainly, in the second person to a student or as a design point to staff, and ask: Which digital tools do you use to analyse and present information, and how well do they serve you? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b24
  forPractitioner: { text: "At threshold, every graduate can study independently and manage their time within a supportive structure; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to study independently and manage your time within a supportive structure.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for independent study and time management: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b24.typical, 4.8.b24.excellent, qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Bring this up when a student struggles with deadlines or plans independent work. Put it plainly, in the second person to a student or as a design point to staff, and ask: How do you plan a week of independent study? What support do you still lean on? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b24.excellent
  forPractitioner: { text: "At the excellent level, graduates can study with high autonomy and good organisation, managing their time to attain consistently, proficiently and steadily.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to study with high autonomy and good organisation, managing your time to attain consistently, proficiently and steadily.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for independent study and time management, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b24, 4.8.b24.typical, qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Bring this up when a student struggles with deadlines or plans independent work. Put it plainly, in the second person to a student or as a design point to staff, and ask: How do you plan a week of independent study? What support do you still lean on? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b24.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can study independently and manage their time so as to attain consistently, proficiently and steadily.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to study independently and manage your time so as to attain consistently, proficiently and steadily.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for independent study and time management, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b24, 4.8.b24.excellent, qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/transferable/r3/2.1 (with .../transferable/r3/2.2)."
  author-agent-dialogue: "Bring this up when a student struggles with deadlines or plans independent work. Put it plainly, in the second person to a student or as a design point to staff, and ask: How do you plan a week of independent study? What support do you still lean on? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b25
  forPractitioner: { text: "At threshold, every graduate can carry out tasks given to them in a group and join in its discussions; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to carry out tasks given to you in a group and join in its discussions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for group work and leadership: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b25.typical, 4.8.b25.excellent, qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Bring this up when a student does group work. Put it plainly, in the second person to a student or as a design point to staff, and ask: What role did you take in your last group, and what did the group achieve because of you? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b25.excellent
  forPractitioner: { text: "At the excellent level, graduates can lead a group and support others' participation so that it meets its aims.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to lead a group and support others' participation so that it meets its aims.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for group work and leadership, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b25, 4.8.b25.typical, qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/annex-d/transferable/r2/1st."
  author-agent-dialogue: "Bring this up when a student does group work. Put it plainly, in the second person to a student or as a design point to staff, and ask: What role did you take in your last group, and what did the group achieve because of you? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b25.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can work as a member or leader of a group and help it meet its aims.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to work as a member or leader of a group and help it meet its aims.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for group work and leadership, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b25, 4.8.b25.excellent, qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/annex-d/transferable/r2/2.1 (with .../transferable/r2/2.2)."
  author-agent-dialogue: "Bring this up when a student does group work. Put it plainly, in the second person to a student or as a design point to staff, and ask: What role did you take in your last group, and what did the group achieve because of you? Do not read the table aloud, and never present this typical level as the pass mark."
- statement: qaa/geography-2022/4.8.b26
  forPractitioner: { text: "At threshold, every graduate can describe how they learn and give a basic account of their own strengths and weaknesses; this is the floor for honours and integrated master's alike.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your degree, you will be able to describe how you learn and give a basic account of your own strengths and weaknesses.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as the threshold standard for reflecting on one's own learning: the least a Geography graduate shows for the award, not a typical result. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, threshold column, and do not call it a regulatory requirement. Set it beside 4.8.b26.typical, 4.8.b26.excellent, qaa/fheq-2024/4.15.b9.3 and qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Bring this up when a student reflects on feedback or plans their development. Put it plainly, in the second person to a student or as a design point to staff, and ask: What are your strongest and weakest skills, and what will you do differently next time? Do not read the table aloud, and make clear this is the floor, not the aim."
- statement: qaa/geography-2022/4.8.b26.excellent
  forPractitioner: { text: "At the excellent level, graduates can reflect critically on how they learn, weighing their strengths and weaknesses and showing they understand other strategies.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will be able to reflect critically on how you learn, weighing your strengths and weaknesses and showing you understand other strategies.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the excellent standard for reflecting on one's own learning, an aspiration the issuer describes above the typical, not a requirement. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, excellent column, and do not call it a regulatory requirement. Set it beside 4.8.b26, 4.8.b26.typical, qaa/fheq-2024/4.15.b9.3 and qaa/fheq-2024/annex-d/transferable/r5/1st."
  author-agent-dialogue: "Bring this up when a student reflects on feedback or plans their development. Put it plainly, in the second person to a student or as a design point to staff, and ask: What are your strongest and weakest skills, and what will you do differently next time? Do not read the table aloud, and never present this excellent level as the minimum."
- statement: qaa/geography-2022/4.8.b26.typical
  forPractitioner: { text: "At the typical level, which most graduates reach, graduates can analyse how they learn and evaluate their own strengths and weaknesses.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical level, which most students reach, you will be able to analyse how you learn and evaluate your own strengths and weaknesses.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the typical standard for reflecting on one's own learning, which the issuer describes without a modal and which most graduates reach above the threshold. Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's degrees (4.4), so do not present it as a separate Level 7 standard. Cite it as QAA, 2022, Geography Subject Benchmark Statement, para 4.8, table, generic skills, typical column, and do not call it a regulatory requirement. Set it beside 4.8.b26, 4.8.b26.excellent, qaa/fheq-2024/4.15.b9.3 and qaa/fheq-2024/annex-d/transferable/r5/2.1 (with .../transferable/r5/2.2)."
  author-agent-dialogue: "Bring this up when a student reflects on feedback or plans their development. Put it plainly, in the second person to a student or as a design point to staff, and ask: What are your strongest and weakest skills, and what will you do differently next time? Do not read the table aloud, and never present this typical level as the pass mark."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 4.2 (Annex D for FHEQ Level 6)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 4.2 (Annex D for FQHEIS Level 10)" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.10 (integrated master's)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.10 (integrated master's)" }
  - { id: "spine:6", role: "inferred", locator: "std:ref:uk-framework R2: the honours award and the table's level (Part E)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 4.2: Annex D for FHEQ Level 6 and FQHEIS Level 10 degrees)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.10: integrated master's at FHEQ Level 7, FQHEIS Level 11)" }
  - { from: "fheq:6", to: "spine:6", relation: "levelEquivalent", basis: "inferred from std:ref:uk-framework R2 (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.5", "1.6", "1.7", "1.8", "1.9", "2.3", "2.5", "2.6", "2.15", "3.8", "3.19"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["2.3", "2.4", "2.5", "2.6", "2.11", "2.13", "3.19", "3.40"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.10", "3.2", "3.6", "3.12", "3.20", "4.5", "4.8"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.11", "1.12", "2.14", "3.34"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-geography-2019-benchmarks (fourth edition, 2019; not held)", note: "edition history in the back matter, section 6" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 (4.2; section 5)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS Levels 10 and 11 (2.10, 4.2)" }
- { rel: "themeReference", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "three ESD principles taken from it (1.10; section 5)" }
- { rel: "themeReference", target: "std:doc:qaa-enterprise-2018-guidance", note: "the deeper generic analysis of enterprise (1.12; section 5)" }
- { rel: "refersTo", target: "Royal Geographical Society (with IBG): Chartered Geographer and programme accreditation (not yet ingested)", note: "2.18; section 5 (Part E)" }
- { rel: "refersTo", target: "Equality Act 2010", note: "protected characteristics (1.5)" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance; QAA Glossary", note: "front matter" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2022-03"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "advisory group of 2022 named; thanks to the Disabled Students' Commission and two named contributors (D1, section 6)"
replacedBy: "none"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- Geography studies how societies and environments shape each other, through the lenses of scale, place, space and time (D1, 1.1)
- It is at once a STEM and a SHAPE subject, joining natural and social sciences with arts and humanities, and courses run as BA, BSc, Scottish MA and integrated master's (D1, 1.2; 1.3)
- It values plural ways of knowing, qualitative and quantitative, and rests on fieldwork, laboratory work, spatial data analysis, modelling, GIS and remote sensing (D1, 1.4)
- It sees itself as an inclusive learning community that must face its colonial origins and carry values of care and solidarity through the whole curriculum (D1, 1.5 to 1.8)
- Fieldwork, in an expansive sense of the field from landscapes to archives and digital spaces, is required throughout the degree (D1, 3.13 to 3.15)
- Geocapabilities, the subject's own capabilities of thinking spatially and holistically about place, society and environment, grow as students progress (D1, 3.22)

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "A collective duty to embed equity and inclusion, framed by the discipline's colonial past; carried into curriculum values, critical theory and inclusive fieldwork and partnerships (D1, 1.5 to 1.9; 2.6; 2.15; 3.19)"
  statements: ["qaa/geography-2022/1.5", "qaa/geography-2022/1.6", "qaa/geography-2022/1.7", "qaa/geography-2022/1.8", "qaa/geography-2022/2.6", "qaa/geography-2022/2.15", "qaa/geography-2022/3.19", "qaa/geography-2022/4.8.b1", "qaa/geography-2022/4.8.b3"]
- theme: theme:accessibility
  inThisSubject: "Inclusive design across teaching, assessment and above all fieldwork, with affordable trips, flexible delivery and allowance for unequal access to technology (D1, 2.3 to 2.6; 2.11 to 2.13; 3.19; 3.40)"
  statements: ["qaa/geography-2022/2.6", "qaa/geography-2022/2.13", "qaa/geography-2022/3.19", "qaa/geography-2022/3.40"]
- theme: theme:esd
  inThisSubject: "Sustainable development is core content and a rung row; fieldwork carries a carbon audit; three principles from the ESD guidance shape teaching (D1, 1.10; 3.20; 4.5; 4.8)"
  statements: ["qaa/geography-2022/3.20", "qaa/geography-2022/4.5", "qaa/geography-2022/4.8.b7", "qaa/geography-2022/4.8.b7.typical", "qaa/geography-2022/4.8.b7.excellent", "qaa/geography-2022/3.34.b8"]
- theme: theme:enterprise
  inThisSubject: "Employability, entrepreneurship and enterprise read broadly: data and spatial skills for decisions, and social, green and digital enterprise valued beside economic surplus (D1, 1.11; 1.12; 2.14; 3.34)"
  statements: ["qaa/geography-2022/1.12", "qaa/geography-2022/3.34.b3"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.2", gloss: "the discipline as a whole and its four strands of concepts" }
  - { component: "3.3", gloss: "spatial distribution and change across scales" }
  - { component: "3.4", gloss: "place and how it is made" }
  - { component: "3.5", gloss: "systems and human-environment interaction" }
  - { component: "3.6", gloss: "human patterns and processes; development and sustainability" }
  - { component: "3.7", gloss: "physical environmental change" }
  - { component: "3.8", gloss: "history of the discipline and decolonial practice" }
  - { component: "3.9", gloss: "representation and mapping" }
  - { component: "3.10", gloss: "research design and methodologies" }
  - { component: "3.11", gloss: "GISci, GIS, remote sensing and statistics" }
  - { component: "3.12", gloss: "global and local issues and applied problem-solving" }
practices:
  - { component: "3.13", kind: "learning", gloss: "fieldwork as experiential learning in every course" }
  - { component: "3.14", kind: "learning", gloss: "access to many kinds of field" }
  - { component: "3.15", kind: "teaching", gloss: "fieldwork through the whole degree" }
  - { component: "3.16", kind: "learning", gloss: "field data collection and laboratory analysis" }
  - { component: "3.17", kind: "teaching", gloss: "virtual fieldwork" }
  - { component: "3.18", kind: "teaching", gloss: "ethics and risk assessment of fieldwork" }
  - { component: "3.19", kind: "teaching", gloss: "inclusive fieldwork and inclusivity assessment" }
  - { component: "3.20", kind: "teaching", gloss: "carbon audit of fieldwork" }
  - { component: "3.21", kind: "teaching", gloss: "staffing fieldwork" }
  - { component: "3.35", kind: "teaching", gloss: "innovative teaching contexts" }
  - { component: "3.36", kind: "teaching", gloss: "range of teaching approaches" }
  - { component: "3.37", kind: "learning", gloss: "roles of experiential learning" }
  - { component: "3.38", kind: "learning", gloss: "independent research and the dissertation" }
  - { component: "3.39", kind: "teaching", gloss: "a wide mix of styles" }
  - { component: "3.40", kind: "assessment", gloss: "assessment and feedback strategy" }
  - { component: "3.41", kind: "assessment", gloss: "assessment methods students meet" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.8", award: "bachelor's with honours; integrated master's", items: 23 }
  - { rung: "typical", leadIn: "4.8", award: "bachelor's with honours; integrated master's", items: 23 }
  - { rung: "excellent", leadIn: "4.8", award: "bachelor's with honours; integrated master's", items: 23 }
rungBases: "One table at 4.8, flattened in the held text, lists each of 22 outcomes once under three columns headed Threshold, Typical and Excellent, in three blocks (knowledge and understanding 8, subject-specific skills 7, generic skills 7); 4.4 introduces it for honours and integrated master's alike; 4.5 to 4.7 summarise each rung in prose and are recorded as one record per rung. Threshold is the minimum for the award (4.1); typical and excellent carry no modal (describes)."
outcomeLists:
  - { leadIn: "4.8", gloss: "what successful graduates should have developed, above the table", items: 4, award: ["bachelor's with honours", "integrated master's"] }
  - { leadIn: "3.30", gloss: "subject-specific skills, most of which graduates show (3.23)", items: 11, award: ["bachelor's with honours", "integrated master's"] }
  - { leadIn: "3.32", gloss: "generic intellectual skills (3.23)", items: 8, award: ["bachelor's with honours", "integrated master's"] }
  - { leadIn: "3.33", gloss: "generic skills (3.23)", items: 10, award: ["bachelor's with honours", "integrated master's"] }
  - { leadIn: "3.34", gloss: "personal attributes (3.23)", items: 10, award: ["bachelor's with honours", "integrated master's"] }
outcomes:
  - { outcome: "overall rung profile", threshold: "qaa/geography-2022/4.5", typical: "qaa/geography-2022/4.6", excellent: "qaa/geography-2022/4.7", basis: "stated", domain: "understanding", award: "bachelor's with honours; integrated master's" }
  - { outcome: "change and variability in societies and environments", threshold: "qaa/geography-2022/4.8.b5", typical: "qaa/geography-2022/4.8.b5.typical", excellent: "qaa/geography-2022/4.8.b5.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours; integrated master's" }
  - { outcome: "the two-way relationships between societies and environments", threshold: "qaa/geography-2022/4.8.b6", typical: "qaa/geography-2022/4.8.b6.typical", excellent: "qaa/geography-2022/4.8.b6.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours; integrated master's" }
  - { outcome: "sustainability and sustainable development", threshold: "qaa/geography-2022/4.8.b7", typical: "qaa/geography-2022/4.8.b7.typical", excellent: "qaa/geography-2022/4.8.b7.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours; integrated master's" }
  - { outcome: "the history of geography and its making of knowledge", threshold: "qaa/geography-2022/4.8.b8", typical: "qaa/geography-2022/4.8.b8.typical", excellent: "qaa/geography-2022/4.8.b8.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours; integrated master's" }
  - { outcome: "the diversity and interdependence of places", threshold: "qaa/geography-2022/4.8.b9", typical: "qaa/geography-2022/4.8.b9.typical", excellent: "qaa/geography-2022/4.8.b9.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours; integrated master's" }
  - { outcome: "ways of producing geographical knowledge", threshold: "qaa/geography-2022/4.8.b10", typical: "qaa/geography-2022/4.8.b10.typical", excellent: "qaa/geography-2022/4.8.b10.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours; integrated master's" }
  - { outcome: "applying geographical concepts", threshold: "qaa/geography-2022/4.8.b11", typical: "qaa/geography-2022/4.8.b11.typical", excellent: "qaa/geography-2022/4.8.b11.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours; integrated master's" }
  - { outcome: "accuracy, precision and uncertainty in data", threshold: "qaa/geography-2022/4.8.b12", typical: "qaa/geography-2022/4.8.b12.typical", excellent: "qaa/geography-2022/4.8.b12.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours; integrated master's" }
  - { outcome: "research design and execution in field research", threshold: "qaa/geography-2022/4.8.b13", typical: "qaa/geography-2022/4.8.b13.typical", excellent: "qaa/geography-2022/4.8.b13.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours; integrated master's" }
  - { outcome: "techniques for collecting geographical information", threshold: "qaa/geography-2022/4.8.b14", typical: "qaa/geography-2022/4.8.b14.typical", excellent: "qaa/geography-2022/4.8.b14.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours; integrated master's" }
  - { outcome: "quantitative and qualitative analysis", threshold: "qaa/geography-2022/4.8.b15", typical: "qaa/geography-2022/4.8.b15.typical", excellent: "qaa/geography-2022/4.8.b15.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours; integrated master's" }
  - { outcome: "specialised techniques of analysis", threshold: "qaa/geography-2022/4.8.b16", typical: "qaa/geography-2022/4.8.b16.typical", excellent: "qaa/geography-2022/4.8.b16.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours; integrated master's" }
  - { outcome: "synthesising and interpreting information", threshold: "qaa/geography-2022/4.8.b17", typical: "qaa/geography-2022/4.8.b17.typical", excellent: "qaa/geography-2022/4.8.b17.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours; integrated master's" }
  - { outcome: "presenting geographical information", threshold: "qaa/geography-2022/4.8.b18", typical: "qaa/geography-2022/4.8.b18.typical", excellent: "qaa/geography-2022/4.8.b18.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours; integrated master's" }
  - { outcome: "communicating geographical ideas", threshold: "qaa/geography-2022/4.8.b19", typical: "qaa/geography-2022/4.8.b19.typical", excellent: "qaa/geography-2022/4.8.b19.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours; integrated master's" }
  - { outcome: "views on geographical issues", threshold: "qaa/geography-2022/4.8.b20", typical: "qaa/geography-2022/4.8.b20.typical", excellent: "qaa/geography-2022/4.8.b20.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours; integrated master's" }
  - { outcome: "positionality and assumptions", threshold: "qaa/geography-2022/4.8.b21", typical: "qaa/geography-2022/4.8.b21.typical", excellent: "qaa/geography-2022/4.8.b21.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours; integrated master's" }
  - { outcome: "reasoned argument", threshold: "qaa/geography-2022/4.8.b22", typical: "qaa/geography-2022/4.8.b22.typical", excellent: "qaa/geography-2022/4.8.b22.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours; integrated master's" }
  - { outcome: "communications technology and ICT", threshold: "qaa/geography-2022/4.8.b23", typical: "qaa/geography-2022/4.8.b23.typical", excellent: "qaa/geography-2022/4.8.b23.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours; integrated master's" }
  - { outcome: "independent study and time management", threshold: "qaa/geography-2022/4.8.b24", typical: "qaa/geography-2022/4.8.b24.typical", excellent: "qaa/geography-2022/4.8.b24.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours; integrated master's" }
  - { outcome: "group work and leadership", threshold: "qaa/geography-2022/4.8.b25", typical: "qaa/geography-2022/4.8.b25.typical", excellent: "qaa/geography-2022/4.8.b25.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours; integrated master's" }
  - { outcome: "reflecting on one's own learning", threshold: "qaa/geography-2022/4.8.b26", typical: "qaa/geography-2022/4.8.b26.typical", excellent: "qaa/geography-2022/4.8.b26.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours; integrated master's" }
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
- { body: "Royal Geographical Society (with the Institute of British Geographers)", says: "a learned society institutions can work with, supporting understanding of careers and routes to accreditation, including its Chartered Geographer status (D1, 2.18); the back matter adds its voluntary programme accreditation scheme, aligned with the statement (D1, section 5)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equity, equality, diversity and inclusion", carriedIn: ["1.5", "1.6", "1.7", "1.8", "1.9", "2.3", "2.5", "2.6", "2.15", "3.8", "3.19"], statements: ["1.5", "1.6", "1.7", "1.8", "2.6", "2.15", "3.19", "4.8.b1", "4.8.b3"] }
  - { id: "theme:accessibility", named: "Accessibility", carriedIn: ["2.3", "2.4", "2.5", "2.6", "2.11", "2.13", "3.19", "3.40"], statements: ["2.6", "2.13", "3.19", "3.40"] }
  - { id: "theme:esd", named: "Sustainability; Education for Sustainable Development (ESD)", carriedIn: ["1.10", "3.2", "3.6", "3.12", "3.20", "4.5", "4.8"], statements: ["3.20", "4.5", "4.8.b7", "4.8.b7.typical", "4.8.b7.excellent"] }
  - { id: "theme:enterprise", named: "Entrepreneurship and enterprise education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.11", "1.12", "2.14", "3.34"], statements: ["1.12", "3.34.b3"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.10", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.10", "4.2"] }
bodies:
  - { body: "Royal Geographical Society (with the Institute of British Geographers)", citedIn: ["2.18"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "the descriptions of the four honours classes, for performance above the threshold" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Advance HE and QAA's Education for Sustainable Development (ESD) Guidance", citedIn: ["1.10"], role: "source of the three ESD principles for geography" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers", citedIn: ["1.12"], role: "the deeper generic analysis of enterprise education" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "geocapabilities", definition: "the subject's own capabilities: grasping the weight of place, space, scale, landscape and nature in life on Earth, thinking spatially, seeing how society and environment shape each other, and thinking holistically and critically (D1, 3.22)", beneficiaryDefinition: "the ways of thinking that geography builds in you: spatially, about places, and about people and environments together", scopeNote: "cited to Walkington and others (2018) in the back matter", category: "unknown", practices: ["geography"] }
- { slug: "reproducibility", definition: "being able to repeat results and the inferences drawn from them (D1, 3.27)", beneficiaryDefinition: "whether someone else could get the same results and conclusions from your work", scopeNote: "named with openness and transparency in spatial data analysis", category: "unknown", practices: ["geography"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "geocapabilities", form: "geocapabilities", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "reproducibility", form: "reproducibility", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement: Geography"
  edition: "March 2022 (fifth edition)"
  year: 2022
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/geography-2022/geography-2022.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: c19bcde6392a92c322294fbd4a0d50c50206840eebc546fe98395c3c7e2e9488
  heldFiles: ["wkspc2601-library/txt/qaa-2022-geography-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2022-geography-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2022-geography-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2022-geography-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0063", source: "Royal Geographical Society (with IBG): programme accreditation criteria and Chartered Geographer requirements", why: "SB5 requirements; S7" }
- { w: "W-std-0064", source: "QAA Subject Benchmark Statement: Geography, fourth edition (2019)", why: "S7 supersedes; edition comparison" }
```

## Part E Gaps and questions
- Rung shape: one table (4.8) listing each outcome once under Threshold, Typical and Excellent columns, flattened in the held text in three blocks; recorded as one record per rung on each cell (batch 1 convention), ids 4.8.b5 to 4.8.b26 with .typical and .excellent. Unlike Psychology (separate lists per rung).
- Rung prose: 4.5, 4.6 and 4.7 summarise the threshold, typical and excellent graduate; recorded as rung records with gradeOf stated (4.6 "distinguished from the threshold level"; 4.7 "beyond the typical standard"). Their domain is set to understanding for want of a mixed value: P3 to confirm.
- Force: threshold cells take "threshold" from 4.1 (the minimum a student will have demonstrated for honours). The table lead-in (4.4, "expresses performance") has no modal, so typical and excellent cells and 4.6 and 4.7 are `describes` (forceFrom 4.4). For Abbott: confirm.
- Table cells split by page breaks, spans cut at the head only: 4.8.b9.typical and 4.8.b9.excellent (tail "places at various spatial scales." after page 20) and 4.8.b15.typical and 4.8.b15.excellent (tails "in the application of a range of these approaches." and "sophisticated application of a range of these approaches." after page 21). P3 to check the placement of the two tails.
- Row placements in the flattened table read by content and order; none uncertain apart from the split cells above. Row 4.8.b11 pairs "carry out routine investigations as instructed" (threshold) with applying concepts (typical, excellent): the issuer pairs them in one row, so gradeOf is stated, but the content match is loose.
- Award: the table is stated for "a bachelor's degree with honours or integrated master's degree" (4.4) with no separate master's column; records carry both awards at fheq:6. The integrated master's level (fheq:7, fqheis:11, from 2.10) has no wording of its own.
- Outcome lists 3.30 and 3.32 to 3.34 are recorded as statements: 3.23 says graduates "are able to demonstrate competence in most of" the skills and attributes itemised, so each item carries force will (forceFrom 3.23) with the "most of" qualifier in every version. P3 to confirm they count as an outcome list (lead-ins say "include").
- 3.23 itself, the lead-in for those lists, is not cut as a separate record. 4.8.b4 is cut with find: the skeleton span ran into the whole table.
- Not cut, plain-present learner descriptions: 3.2 (its four bullets, "appreciate the geographical meanings") and 3.4, 3.6 to 3.12, 3.22, 3.25, 3.27 to 3.29 ("Geographers understand / are aware / are skilled"). They state what geographers know but have no modal; P3 to decide (open point 5).
- Not cut, plain-present provider norms: 2.2 ("Course design normally includes"), 2.3, 2.4, 2.11, 2.12, 3.1 ("It is anticipated that single honours degree courses ... address"), 3.13 ("Fieldwork is integral to all Geography courses"), 3.36, 3.38 ("it is anticipated that some form of independent research work is supported").
- Obliging words outside the five: "need to" and "responsibility and duty" (1.5, recorded will from "will need to"); "responsible for" and "need to" (2.6, recorded should); "require access" (2.6, 3.14, 3.16, 3.29: needs of resources, not cut); "requires" (3.8 "A geographical education requires that learners examine their own place in the world"; 3.38 "learning requires critical reflection": not cut, for Abbott); "required" (3.15, recorded must); "need to" (3.6, "needs to be an integral part", not cut); "is essential" (2.20, 3.29).
- 3.21 holds should (resourcing) and must (employers recognising staff capacity) in one paragraph; recorded must, both kept in the versions.
- 2.21 ("external examiners will be asked to comment") describes typical practice ("Typically"); not cut.
- Themes: the front matter names "employability, entrepreneurship and enterprise education" as one cross-cutting theme; recorded under theme:enterprise with 2.14 (employability) in carriedIn. A separate theme:employability id would be new: for Abbott.
- Frameworks: FHEQ and FQHEIS (SCQF) cited at 2.10 and 4.2. No CQFW citation; the front matter names the Quality Assessment Framework for Wales and the Quality Enhancement Framework in Scotland, quality regimes not qualification frameworks.
- Bodies and organisations: RGS-IBG (2.18; section 5). Advance HE appears only as co-author of the ESD guidance (1.10). Office for Students and the Disabled Students' Commission appear only in excluded matter. The PSRBs and learned societies named generically in the front matter are not bodies.
- Inferred: subjects codes hecos 100409 geography and cah CAH26-01-01 (the text names the subject, not the codes); statedSubjects physical and human geography codes 100410 and 100478. P3 to confirm.
- Inferred: spine:6 and the fheq:6 to spine:6 crosswalk, from std:ref:uk-framework R2.
- Framework pointers in each author-agent-written instruction (qaa/fheq-2024/4.15.*, Annex D bands) are our reading of the nearest descriptor; typical cells are set beside both the 2.2 and 2.1 bands. P3 to check.
- Educational aside: the issuer cites Walkington and others (2018) on geocapabilities (back matter): pedagogy named for theory ingest.
- Unknown: S9 commentary not researched.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:32: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0108 (P1); built by tools/bm_build.py.
