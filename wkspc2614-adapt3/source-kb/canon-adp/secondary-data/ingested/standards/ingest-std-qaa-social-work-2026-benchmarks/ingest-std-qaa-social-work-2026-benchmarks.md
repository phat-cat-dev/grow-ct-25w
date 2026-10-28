---
id: std:doc:qaa-social-work-2026-benchmarks
title: "Subject Benchmark Statement Social Work"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100503", label: "social work", basis: "stated" }
  - { scheme: "cah", code: "CAH15-04-01", label: "social work", basis: "stated" }
edition: "April 2026 (fifth edition)"
published: 2026-04
status: current
supersedes: "Subject Benchmark Statement: Social Work, fourth edition (2019; minor update of the 2016 statement)"
heldText: { method: sha256-bytes, raw: 3e0c995b05b7185fed01b86ff5553bfbe4ad905905db55f24ef359790d2182b5, normalised: db8866bcbeb3c22d55c8e2166ae61adcf22fc8c52e2c92359cd43f49bbe0e208 }
heldTextStan: { method: sha256-stan, raw: 3e0c995b05b7185fed01b86ff5553bfbe4ad905905db55f24ef359790d2182b5, normalised: 0821abda154a9863568cf21db7dc2a8a37d17d81b50fc2d1ec75b720b166c272 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2026 revision with five cross-cutting themes (EEDI; accessibility; ESD; EEE; generative AI)"
awardsCovered: ["bachelor's with honours", "integrated master's", "master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it sends readers to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0130 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:42"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Social Work (QAA, April 2026)

> Run 0130, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2026-social-work-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a social work student must have shown by the end of an honours degree, an integrated master's or a taught master's: one rung only, the minimum threshold, set out for honours as four categories (knowledge and understanding, demonstrable skills, values and ethics, the regulator's requirements) with 34 lettered outcomes, and for the two master's awards as stronger headline statements that point back to those outcomes. Reach for it when designing, approving, reviewing or describing a social work course. It sits under the four UK regulators, whose approval and registration rules are separate, and it is not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA on 16 April 2026 as the fifth edition, the statement sets social work in the IFSW global definition, describes the subject's purposes and distinctive features, the regulators of the four nations and their approval and registration rules, content, teaching, learning and assessment, and minimum threshold standards for bachelor's degrees with honours (FHEQ 6, SCQF 10), integrated master's and postgraduate taught master's degrees (FHEQ 7, SCQF 11). It states no typical or excellent lists: it maps threshold to a third, typical to a 2.2 or 2.1 and excellent to a first and refers to Annex D of the Frameworks for the classes. It treats five cross-cutting themes: equity, equality, diversity and inclusion; accessibility and the needs of disabled students; education for sustainable development; employability, entrepreneurship and enterprise education; and generative artificial intelligence. Bodies named: Social Care Wales, Social Work England, the Northern Ireland Social Care Council, the Scottish Social Services Council, the Professional Standards Authority and the IFSW.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Social Work"
edition: "April 2026 (fifth edition)"
dates:
  published: 2026-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector-owned reference point (D1, front matter); in England not a sector-recognised standard under the Office for Students' framework; part of the quality arrangements in Scotland, Wales and Northern Ireland (D1, front matter: Relationship to legislation). Approval and registration rest with the four regulators (D1, 1.4, 2.9 to 2.22)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2026", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a Social Work graduate can be expected to know, do and understand at the end of their studies, and the nature of awards in the subject, as minimum threshold standards for honours, integrated master's and postgraduate taught master's degrees (D1, front matter: About this Statement; 4.3)"
appliesTo:
  awards: ["bachelor's degrees with honours", "integrated master's degrees", "postgraduate taught master's degrees", "postgraduate certificates and diplomas (the master's standards can also apply, 4.15)", "degree apprenticeships (named, 2.24)"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This Subject Benchmark Statement sets out the minimum threshold standards that a Social Work student will have demonstrated when they are awarded: a bachelor's degree with honours, an integrated master's degree, a postgraduate taught master's degree.\" (D1, 4.3)"
statedSubjects:
  - { name: "Social Work", locator: "(D1, title; 1.1; 4.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100503", label: "social work" }, { scheme: "cah", code: "CAH15-04-01", label: "social work" }] }
  - { name: "Bachelor of Science (BSc) or Arts (BA) degree ... postgraduate conversion course ... postgraduate diploma (PgDip) ... Master of Science (MSc or MSci) or Arts (MA) ... degree apprenticeship", locator: "(D1, 2.24)", kind: "programme title", codes: [{ scheme: "hecos", code: "100503", label: "social work" }] }
  - { name: "honours-level degree in Social Work (the professional qualification for social workers, probation officers and education welfare officers in Northern Ireland)", locator: "(D1, 2.18)", kind: "programme title", codes: [{ scheme: "hecos", code: "100503", label: "social work" }] }
  - { name: "generic honours degree in Social Work, or an equivalent postgraduate award (Scotland)", locator: "(D1, 2.21)", kind: "programme title", codes: [{ scheme: "hecos", code: "100503", label: "social work" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Work degree", gloss: "the IFSW global definition of the profession as the frame for UK social work" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Work degree", gloss: "the statement as a route map for education grounded in social justice, inclusion and ethical, reflective practice" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Work degree", gloss: "professional qualification tied to an academic level; honours as the minimum route into the profession" }
  - { number: "1.4", order: 6, componentType: stem, parent: "section 1", heading: "Context and purposes of a Social Work degree", gloss: "statutory registration since 2000; the protected title and the four national regulators (listed)" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Work degree", gloss: "regulators approve courses and regulate practitioners to protect the public" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Work degree", gloss: "regulators' standards shape curriculum and assessment" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Work degree", gloss: "an academic discipline applied through practice; integrated knowledge, skills, values and research" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Work degree", gloss: "complex, uncertain settings; what social workers must be equipped for and expected to do (S4)" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Work degree", gloss: "interagency and multi-agency working and knowledge of other roles" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Work degree", gloss: "practice as core learning, in placements and other experiential settings" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Work degree", gloss: "regulators' stipulations inform design, content and practice learning" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "the scope of EEDI and intersectionality; EEDI central to the subject" }
  - { number: "1.13", order: 15, componentType: stem, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "inclusive learning communities and reference points for equality (listed)" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "the duty to make reasonable adjustments, linked to IFSW principles (S4)" }
  - { number: "1.15", order: 17, componentType: stem, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "self-identity and intersectionality; widening access; awarding gaps; cross-cutting topics for curricula (listed)" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "a diverse workforce and staff; reflecting on one's own privileges and barriers" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "the legal duty on courses and placements to adjust (S4); QAA guidance on inclusive communities" }
  - { number: "1.18", order: 20, componentType: stem, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "examples of how courses address EEDI (listed)" }
  - { number: "1.19", order: 21, componentType: stem, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "anti-oppressive and anti-racist values built into design, content, teaching and assessment (listed)" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "dismantling oppression and racism, with a commitment against anti-Black racism" }
  - { number: "1.21", order: 23, componentType: stem, parent: "section 1", heading: "Equity, equality, diversity and inclusion", gloss: "examples of anti-racist and decolonising course practice (listed)" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "equality and Welsh-language law across the four nations; a proactive approach to access" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessible environments as legal duty and professional value" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessible design and the expectation of anticipatory adjustments (S4)" }
  - { number: "1.25", order: 27, componentType: stem, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "how courses secure equitable access while keeping standards (listed)" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "social work's part in sustainable development and climate impacts; three generations of rights" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "graduates as global citizens aware of climate and environmental effects" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "a value-based profession; reflecting on social and environmental impacts" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ESD and the UN SDGs as shared social work goals" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "UNESCO key competencies for the SDGs, embedded in course design and assessment" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ESD content and action-oriented, transformative pedagogy" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "IFSW support for the SDGs; ESD as a lens, citing the QAA and Advance HE ESD guidance" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "inclusion and leaving no-one behind; applying skills to sustainability problems" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "employability, enterprise and entrepreneurship education and its benefits" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "practice-based learning and links with outside organisations" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "entrepreneurship education for a self-directed professional life" }
  - { number: "1.37", order: 39, componentType: stem, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "the entrepreneurial mindset in social work (listed)" }
  - { number: "1.38", order: 40, componentType: stem, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "what course experiences offer for careers and enterprise (listed)" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "enterprise behaviours" }
  - { number: "1.40", order: 42, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "enterprise attributes" }
  - { number: "1.41", order: 43, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "skills for professional practice" }
  - { number: "1.42", order: 44, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "digital competence and transferable skills" }
  - { number: "1.43", order: 45, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "benefits of enterprise learning for confidence and career pathways" }
  - { number: "1.44", order: 46, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "enterprise skills employers prize; the aim of competent, confident entrants" }
  - { number: "1.45", order: 47, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "AI and generative AI in society and practice; procedures for authenticity (S4)" }
  - { number: "1.46", order: 48, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "engaging with technologies in many spaces; the need to navigate them (S4)" }
  - { number: "1.47", order: 49, componentType: stem, parent: "section 1", heading: "Generative artificial intelligence", gloss: "what engagement with generative AI includes (listed)" }
  - { number: "1.48", order: 50, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "values guide technology use; technology does not replace human relationships (S4)" }
  - { number: "2.1", order: 52, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "distinctive focus on practice in complex situations; partnership with employers, people with lived experience and students" }
  - { number: "2.2", order: 53, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "integrated study of knowledge, skills, values and research; analytic and practical understanding" }
  - { number: "2.3", order: 54, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "preparing for work with many people and groups; including care-experienced students" }
  - { number: "2.4", order: 55, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "values and ethics, difficult decisions and the study of dilemmas as a core requirement (S4)" }
  - { number: "2.5", order: 56, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "the subject's heritage and its contested scope" }
  - { number: "2.6", order: 57, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "different and changing welfare contexts in the UK and internationally" }
  - { number: "2.7", order: 58, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "competing views of social work: justice, care and order" }
  - { number: "2.8", order: 59, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "a changing profession; qualified workers need to understand and lead change (S4)" }
  - { number: "2.9", order: 60, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies", gloss: "regulators' standards shape design and assessment" }
  - { number: "2.10", order: 61, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies: Cymru/Wales", gloss: "the Welsh regulator, its history and the protected title" }
  - { number: "2.11", order: 62, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies: Cymru/Wales", gloss: "approval by Social Care Wales; the Welsh qualification framework and context (S4)" }
  - { number: "2.12", order: 63, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies: Cymru/Wales", gloss: "student registration with Social Care Wales and its Code (S4)" }
  - { number: "2.13", order: 64, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies: England", gloss: "the regulator for England and the protected title" }
  - { number: "2.14", order: 65, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies: England", gloss: "approval by Social Work England against its standards (S4); oversight by the Professional Standards Authority" }
  - { number: "2.15", order: 66, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies: England", gloss: "registration after an approved course; post-qualifying statements and the supported first year" }
  - { number: "2.16", order: 67, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies: Northern Ireland", gloss: "the Northern Ireland regulator and the protected title" }
  - { number: "2.17", order: 68, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies: Northern Ireland", gloss: "the Northern Ireland framework specification; learning on political violence and integrated care (S4)" }
  - { number: "2.18", order: 69, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies: Northern Ireland", gloss: "honours as the professional qualification in Northern Ireland; student registration; the assessed year (S4)" }
  - { number: "2.19", order: 70, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies: Northern Ireland", gloss: "standards of conduct and practice for registrants and students" }
  - { number: "2.20", order: 71, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies: Scotland", gloss: "the Scottish regulator and the protected title" }
  - { number: "2.21", order: 72, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies: Scotland", gloss: "SSSC approval, codes and registers; the honours or postgraduate award needed to qualify (S4)" }
  - { number: "2.22", order: 73, componentType: paragraph, parent: "section 2", heading: "Regulatory bodies: Scotland", gloss: "registration with the SSSC after an approved programme" }
  - { number: "2.23", order: 74, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through levels to the threshold skills (FHEQ 6 and 7; SCQF 10 and 11) (S4)" }
  - { number: "2.24", order: 75, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "routes and awards, including apprenticeships; integrated practice learning in all (S4)" }
  - { number: "2.25", order: 76, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "design flexibility within the broad base of the discipline" }
  - { number: "2.26", order: 77, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "seminal and contemporary theory and culturally diverse viewpoints" }
  - { number: "2.27", order: 78, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "ethics central to design; students apply ethics to themselves and judge others (S4)" }
  - { number: "2.28", order: 79, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "duration and level of honours in England, Wales and Northern Ireland" }
  - { number: "2.29", order: 80, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "Scottish ordinary and honours degrees and the Scottish MA" }
  - { number: "2.30", order: 81, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "integrated master's: length and the two levels it meets" }
  - { number: "2.31", order: 82, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "part-time credit equivalence" }
  - { number: "2.32", order: 83, componentType: stem, parent: "section 2", heading: "Flexibility", gloss: "flexible delivery modes (listed)" }
  - { number: "2.33", order: 84, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "delivery with partners; the statement's role for partners" }
  - { number: "2.34", order: 85, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership with people with lived or living experience (S4)" }
  - { number: "2.35", order: 86, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership with practice learning providers; written agreements; stakeholder views in design (S4)" }
  - { number: "2.36", order: 87, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "courses aligned with the relevant regulator's standards (S4)" }
  - { number: "2.37", order: 88, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership benefits and the student voice" }
  - { number: "2.38", order: 89, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "routine monitoring and periodic review by awarding bodies" }
  - { number: "2.39", order: 90, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "externality and external reviewers (S4)" }
  - { number: "2.40", order: 91, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examining and its use of the statement" }
  - { number: "2.41", order: 92, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "stakeholders in monitoring and review" }
  - { number: "2.42", order: 93, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "approval and ongoing monitoring by regulators (S4)" }
  - { number: "3.1", order: 95, componentType: area, parent: "section 3", heading: "Content", gloss: "frameworks in design; principles for content; co-production and decolonised content (S4)" }
  - { number: "3.2", order: 96, componentType: area, parent: "section 3", heading: "Content", gloss: "knowledge, skills, values and behaviours for reflective practitioners" }
  - { number: "3.3", order: 97, componentType: area, parent: "section 3", heading: "Content", gloss: "typical content: research, theory, methods, values, policy, law and leadership" }
  - { number: "3.4", order: 98, componentType: practice, parent: "section 3", heading: "Content", gloss: "practice-based learning and the integration of knowledge into practice (S4)" }
  - { number: "3.5", order: 99, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "sequencing for incremental learning by level" }
  - { number: "3.6", order: 100, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "scaffolded teaching, growing responsibility and a range of facilitators (S4)" }
  - { number: "3.7", order: 101, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "five learning themes and the methods that carry them" }
  - { number: "3.8", order: 102, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "principles and purposes of assessment; readiness and fitness for practice (S4)" }
  - { number: "3.9", order: 103, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "a diverse range of assessment methods and assessors" }
  - { number: "4.1", order: 105, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "a professional qualification at undergraduate or postgraduate level; academic and practice requirements (S4)" }
  - { number: "4.2", order: 106, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "threshold standards are not competence standards; equality guidance for providers (S4)" }
  - { number: "4.3", order: 107, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "lead-in: the three awards for which minimum threshold standards are set (scope, not an outcome list)" }
  - { number: "4.4", order: 108, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "standards shown over time show the expected range of attainment" }
  - { number: "4.5", order: 109, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "practice requirements common to all routes; academic levels 6 and 7; regulators' outcomes also apply (S4)" }
  - { number: "4.6", order: 110, componentType: paragraph, parent: "section 4", heading: "Classification", gloss: "most students exceed the threshold; providers decide the evidence" }
  - { number: "4.7", order: 111, componentType: paragraph, parent: "section 4", heading: "Classification", gloss: "Annex D for honours classes; threshold, typical and excellent mapped to degree classes" }
  - { number: "4.8", order: 112, componentType: paragraph, parent: "section 4", heading: "Classification", gloss: "classes for integrated master's and merit and distinction for master's; marking schemes (S4)" }
  - { number: "4.9", order: 113, componentType: paragraph, parent: "section 4", heading: "Bachelor's degree with honours: Minimum standards", gloss: "honours graduates must reach at least threshold across four categories (S4)" }
  - { number: "4.10", order: 114, componentType: paragraph, parent: "section 4", heading: "Bachelor's degree with honours: Minimum standards", gloss: "threshold criteria follow marking schemes; practice days set by the regulator (S4)" }
  - { number: "4.11", order: 115, componentType: stem, parent: "section 4", heading: "Bachelor's degree with honours: Minimum standards", gloss: "lead-in: the honours threshold in four categories, with 34 lettered outcomes (S4, 38 records)" }
  - { number: "4.12", order: 116, componentType: paragraph, parent: "section 4", heading: "Integrated master's degree: Threshold level (3rd class degree)", gloss: "what an integrated master's adds, meeting both undergraduate and master's standards (S4)" }
  - { number: "4.13", order: 117, componentType: paragraph, parent: "section 4", heading: "Integrated master's degree: Threshold level (3rd class degree)", gloss: "integrated master's graduates must reach at least threshold, as in 4.11 (S4)" }
  - { number: "4.14", order: 118, componentType: paragraph, parent: "section 4", heading: "Integrated master's degree: Threshold level (3rd class degree)", gloss: "lead-in: the integrated master's threshold in four categories (S4, 6 records)" }
  - { number: "4.15", order: 119, componentType: paragraph, parent: "section 4", heading: "Postgraduate master's degree benchmark standards", gloss: "the master's standards also apply to postgraduate certificates and diplomas" }
  - { number: "4.16", order: 120, componentType: paragraph, parent: "section 4", heading: "Postgraduate master's degree: Threshold level (pass degree)", gloss: "master's graduates must reach at least threshold across outcome categories (S4)" }
  - { number: "4.17", order: 121, componentType: paragraph, parent: "section 4", heading: "Postgraduate master's degree: Threshold level (pass degree)", gloss: "lead-in: the postgraduate master's threshold in four categories (S4, 8 records)" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Social Work degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Social Work course", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "none", heading: "Contents", kind: "contents" }
  - { number: "5", heading: "List of references and further resources", kind: "references" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "acknowledgements" }
  - { number: "none", heading: "Fifth Edition; publication date; copyright notice", kind: "other: back matter, read for S1 and S8" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 88 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/social-work-2026/1.8
  locator: { number: "1.8", headingPath: ["Context and purposes of a Social Work degree", "Purposes and characteristics of a Social Work degree"] }
  span: { start: 11521, end: 12361 }
  source: "1.8 Social work is practised in a diverse range of settings, reflecting the diversity and complexity of contemporary society. The dynamic relationship between society, the state, and the profession remains fundamental to social work's role in supporting individuals affected by trauma and those in need or at risk. Operating in contexts marked by uncertainty,\n\n4\ncomplexity and ambiguity, social workers must be equipped with the knowledge and skills to navigate these challenges effectively. The administration of social work in some sectors includes the development of social policy and legislation. Social workers are also expected to engage critically with ongoing debates concerning the nature, scope and purpose of the profession, and to demonstrate the capacity to analyse, adapt to, manage, and ultimately lead processes of change.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must
  level: none
  appliesTo: "social workers, and so those qualifying"
  addressee: learner
  verbs: ["equipped", "engage", "demonstrate", "analyse", "manage", "lead"]
  about: "equipped for complexity and able to lead change"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Because the work takes place amid uncertainty, complexity and ambiguity, social workers must have the knowledge and skills to cope with it; they are also expected to take a critical part in debate about what the profession is for and to show they can analyse, adjust to, manage and in time lead change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/1.14
  locator: { number: "1.14", headingPath: ["Context and purposes of a Social Work degree", "Equity, equality, diversity and inclusion"] }
  span: { start: 14744, end: 15230 }
  source: "1.14 Course providers have a duty to make reasonable adjustments for their students to provide an accessible learning environment open to all, including those with protected characteristics. This approach aligns with the International Federation of Social Workers (IFSW) definition of social work, and specifically 'principles of social justice, human rights, collective responsibility and respect for diversities are central to social work' as well as relevant professional standards.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "duty" read as must
  level: none
  appliesTo: "course providers"
  addressee: provider
  verbs: ["make", "provide"]
  about: "duty to make reasonable adjustments"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Course providers carry a duty to adjust reasonably for students so the learning environment is accessible to everyone, those with protected characteristics included, in keeping with the IFSW principles of justice, rights, shared responsibility and respect for difference."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of a Social Work degree", "Equity, equality, diversity and inclusion"] }
  span: { start: 17279, end: 17582 }
  source: "1.17 Course providers and practice placements have a legal duty to make reasonable adjustments for students to provide an accessible learning environment open to all, including those with protected characteristics. Further guidance is available in QAA's Creating Inclusive Subject Learning Communities.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "duty" read as must
  level: none
  appliesTo: "course providers and practice placements"
  addressee: provider
  verbs: ["make", "provide"]
  about: "legal duty to adjust, on courses and placements"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Both course providers and practice placements hold a legal duty to adjust reasonably so the learning environment is open and accessible to all students, including those with protected characteristics; QAA guidance on inclusive subject communities gives more."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of a Social Work degree", "Accessibility and the needs of disabled students"] }
  span: { start: 21829, end: 22254 }
  source: "1.24 Courses can be designed to accommodate students with individual requirements, ensuring accessibility is embedded in both curriculum design and the broader student experience. Course providers are expected to make anticipatory reasonable adjustments to teaching, learning and assessment, whether on campus, online or in practice settings, to enable all students to achieve and demonstrate the intended learning outcomes.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "requirements" read as must
  level: none
  appliesTo: "course providers"
  addressee: provider
  verbs: ["make", "enable"]
  about: "anticipatory reasonable adjustments in every setting"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses can be built to accommodate individual needs with access designed in, and providers are expected to make adjustments in advance to teaching, learning and assessment, on campus, online and in practice, so that every student can reach and show the intended outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/1.45
  locator: { number: "1.45", headingPath: ["Context and purposes of a Social Work degree", "Generative artificial intelligence"] }
  span: { start: 35356, end: 36156 }
  source: "1.45 Contemporary and emerging forms of artificial intelligence, including Generative artificial intelligence (GenAI), have become integral components of modern society. These technologies not only underpin but actively shape social relationships, individual lived experiences, sociopolitical discourse, and numerous other facets of community and cultural life. Social Work students and social workers critically engage with technologies in their learning and practice to ensure effective support for people, congruent with social work values. Course providers can support students to use technologies competently and critically, legally and ethically, and for the benefit of individuals and communities. It is expected that procedures will be in place to ensure authenticity and academic integrity.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "course providers"
  addressee: provider
  verbs: ["ensure"]
  about: "procedures for authenticity and integrity with generative AI"
  themes: [theme:generative-ai]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "AI, generative AI included, now shapes society and practice; students and social workers engage with it critically to support people in line with social work values, providers can help them use it competently, critically, lawfully and ethically, and procedures will be in place to protect authenticity and academic integrity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/1.46
  locator: { number: "1.46", headingPath: ["Context and purposes of a Social Work degree", "Generative artificial intelligence"] }
  span: { start: 36156, end: 37155 }
  source: "1.46 There are many ways to engage with technologies, in various places and spaces: higher education (or other) settings, online and virtual spaces, practice learning contexts, and others. Students and educators engage with technologies at both an individual level, within whole groups, and across communities and societies, and with differing levels of access and accessibility. Students and educators need to be able to navigate these from a variety of perspectives, keeping abreast of evolving technologies and their uses, and harnessing their far-reaching impacts for enhancing learning and teaching, research, practice learning, and social work practice. Educators and placement providers engage with ways technologies can empower and improve the lives of people and communities, and recognise, respond to and challenge the risks and discrimination they can create and reinforce for individuals and groups. Further guidance and support is provided in QAA advice and resources on Generative AI.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: none
  appliesTo: "students and educators"
  addressee: both
  verbs: ["navigate"]
  about: "navigating technologies and their risks"
  themes: [theme:generative-ai]
  domain: generic-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Technologies are met in many places and at many scales, with unequal access; students and educators need to handle them from varied angles, keep up with change and use them to improve learning, research and practice, while recognising and challenging the harm and discrimination they can create."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/1.48
  locator: { number: "1.48", headingPath: ["Context and purposes of a Social Work degree", "Generative artificial intelligence"] }
  span: { start: 37587, end: 37816 }
  source: "1.48 It is expected that social work values guide student and educator engagements with technology throughout the learning journey and that technologies and digital options do not replace human relationships or interactions.\n\n12\n"
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "students and educators"
  addressee: both
  verbs: ["guide", "replace"]
  about: "values guide technology; it never replaces relationships"
  themes: [theme:generative-ai]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Social work values are expected to steer how students and staff use technology throughout learning, and technology and digital options should not stand in for human relationships or contact."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of a Social Work course", "Design"] }
  span: { start: 39364, end: 40181 }
  source: "2.4 Social Work education is rooted in values and ethics that require social work practitioners to recognise the dignity of the individual, but also to make and implement difficult decisions (including the restriction of liberty) in human situations that involve the potential for benefit or harm. Courses therefore involve the study and application of, and critical reflection upon, ethical principles and professional dilemmas as a core requirement. Reflected by the four nations' regulators, this involves showing respect for persons, honouring the diverse and distinctive organisations and communities that make up society, promoting social justice and combating processes that lead to discrimination, racism, marginalisation, inequality and social exclusion, which impact upon the individual, family or society.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Social Work courses"
  addressee: provider
  verbs: ["involve"]
  about: "ethics and dilemmas as a core requirement"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Social work education rests on values and ethics that ask practitioners to respect individual dignity yet also to take and carry out hard decisions, liberty included, where benefit and harm are both possible; courses therefore require the study, use of and critical reflection on ethical principles and dilemmas, which the regulators of all four nations reflect."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of a Social Work course", "Design"] }
  span: { start: 41513, end: 42273 }
  source: "2.8 Social work, both as an occupational practice and as an academic subject, evolves, adapts and changes in response to the social, political and economic challenges and demands of contemporary social welfare policy, practice and legislation. Social work is responsive to change in supporting people and communities. While social work is undertaken in a wide range of settings, the relationship between society, state and social work remains central to the role of social work. Qualified social workers therefore need to be equipped both to understand and to work within this context of contested debate about the nature, scope and purpose of social work, and be enabled to analyse, adapt to, manage and eventually lead processes of change. Regulatory bodies\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: none
  appliesTo: "qualified social workers, and so those qualifying"
  addressee: learner
  verbs: ["understand", "work", "analyse", "manage", "lead"]
  about: "working within contested debate and leading change"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Social work changes with social, political and economic pressures and with policy and law; qualified social workers need to be ready to understand and work within argument over the profession's nature and purpose, and to analyse, adapt to, manage and finally lead change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of a Social Work course", "Regulatory bodies: Cymru/Wales"] }
  span: { start: 42843, end: 43626 }
  source: "2.11 Social Work courses must be approved by Social Care Wales. The professional requirements for the Social Work degree are contained in the framework for Social Work Qualifications. The award in Wales is based on the National Occupational Standards, the Code of Professional Practice for Social Care, and this Subject Benchmark Statement. Social Work degrees may be offered as a bachelor's degree or a postgraduate qualification. Courses are delivered through partnerships between degree-awarding bodies and local authority employers and comprise both academic and practical learning. Social Work degrees in Wales must be informed by contemporary legislation and social policy, as well as regulatory developments relevant to Wales and their relationship to the UK-wide context(s).\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Social Work courses in Wales"
  addressee: provider
  verbs: ["approved", "informed"]
  about: "approval by Social Care Wales and the Welsh context"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "In Wales, courses must have Social Care Wales approval; the professional requirements sit in its qualifications framework and the award draws on the National Occupational Standards, the Welsh code of practice for social care and this statement; degrees run through partnerships with local authority employers and must reflect current Welsh law, policy and regulation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of a Social Work course", "Regulatory bodies: Cymru/Wales"] }
  span: { start: 43626, end: 43859 }
  source: "2.12 Social Work students must register with Social Care Wales and demonstrate both an understanding of, and ability to adhere to, the Code of Professional Practice for Social Care throughout their studies and into practice. England\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Social Work students in Wales"
  addressee: learner
  verbs: ["register", "demonstrate", "adhere"]
  about: "registering with Social Care Wales and following its Code"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Students in Wales must register with Social Care Wales and show that they understand and keep to its Code of Professional Practice for Social Care, during their studies and on into practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of a Social Work course", "Regulatory bodies: England"] }
  span: { start: 44093, end: 44680 }
  source: "2.14 Social Work courses must be approved by Social Work England with courses needing to meet the Education and Training Standards and produce graduates who can demonstrate that they meet the Professional Standards. Social Work England-approved courses also reflect the wider curriculum guidance available for the profession, including Social Work England's knowledge, skills and behaviours and this Subject Benchmark Statement. The Professional Standards Authority oversees Social Work England as well as eight other health and care professional regulatory bodies operating in England.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Social Work courses in England"
  addressee: provider
  verbs: ["approved", "meet", "demonstrate"]
  about: "approval by Social Work England against its standards"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "In England, courses must have Social Work England approval, meeting its Education and Training Standards and producing graduates who can show they meet its Professional Standards; approved courses also reflect wider curriculum guidance and this statement, and the Professional Standards Authority oversees the regulator."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/2.17
  locator: { number: "2.17", headingPath: ["Distinctive features of a Social Work course", "Regulatory bodies: Northern Ireland"] }
  span: { start: 45381, end: 46375 }
  source: "2.17 The Northern Ireland Assembly is responsible for overseeing the delivery of education and integrated health and social services in Northern Ireland. The Social Care Council and the Department of Health, Social Services and Public Safety (now the Department of Health) jointly produced the Northern Ireland Framework Specification for the Degree in Social Work (2003), which was reviewed and updated in 2014, then further amended in 2015. This sets out a single comprehensive set of learning requirements and outcomes for degrees in Social Work. It is framed by the relevant national occupational standards and the QAA Subject Benchmark Statement for Social Work. In addition, there are several distinctive learning requirements and outcomes that are specific to Northern Ireland. Students are required to understand the impact of Northern Ireland's political violence on their practice and consider their role in integrated health and social care organisations in a post-conflict society.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Social Work students in Northern Ireland"
  addressee: learner
  verbs: ["understand", "consider"]
  about: "political violence and integrated care in Northern Ireland"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Northern Ireland's framework specification, written jointly by the regulator and the health department, gives one set of learning requirements and outcomes, with some particular to the region, where students are required to grasp how its political violence bears on their practice and to consider their place in integrated health and social care after conflict."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/2.18
  locator: { number: "2.18", headingPath: ["Distinctive features of a Social Work course", "Regulatory bodies: Northern Ireland"] }
  span: { start: 46375, end: 46913 }
  source: "2.18 Since September 2004, an honours-level degree in Social Work is the recognised professional qualification for all social workers, probation officers and education welfare officers in Northern Ireland. Following the introduction of the protection of title on 1 June 2005, all Social Work students and qualified social workers are required to register with the Social Care Council. Social Work graduates in Northern Ireland are registered by the Social Care Council with a condition that they undertake an Assessed Year in Employment.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Social Work students and social workers in Northern Ireland"
  addressee: learner
  verbs: ["register", "undertake"]
  about: "registration and the assessed year in Northern Ireland"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Since 2004 an honours degree in Social Work is the recognised qualification there for social workers, for probation officers and for education welfare officers; since protection of title in 2005 every student and qualified social worker is required to register with the Social Care Council, and graduates register on condition of an Assessed Year in Employment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/2.21
  locator: { number: "2.21", headingPath: ["Distinctive features of a Social Work course", "Regulatory bodies: Scotland"] }
  span: { start: 47550, end: 48538 }
  source: "2.21 All qualifying courses in Social Work are approved by the SSSC which was established in October 2001 under the Regulation of Care (Scotland) Act 2001. It aims to strengthen professionalism, raise standards of practice, and ensure the social services workforce is trained, trusted and skilled. It maintains registers of the workforce, sets codes of practice, regulates training and education, and investigates cases where workforce standards are not met. As the social worker title is protected in law, to practice as a social worker in Scotland requires a recognised social work qualification and registration with the SSSC. The Standards in Social Work Education and Ethical Principles and the Scottish Requirements for Social Work Education have both been revised since the Framework for Social Work Education was published in 2003. Social Work students must achieve a generic honours degree in Social Work, or an equivalent postgraduate award, to become professionally qualified.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Social Work students in Scotland"
  addressee: learner
  verbs: ["achieve"]
  about: "the qualifying award and SSSC registration in Scotland"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The SSSC approves all qualifying courses, keeps registers, sets codes and regulates training; practising in Scotland needs a recognised qualification and SSSC registration, and to qualify professionally students must gain a generic Social Work honours degree or a postgraduate award of equal standing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/2.23
  locator: { number: "2.23", headingPath: ["Distinctive features of a Social Work course", "Progression"] }
  span: { start: 48668, end: 49380 }
  source: "2.23 Over the course of a standard undergraduate degree with honours (FHEQ Level 6; FQHEIS/SCQF Level 10) or, if available, an integrated master's degree (FHEQ Level 7; FQHEIS/SCQF Level 11) a Social Work student will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the attainment of knowledge, expertise and experience that builds towards the final achievement of meeting the threshold subject-specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including practice components.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students progressing through a course"
  addressee: both
  verbs: ["progress", "include"]
  about: "progression through levels to the threshold skills"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Across an honours degree (FHEQ 6; SCQF 10) or an integrated master's (FHEQ 7; SCQF 11), students move from level to level under each institution's rules; each level is expected to build towards meeting the threshold subject and generic skills, usually with credit gained for all learning and assessment, practice included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/2.24
  locator: { number: "2.24", headingPath: ["Distinctive features of a Social Work course", "Progression"] }
  span: { start: 49380, end: 49918 }
  source: "2.24 Social Work can be studied as a Bachelor of Science (BSc) or Arts (BA) degree, or an equivalent postgraduate conversion course, as well as at a more advanced level – for example, as a postgraduate diploma (PgDip) or as a Master of Science (MSc or MSci) or Arts (MA). The range of programme pathways is diverse, including through a degree apprenticeship. All these options will include practice learning integrated into the programme, to provide students with an opportunity to apply and develop their skills in real-life situations.\n"
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "all Social Work routes"
  addressee: provider
  verbs: ["include", "apply", "develop"]
  about: "practice learning integrated into every route"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Social work can be taken as a BA or BSc, a postgraduate conversion, a PgDip, an MSc, MSci or MA, or a degree apprenticeship, and every one of these routes will build in practice learning so students can use and grow their skills in real situations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/2.27
  locator: { number: "2.27", headingPath: ["Distinctive features of a Social Work course", "Progression"] }
  span: { start: 50574, end: 51081 }
  source: "2.27 Ethical understanding, ethical behaviour, social justice and professional values are at the core of social work and therefore central to course design. For example, there will be a range of activities that will facilitate the comprehensive application of social work values and ethics in research, professional practice and everyday conduct. Students will be able to apply this to their own value base and ethical behaviour as well as critically evaluating the ethical behaviour of others. Flexibility\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["apply", "evaluating"]
  about: "applying ethics to oneself and judging others"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Ethics, social justice and professional values sit at the centre of design, with activities that carry values into research, practice and daily conduct; students will be able to bring this to bear on their own values and behaviour and to judge critically how others behave ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/2.34
  locator: { number: "2.34", headingPath: ["Distinctive features of a Social Work course", "Partnership"] }
  span: { start: 54519, end: 54819 }
  source: "2.34 Social Work courses are expected to work in partnership with people with lived or living experience to promote understanding, empathy and effective practice. This allows students to hear a diverse range of perspectives and challenge their perceptions, as well as encouraging broader reflection.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: none
  appliesTo: "Social Work courses"
  addressee: provider
  verbs: ["work", "promote"]
  about: "partnership with people with lived experience"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses are expected to work alongside people with lived or living experience to build understanding, empathy and good practice, so students hear many perspectives, test their assumptions and reflect more widely."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/2.35
  locator: { number: "2.35", headingPath: ["Distinctive features of a Social Work course", "Partnership"] }
  span: { start: 54819, end: 55320 }
  source: "2.35 Courses work in partnership with practice learning providers and relevant external stakeholders. Practice-based learning will be subject to a collaborative written agreement between practice educators, supervisors, course providers, placement providers, and students. Social Work courses are expected to ensure that the views of employers, practitioners and people with lived or living experience of social work are incorporated into the design, ongoing development and review of the curriculum.\n"
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Social Work courses and practice partners"
  addressee: provider
  verbs: ["ensure"]
  about: "written practice agreements and stakeholder views in design"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses partner with practice learning providers and stakeholders; practice-based learning will rest on a written agreement among practice educators, supervisors, course and placement providers and students, and courses are expected to bring in the views of employers, practitioners and those with lived experience when designing and reviewing the curriculum."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/2.36
  locator: { number: "2.36", headingPath: ["Distinctive features of a Social Work course", "Partnership"] }
  span: { start: 55320, end: 55462 }
  source: "2.36 Courses should be written in alignment with the regulatory body standards relevant to the country in which they are being delivered.\n\n17\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Social Work courses"
  addressee: provider
  verbs: ["written"]
  about: "alignment with the relevant regulator's standards"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should be written to align with the standards of the regulator in the nation where they run."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/2.39
  locator: { number: "2.39", headingPath: ["Distinctive features of a Social Work course", "Monitoring and review"] }
  span: { start: 56597, end: 56896 }
  source: "2.39 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers as part of periodic review to gain an independent perspective on any proposed changes and ensure threshold standards are achieved, and content is appropriate for the subject.\n"
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Externality is essential to UK quality assurance: providers will bring in external reviewers in periodic review for an independent view of proposed changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/2.42
  locator: { number: "2.42", headingPath: ["Distinctive features of a Social Work course", "Monitoring and review"] }
  span: { start: 58038, end: 58220 }
  source: "2.42 Social Work courses will require approval and ongoing monitoring from regulatory bodies. These are usually done through a combination of site visits and desk-based reviews.\n\n18\n"
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Social Work courses"
  addressee: provider
  verbs: ["require"]
  about: "regulatory approval and ongoing monitoring"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses will need regulators' approval and continuing monitoring, usually through a mix of visits and desk review."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/3.1
  locator: { number: "3.1", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 58262, end: 58933 }
  source: "3.1 Providers use the relevant national qualifications frameworks pertaining in the specific jurisdiction in designing courses at specific levels. It is expected that Social Work course content is based on principles of being relevant, contemporary, evidence informed, current and coherent. It is beneficial if courses are co-produced with stakeholders, as well as responsive to emerging need and insights, locally, nationally and globally. Course content that is inclusive and decolonised supports social work values. Social Work students learn to work with and to support individuals, families, groups and communities in a variety of settings and across the life span.\n"
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "Social Work courses"
  addressee: provider
  verbs: ["use", "based"]
  about: "principles for course content"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Providers design at set levels using the national frameworks of their nation; content is expected to be relevant, up to date, evidence informed, current and coherent, and co-production, responsiveness and inclusive, decolonised content are welcomed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 60005, end: 60724 }
  source: "3.4 The necessity to engage in practical learning is a fundamental part of the Social Work curriculum. Conducted in work-based settings, practice-based learning involves active participation and direct interaction with individuals who have lived or living experience, including parents, carers, wider community and other professionals. It can also encompass observing other professionals and individuals with lived experience, developing and analysing skills, shadowing, supervision, reflective analysis, research, and interdisciplinary or multi-agency interventions within social work and related organisations. There is an expectation for the clear integration and application of social work knowledge into practice.\n"
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "students and courses"
  addressee: both
  verbs: ["engage"]
  about: "practice-based learning and integration of knowledge into practice"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Practical learning is fundamental: in work settings it means taking part directly with people with lived experience, families, carers, communities and other professionals, alongside observation, shadowing, supervision, reflection and research, and knowledge is expected to be clearly integrated into practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/3.6
  locator: { number: "3.6", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 60926, end: 61560 }
  source: "3.6 Teaching and learning is scaffolded in such a way that Social Work students receive a comprehensive induction to higher education and orientation to each level of progression. As students' progress through the course, they assume increasing responsibility for their own learning, preparing them for their future careers. The aim is to design teaching and learning strategies that are inclusive, accessible, engaging, effective and enjoyable for students. It is expected that learning is facilitated by a range of people, including academic staff, researchers, social work practitioners and people with lived or living experience.\n"
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "Social Work courses"
  addressee: provider
  verbs: ["facilitated"]
  about: "scaffolded teaching and a range of facilitators"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching is staged, starting with induction and orientation at each level, students take more responsibility as they progress, and learning is expected to be led by a range of people, including academics, researchers, practitioners and people with lived experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/3.8
  locator: { number: "3.8", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 62247, end: 63235 }
  source: "3.8 Assessment of Social Work students is grounded in principles of inclusivity, accessibility and integrity, and will incorporate feedback and feed forward. The core purpose of assessment is to measure learning and ability, ensure professional standards are met and to provide a means for students to reflect on their performance and receive regular feedback on their achievements and development needs. Courses set tasks that promote learning, develop and test relevant knowledge and skills, drawing on various sources, including practice contexts. Assessments can be authentic and reflect the requirements of the profession. Some assessments across courses may include co-production and co-delivery with stakeholders. Assessment criteria are clearly articulated and linked to module and course learning outcomes. Assessment enables judgments to be made regarding readiness for practice, progress, and the final award, ensuring fitness for practice in line with professional standards.\n"
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Social Work courses"
  addressee: provider
  verbs: ["incorporate"]
  about: "assessment principles and readiness for practice"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment rests on inclusion, accessibility and integrity and will build in feedback and feed forward; it measures learning, checks professional standards and supports reflection, with clear criteria linked to outcomes, and it judges readiness for practice, progress and the final award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/4.1
  locator: { number: "4.1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 63995, end: 64451 }
  source: "4.1 Social Work is a professional social work qualification which can be delivered in an undergraduate honours degree or postgraduate award. It is an academic subject applied through professional practice. Students must demonstrate that they have met both the academic and practice requirements of their course. Graduates are also expected to meet any specific standards set by the relevant regulatory body in the country in which the course is delivered.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Social Work students and graduates"
  addressee: learner
  verbs: ["demonstrate", "met", "meet"]
  about: "academic and practice requirements, and regulators' standards"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Social work is a professional qualification at undergraduate or postgraduate level; students must show they have met both the academic and the practice requirements of their course, and graduates are also expected to meet any standards of the regulator in their nation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 64451, end: 64996 }
  source: "4.2 Please note that minimum threshold standards described here are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards (as defined by the Equality Act 2010 and relevant equality legislation in Northern Ireland) as part of a programme specification, these can be informed by the relevant Subject Benchmark Statement along with any PSRB requirements. In these circumstances, providers should follow the most recent guidance from the Equality and Human Rights Commission.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "providers developing competence standards"
  addressee: provider
  verbs: ["follow"]
  about: "threshold standards are not competence standards"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The minimum threshold standards are not meant as universal competence standards; a provider that sets competence standards under equality law may draw on the statement and PSRB requirements, and in that case should follow the latest Equality and Human Rights Commission guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/4.5
  locator: { number: "4.5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65424, end: 66053 }
  source: "4.5 While the requirements for practice are standard across undergraduate and postgraduate Social Work courses, the academic course and modules will be designed and assessed at the appropriate level, Level 6 (SCQF Level 10 in Scotland) or Level 7 (SCQF Level 11 in Scotland). As such, their application to an individual course is necessarily contextual. All Social Work degrees are accredited by regulatory bodies (see section 2 for more details). Learning outcomes defined by the regulator to support development of knowledge, skills, values and behaviours required for professional registration will also apply. Classification\n"
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Social Work courses"
  addressee: provider
  verbs: ["designed", "assessed", "apply"]
  about: "academic level 6 or 7 and regulator outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Practice requirements are the same across undergraduate and postgraduate routes, but academic study will be designed and assessed at the right level, 6 (SCQF 10) or 7 (SCQF 11); every degree is accredited by a regulator, whose outcomes for registration will also apply."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/4.8
  locator: { number: "4.8", headingPath: ["Benchmark standards", "Classification"] }
  span: { start: 66838, end: 67257 }
  source: "4.8 Similar classification practices are in place for integrated master's courses, with 2:2, 2:1 and 1st class awards. For master's courses, achievement above the threshold results in\n\n21\nawards of merit and distinction. For all awards, criteria for achievement above the threshold will be in line with the higher education provider's common or generic marking schemes. Bachelor's degree with honours Minimum standards\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "providers classifying awards"
  addressee: provider
  verbs: []
  about: "classes above threshold follow the provider's marking schemes"
  themes: [none]
  domain: none
  award: ["integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Integrated master's degrees use similar classes (2:2, 2:1 and first), master's degrees give merit and distinction above the threshold, and for every award the criteria above threshold will follow the provider's common or generic marking schemes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/4.9
  locator: { number: "4.9", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 67257, end: 67535 }
  source: "4.9 Students graduating with a bachelor's degree with honours in Social Work must demonstrate at least a threshold-level of attainment across all categories outlined in four main areas: knowledge and understanding, demonstrable skills, values and ethics, and PSRB requirements.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["demonstrate"]
  about: "at least threshold across four categories"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours graduates in Social Work must show at least threshold attainment in every category of four areas: what they know and understand, the skills they show, values and ethics, and PSRB requirements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.10
  locator: { number: "4.10", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 67535, end: 67923 }
  source: "4.10 Criteria for achievement at threshold level will be in line with the higher education provider's common or generic marking schemes for undergraduate courses and the sector- recognised standards that are in use in each of the nations of the UK. The threshold, including the required number of mandatory days in practice will also be determined by the relevant professional regulator.\n"
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "providers and regulators"
  addressee: provider
  verbs: ["determined"]
  about: "threshold criteria and practice days"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold criteria will follow the provider's common or generic undergraduate marking schemes and the sector standards used in each UK nation, and the regulator will also set the threshold, including the required number of mandatory practice days."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/4.11.a
  locator: { number: "4.11.a", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 68220, end: 68315 }
  source: "awareness of the role of social work across the globe and in the UK and its constituent nations"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "social work's role worldwide and across the UK nations"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown an awareness of what social work does internationally, in the UK and in each of the four UK nations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.aa
  locator: { number: "4.11.aa", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 71886, end: 72047 }
  source: "make and implement difficult decisions (including the restriction of liberty) in human situations that involve the potential for benefit while understanding harm"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["make", "implement", "understanding"]
  about: "difficult decisions, including restricting liberty"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to take and carry out hard decisions, liberty-restricting ones included, in human situations that may bring benefit while understanding the harm involved."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.b
  locator: { number: "4.11.b", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 68319, end: 68406 }
  source: "understanding of social work across statutory, independent, voluntary and third sectors"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "social work across the sectors"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown an understanding of how social work operates in statutory, independent and voluntary bodies and the wider third sector."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.bb
  locator: { number: "4.11.bb", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 72052, end: 72118 }
  source: "confidently defend decisions made, drawing on a wide evidence base"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["defend", "drawing"]
  about: "defending decisions with evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to defend decisions with confidence, using a broad range of evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.c
  locator: { number: "4.11.c", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 68410, end: 68547 }
  source: "the ability to identify, assess and critically apply research to support a strong evidence base to inform and guide professional practice"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["identify", "assess", "apply"]
  about: "research as the evidence base for practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the ability to find, judge and critically use research so that professional practice rests on sound evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.cc
  locator: { number: "4.11.cc", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 72123, end: 72178 }
  source: "demonstrate professional leadership and advocacy skills"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "leadership and advocacy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to show professional leadership and skill in advocacy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.d
  locator: { number: "4.11.d", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 68551, end: 68679 }
  source: "a critical understanding of theory, policy, legislative context, methods and skills, and awareness of how they apply to practice"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["apply"]
  about: "theory, policy, law, methods and skills in practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown a critical understanding of theory, policy, the legal framework, methods and skills, and of how each bears on practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.dd
  locator: { number: "4.11.dd", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 72183, end: 72299 }
  source: "maintain professional boundaries, working within the limits of the role, identifying sources of support where needed"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["maintain", "working", "identifying"]
  about: "professional boundaries"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to keep professional boundaries, stay within the limits of the role and find support when needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.ds
  locator: { number: "4.11.ds", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 70182, end: 70402 }
  source: "a consistent application of social work skills. Reflective application of a range of social work methods, underpinned by critical thinking, evidence-informed decision-making, and understanding of diverse practice context"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "consistent, reflective use of social work skills and methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown consistent use of social work skills and reflective use of a range of methods, grounded in critical thinking, decisions informed by evidence and an understanding of varied practice settings, across items n to hh."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.e
  locator: { number: "4.11.e", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 68683, end: 68810 }
  source: "evidence and demonstration of knowledge, skills and wider behaviours or professional competencies required by regulatory bodies"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "the regulators' required knowledge, skills and behaviours"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown evidence of the knowledge, skills, broader behaviours or professional competences that the regulators require."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.ee
  locator: { number: "4.11.ee", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 72304, end: 72372 }
  source: "critically reflect on their performance, using feedback and evidence"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["reflect", "using"]
  about: "critical reflection on performance"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to reflect critically on one's own performance, drawing on feedback and evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.f
  locator: { number: "4.11.f", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 68814, end: 68931 }
  source: "engagement with contemporary cultural and societal debates, such as those concerning inequality, power and oppression"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "current debates on inequality, power and oppression"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown engagement with current cultural and social debates, for instance about inequality, power and oppression."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.ff
  locator: { number: "4.11.ff", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 72377, end: 72478 }
  source: "engage in continuous professional development, identifying gaps in knowledge and ways to resolve them"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["engage", "identifying", "resolve"]
  about: "continuing professional development"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to take part in continuing professional development, spotting gaps in knowledge and how to close them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.g
  locator: { number: "4.11.g", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 68935, end: 69380 }
  source: "understanding of the relevance of climate change, social, ecological and environmental justice, conflict and diminishing democracy, and the role of social work in addressing the impact on individuals, families and communities, environmental hazards in terms of their impacts on fulfilling individuals' and communities' human rights and the disproportionate burden on those already facing hardship or inequality such as poverty, racism or ableism"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "climate and environmental justice and social work's part"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown an understanding of why climate change, environmental and social justice, conflict and weakening democracy matter, of social work's part in meeting their effects on people and communities, and of how environmental harm and its threat to human rights fall hardest on those already facing poverty, racism, ableism or other disadvantage."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.gg
  locator: { number: "4.11.gg", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 72483, end: 72624 }
  source: "use support and supervision effectively, to maintain safe, effective, accountable and sustainable practice in a demanding working environment"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["use", "maintain"]
  about: "support and supervision"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to make good use of support and supervision so that practice stays safe, effective, accountable and sustainable under heavy demands."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.h
  locator: { number: "4.11.h", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 69384, end: 69462 }
  source: "the ability to understand, identify and appropriately respond to need and risk"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["understand", "identify", "respond"]
  about: "need and risk"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the ability to recognise and make sense of need and risk and to respond to them fittingly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.hh
  locator: { number: "4.11.hh", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 72629, end: 72732 }
  source: "take responsibility for their own wellbeing, including by taking appropriate action and seeking support"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["take", "taking", "seeking"]
  about: "own wellbeing"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to take responsibility for one's own wellbeing, acting appropriately and seeking support."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.i
  locator: { number: "4.11.i", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 69466, end: 69582 }
  source: "recognition of intersectional issues that might impact on need and risk, and to respond and challenge where required"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["respond", "challenge"]
  about: "intersecting factors in need and risk"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown recognition of how overlapping parts of identity and disadvantage can shape need and risk, with the ability to respond and to challenge when needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.j
  locator: { number: "4.11.j", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 69586, end: 69721 }
  source: "understanding of the knowledge base and values of social work, and their integrated application and use when working across disciplines"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "knowledge base and values across disciplines"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown an understanding of the profession's knowledge base and values and of how to apply them together when working with other disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.k
  locator: { number: "4.11.k", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 69725, end: 69869 }
  source: "critical awareness of contested political and societal contexts and commitment to anti- discriminatory, anti-oppressive and anti-racist practice"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "contested contexts and a commitment against oppression"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown critical awareness of disputed political and social contexts, with a commitment to practice that opposes discrimination, oppression and racism."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.ku
  locator: { number: "4.11.ku", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 68058, end: 68204 }
  source: "a coherent knowledge and understanding of the context of professional social work, the knowledge base of social work and its practical application"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "joined-up knowledge of the profession's context, knowledge base and its use"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown a joined-up knowledge and understanding of where professional social work takes place, of what the profession knows and of how that knowledge is used, across items a to m."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.l
  locator: { number: "4.11.l", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 69877, end: 70020 }
  source: "an ability to use knowledge and understanding to effectively relate to people with lived experience and other professionals to improve outcomes"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["use", "relate"]
  about: "relating to people with lived experience and professionals"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the ability to draw on knowledge and understanding to work effectively with people who have lived experience and with other professionals, so that outcomes improve."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.m
  locator: { number: "4.11.m", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 70024, end: 70159 }
  source: "continuous learning, reflection on experience and use of feedback, with the ability to incorporate this in future learning and practice"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["incorporate"]
  about: "continuous learning, reflection and feedback"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown continuing learning, reflection on experience and use of feedback, carried forward into later study and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.n
  locator: { number: "4.11.n", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 70434, end: 70571 }
  source: "use knowledge, understanding and critical thinking to inform practice, drawing on theory, policy, legislative context, methods and skills"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["use", "inform", "drawing"]
  about: "critical thinking informing practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to bring knowledge, understanding and critical thinking to bear on practice, using theory, policy, law, methods and skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.o
  locator: { number: "4.11.o", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 70575, end: 70652 }
  source: "use and evaluate research and wider evidence to inform practice and decisions"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["use", "evaluate", "inform"]
  about: "research and evidence for decisions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to use and weigh research and other evidence when shaping practice and decisions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.p
  locator: { number: "4.11.p", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 70656, end: 70789 }
  source: "build relationships and work in partnership with individuals with lived or living experience, and other professionals across agencies"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["build", "work"]
  about: "relationships and partnership working"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to form relationships and partnerships with people with lived or living experience and with professionals from other agencies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.psrb
  locator: { number: "4.11.psrb", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 72936, end: 73062 }
  source: "Demonstration of the minimum requirements set by the professional regulator, including the required number of days in practice"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "the regulator's minimum requirements, including practice days"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown that the professional regulator's minimum requirements are met, the required number of practice days included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.q
  locator: { number: "4.11.q", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 70793, end: 70837 }
  source: "practice in environmentally sustainable ways"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["practice"]
  about: "environmentally sustainable practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to work in ways that are environmentally sustainable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.r
  locator: { number: "4.11.r", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 70841, end: 71003 }
  source: "communicate effectively verbally, non-verbally and in writing with individuals with lived or living experience, and other professionals across contexts and levels"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["communicate"]
  about: "communication with people and professionals"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to communicate well in speech, without words and in writing with people with lived experience and with professionals in many settings and at many levels."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.s
  locator: { number: "4.11.s", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 71007, end: 71138 }
  source: "work within teams, systems and processes, gathering, processing and analysing information to enable understanding and interventions"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["work", "gathering", "processing", "analysing"]
  about: "teamwork and handling information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to work inside teams, systems and processes, collecting, handling and analysing information to inform understanding and action."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.t
  locator: { number: "4.11.t", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 71142, end: 71193 }
  source: "work across and with other agencies and disciplines"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["work"]
  about: "working across agencies and disciplines"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to work across and alongside other agencies and disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.u
  locator: { number: "4.11.u", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 71197, end: 71352 }
  source: "demonstrate the application of social work values and ethics, including cultural humility and anti-discriminatory, anti-oppressive and anti-racist practice"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "values, ethics and anti-oppressive practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to show social work values and ethics in action, with cultural humility and practice that opposes discrimination, oppression and racism."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.v
  locator: { number: "4.11.v", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 71356, end: 71479 }
  source: "maintain appropriate standards of personal and professional conduct, drawing on relevant codes of practice and/or standards"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["maintain", "drawing"]
  about: "personal and professional conduct"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to keep fitting standards of personal and professional conduct, guided by the relevant codes and standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.ve
  locator: { number: "4.11.ve", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 72757, end: 72915 }
  source: "a commitment to professional social work practice, guided by the core values of the profession, ethical principles and a sense of global social responsibility"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["guided"]
  about: "commitment to professional values and ethics"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown a commitment to professional social work practice steered by the profession's core values, ethical principles and a sense of responsibility to the wider world."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.w
  locator: { number: "4.11.w", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 71483, end: 71584 }
  source: "critically engage with digital technology to collate, analyse, select, record and present information"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["engage", "collate", "analyse", "select", "record", "present"]
  about: "digital technology and information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to use digital technology critically to gather, analyse, choose, record and present information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.x
  locator: { number: "4.11.x", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 71588, end: 71723 }
  source: "exercise an appropriate level of autonomy and decision-making within the context of organisations to ensure safe and effective practice"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["exercise", "ensure"]
  about: "autonomy and decisions within organisations"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to use a suitable degree of independence and judgement within organisations so that practice stays safe and effective."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.y
  locator: { number: "4.11.y", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 71727, end: 71789 }
  source: "support people to improve outcomes, and manage and reduce risk"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["support", "manage", "reduce"]
  about: "improving outcomes and managing risk"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to help people improve their outcomes and to manage and lessen risk."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.11.z
  locator: { number: "4.11.z", headingPath: ["Benchmark standards", "Bachelor's degree with honours: Minimum standards"] }
  span: { start: 71793, end: 71881 }
  source: "recognise the dignity of the individual, working in a strengths-based and empowering way"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["recognise", "working"]
  about: "dignity and strengths-based practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to respect each person's dignity and to work in ways that build on strengths and empower."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.12
  locator: { number: "4.12", headingPath: ["Benchmark standards", "Integrated master's degree: Threshold level (3rd class degree)"] }
  span: { start: 73126, end: 73467 }
  source: "4.12 Integrated master's degrees in Social Work typically add an extra year of full-time equivalent study to an honours degree in Social Work and include the equivalent of a year's worth of study at master's level, often including research and are required to meet the benchmarks of both an undergraduate and a master's Social Work degrees.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "integrated master's courses"
  addressee: provider
  verbs: ["add", "include", "meet"]
  about: "integrated master's meets both levels"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Integrated master's degrees usually add a further full-time year to honours, with about a year at master's level, often research, and are required to satisfy the standards for undergraduate and for master's social work degrees alike."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-work-2026/4.13
  locator: { number: "4.13", headingPath: ["Benchmark standards", "Integrated master's degree: Threshold level (3rd class degree)"] }
  span: { start: 73467, end: 74052 }
  source: "4.13 With regard to undergraduate courses, students graduating with an integrated master's degree in Social Work must demonstrate at least a threshold-level of attainment across all categories outlined in knowledge and understanding, demonstrable skills, values and ethics, and PSRB requirements as detailed in paragraph 4.11 above. Threshold-level attainment often maps onto that associated with a 3rd class honours degree. The threshold, including the required number of mandatory days in practice, will also be determined by the requirements of the relevant professional regulator.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "integrated master's graduates"
  addressee: learner
  verbs: ["demonstrate"]
  about: "integrated master's: at least threshold, as in 4.11"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Integrated master's graduates must show at least threshold attainment across all categories of 4.11; threshold often maps to a third, and the regulator also sets it, including mandatory practice days."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.14.ds
  locator: { number: "4.14.ds", headingPath: ["Benchmark standards", "Integrated master's degree: Threshold level (3rd class degree)"] }
  span: { start: 74555, end: 74623 }
  source: "a consistent application of social work skills (paragraph 4.11 n-hh)"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "consistent use of social work skills"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will have shown consistent use of the social work skills of 4.11 n to hh."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.14.inquiry
  locator: { number: "4.14.inquiry", headingPath: ["Benchmark standards", "Integrated master's degree: Threshold level (3rd class degree)"] }
  span: { start: 74378, end: 74533 }
  source: "Evidence of achievement in completion of an element of self-directed study, involving personal inquiry, for example a research project or synoptic project."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["involving"]
  about: "a self-directed inquiry project"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will have shown evidence of completing a piece of self-directed study built on personal inquiry, such as a research or synoptic project."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.14.ku
  locator: { number: "4.14.ku", headingPath: ["Benchmark standards", "Integrated master's degree: Threshold level (3rd class degree)"] }
  span: { start: 74199, end: 74376 }
  source: "a broad and critical knowledge and understanding of the context of professional social work, the knowledge base of social work and its practical application (paragraph 4.11 a-m)"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "broad, critical knowledge of the profession's context and knowledge base"
  themes: [none]
  domain: knowledge
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will have shown a wide and critical knowledge and understanding of where social work takes place, what it knows and how that is used, across the areas of 4.11 a to m."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.14.methods
  locator: { number: "4.14.methods", headingPath: ["Benchmark standards", "Integrated master's degree: Threshold level (3rd class degree)"] }
  span: { start: 74625, end: 74826 }
  source: "The consistent and reflective application of a range of social work methods, underpinned by critical thinking, evidence-informed decision-making, and a nuanced understanding of diverse practice context"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "consistent, reflective methods with nuanced understanding of settings"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will have shown consistent and reflective use of a range of social work methods, resting on critical thinking, evidence-based decisions and a finely judged grasp of varied practice settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.14.psrb
  locator: { number: "4.14.psrb", headingPath: ["Benchmark standards", "Integrated master's degree: Threshold level (3rd class degree)"] }
  span: { start: 75057, end: 75183 }
  source: "Demonstration of the minimum requirements set by the professional regulator, including the required number of days in practice"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "the regulator's minimum requirements, including practice days"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will have shown that the professional regulator's minimum requirements are met, the required practice days included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.14.ve
  locator: { number: "4.14.ve", headingPath: ["Benchmark standards", "Integrated master's degree: Threshold level (3rd class degree)"] }
  span: { start: 74847, end: 75036 }
  source: "a commitment to and critical understanding of professional social work practice, guided by the core values of the profession, ethical principles, and a sense of global social responsibility"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["guided"]
  about: "commitment to and critical understanding of values"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Will have shown a commitment to, and a critical understanding of, professional practice led by the profession's core values, ethics and a sense of global social responsibility."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.16
  locator: { number: "4.16", headingPath: ["Benchmark standards", "Postgraduate master's degree: Threshold level (pass degree)"] }
  span: { start: 75588, end: 76028 }
  source: "4.16 With regard to postgraduate courses, students graduating with a master's degree in Social Work must demonstrate at least a threshold-level of attainment across all relevant\n\n24\noutcome categories. Threshold-level attainment typically maps onto that associated with a pass degree. The threshold, including the required number of mandatory days in practice, will also be determined by the relevant professional regulator's requirements.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "postgraduate master's graduates"
  addressee: learner
  verbs: ["demonstrate"]
  about: "master's: at least threshold across categories"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates in Social Work must show at least threshold attainment in all relevant outcome categories; threshold usually maps to a pass, and the regulator also sets it, including mandatory practice days."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.17.concepts
  locator: { number: "4.17.concepts", headingPath: ["Benchmark standards", "Postgraduate master's degree: Threshold level (pass degree)"] }
  span: { start: 76344, end: 76451 }
  source: "the capacity to interrogate and apply complex concepts to practice with intellectual rigour and reflexivity"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["interrogate", "apply"]
  about: "interrogating and applying complex concepts"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to question and apply complex concepts in practice with rigour and reflexivity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.17.ds
  locator: { number: "4.17.ds", headingPath: ["Benchmark standards", "Postgraduate master's degree: Threshold level (pass degree)"] }
  span: { start: 76676, end: 76756 }
  source: "a consistent application of social work skills and methods (paragraph\n4.11 n-hh)"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "consistent use of social work skills and methods"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown consistent use of the skills and methods of 4.11 n to hh."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.17.inquiry
  locator: { number: "4.17.inquiry", headingPath: ["Benchmark standards", "Postgraduate master's degree: Threshold level (pass degree)"] }
  span: { start: 76453, end: 76653 }
  source: "Evidence of achievement in completion of an element of self-directed study, involving personal inquiry, for example a research project or synoptic project and the ability to generate original insights"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["involving", "generate"]
  about: "self-directed inquiry with original insight"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown evidence of completing self-directed study built on personal inquiry, such as a research or synoptic project, and the ability to reach original insights."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.17.judgement
  locator: { number: "4.17.judgement", headingPath: ["Benchmark standards", "Postgraduate master's degree: Threshold level (pass degree)"] }
  span: { start: 76920, end: 76987 }
  source: "Exercise professional judgement in ethically challenging situations"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["exercise"]
  about: "professional judgement in ethically hard situations"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown professional judgement in situations that are ethically difficult."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.17.ku
  locator: { number: "4.17.ku", headingPath: ["Benchmark standards", "Postgraduate master's degree: Threshold level (pass degree)"] }
  span: { start: 76163, end: 76323 }
  source: "A critically informed understanding of the contexts shaping professional social work, alongside a sophisticated grasp of its knowledge base (paragraph 4.11 a-m)"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "critically informed understanding of contexts and a sophisticated grasp of the knowledge base"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown a critically informed understanding of what shapes professional social work and a sophisticated command of its knowledge base, across 4.11 a to m."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.17.practice
  locator: { number: "4.17.practice", headingPath: ["Benchmark standards", "Postgraduate master's degree: Threshold level (pass degree)"] }
  span: { start: 76758, end: 76918 }
  source: "Practice is underpinned by critical thinking, evidence-informed decision-making, and understanding of the complexities inherent in diverse practice environments"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["underpinned"]
  about: "practice grounded in critical thinking and evidence"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown practice that rests on critical thinking, decisions informed by evidence and an understanding of the complexity of different practice environments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.17.psrb
  locator: { number: "4.17.psrb", headingPath: ["Benchmark standards", "Postgraduate master's degree: Threshold level (pass degree)"] }
  span: { start: 77251, end: 77377 }
  source: "Demonstration of the minimum requirements set by the professional regulator, including the required number of days in practice"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: []
  about: "the regulator's minimum requirements, including practice days"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown that the professional regulator's minimum requirements are met, the required practice days included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-work-2026/4.17.ve
  locator: { number: "4.17.ve", headingPath: ["Benchmark standards", "Postgraduate master's degree: Threshold level (pass degree)"] }
  span: { start: 77008, end: 77230 }
  source: "a commitment to and critical understanding and application of professional social work practice, guided by the core values of the profession, ethical principles, and a critical understanding of global social responsibility"
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the subject at threshold"
  addressee: learner
  verbs: ["guided"]
  about: "commitment to, critical understanding and application of values"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will have shown a commitment to, and critical understanding and use of, professional practice led by core values, ethics and a critical view of global social responsibility."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/social-work-2026/1.8
  forPractitioner: { text: "Courses prepare students for settings marked by uncertainty and ambiguity: social workers must hold the knowledge and skills these demand, and are expected to debate the purpose of the profession critically and to show they can handle and eventually lead change.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "As a social worker you must be ready for situations that are uncertain, complex and unclear. You will be expected to question what social work is for and to show you can make sense of change, adapt to it, manage it and, later on, lead it.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a statement of what the profession must equip people for, not as a numbered outcome of any award. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 1.8. Do not turn it into a threshold outcome or claim it sets a level. Set it beside qaa/social-work-2026/2.8, qaa/social-work-2026/4.11.x, qaa/social-work-2026/4.11.cc and spine:6 in std:ref:uk-framework."
  author-agent-dialogue: "Raise it when a student or team talks about uncertainty in practice or about leading change. With a student, put it as 'you'; with staff, as what the course must prepare people for. Ask: 'Where have you had to act without a clear answer, and what helped?' Avoid quoting the paragraph at length or treating leadership of change as something a new graduate must already show."
- statement: qaa/social-work-2026/1.14
  forPractitioner: { text: "Make reasonable adjustments so that every student, including those with protected characteristics, can learn in an accessible setting; the statement ties this duty to the profession's own principles as well as to law.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty on the course provider, worded by the issuer as a 'duty' (recorded here as describes, Part E). Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 1.14. Do not present it as a student outcome or as the statement creating a legal duty of its own. Set it beside qaa/social-work-2026/1.17, qaa/social-work-2026/1.24."
  author-agent-dialogue: "Raise it with a programme team reviewing access or adjustments. Frame it as the provider's duty, in plain terms. Ask: 'How would a student with a protected characteristic find out what adjustments are open to them?' Do not put this duty to a student as something they must do."
- statement: qaa/social-work-2026/1.17
  forPractitioner: { text: "The legal duty to make reasonable adjustments reaches placements as well as the university: agree with placement partners how adjustments made on campus carry over into practice settings.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider and placements; the student meets its effect", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a legal duty on courses and on placement settings alike, recorded as describes because the issuer uses 'duty' (Part E). Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 1.17. Do not claim the statement adds to the law. Set it beside qaa/social-work-2026/1.14, qaa/social-work-2026/1.24, qaa/social-work-2026/2.35."
  author-agent-dialogue: "Raise it when a team plans placements or a student's adjustments need to follow them into practice. Frame it for staff as a shared duty with placement partners. Ask: 'Who in the placement knows about this student's agreed adjustments, and how?' Avoid telling a student that arranging adjustments is their job."
- statement: qaa/social-work-2026/1.24
  forPractitioner: { text: "Anticipate adjustments rather than waiting for requests, across campus, online and practice settings, so that all students can meet and evidence the outcomes; build accessibility into the curriculum itself.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: an expectation of the provider; the student meets its effect", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an expectation placed on providers ('expected to', recorded as describes, Part E). Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 1.24. Do not claim it lowers the outcomes; it concerns how students reach them. Set it beside qaa/social-work-2026/1.14, qaa/social-work-2026/1.17, qaa/social-work-2026/3.8."
  author-agent-dialogue: "Raise it with a programme team designing teaching or assessment. Put it as planning ahead for access, including in practice settings. Ask: 'Which assessment in this module would a disabled student find hardest, and what could you change now?' Do not give this to a student as their task."
- statement: qaa/social-work-2026/1.45
  forPractitioner: { text: "Have procedures that protect authenticity and academic integrity where students use generative AI, and support students to use these tools competently, critically, lawfully and ethically for the good of people and communities.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: an expectation of the provider; the student meets its effect", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation that providers will have integrity procedures for AI use. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 1.45. Do not claim it bans or endorses particular tools. Set it beside qaa/social-work-2026/1.46, qaa/social-work-2026/1.48, qaa/social-work-2026/4.11.w."
  author-agent-dialogue: "Raise it when a team reviews assessment design or integrity rules in the light of AI. Frame it for staff as procedures plus support. Ask: 'Would your students know which uses of AI are allowed in this assessment and why?' Avoid presenting it to a student as a rule they must police."
- statement: qaa/social-work-2026/1.46
  forPractitioner: { text: "Staff and students alike need to keep pace with changing technologies, use them to strengthen learning and practice, and recognise and challenge the risks and discrimination they can bring for individuals and groups.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You need to be able to find your way around changing technologies from different points of view, keep up to date, use them to help your learning and practice, and notice and push back on the harm or unfairness they can cause.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a need shared by students and staff, worded 'need to' and recorded as describes (Part E); it is not a numbered outcome. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 1.46. Do not claim it sets a level. Set it beside qaa/social-work-2026/1.45, qaa/social-work-2026/1.48, qaa/social-work-2026/4.11.w and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when someone asks how they should use digital tools or AI in study or practice. With a student say 'you'; with staff, note it applies to them too. Ask: 'Which technology you use could put someone at a disadvantage, and how would you spot it?' Avoid reading the paragraph aloud or treating it as a test students must pass."
- statement: qaa/social-work-2026/1.48
  forPractitioner: { text: "Expect values to steer every use of technology in the course, and keep digital options from replacing the human contact that the profession depends on.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are expected to let social work values guide how you use technology, and to make sure digital tools never take the place of real human relationships with the people you work with.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an expectation ('it is expected', recorded as describes, Part E) for students and staff. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 1.48. Do not claim it forbids digital delivery. Set it beside qaa/social-work-2026/1.45, qaa/social-work-2026/1.46, qaa/social-work-2026/4.11.z."
  author-agent-dialogue: "Raise it when a student or team considers using technology with people who use services. Put it plainly: relationships come first. Ask: 'In this case, what would be lost if the contact happened only through a screen or a tool?' Avoid lecturing or quoting at length."
- statement: qaa/social-work-2026/2.4
  forPractitioner: { text: "Make ethical principles and professional dilemmas a core, required part of the course: their study, their application and critical reflection on them, including decisions that restrict liberty.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on course design; the student-facing outcome is in 4.11 aa and 2.27", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a core requirement of course design, recorded as must from 'core requirement'. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.4. Do not present it as a student outcome in its own right. Set it beside qaa/social-work-2026/2.27, qaa/social-work-2026/4.11.u, qaa/social-work-2026/4.11.aa, qaa/social-work-2026/4.11.ve."
  author-agent-dialogue: "Raise it when a programme team maps where ethics and dilemmas are taught and assessed. Frame it as a required strand of the course. Ask: 'Where do students first practise reasoning through a decision that limits someone's liberty?' Do not hand this to a student as their duty."
- statement: qaa/social-work-2026/2.8
  forPractitioner: { text: "Prepare students to work inside a contested profession: they need to grasp the debate about what social work is for and to build the capacity to handle change and, over time, lead it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You need to understand that people disagree about what social work is for, be able to work within that debate, and build your ability to cope with change, manage it and eventually lead it.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a need ('need to', recorded as describes, Part E) for qualified practitioners, which courses prepare for. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.8. Do not claim graduates must already lead change at the award. Set it beside qaa/social-work-2026/1.8, qaa/social-work-2026/4.11.cc, qaa/social-work-2026/4.11.k and qaa/fheq-2024/4.15.b9.2."
  author-agent-dialogue: "Raise it when a student is unsettled by conflicting views of the profession's role. Put it plainly and in the second person. Ask: 'Which view of social work's purpose do you lean towards, and what would someone who disagrees say?' Avoid settling the debate for them."
- statement: qaa/social-work-2026/2.11
  forPractitioner: { text: "For a Welsh course, secure Social Care Wales approval, meet its qualifications framework, deliver through partnership with local authority employers, and keep content current with Welsh legislation, social policy and regulation.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course in Wales; the student-facing rule is in 2.12", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement on Welsh courses (must), set by Social Care Wales, not by QAA. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.11. Do not claim the statement approves courses. Set it beside qaa/social-work-2026/2.12, qaa/social-work-2026/2.36, qaa/social-work-2026/2.42."
  author-agent-dialogue: "Raise it with a team running or planning a course in Wales. Frame it as the regulator's approval route. Ask: 'Which Welsh legislation or policy changed this year, and where does the course pick it up?' Do not present it to a student as their obligation."
- statement: qaa/social-work-2026/2.12
  forPractitioner: { text: "Students on Welsh courses must register with Social Care Wales and show they understand and follow its Code of Professional Practice while studying and after qualifying.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you study in Wales, you must register with Social Care Wales and show that you understand its Code of Professional Practice and follow it, both while you study and once you qualify.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a must on students in Wales that comes from the Welsh regulator. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.12. Do not claim it applies in England, Scotland or Northern Ireland. Set it beside qaa/social-work-2026/2.11, qaa/social-work-2026/2.18, qaa/social-work-2026/4.11.v."
  author-agent-dialogue: "Raise it with a student starting a course in Wales, or one unsure about conduct rules. Say it plainly in the second person. Ask: 'Have you registered yet, and which part of the Code do you find hardest to keep in placement?' Avoid reading the Code out at length."
- statement: qaa/social-work-2026/2.14
  forPractitioner: { text: "For a course in England, secure Social Work England approval against the Education and Training Standards, and make sure graduates can evidence the Professional Standards; reflect the regulator's knowledge, skills and behaviours guidance too.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course in England; the student meets its effect at registration", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a must on English courses that comes from Social Work England. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.14. Do not claim the statement is one of the regulator's standards. Set it beside qaa/social-work-2026/2.36, qaa/social-work-2026/2.42, qaa/social-work-2026/4.11.e."
  author-agent-dialogue: "Raise it with a team preparing for approval or review in England. Frame it as the regulator's route, with the statement as one input. Ask: 'Where in your mapping does each Professional Standard get evidenced by a graduate?' Do not put this to a student as their duty."
- statement: qaa/social-work-2026/2.17
  forPractitioner: { text: "On a Northern Ireland course, students are required to understand the effect of political violence on practice and their role in joined-up health and social care bodies in a society emerging from conflict.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you study in Northern Ireland, you are required to understand how its history of political violence affects your practice and to think about your role in joined-up health and social care in a society after conflict.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('required', recorded as must) on students in Northern Ireland, drawn from its framework specification. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.17. Do not claim it applies elsewhere in the UK. Set it beside qaa/social-work-2026/2.18, qaa/social-work-2026/4.11.k, qaa/social-work-2026/4.11.a."
  author-agent-dialogue: "Raise it with a student or team on a Northern Ireland course, especially before placement. Say it plainly and with care. Ask: 'How might the legacy of the conflict shape what a family expects of you as a social worker?' Avoid lecturing on the history."
- statement: qaa/social-work-2026/2.18
  forPractitioner: { text: "In Northern Ireland, students must register with the Social Care Council, honours is the professional qualification, and new graduates are registered on condition that they complete an Assessed Year in Employment.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you study in Northern Ireland, you must register with the Social Care Council as a student, and once you graduate your registration depends on completing an assessed first year in work.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('required', recorded as must) from the Northern Ireland regulator. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.18. Do not claim the assessed year is part of the degree. Set it beside qaa/social-work-2026/2.12, qaa/social-work-2026/2.21, qaa/social-work-2026/4.11.psrb."
  author-agent-dialogue: "Raise it with a student in Northern Ireland asking about registration or the first job. Say it plainly in the second person. Ask: 'What support will you look for in your assessed year?' Avoid reading out the dates and acts."
- statement: qaa/social-work-2026/2.21
  forPractitioner: { text: "In Scotland, to qualify, students must hold a generic Social Work honours degree or a postgraduate award of equal standing, and practice needs SSSC registration; courses work to the SSSC's revised standards and requirements.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you study in Scotland, to qualify you must gain a generic Social Work honours degree or a postgraduate award of equal standing, and you will need to register with the SSSC to practise.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a must on students in Scotland, set by the Scottish regulator's route to qualification. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.21. Do not claim an ordinary degree qualifies. Set it beside qaa/social-work-2026/2.22, qaa/social-work-2026/2.18, qaa/social-work-2026/4.9 and fqheis:10 (qaa/fqheis-2024/4.16.b1)."
  author-agent-dialogue: "Raise it with a student in Scotland weighing routes into the profession. Say it plainly in the second person. Ask: 'Is the route you are on an honours or postgraduate award approved by the SSSC?' Avoid reading out the history of the regulator."
- statement: qaa/social-work-2026/2.23
  forPractitioner: { text: "Design each level so that it builds towards the threshold subject-specific and generic skills, and expect students to complete and gain credit for every element, practice components included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As you move from one level of your course to the next, each stage builds towards the minimum skills you need by the end, and you will usually need to pass everything, including your practice learning.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation of how levels build towards the threshold, with 'will usually include' for credit. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.23. Do not claim it sets outcomes for earlier levels. Set it beside qaa/social-work-2026/4.9, qaa/social-work-2026/4.11.ku, qaa/social-work-2026/3.5 and spine:4 to spine:6 in std:ref:uk-framework."
  author-agent-dialogue: "Raise it when a student asks how earlier years count or a team plans level outcomes. With a student, say 'you'; with staff, talk about staged design. Ask: 'What from your first year are you still using now?' Avoid suggesting earlier levels must meet the final threshold."
- statement: qaa/social-work-2026/2.24
  forPractitioner: { text: "Whatever the route, from BA to MA or apprenticeship, build practice learning into the programme so that students apply and develop their skills in real situations.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on course design; the student meets its effect", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will on every route: practice learning is part of all of them. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.24. Do not claim it sets a number of practice days; the regulators do (4.10). Set it beside qaa/social-work-2026/3.4, qaa/social-work-2026/4.10, qaa/social-work-2026/4.11.psrb."
  author-agent-dialogue: "Raise it when a team designs a new route, such as an apprenticeship. Frame it for staff as integration, not an add-on. Ask: 'How does what students do in practice feed back into the taught modules?' Do not present it to a student as their responsibility."
- statement: qaa/social-work-2026/2.27
  forPractitioner: { text: "Build activities that apply values and ethics to research, practice and conduct; students will be able to apply them to their own value base and critically evaluate the ethical conduct of others.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to apply social work values and ethics to your own beliefs and behaviour, and to judge critically how ethically other people act.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) for students, not tied to one award. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.27. Do not claim it is one of the lettered threshold outcomes, though it echoes them. Set it beside qaa/social-work-2026/4.11.u, qaa/social-work-2026/4.11.ve, qaa/social-work-2026/2.4."
  author-agent-dialogue: "Raise it when a student reflects on a value conflict in placement. Say it plainly in the second person. Ask: 'Where did your own values pull against what you were asked to do, and how did you judge it?' Avoid moralising or reading the paragraph aloud."
- statement: qaa/social-work-2026/2.34
  forPractitioner: { text: "Partner with people who have lived or living experience so that students hear a wide range of voices, question their own perceptions and reflect more broadly.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: an expectation of the course; the student meets its effect", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an expectation on courses ('expected to', recorded as describes, Part E). Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.34. Do not claim it specifies a model of involvement. Set it beside qaa/social-work-2026/2.35, qaa/social-work-2026/3.6, qaa/social-work-2026/4.11.p."
  author-agent-dialogue: "Raise it when a team reviews how people with lived experience take part. Frame it as partnership, not consultation alone. Ask: 'Where in the course do people with lived experience shape what is taught, not just tell their story?' Do not give this to a student as a duty."
- statement: qaa/social-work-2026/2.35
  forPractitioner: { text: "Put every practice placement under a written collaborative agreement among all parties, and bring employers', practitioners' and lived experience views into curriculum design, development and review.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course and its partners; the student is a party to the agreement but the duty is the course's", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will on placement agreements and an expectation ('expected to', Part E) on stakeholder involvement. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.35. Do not claim it sets the agreement's content. Set it beside qaa/social-work-2026/2.34, qaa/social-work-2026/1.17, qaa/social-work-2026/2.36."
  author-agent-dialogue: "Raise it when a team sets up or reviews placement arrangements. Frame it as shared written agreement and shared design. Ask: 'Does every placement have a written agreement that the student has seen and signed?' Avoid presenting the agreement as the student's job to arrange."
- statement: qaa/social-work-2026/2.36
  forPractitioner: { text: "Write the course so that it lines up with the standards of the regulator for the nation where it is delivered.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a should on course design. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.36. Do not claim the statement can stand in for the regulator's standards. Set it beside qaa/social-work-2026/2.11, qaa/social-work-2026/2.14, qaa/social-work-2026/2.42."
  author-agent-dialogue: "Raise it with a team writing or revising a course. Frame it as aligning to the national regulator. Ask: 'Which regulator's standards is this course mapped against, and when was that mapping last checked?' Do not put this to a student."
- statement: qaa/social-work-2026/2.39
  forPractitioner: { text: "Include external reviewers in periodic review to test proposed changes independently and confirm threshold standards and subject content.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will on providers in periodic review. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.39. Do not claim it describes external examining, which 2.40 covers. Set it beside qaa/social-work-2026/2.42, qaa/social-work-2026/4.9."
  author-agent-dialogue: "Raise it with a team preparing a periodic review. Frame it as external challenge. Ask: 'Who outside the institution will test whether the threshold is secure?' Do not raise it with students."
- statement: qaa/social-work-2026/2.42
  forPractitioner: { text: "Expect regulatory approval and continued monitoring of the course, normally by site visits combined with desk-based review.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will on courses: regulators approve and monitor them. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 2.42. Do not claim QAA approves social work courses. Set it beside qaa/social-work-2026/2.11, qaa/social-work-2026/2.14, qaa/social-work-2026/2.36."
  author-agent-dialogue: "Raise it with a team planning for a regulator's visit. Frame it as ongoing, not one-off. Ask: 'What evidence would a desk review ask for first?' Do not put this to a student."
- statement: qaa/social-work-2026/3.1
  forPractitioner: { text: "Base content on relevance, currency, evidence and coherence; design at the right framework level for your nation; co-produce with stakeholders where you can and make content inclusive and decolonised.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: an expectation of the course", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an expectation ('it is expected', recorded as describes, Part E) on course content. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 3.1. Do not claim it names a particular framework; it refers to the national frameworks in general. Set it beside qaa/social-work-2026/2.26, qaa/social-work-2026/3.4, qaa/social-work-2026/1.21."
  author-agent-dialogue: "Raise it when a team refreshes content. Frame it for staff as five tests of content. Ask: 'Which topic in this module is least current, and whose perspectives are missing from it?' Do not hand this to a student."
- statement: qaa/social-work-2026/3.4
  forPractitioner: { text: "Make practice learning central, with direct work alongside people with lived experience and professionals, and expect students to show clearly how they bring knowledge into practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Learning in practice is a core part of your course: you will work directly with people and other professionals, and you are expected to show clearly how you put what you know into practice.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an expectation on integration ('there is an expectation', recorded as describes, Part E). Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 3.4. Do not claim it sets the length or type of placement. Set it beside qaa/social-work-2026/2.24, qaa/social-work-2026/4.11.n, qaa/social-work-2026/4.11.l and qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise it when a student struggles to link theory with what they do on placement. Say it plainly in the second person. Ask: 'Which idea from your reading did you actually use this week, and how?' Avoid quoting the paragraph's list at length."
- statement: qaa/social-work-2026/3.6
  forPractitioner: { text: "Scaffold teaching from induction onward, hand students more responsibility over time, and involve academics, researchers, practitioners and people with lived experience in facilitating learning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: an expectation of the course", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an expectation ('it is expected', recorded as describes, Part E) on who teaches. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 3.6. Do not claim it fixes a ratio of contributors. Set it beside qaa/social-work-2026/2.34, qaa/social-work-2026/3.8."
  author-agent-dialogue: "Raise it with a team planning teaching across levels. Frame it as scaffolding plus a range of voices. Ask: 'Where does responsibility for learning visibly shift to students?' Do not put it to a student as a duty."
- statement: qaa/social-work-2026/3.8
  forPractitioner: { text: "Ground assessment in inclusion, accessibility and integrity, build in feedback and feed forward, link criteria to outcomes and use assessment to judge readiness and fitness for practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course's assessment", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will on assessment design (feedback and feed forward). Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 3.8. Do not claim it prescribes methods; 3.9 lists examples. Set it beside qaa/social-work-2026/1.24, qaa/social-work-2026/4.11.ee, qaa/social-work-2026/4.10."
  author-agent-dialogue: "Raise it with a team reviewing assessment. Frame it as principles plus readiness for practice. Ask: 'How does feedback on this task help the student with the next one?' Do not put this to a student."
- statement: qaa/social-work-2026/4.1
  forPractitioner: { text: "Assess both academic and practice requirements, since students must show they meet both; graduates also face the national regulator's own standards.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must show that you have met both the academic and the practice requirements of your course, and you will also be expected to meet the standards of the regulator in the nation where you study.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a must on students for both academic and practice requirements, at every award covered. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.1. Do not claim the statement sets the regulator's standards. Set it beside qaa/social-work-2026/4.9, qaa/social-work-2026/4.13, qaa/social-work-2026/4.16, qaa/social-work-2026/4.11.psrb."
  author-agent-dialogue: "Raise it when a student is strong in one side, academic or practice, and weak in the other. Say it plainly in the second person. Ask: 'Which side of your course feels less secure right now, and what is the evidence?' Avoid suggesting one side can make up for the other."
- statement: qaa/social-work-2026/4.2
  forPractitioner: { text: "Do not treat the threshold standards as competence standards in the equality-law sense; if you write competence standards, follow the latest EHRC guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a should on providers that write competence standards, and as a limit on how the threshold is used. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.2. Do not claim the threshold outcomes are competence standards. Set it beside qaa/social-work-2026/4.9, qaa/social-work-2026/1.14."
  author-agent-dialogue: "Raise it when a team proposes using the outcomes to bar a disabled student. Frame it for staff with care. Ask: 'Is this a competence standard you have justified under equality law, or a learning outcome?' Do not raise it with students as their concern."
- statement: qaa/social-work-2026/4.5
  forPractitioner: { text: "Keep practice requirements common across routes while pitching academic modules at Level 6 (SCQF 10) or Level 7 (SCQF 11), and apply the regulator's learning outcomes for registration as well.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on course design", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will on course design: academic level differs, practice does not. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.5. Do not claim practice expectations rise at master's level. Set it beside qaa/social-work-2026/4.9, qaa/social-work-2026/4.12, qaa/social-work-2026/4.16, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it with a team running both undergraduate and postgraduate routes. Frame it as one practice standard, two academic levels. Ask: 'What makes an assignment on your master's route a level 7 task rather than a level 6 one?' Do not put this to a student."
- statement: qaa/social-work-2026/4.8
  forPractitioner: { text: "Classify achievement above the threshold through your institution's common or generic marking schemes, for every award covered.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a provider duty in classification", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will on providers: grading above threshold comes from their own schemes, not from the statement. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.8. Do not claim the statement defines merit or distinction. Set it beside qaa/social-work-2026/4.10 and qaa/fheq-2024/annex-d/summary/r1/2.1."
  author-agent-dialogue: "Raise it when someone asks what a merit or a 2:1 looks like in social work. Frame it as the institution's marking scheme. Ask: 'Which marking descriptors does your institution use above the pass?' Avoid inventing subject criteria for higher classes."
- statement: qaa/social-work-2026/4.9
  forPractitioner: { text: "Make sure every honours graduate reaches at least the threshold in all four areas: knowledge and understanding, skills, values and ethics, and the regulator's requirements.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To gain your honours degree you must reach at least the minimum standard in all four areas: what you know and understand, the skills you show, your values and ethics, and the regulator's requirements.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as the must that makes 4.11 a threshold for the honours award at FHEQ level 6 (SCQF 10). Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.9. Do not claim a strong area can offset a weak one. Set it beside qaa/social-work-2026/4.11.ku, qaa/social-work-2026/4.11.ds, qaa/social-work-2026/4.11.ve, qaa/social-work-2026/4.11.psrb and qaa/fheq-2024/annex-d/summary/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must pass to qualify. Say it plainly in the second person. Ask: 'Which of the four areas do you have the least evidence for so far?' Avoid presenting the minimum as what a good degree looks like."
- statement: qaa/social-work-2026/4.10
  forPractitioner: { text: "Set threshold criteria in line with your undergraduate marking scheme and the sector standards of your nation, and take the number of practice days from the regulator.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a provider and regulator matter", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will on how the honours threshold is set: by marking schemes and by the regulator. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.10. Do not state a number of practice days from the statement. Set it beside qaa/social-work-2026/4.9, qaa/social-work-2026/4.11.psrb, qaa/social-work-2026/4.13, qaa/social-work-2026/4.16."
  author-agent-dialogue: "Raise it when a team asks how many practice days are needed or how the pass is set. Frame it as the regulator's figure and the institution's scheme. Ask: 'Which regulator sets your practice days, and where is that written down?' Do not put this to a student as their task."
- statement: qaa/social-work-2026/4.11.a
  forPractitioner: { text: "At threshold, honours graduates will have shown awareness of the profession's role internationally, across the UK and within each of its four nations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you know what social work does around the world, across the UK and in each of the four UK nations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on social work's role worldwide and across the UK nations. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 a). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.b, qaa/social-work-2026/2.6 and the framework descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at social work's role worldwide and across the UK nations. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'How does social work differ between the nation you train in and another nation or country?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.aa
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to make and carry out difficult decisions, including those that restrict liberty, weighing possible benefit against harm.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can make and carry out hard decisions, including ones that limit someone's freedom, while weighing up the good and the harm they may do.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on difficult decisions, including restricting liberty. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 aa). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.bb, qaa/social-work-2026/2.4, qaa/social-work-2026/4.11.x and the framework descriptor qaa/fheq-2024/4.15.b9.2."
  author-agent-dialogue: "Bring it up when a student or programme team looks at difficult decisions, including restricting liberty. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What would you need to know before agreeing to a decision that limits someone's freedom?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.b
  forPractitioner: { text: "At threshold, honours graduates will have shown understanding of how the profession works in statutory, independent and voluntary organisations and the third sector.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you understand how social work is done in statutory services, independent and voluntary organisations and the third sector.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on social work across the sectors. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 b). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.a, qaa/social-work-2026/4.11.t and the framework descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at social work across the sectors. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What changes for a social worker moving from a local authority to a charity?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.bb
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to justify decisions confidently on a wide evidence base.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can explain and defend your decisions confidently, using a wide range of evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on defending decisions with evidence. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 bb). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.o, qaa/social-work-2026/4.11.aa and the framework descriptor qaa/fheq-2024/4.15.b3.1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at defending decisions with evidence. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'If a manager or a court questioned your last decision, what evidence would you point to?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.c
  forPractitioner: { text: "At threshold, honours graduates will have shown the ability to locate, appraise and critically apply research so that it grounds and steers practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can find research, judge how good it is and use it critically so your practice rests on sound evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on research as the evidence base for practice. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 c). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.o, qaa/social-work-2026/4.11.bb and the framework descriptor qaa/fheq-2024/4.15.b3.2 and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Bring it up when a student or programme team looks at research as the evidence base for practice. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Can you name a study that changed how you would act in a case, and say how far you trusted it?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.cc
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to show professional leadership and advocacy skills.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can show leadership as a professional and speak up for the people you work with.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on leadership and advocacy. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 cc). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/1.8, qaa/social-work-2026/2.8 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Bring it up when a student or programme team looks at leadership and advocacy. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'When did you speak up for someone whose voice was not being heard?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.d
  forPractitioner: { text: "At threshold, honours graduates will have shown critical understanding of theory, policy, law, methods and skills, and of how each applies in practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you understand theory, policy, the law, methods and skills critically, and see how each one shapes what you do in practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on theory, policy, law, methods and skills in practice. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 d). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.n, qaa/social-work-2026/4.11.j and the framework descriptor qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b3.1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at theory, policy, law, methods and skills in practice. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Which law or policy most shaped a decision you saw on placement, and what theory would explain it?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.dd
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to hold professional boundaries, work within the role's limits and identify support where needed.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you keep professional boundaries, stay within the limits of your role and know where to get support when you need it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on professional boundaries. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 dd). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.v, qaa/social-work-2026/4.11.gg and the framework descriptor qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at professional boundaries. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Where was the edge of your role in a recent case, and who did you turn to?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.ds
  forPractitioner: { text: "At threshold, honours graduates will have shown a consistent use of social work skills and a reflective use of varied methods, resting on critical thinking, evidence-based decisions and understanding of different practice settings, as items n to hh set out.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you use social work skills consistently and choose and reflect on a range of methods, thinking critically and basing decisions on evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on consistent, reflective use of social work skills and methods. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 (demonstrable skills). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.n, qaa/social-work-2026/4.11.hh, qaa/social-work-2026/4.14.ds, qaa/social-work-2026/4.17.ds and the framework descriptor qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Bring it up when a student or programme team looks at consistent, reflective use of social work skills and methods. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Which method did you choose for a recent piece of work, and why that one?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.e
  forPractitioner: { text: "At threshold, honours graduates will have shown evidence of the knowledge, skills, behaviours or competences that the relevant regulator requires.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown evidence that you have the knowledge, skills and professional behaviours your regulator asks for.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on the regulators' required knowledge, skills and behaviours. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 e). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.psrb, qaa/social-work-2026/2.14, qaa/social-work-2026/4.1 and the framework descriptor qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Bring it up when a student or programme team looks at the regulators' required knowledge, skills and behaviours. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Where in your portfolio is the evidence for each of your regulator's standards?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.ee
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to reflect critically on their own performance using feedback and evidence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can reflect critically on how you are doing, using feedback and evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on critical reflection on performance. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 ee). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.m, qaa/social-work-2026/4.11.ff and the framework descriptor qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Bring it up when a student or programme team looks at critical reflection on performance. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What does the evidence say about your last piece of direct work, beyond how it felt?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.f
  forPractitioner: { text: "At threshold, honours graduates will have shown engagement with present-day cultural and social debates, inequality, power and oppression among them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you engage with today's cultural and social debates, for example about inequality, power and oppression.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on current debates on inequality, power and oppression. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 f). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.k, qaa/social-work-2026/4.11.i and the framework descriptor qaa/fheq-2024/4.15.b4."
  author-agent-dialogue: "Bring it up when a student or programme team looks at current debates on inequality, power and oppression. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Which current debate about power or inequality affects the people you work with, and where do you stand?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.ff
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to pursue continuing professional development, identifying knowledge gaps and how to address them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you keep developing as a professional, noticing gaps in what you know and finding ways to fill them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on continuing professional development. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 ff). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.m, qaa/social-work-2026/4.11.ee and the framework descriptor qaa/fheq-2024/4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student or programme team looks at continuing professional development. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What gap in your knowledge did you notice this month, and what is your plan for it?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.g
  forPractitioner: { text: "At threshold, honours graduates will have shown understanding of why climate change, environmental and social justice, conflict and democratic decline matter to the profession, of its role in responding to their effects, and of how environmental harm lands hardest on those already disadvantaged.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you understand why climate change, environmental and social justice, conflict and threats to democracy matter for social work, what social workers can do about their effects, and why environmental harm hits people already facing poverty, racism or ableism hardest.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on climate and environmental justice and social work's part. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 g). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.q, qaa/social-work-2026/1.26, qaa/social-work-2026/1.27 and the framework descriptor qaa/fheq-2024/4.15.b4."
  author-agent-dialogue: "Bring it up when a student or programme team looks at climate and environmental justice and social work's part. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'How could a flood, a heatwave or rising energy bills change the needs of a family you work with?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.gg
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to use support and supervision well, keeping practice safe, effective, accountable and sustainable under pressure.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you make good use of support and supervision so that your work stays safe, effective, accountable and sustainable when the pressure is on.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on support and supervision. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 gg). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.dd, qaa/social-work-2026/4.11.hh and the framework descriptor qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at support and supervision. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What did you bring to your last supervision, and what did you take away?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.h
  forPractitioner: { text: "At threshold, honours graduates will have shown the ability to understand, identify and respond appropriately to need and risk.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can recognise need and risk, make sense of them and respond in the right way.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on need and risk. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 h). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.i, qaa/social-work-2026/4.11.y and the framework descriptor qaa/fheq-2024/4.15.b9.2."
  author-agent-dialogue: "Bring it up when a student or programme team looks at need and risk. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'In your last assessment, what told you this was a risk and not just a need?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.hh
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to take responsibility for their own wellbeing, acting appropriately and seeking support.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you look after your own wellbeing, taking sensible action and asking for support when you need it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on own wellbeing. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 hh). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.gg, qaa/social-work-2026/4.11.dd and the framework descriptor qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at own wellbeing. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What tells you that you need to step back and ask for support?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.i
  forPractitioner: { text: "At threshold, honours graduates will have shown recognition of intersecting factors that bear on need and risk, and the ability to respond and challenge where required.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can see how different parts of someone's identity and situation combine to affect need and risk, and that you respond and challenge when you need to.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on intersecting factors in need and risk. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 i). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.h, qaa/social-work-2026/4.11.f, qaa/social-work-2026/4.11.k and the framework descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Bring it up when a student or programme team looks at intersecting factors in need and risk. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Whose combined circumstances did you nearly overlook, and what made you see them?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.j
  forPractitioner: { text: "At threshold, honours graduates will have shown understanding of social work's knowledge and values and how to use them together in interdisciplinary work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you understand what social work knows and values, and how to use both together when you work with other professions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on knowledge base and values across disciplines. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 j). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.t, qaa/social-work-2026/4.11.ku and the framework descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at knowledge base and values across disciplines. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What did you bring to a meeting with health or education colleagues that only social work could?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.k
  forPractitioner: { text: "At threshold, honours graduates will have shown critical awareness of contested political and social contexts and a commitment to practice that challenges discrimination, oppression and racism.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you are critically aware of disputed political and social contexts and committed to practice that stands against discrimination, oppression and racism.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on contested contexts and a commitment against oppression. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 k). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.u, qaa/social-work-2026/4.11.f, qaa/social-work-2026/1.20 and the framework descriptor qaa/fheq-2024/4.15.b4."
  author-agent-dialogue: "Bring it up when a student or programme team looks at contested contexts and a commitment against oppression. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Where have you seen discrimination built into a system, and what could you do about it?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.ku
  forPractitioner: { text: "At threshold, honours graduates will have shown a coherent grasp of the setting of professional social work, of its knowledge base and of how that knowledge is applied, as items a to m set out.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown a joined-up grasp of where social work happens, what the profession knows and how that knowledge is used in practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on joined-up knowledge of the profession's context, knowledge base and its use. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 (knowledge and understanding). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.a, qaa/social-work-2026/4.11.m, qaa/social-work-2026/4.14.ku, qaa/social-work-2026/4.17.ku and the framework descriptor qaa/fheq-2024/4.15.b1, qaa/fqheis-2024/4.16.b1 and spine:6."
  author-agent-dialogue: "Bring it up when a student or programme team looks at joined-up knowledge of the profession's context, knowledge base and its use. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Which part of social work's knowledge base can you link to something you did in practice?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.l
  forPractitioner: { text: "At threshold, honours graduates will have shown the ability to use knowledge to build effective relationships with people with lived experience and with professionals, to improve outcomes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can use what you know to build good working relationships with people who use services and with other professionals, so that things get better for people.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on relating to people with lived experience and professionals. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 l). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.p, qaa/social-work-2026/4.11.r and the framework descriptor qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Bring it up when a student or programme team looks at relating to people with lived experience and professionals. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What did you do to build trust with someone who was wary of social workers?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.m
  forPractitioner: { text: "At threshold, honours graduates will have shown ongoing learning, reflection on what they have experienced and use of feedback, built into later learning and practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you keep learning, reflect on your experience and use feedback, and carry what you learn into your next piece of study or practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on continuous learning, reflection and feedback. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 m). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.ee, qaa/social-work-2026/4.11.ff and the framework descriptor qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/summary/r3/3rd."
  author-agent-dialogue: "Bring it up when a student or programme team looks at continuous learning, reflection and feedback. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What feedback did you act on last term, and what changed because of it?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.n
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to let knowledge and critical thinking shape practice, drawing on theory, policy, law, methods and skills.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can use your knowledge and critical thinking to shape your practice, drawing on theory, policy, the law, methods and skills.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on critical thinking informing practice. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 n). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.d, qaa/social-work-2026/3.4 and the framework descriptor qaa/fheq-2024/4.15.b3.1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at critical thinking informing practice. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What did critical thinking change in a plan you made recently?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.o
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to use and evaluate research and wider evidence in practice and decision-making.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can use and weigh up research and other evidence when you decide what to do.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on research and evidence for decisions. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 o). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.c, qaa/social-work-2026/4.11.bb and the framework descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Bring it up when a student or programme team looks at research and evidence for decisions. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What evidence did you lean on for your last decision, and what would have made you doubt it?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.p
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to build relationships and partnerships with people with lived experience and with professionals across agencies.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can build relationships and work in partnership with people who use services and with professionals from other agencies.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on relationships and partnership working. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 p). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.l, qaa/social-work-2026/4.11.t, qaa/social-work-2026/2.34 and the framework descriptor qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at relationships and partnership working. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What did partnership look like in practice with someone you supported?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.psrb
  forPractitioner: { text: "At threshold, honours graduates will have shown that the regulator's minimum requirements are met, including the set number of practice days.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you meet the minimum requirements of your regulator, including the number of days in practice it sets.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on the regulator's minimum requirements, including practice days. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 (PSRB requirements). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.10, qaa/social-work-2026/4.11.e, qaa/social-work-2026/4.14.psrb, qaa/social-work-2026/4.17.psrb and the framework descriptor qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Bring it up when a student or programme team looks at the regulator's minimum requirements, including practice days. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'How many practice days does your regulator require, and how many have you logged?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.q
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to practise in environmentally sustainable ways.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can work in ways that look after the environment.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on environmentally sustainable practice. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 q). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.g, qaa/social-work-2026/1.28 and the framework descriptor qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Bring it up when a student or programme team looks at environmentally sustainable practice. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What one change would make your practice more sustainable without costing the people you support?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.r
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to communicate effectively, spoken, non-verbal and written, with people with lived experience and with professionals at all levels.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can communicate well, by speaking, writing and through body language, with people who use services and with professionals in many settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on communication with people and professionals. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 r). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.l, qaa/social-work-2026/4.11.w and the framework descriptor qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Bring it up when a student or programme team looks at communication with people and professionals. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'How did you adapt a written record so the person it was about could read it?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.s
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to work within teams and organisational systems, gathering and analysing information to support understanding and intervention.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can work within teams and organisational systems, collecting and analysing information so you understand a situation and can act on it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on teamwork and handling information. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 s). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.t, qaa/social-work-2026/4.11.w and the framework descriptor qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Bring it up when a student or programme team looks at teamwork and handling information. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What information did you gather that changed your team's view of a case?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.t
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to work with and across other agencies and professions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can work with other agencies and professions and across the boundaries between them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on working across agencies and disciplines. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 t). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.j, qaa/social-work-2026/4.11.p, qaa/social-work-2026/1.9 and the framework descriptor qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at working across agencies and disciplines. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'When did another agency see a case differently from you, and how did you work it out?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.u
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to apply the profession's values and ethics, including cultural humility and practice that counters discrimination, oppression and racism.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can put social work values and ethics into action, with cultural humility and in ways that stand against discrimination, oppression and racism.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on values, ethics and anti-oppressive practice. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 u). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.k, qaa/social-work-2026/4.11.ve, qaa/social-work-2026/2.27 and the framework descriptor qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at values, ethics and anti-oppressive practice. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What did cultural humility mean in a conversation you had with a family?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.v
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to maintain proper personal and professional conduct, using the relevant codes of practice or standards.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you keep to proper standards of personal and professional behaviour, guided by the codes and standards that apply to you.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on personal and professional conduct. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 v). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.dd, qaa/social-work-2026/2.12, qaa/social-work-2026/2.19 and the framework descriptor qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Bring it up when a student or programme team looks at personal and professional conduct. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Which part of your code of conduct is hardest to keep outside work, for example online?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.ve
  forPractitioner: { text: "At threshold, honours graduates will have shown a commitment to professional practice led by the profession's core values and ethics and by a sense of global social responsibility.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you are committed to professional social work practice, guided by its core values, its ethics and a sense of responsibility to people everywhere.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on commitment to professional values and ethics. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 (values and ethics). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.u, qaa/social-work-2026/2.27, qaa/social-work-2026/4.14.ve, qaa/social-work-2026/4.17.ve and the framework descriptor qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at commitment to professional values and ethics. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Which core value of the profession did you find hardest to hold to this year?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.w
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to engage critically with digital tools to collate, analyse, select, record and present information.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can use digital technology critically to gather, analyse, choose, record and present information.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on digital technology and information. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 w). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/1.45, qaa/social-work-2026/1.46, qaa/social-work-2026/4.11.s and the framework descriptor qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Bring it up when a student or programme team looks at digital technology and information. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What did you leave out of a digital case record, and why?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.x
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to exercise suitable autonomy and decision-making within organisations, keeping practice safe and effective.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can act with the right amount of independence and make decisions within your organisation so your practice stays safe and effective.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on autonomy and decisions within organisations. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 x). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.aa, qaa/social-work-2026/4.11.dd and the framework descriptor qaa/fheq-2024/4.15.b9.2 and spine:6."
  author-agent-dialogue: "Bring it up when a student or programme team looks at autonomy and decisions within organisations. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Which decision did you take on your own last week, and which did you rightly take to a supervisor?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.y
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to support people towards better outcomes and to manage and reduce risk.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you can help people improve their situation and manage and reduce risk.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on improving outcomes and managing risk. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 y). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.h, qaa/social-work-2026/4.11.aa and the framework descriptor qaa/fheq-2024/4.15.b9.2."
  author-agent-dialogue: "Bring it up when a student or programme team looks at improving outcomes and managing risk. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'How did you balance someone's wishes against the risk in their situation?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.11.z
  forPractitioner: { text: "At threshold, honours graduates will have shown the capacity to recognise individual dignity and to practise in a strengths-based, empowering way.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your honours degree, you will have shown that you respect each person's dignity and work in ways that build on their strengths and give them more control.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every honours graduate in social work must have shown at FHEQ level 6 (SCQF level 10 in Scotland), here on dignity and strengths-based practice. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.11 z). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.u, qaa/social-work-2026/1.48 and the framework descriptor qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Bring it up when a student or programme team looks at dignity and strengths-based practice. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What strength did you find in someone that changed the plan you made with them?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.12
  forPractitioner: { text: "Design an integrated master's so that it meets both the honours threshold and the master's threshold, with around a year of master's-level study, often including research.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on course design", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('required', recorded as must) on integrated master's design at FHEQ 7 (SCQF 11). Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.12. Do not claim the integrated master's escapes the honours outcomes. Set it beside qaa/social-work-2026/4.13, qaa/social-work-2026/4.14.ku, qaa/social-work-2026/4.17.ku and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it with a team designing an integrated master's. Frame it as meeting two sets of standards. Ask: 'Which modules carry the master's-level year, and how is it different from the honours years?' Do not put this to a student."
- statement: qaa/social-work-2026/4.13
  forPractitioner: { text: "Ensure integrated master's graduates reach at least the 4.11 threshold in every category; the regulator sets the practice days.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To gain an integrated master's in social work you must reach at least the minimum standard in every area set for the honours degree, including the practice days your regulator requires.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as the must that applies the honours threshold to the integrated master's. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.13; the reference to 4.11 is a cross-reference, not a new list. Do not claim a third is the expected outcome. Set it beside qaa/social-work-2026/4.11.ku, qaa/social-work-2026/4.12, qaa/social-work-2026/4.14.ku."
  author-agent-dialogue: "Raise it when an integrated master's student asks what they must pass. Say it plainly in the second person. Ask: 'Have you checked your evidence against the honours areas as well as the master's ones?' Avoid presenting the minimum as the target."
- statement: qaa/social-work-2026/4.14.ds
  forPractitioner: { text: "At threshold, integrated master's graduates will have shown a consistent use of the skills listed at 4.11 n to hh.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your integrated master's, you will have shown that you use the core social work skills consistently.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every integrated master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), on top of the honours outcomes, here on consistent use of social work skills. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.14 (demonstrable skills). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.ds, qaa/social-work-2026/4.14.methods and the framework descriptor qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Bring it up when an integrated master's student or team looks at consistent use of social work skills. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Which of the core skills do you use least confidently, and where could you practise it?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.14.inquiry
  forPractitioner: { text: "At threshold, integrated master's graduates will have shown evidence of a completed self-directed element of personal inquiry, such as a research or synoptic project.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your integrated master's, you will have shown that you have completed a piece of independent study driven by your own inquiry, such as a research project or a project that draws your learning together.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every integrated master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), on top of the honours outcomes, here on a self-directed inquiry project. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.14 (knowledge and understanding). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.17.inquiry, qaa/social-work-2026/4.11.c and the framework descriptor qaa/fheq-2024/4.17.b2 and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Bring it up when an integrated master's student or team looks at a self-directed inquiry project. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What question did your project set out to answer, and who chose it?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.14.ku
  forPractitioner: { text: "At threshold, integrated master's graduates will have shown a broad, critical command of the setting, knowledge base and use of social work knowledge, covering 4.11 a to m.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your integrated master's, you will have shown a wide and critical grasp of where social work happens, what the profession knows and how that knowledge is used.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every integrated master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), on top of the honours outcomes, here on broad, critical knowledge of the profession's context and knowledge base. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.14 (knowledge and understanding). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.ku, qaa/social-work-2026/4.17.ku, qaa/social-work-2026/4.12 and the framework descriptor qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Bring it up when an integrated master's student or team looks at broad, critical knowledge of the profession's context and knowledge base. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Where does your knowledge now go beyond what an honours graduate would know?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.14.methods
  forPractitioner: { text: "At threshold, integrated master's graduates will have shown consistent, reflective use of varied methods, grounded in critical thinking, evidence-informed decisions and a nuanced reading of different practice settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your integrated master's, you will have shown that you use a range of social work methods consistently and reflectively, think critically, base decisions on evidence and read different practice settings with care.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every integrated master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), on top of the honours outcomes, here on consistent, reflective methods with nuanced understanding of settings. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.14 (demonstrable skills). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.ds, qaa/social-work-2026/4.17.practice and the framework descriptor qaa/fheq-2024/4.17.b5 and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Bring it up when an integrated master's student or team looks at consistent, reflective methods with nuanced understanding of settings. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'How did the setting change the method you chose in a recent piece of work?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.14.psrb
  forPractitioner: { text: "At threshold, integrated master's graduates will have shown that the regulator's minimum requirements, including practice days, are met.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your integrated master's, you will have shown that you meet your regulator's minimum requirements, including the number of practice days.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every integrated master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), on top of the honours outcomes, here on the regulator's minimum requirements, including practice days. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.14 (PSRB requirements). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.psrb, qaa/social-work-2026/4.13 and the framework descriptor qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Bring it up when an integrated master's student or team looks at the regulator's minimum requirements, including practice days. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Which regulator's requirements apply to your course, and are your practice days complete?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.14.ve
  forPractitioner: { text: "At threshold, integrated master's graduates will have shown commitment to and critical understanding of professional practice shaped by core values, ethics and global social responsibility.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your integrated master's, you will have shown that you are committed to professional social work practice and understand critically how its values, ethics and responsibility to people everywhere shape it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every integrated master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), on top of the honours outcomes, here on commitment to and critical understanding of values. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.14 (values and ethics). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.ve, qaa/social-work-2026/4.17.ve and the framework descriptor qaa/fheq-2024/4.17.b8.1."
  author-agent-dialogue: "Bring it up when an integrated master's student or team looks at commitment to and critical understanding of values. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Where would you challenge how a core value is usually applied, and why?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.16
  forPractitioner: { text: "Ensure master's graduates reach at least the threshold in every relevant category; a pass corresponds to threshold and the regulator sets the practice days.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To gain your master's in social work you must reach at least the minimum standard in every relevant area, including the practice days your regulator requires.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as the must that makes 4.17 a threshold for the master's award at FHEQ level 7 (SCQF 11). Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.16. Do not claim it describes merit or distinction. Set it beside qaa/social-work-2026/4.17.ku, qaa/social-work-2026/4.17.ds, qaa/social-work-2026/4.8 and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a master's student asks what they need to pass. Say it plainly in the second person. Ask: 'Which outcome area do you have least evidence for so far?' Avoid treating the pass as the expected standard."
- statement: qaa/social-work-2026/4.17.concepts
  forPractitioner: { text: "At threshold, master's graduates will have shown the capacity to interrogate complex concepts and apply them to practice rigorously and reflexively.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your master's, you will have shown that you can question complex ideas and apply them to practice with rigour, while staying aware of your own part in what you see.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), here on interrogating and applying complex concepts. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.17 (knowledge and understanding). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.17.ku, qaa/social-work-2026/4.17.practice and the framework descriptor qaa/fheq-2024/4.17.b4.1 and qaa/fheq-2024/4.17.b3."
  author-agent-dialogue: "Bring it up when a master's student or team looks at interrogating and applying complex concepts. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Which concept did you have to adapt to make sense of a real case?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.17.ds
  forPractitioner: { text: "At threshold, master's graduates will have shown a consistent use of the skills and methods set out at 4.11 n to hh.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your master's, you will have shown that you use the core social work skills and methods consistently.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), here on consistent use of social work skills and methods. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.17 (demonstrable skills). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.ds, qaa/social-work-2026/4.14.ds and the framework descriptor qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Bring it up when a master's student or team looks at consistent use of social work skills and methods. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Which core skill do you rely on most, and which do you avoid?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.17.inquiry
  forPractitioner: { text: "At threshold, master's graduates will have shown evidence of a completed self-directed inquiry, such as a research or synoptic project, and the ability to produce original insights.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your master's, you will have shown that you have completed a piece of independent study driven by your own inquiry and can come up with insights of your own.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), here on self-directed inquiry with original insight. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.17 (knowledge and understanding). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.14.inquiry, qaa/social-work-2026/4.11.c and the framework descriptor qaa/fheq-2024/4.17.b3 and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Bring it up when a master's student or team looks at self-directed inquiry with original insight. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What did your project show that you could not have found in the existing literature?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.17.judgement
  forPractitioner: { text: "At threshold, master's graduates will have shown sound professional judgement in ethically challenging situations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your master's, you will have shown that you can make sound professional judgements when a situation is ethically difficult.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), here on professional judgement in ethically hard situations. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.17 (demonstrable skills). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.aa, qaa/social-work-2026/4.17.ve and the framework descriptor qaa/fheq-2024/4.17.b5 and qaa/fheq-2024/4.17.b8.2."
  author-agent-dialogue: "Bring it up when a master's student or team looks at professional judgement in ethically hard situations. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What made a recent situation ethically hard, and how did you reach your judgement?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.17.ku
  forPractitioner: { text: "At threshold, master's graduates will have shown critically informed understanding of the forces shaping the profession and a sophisticated grasp of its knowledge base, covering 4.11 a to m.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your master's, you will have shown a critical understanding of what shapes social work and a sophisticated grasp of what the profession knows.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), here on critically informed understanding of contexts and a sophisticated grasp of the knowledge base. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.17 (knowledge and understanding). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.ku, qaa/social-work-2026/4.14.ku, qaa/social-work-2026/4.17.concepts and the framework descriptor qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Bring it up when a master's student or team looks at critically informed understanding of contexts and a sophisticated grasp of the knowledge base. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Which part of social work's knowledge base would you now question, and on what grounds?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.17.practice
  forPractitioner: { text: "At threshold, master's graduates will have shown practice grounded in critical thinking, evidence-informed decisions and a grasp of the complexity of varied practice environments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your master's, you will have shown that your practice rests on critical thinking and evidence, and that you understand how complex different practice settings can be.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), here on practice grounded in critical thinking and evidence. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.17 (demonstrable skills). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.14.methods, qaa/social-work-2026/4.17.judgement and the framework descriptor qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Bring it up when a master's student or team looks at practice grounded in critical thinking and evidence. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'What made the setting of your last placement complex, and how did that shape your decisions?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.17.psrb
  forPractitioner: { text: "At threshold, master's graduates will have shown that the regulator's minimum requirements, including practice days, are met.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your master's, you will have shown that you meet your regulator's minimum requirements, including the number of practice days.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), here on the regulator's minimum requirements, including practice days. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.17 (PSRB requirements). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.psrb, qaa/social-work-2026/4.16 and the framework descriptor qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Bring it up when a master's student or team looks at the regulator's minimum requirements, including practice days. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'Which regulator's requirements apply to your course, and are your practice days complete?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
- statement: qaa/social-work-2026/4.17.ve
  forPractitioner: { text: "At threshold, master's graduates will have shown commitment to professional practice, with critical understanding and use of it, shaped by core values, ethics and a critical grasp of global social responsibility.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum for your master's, you will have shown that you are committed to professional social work practice, understand and apply its values and ethics critically, and think critically about responsibility to people everywhere.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome: the minimum every master's graduate in social work must have shown at FHEQ level 7 (SCQF level 11), here on commitment to, critical understanding and application of values. Cite it as QAA (2026), Social Work Subject Benchmark Statement, para 4.17 (values and ethics). Do not claim it is a regulator's standard, a mark of a higher class, or that it holds at another level. Set it beside qaa/social-work-2026/4.11.ve, qaa/social-work-2026/4.14.ve and the framework descriptor qaa/fheq-2024/4.17.b8.1."
  author-agent-dialogue: "Bring it up when a master's student or team looks at commitment to, critical understanding and application of values. With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course to secure. Ask: 'How would you explain global social responsibility to a colleague who thinks it is not part of the job?' Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.23; 2.28; 2.30; 4.5; 4.7" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.23; 2.30; 4.5; 4.15" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.29 (ordinary degree and Scottish MA)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.23; 2.29; 2.30; 4.5; 4.7" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.23; 2.30; 4.5" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.23; 2.30; 4.5: honours at FHEQ Level 6, SCQF Level 10 in Scotland); agrees with std:doc:qaa-fheq-2024-framework S5 (Table 1)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.23; 2.30; 4.5: integrated master's and master's at FHEQ Level 7, SCQF Level 11); agrees with std:doc:qaa-fheq-2024-framework S5 (shared descriptor 4.17)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["front matter", "1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.47", "3.1", "3.9"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["front matter", "1.14", "1.17", "1.22", "1.23", "1.24", "1.25", "1.46", "2.32", "3.6", "3.8"] }
- { id: "theme:esd", role: "carries", carriedIn: ["front matter", "1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.37", "2.32"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["front matter", "1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "1.41", "1.42", "1.43", "1.44"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["front matter", "1.45", "1.46", "1.47", "1.48"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-social-work-2019-benchmarks (not yet ingested)", note: "the fourth edition, 2019, a minor update of the 2016 statement (D1, section 6); this is the fifth edition (back matter)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree classification descriptions for honours (4.7); threshold maps to a third, typical to a 2.2 or 2.1, excellent to a first" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ Levels 6 and 7 (2.23, 2.28, 2.30, 4.5, 4.15)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "SCQF/FQHEIS Levels 9, 10 and 11 (2.23, 2.29, 2.30, 4.5, 4.7)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "quoted on ESD as a lens (1.32)" }
- { rel: "refersTo", target: "QAA Quality Code (2024 update) and QAA Glossary (not ingested)", note: "front matter" }
- { rel: "refersTo", target: "QAA, Creating Inclusive Subject Learning Communities (not ingested)", note: "1.17" }
- { rel: "refersTo", target: "QAA advice and resources on Generative AI (not ingested)", note: "1.46" }
- { rel: "refersTo", target: "Social Care Wales requirements: framework for Social Work Qualifications, National Occupational Standards, Code of Professional Practice for Social Care (not yet ingested)", note: "2.11, 2.12" }
- { rel: "refersTo", target: "Social Work England: Education and Training Standards, Professional Standards, knowledge, skills and behaviours (not yet ingested)", note: "2.14, 2.15" }
- { rel: "refersTo", target: "Northern Ireland Framework Specification for the Degree in Social Work (2015); Standards of Conduct and Practice (not yet ingested)", note: "2.17, 2.19" }
- { rel: "refersTo", target: "SSSC: Standards in Social Work Education and Ethical Principles; Scottish Requirements for Social Work Education (not yet ingested)", note: "2.21" }
- { rel: "readWith", target: "std:doc:qaa-social-policy-2026-benchmarks", note: "inferred: a neighbouring 2026 social science statement; no citation in the text" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2026-04"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "none-stated (advisory group named, section 6)"
replacedBy: "none"
other: "Fifth Edition, published 16 April 2026 (back matter)"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- A practice-based profession and an academic discipline, framed by the IFSW global definition: social change, cohesion, empowerment and liberation, on principles of social justice, human rights, collective responsibility and respect for diversity (D1, 1.1, 2.1).
- An academic subject applied through professional practice, marked by work in complex social situations to protect and promote individual and collective wellbeing (D1, 1.7, 2.1).
- Integrated study of knowledge, skills and values with critical use of research, so that practice is central to learning, in placements and in other experiential settings (D1, 1.10, 2.2, 3.4).
- Values and ethics at its root, including hard decisions that may restrict liberty, and a commitment against discrimination, oppression and racism (D1, 1.20, 2.4).
- A regulated profession with a protected title in each UK nation; regulators approve courses and register students and practitioners (D1, 1.4, 1.5, 2.9 to 2.22).
- Its nature and scope are themselves contested and keep changing with social, political and economic pressures (D1, 2.5, 2.7, 2.8).
- People with lived or living experience take part in teaching, design, assessment and review (D1, 2.1, 2.34, 2.35, 2.41, 3.6).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "headed equity, equality, diversity and inclusion (EEDI): central to the subject's practice; intersectionality, anti-oppressive and anti-racist values across design, content, teaching and assessment, a named commitment against anti-Black racism, decolonising the curriculum and the legal duty to adjust (D1, 1.12 to 1.21)"
  statements: ["qaa/social-work-2026/1.14", "qaa/social-work-2026/1.17", "qaa/social-work-2026/4.11.f", "qaa/social-work-2026/4.11.i", "qaa/social-work-2026/4.11.k", "qaa/social-work-2026/4.11.u"]
- theme: theme:accessibility
  inThisSubject: "headed accessibility and the needs of disabled students: equality and Welsh-language law across the four nations, anticipatory adjustments in practice settings as well as on campus, and access support such as bursaries and lent laptops (D1, 1.22 to 1.25)"
  statements: ["qaa/social-work-2026/1.14", "qaa/social-work-2026/1.17", "qaa/social-work-2026/1.24"]
- theme: theme:esd
  inThisSubject: "social work's place in sustainable development and climate impacts, three generations of rights, the SDGs and UNESCO competencies, and an outcome on environmentally sustainable practice (D1, 1.26 to 1.33; 4.11 g, q)"
  statements: ["qaa/social-work-2026/4.11.g", "qaa/social-work-2026/4.11.q"]
- theme: theme:enterprise
  inThisSubject: "headed employability, entrepreneurship and enterprise education: an entrepreneurial mindset read as professional identity, behaviours, attributes and skills for practice, and careers beyond statutory settings (D1, 1.34 to 1.44)"
  statements: []
- theme: theme:generative-ai
  inThisSubject: "critical, lawful and ethical use of AI in learning and practice, integrity procedures, and values that keep human relationships first (D1, 1.45 to 1.48)"
  statements: ["qaa/social-work-2026/1.45", "qaa/social-work-2026/1.46", "qaa/social-work-2026/1.48", "qaa/social-work-2026/4.11.w"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.1", gloss: "principles for content: relevant, current, evidence-informed and coherent; inclusive and decolonised" }
  - { component: "3.2", gloss: "theoretical, factual (research) and practice knowledge" }
  - { component: "3.3", gloss: "research, theory, skills, methods, values and ethics, social policy, law, service leadership and delivery, UK and global contexts" }
practices:
  - { component: "3.4", kind: "learning", gloss: "practice-based learning in work settings: direct work, observation, shadowing, supervision and reflection" }
  - { component: "3.6", kind: "teaching", gloss: "scaffolded teaching from induction, with academics, researchers, practitioners and people with lived experience" }
  - { component: "3.7", kind: "teaching", gloss: "five learning themes carried by lectures, workshops, problem-based learning, simulation, role play and practice" }
  - { component: "3.8", kind: "assessment", gloss: "inclusive, accessible assessment with feedback and feed forward; judging readiness for practice" }
  - { component: "3.9", kind: "assessment", gloss: "a diverse range of methods and assessors, including people with lived experience" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.11 (requirement 4.9)", award: "bachelor's with honours", items: 38 }
  - { rung: "threshold", leadIn: "4.14 (requirement 4.13)", award: "integrated master's", items: 6 }
  - { rung: "threshold", leadIn: "4.17 (requirement 4.16)", award: "master's", items: 8 }
  - { rung: "typical", leadIn: "none", award: "bachelor's with honours", items: 0 }
  - { rung: "excellent", leadIn: "none", award: "bachelor's with honours", items: 0 }
rungBases: "4.7: threshold maps to a third, typical to a 2.2 or 2.1 and excellent to a first, by reference to Annex D (qaa/fheq-2024/annex-d/summary/*); 4.8: classes above threshold for integrated master's and merit and distinction for master's follow the provider's marking schemes. Threshold items total 52, by award as above"
outcomeLists: []
outcomes:
  - { outcome: "knowledge and understanding headline", threshold: "qaa/social-work-2026/4.11.ku", typical: "none", excellent: "none", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "demonstrable skills headline", threshold: "qaa/social-work-2026/4.11.ds", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "values and ethics", threshold: "qaa/social-work-2026/4.11.ve", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "regulator's requirements", threshold: "qaa/social-work-2026/4.11.psrb", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
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
- { body: "Social Care Wales", says: "the Welsh regulator (replacing the Care Council for Wales); approves courses, sets the qualifications framework and Code of Professional Practice, and registers students (D1, 1.4, 2.10, 2.11, 2.12)", requirements: "not yet ingested (Part E)" }
- { body: "Social Work England", says: "the regulator for England; approves courses against its Education and Training Standards and Professional Standards and registers graduates; post-qualifying Knowledge and Skills Statements and the supported first year (D1, 1.4, 2.13, 2.14, 2.15)", requirements: "not yet ingested (Part E)" }
- { body: "Northern Ireland Social Care Council", says: "the Northern Ireland regulator; with the Department of Health produced the framework specification; registers students and graduates, the latter subject to an Assessed Year in Employment; standards of conduct (D1, 1.4, 2.16 to 2.19)", requirements: "not yet ingested (Part E)" }
- { body: "Scottish Social Services Council (SSSC)", says: "the Scottish regulator; approves all qualifying courses, keeps registers, sets codes and regulates training; the honours or postgraduate route to qualify (D1, 1.4, 2.20, 2.21, 2.22)", requirements: "not yet ingested (Part E)" }
- { body: "Professional Standards Authority", says: "oversees Social Work England and eight other health and care regulators (D1, 2.14)", requirements: "not-applicable-by-design" }
- { body: "International Federation of Social Workers (IFSW)", says: "source of the global definition and principles framing the subject; supports the UN SDGs (D1, 1.1, 1.14, 1.26, 1.32, 2.1)", requirements: "not-applicable-by-design" }
- { body: "Equality and Human Rights Commission; Equality Commission for Northern Ireland", says: "equality reference points; providers writing competence standards should follow the EHRC guidance (D1, 1.13, 4.2)", requirements: "not-applicable-by-design" }
- { body: "Department of Health (Northern Ireland); Northern Ireland Assembly", says: "co-author of the framework specification; oversight of education and health and social care in Northern Ireland (D1, 2.17)", requirements: "not-applicable-by-design" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equity, equality, diversity and inclusion (EEDI)", carriedIn: ["front matter", "1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.47", "3.1", "3.9"], statements: ["qaa/social-work-2026/1.14", "qaa/social-work-2026/1.17", "qaa/social-work-2026/4.11.f", "qaa/social-work-2026/4.11.i", "qaa/social-work-2026/4.11.k", "qaa/social-work-2026/4.11.u"] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["front matter", "1.14", "1.17", "1.22", "1.23", "1.24", "1.25", "1.46", "2.32", "3.6", "3.8"], statements: ["qaa/social-work-2026/1.14", "qaa/social-work-2026/1.17", "qaa/social-work-2026/1.24"] }
  - { id: "theme:esd", named: "Education for sustainable development (ESD)", carriedIn: ["front matter", "1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.37", "2.32"], statements: ["qaa/social-work-2026/4.11.g", "qaa/social-work-2026/4.11.q"] }
  - { id: "theme:enterprise", named: "Employability, entrepreneurship and enterprise education (EEE)", carriedIn: ["front matter", "1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "1.41", "1.42", "1.43", "1.44"], statements: [] }
  - { id: "theme:generative-ai", named: "Generative artificial intelligence (GenAI)", carriedIn: ["front matter", "1.45", "1.46", "1.47", "1.48"], statements: ["qaa/social-work-2026/1.45", "qaa/social-work-2026/1.46", "qaa/social-work-2026/1.48", "qaa/social-work-2026/4.11.w"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.23", "2.28", "2.30", "4.5", "4.7", "4.15"] }
  - { framework: "scqf", levels: ["fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.23", "2.29", "2.30", "4.5", "4.7"] }
bodies:
  - { body: "Social Care Wales", citedIn: ["1.4", "2.10", "2.11", "2.12"] }
  - { body: "Social Work England", citedIn: ["1.4", "2.13", "2.14", "2.15"] }
  - { body: "Northern Ireland Social Care Council", citedIn: ["1.4", "2.16", "2.17", "2.18", "2.19"] }
  - { body: "Scottish Social Services Council", citedIn: ["1.4", "2.20", "2.21", "2.22"] }
  - { body: "Professional Standards Authority", citedIn: ["2.14"] }
  - { body: "International Federation of Social Workers", citedIn: ["1.1", "1.14", "1.26", "1.32", "2.1"] }
  - { body: "Equality and Human Rights Commission", citedIn: ["1.13", "4.2"] }
  - { body: "professional, statutory and regulatory bodies (PSRBs), named generically", citedIn: ["front matter", "4.2", "4.9", "4.11", "4.13", "4.14", "4.17"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.7"], role: "common descriptions of the four honours classes; the statement maps threshold, typical and excellent onto them" }
  - { document: "std:doc:qaa-fheq-2024-framework", named: "FHEQ (Level 6, Level 7); the Qualifications Frameworks", citedIn: ["2.23", "2.28", "2.30", "4.5", "4.15"], role: "levels of the awards" }
  - { document: "std:doc:qaa-fqheis-2024-framework", named: "SCQF/FQHEIS (Levels 9, 10, 11)", citedIn: ["2.23", "2.29", "2.30", "4.5", "4.7"], role: "Scottish levels of the awards" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA/Advance HE Guidance on ESD (2021)", citedIn: ["1.32"], role: "quoted on ESD as a lens" }
  - { document: "QAA Quality Code, 2024 update (not ingested)", named: "the Quality Code", citedIn: ["front matter"], role: "a further reference point" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "QAA Creating Inclusive Subject Learning Communities (not ingested)", named: "QAA's Creating Inclusive Subject Learning Communities", citedIn: ["1.17"], role: "further guidance on inclusion" }
  - { document: "QAA advice and resources on Generative AI (not ingested)", named: "QAA advice and resources on Generative AI", citedIn: ["1.46"], role: "further guidance on AI" }
  - { document: "Equality Act 2010 (law)", named: "The Equality Act 2010", citedIn: ["1.13", "1.22", "4.2"], role: "equality duties and competence standards" }
  - { document: "Welsh Language (Wales) Measure 2011 (law)", named: "The Welsh Language (Wales) Measure 2011", citedIn: ["1.22"], role: "Welsh language in education and social care" }
  - { document: "Special Educational Needs and Disability (Northern Ireland) Order 2005 (law)", named: "The Special Educational Needs and Disability (Northern Ireland) Order 2005", citedIn: ["1.22"], role: "the Northern Ireland access duty" }
  - { document: "UN Sustainable Development Goals (external)", named: "United Nation's Sustainable Development Goals (SDGs)", citedIn: ["1.29", "1.30", "1.32", "1.33"], role: "frame of the ESD theme" }
  - { document: "IFSW Global Definition of the Social Work Profession, 2014 (external)", named: "Global Definition of the Social Work Profession (IFSW 2014)", citedIn: ["1.1", "2.1"], role: "definition framing the subject" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "practice-social-work-education", definition: "learning in professional work-based settings (placement) and in other experiential settings, classroom activity included, sometimes supported by people with lived experience (D1, 1.10)", beneficiaryDefinition: "the part of your course where you learn by doing, on placement and in other hands-on settings", scopeNote: "the statement's own sense of 'practice'", category: "unknown", practices: ["education"] }
- { slug: "threshold-level-attainment", definition: "the minimum standard a student must show for the award, which the statement maps to a third (honours) or a pass (master's) (D1, 4.3, 4.7, 4.13, 4.16)", beneficiaryDefinition: "the minimum you must reach to gain your award", scopeNote: "typical maps to a 2.2 or 2.1 and excellent to a first (4.7); no lists for them", category: "unknown", practices: ["education"] }
- { slug: "intersectionality", definition: "the interconnected nature of social categories such as race or ethnicity, class and gender (D1, 1.15)", beneficiaryDefinition: "how different parts of who someone is combine to shape their experience", scopeNote: "used in 1.12, 1.15 and 4.11 i", category: "unknown", practices: ["social work", "education"] }
- { slug: "eedi", definition: "equity, equality, diversity and inclusion, covering a wide range of identity characteristics (D1, 1.12)", beneficiaryDefinition: "fairness, equal treatment, diversity and inclusion", scopeNote: "the statement's name for the EDI theme", category: "unknown", practices: ["education"] }
- { slug: "generations-of-rights", definition: "first generation civil and political rights; second socio-economic and cultural rights; third rights to the natural world, biodiversity and fairness between generations (D1, 1.26)", beneficiaryDefinition: "three kinds of human rights: freedoms, living standards and a healthy planet", scopeNote: "after the IFSW", category: "unknown", practices: ["social work"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "practice-social-work-education", form: "practice", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "practice-social-work-education", form: "placement", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "discipline-specific" }
- { concept: "threshold-level-attainment", form: "threshold level", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "intersectionality", form: "intersectionality", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "eedi", form: "equity, equality, diversity and inclusion (EEDI)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "generations-of-rights", form: "first, second and third generation rights", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
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
  title: "Subject Benchmark Statement Social Work"
  edition: "April 2026 (fifth edition)"
  year: 2026
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/social-work-2026/social-work-2026.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 3e0c995b05b7185fed01b86ff5553bfbe4ad905905db55f24ef359790d2182b5
  heldFiles: ["wkspc2601-library/txt/qaa-2026-social-work-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2026-social-work-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2026-social-work-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2026-social-work-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0097", source: "the regulators' requirement documents (Social Care Wales, Social Work England, NISCC, SSSC) named in 2.11 to 2.21 and section 5", why: "SB5 requirements, to ingest as standards documents of their own" }
- { w: "W-std-0098", source: "QAA Subject Benchmark Statement: Social Work, fourth edition (2019)", why: "S7 supersedes; a comparison of editions" }
```

## Part E Gaps and questions
- Rungs: one only. The statement gives threshold lists for three awards (honours 4.11, integrated master's 4.14, master's 4.17) and no typical or excellent lists; 4.7 maps threshold to a third, typical to a 2.2 or 2.1 and excellent to a first through Annex D. SB4 records typical and excellent as stated by name only (items 0). Pattern differs from Psychology (three listed rungs) and matches the threshold-only shape (Archaeology).
- Skeleton correction: 4.11 was one candidate (4.11.b1) holding the whole list; it is cut here by the issuer's letters a) to hh) as 4.11.a to 4.11.hh (34 records), plus four category headlines 4.11.ku (knowledge and understanding), 4.11.ds (demonstrable skills), 4.11.ve (values and ethics) and 4.11.psrb (PSRB requirements). The letter ids keep the issuer's numbering, which 4.14 and 4.17 cite ("4.11 a-m", "4.11 n-hh"). The builder's heading path is empty for the letter ids a to z (it reads only numeric parts); cosmetic, for P3.
- Skeleton correction: 4.3.b1 to 4.3.b3 (marked threshold) are the three awards the standards cover, not outcomes; not recorded as statements. 4.3 is a lead-in to section 4 (S3 gloss).
- Skeleton correction: 4.14 and 4.17 were single paragraphs with no candidates; cut into 6 and 8 records by category and sentence, each with `find`. The references "(paragraph 4.11 a-m)" and "(paragraph 4.11 n-hh)" are kept inside the headline spans as cross-references and never made statements (DPN-1); in 4.17 "(paragraph" is split across a page break in the held text.
- Pattern: master's standards are separate paragraphs for two further awards (integrated master's, postgraduate master's), recorded as rung threshold with award and level fheq:7 by the convention; the `.masters` id suffix is not used because the paragraph number already separates the award. The master's statements are stronger headlines over the same lettered outcomes, not new lists. 4.12 says integrated master's degrees must meet both the undergraduate and the master's standards, so 4.11 a to hh also hold for them (not duplicated as records).
- Pattern: the honours threshold is a lead-in ("graduates will have demonstrated the following") followed by four category headings, two of them with lettered lists run inline (a) to hh)) rather than bullets. Force is `threshold` from 4.3 and 4.9 (minimum standards; "must demonstrate at least a threshold-level"), with forceFrom the lead-in paragraph.
- Pattern: a fourth category of threshold outcome, "PSRB requirements", recorded as a rung item (4.11.psrb, 4.14.psrb, 4.17.psrb); the number of practice days is left to the regulator (4.10, 4.13, 4.16).
- No gradeOf links: a single rung, and the master's headlines are other awards, not a rung below. SB4 `outcomes` lists only the four honours category headlines.
- Verbs empty: the knowledge items a), b), e), f), g), j), k) and the category headlines are noun phrases with no action verb in the span; `verbs: []`.
- Obliging words outside the five, recorded as describes for Abbott: "duty" (1.14), "legal duty" (1.17), "expected to" (1.24, 2.34, 2.35 second sentence), "need to" (1.46, 2.8), "it is expected" (1.48, 3.1, 3.6), "there is an expectation" (3.4). Recorded as must where the meaning is plain: "required" (2.17, 2.18, 4.12), "core requirement" (2.4).
- Not recorded as statements (descriptive, legal fact or plain-present provider norms, template open point 5): 1.4 ("illegal" to use the title unless registered; legal fact), 1.9 ("graduates possess"), 1.15 ("course providers are committed"; "will be useful to include"), 1.19 ("course providers make explicit and embed"), 1.22 (statute places a duty), 1.23 ("legal obligation", "responsibility"), 1.25 and 1.38 (lists of what courses do), 1.27 ("courses develop graduates"), 1.44 ("required professional knowledge", an aim), 2.30, 2.38 ("will form part" of review), 2.40 (external examiners "will be asked"), 4.4 and 4.6 (predictions with "will").
- Codes: HECoS 100503 social work and CAH15-04-01 social work, both stated by the subject name. Related codes not added: probation/after-care 100662 (probation officers named as a role in 2.18, not a subject), youth and community work 100466, community work 100655.
- Frameworks: the CQFW is not named; Wales is placed at FHEQ Level 6 (2.28). 3.1 refers to "the relevant national qualifications frameworks" without naming one; not counted in SB6. FHEQ and SCQF/FQHEIS levels match the ingested frameworks (std:doc:qaa-fheq-2024-framework S5; std:doc:qaa-fqheis-2024-framework S5); the SCQF Level 9 ordinary degree and Scottish MA (2.29) are cited but not covered by the standards.
- Annex D: 4.7 cites Annex D for honours and also, as worded, "postgraduate awards at Level 6 (SCQF Level 10 in Scotland)"; recorded as cited. The master's classes (merit, distinction) are left to providers' schemes (4.8).
- Bodies: BASW and the regulators' documents appear only in section 5 (excluded) and are not counted in SB6 bodies; BASW's Shades of Bias is named in 1.21 as an example tool (not a body citation). The 2016 group listed the HCPC and the Care Council for Wales (section 6, excluded).
- Theme naming: the statement names five cross-cutting themes in its front matter and section 1 headings, the fifth being generative AI (theme:generative-ai, convention). Its EDI theme is named EEDI, with equity added.
- Integrated master's headline 4.14.inquiry and master's 4.17.inquiry sit under the knowledge and understanding heading in the issuer's layout but are recorded with domain subject-skill (an inquiry project); for P3.
- S9 commentary not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:42: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0130 (P1); built by tools/bm_build.py.
