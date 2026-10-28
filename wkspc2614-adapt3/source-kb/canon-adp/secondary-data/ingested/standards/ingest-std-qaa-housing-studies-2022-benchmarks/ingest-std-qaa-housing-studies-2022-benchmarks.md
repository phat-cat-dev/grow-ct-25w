---
id: std:doc:qaa-housing-studies-2022-benchmarks
title: "Subject Benchmark Statement: Housing Studies"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100196", label: "housing", basis: "stated" }
  - { scheme: "cah", code: "CAH13-01-04", label: "planning (urban, rural and regional)", basis: "inferred" }
edition: "March 2022 (fourth edition)"
published: 2022-03
status: current
supersedes: "the third edition (2019), named in the membership section; the front matter refers to the previous Statement"
heldText: { method: sha256-bytes, raw: 4372c1fea94af0b1be2110de601f9558386540ee453017d538af6be26935ead0, normalised: e8ad5941d4897919f0233c2ddfc55a688f6702fd147268d8a170124a0ed726a4 }
heldTextStan: { method: sha256-stan, raw: 4372c1fea94af0b1be2110de601f9558386540ee453017d538af6be26935ead0, normalised: 0c6e3188ffbe802ed0b728d9faa4fead652665265675e98bb9f0e95ca711ad46 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2022 revision (fourth edition of Housing Studies)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it explains in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0112 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:45"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Housing Studies (QAA, March 2022)

> Run 0112, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2022-housing-studies-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
An agent reading this document meets the UK sector reference point for Housing Studies degrees: what an honours graduate must understand at the threshold (19 items, para 4.3), what a master's graduate adds (para 4.6 and 4.7), the transferable skills both awards share (para 4.8) and the expectations the statement sets for course design, teaching and assessment, above all on inclusion, sustainability and employability. The typical and excellent rungs are not listed: the statement hands them to each provider's marking scheme and to Annex D of the qualification frameworks. Cite statements by their S4 ids and the issuer's paragraph numbers; read the honours items against FHEQ Level 6 and the master's items against FHEQ Level 7.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Housing studies is an interdisciplinary, vocational field built on the household's need for a home, drawing on the social sciences, law, health, planning and the built environment. The statement covers bachelor's degrees with honours (FHEQ Level 6, FQHEIS Level 10) and master's degrees (FHEQ Level 7, FQHEIS Level 11) and informs foundation degrees and housing modules elsewhere. It states one rung list, the threshold (19 items, para 4.3), and leaves the typical (2:1, 2:2) and excellent (1st) rungs to providers' marking schemes (para 4.4, 4.5) with Annex D as the reference (para 4.2); it adds four master's outcomes (para 4.6), a pointer to the FHEQ Level 7 descriptor (para 4.7) and eight transferable skills for both awards (para 4.8). Three cross-cutting themes run through it: equality, diversity and inclusion; education for sustainable development, built on the UN SDGs and UNESCO's key competencies; and employability and enterprise education; accessibility has its own section. The Chartered Institute of Housing is the one professional body, accrediting many courses and offering its own progression route.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement: Housing Studies"
edition: "March 2022 (fourth edition)"
dates:
  published: 2022-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point published by QAA as a membership organisation; not a sector-recognised standard in England, a key reference point in Wales and Scotland and part of the quality requirements in Northern Ireland (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2022", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what can be expected of a Housing Studies graduate at honours and master's level, and the nature of courses in the subject"
appliesTo:
  awards: ["bachelor's with honours", "master's", "informs: foundation degrees and housing modules in other courses"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"The Statement explicitly sets out the nature and academic standards of bachelor's degrees with honours and master's degrees carrying this subject in their title or containing Housing Studies as a significant part of their course content, for the subject community of housing studies.\" (D1, 1.6)"
statedSubjects:
  - { name: "Housing Studies", locator: "(D1, 1.6)", kind: "subject", codes: [{ scheme: "hecos", code: "100196", label: "housing" }] }
  - { name: "foundation degrees in Housing Studies; modules with substantial housing or homelessness content in urban studies, geography, planning, health, social work and social care", locator: "(D1, 1.6)", kind: "programme title", codes: [] }
  - { name: "Housing Studies joint honours", locator: "(D1, 2.7)", kind: "programme title", codes: [{ scheme: "hecos", code: "100196", label: "housing" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "an interdisciplinary field since the 1980s, now international in reach" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "starting point: the need for a home; production, consumption, rights, health" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "the disciplines it draws on and the aim of the education" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "students arrive by many routes; a strong vocational strand; CIH accreditation" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes of a Housing Studies degree", gloss: "academic, vocational and professional dimensions combined" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes of a Housing Studies degree", gloss: "scope: honours and master's, informing foundation degrees and modules" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes of a Housing Studies degree", gloss: "the CIH's role and the statement's distance from its specification" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Housing Studies degree", gloss: "levels, locations in faculties and modes of study" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Housing Studies degree", gloss: "a framework, not a prescription of how outcomes are reached" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Housing Studies degree", gloss: "devolved governance reflected in courses across the four nations" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Housing Studies degree", gloss: "three complementary themes run through the statement" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "courses uphold the Equality Act 2010" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "social justice and an inclusive curriculum at the core" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "co-produced knowledge and psychologically informed learning spaces" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "graduates confident to challenge decision makers" }
  - { number: "1.16", order: 18, componentType: area, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "themes of inclusive housing knowledge (eight listed)" }
  - { number: "1.17", order: 19, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "questions for an inclusivity lens (twelve listed)" }
  - { number: "1.18", order: 20, componentType: practice, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive learning experiences (five listed)" }
  - { number: "1.19", order: 21, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive behaviours of students and graduates (nine listed)" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "ESD and the UN SDGs; the UNESCO statement quoted" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "ESD as a lens linking economy, society and environment" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Sustainability: developing sustainable development knowledge in housing studies", gloss: "courses aimed at the SDGs' social, economic and environmental concerns" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Sustainability: developing sustainable development knowledge in housing studies", gloss: "SDG 11 and the other goals that bear on housing" }
  - { number: "1.24", order: 26, componentType: area, parent: "section 1", heading: "Sustainability: developing sustainable development competencies", gloss: "the eight UNESCO key competencies, adapted for housing (Figure 2)" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Sustainability: developing sustainable development competencies", gloss: "ESD outcomes linking subject knowledge, competencies and SDGs" }
  - { number: "1.26", order: 28, componentType: stem, parent: "section 1", heading: "Sustainability: developing learning environments to promote sustainable development", gloss: "the learning environment that ESD needs" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Sustainability: developing learning environments to promote sustainable development", gloss: "campus and community as a living laboratory" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Sustainability: developing learning environments to promote sustainable development", gloss: "sustainable development embedded in curriculum design" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Sustainability: developing learning environments to promote sustainable development", gloss: "ESD across content, teaching, structure and assessment" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Sustainability: developing learning environments to promote sustainable development", gloss: "ESD content: physical integrity, social justice, economic development" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Employability and enterprise education", gloss: "a vocational subject with entrepreneurial attributes" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Employability and enterprise education", gloss: "careers across sectors; placements and work-related activity" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Employability and enterprise education", gloss: "entrepreneurship education beyond employment (Figure 3)" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Employability and enterprise education", gloss: "transferable and self-management skills of graduates" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Employability and enterprise education", gloss: "graduate knowledge, reflection, ethics and resilience" }
  - { number: "2.1", order: 39, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "interdisciplinary design around functional knowledge and skills" }
  - { number: "2.2", order: 40, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "CIH standards woven into a three-fold design" }
  - { number: "2.3", order: 41, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "external stakeholders in the curriculum" }
  - { number: "2.4", order: 42, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "contributing disciplines, restated" }
  - { number: "2.5", order: 43, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "accessible environments, materials and site visits" }
  - { number: "2.6", order: 44, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "lived experience of housing in the content; flexible recruitment" }
  - { number: "2.7", order: 45, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through the honours levels to the threshold" }
  - { number: "2.8", order: 46, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards; Scottish four-year honours; route to postgraduate study" }
  - { number: "2.9", order: 47, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "postgraduate taught awards at Level 7 or 11; CIH chartered membership" }
  - { number: "2.10", order: 48, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "widening access, apprenticeships and CIH routes" }
  - { number: "2.11", order: 49, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "recognition of prior learning and support for diverse entrants" }
  - { number: "2.12", order: 50, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "doctoral study and early career research networks" }
  - { number: "2.13", order: 51, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "part-time and full-time routes; employer links" }
  - { number: "2.14", order: 52, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "blended and digital delivery mirroring sector practice" }
  - { number: "2.15", order: 53, componentType: practice, parent: "section 2", heading: "Partnership", gloss: "partnerships for work experience; employer groups" }
  - { number: "2.16", order: 54, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.17", order: 55, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.18", order: 56, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examining and accreditation" }
  - { number: "2.19", order: 57, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "CIH validation where accreditation is sought" }
  - { number: "3.1", order: 59, componentType: area, parent: "section 3", heading: "Content", gloss: "core knowledge and understanding of a typical course (26 topics)" }
  - { number: "3.2", order: 60, componentType: paragraph, parent: "section 3", heading: "Teaching, learning and assessment", gloss: "independent learners as the desired outcome" }
  - { number: "3.3", order: 61, componentType: practice, parent: "section 3", heading: "Teaching, learning and assessment", gloss: "a strategy matched to outcomes; work-based learning where accredited" }
  - { number: "3.4", order: 62, componentType: paragraph, parent: "section 3", heading: "Teaching, learning and assessment", gloss: "student-centred strategy; prior learning; EDI and ESD aligned" }
  - { number: "3.5", order: 63, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "evolving digital contexts and resilience in delivery" }
  - { number: "3.6", order: 64, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "digital expectations, library support and the digital divide" }
  - { number: "3.7", order: 65, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching approaches (seven examples)" }
  - { number: "3.8", order: 66, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "accessible materials and clear module outcomes" }
  - { number: "3.9", order: 67, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "an extended research or practice project" }
  - { number: "3.10", order: 68, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "outcomes may integrate sustainability competencies and SDGs" }
  - { number: "3.11", order: 69, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "diverse environments as a living laboratory" }
  - { number: "3.12", order: 70, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "diverse voices, decolonisation and transformative learning" }
  - { number: "3.13", order: 71, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "blended learning and group work" }
  - { number: "3.14", order: 72, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "the learning environment housing education needs" }
  - { number: "3.15", order: 73, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "an aligned assessment and feedback strategy" }
  - { number: "3.16", order: 74, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "accessible mixed assessment; published criteria" }
  - { number: "3.17", order: 75, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "assessment of, for and as learning (Figure 4)" }
  - { number: "3.18", order: 76, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "self, peer and synoptic assessment; authentic tasks" }
  - { number: "3.19", order: 77, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment types students meet (eight listed)" }
  - { number: "3.20", order: 78, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "a diverse range of methods with adjustments" }
  - { number: "4.1", order: 80, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the threshold is the minimum for an honours award" }
  - { number: "4.2", order: 81, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most perform above it; providers refer to Annex D" }
  - { number: "4.3", order: 82, componentType: stem, parent: "section 4", heading: "Threshold level (3rd class)", gloss: "the threshold rung: nineteen areas of systematic understanding" }
  - { number: "4.4", order: 83, componentType: paragraph, parent: "section 4", heading: "Typical level (2:1 or 2:2)", gloss: "typical rung left to providers' marking schemes" }
  - { number: "4.5", order: 84, componentType: paragraph, parent: "section 4", heading: "Excellent level (1st class)", gloss: "excellent rung left to providers' marking schemes" }
  - { number: "4.6", order: 85, componentType: stem, parent: "section 4", heading: "Master's level degrees in Housing Studies", gloss: "master's outcomes: forefront knowledge and four abilities" }
  - { number: "4.7", order: 86, componentType: paragraph, parent: "section 4", heading: "Master's level degrees in Housing Studies", gloss: "master's level set by the FHEQ Level 7 and FQHEIS Level 11 descriptor" }
  - { number: "4.8", order: 87, componentType: stem, parent: "section 4", heading: "Transferable and generic skills", gloss: "eight transferable and generic skills for both awards" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Housing Studies degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Housing Studies degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "none", heading: "section heading lines 1 to 4", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for SB6 and D3" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for Housing Studies", kind: "other: membership; read for the edition history (S8)" }
  - { number: "none", heading: "Figures 1, 3 and 4 (images: the SDGs; entrepreneurship, enterprise and employability; assessment for, as and of learning)", kind: "other: figures held only by caption" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 78 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/housing-studies-2022/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of a Housing Studies degree", "Characteristics of a Housing Studies degree"] }
  span: { start: 17085, end: 17520 }
  source: "1.10 As noted above, elements of Housing Studies courses reflect global, national and devolved governance structures and these will be reflected in courses across England, Scotland, Wales and Northern Ireland. While the CIH is a UK/international institution, courses will need to take appropriate account of differences in governance, law and policy across the UK and in the different housing bodies operating in the devolved nations.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Housing Studies courses across the UK"
  addressee: provider
  verbs: ["reflected", "take"]
  about: "differences between the four nations"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses will reflect global, national and devolved governance and will need to allow for how housing law, policy and governance, and the housing bodies, differ between England, Scotland, Wales and Northern Ireland, even though the CIH itself works UK-wide."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of a Housing Studies degree", "Equality, diversity and inclusion"] }
  span: { start: 18132, end: 18673 }
  source: "1.13 Housing studies is a subject of social justice. Therefore, its teaching and learning practice will have at its heart an inclusive curriculum that recognises the plurality of contemporary learners' experiences and characteristics, for example, recognising that learners may have experienced housing precarity themselves. Our curriculum uniquely engages with a multitude of policy-making networks, collaborative and intersectional spaces, within which students are encouraged to challenge decision making across both policy and practice.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "teaching and learning in housing studies"
  addressee: provider
  verbs: ["have", "recognises", "challenge"]
  about: "an inclusive curriculum grounded in social justice"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Because housing studies is about social justice, its teaching will centre on an inclusive curriculum that recognises how varied learners are, including that some may have lived through housing precarity, and that invites students to question decisions in policy and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/1.15
  locator: { number: "1.15", headingPath: ["Context and purposes of a Housing Studies degree", "Equality, diversity and inclusion"] }
  span: { start: 19206, end: 19621 }
  source: "1.15 Our Housing Studies graduates of the future will develop the self-reflection and confidence to engage strategically, collaboratively and critically with varied stakeholders across policy, practice and different academic disciplines. Students will have been supported to develop their own confidence in challenging decision making by all stakeholders, bringing housing-specific expertise to these interactions.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["develop", "engage", "challenging"]
  about: "confidence to engage and challenge stakeholders"
  themes: [theme:edi]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Graduates will build the self-reflection and confidence to work strategically, collaboratively and critically with stakeholders in policy, practice and other disciplines, and will have been helped to challenge the decisions of any stakeholder with housing expertise."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of a Housing Studies degree", "Sustainability: developing sustainable development knowledge in housing studies"] }
  span: { start: 25550, end: 25830 }
  source: "1.22 The United Nations Member States in September 2015 set out 17 ambitious goals with specific targets to be met by 2030. In line with these SDGs, Housing Studies courses should be focused towards addressing social, economic and environmental concerns to create a better world.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Housing Studies courses"
  addressee: provider
  verbs: ["focused", "addressing"]
  about: "courses directed at the SDGs' concerns"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "In line with the SDGs set by UN member states in 2015, Housing Studies courses should be directed towards tackling social, economic and environmental concerns for a better world."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of a Housing Studies degree", "Sustainability: developing sustainable development knowledge in housing studies"] }
  span: { start: 25830, end: 27346 }
  source: "1.23 The importance of quality, accessible housing is emphasised across several of the SDGs. For example, UN SDG 11 represents a specific goal for sustainable cities and\n\n8\ncommunities which integrates housing into the sustainable development debate. Many housing studies issues are directly relevant to SDG 11, which seeks to make cities and human settlements inclusive, safe, resilient and sustainable. Within this, target 11.1 is to ensure access for all to adequate, saf e and affordable housing (United Nations, 2015). The housing sector can also contribute to meeting the other 16 SDGs and their associated targets by 2030. For example, affordable housing is key for development and social equality (SDG1 No Poverty). SDG3 Good Health and Well-Being acknowledges how the quality of housing directly affects individual health and well-being, and the role of housing in fostering healthier lifestyles and places/communities. SDG5 Gender Equality recognises that gender- based inequalities can limit women's access to secure and durable housing, and asset ownership. The sustainability of future housing in terms of energy independence and effective use of energy is outlined in SDG7 Affordable and Clean Energy, including the retrofitting of existing housing stock. The expectation is that Housing Studies courses have sufficient sustainability content to ensure that students are aware and confident in discussing sustainability issues in the context of housing. Developing sustainable development competencies\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "The expectation is" read as must
  level: none
  appliesTo: "Housing Studies courses"
  addressee: provider
  verbs: ["ensure", "discussing"]
  about: "enough sustainability content for confident discussion"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Quality, accessible housing runs through several SDGs, SDG 11 above all, and housing can help meet the others (for example SDGs 1, 3, 5 and 7); the stated expectation is that courses hold enough sustainability content for students to be aware of the issues and confident discussing them in housing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/1.25
  locator: { number: "1.25", headingPath: ["Context and purposes of a Housing Studies degree", "Sustainability: developing sustainable development competencies"] }
  span: { start: 29934, end: 30405 }
  source: "1.25 Course and module-level learning outcomes for ESD should interconnect subject- specific knowledge and skills in relation to housing studies, sustainability competencies and the 17 UN SDGs. The expectation is that courses progressively develop the UNESCO competencies and that assessment demonstrates achievement of these competencies. QAA provides guidance on how this can be achieved in practice. Developing learning environments to promote sustainable development\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "course and module outcomes for ESD"
  addressee: provider
  verbs: ["interconnect", "develop"]
  about: "ESD outcomes linking knowledge, competencies and SDGs"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "ESD learning outcomes at course and module level should link housing knowledge and skills with the sustainability competencies and the 17 SDGs; the stated expectation is that courses build the UNESCO competencies step by step and that assessment shows they are achieved."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/1.26.b1
  locator: { number: "1.26.b1", headingPath: ["Context and purposes of a Housing Studies degree", "Sustainability: developing learning environments to promote sustainable development"] }
  span: { start: 30458, end: 30532 }
  source: "interdisciplinary or transdisciplinary learning approaches are facilitated"
  stem: "1.26"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the learning environment for ESD"
  addressee: provider
  verbs: ["facilitated"]
  about: "interdisciplinary or transdisciplinary learning"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "ESD needs a learning environment that supports interdisciplinary or transdisciplinary learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/1.26.b2
  locator: { number: "1.26.b2", headingPath: ["Context and purposes of a Housing Studies degree", "Sustainability: developing learning environments to promote sustainable development"] }
  span: { start: 30535, end: 30579 }
  source: "learning is inclusive and accessible for all"
  stem: "1.26"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the learning environment for ESD"
  addressee: provider
  verbs: []
  about: "inclusive and accessible learning"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "ESD needs learning that includes everyone and that everyone can reach."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/1.26.b3
  locator: { number: "1.26.b3", headingPath: ["Context and purposes of a Housing Studies degree", "Sustainability: developing learning environments to promote sustainable development"] }
  span: { start: 30582, end: 30618 }
  source: "policies support synoptic assessment"
  stem: "1.26"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the learning environment for ESD"
  addressee: provider
  verbs: ["support"]
  about: "policies that support synoptic assessment"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "ESD needs policies that allow synoptic assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/1.26.b4
  locator: { number: "1.26.b4", headingPath: ["Context and purposes of a Housing Studies degree", "Sustainability: developing learning environments to promote sustainable development"] }
  span: { start: 30621, end: 30686 }
  source: "extra and co-curricular opportunities are provided and recognised"
  stem: "1.26"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the learning environment for ESD"
  addressee: provider
  verbs: ["provided", "recognised"]
  about: "extra and co-curricular opportunities"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "ESD needs extra-curricular and co-curricular opportunities that are offered and given recognition."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/1.26.b5
  locator: { number: "1.26.b5", headingPath: ["Context and purposes of a Housing Studies degree", "Sustainability: developing learning environments to promote sustainable development"] }
  span: { start: 30689, end: 30852 }
  source: "learning spaces, including the campus and outdoor environments, are fully utilised to provide alternative locations to develop and express the competencies of ESD."
  stem: "1.26"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the learning environment for ESD"
  addressee: provider
  verbs: ["utilised", "develop", "express"]
  about: "learning spaces used as alternative locations"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "ESD needs campus, outdoor and other learning spaces to be used to the full as places where students build and show its competencies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/1.27
  locator: { number: "1.27", headingPath: ["Context and purposes of a Housing Studies degree", "Sustainability: developing learning environments to promote sustainable development"] }
  span: { start: 30853, end: 31340 }
  source: "1.27 Teaching, learning and assessment should take advantage of the learning opportunities afforded by the campus and the local community, as well as online environments. The use of the campus and community as a 'living laboratory', can offer valuable and authentic learning experiences in housing studies. The expectation is that course provision in housing studies uses a variety of learning environments and opportunities to develop sustainability understanding and competencies.\n\n10\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "teaching, learning and assessment"
  addressee: provider
  verbs: ["take", "uses"]
  about: "the campus and community as a living laboratory"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Teaching, learning and assessment should use the opportunities the campus, the local community and online settings offer; treating campus and community as a living laboratory can give authentic housing learning, and the stated expectation is that courses use varied environments to build sustainability understanding and competencies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/1.28
  locator: { number: "1.28", headingPath: ["Context and purposes of a Housing Studies degree", "Sustainability: developing learning environments to promote sustainable development"] }
  span: { start: 31340, end: 31819 }
  source: "1.28 To promote sustainable development within housing studies, the agenda should be meaningfully embedded in the design of the curriculum at course and module levels. This in turn requires learning environments fit for purpose to support Housing Studies students to acquire the knowledge, understanding and skills necessary to develop values and take actions to transition society towards sustainable futures and to sustain communities and link housing to health and education.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "curriculum design at course and module level"
  addressee: provider
  verbs: ["embedded", "support"]
  about: "sustainable development embedded in the curriculum"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "To advance sustainable development, the agenda should be built into curriculum design at course and module level, with learning environments that let students gain the knowledge, understanding and skills to act towards sustainable futures and to link housing with health and education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/1.29
  locator: { number: "1.29", headingPath: ["Context and purposes of a Housing Studies degree", "Sustainability: developing learning environments to promote sustainable development"] }
  span: { start: 31819, end: 32289 }
  source: "1.29 The incorporation of ESD should be manifested in module content, learning and teaching approaches, structure and delivery, and assessment. Inclusive and interdisciplinary learning approaches are encouraged in which extra and co-curricular opportunities are provided and recognised. Case studies, project-based research and educational visits to communities where symptoms of unsustainability manifest or similar approaches can add value to learning and assessment.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "modules: content, delivery and assessment"
  addressee: provider
  verbs: ["manifested", "encouraged"]
  about: "ESD across content, teaching and assessment"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "ESD should show in module content, teaching and learning methods, structure and delivery and assessment; inclusive, interdisciplinary approaches with recognised extra and co-curricular work are encouraged, and case studies, project research and visits to communities facing unsustainability can enrich learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/1.30
  locator: { number: "1.30", headingPath: ["Context and purposes of a Housing Studies degree", "Sustainability: developing learning environments to promote sustainable development"] }
  span: { start: 32289, end: 33193 }
  source: "1.30 ESD content should focus on the integrity of physical environments, social justice and economic development. A range of economic, environmental and social changes are taking place in housing studies, and literature and resources increasingly include diverse voices and perspectives from under-represented communities. Ideas and perspectives from other disciplines can promote a meaningful multidisciplinary experience to support developing sustainability competencies and meeting the aims of the 17 UN SDGs. Physical and virtual learning spaces within campuses and outdoor environments provide locations to develop and express ESD competencies and digital platforms can also be integral to the interactive learning environment. The housing studies subject area should be able to develop and strengthen learning environments to promote sustainable development. Employability and enterprise education\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "ESD content and the subject area"
  addressee: provider
  verbs: ["focus", "develop", "strengthen"]
  about: "the focus of ESD content and learning environments"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "ESD content should centre on keeping physical environments whole, on social justice and on economic development, drawing on diverse voices and other disciplines; the subject area should be able to build and strengthen environments, physical, virtual and digital, that promote sustainable development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/1.34
  locator: { number: "1.34", headingPath: ["Context and purposes of a Housing Studies degree", "Employability and enterprise education"] }
  span: { start: 35116, end: 35707 }
  source: "1.34 Housing Studies graduates will be equipped with transferable skills that can be applied in the current housing employment context, but also in emerging jobs applying new technologies as they are developed and invented. They will have well-developed self- management skills and be able to motivate themselves and others. They will be able to identify housing-related problems, take responsibility for formulating ideas and implement decisions to address those problems. They will be equipped to manage risk and identify the boundaries of their own professional capability and judgement.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["equipped", "motivate", "identify", "implement", "manage"]
  about: "transferable, self-management and problem-solving skills"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Graduates will have transferable skills for present housing work and for new roles built on new technology; they will manage and motivate themselves and others, spot housing problems, own ideas and decisions to solve them, handle risk and know the limits of their professional competence and judgement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/1.35
  locator: { number: "1.35", headingPath: ["Context and purposes of a Housing Studies degree", "Employability and enterprise education"] }
  span: { start: 35707, end: 37323 }
  source: "1.35 Graduates will have a well-developed knowledge of different aspects of housing, including policy, development, finance, management, research, sustainability, and equality and diversity issues. They will critically reflect on their own knowledge and skills, particularly in f ast-evolving aspects of housing delivery such as digital technology. As reflective practitioners, they will be responsible for their own learning, and be able to organise their own professional development. They will have knowledge of areas closely aligned to housing, such as health, social services and the criminal justice system, and will be able to identify and transfer good practice to their own field of work. Housing Studies graduates understand the individual, social and environmental impact of their own work, and their own civic and social responsibilities. They will in the course of their employment be sensitive to cultures, customs and beliefs, and to ethical and environmental issues. They will be aware of the impact of their work on themselves, the workforce, the community and the economy. Housing Studies graduates working in a range of employment positions will be mindful of professional ethics and standards, particularly in relation to issues of equality and diversity in their relationship with colleagues and customers or service users. They will be resilient in their professional housing work, and resourceful in dealing with a rapidly changing housing environment. They will take a creative, questioning approach to housing issues, and be able to pivot and adapt successf ully to changing situations.\n\n12\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["have", "reflect", "organise", "identify", "transfer", "pivot"]
  about: "professional knowledge, reflection, ethics and resilience"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Graduates will know housing well across policy, development, finance, management, research, sustainability and equality; reflect critically on their own knowledge, especially in fast-changing areas such as digital technology; direct their own learning and development; bring in good practice from neighbouring fields such as health and criminal justice; and work ethically, sensitively, resiliently and creatively, adapting as situations change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of a Housing Studies degree", "Accessibility"] }
  span: { start: 39801, end: 40806 }
  source: "2.5 Housing studies learning environments and materials should be designed to be accessible for students with a wide range of learning and/or mobility needs and for students with lived experiences of structural inequalities which may have limited their prior learning opportunities as a result of their socioeconomic background or protected characteristics. Students with mobility needs, learning needs and lived experience of disadvantage should all be able to participate fully in Housing Studies courses. Where appropriate, students should benefit from particular adjustments and support services in line with national frameworks and institutional service provision. For example, adjustments may be made for those with sensory impairments or who live with dyslexia, dyspraxia or who are on the autism spectrum. In relation to physical accessibility, site visits may often be used as part of modules in order to facilitate learning. These should be arranged so that they are accessible to all students.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "learning environments, materials and site visits"
  addressee: provider
  verbs: ["designed", "participate", "arranged"]
  about: "accessible learning environments and site visits"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Learning environments and materials should be accessible to students with a wide range of learning or mobility needs and to those whose prior learning was limited by structural inequality; all should be able to take full part, with adjustments and support where suitable, and site visits should be arranged so every student can attend."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of a Housing Studies degree", "Accessibility"] }
  span: { start: 40806, end: 41957 }
  source: "2.6 Accessibility of content in relation to equality, diversity and inclusion is also a key focus of Housing Studies courses. All students who study housing studies have lived experience of engaging with housing by the very nature of currently living somewhere and\n\n13\nhaving lived somewhere previously. Some students will have experienced housing-related issues that are included in the curriculum. This can be recognised within course design so that barriers to engaging with this content are not constructed, and so that students can recognise and share their experiences as part of the learning environment if they so wish. Recruitment to Housing Studies courses should be sufficiently flexible to allow for the flourishing of learners with limited prior academic experiences, but who are able to draw upon their experiences of working in or with the housing sector. This flexibility might include 'whole person' approaches to recruitment, liaison with feeder providers of Housing Studies courses and targeted learning support for non-traditional applicants in induction programmes to help with academic writing and critical thinking. Progression\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "course design and recruitment"
  addressee: provider
  verbs: ["recognised", "share", "allow"]
  about: "lived experience in the content; flexible recruitment"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Every student has lived somewhere, and some have faced the housing problems the course teaches; course design can recognise this so that the content raises no barriers and students may share experience if they choose, and recruitment should be flexible enough for learners with little academic background but sector experience to flourish."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of a Housing Studies degree", "Progression"] }
  span: { start: 41957, end: 42606 }
  source: "2.7 Over the course of a degree with honours (FHEQ Level 6; FQHEIS Level 10) a Housing Studies student will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the attainment of certain knowledge, expertise and experience which builds towards the final achievement of meeting all of the threshold-level subject-specific and generic skills listed in this Statement. Joint honours undergraduates will achieve elements of the specific and generic skills for the subject but will add others according to the subjects covered in a joint course.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours students, single and joint"
  addressee: learner
  verbs: ["progress", "achieve"]
  about: "progression to the threshold across the honours levels"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Through an honours degree (FHEQ Level 6, FQHEIS Level 10) a student will move from level to level under institutional rules, each level building towards meeting every threshold subject-specific and generic skill; joint honours students will meet part of these and add others from their second subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of a Housing Studies degree", "Progression"] }
  span: { start: 44651, end: 45743 }
  source: "2.11 Housing Studies courses incorporate mechanisms for the recognition of prior learning (RPL) and the progression route for Housing Studies postgraduate study is diverse. Students join from undergraduate and a wide range of allied/cognate undergraduate courses (such as those listed in paragraph 2.4) or as part of their professional development within their careers, including completion of CIH courses. Clear and supportively operated RPL\n\n14\nregulations are significant for access to undergraduate and postgraduate taught programmes. At postgraduate level, RPL and course regulations should not disadvantage those admitted with alternative/equivalent experience to formal higher education or whose experience is dated. Support should be available for all students, including those with diverse prior learning experience. Study skills packages and similar mechanisms can aid transition into higher-level learning, where appropriate. Study skills support may also cover how to improve assessments, guidance on regulations and options if students encounter difficulties with their studies.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "postgraduate admissions, regulations and support"
  addressee: provider
  verbs: ["disadvantage", "available"]
  about: "fair recognition of prior learning and support for all"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses recognise prior learning and entrants arrive by many routes; at postgraduate level, RPL and course rules should not penalise those admitted on alternative or older experience, and support should be open to all students, for example study skills packages to ease the move into higher-level study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/2.15
  locator: { number: "2.15", headingPath: ["Distinctive features of a Housing Studies degree", "Partnership"] }
  span: { start: 47115, end: 48285 }
  source: "2.15 In line with the professional orientation of the housing studies curriculum (Employability and enterprise education section), partnerships with housing organisations for work experience are a core part of the undergraduate and postgraduate courses. Chartered Membership of CIH accreditation requires prescribed work experience in a housing-related role, and partnerships exist between higher education institutions and employers to facilitate this. These partnerships often enable shared learning, for example through guest speakers, as well as engagement around students' professional development skills. Opportunities also exist for students to engage with employers while completing dissertations, research methods or reflective practice modules. It is anticipated that higher education providers facilitate employer groups which meet regularly to inform and support this partnership working. Partnership groups can include a wide range of housing sector organisations and stakeholders, besides sponsors of individual students. These partners are invited to comment on new curriculum design as well as new approaches to skills development. Monitoring and review\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "courses and students seeking CIH chartered membership"
  addressee: both
  verbs: ["requires", "facilitate"]
  about: "work experience for CIH chartered membership; employer partnerships"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Partnerships with housing organisations for work experience are core to undergraduate and postgraduate courses; CIH chartered membership accreditation requires set work experience in a housing role, and providers are expected to run employer groups that inform curriculum and skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/2.16
  locator: { number: "2.16", headingPath: ["Distinctive features of a Housing Studies degree", "Monitoring and review"] }
  span: { start: 48285, end: 49024 }
  source: "2.16 A major feature of academic quality assurance and enhancement at a higher education institution is having in place monitoring and regular review processes for the courses it delivers. Degree-awarding bodies routinely collect and analyse information and undertake periodic course review according to their own needs. They will draw on a range of external reference points, including this Statement, to ensure that their provision aligns with sector norms. Monitoring and evaluation is a periodic assessment of a course, conducted internally or by external independent evaluators. Evaluation uses information from current\n\n15\nand historic monitoring to develop an understanding of student achievement and inform future course planning.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "degree-awarding bodies"
  addressee: provider
  verbs: ["draw", "ensure"]
  about: "external reference points in monitoring and review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Degree-awarding bodies monitor and periodically review their courses and will use external reference points, this statement among them, to keep their provision in line with sector norms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/2.17
  locator: { number: "2.17", headingPath: ["Distinctive features of a Housing Studies degree", "Monitoring and review"] }
  span: { start: 49024, end: 49336 }
  source: "2.17 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["use", "ensure"]
  about: "external reviewers confirm threshold standards"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Externality is essential to UK quality assurance: providers will bring in external reviewers during periodic review to give an outside view of changes and confirm that threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of a Housing Studies degree", "Monitoring and review"] }
  span: { start: 50334, end: 50759 }
  source: "2.19 Housing St udies courses may be subject to internal institutional monitoring and review processes, external academic review, and external validation/re-validation by the CIH (if they are to be CIH accredited). Where accreditation is sought, this influences core aspects of content and skills that need to be delivered and determines any required engagement with CIH regarding changes to course content and delivery.\n\n16\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "courses seeking CIH accreditation"
  addressee: provider
  verbs: ["delivered", "determines"]
  about: "CIH accreditation shapes content and change"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses may undergo internal monitoring, external review and CIH validation; where a course seeks CIH accreditation, the body's requirements shape the core content and skills it must deliver and the engagement with CIH that changes need."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Teaching, learning and assessment"] }
  span: { start: 55502, end: 56258 }
  source: "3.3 A typical Housing Studies course has a teaching, learning and assessment strategy which makes the appropriateness of the methods used explicit and demonstrable in relation to the anticipated learning outcomes and skills being developed. Learning approaches are linked to the mode of delivery and the student profile. The strategy is expected to include a variety of approaches to teaching, learning and assessment which reflect and accommodate a diversity of learning styles and student needs. Where courses are professionally accredited, the learning and assessment strategy will include opportunities for work-based and/or work-related learning, both for students who are new to housing and also for those with some prior work experience in housing.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "the teaching, learning and assessment strategy"
  addressee: provider
  verbs: ["include"]
  about: "a strategy matched to outcomes; work-based learning where accredited"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A typical course's strategy makes plain why its methods suit the intended outcomes, is expected to use varied approaches that meet varied learning styles and needs, and, where the course is professionally accredited, will include work-based or work-related learning for newcomers and experienced staff alike."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Teaching, learning and assessment"] }
  span: { start: 56258, end: 57102 }
  source: "3.4 It is anticipated that the strategy emphasises a student-centred approach and incorporates mechanisms for review across teaching, learning and assessment approaches. Learning, teaching and assessment are expected to incorporate mechanisms to recognise students' prior knowledge and experience, and to clarify opportunities for exemption from elements of the course, where appropriate. Informed by internal and external good practice guidance, where appropriate, the strategy can be developed with advice, collaboration and inputs from professional colleagues in housing practice. In addition to meeting housing studies competencies, alignment of teaching, learning and assessment activities to embed learning across equality, diversity and inclusion themes and education for sustainable development is encouraged.\n\n18\nTeaching and learning\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: none
  appliesTo: "the teaching, learning and assessment strategy"
  addressee: provider
  verbs: ["emphasises", "incorporate", "recognise"]
  about: "student-centred strategy and recognition of prior learning"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The strategy is anticipated to be student-centred with review built in; learning, teaching and assessment are expected to recognise prior knowledge and experience and to clarify any exemption; practitioners may advise; alignment with EDI and ESD is encouraged."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/3.6
  locator: { number: "3.6", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 57964, end: 58768 }
  source: "3.6 Housing Studies courses should be underpinned by clear information and guidance on expectations around requirements for the use of digital technology (and access to training if needed) as well as support to make best use of library facilities and related resources offered by the higher education provider. Recognition of, and support for, diverse prior experience of academic and digital learning underpins learning and teaching on Housing Studies courses. Institutions providing virtual and blended learning approaches should be aware of the 'digital divide' and make appropriate arrangements to support students engaged in these forms of course delivery. Where possible and appropriate, applicants may be directed to preparatory resources and support for digital learning in advance of enrolment.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "courses and institutions offering virtual and blended learning"
  addressee: provider
  verbs: ["underpinned", "aware"]
  about: "digital expectations, library support and the digital divide"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses should be supported by clear guidance on what digital technology students need (with training if required) and on using library resources; institutions with virtual or blended learning should be alert to the digital divide and arrange support."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/3.7
  locator: { number: "3.7", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 58768, end: 59612 }
  source: "3.7 Within both on-campus and online learning environments, it is expected that a range of teaching approaches are used to accommodate different learning styles and preferences, for example:\n• lectures, which may be in real time or recorded\n• seminars, tutorials or other small-group formats to facilitate student participation and dialogue with tutors and peers\n• one-to-one working with supervisors\n• directed self-study, reading and assessment preparation\n• fieldtrips, site visits and virtual/online visits and practice-related sessions (with reasonable adjustments for disabled students, if required)\n• problem-based learning, peer working and teamwork skills\n• opportunities for negotiated learning and work-based/work-related learning which optimise employability and enterprise themes that are important for professional accreditation.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: none
  appliesTo: "teaching on campus and online"
  addressee: provider
  verbs: ["used", "accommodate"]
  about: "a range of teaching approaches for different learners"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "In both campus and online settings a range of teaching approaches is expected, to suit different learning styles; the examples given run from lectures and seminars to supervision, directed study, fieldwork with adjustments, problem-based learning and negotiated or work-related learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/3.8
  locator: { number: "3.8", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 59612, end: 59915 }
  source: "3.8 Learning materials are expected to be accessible and to provide students with full and accurate documentation relating to their course of study. For each module, learning outcomes will be clearly specified and achievable, supported by an indication of relevant reading and other learning resources.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "learning materials and module outcomes"
  addressee: provider
  verbs: ["specified", "supported"]
  about: "accessible materials and clear module outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Materials are expected to be accessible to all and to give full, accurate course documentation, and each module's learning outcomes will be stated clearly and be achievable, with reading and other resources indicated."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/3.11
  locator: { number: "3.11", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 60283, end: 61160 }
  source: "3.11 Teaching practices should provide opportunities to uncover alternative viewpoints, reflect on experiences, and address real-world challenges. Housing Studies courses should\n\n19\ntake advantage of the learning opportunities afforded by diverse environments, including campuses, local communities and online environments. The campus, community and housing sector environments can be used as a living laboratory where students can learn about, for example, housing innovations, community development, health and well-being, local governance, business and economic development strategies, as well as leadership. Along with online and digital resources, this range of environments can offer authentic and transformational learning experiences. Digital technology is increasingly valuable as an inclusive framework for recording and replicating the living laboratory experience.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "teaching practices and courses"
  addressee: provider
  verbs: ["provide", "take"]
  about: "alternative viewpoints, reflection and real-world challenges in diverse settings"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Teaching should open up alternative viewpoints, reflection on experience and real problems, and courses should use campuses, communities and online spaces as a living laboratory for topics from housing innovation to local governance, with digital tools to record and repeat the experience inclusively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/3.12
  locator: { number: "3.12", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 61160, end: 62081 }
  source: "3.12 Course design should consider how courses in Housing Studies can extend recommended literature and resources to include a greater diversity of voices, particularly tenant voices and perspectives from under-represented communities. Careful consideration should be given to interpretation and reinterpretation of historical approaches to housing studies, and to the decolonisation of the curriculum. Learning experiences should transform the ways of thinking and practising about housing studies and enable students to become informed advocates of sustainable development. Courses should promote meaningful multi, inter and trans-disciplinary experiences that challenge students beyond the traditional conventions of housing studies and UK-centred housing practice through opportunities to develop collaborative and holistic approaches to developing sustainability competencies and meeting the aims of the 17 UN SDGs.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "course design and learning experiences"
  addressee: provider
  verbs: ["consider", "transform", "promote"]
  about: "diverse voices, decolonisation and transformative learning"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Course design should widen literature and resources to include more voices, especially tenants and under-represented communities; historical approaches and the decolonisation of the curriculum should get careful thought; learning should change ways of thinking and practising and make students informed advocates of sustainable development; and courses should offer multi, inter and trans-disciplinary experiences beyond UK-centred practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/3.13
  locator: { number: "3.13", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 62081, end: 62723 }
  source: "3.13 Housing Studies courses are increasingly likely to be delivered through blended learning. Digital teaching and learning can be used creatively, and deployed equitably, to provide a sustainable, inclusive and immersive student experience. Blended learning can use real-world problems and scenarios to encourage students to think creatively about a range of housing practices. Group-based work (including online group work) can help to develop collaborative competencies through meaningful discussions with peers and other stakeholders. Opportunities for critical reflection on personal perspectives and that of others should be promoted.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "blended teaching and learning"
  addressee: provider
  verbs: ["promoted"]
  about: "blended learning, group work and critical reflection"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Blended learning is increasingly likely; digital teaching can be used creatively and fairly for an inclusive, immersive experience, group work builds collaborative competencies and chances for critical reflection on one's own and others' views should be promoted."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/3.14.b1
  locator: { number: "3.14.b1", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 62798, end: 62872 }
  source: "interdisciplinary or transdisciplinary learning approaches are facilitated"
  stem: "3.14"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the learning environment for housing studies"
  addressee: provider
  verbs: ["facilitated"]
  about: "interdisciplinary or transdisciplinary learning"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Housing studies education needs a learning environment that supports learning across disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/3.14.b2
  locator: { number: "3.14.b2", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 62875, end: 62919 }
  source: "learning is inclusive and accessible for all"
  stem: "3.14"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the learning environment for housing studies"
  addressee: provider
  verbs: []
  about: "inclusive and accessible learning"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Housing studies education needs learning that includes everyone and that everyone can reach."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/3.14.b3
  locator: { number: "3.14.b3", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 62922, end: 62978 }
  source: "education for sustainable development underpins learning"
  stem: "3.14"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the learning environment for housing studies"
  addressee: provider
  verbs: ["underpins"]
  about: "ESD underpinning learning"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Housing studies education needs education for sustainable development to sit beneath learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/3.14.b4
  locator: { number: "3.14.b4", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 62981, end: 63046 }
  source: "extra and co-curricular opportunities are provided and recognised"
  stem: "3.14"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the learning environment for housing studies"
  addressee: provider
  verbs: ["provided", "recognised"]
  about: "extra and co-curricular opportunities"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Housing studies education needs extra-curricular and co-curricular opportunities that are offered and recognised."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/3.14.b5
  locator: { number: "3.14.b5", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 63049, end: 63216 }
  source: "learning spaces (including campus, outdoor and virtual environments) are fully utilised to provide alternative locations to develop and express the competencies of ESD"
  stem: "3.14"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the learning environment for housing studies"
  addressee: provider
  verbs: ["utilised", "develop", "express"]
  about: "campus, outdoor and virtual spaces for ESD competencies"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Housing studies education needs campus, outdoor and virtual spaces to be used fully as alternative places to build and show ESD competencies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/3.14.b6
  locator: { number: "3.14.b6", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 63219, end: 63389 }
  source: "policies support synoptic assessment, enabling students to make critical connections across modules and integrate their knowledge as they progress and develop. Assessment"
  stem: "3.14"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the learning environment for housing studies"
  addressee: provider
  verbs: ["support", "enabling", "integrate"]
  about: "policies for synoptic assessment that connect modules"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Housing studies education needs policies that allow synoptic assessment, so students connect learning across modules and integrate it as they progress."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 63390, end: 63969 }
  source: "3.15 Housing studies educators are encouraged to think creatively about a wide range of teaching, learning and assessment practices. An assessment and feedback strategy supports learning and enables students to demonstrate their level of attainment and identify their progress. For each method of assessment, the aims, content requirements and m ar k ing criteria should be clearly defined and aligned, to reflect the diversity of knowledge and skills developed within the curriculum, the approaches to teaching and learning used, and the learning outcomes of the degree course.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "each method of assessment"
  addressee: provider
  verbs: ["defined", "aligned"]
  about: "clear, aligned aims, content and marking criteria"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Educators are encouraged to think creatively about assessment; a strategy for assessment and feedback helps students show their attainment and see their progress, and for each method the aims, content requirements and marking criteria should be clearly set out and aligned with the curriculum, teaching approaches and outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/3.16
  locator: { number: "3.16", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 63969, end: 64449 }
  source: "3.16 Students should have the opportunity to demonstrate their full range of abilities, through a mix of assessment methods that are equally accessible to students from varying\n\n20\neducational backgrounds and in different learning situations, as discussed in the section on equality, diversity and inclusion. It is expected that the means of assessment are documented and distributed to students, and published criteria are made available for all summative methods of assessment.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "students and the assessment regime"
  addressee: provider
  verbs: ["demonstrate", "documented", "distributed"]
  about: "accessible mixed assessment and published criteria"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should be able to show the full range of their abilities through a mix of assessment methods equally open to all backgrounds and situations; the means of assessment are expected to be documented and shared, and criteria published for all summative assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/3.20
  locator: { number: "3.20", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 66321, end: 66567 }
  source: "3.20 It is anticipated that a diverse range of assessment methods is employed to ensure demonstration of the suite of housing studies knowledge, skills and benchmark standards (with reasonable adjustments for disabled students, if required).\n\n22\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: none
  appliesTo: "assessment across the course"
  addressee: provider
  verbs: ["employed", "ensure"]
  about: "a diverse range of assessment methods with adjustments"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It is anticipated that varied assessment methods are used so that the whole range of housing knowledge, skills and standards is shown, with reasonable adjustments for disabled students where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 67187, end: 67701 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropria te evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications fo r bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd. Threshold level (3rd class)\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["refer"]
  about: "providers refer to Annex D for performance above threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do well above the minimum; each provider sets its own way of judging the evidence and should refer to Annex D, which classifies honours outcomes at FHEQ Level 6 and FQHEIS Level 10 and describes the four honours classes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b1
  locator: { number: "4.3.b1", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 67855, end: 67958 }
  source: "the critical role of housing as a key social determinant of the well-being of residents and communities"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "housing as a social determinant of well-being"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of why housing is a key social factor in the well-being of residents and communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b2
  locator: { number: "4.3.b2", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 67961, end: 68099 }
  source: "the reasons for state intervention in the housing market, and the changing nature of the production, consumption and experience of housing"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "state intervention and the changing production, consumption and experience of housing"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of why the state intervenes in housing markets and how producing, consuming and living in housing are changing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b3
  locator: { number: "4.3.b3", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68102, end: 68232 }
  source: "the evolution and identification of housing problems, and developments in the policy and legal framework to address these problems"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "how housing problems emerge and the policy and legal responses"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of how housing problems arise and are recognised, and of how policy and law have developed to deal with them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b4
  locator: { number: "4.3.b4", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68235, end: 68379 }
  source: "how housing policy is formulated and implemented at local and national levels, and how housing policy interacts with wider public policy agendas"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["formulated", "implemented", "interacts"]
  about: "how housing policy is made and implemented"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of how housing policy is made and carried out locally and nationally, and how it connects with wider public policy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b5
  locator: { number: "4.3.b5", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68382, end: 68494 }
  source: "different forms of housing organisations, the governance of these organisations and the challenges of governance"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "housing organisations and their governance"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of the different kinds of housing organisation, how each is governed and the difficulties governance faces."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b6
  locator: { number: "4.3.b6", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68497, end: 68625 }
  source: "different models of housing need, and development of systems which are responsive to the needs of diverse individuals and groups"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "models of housing need and responsive systems"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of the different ways housing need is modelled and of building systems that respond to diverse individuals and groups."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b7
  locator: { number: "4.3.b7", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68628, end: 68768 }
  source: "how housing organisations and professionals can work to address wider social inequalities at structural, institutional and individual levels"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["work", "address"]
  about: "how housing bodies and professionals tackle wider social inequality"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of how housing organisations and practitioners can act on wider social inequalities at structural, institutional and individual level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b8
  locator: { number: "4.3.b8", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68771, end: 68927 }
  source: "comparative approaches to housing systems and policies across the UK and more widely, identifying and implementing learning and good practice as appropriate"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identifying", "implementing"]
  about: "comparative housing systems and transferring good practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of comparing housing systems and policies across the UK and beyond, finding and applying lessons and good practice where they fit."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b9
  locator: { number: "4.3.b9", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 68930, end: 69075 }
  source: "the benefits of involving residents in decision making, and how to engage seldom- heard individuals and groups who face barriers to participation"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["involving", "engage", "face"]
  about: "resident involvement and reaching seldom-heard groups"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of why involving residents in decisions helps and how to reach individuals and groups seldom heard because of barriers to taking part."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b10
  locator: { number: "4.3.b10", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69078, end: 69129 }
  source: "the key principles of housing economics and finance"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "housing economics and finance"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of the core principles of housing economics and housing finance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b11
  locator: { number: "4.3.b11", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69132, end: 69222 }
  source: "the key principles of the business planning cycle, service management and service delivery"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "business planning, service management and delivery"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of the core principles of the business planning cycle and of managing and delivering services."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b12
  locator: { number: "4.3.b12", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69225, end: 69330 }
  source: "the identification and application of appropriate research methods and methodologies in a housing context"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "choosing and applying research methods in housing"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of selecting and using suitable research methods and methodologies in a housing setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b13
  locator: { number: "4.3.b13", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69333, end: 69397 }
  source: "the identification of evidence-based solutions to housing issues"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "evidence-based solutions to housing issues"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of how to find solutions to housing issues that rest on evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b14
  locator: { number: "4.3.b14", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69400, end: 69474 }
  source: "the presentation of information, data and concepts to a range of audiences"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "presenting information, data and concepts to varied audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of presenting information, data and ideas to different audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b15
  locator: { number: "4.3.b15", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69477, end: 69598 }
  source: "the key principles of leadership and management within housing, and how these can be applied within housing organisations"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "leadership and management in housing organisations"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of the core principles of leading and managing in housing and how to apply them in housing organisations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b16
  locator: { number: "4.3.b16", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69601, end: 69759 }
  source: "different aspects of environmental sustainability including the impact of the climate crisis in the design, development, maintenance and management of housing"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "environmental sustainability and the climate crisis in housing"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of aspects of environmental sustainability, including how the climate crisis bears on designing, developing, maintaining and managing housing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b17
  locator: { number: "4.3.b17", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69766, end: 69934 }
  source: "the key principles of the renewal, refurbishment and regeneration of housing; the engagement of residents in these processes; and the achievement of equitable outcomes."
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "renewal, refurbishment and regeneration with resident engagement"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of the core principles of renewing, refurbishing and regenerating housing, involving residents in these processes and reaching fair outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b18
  locator: { number: "4.3.b18", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 69937, end: 69997 }
  source: "the analysis of the factors leading to tenure-related stigma"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: []
  about: "the causes of tenure-related stigma"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have systematic understanding of analysing what leads to stigma attached to housing tenure."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.3.b19
  locator: { number: "4.3.b19", headingPath: ["Benchmark standards", "Threshold level (3rd class)"] }
  span: { start: 70000, end: 70106 }
  source: "for accredited courses, ensure requirements of CIH specification are fully met. Typical level (2:1 or 2:2)"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "accredited honours courses"
  addressee: provider
  verbs: ["ensure", "met"]
  about: "CIH specification met in full on accredited courses"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On accredited courses, the requirements of the CIH specification are to be met in full, as part of the threshold."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/housing-studies-2022/4.4
  locator: { number: "4.4", headingPath: ["Benchmark standards", "Typical level (2:1 or 2:2)"] }
  span: { start: 70107, end: 70315 }
  source: "4.4 Criteria for achievement above threshold level at 2:1 and 2:2 will be in line with the higher education provider's common or generic marking schemes for undergraduate courses. Excellent level (1st class)\n"
  stem: none
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at 2:1 and 2:2"
  addressee: both
  verbs: []
  about: "typical rung set by providers' marking schemes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Criteria for achievement above the threshold at 2:1 and 2:2 will follow each provider's common or generic undergraduate marking scheme; the statement lists no typical items."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.5
  locator: { number: "4.5", headingPath: ["Benchmark standards", "Excellent level (1st class)"] }
  span: { start: 70315, end: 70522 }
  source: "4.5 Criteria for excellent (1st class achievement) will be in line with the higher education provider's common or generic marking schemes for undergraduate courses. Master's level degrees in Housing Studies\n"
  stem: none
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at first class"
  addressee: both
  verbs: []
  about: "excellent rung set by providers' marking schemes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Criteria for excellent, first-class achievement will follow each provider's common or generic undergraduate marking scheme; the statement lists no excellent items."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.6.b1.masters
  locator: { number: "4.6.b1.masters", headingPath: ["Benchmark standards", "Master's level degrees in Housing Studies"] }
  span: { start: 70904, end: 70954 }
  source: "evaluate current research and advanced scholarship"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in Housing Studies"
  addressee: learner
  verbs: ["evaluate"]
  about: "evaluating current research and advanced scholarship"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to judge current research and advanced scholarship."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.6.b2.masters
  locator: { number: "4.6.b2.masters", headingPath: ["Benchmark standards", "Master's level degrees in Housing Studies"] }
  span: { start: 70957, end: 71010 }
  source: "understand how knowledge is advanced through research"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in Housing Studies"
  addressee: learner
  verbs: ["understand"]
  about: "how research advances knowledge"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will understand the ways research moves knowledge forward."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.6.b3.masters
  locator: { number: "4.6.b3.masters", headingPath: ["Benchmark standards", "Master's level degrees in Housing Studies"] }
  span: { start: 71013, end: 71049 }
  source: "identify the boundaries of knowledge"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in Housing Studies"
  addressee: learner
  verbs: ["identify"]
  about: "the limits of current knowledge"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to recognise where present knowledge stops."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.6.b4.masters
  locator: { number: "4.6.b4.masters", headingPath: ["Benchmark standards", "Master's level degrees in Housing Studies"] }
  span: { start: 71052, end: 71094 }
  source: "create new insights in the field of study."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in Housing Studies"
  addressee: learner
  verbs: ["create"]
  about: "creating new insight in the field"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to produce new insight in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.6.masters
  locator: { number: "4.6.masters", headingPath: ["Benchmark standards", "Master's level degrees in Housing Studies"] }
  span: { start: 70526, end: 70793 }
  source: "Master's level degrees in Housing Studies are awarded to students who demonstrate understanding of knowledge in the housing domain, as outlined in the undergraduate threshold, much of which is at the forefront of the academic field of study and professional practice."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in Housing Studies"
  addressee: learner
  verbs: ["demonstrate"]
  about: "understanding of housing knowledge much of it at the forefront of research and practice"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown understanding of the housing knowledge set out for the honours threshold, much of it at the leading edge of scholarship and professional practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.7
  locator: { number: "4.7", headingPath: ["Benchmark standards", "Master's level degrees in Housing Studies"] }
  span: { start: 71095, end: 71409 }
  source: "4.7 Higher level skills are developed and enhanced through self-directed academic and professional development, with master's level students expected to achieve according to the descriptor for a higher education qualification at Level 7 on the FHEQ and SCQF Level 11 on the FQHEIS. Transferable and generic skills\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: ["developed", "enhanced", "achieve"]
  about: "higher-level skills at the FHEQ Level 7 and FQHEIS Level 11 descriptor"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Higher-level skills grow through self-directed academic and professional development, and master's students are expected to achieve to the descriptor for a qualification at FHEQ Level 7 and SCQF Level 11 on the FQHEIS."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Transferable and generic skills"] }
  span: { start: 71514, end: 71662 }
  source: "work independently, and with others, to identify complex problems and produce a synthesis of the state of knowledge on a particular subject or topic"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate and postgraduate graduates"
  addressee: learner
  verbs: ["work", "identify", "produce"]
  about: "independent and joint work on complex problems and synthesis of knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Will be able to work alone and with others to find complex problems and draw together what is known on a subject or topic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Transferable and generic skills"] }
  span: { start: 71665, end: 71826 }
  source: "take personal responsibility for learning, demonstrate conceptual understanding, reach sound judgements and effectively communicate ideas to a range of audiences"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate and postgraduate graduates"
  addressee: learner
  verbs: ["take", "demonstrate", "reach", "communicate"]
  about: "ownership of learning, judgement and communicating ideas"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Will be able to own their learning, show conceptual understanding, judge soundly and communicate ideas well to varied audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Transferable and generic skills"] }
  span: { start: 71829, end: 72013 }
  source: "collaborate with others in assessed and non-assessed learning activities, including with colleagues from other disciplines, reflecting the inter-professional nature of housing practice"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate and postgraduate graduates"
  addressee: learner
  verbs: ["collaborate", "reflecting"]
  about: "collaboration across disciplines in assessed and other activities"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Will be able to work with others in assessed and unassessed activities, including people from other disciplines, as the inter-professional nature of housing work demands."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Transferable and generic skills"] }
  span: { start: 72016, end: 72133 }
  source: "demonstrate awareness of, and professional responsibility for, addressing issues of equality, diversity and inclusion"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate and postgraduate graduates"
  addressee: learner
  verbs: ["demonstrate", "addressing"]
  about: "awareness of and professional responsibility for equality, diversity and inclusion"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Will be able to show awareness of equality, diversity and inclusion issues and take professional responsibility for dealing with them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Transferable and generic skills"] }
  span: { start: 72136, end: 72281 }
  source: "use a variety of information and communications technology packages to assemble and evaluate information, including data, from a range of sources"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate and postgraduate graduates"
  addressee: learner
  verbs: ["use", "assemble", "evaluate"]
  about: "using ICT to gather and evaluate information and data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Will be able to use various information and communications technology packages to collect and judge information and data from many sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.8.b6
  locator: { number: "4.8.b6", headingPath: ["Benchmark standards", "Transferable and generic skills"] }
  span: { start: 72284, end: 72419 }
  source: "identify housing problems, including environmental and sustainability challenges, and formulate alternative solutions to these problems"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate and postgraduate graduates"
  addressee: learner
  verbs: ["identify", "formulate"]
  about: "identifying housing problems, sustainability included, and alternative solutions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Will be able to recognise housing problems, environmental and sustainability ones among them, and devise other possible solutions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.8.b7
  locator: { number: "4.8.b7", headingPath: ["Benchmark standards", "Transferable and generic skills"] }
  span: { start: 72426, end: 72530 }
  source: "reflect on and manage their own learning and personal development, and ethical and professional practice"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate and postgraduate graduates"
  addressee: learner
  verbs: ["reflect", "manage"]
  about: "reflecting on and managing learning, development and ethical practice"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Will be able to reflect on and direct their own learning and personal development and their ethical and professional practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/housing-studies-2022/4.8.b8
  locator: { number: "4.8.b8", headingPath: ["Benchmark standards", "Transferable and generic skills"] }
  span: { start: 72533, end: 72673 }
  source: "consciously reflect on and utilise their learning to enhance employability and entrepreneurship as appropriate to their desired career path."
  stem: "4.8"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate and postgraduate graduates"
  addressee: learner
  verbs: ["reflect", "utilise", "enhance"]
  about: "using learning for employability and entrepreneurship"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Will be able to reflect deliberately on their learning and use it to improve employability and entrepreneurship in line with the career they want."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/housing-studies-2022/1.10
  forPractitioner: { text: "Plan content so that it will take account of how housing law, policy and governance differ between the four nations, and of the different housing bodies in each, rather than teaching one nation's system as the UK model.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will learn how housing law, policy and governance differ between England, Scotland, Wales and Northern Ireland, and which housing bodies work in each.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider expectation, worded 'will need to', that Housing Studies courses take account of the differences in housing law, policy and governance across the four UK nations. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.10. Do not present it as a regulatory rule or as an outcome a student must show on its own. Set it beside the threshold item on comparative housing systems (qaa/housing-studies-2022/4.3.b8)."
  author-agent-dialogue: "Raise it when a programme team plans law and policy content, or when a student asks why other nations' systems appear in the course. With staff, ask which modules compare the four nations and where the devolved housing bodies are taught; with a student, ask which nation's system they expect to work in and what they know of the others. Avoid treating one nation's arrangements as the norm for the UK."
- statement: qaa/housing-studies-2022/1.13
  forPractitioner: { text: "Put an inclusive curriculum at the centre of teaching: assume some students may have known housing precarity at first hand, draw on the many policy networks the subject touches and encourage students to challenge decisions made in policy and in practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will study in a curriculum built around inclusion and social justice, one that recognises that you or others in your group may have lived through housing insecurity and that encourages you to challenge decisions in policy and practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expectation, worded 'will', about how housing studies is taught: an inclusive curriculum rooted in social justice, at any level of the subject. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.13. Do not turn it into a student outcome or a regulatory duty. Set it beside the inclusive behaviours (para 1.19) and the threshold item on addressing social inequalities (qaa/housing-studies-2022/4.3.b7)."
  author-agent-dialogue: "Raise it when a team reviews its curriculum for inclusion, or when a student says the course touches their own housing history. For staff, ask where the course acknowledges students' lived experience of precarity and where students practise challenging decisions; for a student, ask whether they feel able to bring their own experience into discussion if they wish. Avoid pressing any student to disclose their own housing circumstances."
- statement: qaa/housing-studies-2022/1.15
  forPractitioner: { text: "Graduates will leave able to reflect on themselves and to engage stakeholders across policy, practice and other disciplines strategically, collaboratively and critically; design support that lets them practise challenging decisions with housing knowledge behind them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop the self-awareness and confidence to work with people across policy, practice and other disciplines, strategically and critically, and to challenge their decisions using what you know about housing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected graduate outcome, worded 'will', within the statement's section on equality, diversity and inclusion: confidence to engage and challenge stakeholders, a generic skill read at FHEQ Level 6 for honours. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.15. Do not claim it is a threshold item; it sits outside the rung list. Set it beside qaa/housing-studies-2022/4.8.b2, qaa/fheq-2024/4.15.b9.1 and spine:6."
  author-agent-dialogue: "Raise it when a student is preparing for placements, meetings with stakeholders or a debate on policy. Put it plainly: you are expected to grow the confidence to question decisions, using your housing knowledge. Ask: 'When did you last challenge a decision in a group, and what evidence did you use?' Avoid presenting it as a test they must already pass."
- statement: qaa/housing-studies-2022/1.22
  forPractitioner: { text: "Orient the course towards the social, economic and environmental concerns behind the 17 SDGs, so that its purpose is visible in module aims and content.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course design; the student meets it through the curriculum", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on course design: Housing Studies courses are aimed at the social, economic and environmental concerns of the UN Sustainable Development Goals. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.22. Do not present it as a student outcome or as binding regulation. Set it beside the ESD paragraphs 1.25 and 1.28 (qaa/housing-studies-2022/1.25, qaa/housing-studies-2022/1.28) and the Advance HE and QAA ESD guidance (std:doc:qaa-advancehe-esd-2021-guidance)."
  author-agent-dialogue: "Raise it with a programme team reviewing aims or validation documents. Ask: 'Where do your module aims name the SDGs or the concerns behind them?' and 'Which goal does each core module serve?' Avoid putting this to a student as something they must do."
- statement: qaa/housing-studies-2022/1.23
  forPractitioner: { text: "Give the course enough sustainability content, tied to SDG 11 and to goals such as 1, 3, 5 and 7, that students can discuss sustainability in a housing context with knowledge and confidence.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect enough teaching on sustainability, such as the UN goal on sustainable cities and goals on poverty, health, gender equality and energy, to discuss it confidently in housing.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an expectation on courses (the statement says 'the expectation is', a word outside must, should, may and will): enough sustainability content for students to be aware and confident in discussing it. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.23. Do not convert it into a 'must' or a threshold outcome. Set it beside the threshold item on environmental sustainability (qaa/housing-studies-2022/4.3.b16) and spine:6."
  author-agent-dialogue: "Raise it when a team checks sustainability coverage, or when a student asks how housing links to the SDGs. Ask a student: 'Could you explain how housing quality affects health or energy use?'; ask staff which modules teach SDG 11 and its housing target. Avoid reading the SDG list aloud at length."
- statement: qaa/housing-studies-2022/1.25
  forPractitioner: { text: "Write ESD outcomes that join housing knowledge and skills to the UNESCO sustainability competencies and the 17 SDGs; develop the competencies progressively across levels and make sure assessment evidences them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on outcome writing and assessment design; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on writing course and module outcomes for ESD, with a further stated expectation that the UNESCO competencies are developed progressively and assessed. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.25. Do not present the UNESCO competency list (Figure 2, para 1.24) as threshold outcomes. Set it beside qaa/housing-studies-2022/1.28, the ESD guidance (std:doc:qaa-advancehe-esd-2021-guidance) and spine:6 for the honours level."
  author-agent-dialogue: "Raise it with a team drafting outcomes or an assessment map. Ask: 'Which outcome in each module links a housing topic to a sustainability competency or SDG?' and 'Which assessment shows the competency was reached?' Avoid treating the competency figure as a checklist every module must cover."
- statement: qaa/housing-studies-2022/1.26.b1
  forPractitioner: { text: "Make room in the course for learning that crosses disciplines, for example shared modules or joint projects with planning, health or built environment students.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition of the learning environment, provided by the course", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a condition the statement says ESD requires ('requires', read as must) of the learning environment: learning across disciplines. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.26 (first item). Do not present it as a student outcome. Set it beside the matching item in para 3.14 (qaa/housing-studies-2022/3.14.b1)."
  author-agent-dialogue: "Raise it when a team plans shared or cross-disciplinary teaching. Ask: 'Where do students learn alongside other disciplines?' Avoid presenting it to a student as something they must arrange."
- statement: qaa/housing-studies-2022/1.26.b2
  forPractitioner: { text: "Design ESD learning to be inclusive and accessible to all students, including off-campus and site-based activity.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition of the learning environment, provided by the course", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a condition ESD requires of the learning environment: inclusive and accessible learning for all. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.26 (second item). Do not present it as a student outcome. Set it beside the accessibility paragraph (qaa/housing-studies-2022/2.5) and qaa/housing-studies-2022/3.14.b2."
  author-agent-dialogue: "Raise it when sustainability activities involve visits or fieldwork. Ask: 'Could every student take part in this activity as planned?' Avoid presenting it to a student as something they must arrange."
- statement: qaa/housing-studies-2022/1.26.b3
  forPractitioner: { text: "Check that assessment regulations allow synoptic tasks that draw on several modules.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition set by the course regulations", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a condition ESD requires: policies that permit synoptic assessment. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.26 (third item). Do not present it as a student outcome. Set it beside qaa/housing-studies-2022/3.14.b6."
  author-agent-dialogue: "Raise it with a team reviewing assessment regulations. Ask: 'Do your rules allow a task that draws on more than one module?' Avoid presenting it to a student as something they must arrange."
- statement: qaa/housing-studies-2022/1.26.b4
  forPractitioner: { text: "Offer extra-curricular and co-curricular sustainability opportunities and give them formal recognition.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition of the learning environment, provided by the course", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a condition ESD requires: extra and co-curricular opportunities, offered and recognised. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.26 (fourth item). Do not present it as a student outcome. Set it beside qaa/housing-studies-2022/3.14.b4."
  author-agent-dialogue: "Raise it when a team plans activity outside the timetable. Ask: 'How is sustainability work done outside modules recognised?' Avoid presenting it to a student as something they must arrange."
- statement: qaa/housing-studies-2022/1.26.b5
  forPractitioner: { text: "Use the campus, outdoor settings and other spaces as places where students develop and demonstrate sustainability competencies.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition of the learning environment, provided by the course", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a condition ESD requires: full use of campus and outdoor spaces as alternative settings for sustainability competencies. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.26 (fifth item). Do not present it as a student outcome. Set it beside the living laboratory paragraph (qaa/housing-studies-2022/1.27) and qaa/housing-studies-2022/3.14.b5."
  author-agent-dialogue: "Raise it when a team looks for settings beyond the classroom. Ask: 'Which places on or near campus could students use to study housing and sustainability?' Avoid presenting it to a student as something they must arrange."
- statement: qaa/housing-studies-2022/1.27
  forPractitioner: { text: "Use the campus, the local community and online spaces as settings for learning and assessment, for instance as a living laboratory for housing questions, so that students build sustainability understanding and competencies in more than one environment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You can expect some of your learning and assessment to happen on campus, in the local community or online, treating real places as a living laboratory for housing and sustainability.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on teaching, learning and assessment, with a stated expectation that varied environments are used to develop sustainability competencies. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.27. Do not present the living laboratory as compulsory for every module. Set it beside qaa/housing-studies-2022/1.26.b5 and qaa/housing-studies-2022/3.11."
  author-agent-dialogue: "Raise it when a team designs authentic tasks or field activity. Ask staff: 'Which assessment uses a real local housing setting?'; ask a student which local place they would study to see sustainability in practice. Avoid implying that online-only students miss the requirement."
- statement: qaa/housing-studies-2022/1.28
  forPractitioner: { text: "Embed sustainable development in the design of both the course and its modules, and provide environments in which students build the knowledge and skills to act for sustainable communities and to connect housing with health and education.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on curriculum design; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on curriculum design: sustainable development embedded at course and module level. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.28. Do not present it as a student outcome or as regulatory. Set it beside qaa/housing-studies-2022/1.25 and qaa/housing-studies-2022/1.29."
  author-agent-dialogue: "Raise it when a team maps sustainability across its modules. Ask: 'Is sustainable development part of each module's design, or added in one place only?' Avoid putting the design duty to a student."
- statement: qaa/housing-studies-2022/1.29
  forPractitioner: { text: "Make ESD visible in what modules teach, how they teach it, how they are structured and how they assess; use case studies, project-based research and community visits where symptoms of unsustainability show.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on module design; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on modules: ESD present in content, teaching, structure, delivery and assessment. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.29. Do not present the suggested methods (case studies, visits) as required. Set it beside qaa/housing-studies-2022/1.28 and qaa/housing-studies-2022/3.14.b3."
  author-agent-dialogue: "Raise it when a module leader reviews a module. Ask: 'Where does sustainability show in this module's assessment, not only its content?' Avoid putting it to a student as their duty."
- statement: qaa/housing-studies-2022/1.30
  forPractitioner: { text: "Focus ESD content on physical environmental integrity, social justice and economic development, include under-represented voices and other disciplines, and keep improving physical and digital learning spaces for sustainability.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on content and learning environments; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on ESD content and on the subject area's learning environments. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.30. Do not present it as a student outcome. Set it beside qaa/housing-studies-2022/1.29 and the content item on sustainable development perspectives (para 3.1)."
  author-agent-dialogue: "Raise it when a team reviews reading lists and ESD topics. Ask: 'Do the sources in this module include voices from under-represented communities?' Avoid putting the duty to a student."
- statement: qaa/housing-studies-2022/1.34
  forPractitioner: { text: "Graduates will carry transferable skills into current and emerging housing roles: self-management and motivating others, identifying housing problems, taking responsibility for ideas and decisions, managing risk and recognising the bounds of their own professional judgement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will gain skills you can use in housing jobs now and in new roles that technology creates: managing yourself, motivating others, spotting housing problems, taking ownership of ideas and decisions, handling risk and knowing where your professional judgement stops.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected graduate outcome, worded 'will', in the statement's employability section: transferable and self-management skills, a generic skill read at FHEQ Level 6 for honours and Level 7 for a master's. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.34. Do not claim it is on the threshold list. Set it beside qaa/housing-studies-2022/4.8.b1, qaa/housing-studies-2022/4.8.b6, qaa/fheq-2024/4.15.b9.2 and spine:6."
  author-agent-dialogue: "Raise it when a student asks what employers will expect, or prepares for a placement or interview. Put it in plain words and ask: 'Tell me about a housing problem you identified and the decision you took about it' or 'Where are the limits of what you would decide alone?' Avoid presenting all of it as a minimum they must already have."
- statement: qaa/housing-studies-2022/1.35
  forPractitioner: { text: "Graduates will combine broad housing knowledge with reflective, self-directed professional development, transfer good practice from allied fields, act ethically with attention to equality and diversity and stay resilient and adaptable in a changing sector.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know housing broadly, from policy and finance to sustainability and equality; reflect on your own skills, especially as technology changes; take charge of your own development; borrow good practice from fields such as health; and work ethically, resiliently and creatively as things change.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected graduate outcome, worded 'will', in the employability section: a profile of the reflective, ethical and adaptable housing professional, a generic skill read at FHEQ Level 6 for honours. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 1.35. Do not claim it is on the threshold list or that every clause is assessed. Set it beside qaa/housing-studies-2022/4.8.b7, qaa/fheq-2024/4.15.b9.3, qaa/fheq-2024/annex-d/transferable/r5/3rd and spine:6."
  author-agent-dialogue: "Raise it in personal tutoring or reflective writing on professional development. Ask: 'Which part of housing practice is changing fastest for you, and how are you keeping up?' and 'Where have you used an idea from another field?' Avoid reading the whole paragraph aloud."
- statement: qaa/housing-studies-2022/2.5
  forPractitioner: { text: "Design spaces, materials and site visits for students with learning, sensory or mobility needs and for those whose earlier education was limited by disadvantage; make adjustments in line with national frameworks and institutional services so that everyone can participate fully.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to take a full part in your course whatever your learning or mobility needs or your background, with adjustments and support where you need them, including on site visits.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on providers: accessible environments, materials and site visits, with adjustments for disabled students and those affected by structural inequality. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 2.5. Do not present it as a student outcome or as the provider's whole legal duty, which lies in equality law. Set it beside qaa/housing-studies-2022/1.26.b2 and qaa/housing-studies-2022/3.16."
  author-agent-dialogue: "Raise it when a site visit or new material is planned, or when a student mentions a barrier to taking part. For staff, ask: 'Could a wheelchair user or a dyslexic student join this visit and use these materials as planned?'; for a student, ask what would help them take part fully and point them to support. Avoid asking a student to justify their need."
- statement: qaa/housing-studies-2022/2.6
  forPractitioner: { text: "Design content so that students who have faced housing problems are not put off by it and can choose to share their experience; recruit flexibly, for example through whole-person approaches, links with feeder providers and induction support in academic writing and critical thinking for non-traditional entrants.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you have lived through housing problems yourself, the course should let you engage with that content safely and share your experience only if you wish; if you come from housing work rather than academic study, you should find a route in and support to start.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on recruitment flexibility, with course design advised to recognise students' lived experience of housing. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 2.6. Do not present it as an entry requirement or a student outcome. Set it beside qaa/housing-studies-2022/1.13 and qaa/housing-studies-2022/2.11."
  author-agent-dialogue: "Raise it when a team plans admissions or content on homelessness and precarity. Ask staff: 'How does a student with lived experience opt in or out of sharing it?'; ask an applicant from the sector what support with academic writing would help. Avoid probing a student's own housing history."
- statement: qaa/housing-studies-2022/2.7
  forPractitioner: { text: "Plan each level of the honours course to build towards the full set of threshold subject and generic skills by the end; in joint honours, expect part of the set to be met here and the rest supplied by the other subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As you move through each year of an honours degree you will build up, step by step, everything the threshold asks; if you study housing as a joint subject you will meet part of it here and add skills from your other subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation, worded 'will', that progression through the honours levels leads to all the threshold skills, with joint honours meeting part of them. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 2.7, which also states the FHEQ Level 6 and FQHEIS Level 10 equivalence. Do not claim the statement sets outcomes for each year. Set it beside the threshold list (qaa/housing-studies-2022/4.3.b1 to 4.3.b18), qaa/housing-studies-2022/4.8.b1 and spine:6."
  author-agent-dialogue: "Raise it when a student asks how this year connects to the final standard, or a team maps outcomes by level. Ask: 'Which threshold items does this year's work build towards?' Avoid telling a first-year student they must already meet the final threshold."
- statement: qaa/housing-studies-2022/2.11
  forPractitioner: { text: "Write RPL and course regulations so that postgraduate entrants with alternative, equivalent or dated experience are not disadvantaged, and offer support such as study skills packages to every student.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you join with work experience instead of the usual qualifications, the rules should not count against you, and you should be able to get support, such as help with study skills, regulations and difficulties.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on postgraduate regulations and support: RPL that does not disadvantage alternative entrants, and support for all. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 2.11. Do not present RPL as an entitlement to exemption. Set it beside qaa/housing-studies-2022/2.6 and qaa/housing-studies-2022/3.4."
  author-agent-dialogue: "Raise it with an admissions tutor or an applicant from the housing sector. Ask: 'Would an applicant with ten years' practice and an old diploma be treated fairly by our rules?' or ask the applicant what prior learning they want recognised. Avoid promising a student exemption the regulations may not give."
- statement: qaa/housing-studies-2022/2.15
  forPractitioner: { text: "Build partnerships with housing employers to secure the prescribed work experience that CIH chartered membership requires; convene employer groups that meet regularly and invite partners to comment on curriculum and skills development.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you are aiming for chartered membership of the Chartered Institute of Housing, you must complete set work experience in a housing role; your course works with employers to help you find it and to bring guest speakers and projects.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe the requirement as the professional body's: CIH chartered membership accreditation requires prescribed work experience in a housing role ('requires', read as must); the employer groups are only 'anticipated' of providers. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 2.15. Do not claim the statement itself makes work experience compulsory for every degree. Set it beside qaa/housing-studies-2022/2.19, qaa/housing-studies-2022/4.3.b19 and qaa/housing-studies-2022/4.8.b8."
  author-agent-dialogue: "Raise it when a student asks about chartered membership, placements or working while studying. Ask a student: 'Do you intend to seek chartered membership, and where could you gain the work experience it needs?'; ask staff how employer groups shape the curriculum. Avoid telling a student who is not seeking membership that the experience is compulsory."
- statement: qaa/housing-studies-2022/2.16
  forPractitioner: { text: "In monitoring and periodic review, use this statement among other external reference points to check that provision matches sector norms, and use monitoring data to understand achievement and plan ahead.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a quality assurance duty on the awarding body", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation, worded 'will', that awarding bodies use this statement as an external reference point in review. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 2.16. Do not claim the statement is binding in review in England, where its front matter says it is not a sector-recognised standard. Set it beside qaa/housing-studies-2022/2.17."
  author-agent-dialogue: "Raise it with a team preparing periodic review. Ask: 'Which parts of the statement did you check the course against, and what did you find?' Avoid putting it to a student."
- statement: qaa/housing-studies-2022/2.17
  forPractitioner: { text: "Include external reviewers in periodic review so that proposed changes get an outside view and threshold standards and subject content are confirmed.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a quality assurance duty on the provider", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation, worded 'will', that providers use external reviewers to confirm threshold standards and content. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 2.17. Do not present it as a student matter. Set it beside qaa/housing-studies-2022/2.16 and the threshold list (para 4.3)."
  author-agent-dialogue: "Raise it with a team choosing external reviewers. Ask: 'Will the reviewer check the course against the threshold items in para 4.3?' Avoid putting it to a student."
- statement: qaa/housing-studies-2022/2.19
  forPractitioner: { text: "If the course seeks or holds CIH accreditation, deliver the content and skills the CIH requires and engage with the CIH, as it requires, before changing content or delivery.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition on accredited courses, met by the provider", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a condition on CIH-accredited courses ('need to be delivered', 'required engagement', read as must): the CIH's requirements govern core content and changes. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 2.19. Do not present the CIH's requirements as part of this statement; they are the body's own (not yet ingested, Part E). Set it beside qaa/housing-studies-2022/4.3.b19 and qaa/housing-studies-2022/2.15."
  author-agent-dialogue: "Raise it when an accredited course plans a change. Ask: 'Does this change touch content the CIH requires, and have you engaged the CIH?' Avoid putting it to a student."
- statement: qaa/housing-studies-2022/3.3
  forPractitioner: { text: "Make the fit between methods and intended outcomes explicit; use a variety of approaches for different learners; on an accredited course, include work-based or work-related learning for students new to housing and for those already in it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You can expect a mix of teaching and assessment that suits different ways of learning; on a professionally accredited course you will have chances to learn through or about work, whether you are new to housing or already work in it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation on the strategy ('is expected to', outside the five force words) with a firmer 'will' for work-based or work-related learning on accredited courses. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.3. Do not present work-based learning as required on unaccredited courses. Set it beside qaa/housing-studies-2022/2.15 and qaa/housing-studies-2022/3.7."
  author-agent-dialogue: "Raise it when a team writes or reviews its learning and assessment strategy. Ask: 'Where does the strategy show why each method fits the outcomes?' and 'What work-related learning do students new to housing get?' Avoid putting it to a student as their task."
- statement: qaa/housing-studies-2022/3.4
  forPractitioner: { text: "Keep the strategy student-centred and reviewed, recognise what students already know and have done, make exemption routes clear, involve housing practitioners where useful and align activities with EDI and ESD themes.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect your course to recognise what you already know from life and work, to make clear whether any part can be exempted and to build in equality, inclusion and sustainability.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an expectation (the statement says 'anticipated' and 'expected', words outside the five), not a requirement: a student-centred strategy that recognises prior learning. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.4. Do not present the exemption route as an entitlement. Set it beside qaa/housing-studies-2022/2.11 and qaa/housing-studies-2022/3.3."
  author-agent-dialogue: "Raise it when a team reviews its strategy or a student asks whether experience counts. Ask staff: 'How does a student find out what prior learning could exempt them?' Avoid promising a student an exemption."
- statement: qaa/housing-studies-2022/3.6
  forPractitioner: { text: "Tell students clearly what digital technology they need and offer training; support use of the library; where delivery is virtual or blended, plan for students on the wrong side of the digital divide and, where you can, point applicants to preparatory resources.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be told clearly what technology you need and offered training, shown how to use the library well and, if you study online or in a blended way, supported if you lack equipment or connection.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on courses and institutions: clear digital expectations, library support and attention to the digital divide. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.6. Do not present it as a student outcome. Set it beside qaa/housing-studies-2022/3.8 and qaa/housing-studies-2022/4.8.b5."
  author-agent-dialogue: "Raise it when a course moves online or a student struggles with access. Ask a student: 'Do you have the device and connection the course expects, and do you know where to ask for help?'; ask staff where the digital requirements are published. Avoid assuming every student has reliable access."
- statement: qaa/housing-studies-2022/3.7
  forPractitioner: { text: "Use several teaching approaches, for example lectures, small-group work, one-to-one supervision, directed study, site visits with reasonable adjustments, problem-based and team work, and negotiated or work-related learning that serves employability.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect a mix of teaching, such as lectures, seminars, supervision, guided study, site visits, problem-solving in teams and learning through work.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an expectation ('it is expected', a word outside the five) that a range of teaching approaches is used; the list is examples, not a required set. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.7. Do not present any single example as mandatory. Set it beside qaa/housing-studies-2022/3.3 and qaa/housing-studies-2022/3.11."
  author-agent-dialogue: "Raise it when a team reviews its teaching mix. Ask: 'Which learners might this module's methods leave out?' Avoid reading the list of examples aloud as a checklist."
- statement: qaa/housing-studies-2022/3.8
  forPractitioner: { text: "Provide accessible materials and complete, accurate documentation; for every module, state clear and achievable outcomes and indicate the reading and resources that support them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be given clear, achievable outcomes for every module, with guidance on what to read, and accessible, accurate information about your course.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation, worded 'will' for module outcomes and 'expected' for materials. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.8. Do not present it as a student outcome. Set it beside qaa/housing-studies-2022/2.5 and qaa/housing-studies-2022/3.15."
  author-agent-dialogue: "Raise it when a module handbook is drafted or a student cannot find what a module expects. Ask a student: 'Do you know what this module's outcomes are and what to read for them?' Avoid treating unclear outcomes as the student's fault."
- statement: qaa/housing-studies-2022/3.11
  forPractitioner: { text: "Use teaching that surfaces alternative viewpoints, reflection and real-world challenges; treat campus, community and sector settings as a living laboratory and use digital tools to record and share that learning inclusively.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should meet different viewpoints, reflect on experience and work on real housing challenges, often in the community, on campus or online.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on teaching practices and courses: alternative viewpoints, reflection, real-world challenges and diverse settings. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.11. Do not present the living laboratory as required for every module. Set it beside qaa/housing-studies-2022/1.27 and qaa/housing-studies-2022/3.12."
  author-agent-dialogue: "Raise it when a team designs an authentic task. Ask: 'Which real local housing challenge could students work on in this module?' Avoid presenting it to a student as their duty."
- statement: qaa/housing-studies-2022/3.12
  forPractitioner: { text: "Broaden reading lists with tenant voices and under-represented communities, reconsider historical approaches and decolonise the curriculum, aim for learning that changes how students think and practise and give interdisciplinary experiences beyond UK-centred housing practice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should read and hear from a wider range of voices, including tenants and under-represented communities, question how housing history has been told and look beyond UK practice, so that you can speak up well for sustainable development.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a set of 'should' expectations on course design: diverse voices, decolonisation, transformative learning and interdisciplinary experience. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.12. Do not present it as a student outcome. Set it beside qaa/housing-studies-2022/1.30 and the content item on decolonising the curriculum (para 3.1)."
  author-agent-dialogue: "Raise it when a team reviews reading lists or module aims. Ask: 'Whose voices are missing from this module's sources, and where do tenants speak for themselves?' Avoid putting the duty to a student."
- statement: qaa/housing-studies-2022/3.13
  forPractitioner: { text: "Use digital and blended methods creatively and equitably, set real problems and group tasks (online too) and promote critical reflection on students' own perspectives and those of others.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be given chances to reflect critically on your own views and those of others, often through group work and blended learning on real housing problems.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on promoting critical reflection, set in a description of blended learning. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.13. Do not present blended delivery as required. Set it beside qaa/housing-studies-2022/4.8.b3 and qaa/housing-studies-2022/4.8.b7."
  author-agent-dialogue: "Raise it when a team designs online group tasks. Ask: 'Where in this task do students reflect on a view they disagree with?' Avoid putting it to a student as a rule."
- statement: qaa/housing-studies-2022/3.14.b1
  forPractitioner: { text: "Provide learning that crosses disciplines, such as shared modules or joint projects.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition of the learning environment, provided by the course", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a condition housing studies education requires ('requires', read as must) of its learning environment: learning across disciplines. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.14 (first item). Do not present it as a student outcome. Set it beside qaa/housing-studies-2022/1.26.b1 and qaa/housing-studies-2022/4.8.b3."
  author-agent-dialogue: "Raise it when a team plans shared teaching. Ask: 'Where do students learn with other disciplines?' Avoid presenting it to a student as something they must arrange."
- statement: qaa/housing-studies-2022/3.14.b2
  forPractitioner: { text: "Make every part of learning inclusive and accessible to all students.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition of the learning environment, provided by the course", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a condition housing studies education requires: inclusive and accessible learning. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.14 (second item). Do not present it as a student outcome. Set it beside qaa/housing-studies-2022/2.5 and qaa/housing-studies-2022/1.26.b2."
  author-agent-dialogue: "Raise it when a team reviews access to its activities. Ask: 'Who could not take part in this activity as designed?' Avoid presenting it to a student as something they must arrange."
- statement: qaa/housing-studies-2022/3.14.b3
  forPractitioner: { text: "Let sustainable development underpin learning across the course, not one module alone.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition of the learning environment, provided by the course", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a condition housing studies education requires: ESD as a foundation of learning. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.14 (third item). Do not present it as a student outcome. Set it beside qaa/housing-studies-2022/1.28 and qaa/housing-studies-2022/1.29."
  author-agent-dialogue: "Raise it when a team maps ESD. Ask: 'Which modules would lose their point without sustainability?' Avoid presenting it to a student as something they must arrange."
- statement: qaa/housing-studies-2022/3.14.b4
  forPractitioner: { text: "Offer and formally recognise extra and co-curricular opportunities.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition of the learning environment, provided by the course", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a condition housing studies education requires: extra and co-curricular opportunities, offered and recognised. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.14 (fourth item). Do not present it as a student outcome. Set it beside qaa/housing-studies-2022/1.26.b4."
  author-agent-dialogue: "Raise it when a team plans activity outside modules. Ask: 'How is work outside the timetable recognised?' Avoid presenting it to a student as something they must arrange."
- statement: qaa/housing-studies-2022/3.14.b5
  forPractitioner: { text: "Use campus, outdoor and virtual spaces as settings in which students develop and show sustainability competencies.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition of the learning environment, provided by the course", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a condition housing studies education requires: full use of campus, outdoor and virtual spaces for ESD competencies. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.14 (fifth item). Do not present it as a student outcome. Set it beside qaa/housing-studies-2022/1.26.b5 and qaa/housing-studies-2022/3.11."
  author-agent-dialogue: "Raise it when a team looks for settings beyond the lecture room, virtual ones included. Ask: 'Which space could host a sustainability task in this module?' Avoid presenting it to a student as something they must arrange."
- statement: qaa/housing-studies-2022/3.14.b6
  forPractitioner: { text: "Allow synoptic assessment in regulations so that students can link and integrate learning across modules as they progress.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition set by the course regulations", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a condition housing studies education requires: policies supporting synoptic assessment that links modules. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.14 (sixth item). Do not present it as a student outcome. Set it beside qaa/housing-studies-2022/1.26.b3 and qaa/housing-studies-2022/4.8.b1."
  author-agent-dialogue: "Raise it with a team reviewing assessment rules. Ask: 'Where do students pull several modules together in one task?' Avoid presenting it to a student as something they must arrange."
- statement: qaa/housing-studies-2022/3.15
  forPractitioner: { text: "For every assessment method, define aims, content requirements and marking criteria clearly and align them with the knowledge and skills taught, the teaching approaches and the course outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "For every assessment you should be told clearly what it is for, what it must contain and how it will be marked, and these should match what you were taught.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on assessment design: clear, aligned aims, content requirements and marking criteria for each method. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.15. Do not present it as a student outcome. Set it beside qaa/housing-studies-2022/3.16 and the Annex D bands (std:doc:qaa-fheq-2024-framework, Annex D)."
  author-agent-dialogue: "Raise it when a student is unsure what a task wants, or a team writes a brief. Ask a student: 'Can you find the criteria for this task and say what a strong answer needs?'; ask staff whether the criteria match the module outcomes. Avoid blaming the student for an unclear brief."
- statement: qaa/housing-studies-2022/3.16
  forPractitioner: { text: "Offer varied assessment methods, each open on equal terms whatever students' educational background or circumstances, document and share how assessment works and publish criteria for every summative task.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should have the chance to show everything you can do through a mix of assessments that work for students from any background, with the arrangements and marking criteria shared with you in advance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on giving students a fair chance to show their abilities through varied, accessible assessment, with an expectation that criteria are published. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.16. Do not present it as an outcome the student must show. Set it beside qaa/housing-studies-2022/2.5 and qaa/housing-studies-2022/3.15."
  author-agent-dialogue: "Raise it when a student feels one assessment type disadvantages them, or a team reviews its assessment mix. Ask a student: 'Which kind of assessment lets you show your strengths best?'; ask staff whether any student group is held back by the current mix. Avoid presenting a preferred format as a right to choose."
- statement: qaa/housing-studies-2022/3.20
  forPractitioner: { text: "Use a diverse range of methods so that every part of the knowledge, skills and standards can be evidenced, and make reasonable adjustments for disabled students.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect several kinds of assessment, so that you can show the full range of what you know and can do, with adjustments if you are disabled.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an expectation (the statement says 'anticipated', a word outside the five) that diverse methods evidence the knowledge, skills and standards. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 3.20. Do not convert it into a 'must'. Set it beside qaa/housing-studies-2022/3.16 and the threshold list (para 4.3)."
  author-agent-dialogue: "Raise it when a team checks whether its assessments cover every threshold item. Ask: 'Which threshold item has no assessment that evidences it?' Avoid presenting it to a student as their duty."
- statement: qaa/housing-studies-2022/4.2
  forPractitioner: { text: "When deciding what evidence shows performance above the threshold, use your own method but refer to Annex D's descriptions of the 1st, 2:1, 2:2 and 3rd at FHEQ Level 6 and FQHEIS Level 10.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in setting classification evidence", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a 'should' on providers: refer to Annex D of the qualification frameworks when judging performance above the threshold. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.2 and Annex D as std:doc:qaa-fheq-2024-framework, Annex D. Do not claim the statement sets its own classification criteria. Set it beside qaa/fheq-2024/annex-d/summary/r1/3rd and its 2.2, 2.1 and 1st cells, and spine:6."
  author-agent-dialogue: "Raise it when a team writes marking criteria for honours. Ask: 'Where do your criteria for a 2:1 and a first draw on Annex D?' Avoid putting it to a student as their duty."
- statement: qaa/housing-studies-2022/4.3.b1
  forPractitioner: { text: "At threshold, graduates understand systematically how housing shapes the well-being of residents and communities.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand in a systematic way how housing affects the well-being of the people and communities who live in it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of housing as a social determinant of well-being, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 1). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about housing as a social determinant of well-being, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'How does poor housing affect someone's health or well-being, and what evidence shows it?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b2
  forPractitioner: { text: "At threshold, graduates understand systematically the case for state intervention in housing markets and how production, consumption and experience of housing change.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand why governments step into the housing market and how the way homes are built, bought, rented and lived in keeps changing.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of state intervention and the changing production, consumption and experience of housing, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 2). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about state intervention and the changing production, consumption and experience of housing, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'Why might a government intervene in the housing market rather than leave it alone?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b3
  forPractitioner: { text: "At threshold, graduates understand systematically how housing problems evolve and are identified and how policy and legal frameworks respond.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand how housing problems come about and are recognised, and how policy and the law have changed to tackle them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of how housing problems emerge and the policy and legal responses, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 3). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about how housing problems emerge and the policy and legal responses, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'Pick one housing problem: how did it come to be seen as a problem, and what did law or policy do about it?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b4
  forPractitioner: { text: "At threshold, graduates understand systematically how local and national housing policy is formulated and put into effect and how it relates to wider public policy.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand how housing policy is made and put into practice locally and nationally, and how it links with other public policy.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of how housing policy is made and implemented, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 4). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about how housing policy is made and implemented, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'How does a national housing policy become something a local council does, and which other policies does it touch?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b5
  forPractitioner: { text: "At threshold, graduates understand systematically the forms of housing organisation, their governance and its challenges.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand the different types of housing organisation, how they are run and governed and what makes governing them hard.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of housing organisations and their governance, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 5). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about housing organisations and their governance, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'How is a housing association governed differently from a local authority housing department?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b6
  forPractitioner: { text: "At threshold, graduates understand systematically different models of housing need and how to develop systems that respond to diverse people and groups.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand the different ways of defining housing need and how to build systems that respond to many different people and groups.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of models of housing need and responsive systems, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 6). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about models of housing need and responsive systems, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'Which model of housing need would you use to plan for an ageing population, and what would it miss?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b7
  forPractitioner: { text: "At threshold, graduates understand systematically how housing organisations and professionals can tackle social inequalities structurally, institutionally and individually.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand how housing organisations and the people who work in them can tackle wider social inequality at every level, from systems to individuals.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of how housing bodies and professionals tackle wider social inequality, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 7). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd and qaa/housing-studies-2022/1.19 and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about how housing bodies and professionals tackle wider social inequality, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'Where could a housing officer reduce inequality in their own daily work, and where does it need change at a higher level?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b8
  forPractitioner: { text: "At threshold, graduates understand systematically how to compare housing systems and policies within the UK and internationally and how to identify and apply learning and good practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand how to compare housing systems across the UK nations and other countries, and how to pick out and use lessons that work elsewhere.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of comparative housing systems and transferring good practice, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 8). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b3.1, qaa/fheq-2024/annex-d/cognitive/r1/3rd and qaa/housing-studies-2022/1.10 and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about comparative housing systems and transferring good practice, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'What could one UK nation learn from another's approach to homelessness, and would it transfer?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b9
  forPractitioner: { text: "At threshold, graduates understand systematically the benefits of resident involvement in decisions and how to engage seldom-heard people and groups facing barriers.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand why it helps to involve residents in decisions and how to reach people and groups who are rarely heard because something stops them taking part.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of resident involvement and reaching seldom-heard groups, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 9). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about resident involvement and reaching seldom-heard groups, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'Which residents are hardest to hear in a consultation you know of, and what would reach them?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b10
  forPractitioner: { text: "At threshold, graduates understand systematically the main principles of housing economics and finance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand the main ideas of how housing economics and housing finance work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of housing economics and finance, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 10). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about housing economics and finance, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'What drives house prices and rents, and how is new social housing paid for?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b11
  forPractitioner: { text: "At threshold, graduates understand systematically the main principles of business planning, service management and service delivery.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand the main ideas behind business planning and how housing services are managed and delivered.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of business planning, service management and delivery, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 11). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about business planning, service management and delivery, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'How would a housing service plan and check whether it is delivering what tenants need?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b12
  forPractitioner: { text: "At threshold, graduates understand systematically how to identify and apply appropriate research methods and methodologies in housing contexts.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand how to choose the right research methods for a housing question and how to use them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of choosing and applying research methods in housing, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 12). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b2, qaa/fheq-2024/annex-d/practical/r1/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about choosing and applying research methods in housing, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'What method would you use to find out why tenants leave a scheme, and why that one?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b13
  forPractitioner: { text: "At threshold, graduates understand systematically how to identify solutions to housing issues grounded in evidence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand how to find answers to housing issues that are backed by evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of evidence-based solutions to housing issues, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 13). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b3.1, qaa/fheq-2024/annex-d/cognitive/r3/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about evidence-based solutions to housing issues, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'What evidence would persuade you that a solution to overcrowding actually works?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b14
  forPractitioner: { text: "At threshold, graduates understand systematically how to put information, data and concepts across to different audiences.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand how to present information, data and ideas to different kinds of audience.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of presenting information, data and concepts to varied audiences, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 14). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/transferable/r1/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about presenting information, data and concepts to varied audiences, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'How would you explain the same rent data to tenants and to a council committee?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b15
  forPractitioner: { text: "At threshold, graduates understand systematically the key principles of housing leadership and management and their application in housing organisations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand the main ideas of leadership and management in housing and how they are used in housing organisations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of leadership and management in housing organisations, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 15). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about leadership and management in housing organisations, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'What makes a good manager of a housing team, and how have you seen it done?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b16
  forPractitioner: { text: "At threshold, graduates understand systematically aspects of environmental sustainability, including the climate crisis's impact across the design, development, maintenance and management of housing.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand environmental sustainability in housing, including how the climate crisis affects the way homes are designed, built, maintained and managed.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of environmental sustainability and the climate crisis in housing, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 16). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd and qaa/housing-studies-2022/1.23 and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about environmental sustainability and the climate crisis in housing, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'How should the climate crisis change the way an older housing stock is maintained?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b17
  forPractitioner: { text: "At threshold, graduates understand systematically the principles of housing renewal, refurbishment and regeneration, resident engagement in them and equitable outcomes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand the main ideas of renewing, refurbishing and regenerating housing, how to involve residents and how to make the results fair.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of renewal, refurbishment and regeneration with resident engagement, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 17). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about renewal, refurbishment and regeneration with resident engagement, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'Who gains and who loses when an estate is regenerated, and how can residents shape it?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b18
  forPractitioner: { text: "At threshold, graduates understand systematically how to analyse the factors behind tenure-related stigma.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for an honours degree, you will understand how to analyse why people are stigmatised because of the kind of housing tenure they live in.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: systematic understanding of the causes of tenure-related stigma, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 18). Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). Set it beside qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r1/3rd and qaa/housing-studies-2022/1.16 and spine:6."
  author-agent-dialogue: "Raise it when a student asks what an honours degree in housing expects them to understand about the causes of tenure-related stigma, or when a team checks module coverage. For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. Ask: 'Why are social tenants sometimes stigmatised, and where does that come from?' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."
- statement: qaa/housing-studies-2022/4.3.b19
  forPractitioner: { text: "If the course is accredited by the CIH, make sure every requirement of its specification is fully met.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on accredited courses, not an understanding the student shows", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a condition placed in the threshold list for accredited courses only: the CIH specification must be fully met. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.3 (item 19). Do not present it as a learning outcome or as applying to unaccredited courses; the CIH specification is the body's own document (not yet ingested, Part E). Set it beside qaa/housing-studies-2022/2.19 and qaa/housing-studies-2022/2.15."
  author-agent-dialogue: "Raise it when an accredited course reviews its outcomes. Ask: 'Which CIH requirements does each module meet, and are any left uncovered?' Avoid putting it to a student as an item they must show."
- statement: qaa/housing-studies-2022/4.4
  forPractitioner: { text: "Judge 2:1 and 2:2 work against your institution's common or generic undergraduate marking scheme; the statement gives no subject list for this rung.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a 2:1 or a 2:2 you will be judged against your university's own marking scheme, which goes beyond the threshold.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the typical rung, stated as a 'will' that hands its criteria to each provider's marking scheme rather than listing outcomes. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.4. Do not invent subject-specific typical outcomes. Set it beside qaa/fheq-2024/annex-d/summary/r1/2.2 and qaa/fheq-2024/annex-d/summary/r1/2.1, the threshold list (qaa/housing-studies-2022/4.3.b1) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what a 2:1 needs in this subject. Put it plainly: the subject sets the floor, your university's marking scheme sets the 2:1 and 2:2. Ask: 'Have you read the marking criteria for your next assessment?' Avoid presenting the threshold items as enough for a 2:1."
- statement: qaa/housing-studies-2022/4.5
  forPractitioner: { text: "Judge first-class work against your institution's common or generic undergraduate marking scheme; the statement gives no subject list for this rung.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a first you will be judged against your university's own marking scheme for excellent work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung, stated as a 'will' that hands its criteria to each provider's marking scheme. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.5. Do not invent subject-specific excellent outcomes or treat them as the minimum. Set it beside qaa/fheq-2024/annex-d/summary/r1/1st, qaa/housing-studies-2022/4.4 and spine:6."
  author-agent-dialogue: "Raise it when a student asks what a first looks like. Put it plainly: the subject leaves it to your university's criteria, which usually reward independence and originality. Ask: 'What would make your next piece go beyond what was taught?' Avoid presenting first-class qualities as the pass mark."
- statement: qaa/housing-studies-2022/4.6.b1.masters
  forPractitioner: { text: "Master's graduates evaluate current research and advanced scholarship critically.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a master's you will be able to judge the quality and value of current research and advanced scholarship.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a condition of a master's award in Housing Studies, read at the threshold: evaluating current research and advanced scholarship, at FHEQ Level 7 (FQHEIS Level 11). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.6. Do not apply it to the honours degree or call it regulatory. Set it beside qaa/fheq-2024/4.17.b4.1 and spine:7."
  author-agent-dialogue: "Raise it with a master's student planning a dissertation or critical review, or with a team writing master's outcomes. Put it plainly in the second person for a student and as a minimum for the award for staff. Ask: 'Which recent housing study would you challenge, and on what grounds?' Avoid reading the paragraph aloud or confusing it with the honours threshold."
- statement: qaa/housing-studies-2022/4.6.b2.masters
  forPractitioner: { text: "Master's graduates understand how research advances knowledge.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a master's you will understand how research moves knowledge forward.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a condition of a master's award in Housing Studies, read at the threshold: how research advances knowledge, at FHEQ Level 7 (FQHEIS Level 11). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.6. Do not apply it to the honours degree or call it regulatory. Set it beside qaa/fheq-2024/4.17.b3 and spine:7."
  author-agent-dialogue: "Raise it with a master's student planning a dissertation or critical review, or with a team writing master's outcomes. Put it plainly in the second person for a student and as a minimum for the award for staff. Ask: 'How did one study you know change what the field thought about housing?' Avoid reading the paragraph aloud or confusing it with the honours threshold."
- statement: qaa/housing-studies-2022/4.6.b3.masters
  forPractitioner: { text: "Master's graduates identify where the limits of current knowledge lie.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a master's you will be able to see where current knowledge in housing runs out.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a condition of a master's award in Housing Studies, read at the threshold: the limits of current knowledge, at FHEQ Level 7 (FQHEIS Level 11). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.6. Do not apply it to the honours degree or call it regulatory. Set it beside qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it with a master's student planning a dissertation or critical review, or with a team writing master's outcomes. Put it plainly in the second person for a student and as a minimum for the award for staff. Ask: 'What question in your topic does nobody yet have a good answer to?' Avoid reading the paragraph aloud or confusing it with the honours threshold."
- statement: qaa/housing-studies-2022/4.6.b4.masters
  forPractitioner: { text: "Master's graduates create new insights in housing studies.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a master's you will be able to produce new insight in housing studies.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a condition of a master's award in Housing Studies, read at the threshold: creating new insight in the field, at FHEQ Level 7 (FQHEIS Level 11). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.6. Do not apply it to the honours degree or call it regulatory. Set it beside qaa/fheq-2024/4.17.b3, qaa/fheq-2024/4.17.b6 and spine:7."
  author-agent-dialogue: "Raise it with a master's student planning a dissertation or critical review, or with a team writing master's outcomes. Put it plainly in the second person for a student and as a minimum for the award for staff. Ask: 'What will your dissertation add that was not known before?' Avoid reading the paragraph aloud or confusing it with the honours threshold."
- statement: qaa/housing-studies-2022/4.6.masters
  forPractitioner: { text: "Master's graduates show understanding of the housing knowledge in the undergraduate threshold, with much of it reaching the forefront of research and of practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a master's in housing you will show you understand the knowledge set for the honours degree, much of it at the leading edge of research and professional practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a condition of a master's award in Housing Studies, read at the threshold: understanding of housing knowledge much of it at the forefront of research and practice, at FHEQ Level 7 (FQHEIS Level 11). Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.6. Do not apply it to the honours degree or call it regulatory. Set it beside qaa/fheq-2024/4.17.b1, qaa/housing-studies-2022/4.3.b1 and spine:7."
  author-agent-dialogue: "Raise it with a master's student planning a dissertation or critical review, or with a team writing master's outcomes. Put it plainly in the second person for a student and as a minimum for the award for staff. Ask: 'Which part of your housing knowledge is closest to current research or new practice?' Avoid reading the paragraph aloud or confusing it with the honours threshold."
- statement: qaa/housing-studies-2022/4.7
  forPractitioner: { text: "Develop master's students' higher-level skills through self-directed academic and professional work, and set master's outcomes against the FHEQ Level 7 (FQHEIS Level 11) qualification descriptor.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "On a master's course you will build higher-level skills largely by directing your own academic and professional development, to the level set for master's qualifications across the UK.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an expectation ('expected to', a word outside the five) that master's students achieve to the FHEQ Level 7 and FQHEIS Level 11 descriptor, which the statement adopts rather than restates. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.7. Do not copy the descriptor into a programme document as if it were the statement's own text. Set it beside qaa/fheq-2024/4.17.b1 to qaa/fheq-2024/4.17.b8.3 (shared by fqheis:11) and spine:7."
  author-agent-dialogue: "Raise it when a master's student asks how master's study differs from undergraduate study. Put it plainly: more of the work is self-directed and the bar is set by the national master's descriptor. Ask: 'Which part of your learning are you now steering yourself?' Avoid reading the descriptor aloud at length."
- statement: qaa/housing-studies-2022/4.8.b1
  forPractitioner: { text: "Graduates will work alone and in teams to pinpoint complex problems and synthesise the current state of knowledge on a subject or topic.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you will be able to work on your own and with others to spot complex problems and pull together what is already known about a topic.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a skill the statement makes a condition of both undergraduate and postgraduate Housing Studies awards ('are able to', recorded as will): independent and joint work on complex problems and synthesis of knowledge. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.8 (item 1). Do not present it as housing knowledge or as regulatory, and read it at the award's level. At honours set it beside qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/3rd and spine:6; for a master's, beside qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise it when a student reflects on skills for a portfolio, placement or job application, or when a team maps skills across modules. Put it in plain words, in the second person for a student, and as a skill the award requires for staff. Ask: 'Can you sum up in a page what is known about a housing problem you care about?' Avoid reading the item aloud at length or implying the master's and honours versions demand the same depth."
- statement: qaa/housing-studies-2022/4.8.b2
  forPractitioner: { text: "Graduates will take personal responsibility for their learning, show conceptual understanding, make sound judgements and communicate ideas effectively to different audiences.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you will be able to take charge of your learning, show you grasp the ideas, make sound judgements and explain your ideas well to different people.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a skill the statement makes a condition of both undergraduate and postgraduate Housing Studies awards ('are able to', recorded as will): ownership of learning, judgement and communicating ideas. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.8 (item 2). Do not present it as housing knowledge or as regulatory, and read it at the award's level. At honours set it beside qaa/fheq-2024/4.15.b5, qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/transferable/r1/3rd and spine:6; for a master's, beside qaa/fheq-2024/4.17.b5, qaa/fheq-2024/4.17.b8.3 and spine:7."
  author-agent-dialogue: "Raise it when a student reflects on skills for a portfolio, placement or job application, or when a team maps skills across modules. Put it in plain words, in the second person for a student, and as a skill the award requires for staff. Ask: 'When did you last change your view after weighing evidence, and how did you explain it?' Avoid reading the item aloud at length or implying the master's and honours versions demand the same depth."
- statement: qaa/housing-studies-2022/4.8.b3
  forPractitioner: { text: "Graduates will collaborate in assessed and non-assessed activities, including with other disciplines, mirroring the inter-professional character of housing practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you will be able to work with others, including people from other professions, in assessed and unassessed tasks, as you will in housing work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a skill the statement makes a condition of both undergraduate and postgraduate Housing Studies awards ('are able to', recorded as will): collaboration across disciplines in assessed and other activities. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.8 (item 3). Do not present it as housing knowledge or as regulatory, and read it at the award's level. At honours set it beside qaa/fheq-2024/annex-d/transferable/r2/3rd, qaa/fheq-2024/4.15.b9.1 and spine:6; for a master's, beside qaa/fheq-2024/4.17.b8.1 and spine:7."
  author-agent-dialogue: "Raise it when a student reflects on skills for a portfolio, placement or job application, or when a team maps skills across modules. Put it in plain words, in the second person for a student, and as a skill the award requires for staff. Ask: 'What did you learn from working with someone trained in another profession?' Avoid reading the item aloud at length or implying the master's and honours versions demand the same depth."
- statement: qaa/housing-studies-2022/4.8.b4
  forPractitioner: { text: "Graduates will show awareness of equality, diversity and inclusion issues and accept professional responsibility for addressing them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you will be able to show that you understand issues of equality, diversity and inclusion and that you take professional responsibility for acting on them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a skill the statement makes a condition of both undergraduate and postgraduate Housing Studies awards ('are able to', recorded as will): awareness of and professional responsibility for equality, diversity and inclusion. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.8 (item 4). Do not present it as housing knowledge or as regulatory, and read it at the award's level. At honours set it beside qaa/fheq-2024/4.15.b9.1, qaa/housing-studies-2022/1.19 and spine:6; for a master's, beside qaa/fheq-2024/4.17.b8.1 and spine:7."
  author-agent-dialogue: "Raise it when a student reflects on skills for a portfolio, placement or job application, or when a team maps skills across modules. Put it in plain words, in the second person for a student, and as a skill the award requires for staff. Ask: 'Where in housing work would you have to act on unfairness, and what would you do?' Avoid reading the item aloud at length or implying the master's and honours versions demand the same depth."
- statement: qaa/housing-studies-2022/4.8.b5
  forPractitioner: { text: "Graduates will use a range of ICT packages to gather and weigh information and data from varied sources.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you will be able to use a range of software to gather and assess information and data from different sources.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a skill the statement makes a condition of both undergraduate and postgraduate Housing Studies awards ('are able to', recorded as will): using ICT to gather and evaluate information and data. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.8 (item 5). Do not present it as housing knowledge or as regulatory, and read it at the award's level. At honours set it beside qaa/fheq-2024/annex-d/transferable/r1/3rd, qaa/fheq-2024/annex-d/practical/r4/3rd and spine:6; for a master's, beside qaa/fheq-2024/4.17.b2 and spine:7."
  author-agent-dialogue: "Raise it when a student reflects on skills for a portfolio, placement or job application, or when a team maps skills across modules. Put it in plain words, in the second person for a student, and as a skill the award requires for staff. Ask: 'Which tools do you use to find and check housing data, and how do you judge a source?' Avoid reading the item aloud at length or implying the master's and honours versions demand the same depth."
- statement: qaa/housing-studies-2022/4.8.b6
  forPractitioner: { text: "Graduates will identify housing problems, environmental and sustainability ones among them, and devise alternative solutions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you will be able to spot housing problems, including environmental and sustainability ones, and come up with different ways to solve them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a skill the statement makes a condition of both undergraduate and postgraduate Housing Studies awards ('are able to', recorded as will): identifying housing problems, sustainability included, and alternative solutions. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.8 (item 6). Do not present it as housing knowledge or as regulatory, and read it at the award's level. At honours set it beside qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r3/3rd and spine:6; for a master's, beside qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise it when a student reflects on skills for a portfolio, placement or job application, or when a team maps skills across modules. Put it in plain words, in the second person for a student, and as a skill the award requires for staff. Ask: 'For one housing problem, what are two different solutions and what does each cost the environment?' Avoid reading the item aloud at length or implying the master's and honours versions demand the same depth."
- statement: qaa/housing-studies-2022/4.8.b7
  forPractitioner: { text: "Graduates will reflect on and direct their own learning, personal development and ethical, professional practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you will be able to reflect on and manage your own learning and personal growth, and how you act ethically and professionally.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a skill the statement makes a condition of both undergraduate and postgraduate Housing Studies awards ('are able to', recorded as will): reflecting on and managing learning, development and ethical practice. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.8 (item 7). Do not present it as housing knowledge or as regulatory, and read it at the award's level. At honours set it beside qaa/fheq-2024/annex-d/transferable/r3/3rd, qaa/fheq-2024/annex-d/transferable/r5/3rd, qaa/fheq-2024/4.15.b9.3 and spine:6; for a master's, beside qaa/fheq-2024/4.17.b8.3 and spine:7."
  author-agent-dialogue: "Raise it when a student reflects on skills for a portfolio, placement or job application, or when a team maps skills across modules. Put it in plain words, in the second person for a student, and as a skill the award requires for staff. Ask: 'What would you change about how you learn, and why?' Avoid reading the item aloud at length or implying the master's and honours versions demand the same depth."
- statement: qaa/housing-studies-2022/4.8.b8
  forPractitioner: { text: "Graduates will consciously reflect on and use their learning to strengthen their employability and entrepreneurship for the career they intend.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you will be able to think about what you have learned and use it to make yourself more employable and enterprising for the career you want.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a skill the statement makes a condition of both undergraduate and postgraduate Housing Studies awards ('are able to', recorded as will): using learning for employability and entrepreneurship. Cite it as QAA, 2022, Housing Studies Subject Benchmark Statement, para 4.8 (item 8). Do not present it as housing knowledge or as regulatory, and read it at the award's level. At honours set it beside qaa/fheq-2024/annex-d/transferable/r4/3rd, qaa/fheq-2024/4.15.b9.3 and spine:6; for a master's, beside qaa/fheq-2024/4.17.b8.1 and spine:7."
  author-agent-dialogue: "Raise it when a student reflects on skills for a portfolio, placement or job application, or when a team maps skills across modules. Put it in plain words, in the second person for a student, and as a skill the award requires for staff. Ask: 'Which thing you learned this year would most help you get the housing job you want?' Avoid reading the item aloud at length or implying the master's and honours versions demand the same depth."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.7; 4.2" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.7; 4.2" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.9; 4.7" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.9; 4.7" }
  - { id: "spine:6", role: "inferred", locator: "std:ref:uk-framework R2 (honours)" }
  - { id: "spine:7", role: "inferred", locator: "std:ref:uk-framework R2 (master's)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.7: degree with honours, FHEQ Level 6, FQHEIS Level 10; 4.2)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.9; 4.7: one descriptor, FHEQ Level 7 and SCQF Level 11)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.11", "1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "1.19"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.11", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "1.28", "1.29", "1.30"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.11", "1.31", "1.32", "1.33", "1.34", "1.35"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["2.5", "2.6"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-housing-studies-2019-benchmarks (not ingested)", note: "the third edition (2019), named in section 6; the front matter lists key changes from the previous Statement" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 (4.2); the FHEQ Level 7 descriptor (4.7)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS Levels 10 and 11 (2.7, 2.9, 4.7)" }
- { rel: "cites", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "quoted for the UNESCO definition of ESD (1.20); source of Figure 4 (3.17)" }
- { rel: "cites", target: "std:doc:qaa-enterprise-2018-guidance", note: "source of Figure 3 (1.33)" }
- { rel: "refersTo", target: "CIH specification for chartered membership and CIH Professional Standards (not yet ingested)", note: "1.4, 2.2, 2.19, 4.3: Part E" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance; QAA Glossary; QAA guide to comparing qualifications in the UK and Ireland (not ingested)", note: "front matter; 2.10" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2022-03"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "advisory group with members from all four nations, including the CIH (D1, front matter; section 6)"
replacedBy: "none"
editions: "first 2007 (original), second 2014, third 2019 (aligned with the 2018 Quality Code), fourth March 2022 (D1, section 6)"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- A field of study, interdisciplinary since the early 1980s, that starts from a household's basic need for a home in which to live well and flourish (D1, 1.1, 1.2, 2.1).
- It links home, dwellings and neighbourhoods with the institutions and actors that provide housing, across market and social sectors, judged by adequacy, affordability and security (D1, 1.2).
- It draws on the social sciences, law, health, geography, planning, surveying, construction, architecture and management; it applies theory to practical situations (D1, 1.3, 2.4, 3.1).
- It is vocational and functional: knowledge that can be applied, with a three-fold design joining behaviours and values, skills and knowledge, shaped by the CIH's professional standards (D1, 1.4, 2.1, 2.2).
- It sees itself as a subject of social justice, attentive to rights, homelessness and the lived experience of housing, including students' own (D1, 1.2, 1.13, 2.6).
- Its courses reflect devolved housing law, policy and governance across the four UK nations (D1, 1.10).
- Students arrive by many routes, often already working in housing; recognition of prior learning, part-time study and employer partnerships are characteristic (D1, 1.4, 2.6, 2.11, 2.13, 2.15).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "framed as social justice: housing rights, disadvantage, intersectional inequality, class and tenure stigma and the most vulnerable groups as content; an inclusive curriculum that recognises students may have known housing precarity; inclusive behaviours for graduates (D1, 1.12 to 1.19); also in content and the generic skills (D1, 3.1, 4.8)"
  statements: ["qaa/housing-studies-2022/1.13", "qaa/housing-studies-2022/1.15", "qaa/housing-studies-2022/4.3.b7", "qaa/housing-studies-2022/4.3.b18", "qaa/housing-studies-2022/4.8.b4", "qaa/housing-studies-2022/3.12"]
- theme: theme:esd
  inThisSubject: "built on the UN SDGs, with SDG 11 and target 11.1 on adequate, safe and affordable housing at the centre; UNESCO's eight competencies adapted for housing; the campus and community as a living laboratory (D1, 1.20 to 1.30); repeated in delivery and in the threshold and generic skills (D1, 3.14, 4.3, 4.8)"
  statements: ["qaa/housing-studies-2022/1.22", "qaa/housing-studies-2022/1.23", "qaa/housing-studies-2022/1.25", "qaa/housing-studies-2022/1.26.b1", "qaa/housing-studies-2022/1.26.b2", "qaa/housing-studies-2022/1.26.b3", "qaa/housing-studies-2022/1.26.b4", "qaa/housing-studies-2022/1.26.b5", "qaa/housing-studies-2022/1.27", "qaa/housing-studies-2022/1.28", "qaa/housing-studies-2022/1.29", "qaa/housing-studies-2022/1.30", "qaa/housing-studies-2022/3.14.b3", "qaa/housing-studies-2022/3.14.b5", "qaa/housing-studies-2022/4.3.b16", "qaa/housing-studies-2022/4.8.b6"]
- theme: theme:enterprise
  inThisSubject: "headed employability and enterprise education: a vocational subject whose entrepreneurship includes social entrepreneurship, careers across public, private and third sectors, placements and the reflective, resilient practitioner (D1, 1.31 to 1.35); work experience through employer partnerships (D1, 2.15)"
  statements: ["qaa/housing-studies-2022/1.34", "qaa/housing-studies-2022/1.35", "qaa/housing-studies-2022/2.15", "qaa/housing-studies-2022/4.8.b8"]
- theme: theme:accessibility
  inThisSubject: "accessible environments, materials and site visits for students with learning or mobility needs and for those disadvantaged by structural inequality; content designed so lived experience of housing problems is not a barrier (D1, 2.5, 2.6); adjustments in teaching and assessment (D1, 3.7, 3.20)"
  statements: ["qaa/housing-studies-2022/2.5", "qaa/housing-studies-2022/2.6", "qaa/housing-studies-2022/1.26.b2", "qaa/housing-studies-2022/3.14.b2", "qaa/housing-studies-2022/3.16", "qaa/housing-studies-2022/3.20"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.1", gloss: "26 core topics: meanings of home and homelessness; EDI and decolonisation; sustainable development and the climate crisis; people and place; history, policy, law, governance and regulation; leadership and management; politics; economics and finance; inequality and tenure stigma; strategic planning; devolution; place and regeneration; place and property management; housing practice and services; homelessness; housing and health; sustainable construction and retrofit; contemporary and digital practice; ethics and professionalism; research methods" }
  - { component: "1.16", gloss: "themes of inclusive housing knowledge: rights, disadvantage, need, differential access, social harm, intersectional inequality, class and tenure stigma, vulnerable migrants and refugees" }
  - { component: "1.24", gloss: "the eight UNESCO key competencies for sustainability adapted to housing (Figure 2)" }
practices:
  - { component: "3.7", kind: "teaching", gloss: "lectures, small groups, supervision, directed study, site and virtual visits, problem-based and team learning, negotiated and work-related learning" }
  - { component: "3.11", kind: "teaching", gloss: "alternative viewpoints, reflection and real challenges in a living laboratory" }
  - { component: "3.13", kind: "learning", gloss: "blended and online group learning on real problems" }
  - { component: "3.14", kind: "learning", gloss: "an interdisciplinary, inclusive learning environment with ESD and synoptic assessment" }
  - { component: "1.18", kind: "learning", gloss: "inclusive learning experiences around housing disadvantage and respect for views" }
  - { component: "2.15", kind: "learning", gloss: "work experience through employer partnerships" }
  - { component: "3.3", kind: "learning", gloss: "work-based and work-related learning on accredited courses" }
  - { component: "3.15", kind: "assessment", gloss: "an aligned assessment and feedback strategy with clear criteria" }
  - { component: "3.18", kind: "assessment", gloss: "self, peer and synoptic assessment; authentic tasks; ESD assessed in and beyond the curriculum" }
  - { component: "3.19", kind: "assessment", gloss: "essays, reports, policy briefs, exams, presentations, projects, journals, dissertations, digital and work-based assessment" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.3", award: "bachelor's with honours", items: 19 }
  - { rung: "threshold", leadIn: "4.6", award: "master's", items: 5 }
  - { rung: "typical", leadIn: "4.4", award: "bachelor's with honours", items: 1 }
  - { rung: "excellent", leadIn: "4.5", award: "bachelor's with honours", items: 1 }
rungBases: "4.1: the threshold is the minimum for an honours award; 4.2: most students perform well above it, judged by each provider with reference to Annex D; 4.4 and 4.5: typical (2:1, 2:2) and excellent (1st) follow providers' marking schemes, with no subject items listed. The master's list (4.6) is another award, recorded at its threshold."
outcomeLists:
  - { leadIn: "4.8", gloss: "transferable and generic skills for undergraduate and postgraduate awards", items: 8, award: ["honours", "master's"] }
outcomes: []
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
- { body: "Chartered Institute of Housing (CIH)", says: "a leading UK and international professional body that accredits many courses and influences their outcomes; the statement draws on its accreditation but stays distinct from its specification; its Professional Standards Framework shapes course values; chartered membership needs prescribed work experience and a CIH-accredited Postgraduate Diploma usually meets its criteria; it offers its own progression routes and validates courses (D1, front matter, 1.4, 1.7, 1.10, 2.2, 2.9, 2.10, 2.11, 2.15, 2.19, 4.3)", requirements: "not yet ingested (Part E)" }
- { body: "Housing Studies Association; Collaborative Centre for Housing Evidence", says: "external networks that support an early career research community (D1, 2.12)", requirements: "not-applicable-by-design" }
- { body: "Office for Students", says: "its regulatory framework does not treat Subject Benchmark Statements as sector-recognised standards in England (D1, front matter)", requirements: "not-applicable-by-design" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["front matter", "1.11", "1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "1.19", "1.21", "1.23", "1.26", "1.29", "1.33", "1.35", "2.2", "2.6", "3.1", "3.2", "3.4", "3.12", "3.13", "3.14", "3.16", "4.8"], statements: ["qaa/housing-studies-2022/1.13", "qaa/housing-studies-2022/1.15", "qaa/housing-studies-2022/1.26.b2", "qaa/housing-studies-2022/2.6", "qaa/housing-studies-2022/3.12", "qaa/housing-studies-2022/3.14.b2", "qaa/housing-studies-2022/3.16", "qaa/housing-studies-2022/4.3.b7", "qaa/housing-studies-2022/4.3.b18", "qaa/housing-studies-2022/4.8.b4"] }
  - { id: "theme:esd", named: "Sustainability (front matter and 1.11: education for sustainable development; education for sustainability)", carriedIn: ["front matter", "1.11", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "1.28", "1.29", "1.30", "1.33", "1.35", "3.1", "3.4", "3.10", "3.12", "3.13", "3.14", "3.17", "3.18", "4.3", "4.8"], statements: ["qaa/housing-studies-2022/1.22", "qaa/housing-studies-2022/1.23", "qaa/housing-studies-2022/1.25", "qaa/housing-studies-2022/1.26.b1", "qaa/housing-studies-2022/1.26.b2", "qaa/housing-studies-2022/1.26.b3", "qaa/housing-studies-2022/1.26.b4", "qaa/housing-studies-2022/1.26.b5", "qaa/housing-studies-2022/1.27", "qaa/housing-studies-2022/1.28", "qaa/housing-studies-2022/1.29", "qaa/housing-studies-2022/1.30", "qaa/housing-studies-2022/3.12", "qaa/housing-studies-2022/3.14.b3", "qaa/housing-studies-2022/3.14.b5", "qaa/housing-studies-2022/4.3.b16", "qaa/housing-studies-2022/4.8.b6"] }
  - { id: "theme:enterprise", named: "Employability and enterprise education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["front matter", "1.11", "1.21", "1.31", "1.32", "1.33", "2.13", "2.15", "3.7", "4.8"], statements: ["qaa/housing-studies-2022/1.34", "qaa/housing-studies-2022/1.35", "qaa/housing-studies-2022/2.15", "qaa/housing-studies-2022/4.8.b8"] }
  - { id: "theme:accessibility", named: "Accessibility", carriedIn: ["1.26", "2.5", "2.6", "3.7", "3.8", "3.14", "3.16", "3.20"], statements: ["qaa/housing-studies-2022/1.26.b2", "qaa/housing-studies-2022/2.5", "qaa/housing-studies-2022/3.8", "qaa/housing-studies-2022/3.14.b2", "qaa/housing-studies-2022/3.16", "qaa/housing-studies-2022/3.20"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.7", "2.9", "4.2", "4.7", "back matter"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.7", "2.9", "2.10", "4.2", "4.7"] }
  - { framework: "other: national qualification and credit frameworks, unnamed", levels: [], citedIn: ["1.9"] }
bodies:
  - { body: "Chartered Institute of Housing", citedIn: ["front matter", "1.4", "1.7", "1.10", "2.2", "2.9", "2.10", "2.11", "2.15", "2.19", "4.3", "back matter"] }
  - { body: "Housing Studies Association", citedIn: ["2.12"] }
  - { body: "Collaborative Centre for Housing Evidence", citedIn: ["2.12"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "the four honours classifications, the reference for performance above the threshold" }
  - { document: "std:doc:qaa-fheq-2024-framework", named: "the descriptor for a higher education qualification at Level 7 on the FHEQ; QAA (2014) The Frameworks for Higher Education Qualifications", citedIn: ["4.7", "back matter"], role: "sets the master's level" }
  - { document: "std:doc:qaa-fqheis-2024-framework", named: "SCQF Level 11 on the FQHEIS", citedIn: ["4.7"], role: "the Scottish name for the master's level" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Education for Sustainable Development Guidance (Advance HE and QAA, 2021)", citedIn: ["1.20", "3.17", "back matter"], role: "the UNESCO definition of ESD; assessment of, for and as learning (Figure 4)" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and entrepreneurship education (QAA 2018)", citedIn: ["1.33", "back matter"], role: "Figure 3, the relationship of entrepreneurship, enterprise and employability" }
  - { document: "not yet ingested: listed in Part E", named: "QAA guide to comparing qualifications in the UK and Ireland", citedIn: ["2.10"], role: "comparing qualification frameworks" }
  - { document: "not yet ingested: listed in Part E", named: "Advice and Guidance to support the Quality Code; QAA's Glossary; The UK Quality Code for Higher Education (2018)", citedIn: ["front matter", "back matter"], role: "course design and review; unfamiliar terms" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "education-for-sustainable-development", definition: "the process of building curriculum structures and subject content that support and enact sustainable development (D1, 1.20)", beneficiaryDefinition: "learning designed so that you can understand and act for sustainable development", scopeNote: "ESD in the text; theme:esd", category: "unknown", practices: ["education"] }
- { slug: "sustainable-development", definition: "an aspirational, continuing process of addressing social, environmental and economic concerns for a better world (D1, 1.20)", beneficiaryDefinition: "working on social, environmental and economic problems together to make the world better", scopeNote: "as the statement defines it", category: "unknown", practices: ["education"] }
- { slug: "living-laboratory", definition: "the campus, community and housing sector used as a setting for authentic learning (D1, 1.27, 3.11)", beneficiaryDefinition: "using real places around you as somewhere to study housing", scopeNote: "", category: "unknown", practices: ["education"] }
- { slug: "recognition-of-prior-learning", definition: "mechanisms that credit learning gained before entry, from study or work (D1, 2.11)", beneficiaryDefinition: "having what you already learned at work or elsewhere counted towards your course", scopeNote: "RPL in the text", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "education-for-sustainable-development", form: "Education for Sustainable Development (ESD)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "sustainable-development", form: "Sustainable Development", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "living-laboratory", form: "'living laboratory'", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "recognition-of-prior-learning", form: "recognition of prior learning (RPL)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement: Housing Studies"
  edition: "March 2022 (fourth edition)"
  year: 2022
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/housing-studies-2022/housing-studies-2022.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 4372c1fea94af0b1be2110de601f9558386540ee453017d538af6be26935ead0
  heldFiles: ["wkspc2601-library/txt/qaa-2022-housing-studies-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2022-housing-studies-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2022-housing-studies-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2022-housing-studies-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0069", source: "Chartered Institute of Housing: specification for chartered membership (course validation) and Professional Standards", why: "the body's requirements linked from 2.19, 4.3 and SB5" }
- { w: "W-std-0070", source: "QAA guide to comparing qualifications in the UK and Ireland", why: "named in 2.10" }
- { w: "W-std-0043", source: "UNESCO (2017) Education for Sustainable Development Goals: Learning Objectives; United Nations (2015) Transforming Our World", why: "the competencies and goals 1.20 to 1.25 build on" }
```

## Part E Gaps and questions
- Run 0112 pattern: one rung list only. The threshold (4.3, 19 items) is listed; typical (4.4) and excellent (4.5) are one-sentence paragraphs that hand their criteria to providers' marking schemes. Each is recorded as one rung statement (rung typical, excellent) with no items beneath it; SB4 outcomes is empty and no gradeOf link is made. Unlike Psychology (three parallel lists).
- Threshold lead-in (4.3) has no modal: "are awarded to students who meet the following threshold standard, demonstrating systematic understanding of"; force recorded as threshold, the issuer defining it as the minimum for the award (4.1).
- 4.3.b19 ("for accredited courses, ensure requirements of CIH specification are fully met") is a provider condition inside the threshold list; recorded as a threshold record with domain none and addressee provider. For P3.
- Master's level: 4.6 is another award, recorded per the batch-1 convention as rung threshold, award master's, level fheq:7, with the id suffix .masters (the stem sentence as 4.6.masters, the four items as 4.6.b1.masters to 4.6.b4.masters, cut by find). Its lead-in also has no modal; force threshold.
- 4.7 says master's students are "expected to achieve" to the FHEQ Level 7 and FQHEIS Level 11 descriptor: "expected to" is outside the five; force describes. For Abbott.
- 4.8's lead-in covers "Undergraduate and postgraduate degrees": the eight skills are recorded once with award [bachelor's with honours, master's] and level fheq:6; at a master's they read at fheq:7. For P3 whether to split by award.
- Obliging words outside the five, recorded as describes: "the expectation is" (1.23), "anticipated" and "expected to" (3.4), "it is expected" (3.7), "anticipated" (3.20), "expected to" (4.7). Also met inside statements recorded at a modal they carry: "expectation is" (1.25, 1.27), "is expected to" (3.3, 3.8, 3.16), "anticipated" (2.15). For Abbott.
- "requires" read as must (convention: required is must): ESD "requires a learning environment in which" (1.26, five items) and housing studies education "requires a learning environment in which" (3.14, six items); CIH chartered membership "requires prescribed work experience" (2.15); "need to be delivered" and "required engagement" (2.19). The two environment lists overlap (four items near-identical); both recorded. For P3.
- "will need to" (1.10) recorded at its modal will; the need is plain. For Abbott.
- Plain-present provider norms, not statements (template open point 5): 1.4 (courses support students), 1.12 (courses acknowledge and promote the Equality Act 2010), 2.9 (objectives achieved at Level 7/11), 2.13, 2.14, 3.18 (assessment tasks ensure students are able to demonstrate at least the threshold).
- Not cut as statements: 1.16 (themes of inclusive knowledge, no modal); 1.17 (questions); 1.18 ("would include"); 1.19 (inclusive behaviours that "can be identified as", nine items: a list of graduate behaviours with no outcome lead-in; strong candidate for P3); 1.24 Figure 2 (26 competency items under "A Housing Studies student who displays this competency can", adapted from UNESCO and flattened from a table with its column headings run into the items; read as a description of the competencies, with 1.25 carrying the expectation; for P3); 2.8 ("would be expected"); 2.18 ("typically ... will be asked", a description of external examining); 3.2 (desired outcomes, no modal); 3.9 ("desirable"); 3.10 ("may"); 4.1 (introduces the threshold, used as rungBases).
- Skeleton corrections: 3.1 tagged as a typical rung lead-in because of "a typical Housing Studies course"; it is the content list (SB3 area), not a rung. Skeleton rung counts (threshold 23, typical 26) set aside. Candidate statements 1.16.b*, 1.17.b*, 1.18.b*, 1.19.b*, 1.24.b*, 3.1.b*, 3.7.b*, 3.19.b* not taken (see above); 3.7 recorded once as a paragraph statement because its list is examples.
- Headings run into the preceding paragraph in the held text (for example "Equality, diversity and inclusion" at the end of 1.11, "Sustainability" in the last item of 1.19, "Employability and enterprise education" at the end of 1.30); SB6 citedIn excludes paragraphs that carry a theme only through such a trailing heading.
- Codes: HECoS 100196 housing (basis stated: the statement names the subject, matching the HECoS term); CAH13-01-04 planning (urban, rural and regional) is the CAH3 parent of 100196 in the HESA store, basis inferred; the statement names no code. For P3.
- Levels inferred from the reference framework: spine:6 and spine:7 (std:ref:uk-framework R2), used in S5 and the agent instructions.
- 2.10 cites "SCQF 5-8 equivalent" for CIH courses at Levels 2 to 5 and CIH entry at "Levels 4, 5 or 6" after Levels 3, 4 and 5 (framework unnamed, likely the RQF or CQFW); SCQF 5 and 6 fall outside the fqheis ids (fqheis:7 to 12), so no level ids are recorded for them. For P3.
- 2.9 names "Postgraduate Certificate of Education" as a postgraduate exit award; likely a slip for Postgraduate Certificate (recall); not corrected.
- Foundation degrees (fheq:5) are informed by the statement (1.6, 1.9) but not covered; levelsCovered holds only the two awards it sets standards for.
- Bodies: the CIH's specification and Professional Standards are not yet ingested (SB5, D3). Advance HE is co-issuer of the ESD guidance, not a body here.
- Shared documents not yet ingested: QAA guide to comparing qualifications (2.10); Quality Code and its Advice and Guidance, QAA Glossary (front matter). The 2014 Frameworks cited in section 5 are read as the 2024 edition (std:doc:qaa-fheq-2024-framework); for P3.
- Supersedes: the third edition (2019) is named in section 6 but not ingested; S7 target is a placeholder id.
- Generative AI: not named in this statement (no theme:generative-ai).
- S9 not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:45: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0112 (P1); built by tools/bm_build.py.
