---
id: std:doc:qaa-osteopathy-2024-benchmarks
title: "Subject Benchmark Statement Osteopathy"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100243", label: "osteopathy", basis: "stated" }
  - { scheme: "cah", code: "CAH02-06-06", label: "complementary and alternative medicine", basis: "inferred" }
  - { scheme: "cah", code: "CAH02-06", label: "allied health", basis: "inferred" }
  - { scheme: "cah", code: "CAH02", label: "subjects allied to medicine", basis: "inferred" }
edition: "April 2024 (fifth edition)"
published: 2024-04
status: current
supersedes: "the previous Osteopathy statement (not named in the text; the text dates the third edition 2019, the second 2014 and the original 2007: Part E)"
heldText: { method: sha256-bytes, raw: dc11b8bca50a250cf49ea4d936ebb9b0ad011096993b0f82a0f107ee823dd3fb, normalised: 08d3b0d44df2d901baf390976d9e4636764cbccb8d29f5ec6a0d1e36fc849b35 }
heldTextStan: { method: sha256-stan, raw: dc11b8bca50a250cf49ea4d936ebb9b0ad011096993b0f82a0f107ee823dd3fb, normalised: ab7e626c076b967f41871829e38282122d5fadd5b5c8a1a5b3c5f3d700f7a6fc }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, revision with cross-cutting themes (fifth edition of this statement, April 2024)"
awardsCovered: ["bachelor's with honours", "integrated master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0123 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:11"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Osteopathy (QAA, April 2024)

> Run 0123, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2024-osteopathy-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate of a pre-registration osteopathy course should know, understand and be able to do: a short profile of the graduate (3.4), 83 detailed outcomes in fourteen lettered groups (3.6) and a single threshold list for the honours award (6.10), with typical and higher achievement left to each provider and Annex D. Reach for it when designing, reviewing or describing an osteopathy course, its outcomes or its assessment. It is not the regulator's standard: registration rests on the General Osteopathic Council's Osteopathic Practice Standards and its Recognised Qualification process, which the statement reports but does not hold.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2024 as the fifth edition, the statement covers osteopathy as a primary healthcare profession regulated by the General Osteopathic Council. It sets out the context and purposes of the degree, education and training and the awarding level (bachelor's with honours at FHEQ level 6 and integrated master's at level 7; SCQF level 11 named), a broad curriculum and 83 graduate outcomes in fourteen groups, teaching and learning, assessment against the Osteopathic Practice Standards and benchmark standards stated at the threshold only (13 items), with achievement above it referred to Annex D. It carries the four cross-cutting themes (equality, diversity and inclusion; accessibility; education for sustainable development; enterprise and entrepreneurship), names the regulator, the Professional Standards Authority, the Privy Council, NCOR, NICE and CEN, and cites the FHEQ, the FQHEIS and the Quality Code.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Osteopathy"
edition: "April 2024 (fifth edition)"
dates:
  published: 2024-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of current quality arrangements in Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2024", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate of a pre-registration osteopathy course is expected to know, understand and be able to do, and the threshold standards for the honours award"
appliesTo:
  awards: ["bachelor's with honours", "integrated master's", "pre-registration master's (named at 2.8)"]
  levels: ["fheq:6", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This document is a QAA Subject Benchmark Statement for Osteopathy that defines what can be expected of a graduate in the subject\" (D1, front matter); \"pre-registration osteopathic courses currently satisfy bachelor's ( Level 6) and integrated master's (Level 7) degree levels\" (D1, 6.9)"
statedSubjects:
  - { name: "Osteopathy", locator: "(D1, front matter; 1.1; 6.10)", kind: "subject", codes: [{ scheme: "hecos", code: "100243", label: "osteopathy" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "osteopaths as primary healthcare practitioners; an Allied Health Profession in England" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "the range of management strategies osteopaths use" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "settings of practice and the scope of a first consultation; referral" }
  - { number: "1.4", order: 6, componentType: stem, parent: "section 1", heading: "Context", gloss: "clinical training in institutional clinics; the kinds of institution that teach the subject" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Osteopathy degree", gloss: "regulation by the GOsC; Recognised Qualifications must deliver the OPS" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Osteopathy degree", gloss: "preparing students for autonomous practice from graduation" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Osteopathy degree", gloss: "employment patterns: self-employed, salaried, NHS and other roles" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Osteopathy degree", gloss: "osteopathy in independent clinical guidance, notably on back pain" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Osteopathy degree", gloss: "NCOR and the osteopathic evidence base" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Osteopathy degree", gloss: "osteopathy as a global profession; the CEN standard" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Osteopathic practice", gloss: "what osteopathic practice blends: knowledge, skills and principles" }
  - { number: "1.12", order: 14, componentType: stem, parent: "section 1", heading: "Osteopathic practice", gloss: "seven features that characterise osteopathic practice" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "a collective responsibility for equity and inclusion beyond legal minimums" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "an inclusive learning community that counters systemic disadvantage" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "critical interrogation of dominant thought; equity as a right" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "core values to run through the whole curriculum" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "critical theory across the curriculum; anticipatory design" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "anticipatory design and caring for self and others" }
  - { number: "1.19", order: 21, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "questions to test how a course takes account of EDI" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "how students first meet osteopathy; widening access" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "part-time and full-time modes and parity of experience" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "accessibility across all modes of teaching, learning and assessment" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development (ESD)", gloss: "whole-person training and critical study of the profession for sustainability" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development (ESD)", gloss: "the eight UNESCO sustainability competencies in the learning environment" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development (ESD)", gloss: "contextualising learning; personal and social responsibility as an aim" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "growing demand for osteopathy across sectors" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "graduates articulating the value of their skills; enterprising self-awareness" }
  - { number: "1.28", order: 30, componentType: stem, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "what an entrepreneurial mindset involves" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "EEE and its part in an ethical career" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprising behaviours" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprising attributes" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "competencies for employed or self-employed practice" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "digital competency used creatively and accessibly" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "employability and enterprise in curriculum design" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "external speakers and alumni recommended" }
  - { number: "1.36", order: 38, componentType: practice, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "assignments that build business and evaluative skill" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "initiatives with placement providers, employers and stakeholders" }
  - { number: "1.38", order: 40, componentType: practice, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "supervised clinic practice as a bridge to an entrepreneurial mindset" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "career pathways and the can-do confidence EEE builds" }
  - { number: "2.1", order: 43, componentType: paragraph, parent: "section 2", heading: "Education and training", gloss: "a common approach to the regulator's capabilities" }
  - { number: "2.2", order: 44, componentType: practice, parent: "section 2", heading: "Education and training", gloss: "evidence-based pedagogy; feed-forward feedback and self-assessment" }
  - { number: "2.3", order: 45, componentType: paragraph, parent: "section 2", heading: "Education and training", gloss: "progressive levels, clinical reasoning, supervised experience and autonomy in learning" }
  - { number: "2.4", order: 46, componentType: practice, parent: "section 2", heading: "Education and training", gloss: "technical skill integrated with closely supervised clinical work" }
  - { number: "2.5", order: 47, componentType: paragraph, parent: "section 2", heading: "Education and training", gloss: "core sciences, communication and patient-centred teaching" }
  - { number: "2.6", order: 48, componentType: paragraph, parent: "section 2", heading: "Education and training", gloss: "clinical reasoning frameworks for critical awareness" }
  - { number: "2.7", order: 49, componentType: paragraph, parent: "section 2", heading: "Awarding level", gloss: "training reflects the degree-level descriptors of the FHEQ and FQHEIS" }
  - { number: "2.8", order: 50, componentType: paragraph, parent: "section 2", heading: "Awarding level", gloss: "awarding levels and course lengths" }
  - { number: "3.1", order: 52, componentType: area, parent: "section 3", heading: "Knowledge, understanding and skills", gloss: "the broad curriculum of an osteopathy degree" }
  - { number: "3.2", order: 53, componentType: paragraph, parent: "section 3", heading: "Knowledge, understanding and skills", gloss: "the OPS combined with the curriculum to prepare graduates" }
  - { number: "3.3", order: 54, componentType: paragraph, parent: "section 3", heading: "Knowledge, understanding and skills", gloss: "integrating knowledge and skills for safe practice and learner autonomy" }
  - { number: "3.4", order: 55, componentType: stem, parent: "section 3", heading: "The key characteristics of graduates in Osteopathy", gloss: "six key characteristics of the osteopathy graduate" }
  - { number: "3.5", order: 56, componentType: paragraph, parent: "section 3", heading: "The key characteristics of graduates in Osteopathy", gloss: "competent students graduate as safe, rounded practitioners" }
  - { number: "3.6", order: 57, componentType: stem, parent: "section 3", heading: "The key characteristics of graduates in Osteopathy", gloss: "the detailed graduate outcomes in fourteen lettered groups" }
  - { number: "4.1", order: 59, componentType: paragraph, parent: "section 4", heading: "Teaching and learning", gloss: "teaching and learning towards GO-SET and the OPS themes" }
  - { number: "4.2", order: 60, componentType: paragraph, parent: "section 4", heading: "Teaching and learning", gloss: "progressive, critical and reflective learning; skills students gain" }
  - { number: "4.3", order: 61, componentType: practice, parent: "section 4", heading: "Teaching and learning", gloss: "evolving, innovative and research-informed teaching" }
  - { number: "4.4", order: 62, componentType: practice, parent: "section 4", heading: "Teaching and learning", gloss: "supervised clinical learning across diverse patient groups" }
  - { number: "5.1", order: 64, componentType: paragraph, parent: "section 5", heading: "Assessment", gloss: "assessment towards meeting the OPS; the condition to graduate" }
  - { number: "5.2", order: 65, componentType: paragraph, parent: "section 5", heading: "Assessment", gloss: "authentic assessment shaped by practitioners and patients" }
  - { number: "5.3", order: 66, componentType: paragraph, parent: "section 5", heading: "Assessment", gloss: "varied, valid and reliable assessment tools" }
  - { number: "5.4", order: 67, componentType: paragraph, parent: "section 5", heading: "Assessment", gloss: "assessment that tracks growing complexity towards autonomy" }
  - { number: "6.1", order: 69, componentType: paragraph, parent: "section 6", heading: "Introduction", gloss: "the standards are the minimum threshold for the honours award" }
  - { number: "6.2", order: 70, componentType: paragraph, parent: "section 6", heading: "Introduction", gloss: "most students exceed the threshold; Annex D for higher achievement" }
  - { number: "6.3", order: 71, componentType: paragraph, parent: "section 6", heading: "Introduction", gloss: "osteopathy's holistic, person-centred approach" }
  - { number: "6.4", order: 72, componentType: paragraph, parent: "section 6", heading: "Introduction", gloss: "pre-registration courses with supervised clinical practice and the OPS themes" }
  - { number: "6.5", order: 73, componentType: area, parent: "section 6", heading: "Introduction", gloss: "the scientific and clinical foundation of training" }
  - { number: "6.6", order: 74, componentType: paragraph, parent: "section 6", heading: "Introduction", gloss: "evidence-informed practice and research skills" }
  - { number: "6.7", order: 75, componentType: paragraph, parent: "section 6", heading: "Introduction", gloss: "reflective practice and CPD after graduation" }
  - { number: "6.8", order: 76, componentType: paragraph, parent: "section 6", heading: "Introduction", gloss: "Recognised Qualification approval and the OPS" }
  - { number: "6.9", order: 77, componentType: paragraph, parent: "section 6", heading: "Introduction", gloss: "the capabilities map to framework levels 6 and 7 and SCQF 11" }
  - { number: "6.10", order: 78, componentType: stem, parent: "section 6", heading: "Standards", gloss: "the thirteen threshold standards for the honours award" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of an Osteopathy degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Education and training", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Knowledge, understanding and skills", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Teaching and learning", gloss: "section 4" }
  - { number: "5", componentType: section, parent: none, heading: "Assessment", gloss: "section 5" }
  - { number: "6", componentType: section, parent: none, heading: "Benchmark Standards", gloss: "section 6" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "section headings", heading: "the six numbered section heading lines", kind: "other: headings, recorded in SECTIONS" }
  - { number: "7", heading: "List of references and further resources", kind: "other: back matter, references" }
  - { number: "8", heading: "Membership of the Advisory Group", kind: "other: back matter, membership; read for S8" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 129 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/osteopathy-2024/1.5
  locator: { number: "1.5", headingPath: ["Context and purposes of an Osteopathy degree", "Purposes and characteristics of an Osteopathy degree"] }
  span: { start: 9624, end: 10536 }
  source: "1.5 Osteopathic students follow an extended degree course, combining academic and hands-on clinical work. The General Osteopathic Council (GOsC) regulates the practice of osteopathy in the UK. By law (the Osteopaths Act 1993), only those registered with the GOsC are entitled to call themselves osteopaths and practise osteopathy in the UK. A student wishing to study in the UK to become an osteopath must gain a qualification recognised by the GOsC and approved by the Privy Council. All Recognised Qualifications (RQs) must deliver the GOsC's Osteopathic Practice Standards (OPS) . RQs should also align with the GOsC's guidance, including the Graduate Outcomes and Standards for Education and Training which sets out the outcomes that will help graduates to demonstrate that they meet the OPS. The Professional Standards Authority oversees the GOsC as well as nine other health professional regulatory bodies."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "anyone seeking to practise as an osteopath in the UK"
  addressee: learner
  verbs: ["regulates", "gain", "deliver", "align"]
  about: "registration, Recognised Qualifications and the OPS"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Osteopathy courses are extended and mix academic with hands-on clinical work; the General Osteopathic Council regulates the profession and by law only its registrants may use the title or practise; anyone who trains here as an osteopath must gain a qualification the regulator recognises and the Privy Council approves; every Recognised Qualification must deliver the Osteopathic Practice Standards and should align with the regulator's guidance on graduate outcomes; the Professional Standards Authority oversees the regulator."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/1.6
  locator: { number: "1.6", headingPath: ["Context and purposes of an Osteopathy degree", "Purposes and characteristics of an Osteopathy degree"] }
  span: { start: 10537, end: 11059 }
  source: "1.6 Once qualified and registered with GOsC, osteopaths can practise independently. Thus, it is critical that throughout pre-registration education osteopaths are prepared for autonomous practice at the point of graduation. This requires them to develop both the skills\n\n4\nand criticality to integrate into the osteopathic and wider health community to provide effective patient care, and the reflexivity, insight and ability to keep themselves up to date with evidence (including clinical guidelines) and fit to practise."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "students on pre-registration courses"
  addressee: learner
  verbs: ["prepared", "requires", "develop"]
  about: "readiness for autonomous practice at graduation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Once qualified and registered, osteopaths may practise on their own, so pre-registration education must ready them for autonomous practice by graduation; this requires them to develop the skills and criticality to join the osteopathic and wider health community and care well for patients, and the reflexivity and insight to keep abreast of evidence and stay fit to practise."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/1.12.b1
  locator: { number: "1.12.b1", headingPath: ["Context and purposes of an Osteopathy degree", "Osteopathic practice"] }
  span: { start: 13253, end: 13514 }
  source: "Emphasis is on the person and not on their condition. This has been a longstanding tenet for osteopathy and should inform the osteopathic approach to care. It involves viewing the person as having an integrated blend of influences that combine to affect health."
  stem: "1.12"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "osteopathic practice and its teaching"
  addressee: both
  verbs: ["inform", "involves", "viewing"]
  about: "care centred on the person, not the condition"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Focusing on the person rather than the condition is a long-held principle of osteopathy and should shape the osteopathic approach to care; it means seeing the person as a combined mix of influences that together affect health."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of an Osteopathy degree", "Equality, diversity and inclusion"] }
  span: { start: 15414, end: 16562 }
  source: "1.13 Osteopathy, as an inclusive learning community, has a collective responsibility to embed equity, equality, diversity and inclusion within all institutions, processes, curricula, and pedagogies. This responsibility to go beyond the minimum expectations of equality ensures an equitable community that recognises learners’ difference in prior experience and opportunity and can help to remedy systemic disadvantages in the subject, for example: through widening participation agendas to ensure economic disadvantage does not hinder a student's access, experience or outcome; countering the underrepresentation of marginalised groups inclusive of, and beyond, those with protected characteristics as defined by the Equality Act 2010 ; adopting a zero-tolerance approach to discrimination and harassment, including everyday microaggressions; ensuring access for neurodiverse community members; and closing structural awarding gaps. All participants in the community will need to engage, reflect and change to uphold this responsibility and duty, which will impact education, student participation, population health, and patient care perspectives."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "everyone in the osteopathic learning community"
  addressee: both
  verbs: ["embed", "engage", "reflect", "change", "uphold"]
  about: "shared responsibility for equity and inclusion"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The osteopathic learning community holds a shared responsibility, going past the legal minimum, to build equity, equality, diversity and inclusion into institutions, processes, curricula and teaching, for example by widening participation, countering under-representation, refusing all discrimination and harassment, securing access for neurodiverse members and closing awarding gaps; everyone in it will need to engage, reflect and change to meet this duty."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/1.14
  locator: { number: "1.14", headingPath: ["Context and purposes of an Osteopathy degree", "Equality, diversity and inclusion"] }
  span: { start: 16563, end: 17530 }
  source: "1.14 All involved in osteopathy should foster an inclusive learning community encompassing a range of participants, such as students, academics, professional staff, patients, visitors and external partners to counter systemic disadvantage. Equity , diversity and inclusion require a strong commitment and concerted action to build an inclusive environment where opportunities are open to all and where everybody can reach their full potential without fear of harassment, prejudice or discrimination. Contemporary legacies of systemic disadvantage, for example, racism, classism, ablism, homophobia and patriarchy, must therefore be acknowledged and countered by fostering an inclusive learning community encompassing a range of participants, such as students, academics, professional staff, patients, visitors and external partners. This could include, for example, the provision of diverse osteopathic educational methods to address the challenges of EDI and access."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "everyone involved in osteopathy and its learning community"
  addressee: both
  verbs: ["foster", "require", "build", "acknowledged", "countered"]
  about: "an inclusive community that counters systemic disadvantage"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Everyone in osteopathy should build an inclusive learning community of students, staff, patients, visitors and partners that works against systemic disadvantage; inclusion needs strong commitment and joint action so that all can reach their potential free of harassment, prejudice or discrimination; present-day legacies such as racism, classism, ableism, homophobia and patriarchy must be acknowledged and countered, for instance through varied teaching methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/1.15
  locator: { number: "1.15", headingPath: ["Context and purposes of an Osteopathy degree", "Equality, diversity and inclusion"] }
  span: { start: 17531, end: 18097 }
  source: "1.15 Osteopathic undergraduate and postgraduate studies should continually critically interrogate the language, perceptions, and entrenchment of dominant systems of thought, within concepts of knowledge and power. Recognition and commitment to agency, equal rights and inherent dignity of all humans form the foundation of social justice. Equity is positioned as an ethical consideration of each person’s multiple identities and experiences and a fundamental human right in relation to supporting and advocating for anti-oppressive knowledge generation and practice."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "undergraduate and postgraduate osteopathic study"
  addressee: provider
  verbs: ["interrogate"]
  about: "critical interrogation of dominant thought"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Osteopathic study at every level should keep questioning critically the language, perceptions and entrenched dominant systems of thought within ideas of knowledge and power; social justice rests on agency, equal rights and human dignity, and equity is treated as an ethical matter and a basic right that supports anti-oppressive knowledge and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/osteopathy-2024/1.16
  locator: { number: "1.16", headingPath: ["Context and purposes of an Osteopathy degree", "Equality, diversity and inclusion"] }
  span: { start: 18101, end: 19045 }
  source: "1.16 The following core values underpin osteopathy’s inclusive learning community: an ethics of care towards patients, students, educational faculty and members of the public embracing and valuing plurality of knowledges and experiences; respect for a range of perspectives and lifestyles; attentiveness to the opportunities and challenges raised by decolonial imperatives; and solidarity in recognising and addressing injustice. These values should be integrated throughout the curriculum and not be siloed within individual modules and/or sub-disciplines. This will enhance the contribution that studying osteopathy can make to realising transformative justice across education and healthcare, and supporting osteopathic students to engage with health inequalities, social determinants, and varied patient populations (Office for Health Improvement and Disparities 2022; Bambra et al. 2023; NIHR 2021; Versus Arthtritis 2019; Rashbrook 2019)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the osteopathy curriculum"
  addressee: provider
  verbs: ["underpin", "integrated", "siloed"]
  about: "core values across the curriculum"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "An ethics of care, valuing plural knowledges and experiences, respect for different perspectives and lifestyles, attention to decolonial imperatives and solidarity against injustice underpin the inclusive community; these values should run through the whole curriculum rather than sit in single modules, helping students engage with health inequalities and varied patient groups."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/osteopathy-2024/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of an Osteopathy degree", "Equality, diversity and inclusion"] }
  span: { start: 19046, end: 19920 }
  source: "1.17 The core values underpinning osteopathy’s inclusive learning community aligns with, and encourages, curricula design principles that stimulate critical thinking informed by a variety of progressive theoretical perspectives and educational research. These include, but are not limited to, theoretical perspectives from critical theory, critical race theory, decoloniality, disability studies, feminist, queer, and science and technology studies. The application of critical theory is relevant to, and should be applied across, the osteopathic discipline and curricula content. The core values also promote anticipatory design and practices, which are considerate of the particularities associated with sites of learning, for example, online, face-to-face, in technique class, in the clinic, paying close attention to those that may have historically been less inclusive."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the osteopathy curriculum and its design"
  addressee: provider
  verbs: ["stimulate", "applied", "promote"]
  about: "critical theory and anticipatory design"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The core values support curriculum design that encourages critical thinking drawn from progressive theories and educational research, drawing on critical and critical race theory, decolonial thought, disability, feminist and queer studies and the study of science and technology; critical theory should be applied across the discipline and its content, and the values also favour anticipatory design suited to each site of learning, with care for those that have been less inclusive."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/osteopathy-2024/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of an Osteopathy degree", "Equality, diversity and inclusion"] }
  span: { start: 19921, end: 20650 }
  source: "1.18 Effective anticipatory design and practice in osteopathy acknowledges the importance of providing a supportive cultural and institutional context for teaching, learning and research, within which participants are encouraged to embrace intellectual, methodological, and practical challenges. Effective anticipatory design and practice also enhance the individual and collective capability to work with the discomfort associated with encountering alternative perspectives, learning new knowledge, and gaining new skills. This requires osteopathy’s inclusive learning community to develop and promote techniques to care for the self and others, as part of a sustained consideration for emotional, mental and physical wellbeing."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "osteopathy's inclusive learning community"
  addressee: both
  verbs: ["acknowledges", "requires", "develop", "promote"]
  about: "anticipatory design and care for self and others"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Effective anticipatory design gives a supportive cultural and institutional setting for teaching, learning and research in which people are encouraged to take on challenges, and builds the capacity to work with the discomfort of new perspectives, knowledge and skills; this requires the learning community to develop and promote ways of caring for self and others, with sustained attention to emotional, mental and physical wellbeing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of an Osteopathy degree", "Accessibility"] }
  span: { start: 22133, end: 23545 }
  source: "1.22 The combined use of digital/virtual, face-to-face, synchronous, or asynchronous teaching and learning can provide opportunities for knowledge sharing and skills acquisition that are fair and accessible to all. Students' engagement with face-to-face or online learning environments and teaching activities (including assessment) will not always be equal or consistent due to several factors. For example, students may have personal commitments, such as caring responsibilities, that prevent them from attending scheduled lectures. Alternatively, they may need to make reasonable adjustments to ensure that they can access and engage with learning materials, for example if they have specific disabilities, special educational needs or limited access to digital resources or bandwidth due to geographical or economic conditions. Wherever possible, all modes of teaching, learning and assessment will be underpinned by a concern for accessibility, which can be achieved in a variety of ways. These include captioning of recorded lectures, recording of synchronous content, accessible design of virtual learning environments; it is for subject specialists to determine the most appropriate means of promoting fair and equitable access to learning and removing barriers to success. Supportive measures have to be enacted without compromising the regulatory framework that supports patient safety and well- being."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "all modes of teaching, learning and assessment"
  addressee: provider
  verbs: ["underpinned", "achieved", "determine", "enacted"]
  about: "accessibility in every mode of teaching, learning and assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Blended digital and face-to-face, live and recorded teaching can make learning fair and accessible, though students' engagement varies with caring duties, disabilities, special educational needs or poor digital access; wherever possible all teaching, learning and assessment will rest on a concern for accessibility, such as captions, recordings and accessible virtual environments, with subject specialists choosing the means; supportive measures have to be put in place without weakening the regulation that keeps patients safe."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/osteopathy-2024/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of an Osteopathy degree", "Education for Sustainable Development (ESD)"] }
  span: { start: 24456, end: 25048 }
  source: "1.24 All eight of the UNESCO sustainability competencies (systems thinking; anticipatory; normative; strategic; collaboration; critical thinking; self-awareness; integrated problem- solving) are considered essential for the sustainability of osteopathy. The qualified osteopath within their professional and working context requires the practical operation of all the competencies in the delivery of their professional services. The learning environment for osteopathy therefore requires these competencies to be manifested and exemplified within the learning facilities and course curricula."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the osteopathic learning environment"
  addressee: provider
  verbs: ["considered", "requires", "manifested", "exemplified"]
  about: "UNESCO sustainability competencies in the learning environment"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "All eight UNESCO sustainability competencies are held essential to the sustainability of osteopathy; qualified osteopaths need to use them all in practice, so the osteopathic learning environment requires them to be shown and modelled in learning facilities and curricula."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/osteopathy-2024/1.25
  locator: { number: "1.25", headingPath: ["Context and purposes of an Osteopathy degree", "Education for Sustainable Development (ESD)"] }
  span: { start: 25049, end: 25580 }
  source: "1.25 To develop learning environments that promote sustainable development, undergraduate osteopathic training aims to contextualise theoretical learning and professional provision at a practice level within the social, economic and political arena, and promote the employability of their graduates. Engendering personal and social responsibility for the well-being of others and themselves should be a developmental aim. More\n\n8\ninformation on education for sustainable development can be found in the QAA and Advance HE guidance."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "undergraduate osteopathic training"
  addressee: both
  verbs: ["contextualise", "promote", "engendering"]
  about: "personal and social responsibility as a developmental aim"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "To build learning environments that advance sustainable development, undergraduate training aims to set theory and professional provision in their social, economic and political context and to promote graduates' employability; growing a sense of responsibility, personal and social, for one's own and others' well-being should be a developmental aim, and guidance from QAA and Advance HE gives more on education for sustainable development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/1.27
  locator: { number: "1.27", headingPath: ["Context and purposes of an Osteopathy degree", "Enterprise and entrepreneurship education"] }
  span: { start: 25888, end: 26648 }
  source: "1.27 Osteopathy graduates can collect, analyse and manipulate a range of quantitative and qualitative data and should understand the commercial as well as practical value of their skillsets and be able to articulate and demonstrate them to potential employers and in plans for self-employment, private practice or further study. They should also be encouraged to develop self-awareness of their own enterprising and entrepreneurial capabilities in osteopathy, as well as the motivation and self-discipline to apply these flexibly in different ways and in changing contexts. This might include recognising themselves as being creative or resourceful; translating ideas into actions; prepared to challenge assumptions through critical investigation and research."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "osteopathy graduates"
  addressee: learner
  verbs: ["collect", "analyse", "manipulate", "understand", "articulate", "demonstrate", "encouraged", "develop", "apply"]
  about: "enterprising skills and their value"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Osteopathy graduates can collect, analyse and handle varied data and should understand the commercial and practical worth of their skills and be able to explain and show them to employers and when planning self-employment, private practice or more study; they should also be encouraged to become aware of their own enterprising capabilities and to apply them flexibly as contexts change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/1.33
  locator: { number: "1.33", headingPath: ["Context and purposes of an Osteopathy degree", "Enterprise and entrepreneurship education"] }
  span: { start: 29245, end: 29451 }
  source: "1.33 Developing digital competency and transferable skills should include using digital technology to communicate ideas creatively, innovatively and accessibly to enhance academic success and employability."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students developing digital and transferable skills"
  addressee: both
  verbs: ["include", "using", "communicate", "enhance"]
  about: "digital competency used creatively and accessibly"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Building digital competence and transferable skills should take in the use of digital technology to share ideas creatively, innovatively and accessibly, to support academic success and employability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/1.34
  locator: { number: "1.34", headingPath: ["Context and purposes of an Osteopathy degree", "Enterprise and entrepreneurship education"] }
  span: { start: 29452, end: 29852 }
  source: "1.34 The development of such professional knowledge, skills and competencies in osteopathy should be a key aspect of curriculum design and might be achieved across the duration of a training programme. Learning outcomes, teaching, and learning activities and authentic assessment for employability, enterprise and entrepreneurship may be explicit within dedicated modules and embedded across modules."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "curriculum design"
  addressee: provider
  verbs: ["achieved", "embedded"]
  about: "employability and enterprise in curriculum design"
  themes: [theme:enterprise]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Developing these professional knowledge, skills and competencies should be a central part of curriculum design and can be spread across the training; outcomes, teaching and authentic assessment for employability and enterprise may sit in dedicated modules and be embedded across others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/osteopathy-2024/1.35
  locator: { number: "1.35", headingPath: ["Context and purposes of an Osteopathy degree", "Enterprise and entrepreneurship education"] }
  span: { start: 29853, end: 30232 }
  source: "1.35 The engagement of external speakers or representation from the profession and alumni to enrich teaching and offer first-hand experience is recommended. Exposure to a variety of osteopaths will develop awareness of the working context and could enhance the competencies of graduates to deal with market forces and promote themselves ethically as an osteopath upon graduation."
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "teaching on osteopathy courses"
  addressee: provider
  verbs: ["recommended", "enrich", "offer"]
  about: "external speakers and alumni in teaching"
  themes: [theme:enterprise]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Bringing in external speakers, members of the profession and alumni to enrich teaching and share first-hand experience is recommended; meeting a range of osteopaths builds awareness of the working context and can strengthen graduates' ability to handle market forces and promote themselves ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/osteopathy-2024/2.3
  locator: { number: "2.3", headingPath: ["Education and training", ""] }
  span: { start: 32875, end: 33683 }
  source: "2.3 This approach combines academic and theoretical learning framed around progressive levels aligned to the UK Quality Code for Higher Education (Quality Code ), including procedural, propositional and psychomotor knowledge centred in an osteopathic clinical framework. The applied practical and clinical reasoning skills should robustly support osteopathic clinical decision-making and safe, effective practice ensuring continuing student fitness to practise. Furthermore, supervised clinical experience is essential to the development of osteopathic skills. Autonomy in learning is also required to enable and ensure lifelong learning and reflective practice. Knowledge of the healthcare environment in the UK, business and regulatory requirements are sufficient to enable graduates to work independently."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "osteopathy courses and their students"
  addressee: both
  verbs: ["support", "ensuring", "required", "enable"]
  about: "clinical reasoning, supervised experience and autonomy in learning"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Academic and theoretical learning progresses through levels in line with the Quality Code and spans procedural, propositional and psychomotor knowledge within a clinical framework; practical and clinical reasoning skills should firmly support clinical decisions and safe, effective practice that keeps students fit to practise; supervised clinical experience is essential and autonomy in learning is required for lifelong learning and reflection; enough knowledge of UK healthcare, business and regulation lets graduates work independently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/2.5
  locator: { number: "2.5", headingPath: ["Education and training", ""] }
  span: { start: 34146, end: 34651 }
  source: "2.5 As befits a primary healthcare profession, it is important that osteopathic students graduate with comprehensive knowledge and demonstrate understanding of anatomy, physiology and pathology, as well as acquiring excellent communication and interpersonal skills to liaise with both patients and other health professionals. Osteopathic teaching and learning should emphasise patient-centred care, including a comprehensive understanding of psychosocial factors, to support and guide the patient journey."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "osteopathy courses and their graduates"
  addressee: both
  verbs: ["graduate", "demonstrate", "acquiring", "emphasise", "support", "guide"]
  about: "core sciences, communication and patient-centred teaching"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "As a primary healthcare profession, osteopathy needs students to graduate with full knowledge and understanding of anatomy, physiology and pathology and excellent communication and interpersonal skills for working with patients and other professionals; teaching and learning should stress patient-centred care, including a full grasp of psychosocial factors, to support the patient's journey."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.4.b1
  locator: { number: "3.4.b1", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 36685, end: 36874 }
  source: "is competent, with a high level of practical skills, including manual therapy skills, and problem-solving ability covering a variety of approaches to support different patient presentations"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of pre-registration osteopathy courses"
  addressee: learner
  verbs: ["support"]
  about: "practical competence and problem-solving"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show they are a competent practitioner with strong practical skills (manual therapy among them) and the problem-solving to draw on varied approaches for different presentations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.4.b2
  locator: { number: "3.4.b2", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 36877, end: 37062 }
  source: "demonstrates a developed knowledge base and clinical ability to allow them to integrate multiple factors in taking a comprehensive overall approach to the health needs of the individual"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of pre-registration osteopathy courses"
  addressee: learner
  verbs: ["demonstrates", "allow", "integrate"]
  about: "integrating many factors in whole-person care"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show a developed knowledge base and clinical ability that lets them bring many factors together in a full, overall approach to a person's health needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.4.b3
  locator: { number: "3.4.b3", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 37065, end: 37160 }
  source: "is caring, empathetic and trustworthy, with the ability to work in partnership with the patient"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of pre-registration osteopathy courses"
  addressee: learner
  verbs: ["work"]
  about: "a caring partnership with the patient"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show they are caring, empathetic and trustworthy and can work as the patient's partner."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.4.b4
  locator: { number: "3.4.b4", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 37163, end: 37310 }
  source: "is professional, with attitudes, values and behaviours consistent with being a healthcare practitioner, including consent, safeguarding and candour"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of pre-registration osteopathy courses"
  addressee: learner
  verbs: []
  about: "professional attitudes, values and behaviour"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show professional attitudes, values and behaviour fitting a healthcare practitioner, including on consent, safeguarding and candour."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.4.b5
  locator: { number: "3.4.b5", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 37313, end: 37385 }
  source: "is reflective, self-aware, inquiring and committed to life-long learning"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of pre-registration osteopathy courses"
  addressee: learner
  verbs: []
  about: "reflection, self-awareness and lifelong learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show they are reflective, self-aware and enquiring, and committed to learning throughout life."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.4.b6
  locator: { number: "3.4.b6", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 37388, end: 37594 }
  source: "appreciates the role of osteopathy in treating patients of all ages but is aware of the limitations of the scope of osteopathic practice, particularly in the context of their own knowledge and capabilities."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of pre-registration osteopathy courses"
  addressee: learner
  verbs: ["appreciates"]
  about: "the scope and limits of osteopathy and of oneself"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to show they value osteopathy's role in treating patients of every age while knowing the limits of its scope, above all in relation to their own knowledge and abilities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.5
  locator: { number: "3.5", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 37595, end: 38166 }
  source: "3.5 Competent students will develop core knowledge, understanding and skills and will have capability to apply these to patient evaluation and management, graduating as safe and rounded practitioners. The following outcomes describe the more detailed clinical, academic and practical expectations of the osteopathic graduate. They are designed to demonstrate the professional capabilities that are needed to become registered as an osteopath in the UK as set out in the OPS and accompanying Graduate Outcomes and\n\n12\nStandards for Education and Training provided by GOsC."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "competent students on graduation"
  addressee: learner
  verbs: ["develop", "apply", "graduating"]
  about: "core capability for safe practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Competent students will build core knowledge, understanding and skill and be able to apply them to evaluating and managing patients, graduating as safe, rounded practitioners; the outcomes in 3.6 set out the detail and are designed to show the capabilities needed to register as an osteopath in the UK under the OPS and the regulator's graduate outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.a.i
  locator: { number: "3.6.a.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 38372, end: 38648 }
  source: "A detailed and integrated knowledge of human structure and function, with emphasis on the neuro-musculoskeletal system, sufficient to recognise, identify and critically differentiate between normal diversity and abnormal anatomical structures and processes in the living body."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["recognise", "identify", "differentiate"]
  about: "human structure and function"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will have a detailed, joined-up knowledge of how the human body is built and works, centred on the neuromusculoskeletal system, enough to tell normal variation from abnormal structure and process in living people."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.a.ii
  locator: { number: "3.6.a.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 38652, end: 38917 }
  source: "Contemporary scientific and medical knowledge of human disease sufficient to inform clinical judgement regarding clinical examination and palpatory findings, and to recognise disorders that require referral for more investigation or additional professional support."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["inform", "recognise"]
  about: "disease knowledge for judgement and referral"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will know enough current science and medicine about human disease to guide clinical judgement on examination and palpation findings and to spot conditions that need referral for further tests or other professional help."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.a.iii
  locator: { number: "3.6.a.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 38922, end: 39164 }
  source: "Knowledge of human psychology and sociology, relevant to the acquisition and maintenance of health, and appreciation of individual needs, values and beliefs, sufficient to provide a context for clinical decision-making and patient management."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["provide"]
  about: "psychology and sociology of health"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will know the psychology and sociology that bear on gaining and keeping health, and appreciate each person's needs, values and beliefs, enough to frame clinical decisions and patient management."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.a.iv
  locator: { number: "3.6.a.iv", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 39168, end: 39303 }
  source: "Knowledge of pain neurophysiology and psychosocial influences and the impact these have on the patient and their clinical presentation."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: []
  about: "pain neurophysiology and psychosocial influence"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will know the neurophysiology of pain and the psychosocial influences on it, and how both affect the patient and the way their problem presents."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.a.v
  locator: { number: "3.6.a.v", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 39306, end: 39444 }
  source: "Understand the role of touch within treatment and how this can influence patients’ responses to the application of osteopathic techniques."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["understand", "influence"]
  about: "the role of touch in treatment"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will understand what touch does within treatment and how it can affect the way patients respond to osteopathic techniques."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.a.vi
  locator: { number: "3.6.a.vi", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 39448, end: 39568 }
  source: "Recognise that the presenting problem may mask underlying health concerns that involve physical and behavioural aspects."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["recognise", "mask", "involve"]
  about: "concerns hidden behind the presenting problem"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will recognise that the problem a patient brings may hide other health concerns, physical and behavioural."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.a.vii
  locator: { number: "3.6.a.vii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 39573, end: 39793 }
  source: "Knowledge to select, effectively apply and monitor an appropriate range of osteopathic techniques and management approaches specific to the needs of the patient, acknowledging any relative and absolute contraindications."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["select", "apply", "monitor", "acknowledging"]
  about: "choosing and monitoring techniques safely"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will know how to choose, use well and monitor a suitable range of osteopathic techniques and management approaches for each patient, taking account of relative and absolute contraindications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.a.viii
  locator: { number: "3.6.a.viii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 39799, end: 40068 }
  source: "Knowledge and understanding of concepts relating to research methodologies, demonstrating the ability to critically appraise and evaluate the quality of quantitative and qualitative clinical research sufficient to inform clinical decision-making and patient management."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["demonstrating", "appraise", "evaluate", "inform"]
  about: "research methods and critical appraisal"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will know and understand research methodology and be able to appraise critically how good numerical and qualitative clinical studies are, enough to guide clinical decisions and patient management."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.b.i
  locator: { number: "3.6.b.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 40112, end: 40248 }
  source: "A critical understanding of principles and concepts of osteopathy and how these may inform rational clinical decision-making activities."
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["inform"]
  about: "osteopathic principles in clinical reasoning"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will understand critically the principles and concepts of osteopathy and how they can guide rational clinical decisions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.b.ii
  locator: { number: "3.6.b.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 40252, end: 40397 }
  source: "An understanding of models of health, disease and illness and how these inform a critical consideration of practical patient care and management."
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["inform"]
  about: "models of health, disease and illness"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will understand models of health, disease and illness and how they shape critical thinking about practical care and management of patients."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.b.iii
  locator: { number: "3.6.b.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 40402, end: 40520 }
  source: "A critical awareness and adaptation of principles, perspectives and practice of other relevant healthcare professions."
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: []
  about: "principles of other health professions"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be critically aware of the principles, perspectives and practice of other relevant health professions and able to adapt them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.b.iv
  locator: { number: "3.6.b.iv", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 40524, end: 40747 }
  source: "An understanding of how osteopathic principles are applied through different osteopathic treatment and management approaches and how to select or modify techniques to meet the needs and preferences of an individual patient."
  stem: "3.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["applied", "select", "modify", "meet"]
  about: "applying principles through treatment approaches"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will understand how osteopathic principles are put into practice through different treatment and management approaches, and how to choose or adapt techniques to suit an individual patient's needs and preferences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.c.i
  locator: { number: "3.6.c.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 40803, end: 40869 }
  source: "Understand different models relating to therapeutic relationships."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["understand"]
  about: "models of the therapeutic relationship"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will understand the different models of the therapeutic relationship."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.c.ii
  locator: { number: "3.6.c.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 40873, end: 41023 }
  source: "Demonstrate the elements and boundaries of a therapeutic relationship with the appropriate skills to form an appropriate partnership with the patient."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["demonstrate", "form"]
  about: "elements and boundaries of the therapeutic relationship"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will show the parts and limits of a therapeutic relationship, with the skills to build a fitting partnership with the patient."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.c.iii
  locator: { number: "3.6.c.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 41028, end: 41171 }
  source: "Show self-awareness to identify potential boundary issues, and to manage these effectively, ensuring ongoing standards of care for the patient."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["show", "identify", "manage", "ensuring"]
  about: "recognising and managing boundary issues"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will show the self-awareness to spot possible boundary problems and handle them well, so that care stays at a proper standard."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.c.iv
  locator: { number: "3.6.c.iv", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 41175, end: 41333 }
  source: "Deal with unfamiliar situations or uncertainty effectively and efficiently, applying duty of candour and the self-awareness to manage the case with integrity."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["deal", "applying", "manage"]
  about: "uncertainty, candour and integrity"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will cope well and promptly with the unfamiliar or uncertain, being open with patients when things go wrong and aware enough of themselves to manage the case honestly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.c.v
  locator: { number: "3.6.c.v", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 41336, end: 41439 }
  source: "Justify acceptable management strategies to cope with ethical issues likely to confront a practitioner."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["justify", "cope", "confront"]
  about: "ethical issues in practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to defend sound strategies for handling the ethical problems a practitioner is likely to meet."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.c.vi
  locator: { number: "3.6.c.vi", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 41443, end: 41655 }
  source: "Maintain patient confidentiality and act only with the informed consent of the patient or other individual able to consent on the patient’s behalf, except in cases where safeguarding concerns would override this."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["maintain", "act", "override"]
  about: "confidentiality and informed consent"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will keep patient information confidential and act only with informed consent from the patient or someone able to consent for them, unless safeguarding concerns take precedence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.c.vii
  locator: { number: "3.6.c.vii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 41660, end: 41822 }
  source: "Adopt appropriate strategies for physical and psychological self-care during interactions with patients to maintain a high standard of professional effectiveness."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["adopt", "maintain"]
  about: "self-care during patient contact"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will use suitable ways of looking after their own physical and psychological well-being while working with patients, to stay professionally effective."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.d.i
  locator: { number: "3.6.d.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 41849, end: 42090 }
  source: "Understand the range and forms of human communication and their strengths and limitations with the skill to move between these different approaches with patients and colleagues, adapting appropriately to the individual they are dealing with."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["understand", "move", "adapting"]
  about: "forms of communication and adapting them"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will understand the kinds of human communication and what each does well and badly, and be able to switch between them with patients and colleagues to suit the person."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.d.ii
  locator: { number: "3.6.d.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 42094, end: 42267 }
  source: "Skilled in relating, integrating and responding to information and data acquired by verbal and non-verbal means, either face-to-face or using telehealth and online meetings."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["relating", "integrating", "responding", "acquired"]
  about: "verbal, non-verbal and remote information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be skilled at linking, combining and acting on information gathered by verbal and non-verbal means, in person or through telehealth and online meetings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.d.iii
  locator: { number: "3.6.d.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 42272, end: 42442 }
  source: "Developing a comprehensive vocabulary to translate palpatory experiences to appropriate language to clearly communicate with colleagues, other professionals and patients."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["developing", "translate", "communicate"]
  about: "language for palpatory findings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be building a full vocabulary that turns what is felt in palpation into suitable language for clear communication with colleagues, other professionals and patients."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.d.iv
  locator: { number: "3.6.d.iv", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 42446, end: 42663 }
  source: "Speak with a critical reasoned perspective about osteopathy, its relative limitations, strengths and potential, appraising research, opinion and anecdote to make sense of therapeutic claims to further inform patients."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["speak", "appraising", "make", "inform"]
  about: "speaking critically about osteopathy and its claims"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will talk about osteopathy from a critical, reasoned standpoint, covering its limits, strengths and potential, weighing research, opinion and anecdote to judge therapeutic claims and better inform patients."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.d.v
  locator: { number: "3.6.d.v", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 42666, end: 43228 }
  source: "Skilled in digital literacy consistent with the efficient management of a modern osteopathic practice, including:\n- the ability to interact with other healthcare professionals\n- the production of written reports and presentations of high quality for referral and related purposes\n- the ability to use information technology for research and clinic-related purposes\n- the ability to manage and present financial and other data needed for compliance with legal requirements\n- the ability to analyse quantitative and qualitative data for audit and related purposes."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["interact", "use", "manage", "present", "analyse"]
  about: "digital literacy for running a practice"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be digitally literate enough to run a modern osteopathic practice efficiently: working with other health professionals, writing good reports and presentations for referral, using technology for research and clinic tasks, handling financial and other data for legal compliance and analysing data of both kinds for audit."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.e.i
  locator: { number: "3.6.e.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 43292, end: 43435 }
  source: "Demonstrate effective and efficient completion of a detailed case history of the patient and an analysis of the patient's presenting complaint."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["demonstrate"]
  about: "case history and analysis of the complaint"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will show effective, efficient taking of a detailed case history and analysis of the presenting complaint."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.e.ii
  locator: { number: "3.6.e.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 43443, end: 43604 }
  source: "Recognise the relative importance of the psychosocial context of the patient's presenting complaint and the role of shared decision making in treatment planning."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["recognise"]
  about: "psychosocial context and shared decisions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will recognise how much the psychosocial setting of the complaint matters and the part shared decision-making plays in planning treatment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.e.iii
  locator: { number: "3.6.e.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 43609, end: 43722 }
  source: "Identify the needs of the patient and facilitate specific clinical investigations or other referrals as required."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["identify", "facilitate"]
  about: "identifying needs and arranging investigations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will identify the patient's needs and arrange specific clinical investigations or other referrals where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.e.iv
  locator: { number: "3.6.e.iv", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 43726, end: 43944 }
  source: "Conduct a thorough and ongoing evaluation of the patient, which may include a biomechanical, psychosocial, attitudinal, palpatory and clinical examination, as appropriate and sensitive to the individual’s presentation."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["conduct", "include"]
  about: "thorough, ongoing evaluation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will carry out a thorough, continuing evaluation of the patient, possibly including biomechanical, psychosocial, attitudinal, palpatory and clinical examination, as suits and respects the person's presentation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.e.v
  locator: { number: "3.6.e.v", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 43947, end: 44146 }
  source: "Generate several hypotheses to explain the patient's presenting complaint, to aid the formulation of a treatment plan or onward referral, including an accessible explanation of the working diagnosis."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["generate", "explain", "aid"]
  about: "hypotheses and the working diagnosis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will produce several hypotheses for the presenting complaint to support a treatment plan or onward referral, with an explanation of the working diagnosis the patient can follow."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.e.vi
  locator: { number: "3.6.e.vi", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 44150, end: 44337 }
  source: "Recognise the characteristics and consequences of non-verbal communication and issues around protected characteristics and socioeconomic status as they may impact on the patient's health."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["recognise", "impact"]
  about: "non-verbal cues, protected characteristics and socioeconomic status"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will recognise the features and effects of non-verbal communication, and how protected characteristics and socioeconomic status may bear on the patient's health."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.e.vii
  locator: { number: "3.6.e.vii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 44342, end: 44423 }
  source: "Generate complete and accurate records of the outcomes of the patient evaluation."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["generate"]
  about: "records of the evaluation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will produce full, accurate records of what the patient evaluation found."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.f.i
  locator: { number: "3.6.f.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 44498, end: 44608 }
  source: "A critical appraisal of the therapeutic value of touch and palpatory influence within diagnosis and treatment."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: []
  about: "the therapeutic value of touch and palpation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will appraise critically what touch and palpation contribute to diagnosis and treatment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.f.ii
  locator: { number: "3.6.f.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 44612, end: 44786 }
  source: "Awareness of the need for ongoing communication with the patient around the use of touch and palpation for confirmation of findings and to ensure patient consent and comfort."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["ensure"]
  about: "talking with patients about touch and consent"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be aware that one must keep talking with the patient about touch and palpation, to confirm findings and to secure consent and comfort."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.f.iii
  locator: { number: "3.6.f.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 44791, end: 44944 }
  source: "The relevant use of criticality to recognise and understand the structure and function of the tissues during palpation as part of the evaluation process."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["recognise", "understand"]
  about: "critical palpation of tissues"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will use criticality to recognise and understand tissue structure and function when palpating during evaluation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.f.iv
  locator: { number: "3.6.f.iv", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 44948, end: 45066 }
  source: "The use of palpation both as a complementary diagnostic, and therapeutic technique to provide reassurance to patients."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["provide"]
  about: "palpation as diagnostic and therapeutic technique"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will use palpation both to help diagnosis and as a therapeutic technique that reassures patients."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.f.v
  locator: { number: "3.6.f.v", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 45069, end: 45246 }
  source: "Demonstrate a sensitivity in using palpatory skill, with an awareness of its limitations and recognise ongoing opportunities for enhancing development of these practical skills."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["demonstrate", "using", "recognise"]
  about: "sensitive palpation and its limits"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will show sensitivity in palpation, knowing its limits and seeing continuing chances to develop the skill."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.f.vi
  locator: { number: "3.6.f.vi", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 45250, end: 45388 }
  source: "Make accurate, consistent and appropriate records of palpatory findings in parallel with objective measures and patient reported outcomes."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["make"]
  about: "recording palpatory findings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will record palpatory findings accurately, consistently and suitably alongside objective measures and outcomes reported by patients."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.f.vii
  locator: { number: "3.6.f.vii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 45393, end: 45521 }
  source: "Use palpation in conjunction with other evaluation methods to inform a working diagnostic hypothesis and ongoing treatment plan."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["use", "inform"]
  about: "palpation combined with other methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will combine palpation with other evaluation methods to shape a working diagnostic hypothesis and a continuing treatment plan."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.g.i
  locator: { number: "3.6.g.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 45599, end: 45711 }
  source: "Perform a detailed analysis and reflection on information gathered during patient history taking and evaluation."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["perform", "gathered"]
  about: "analysing history and evaluation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will analyse and reflect in detail on what history taking and evaluation have produced."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.g.ii
  locator: { number: "3.6.g.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 45715, end: 45812 }
  source: "Generate and justify a set of hypotheses for the aetiology of the patient's presenting complaint."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["generate", "justify"]
  about: "hypotheses on the cause of the complaint"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will generate and justify a set of hypotheses about the cause of the presenting complaint."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.g.iii
  locator: { number: "3.6.g.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 45817, end: 45960 }
  source: "Establish how to inform the patient or person with parental responsibility or guardianship of findings and discuss potential courses of action."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["establish", "inform", "discuss"]
  about: "telling patients or guardians about findings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will work out how to tell the patient, or a person with parental responsibility or guardianship, about findings and talk through possible courses of action."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.g.iv
  locator: { number: "3.6.g.iv", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 45964, end: 46180 }
  source: "Consider appropriate courses of action based on a rational and shared decision- making process which includes a critical consideration of personal limits of competence and the likely effects of osteopathic treatment."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["consider", "includes"]
  about: "shared, reasoned choice of action"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will weigh suitable courses of action through rational, shared decision-making that critically considers the limits of their own competence and the likely effects of treatment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.g.v
  locator: { number: "3.6.g.v", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 46187, end: 46351 }
  source: "With the consent of the patient, or person who can consent on their behalf, make referrals to other healthcare professionals for further investigations if required."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["consent", "make"]
  about: "referral for investigation with consent"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will, with consent from the patient or someone who can consent for them, refer to other health professionals for further investigation where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.g.vi
  locator: { number: "3.6.g.vi", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 46355, end: 46519 }
  source: "Formulate a treatment plan and prognosis that includes monitoring the effect of treatment during and after its application over the course of planned interventions."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["formulate", "includes", "monitoring"]
  about: "treatment plan, prognosis and monitoring"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will draw up a treatment plan and prognosis that tracks the effect of treatment during and after each session across the planned course of care."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.g.vii
  locator: { number: "3.6.g.vii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 46524, end: 46614 }
  source: "Identify and reflect on the obstacles to progress and to plan and take appropriate action."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["identify", "reflect", "plan", "take"]
  about: "obstacles to progress"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will identify and reflect on what is holding back progress and plan and act on it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.h.i
  locator: { number: "3.6.h.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 46676, end: 46874 }
  source: "Demonstrate an awareness of, and ability to select from, the wide range of indirect and direct osteopathic technical approaches as appropriate to the patient and informed by available best evidence."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["demonstrate", "select", "informed"]
  about: "choosing among technical approaches"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will show awareness of, and the ability to choose from, the wide range of direct and indirect osteopathic techniques to suit the patient, guided by the best evidence available."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.h.ii
  locator: { number: "3.6.h.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 46878, end: 47048 }
  source: "Demonstrate awareness and application of a range of patient management approaches developed in conjunction with the patient, considering individual preferences and needs."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["demonstrate", "developed", "considering"]
  about: "patient management agreed with the patient"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will show awareness and use of a range of management approaches agreed with the patient, taking account of their preferences and needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.h.iii
  locator: { number: "3.6.h.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 47053, end: 47162 }
  source: "Rationalise indications and contraindications of using specific osteopathic techniques or their modification."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["rationalise"]
  about: "indications and contraindications"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will reason through the indications and contraindications for specific techniques or their modification."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.h.iv
  locator: { number: "3.6.h.iv", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 47166, end: 47311 }
  source: "Adapt osteopathic approaches and justify or amend its mode of use further in relation to the feedback received as a patient-centred intervention."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["adapt", "justify", "amend"]
  about: "adapting approaches to feedback"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will adapt osteopathic approaches and justify or change how they are used in response to the patient's feedback, as person-centred care."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.i.i
  locator: { number: "3.6.i.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 47366, end: 47534 }
  source: "Monitor spontaneous changes to recognise and record adverse reactions to osteopathic treatment, and initiate appropriate responses, including referral when appropriate."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["monitor", "recognise", "record", "initiate"]
  about: "adverse reactions to treatment"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will watch for spontaneous changes so as to spot and record adverse reactions to treatment, and respond suitably, referring on where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.i.ii
  locator: { number: "3.6.i.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 47538, end: 47607 }
  source: "Maintain an open-minded and inquiring approach to treatment outcomes."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["maintain"]
  about: "an open mind about outcomes"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will keep an open, enquiring mind about the results of treatment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.i.iii
  locator: { number: "3.6.i.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 47612, end: 47742 }
  source: "Record evaluation findings and their interpretation accurately, legibly and accessibly in the case notes of an individual patient."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["record"]
  about: "recording evaluation findings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will write down evaluation findings and what they mean accurately, legibly and accessibly in each patient's notes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.i.iv
  locator: { number: "3.6.i.iv", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 47746, end: 47937 }
  source: "Gather and organise a comprehensive range of qualitative and quantitative data, outcome measures and evidence relevant to the response of an individual patient to an osteopathic intervention."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["gather", "organise"]
  about: "outcome data for an individual patient"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will collect and organise a full range of data, outcome measures and evidence of both kinds on how an individual patient responds to treatment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.j.i
  locator: { number: "3.6.j.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 48014, end: 48152 }
  source: "Operate with a critical appreciation of the key concepts and organisation of health education and health promotion in the UK and overseas."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["operate"]
  about: "health education and health promotion"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will work with a critical grasp of the main ideas behind health education and promotion and how they are organised in the UK and abroad."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.j.ii
  locator: { number: "3.6.j.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 48156, end: 48356 }
  source: "An understanding of the significance and potential effect of psychosocial, cultural, and socioeconomic factors in helping patients to make informed choices about their personal healthcare maintenance."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["helping", "make"]
  about: "social and cultural factors in health choices"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will understand how far psychosocial, cultural and socioeconomic factors matter in helping patients make informed choices about looking after their health."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.j.iii
  locator: { number: "3.6.j.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 48361, end: 48500 }
  source: "Work in partnership with the patient to identify self-care activities, that may include dietary advice, exercise and lifestyle adjustments."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["work", "identify", "include"]
  about: "self-care planned with the patient"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will work with the patient to agree self-care, which may cover diet, exercise and changes to lifestyle."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.j.iv
  locator: { number: "3.6.j.iv", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 48504, end: 48664 }
  source: "Offer realistic advice concerning the location and effective use of local healthcare promoting activities consistent with community, cultural and ethnic values."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["offer"]
  about: "advice on local health-promoting activity"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will give realistic advice on where to find local health-promoting activities and how to use them well, in keeping with community, cultural and ethnic values."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.j.v
  locator: { number: "3.6.j.v", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 48667, end: 48797 }
  source: "Care for their own health and well-being and follow due diligence with the appropriate procedures to manage communicable diseases."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["care", "follow", "manage"]
  about: "own health and infection control"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will look after their own health and well-being and carefully follow the procedures for managing communicable disease."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.j.vi
  locator: { number: "3.6.j.vi", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 48801, end: 48927 }
  source: "Identify potential benefits and limitations of referring an individual patient to other healthcare practitioners or processes."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["identify", "referring"]
  about: "benefits and limits of referral"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will identify what referring a patient to other practitioners or services could gain and where it falls short."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.k.i
  locator: { number: "3.6.k.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 49015, end: 49126 }
  source: "Be committed to lifelong learning through reflective and active approaches to skills and knowledge acquisition."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["be committed"]
  about: "commitment to lifelong learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be committed to learning throughout life, building skills and knowledge through reflection and active approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.k.ii
  locator: { number: "3.6.k.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 49130, end: 49257 }
  source: "Be critically aware of the level of practical skills and clinical knowledge required to deliver the expected standards of care."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["deliver"]
  about: "awareness of what safe care demands"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be critically aware of the practical skill and clinical knowledge needed to give the expected standard of care."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.k.iii
  locator: { number: "3.6.k.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 49262, end: 49414 }
  source: "Be able to reflect on personal and professional strengths and limitations to plan and enact ongoing self-directed professional development and learning."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["reflect", "plan", "enact"]
  about: "self-directed development"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to weigh up their own strengths and weaknesses, personal and professional, so as to plan and carry out continuing self-directed development and learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.k.iv
  locator: { number: "3.6.k.iv", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 49418, end: 49626 }
  source: "Be able to record reflective activities around clinical practice, evidenced through a professional portfolio, sufficient to demonstrate continuing professional development for the professional statutory body."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["record", "evidenced", "demonstrate"]
  about: "a reflective portfolio for CPD"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to record reflection on clinical practice in a professional portfolio, enough to show continuing professional development to the statutory regulator."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.k.ix
  locator: { number: "3.6.k.ix", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 50305, end: 50441 }
  source: "The ability to contribute to and/or understand research and other scholarly activities to support personal and professional development."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["contribute", "understand", "support"]
  about: "research and scholarship"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be able to contribute to or understand research and other scholarship in support of personal and professional growth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.k.v
  locator: { number: "3.6.k.v", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 49629, end: 49822 }
  source: "Evidence of critical problem-solving skills to a level that informs and guides the interpretation of clinical and other data and contributes to effective clinical reasoning and decision-making."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["informs", "guides", "contributes"]
  about: "critical problem-solving in clinical reasoning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will show critical problem-solving skill at a level that guides the reading of clinical and other data and supports sound clinical reasoning and decisions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.k.vi
  locator: { number: "3.6.k.vi", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 49826, end: 50041 }
  source: "Evidence of engagement in peer-review, facilitating respectful feedback and discussion with colleagues that enables collaboration in group activities relevant to the development of the individual and the profession."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["facilitating", "enables"]
  about: "peer review and respectful feedback"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will show engagement in peer review, giving respectful feedback and discussion that lets colleagues work together for their own and the profession's development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.k.vii
  locator: { number: "3.6.k.vii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 50046, end: 50156 }
  source: "Self-care and self-awareness sufficient to consistently maintain an acceptable standard of care for a patient."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["maintain"]
  about: "self-care and self-awareness for safe care"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will have the self-care and self-awareness to keep giving patients an acceptable standard of care consistently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.k.viii
  locator: { number: "3.6.k.viii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 50162, end: 50301 }
  source: "The attitudes and skills necessary to comply fully with continuing fitness to practise standard requirements to maintain registered status."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["comply", "maintain"]
  about: "continuing fitness to practise"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will have the attitudes and skills needed to meet continuing fitness to practise requirements in full and keep their registration."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.l.i
  locator: { number: "3.6.l.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 50514, end: 50603 }
  source: "Understand the concept and significance of statutory regulation authorised by Parliament."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["understand", "authorised"]
  about: "statutory regulation"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will understand what statutory regulation, as authorised by Parliament, is and why it matters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.l.ii
  locator: { number: "3.6.l.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 50607, end: 50753 }
  source: "Abide by the professional standards outlined in the OPS and other guidance issued by the General Osteopathic Council and other appropriate bodies."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["abide", "outlined", "issued"]
  about: "professional standards and guidance"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will keep to the professional standards in the OPS and the other guidance from the General Osteopathic Council and other relevant bodies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.l.iii
  locator: { number: "3.6.l.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 50758, end: 50997 }
  source: "Practise osteopathy safely, competently, and effectively in accordance with the law. This includes, for example, compliance with consent, safeguarding, equality, diversity and inclusivity, data protection and health and safety legislation."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["practise", "includes"]
  about: "safe, competent and lawful practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will practise safely, competently and effectively within the law, for example complying with legislation on consent, safeguarding, equality, diversity and inclusion, data protection and health and safety."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.l.iv
  locator: { number: "3.6.l.iv", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 51001, end: 51809 }
  source: "Act quickly to prevent harm. Appropriate action may include managing the situation by oneself, discussing with a colleague, or reporting to another appropriate authority or body. Acting in all circumstances where patient safety may be at risk will include, for example:\n- disclosing and apologising to patients and discussing and agreeing how to make things better\n- being aware of and complying with the legislative framework and principles in relation to safeguarding vulnerable adults and children\n- acting in circumstances where colleagues' actions may be putting patients at risk of harm or financial loss\n- taking appropriate action where practitioner health may impact on the ability to practise safely\n\n17\n- reporting relevant and appropriate information about conduct or competence to the regulator."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["act", "prevent", "include"]
  about: "acting to prevent harm"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will act promptly to prevent harm, whether by managing the situation alone, consulting a colleague or reporting to a suitable authority; acting where patient safety may be at risk covers candour with patients, safeguarding law, colleagues putting patients at risk, practitioner health and reporting conduct or competence to the regulator."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.l.v
  locator: { number: "3.6.l.v", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 51812, end: 51877 }
  source: "Respect and uphold patient dignity, autonomy and confidentiality."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["respect", "uphold"]
  about: "dignity, autonomy and confidentiality"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will respect and protect patients' dignity, autonomy and confidentiality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.l.vi
  locator: { number: "3.6.l.vi", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 51881, end: 51937 }
  source: "Disclose and justify actions to others when appropriate."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["disclose", "justify"]
  about: "disclosing and justifying actions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will be open about their actions to others and justify them when appropriate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.l.vii
  locator: { number: "3.6.l.vii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 51942, end: 52102 }
  source: "Take responsibility for maintaining professional boundaries and uphold high standards of personal and professional conduct, and the integrity of the profession."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["take", "maintaining", "uphold"]
  about: "boundaries, conduct and integrity"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will take responsibility for keeping professional boundaries and maintain high personal and professional conduct and the profession's integrity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.m.i
  locator: { number: "3.6.m.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 52167, end: 52404 }
  source: "A critical understanding of the delivery of healthcare provision in the UK and overseas and the contribution of osteopathy within the context of one of the Allied Health Professions in NHS England and as primary healthcare practitioners."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: []
  about: "healthcare delivery and osteopathy's place in it"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will critically understand how healthcare is delivered in the UK and abroad and what osteopathy contributes, as an Allied Health Profession in NHS England and as primary healthcare."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.m.ii
  locator: { number: "3.6.m.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 52408, end: 52579 }
  source: "A critical understanding of the specific claims of a range of conventional and non- conventional healthcare professions and how these relate to the practice of osteopathy."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["relate"]
  about: "claims of other health professions"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will critically understand what a range of conventional and non-conventional health professions claim and how this relates to osteopathic practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.m.iii
  locator: { number: "3.6.m.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 52584, end: 52687 }
  source: "Demonstrate a critical evaluation of the current claims of osteopathic practice in the UK and overseas."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["demonstrate"]
  about: "evaluating osteopathy's claims"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will show critical evaluation of what osteopathic practice currently claims, in the UK and abroad."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.n.i
  locator: { number: "3.6.n.i", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 52786, end: 53019 }
  source: "Understand financial and practice management operational details in accordance with legal and ethical requirements, including health and safety standards, and employment legislation and any other relevant guidance or applicable laws."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["understand"]
  about: "financial and practice management within the law"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will understand the financial and operational detail of managing a practice within legal and ethical requirements, including health and safety, employment law and other relevant guidance or law."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.n.ii
  locator: { number: "3.6.n.ii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 53023, end: 53173 }
  source: "Understand the role of audit in monitoring the quality of practice and the ability to contribute to the generation of operational and strategic plans."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["understand", "contribute"]
  about: "audit and planning"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will understand audit's part in checking the quality of practice and be able to help produce operational and strategic plans."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.n.iii
  locator: { number: "3.6.n.iii", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 53178, end: 53305 }
  source: "Maintain patient records and information in compliance with legal and ethical requirements of confidentiality and peer support."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["maintain"]
  about: "compliant patient records"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will keep patient records and information in line with what law and ethics require on confidentiality and peer support."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.n.iv
  locator: { number: "3.6.n.iv", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 53309, end: 53520 }
  source: "Generate effective and high standards of contact with external agencies, including referrals to other healthcare professionals within and outside of the NHS, insurance companies and public service organisations."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["generate"]
  about: "contact with external agencies"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will keep effective, high-standard contact with outside agencies, including referrals to health professionals in and beyond the NHS, insurers and public services."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/3.6.n.v
  locator: { number: "3.6.n.v", headingPath: ["Knowledge, understanding and skills", "The key characteristics of graduates in Osteopathy"] }
  span: { start: 53523, end: 53655 }
  source: "Demonstrate knowledge of business skills necessary to establish a viable osteopathic business that prioritises patients over profit."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on successful completion of a pre-registration osteopathy course"
  addressee: learner
  verbs: ["demonstrate", "establish", "prioritises"]
  about: "business skills for a viable practice"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Will show knowledge of the business skills needed to set up a viable osteopathic business that puts patients before profit."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/4.2
  locator: { number: "4.2", headingPath: ["Teaching and learning", ""] }
  span: { start: 53966, end: 54628 }
  source: "4.2 Knowledge, skills and experience are progressively accumulated throughout the duration of the course. The teaching and learning experience will be a critical and reflective approach to osteopathy with consideration of osteopathic concepts and principles and personalised care for patients. Students will be equipped with reflective, leadership, peer review and lifelong learning skills. The integration of theoretical and practical knowledge and skills prepares students to work autonomously as an osteopath in professional practice. Teaching and learning methods reflect the diverse learning styles of students, delivered in a sustainable and inclusive way."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of osteopathy"
  addressee: learner
  verbs: ["accumulated", "equipped", "prepares", "reflect"]
  about: "reflective, leadership, peer review and lifelong learning skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Knowledge, skills and experience build up across the course; teaching and learning will take a critical, reflective approach to osteopathy with attention to its concepts, principles and personalised care; students will gain reflective, leadership, peer review and lifelong learning skills; joining theory and practice prepares them to work autonomously, and methods suit diverse learning styles and are delivered sustainably and inclusively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/5.1
  locator: { number: "5.1", headingPath: ["Assessment", ""] }
  span: { start: 55987, end: 56221 }
  source: "5.1 Assessment strategies should support students in their development as practitioners and ultimately should enable students to demonstrate that they have met the OPS. Only students who meet these standards are permitted to graduate."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment on pre-registration courses"
  addressee: both
  verbs: ["support", "enable", "demonstrate", "met", "permitted"]
  about: "assessment towards the OPS; the condition to graduate"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment strategies should support students' development as practitioners and in the end let them show they meet the OPS; only students who meet those standards may graduate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/5.2
  locator: { number: "5.2", headingPath: ["Assessment", ""] }
  span: { start: 56222, end: 56625 }
  source: "5.2 Assessment strategies should reflect the range and depth of competence required to meet the OPS and relate to real-life situations and practice where possible, to better prepare students for postgraduation and lifelong learning. Experienced and qualified educators and practitioners should play a central role in developing assessment strategies, which should also be supported by the patient voice."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment strategies"
  addressee: provider
  verbs: ["reflect", "relate", "prepare", "play", "supported"]
  about: "authentic assessment shaped by practitioners and patients"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment strategies should match the range and depth of competence the OPS requires and relate, where possible, to real situations and practice; experienced, qualified educators and practitioners should lead their design, with the patient voice in support."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/osteopathy-2024/5.3
  locator: { number: "5.3", headingPath: ["Assessment", ""] }
  span: { start: 56626, end: 57106 }
  source: "5.3 A diverse range of assessment tools should be utilised, to support students in their learning and development, and to support a range of learning styles and differences. These should be valid and reliable, providing a transparent and supportive pathway for student progression and achievement. Central to assessment strategies should be the use of formative and summative assessments, and the involvement of peers, patients, educators and external expertise where appropriate."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment tools"
  addressee: provider
  verbs: ["utilised", "support", "providing"]
  about: "varied, valid and reliable assessment"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "A varied range of assessment tools should be used to support learning and development and different learning styles and differences; they should be valid and reliable and give a clear, supportive path to progression, with formative and summative assessment and the involvement of peers, patients, educators and outside experts where suitable at the centre."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/osteopathy-2024/5.4
  locator: { number: "5.4", headingPath: ["Assessment", ""] }
  span: { start: 57107, end: 57532 }
  source: "5.4 Assessment of students should reflect the increasing complexity of their studies and responsibilities, and the requirements of meeting the OPS. This should support students as they move from novice to competent practitioner, where they will need to be able to manage clinical uncertainty and demonstrate the qualities and competence of an autonomous healthcare practitioner, capable of working in a range of environments."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "assessment and the students it serves"
  addressee: both
  verbs: ["reflect", "support", "move", "manage", "demonstrate"]
  about: "assessment that tracks growing complexity towards autonomy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Assessment should mirror the rising complexity and responsibility of study and the demands of the OPS, supporting students from novice to competent practitioner, when they will need to manage clinical uncertainty and show the qualities and competence of an autonomous practitioner able to work in many settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.2
  locator: { number: "6.2", headingPath: ["Benchmark Standards", "Introduction"] }
  span: { start: 57907, end: 58227 }
  source: "6.2 Most students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "each higher education provider"
  addressee: provider
  verbs: ["perform", "refer"]
  about: "achievement above threshold and Annex D"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do well above the minimum threshold standards; each provider has its own way of deciding what counts as evidence of this and should refer to Annex D of the UK qualifications frameworks."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/osteopathy-2024/6.6
  locator: { number: "6.6", headingPath: ["Benchmark Standards", "Introduction"] }
  span: { start: 60788, end: 61378 }
  source: "6.6 Students develop skills to critically engage with the three components of evidence- informed practice (clinical experience, research, and patient expectations). They are expected to be able to evaluate the clinical relevance of published research both within and outside of the profession, conduct audits, service evaluation and research for improving the quality of osteopathic practice and patient care, as well as for current professional issues. Osteopaths are expected to support and develop an effective evidenced-informed approach for patient care regardless of practice setting."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "students and osteopaths"
  addressee: learner
  verbs: ["engage", "evaluate", "conduct", "support", "develop"]
  about: "evidence-informed practice and research skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Students develop the skills to engage critically with evidence-informed practice in its three parts, namely research, clinical experience and what patients expect; they are expected to judge how clinically relevant published research is and to carry out audits, service evaluations and research to improve practice, care and current professional issues; in any setting osteopaths are expected to back and build an evidence-informed approach."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.8
  locator: { number: "6.8", headingPath: ["Benchmark Standards", "Introduction"] }
  span: { start: 61919, end: 62403 }
  source: "6.8 Osteopathic education courses are approved by the professional regulator, the General Osteopathic Council, through gaining Recognised Qualification (RQ) status which is reviewed regularly. This requires observing the General Osteopathic Council’s Graduate Outcomes and Standards for Education and Training (September 2022) as well as demonstrating the effective delivery of the OPS which graduating students and registered osteopaths are required to meet throughout their careers."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "osteopathy courses, graduating students and registered osteopaths"
  addressee: both
  verbs: ["approved", "reviewed", "requires", "observing", "demonstrating", "required", "meet"]
  about: "Recognised Qualification approval and the OPS"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Osteopathy courses are approved by the regulator, the General Osteopathic Council, through Recognised Qualification status that is reviewed regularly; this requires following its graduate outcomes and education standards of September 2022 and showing that the OPS are delivered well; those graduating and those registered must meet the OPS for the whole of their careers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.10.b1
  locator: { number: "6.10.b1", headingPath: ["Benchmark Standards", "Standards"] }
  span: { start: 63134, end: 63378 }
  source: "development of a high level of interpersonal and communication skills to interact and communicate professionally, ethically and effectively, from an informed perspective with a diverse range of patients, peers and other healthcare professionals"
  stem: "6.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students awarded an honours degree in osteopathy"
  addressee: learner
  verbs: ["interact", "communicate"]
  about: "interpersonal and communication skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have developed strong interpersonal and communication skills for dealing professionally, ethically and effectively, from an informed position, with diverse patients, peers and other health professionals; this is the minimum for the honours award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.10.b2
  locator: { number: "6.10.b2", headingPath: ["Benchmark Standards", "Standards"] }
  span: { start: 63381, end: 63526 }
  source: "a critical understanding of osteopathic philosophy, principles and concepts and how these may inform rational clinical decision-making activities"
  stem: "6.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students awarded an honours degree in osteopathy"
  addressee: learner
  verbs: ["inform"]
  about: "osteopathic philosophy and principles in decisions"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown a critical grasp of the philosophy, principles and concepts of osteopathy and how they can guide reasoned clinical decisions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.10.b3
  locator: { number: "6.10.b3", headingPath: ["Benchmark Standards", "Standards"] }
  span: { start: 63529, end: 63765 }
  source: "the acquisition of coherent and detailed knowledge and understanding of the interrelationship of biological, physical and behavioural sciences that underpin osteopathic practice and their clinical application throughout a patient’s life"
  stem: "6.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students awarded an honours degree in osteopathy"
  addressee: learner
  verbs: ["underpin"]
  about: "the sciences underpinning practice across the lifespan"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have gained coherent, detailed knowledge and understanding of how the biological, physical and behavioural sciences behind osteopathy interrelate and apply clinically across a patient's life."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.10.b4
  locator: { number: "6.10.b4", headingPath: ["Benchmark Standards", "Standards"] }
  span: { start: 63768, end: 64185 }
  source: "the ability to undertake a clinical and osteopathic assessment process sufficient to assess a patient safely and effectively in order to make a working diagnosis and, in partnership with the patient, through shared decision making, formulate a treatment plan, taking into account their physical, biopsychosocial, cultural, equality and diversity needs, as well as their individual values, preferences and expectations"
  stem: "6.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students awarded an honours degree in osteopathy"
  addressee: learner
  verbs: ["undertake", "assess", "make", "formulate", "taking"]
  about: "safe assessment, working diagnosis and shared planning"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the ability to carry out a clinical and osteopathic assessment that lets them assess a patient safely and effectively, reach a working diagnosis and, with the patient through shared decisions, form a treatment plan that allows for physical, biopsychosocial, cultural, equality and diversity needs and the person's values, preferences and expectations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.10.b5
  locator: { number: "6.10.b5", headingPath: ["Benchmark Standards", "Standards"] }
  span: { start: 64188, end: 64467 }
  source: "a critical approach to the clinical and osteopathic assessment of a patient, using problem-solving and clinical reasoning skills, that draws upon the knowledge gained, including areas that might be incomplete, complex or unpredictable, to inform treatment and management planning"
  stem: "6.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students awarded an honours degree in osteopathy"
  addressee: learner
  verbs: ["using", "draws", "inform"]
  about: "critical clinical reasoning with incomplete knowledge"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown a critical approach to clinical and osteopathic assessment, using problem-solving and clinical reasoning that draws on what they know, including where it may be incomplete, complex or unpredictable, to shape treatment and management plans."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.10.b6
  locator: { number: "6.10.b6", headingPath: ["Benchmark Standards", "Standards"] }
  span: { start: 64470, end: 64775 }
  source: "the ability to critically select, to apply and justify the use of osteopathic treatment approaches specific to the needs of a patient, and to monitor and evaluate their effect during the patient’s treatment plan, as well as guide and educate the patient, as needed, to support their treatment progression."
  stem: "6.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students awarded an honours degree in osteopathy"
  addressee: learner
  verbs: ["select", "apply", "justify", "monitor", "evaluate", "guide", "educate", "support"]
  about: "selecting, applying and evaluating treatment"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the ability to choose critically, apply and justify osteopathic treatment suited to a patient's needs, to monitor and judge its effect over the treatment plan and to guide and educate the patient as needed to help progress."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.10.b7
  locator: { number: "6.10.b7", headingPath: ["Benchmark Standards", "Standards"] }
  span: { start: 64778, end: 65139 }
  source: "an appreciation of the value of osteopaths’ abilities to support patients’ well-being throughout their lifespan and through changing public health considerations. This also includes the value of osteopathic care even when the patient may have a lifelong\n\n22\nillness or disability but can benefit from advice and treatment which supports palliation or well-being"
  stem: "6.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students awarded an honours degree in osteopathy"
  addressee: learner
  verbs: ["support", "benefit"]
  about: "supporting well-being across the lifespan, including long-term illness"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown they appreciate how osteopaths can support patients' well-being across the lifespan and as public health priorities change, including care that eases or supports well-being when a patient lives with lifelong illness or disability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.10.b8
  locator: { number: "6.10.b8", headingPath: ["Benchmark Standards", "Standards"] }
  span: { start: 65142, end: 65368 }
  source: "an understanding of the distinctiveness of osteopathic treatment approaches to patient care to effectively collaborate with other healthcare professions as and when needed, to ensure best patient and population health outcomes"
  stem: "6.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students awarded an honours degree in osteopathy"
  addressee: learner
  verbs: ["collaborate", "ensure"]
  about: "osteopathy's distinctiveness for collaboration"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown understanding of what is distinctive about osteopathic treatment, so as to work well with other health professions when needed and secure the best outcomes for patients and populations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.10.b9
  locator: { number: "6.10.b9", headingPath: ["Benchmark Standards", "Standards"] }
  span: { start: 65371, end: 65708 }
  source: "an appreciation and self-awareness of the limits of one's own competence, skills, knowledge and experience, within the fields of osteopathic practice, education and research, to seek further development through CPD, mentoring and shadowing opportunities or patient referral to another osteopath or healthcare professional, as appropriate"
  stem: "6.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students awarded an honours degree in osteopathy"
  addressee: learner
  verbs: ["seek"]
  about: "knowing the limits of one's own competence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown awareness of the limits of their own competence, skill, knowledge and experience in practice, education and research, and will seek development through CPD, mentoring and shadowing or refer the patient to another osteopath or health professional as fitting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.10.b10
  locator: { number: "6.10.b10", headingPath: ["Benchmark Standards", "Standards"] }
  span: { start: 65711, end: 65968 }
  source: "an understanding and demonstration of the commitment to ongoing professional self- directed learning that informs osteopathic practice, monitors and develops the quality of osteopathic care delivered, and draws upon relevant contemporary advice and research"
  stem: "6.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students awarded an honours degree in osteopathy"
  addressee: learner
  verbs: ["informs", "monitors", "develops", "draws"]
  about: "self-directed professional learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown understanding of, and commitment to, continuing self-directed professional learning that shapes practice, tracks and improves the quality of care and uses current advice and research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.10.b11
  locator: { number: "6.10.b11", headingPath: ["Benchmark Standards", "Standards"] }
  span: { start: 65971, end: 66269 }
  source: "an awareness and effective application of clinically relevant published research, clinical experience, and patient expectations to critically support and evaluate evidence-informed practice for ongoing development of osteopathic practice standards and contribution to patients’ healthcare provision"
  stem: "6.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students awarded an honours degree in osteopathy"
  addressee: learner
  verbs: ["support", "evaluate"]
  about: "evidence-informed practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown awareness and effective use of clinically relevant research, clinical experience and patient expectations to support and judge evidence-informed practice critically, for the development of practice standards and patients' care."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.10.b12
  locator: { number: "6.10.b12", headingPath: ["Benchmark Standards", "Standards"] }
  span: { start: 66272, end: 66471 }
  source: "an understanding and demonstration of the ability to critically evaluate ones' own professional integrity, being mindful of probity, respect, self-care and duty of candour within osteopathic practice"
  stem: "6.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students awarded an honours degree in osteopathy"
  addressee: learner
  verbs: ["evaluate"]
  about: "professional integrity, probity and candour"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown understanding and the ability to judge critically their own professional integrity, with attention to probity, respect, self-care and the duty of candour in practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/osteopathy-2024/6.10.b13
  locator: { number: "6.10.b13", headingPath: ["Benchmark Standards", "Standards"] }
  span: { start: 66474, end: 66654 }
  source: "an ability to make decision in unfamiliar, complex and unpredictable professional circumstances, drawing on qualities such as leadership, resilience, commitment and accountability."
  stem: "6.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students awarded an honours degree in osteopathy"
  addressee: learner
  verbs: ["make", "drawing"]
  about: "decisions in complex, unpredictable situations"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown they can make decisions in unfamiliar, complex and unpredictable professional settings, using leadership, resilience, commitment and accountability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/osteopathy-2024/1.5
  forPractitioner: { text: "Courses that lead to registration must hold Recognised Qualification status from the GOsC with Privy Council approval, must deliver the Osteopathic Practice Standards and should align with the regulator's guidance, including its graduate outcomes and education standards.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you want to practise as an osteopath in the UK, you must gain a qualification recognised by the professional regulator, because by law only registered osteopaths may use the title or practise.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a legal and regulatory requirement the statement reports, not as a graduate outcome: entry to the register depends on a Recognised Qualification approved by the regulator and the Privy Council, and such a qualification must deliver the regulator's practice standards. It applies to the qualification whatever its level (bachelor's at FHEQ 6, integrated master's at FHEQ 7). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.5, and cite the regulator's own documents for the detail. Set it beside qaa/osteopathy-2024/6.8 and 2.1, and do not claim the statement itself sets or confers registration."
  author-agent-dialogue: "Raise it when a prospective or current student asks whether the course leads to practice as an osteopath. Tell a student plainly that you must hold a recognised qualification and register with the regulator before you can use the title; with a programme team, frame it as the condition the course's recognition rests on. Ask whether the person knows if their course holds Recognised Qualification status and what registration involves. Avoid reciting the legislation at length or suggesting the statement itself grants the right to practise."
- statement: qaa/osteopathy-2024/1.6
  forPractitioner: { text: "Because registered osteopaths may practise independently, the course must prepare students for autonomous practice by graduation: the skills and criticality to work within the osteopathic and wider health community, and the reflexivity to keep abreast of evidence and remain fit to practise.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Because you may work on your own as soon as you register, your course must prepare you for independent practice by the time you graduate: you will need the skills and critical thinking to work with other health professionals, and the habit of keeping up with evidence and staying fit to practise.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a requirement the statement places on pre-registration education: graduates must be ready for autonomous practice at the point of graduation, at FHEQ level 6 for the honours award and level 7 for integrated master's. The issuer's words are 'it is critical' and 'requires', recorded here as must (Part E). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.6. Set it beside the threshold standards qaa/osteopathy-2024/6.10.b9, 6.10.b10 and 6.10.b13 and the level 6 descriptor qaa/fheq-2024/4.15.b9.2, and do not claim it adds a registration condition of its own."
  author-agent-dialogue: "Raise it when a student or team asks why the course stresses independence, reflection and keeping up with evidence. Tell a student plainly that you could be practising alone soon after you graduate, so the course aims to make you ready for that; with staff, frame it as the design goal behind clinic autonomy and reflective tasks. Ask how ready the person feels to make decisions without a tutor in the room, and how they keep up with new evidence. Avoid presenting it as a separate test or quoting the paragraph at length."
- statement: qaa/osteopathy-2024/1.12.b1
  forPractitioner: { text: "Teach and model care that centres on the person rather than the condition: this long-held tenet should shape the approach to care, treating health as the product of many interacting influences.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should centre your care on the person, not just their condition, seeing their health as the result of many influences working together.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) about the osteopathic approach to care, given as the first of the features of practice listed in 1.12; it holds for practice and teaching at every level and sets no award outcome. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.12, first bullet. Set it beside the person-centred outcomes qaa/osteopathy-2024/3.4.b2, 3.6.h.ii and 6.10.b4, and do not present it as a measurable threshold or as the regulator's standard."
  author-agent-dialogue: "Raise it when a student's case discussion narrows to the tissue or the diagnosis and loses the person. Put it to a student as advice on how you should approach every patient; to staff, as a principle to model in clinic teaching. Ask what else in the patient's life might be shaping their health, and how that changed the plan. Avoid lecturing on osteopathic philosophy or quoting the passage at length."
- statement: qaa/osteopathy-2024/1.13
  forPractitioner: { text: "Embed equity, equality, diversity and inclusion across institutions, processes, curricula and pedagogy as a collective responsibility that goes past legal minimums: widen participation, counter under-representation, tolerate no discrimination or microaggression, secure access for neurodiverse members and close awarding gaps; all participants will need to engage, reflect and change.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You, like everyone in the osteopathic community, will be expected to engage, reflect and be open to change so that learning is fair and inclusive for all.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation (will) on everyone in the osteopathic learning community, staff and students alike, under the equality, diversity and inclusion theme; it is not a level outcome and holds across the course. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.13. Say that the issuer frames it as a collective responsibility and duty, not as a legal requirement beyond the Equality Act it names. Set it beside qaa/osteopathy-2024/1.14 to 1.18 and the threshold standard 6.10.b4 on equality and diversity needs in treatment planning."
  author-agent-dialogue: "Raise it when equity, access, awarding gaps or discrimination come up in course review or student discussion. With a student, say in plain words that you are part of a community expected to reflect and change to make learning fair; with staff, frame it as a shared duty that reaches past legal minimums. Ask what one change the person or team could make, and what the data on progression and attainment show. Avoid treating it as a student's sole burden or reading the paragraph aloud."
- statement: qaa/osteopathy-2024/1.14
  forPractitioner: { text: "Foster an inclusive community of students, academics, professional staff, patients, visitors and partners; act with commitment so all can reach their potential without harassment or discrimination; acknowledge and counter the legacies of systemic disadvantage, for example with diverse teaching methods. The countering is a must; the fostering a should.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You should help build a learning community where everyone, patients and visitors included, belongs, and where racism, ableism, homophobia and other prejudice must be named and challenged.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as mixed in force: the community should foster inclusion, and legacies of systemic disadvantage must be acknowledged and countered; it is recorded at must, with the should part noted in Part E. It applies to the whole learning community, not to a level or award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.14. Set it beside qaa/osteopathy-2024/1.13 and 1.15 to 1.18, and do not present it as a statutory duty beyond what the Equality Act cited at 1.13 imposes."
  author-agent-dialogue: "Raise it when a team plans inclusive teaching or responds to harassment or discrimination, or when a student raises a concern. With a student, say plainly that you belong to a community that should include everyone and must challenge prejudice; with staff, frame it as an obligation on the institution and its people. Ask who is not yet included in the community and what would change that. Avoid reading lists of prejudices aloud or putting the institution's duty on an individual student."
- statement: qaa/osteopathy-2024/1.15
  forPractitioner: { text: "Build continual critical interrogation of the discipline's language, perceptions and dominant systems of thought into undergraduate and postgraduate study, framing equity as an ethical matter and a human right that supports anti-oppressive knowledge and practice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on courses in shaping the curriculum; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) on undergraduate and postgraduate osteopathic curricula, under the equality, diversity and inclusion theme; it is a curriculum duty, not a student outcome at a set level. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.15. Set it beside qaa/osteopathy-2024/1.16 and 1.17 on core values and critical theory, and do not present it as a learning outcome students must evidence."
  author-agent-dialogue: "Raise it with a programme team reviewing curriculum content, reading lists or the language used about patients and bodies of knowledge. Frame it for staff as a standing invitation to question whose knowledge the course privileges. Ask which accepted ideas in the course have not been questioned recently, and whose voices are missing. Avoid presenting it to students as a requirement on them."
- statement: qaa/osteopathy-2024/1.16
  forPractitioner: { text: "Integrate the community's core values (an ethics of care, plural knowledges, respect, decolonial attention and solidarity) across the curriculum, not in isolated modules, so that students engage with health inequalities, social determinants and diverse patients.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design; the student meets its effect in the curriculum", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) on curriculum design under the equality, diversity and inclusion theme: the named core values are to run through the whole curriculum, not sit in one module; it sets no level outcome. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.16. Set it beside qaa/osteopathy-2024/1.15, 1.17 and the outcomes that touch patient diversity, 3.6.e.vi and 6.10.b4, and do not claim the health-inequality sources it cites as part of the standard."
  author-agent-dialogue: "Raise it when a team maps where equality, diversity and inclusion appear in the course. Frame it for staff as a test of spread: are the values present across modules or confined to one? Ask where in the clinical modules health inequalities and social determinants are discussed. Avoid giving it to students as a duty of theirs."
- statement: qaa/osteopathy-2024/1.17
  forPractitioner: { text: "Apply critical theory across the discipline and curriculum (critical race theory, decoloniality, disability, feminist, queer and science and technology studies among others) and design anticipatorily for each learning site, whether online, face to face, technique class or clinic.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) on the curriculum under the equality, diversity and inclusion theme: critical theory applied across the discipline, and anticipatory design for each site of learning. It is a design duty and sets no student level. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.17. Set it beside qaa/osteopathy-2024/1.16 and 1.18, and name the listed perspectives as examples, not a required syllabus."
  author-agent-dialogue: "Raise it when a team designs teaching for technique classes, clinic or online learning, or chooses theoretical perspectives for the curriculum. Frame it for staff as an expectation that critical perspectives reach clinical teaching, not only theory modules. Ask which learning sites have been least inclusive in the past and what anticipatory changes would help. Avoid presenting the perspectives as mandatory content or as a student requirement."
- statement: qaa/osteopathy-2024/1.18
  forPractitioner: { text: "Provide a supportive cultural and institutional context that helps people stay with the discomfort of new perspectives and skills; this requires the community to develop and promote ways of caring for self and others and to attend to emotional, mental and physical wellbeing.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will be part of a community that is required to develop ways of caring for yourself and others, so that you can cope with the discomfort of meeting new ideas and learning new skills.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a requirement (the issuer's word is requires, recorded as must) on the osteopathic learning community to develop and promote care for self and others; it is a community and design duty under the equality, diversity and inclusion theme, with no level outcome. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.18. Set it beside qaa/osteopathy-2024/1.17 and the self-care outcomes 3.6.c.vii and 3.6.k.vii, and do not present it as a standard for a wellbeing service."
  author-agent-dialogue: "Raise it when students or staff talk about the discomfort of challenging ideas, hands-on learning or difficult clinic encounters. With a student, say plainly that feeling unsettled when learning something new is expected and that the community should help you look after yourself and others; with staff, frame it as a design obligation. Ask what support would help the person stay with a difficult learning moment. Avoid reading it aloud or turning it into a counselling referral by default."
- statement: qaa/osteopathy-2024/1.22
  forPractitioner: { text: "Wherever possible, underpin every mode of teaching, learning and assessment with a concern for accessibility (captioning, recording live sessions, accessible VLE design), choose the means as subject specialists and put supportive measures in place without weakening the regulation that keeps patients safe.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course delivery; the student meets its effect and arranges adjustments with the course", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation (will, wherever possible) that every mode of teaching, learning and assessment rests on a concern for accessibility, under the accessibility theme; it is a provider duty, not a student outcome, and holds at every level. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.22. State the limit the issuer sets: support must not compromise the regulation that protects patient safety. Set it beside qaa/osteopathy-2024/1.20 and 1.21 and the access points of the equality theme at 1.13 and 1.14."
  author-agent-dialogue: "Raise it when a student needs adjustments or cannot attend live sessions, or a team plans recorded, online or clinic-based delivery. With staff, frame it as a standing duty to design for access and to choose the means as subject specialists; with a student, explain only that the course should make learning accessible and how to ask for support. Ask which parts of the course are hardest to reach for students with caring duties, disabilities or poor connections. Avoid promising an adjustment that would affect patient safety in clinic."
- statement: qaa/osteopathy-2024/1.24
  forPractitioner: { text: "Make all eight UNESCO sustainability competencies visible and modelled in learning facilities and curricula: the issuer says practice needs them all and the learning environment therefore requires them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the learning environment and curriculum; the student meets its effect", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a requirement on the learning environment (the issuer's word is requires, recorded as must; Part E) under education for sustainable development: the eight UNESCO competencies are to be shown and modelled in facilities and curricula. It sets no level outcome. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.24, and the guidance named at 1.25 as std:doc:qaa-advancehe-esd-2021-guidance. Set it beside qaa/osteopathy-2024/1.23 and 1.25, and do not claim the statement lists the competencies as assessed graduate outcomes."
  author-agent-dialogue: "Raise it when a team maps sustainability across the curriculum or the estate. Frame it for staff as a requirement to make the eight competencies (systems thinking through to integrated problem-solving) visible in teaching and clinic. Ask which of the eight the course currently models least, and where it could. Avoid presenting the list to students as a checklist they must pass."
- statement: qaa/osteopathy-2024/1.25
  forPractitioner: { text: "Set theoretical learning and professional provision in their social, economic and political context and promote employability; treat personal and social responsibility for others' and one's own well-being as a developmental aim (should).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should grow in your sense of responsibility for your own and other people's well-being, and see your future practice in its social, economic and political setting.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) that personal and social responsibility for well-being is a developmental aim, under education for sustainable development; it holds across undergraduate training, not at a single level. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.25, and the QAA and Advance HE guidance it names as std:doc:qaa-advancehe-esd-2021-guidance. Set it beside qaa/osteopathy-2024/1.23 and 1.24 and the self-care outcomes 3.6.j.v and 3.6.k.vii, and do not present it as an assessed threshold."
  author-agent-dialogue: "Raise it when sustainability, social responsibility or students' own well-being is discussed as part of becoming a professional. With a student, say in plain words that the course aims to grow your sense of responsibility for others and yourself; with staff, frame it as a developmental aim to plan for. Ask how the person's practice could affect the well-being of their community, and how they look after themselves. Avoid treating it as a pass or fail requirement."
- statement: qaa/osteopathy-2024/1.27
  forPractitioner: { text: "Graduates should understand the commercial and practical value of their skills and be able to articulate and show it to employers and in plans for their own practice or further study; courses should encourage awareness of their enterprising and entrepreneurial capabilities and the motivation to apply them flexibly.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should understand what your skills are worth, commercially and practically, and be able to explain and show them to employers or when planning your own practice or further study; you should also come to recognise your own enterprising strengths and use them flexibly.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) of osteopathy graduates under the enterprise and entrepreneurship theme: understanding and articulating the value of their skills, and being encouraged towards enterprising self-awareness; it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.27. Set it beside qaa/osteopathy-2024/1.28 to 1.32 on the entrepreneurial mindset, the outcomes 3.6.n.v and 3.6.d.v and the level descriptor qaa/fheq-2024/4.15.b9.1, and do not present the examples that follow it in 1.28 to 1.32 as required."
  author-agent-dialogue: "Raise it when a student talks about careers, self-employment, opening a practice or further study. Put it plainly: you should be able to say what your skills are worth and show them to an employer or in a business plan. Ask what the person would say if a clinic owner asked what they bring, and which enterprising strengths they see in themselves. Avoid turning it into a sales pitch or implying every graduate must run a business."
- statement: qaa/osteopathy-2024/1.33
  forPractitioner: { text: "Develop digital competency and transferable skills through using digital tools to get ideas across creatively, innovatively and accessibly, for academic success and employability.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should use digital tools to share your ideas creatively and accessibly, which will help both your studies and your career.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) about how digital competency and transferable skills are developed, under the enterprise and employability theme with an accessibility element; it holds across the course and refines the communication strand at FHEQ level 6. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.33. Set it beside qaa/osteopathy-2024/3.6.d.v (digital literacy for practice) and the level 6 descriptor qaa/fheq-2024/4.15.b8, and do not present it as a named digital qualification."
  author-agent-dialogue: "Raise it when a student prepares presentations, online content or patient materials, or a team plans digital skills teaching. Tell a student plainly that you should be able to use digital tools to get ideas across in creative and accessible ways; with staff, frame it as an expectation for where digital work sits in the course. Ask whether a piece of the person's recent work would reach someone using a screen reader or captions. Avoid reducing it to software training."
- statement: qaa/osteopathy-2024/1.34
  forPractitioner: { text: "Make professional, employability and enterprise development a key part of curriculum design across the programme, with outcomes, activities and authentic assessment in dedicated modules and embedded in others.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on curriculum design; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) on curriculum design under the enterprise and entrepreneurship theme: employability, enterprise and entrepreneurship are to be a key aspect, with their placement left open (may). It is a design duty with no level of its own. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.34. Set it beside qaa/osteopathy-2024/1.27, 1.35 to 1.38 and the outcome 3.6.n.v, and do not claim it requires a dedicated module."
  author-agent-dialogue: "Raise it with a programme team mapping employability and enterprise across modules. Frame it for staff as a design expectation with freedom over where it sits. Ask where students now meet authentic assessment of their business and career skills, and whether it is spread or concentrated. Avoid presenting it to students as a duty of theirs."
- statement: qaa/osteopathy-2024/1.35
  forPractitioner: { text: "Involve external speakers, practitioners and alumni in teaching (the issuer recommends it), so students meet varied osteopaths and grow ready to handle the market and present themselves ethically.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a recommendation to the course on its teaching", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a recommendation to courses under the enterprise theme; the issuer's word is recommended, outside the five force words, so it is recorded as describes (Part E) and should not be written up as a must or a should. It holds for teaching across the course, not at a level. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 1.35. Set it beside qaa/osteopathy-2024/1.34 and 1.36 to 1.38."
  author-agent-dialogue: "Raise it when a team plans guest teaching, alumni links or careers input. Frame it for staff as a recommendation, not a requirement, and as a way to show students varied working lives. Ask which kinds of practice students currently never hear about first-hand. Avoid presenting it to students as an obligation."
- statement: qaa/osteopathy-2024/2.3
  forPractitioner: { text: "Design progression aligned to the Quality Code across procedural, propositional and psychomotor knowledge; make applied and clinical reasoning robustly support safe, effective decisions and continuing fitness to practise; provide supervised clinical experience and require autonomy in learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your practical and clinical reasoning skills should firmly support safe, effective decisions about patients and keep you fit to practise; supervised clinic work is central, and you will need to take charge of your own learning.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) that applied and clinical reasoning robustly support safe decision-making, joined by two plain statements that supervised clinical experience is essential and autonomy in learning is required; it applies across the course up to FHEQ level 6 or 7. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 2.3. Set it beside qaa/osteopathy-2024/3.6.g.iv, 3.6.k.iii, the threshold standard 6.10.b5 and the level 6 descriptor qaa/fheq-2024/4.15.b5, and do not claim it sets hours of clinical practice (the figure is in 6.4)."
  author-agent-dialogue: "Raise it when a student asks why clinic matters so much or struggles to take charge of their own learning, or a team reviews clinical progression. Put it plainly to a student: your reasoning should support safe decisions, clinic experience is essential and you are expected to direct your own learning; for staff, frame it as how progression and supervision are designed. Ask how the person reasons from findings to a decision, and what they do to learn between clinic sessions. Avoid quoting the paragraph at length."
- statement: qaa/osteopathy-2024/2.5
  forPractitioner: { text: "Ensure graduates leave with comprehensive anatomy, physiology and pathology and excellent communication and interpersonal skills; teaching and learning should emphasise patient-centred care, psychosocial factors included.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You will need a thorough knowledge of anatomy, physiology and pathology and excellent communication skills, and your teaching should put the patient, with their psychological and social circumstances, at the centre.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) that osteopathic teaching emphasises patient-centred care, set beside a statement that graduates need comprehensive anatomy, physiology and pathology and excellent communication; it bears on the honours award at FHEQ level 6. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 2.5. Set it beside qaa/osteopathy-2024/3.6.a.i, 3.6.d.i and the threshold standards 6.10.b1 and 6.10.b3, and the level descriptor qaa/fheq-2024/4.15.b1; do not present the word excellent here as a rung above threshold."
  author-agent-dialogue: "Raise it when a team weighs the balance of basic science, communication and patient-centred teaching. With staff, frame it as an expectation about emphasis in teaching; with a student, say plainly that you will need strong science and people skills and that care starts from the patient. Ask where in the course patient-centred care is taught and practised, not only described. Avoid treating the word excellent as the minimum standard."
- statement: qaa/osteopathy-2024/3.4.b1
  forPractitioner: { text: "Graduates will be competent, with highly developed practical and manual therapy skills and problem-solving across approaches for different presentations.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be a competent practitioner with strong hands-on and manual therapy skills, able to solve problems using a range of approaches for different patients.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as one of six key characteristics the statement expects an osteopathy graduate to be able to show (practical competence and problem-solving); the lead-in at 3.4 says a graduate can demonstrate it, recorded here as will, at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.4, bullet 1. Do not present it as a separate threshold: it summarises qualities that the outcomes in 3.6 and the threshold list in 6.10 spell out. Set it beside qaa/osteopathy-2024/6.10.b6 and 3.6.h.i and the level descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when a student asks what kind of practitioner the course aims to produce. With a student, put it in plain second-person words as part of the practitioner you are becoming; with staff, frame it as a quality the whole course builds and the clinic shows. Ask: Which kinds of patient presentation do you feel least equipped to handle with your current range of approaches? Avoid reading the list aloud or treating one bullet as the whole picture of a graduate."
- statement: qaa/osteopathy-2024/3.4.b2
  forPractitioner: { text: "Graduates will have a developed knowledge base and the clinical ability to integrate multiple factors into a comprehensive approach to each person's health needs.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will have the knowledge and clinical ability to bring many factors together and look at a patient's health needs as a whole.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as one of six key characteristics the statement expects an osteopathy graduate to be able to show (integrating many factors in whole-person care); the lead-in at 3.4 says a graduate can demonstrate it, recorded here as will, at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.4, bullet 2. Do not present it as a separate threshold: it summarises qualities that the outcomes in 3.6 and the threshold list in 6.10 spell out. Set it beside qaa/osteopathy-2024/6.10.b4 and 1.12.b1 and the level descriptor qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a case discussion needs to pull several factors together. With a student, put it in plain second-person words as part of the practitioner you are becoming; with staff, frame it as a quality the whole course builds and the clinic shows. Ask: In your last complex case, which factors did you bring together, and which did you leave out? Avoid reading the list aloud or treating one bullet as the whole picture of a graduate."
- statement: qaa/osteopathy-2024/3.4.b3
  forPractitioner: { text: "Graduates will be caring, empathetic and trustworthy and able to work in partnership with patients.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be caring, empathetic and trustworthy, and work with patients as partners.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as one of six key characteristics the statement expects an osteopathy graduate to be able to show (a caring partnership with the patient); the lead-in at 3.4 says a graduate can demonstrate it, recorded here as will, at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.4, bullet 3. Do not present it as a separate threshold: it summarises qualities that the outcomes in 3.6 and the threshold list in 6.10 spell out. Set it beside qaa/osteopathy-2024/3.6.c.ii and 3.6.j.iii and the level descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when the therapeutic relationship or patient trust comes up. With a student, put it in plain second-person words as part of the practitioner you are becoming; with staff, frame it as a quality the whole course builds and the clinic shows. Ask: How would a patient you treated describe working with you? Avoid reading the list aloud or treating one bullet as the whole picture of a graduate."
- statement: qaa/osteopathy-2024/3.4.b4
  forPractitioner: { text: "Graduates will hold the attitudes, values and behaviours of a healthcare practitioner, including consent, safeguarding and candour.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will act with the attitudes, values and behaviour expected of a health professional, including on consent, safeguarding and honesty when things go wrong.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as one of six key characteristics the statement expects an osteopathy graduate to be able to show (professional attitudes, values and behaviour); the lead-in at 3.4 says a graduate can demonstrate it, recorded here as will, at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.4, bullet 4. Do not present it as a separate threshold: it summarises qualities that the outcomes in 3.6 and the threshold list in 6.10 spell out. Set it beside qaa/osteopathy-2024/3.6.l.iii and 6.10.b12 and the level descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when professional behaviour, consent or safeguarding is in question. With a student, put it in plain second-person words as part of the practitioner you are becoming; with staff, frame it as a quality the whole course builds and the clinic shows. Ask: When did consent or safeguarding shape what you did in clinic? Avoid reading the list aloud or treating one bullet as the whole picture of a graduate."
- statement: qaa/osteopathy-2024/3.4.b5
  forPractitioner: { text: "Graduates will be reflective, self-aware and enquiring and committed to lifelong learning.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be reflective, self-aware and curious, and committed to learning throughout your career.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as one of six key characteristics the statement expects an osteopathy graduate to be able to show (reflection, self-awareness and lifelong learning); the lead-in at 3.4 says a graduate can demonstrate it, recorded here as will, at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.4, bullet 5. Do not present it as a separate threshold: it summarises qualities that the outcomes in 3.6 and the threshold list in 6.10 spell out. Set it beside qaa/osteopathy-2024/3.6.k.i and 6.10.b10 and the level descriptor qaa/fheq-2024/4.15.b9.3 (spine:6)."
  author-agent-dialogue: "Raise it when a student plans their development or reflects on their learning. With a student, put it in plain second-person words as part of the practitioner you are becoming; with staff, frame it as a quality the whole course builds and the clinic shows. Ask: What has reflection changed in how you practise this year? Avoid reading the list aloud or treating one bullet as the whole picture of a graduate."
- statement: qaa/osteopathy-2024/3.4.b6
  forPractitioner: { text: "Graduates will appreciate osteopathy's role across all ages and know the limits of its scope, especially those set by their own knowledge and capability.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will value what osteopathy can do for patients of all ages and know where its limits lie, especially the limits of your own knowledge and skill.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as one of six key characteristics the statement expects an osteopathy graduate to be able to show (the scope and limits of osteopathy and of oneself); the lead-in at 3.4 says a graduate can demonstrate it, recorded here as will, at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.4, bullet 6. Do not present it as a separate threshold: it summarises qualities that the outcomes in 3.6 and the threshold list in 6.10 spell out. Set it beside qaa/osteopathy-2024/6.10.b9 and 3.6.j.vi and the level descriptor qaa/fheq-2024/4.15.b4 (spine:6)."
  author-agent-dialogue: "Raise it when a student considers treating a patient outside their experience, such as a child or an older adult with complex needs. With a student, put it in plain second-person words as part of the practitioner you are becoming; with staff, frame it as a quality the whole course builds and the clinic shows. Ask: Which patients would you refer on at this stage, and why? Avoid reading the list aloud or treating one bullet as the whole picture of a graduate."
- statement: qaa/osteopathy-2024/3.5
  forPractitioner: { text: "Competent students will build core knowledge, understanding and skill and be able to use them in evaluating and managing patients, graduating as safe, rounded practitioners; 3.6 sets out the detail against the registration requirements.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will build the core knowledge, understanding and skills of osteopathy and be able to use them to assess and care for patients, so that you graduate as a safe, all-round practitioner ready to register.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an outcome statement (will) that introduces the detailed outcomes in 3.6: competent students develop core capability and graduate as safe, rounded practitioners, at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.5. Say that the outcomes are designed to show the capabilities registration needs, not that meeting them registers anyone. Set it beside qaa/osteopathy-2024/3.4, the 3.6 outcomes and the threshold list 6.10, and the level descriptor qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise it when a student asks what the course expects of them by the end, or a team introduces the outcome framework. Put it plainly to a student: you will build the core knowledge and skills to assess and care for patients safely; for staff, frame it as the purpose of the 3.6 outcomes. Ask which parts of patient evaluation and management the person feels least ready for. Avoid listing all the 3.6 outcomes at once."
- statement: qaa/osteopathy-2024/3.6.a.i
  forPractitioner: { text: "Graduates will know human anatomy and physiology in integrated detail, above all the neuromusculoskeletal system, well enough to tell normal variation from pathology in a living patient.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know in detail how the body is built and how it works, especially muscles, bones, joints and nerves, so that you can tell normal variation from something abnormal in a living person.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on knowledge for safe, competent practice; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 a) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b3, the other items in group a) and the level 6 descriptor qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student asks what science they need, or a team reviews the knowledge base of the course. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Could you explain how you would tell a normal anatomical variant from an abnormal finding in a patient you examined? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.a.ii
  forPractitioner: { text: "Graduates will hold current scientific and medical knowledge of disease, enough to support judgement about examination and palpatory findings and to identify when a patient needs referring on.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know enough about disease to make sense of what you find when you examine and palpate a patient, and to notice when someone needs referring for tests or other professional help.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on knowledge for safe, competent practice; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 a) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b3, the other items in group a) and the level 6 descriptor qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student asks what science they need, or a team reviews the knowledge base of the course. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Which findings in a recent case would make you stop and refer the patient on, and why? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.a.iii
  forPractitioner: { text: "Graduates will know the psychology and sociology relevant to health and appreciate individual needs, values and beliefs, as context for their clinical decisions and management of patients.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand the psychological and social side of health and respect each patient's needs, values and beliefs, so that they shape the decisions you make about care.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on knowledge for safe, competent practice; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 a) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b3, the other items in group a) and the level 6 descriptor qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student asks what science they need, or a team reviews the knowledge base of the course. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How did a patient's beliefs or circumstances change the plan you agreed with them? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.a.iv
  forPractitioner: { text: "Graduates will know pain neurophysiology and the psychosocial factors in pain, and how these shape the patient's experience and clinical picture.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how pain works in the nervous system, how psychological and social factors affect it, and how both change what a patient experiences and shows you.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on knowledge for safe, competent practice; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 a) iv. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b3, the other items in group a) and the level 6 descriptor qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student asks what science they need, or a team reviews the knowledge base of the course. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What would you say to a patient about why their pain has lasted longer than the tissue injury? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.a.v
  forPractitioner: { text: "Graduates will understand the place of touch in treatment and how it can shape patients' responses to techniques.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand the part touch plays in treatment and how it can change the way a patient responds to what you do.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on knowledge for safe, competent practice; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 a) v. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b3, the other items in group a) and the level 6 descriptor qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student asks what science they need, or a team reviews the knowledge base of the course. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How might the way you touch a patient change how they respond to a technique? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.a.vi
  forPractitioner: { text: "Graduates will recognise that a presenting complaint can conceal underlying physical or behavioural health issues.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be alert to the chance that the problem a patient comes with may be hiding another health issue, physical or behavioural.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on knowledge for safe, competent practice; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 a) vi. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b3, the other items in group a) and the level 6 descriptor qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student asks what science they need, or a team reviews the knowledge base of the course. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: In your last few new patients, what else could have lain behind the complaint they described? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.a.vii
  forPractitioner: { text: "Graduates will know how to select, apply and monitor osteopathic techniques and management suited to the individual, alert to relative and absolute contraindications.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know how to pick, carry out and keep track of the right osteopathic techniques and ways of managing care for each patient, and when a technique should not be used.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on knowledge for safe, competent practice; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 a) vii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b3, the other items in group a) and the level 6 descriptor qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student asks what science they need, or a team reviews the knowledge base of the course. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Which contraindications did you check before choosing your techniques for that patient? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.a.viii
  forPractitioner: { text: "Graduates will understand research methodologies and critically judge the quality of clinical studies of either kind, numerical or qualitative, so that evidence informs their decisions and care.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how clinical research is done and be able to judge how good a study is, whether numerical or qualitative, so that evidence guides your decisions about patients.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on knowledge for safe, competent practice; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 a) viii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b3, the other items in group a) and the level 6 descriptor qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student asks what science they need, or a team reviews the knowledge base of the course. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Take one study you have read recently: how would you judge whether its findings should change what you do? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.b.i
  forPractitioner: { text: "Graduates will have a critical grasp of osteopathic principles and concepts and how they can support reasoned clinical decision-making.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand the principles and ideas of osteopathy critically and know how they can guide sound clinical decisions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on concepts and principles of osteopathy; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 b) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b2, the other items in group b) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when talk turns to osteopathic principles and how they guide clinical reasoning. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Which osteopathic principle shaped a recent decision you made, and how would you defend that choice? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.b.ii
  forPractitioner: { text: "Graduates will understand models of health, disease and illness and use them to think critically about patient care and management.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand different ways of thinking about health, disease and illness and use them to think critically about how you care for patients.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on concepts and principles of osteopathy; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 b) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b2, the other items in group b) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when talk turns to osteopathic principles and how they guide clinical reasoning. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Which model of health best explains your approach to a patient you are seeing now? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.b.iii
  forPractitioner: { text: "Graduates will be critically aware of how other relevant health professions think and work, and will adapt what is useful from them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know, critically, how other health professions think and work, and be able to adapt what is useful from them in your own practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on concepts and principles of osteopathy; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 b) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b2, the other items in group b) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when talk turns to osteopathic principles and how they guide clinical reasoning. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What could you learn from how a physiotherapist or GP would approach the same patient? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.b.iv
  forPractitioner: { text: "Graduates will understand how principles translate into varied osteopathic treatment and management, and how to choose or adapt techniques for the individual's needs and preferences.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how osteopathic principles show up in different treatments, and how to choose or adjust techniques to suit each patient's needs and wishes.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on concepts and principles of osteopathy; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 b) iv. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b2, the other items in group b) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when talk turns to osteopathic principles and how they guide clinical reasoning. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How did you adapt a technique last week to fit what a patient needed or preferred? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.c.i
  forPractitioner: { text: "Graduates will understand a range of models of the therapeutic relationship.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand the different ways of thinking about the relationship between practitioner and patient.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professionalism and therapeutic relationships; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 c) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group c) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student reflects on a therapeutic relationship, a boundary or an ethical problem. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Which model of the therapeutic relationship best describes how you worked with a recent patient? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.c.ii
  forPractitioner: { text: "Graduates will demonstrate what a therapeutic relationship involves and where its boundaries lie, with the skills to build a proper partnership with each patient.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to show what a good therapeutic relationship involves and where its limits lie, and build a proper partnership with each patient.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professionalism and therapeutic relationships; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 c) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group c) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student reflects on a therapeutic relationship, a boundary or an ethical problem. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Where would you draw the line with a patient who wants more than clinical care from you? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.c.iii
  forPractitioner: { text: "Graduates will show the self-awareness to identify and manage potential boundary issues effectively, keeping standards of care intact.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be self-aware enough to notice when a boundary issue might be arising and deal with it well, so your patient's care does not suffer.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professionalism and therapeutic relationships; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 c) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group c) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student reflects on a therapeutic relationship, a boundary or an ethical problem. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Can you think of a moment in clinic when a boundary felt unclear, and what did you do? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.c.iv
  forPractitioner: { text: "Graduates will deal effectively with unfamiliar situations and uncertainty, apply the duty of candour and manage the case with integrity and self-awareness.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to handle situations that are new or uncertain, be open and honest with patients when something goes wrong, and manage the case with integrity.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professionalism and therapeutic relationships; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 c) iv. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group c) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student reflects on a therapeutic relationship, a boundary or an ethical problem. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Tell me about a time you were unsure what was going on with a patient: what did you do, and what did you tell them? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.c.v
  forPractitioner: { text: "Graduates will justify acceptable strategies for managing the ethical issues practitioners commonly face.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to explain and defend how you would handle the ethical problems you are likely to meet in practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professionalism and therapeutic relationships; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 c) v. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group c) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student reflects on a therapeutic relationship, a boundary or an ethical problem. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What ethical dilemma have you met in clinic, and how would you justify the way you handled it? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.c.vi
  forPractitioner: { text: "Graduates will maintain confidentiality and act only on informed consent from the patient or an authorised person, save where safeguarding overrides it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will keep patients' information confidential and act only with their informed consent, or that of someone who can consent for them, except where a safeguarding concern comes first.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professionalism and therapeutic relationships; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 c) vi. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group c) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student reflects on a therapeutic relationship, a boundary or an ethical problem. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: When would a safeguarding concern lead you to share information without a patient's agreement? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.c.vii
  forPractitioner: { text: "Graduates will use suitable physical and psychological self-care strategies in patient work to sustain professional effectiveness.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will look after your own physical and mental well-being while treating patients, so that you can keep working at your best.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professionalism and therapeutic relationships; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 c) vii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group c) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student reflects on a therapeutic relationship, a boundary or an ethical problem. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What do you do to look after yourself during a demanding clinic session? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.d.i
  forPractitioner: { text: "Graduates will understand the forms of communication and their strengths and limits, and shift between them with patients and colleagues to fit the individual.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand different ways people communicate, what each does well and less well, and switch between them to suit the patient or colleague in front of you.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on communication; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 d) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b1, the other items in group d) and the level 6 descriptor qaa/fheq-2024/4.15.b8 (spine:6)."
  author-agent-dialogue: "Raise it when communication with patients or colleagues, in person or online, comes up. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How did you change the way you explained something for a patient who was not following you? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.d.ii
  forPractitioner: { text: "Graduates will relate, integrate and respond to information gathered verbally and non-verbally, face to face or by telehealth and online.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be good at picking up, combining and responding to what patients tell you and show you, in person or online.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on communication; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 d) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b1, the other items in group d) and the level 6 descriptor qaa/fheq-2024/4.15.b8 (spine:6)."
  author-agent-dialogue: "Raise it when communication with patients or colleagues, in person or online, comes up. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What did you notice in a remote consultation that you might have missed, or caught, in person? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.d.iii
  forPractitioner: { text: "Graduates will be developing a full vocabulary to put palpatory findings into words suited to colleagues, other professionals and patients.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be building the vocabulary to put what you feel with your hands into clear words for patients, colleagues and other professionals.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on communication; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 d) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b1, the other items in group d) and the level 6 descriptor qaa/fheq-2024/4.15.b8 (spine:6)."
  author-agent-dialogue: "Raise it when communication with patients or colleagues, in person or online, comes up. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How would you describe a palpatory finding to a GP, and how would you describe it to the patient? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.d.iv
  forPractitioner: { text: "Graduates will discuss osteopathy critically, including its limits, strengths and potential, weighing research against opinion and anecdote to assess therapeutic claims for patients.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to talk about osteopathy critically, including what it cannot do as well as what it can, and weigh research against opinion and anecdote when telling patients what to expect.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on communication; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 d) iv. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b1, the other items in group d) and the level 6 descriptor qaa/fheq-2024/4.15.b8 (spine:6)."
  author-agent-dialogue: "Raise it when communication with patients or colleagues, in person or online, comes up. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: If a patient asked whether osteopathy can cure their condition, how would you answer honestly? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.d.v
  forPractitioner: { text: "Graduates will have the digital literacy to run a modern practice: liaising with other professionals, producing high-quality referral reports and presentations, using technology for research and clinical work, managing financial and compliance data and analysing data for audit.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be confident with the digital side of running a practice: working with other health professionals, writing good referral reports, using technology for research and clinic work, keeping financial and legal records and analysing data for audit.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on communication; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 d) v. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b1, the other items in group d) and the level 6 descriptor qaa/fheq-2024/4.15.b8 (spine:6)."
  author-agent-dialogue: "Raise it when communication with patients or colleagues, in person or online, comes up. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Which parts of running a practice's records and data do you feel ready for, and which not yet? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.e.i
  forPractitioner: { text: "Graduates will demonstrate effective, efficient detailed case-history taking and analysis of the presenting complaint.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to take a detailed case history efficiently and analyse the problem the patient has come with.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on identifying and evaluating the patient's needs; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 e) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group e) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when a student is learning to assess a new patient or a team reviews clinical assessment. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What questions in your case history most often change your thinking about the complaint? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.e.ii
  forPractitioner: { text: "Graduates will recognise the weight of a complaint's psychosocial context and the part shared decisions play in planning treatment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will recognise how much a patient's life and circumstances matter to their problem, and how deciding together shapes the treatment plan.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on identifying and evaluating the patient's needs; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 e) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group e) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when a student is learning to assess a new patient or a team reviews clinical assessment. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How did the patient take part in deciding their treatment plan last time? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.e.iii
  forPractitioner: { text: "Graduates will identify patients' needs and arrange specific investigations or referrals as needed.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to work out what a patient needs and arrange tests or referrals when they are called for.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on identifying and evaluating the patient's needs; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 e) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group e) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when a student is learning to assess a new patient or a team reviews clinical assessment. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: When did you last decide a patient needed an investigation, and how did you arrange it? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.e.iv
  forPractitioner: { text: "Graduates will evaluate patients thoroughly and continuously, using biomechanical, psychosocial, attitudinal, palpatory and clinical examination as the presentation warrants.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will examine each patient thoroughly and keep reassessing them, using physical, psychological, hands-on and clinical tests as fits their situation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on identifying and evaluating the patient's needs; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 e) iv. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group e) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when a student is learning to assess a new patient or a team reviews clinical assessment. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How did you decide which parts of the examination to use with your last new patient? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.e.v
  forPractitioner: { text: "Graduates will generate several hypotheses for the complaint to inform a plan or referral, and explain the working diagnosis accessibly.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to come up with several possible explanations for a patient's problem, use them to plan treatment or refer on, and explain your working diagnosis in words they understand.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on identifying and evaluating the patient's needs; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 e) v. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group e) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when a student is learning to assess a new patient or a team reviews clinical assessment. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What were your competing hypotheses for a recent case, and how did you explain the working one to the patient? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.e.vi
  forPractitioner: { text: "Graduates will recognise what non-verbal communication shows and how protected characteristics and socioeconomic status can affect health.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will notice what patients communicate without words and understand how things like their background, identity and income can affect their health.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on identifying and evaluating the patient's needs; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 e) vi. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group e) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when a student is learning to assess a new patient or a team reviews clinical assessment. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How might a patient's circumstances or identity have shaped their health and how they spoke to you? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.e.vii
  forPractitioner: { text: "Graduates will generate complete, accurate records of evaluation outcomes.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will keep full and accurate records of what you find when you assess a patient.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on identifying and evaluating the patient's needs; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 e) vii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group e) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when a student is learning to assess a new patient or a team reviews clinical assessment. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Would another practitioner reading your notes understand exactly what you found and why? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.f.i
  forPractitioner: { text: "Graduates will critically appraise the therapeutic value of touch and palpation in diagnosis and treatment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to judge critically what touch and palpation add to diagnosing and treating patients.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on palpation; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 f) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group f) and the level 6 descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when palpation, touch or consent in hands-on work is the subject. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What do you think palpation added to your diagnosis in a recent case, and what could it not tell you? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.f.ii
  forPractitioner: { text: "Graduates will be aware of the need for continuing dialogue with patients about touch and palpation, to confirm findings and keep consent and comfort.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will keep talking with patients about how and why you are touching them, to check your findings and make sure they consent and are comfortable.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on palpation; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 f) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group f) and the level 6 descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when palpation, touch or consent in hands-on work is the subject. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How do you check, during treatment, that a patient is still comfortable and consenting? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.f.iii
  forPractitioner: { text: "Graduates will apply criticality in palpation to recognise and understand tissue structure and function during evaluation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will think critically about what you feel when you palpate, recognising how the tissues are built and working.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on palpation; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 f) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group f) and the level 6 descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when palpation, touch or consent in hands-on work is the subject. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How confident are you that what you feel matches what is there, and how do you check? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.f.iv
  forPractitioner: { text: "Graduates will use palpation as a complementary diagnostic tool and as a reassuring therapeutic technique.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will use palpation both to help work out what is wrong and as a way of treating and reassuring patients.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on palpation; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 f) iv. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group f) and the level 6 descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when palpation, touch or consent in hands-on work is the subject. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: When has palpation reassured a patient as well as informing you? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.f.v
  forPractitioner: { text: "Graduates will palpate with sensitivity, aware of its limits and of continuing ways to develop the skill.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will palpate with sensitivity, know the limits of what it tells you and keep looking for ways to improve.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on palpation; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 f) v. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group f) and the level 6 descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when palpation, touch or consent in hands-on work is the subject. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Where are the limits of your palpation skill at the moment, and how are you working on them? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.f.vi
  forPractitioner: { text: "Graduates will record palpatory findings accurately and consistently, alongside objective measures and patient-reported outcomes.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will record what you find by palpation accurately and consistently, next to objective measures and what the patient reports.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on palpation; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 f) vi. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group f) and the level 6 descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when palpation, touch or consent in hands-on work is the subject. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How do you record a palpatory finding so that you can compare it next session? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.f.vii
  forPractitioner: { text: "Graduates will use palpation with other assessment methods to inform a working diagnosis and ongoing plan.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will combine palpation with other ways of assessing a patient to form a working diagnosis and plan.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on palpation; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 f) vii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b4, the other items in group f) and the level 6 descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when palpation, touch or consent in hands-on work is the subject. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How did your palpation findings fit, or clash with, the rest of your assessment? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.g.i
  forPractitioner: { text: "Graduates will analyse and reflect in detail on information from history taking and evaluation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will analyse and reflect carefully on what you learned from the case history and examination.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on planning, justifying and monitoring treatment; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 g) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b5, the other items in group g) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when treatment planning, hypotheses or referral decisions are being discussed. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What did reflecting on your notes after the session change about your view of the case? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.g.ii
  forPractitioner: { text: "Graduates will generate and justify hypotheses for the aetiology of the presenting complaint.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to put forward and justify possible causes for the patient's problem.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on planning, justifying and monitoring treatment; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 g) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b5, the other items in group g) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when treatment planning, hypotheses or referral decisions are being discussed. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Which cause did you rank first for a recent complaint, and what evidence supported it? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.g.iii
  forPractitioner: { text: "Graduates will establish how to share findings with the patient or a parent or guardian and discuss the options.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know how to explain your findings to a patient, or to a parent or guardian, and talk through the options.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on planning, justifying and monitoring treatment; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 g) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b5, the other items in group g) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when treatment planning, hypotheses or referral decisions are being discussed. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How would you explain your findings and options to the parent of a young patient? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.g.iv
  forPractitioner: { text: "Graduates will consider options through rational, shared decision-making, critically weighing their own limits of competence and treatment's likely effects.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will weigh up options with the patient in a reasoned way, thinking critically about the limits of your own competence and what treatment is likely to do.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on planning, justifying and monitoring treatment; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 g) iv. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b5, the other items in group g) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when treatment planning, hypotheses or referral decisions are being discussed. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: When did the limits of your competence shape the option you and a patient chose? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.g.v
  forPractitioner: { text: "Graduates will refer patients to other health professionals for further investigation when needed, with proper consent.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will refer patients to other health professionals for further tests when needed, with their consent or that of someone who can consent for them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on planning, justifying and monitoring treatment; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 g) v. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b5, the other items in group g) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when treatment planning, hypotheses or referral decisions are being discussed. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How do you gain consent for a referral, and what do you do if the patient declines? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.g.vi
  forPractitioner: { text: "Graduates will formulate a plan and prognosis that monitors treatment effects during and after application over the planned course.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will draw up a treatment plan and prognosis and keep checking how treatment is working, during and after each session.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on planning, justifying and monitoring treatment; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 g) vi. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b5, the other items in group g) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when treatment planning, hypotheses or referral decisions are being discussed. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How did you decide on the prognosis you gave, and how will you know if treatment is on track? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.g.vii
  forPractitioner: { text: "Graduates will identify and reflect on obstacles to progress and plan and take suitable action.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will spot and think about what is getting in the way of a patient's progress, then plan and act on it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on planning, justifying and monitoring treatment; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 g) vii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b5, the other items in group g) and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when treatment planning, hypotheses or referral decisions are being discussed. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What has slowed a patient's progress recently, and what did you change? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.h.i
  forPractitioner: { text: "Graduates will demonstrate knowledge of, and choice among, the full range of direct and indirect techniques, matched to the patient and guided by best evidence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know the wide range of direct and indirect osteopathic techniques and be able to choose the right ones for each patient, guided by the best evidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on conducting treatment and patient management; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 h) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b6, the other items in group h) and the level 6 descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when a student is choosing or adapting techniques and management. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Why did you choose a direct or an indirect approach with your last patient? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.h.ii
  forPractitioner: { text: "Graduates will demonstrate a range of patient management approaches developed with the patient and responsive to their preferences and needs.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will use a range of ways of managing a patient's care, worked out with them and shaped by what they need and prefer.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on conducting treatment and patient management; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 h) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b6, the other items in group h) and the level 6 descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when a student is choosing or adapting techniques and management. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How did a patient's preferences change the management approach you agreed? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.h.iii
  forPractitioner: { text: "Graduates will rationalise indications and contraindications for specific techniques and their adaptations.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to explain when a particular technique, or a changed version of it, is or is not suitable.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on conducting treatment and patient management; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 h) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b6, the other items in group h) and the level 6 descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when a student is choosing or adapting techniques and management. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What made a technique unsuitable for a patient you saw, and what did you do instead? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.h.iv
  forPractitioner: { text: "Graduates will adapt approaches and justify or amend their use in response to patient feedback, as person-centred intervention.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will adjust your approach in response to how the patient reacts, and be able to explain why.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on conducting treatment and patient management; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 h) iv. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b6, the other items in group h) and the level 6 descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when a student is choosing or adapting techniques and management. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: When did a patient's feedback make you change a technique mid-treatment? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.i.i
  forPractitioner: { text: "Graduates will monitor for and record adverse reactions to treatment and respond suitably, including by referral.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will watch for and record any unwanted reactions to treatment and respond properly, including referring the patient on if needed.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on evaluating progress after treatment; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 i) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b6, the other items in group i) and the level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when a student reviews a patient's response to treatment. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What would you do if a patient reported feeling worse after treatment? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.i.ii
  forPractitioner: { text: "Graduates will maintain an open-minded, enquiring stance towards treatment outcomes.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will stay open-minded and curious about how your treatments turn out.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on evaluating progress after treatment; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 i) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b6, the other items in group i) and the level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when a student reviews a patient's response to treatment. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: When did an outcome surprise you, and what did you learn from it? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.i.iii
  forPractitioner: { text: "Graduates will write evaluation findings and what they mean into case notes accurately, legibly and accessibly.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will write up what you found and what you think it means clearly and accurately in each patient's notes.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on evaluating progress after treatment; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 i) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b6, the other items in group i) and the level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when a student reviews a patient's response to treatment. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Could a colleague act safely on your notes if you were absent? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.i.iv
  forPractitioner: { text: "Graduates will gather and organise qualitative and quantitative data, outcome measures and evidence on a patient's response to treatment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will collect and organise numbers, measures and patients' own accounts to show how someone is responding to treatment.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on evaluating progress after treatment; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 i) iv. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b6, the other items in group i) and the level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when a student reviews a patient's response to treatment. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Which outcome measures do you use to show a patient's progress? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.j.i
  forPractitioner: { text: "Graduates will work with a critical appreciation of the concepts and organisation of health education and promotion at home and abroad.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand critically how health education and health promotion work, in the UK and elsewhere.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on advice and support for healthy living; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 j) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b7, the other items in group j) and the level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when advice on healthy living or referral to other services is in question. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How does what you advise patients fit with national health promotion messages? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.j.ii
  forPractitioner: { text: "Graduates will understand the bearing of psychosocial, cultural and socioeconomic factors on patients' informed choices about their own health maintenance.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how people's circumstances, culture and income affect the choices they make about their health, and use this to help them choose well.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on advice and support for healthy living; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 j) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b7, the other items in group j) and the level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when advice on healthy living or referral to other services is in question. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What got in the way of a patient following your advice, and how could you have helped? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.j.iii
  forPractitioner: { text: "Graduates will work in partnership with patients to identify self-care, such as dietary advice, exercise and lifestyle change.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will work with patients to agree what they can do for themselves, such as diet, exercise and changes to daily life.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on advice and support for healthy living; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 j) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b7, the other items in group j) and the level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when advice on healthy living or referral to other services is in question. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What self-care did you agree with a patient, and how did you check it suited them? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.j.iv
  forPractitioner: { text: "Graduates will offer realistic advice on local health-promoting activities that respects community, cultural and ethnic values.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to point patients to realistic local activities that support their health, in ways that respect their community and culture.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on advice and support for healthy living; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 j) iv. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b7, the other items in group j) and the level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when advice on healthy living or referral to other services is in question. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What local activities could you recommend to a patient, and would they fit that patient's life? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.j.v
  forPractitioner: { text: "Graduates will care for their own health and follow due diligence and procedures for communicable disease.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will look after your own health and follow infection-control procedures carefully.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on advice and support for healthy living; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 j) v. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b7, the other items in group j) and the level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when advice on healthy living or referral to other services is in question. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What infection-control steps do you take between patients? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.j.vi
  forPractitioner: { text: "Graduates will identify the potential benefits and limits of referring patients to other practitioners or services.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to weigh up what a patient could gain from being referred elsewhere, and what the drawbacks might be.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on advice and support for healthy living; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 j) vi. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b7, the other items in group j) and the level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when advice on healthy living or referral to other services is in question. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: For a patient you referred, what did you expect them to gain and what were the risks? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.k.i
  forPractitioner: { text: "Graduates will commit to lifelong learning, gaining skills and knowledge through reflective and active approaches.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be committed to learning throughout your career, using reflection and active practice to keep building your skills and knowledge.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on personal and professional development; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 k) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b10, the other items in group k) and the level 6 descriptor qaa/fheq-2024/4.15.b5 (spine:6)."
  author-agent-dialogue: "Raise it when a student plans their learning, reflection or continuing development. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What have you learned recently outside the set curriculum, and how did you go about it? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.k.ii
  forPractitioner: { text: "Graduates will be critically aware of the level of practical skill and clinical knowledge the expected standards of care require.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know, critically, what level of practical skill and clinical knowledge good care demands of you.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on personal and professional development; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 k) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b10, the other items in group k) and the level 6 descriptor qaa/fheq-2024/4.15.b5 (spine:6)."
  author-agent-dialogue: "Raise it when a student plans their learning, reflection or continuing development. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Where does your current skill fall short of what safe care needs, and what is your plan? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.k.iii
  forPractitioner: { text: "Graduates will reflect on their strengths and limits and plan and carry out ongoing self-directed development.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reflect on your strengths and weaknesses, plan how to develop and follow your plan through.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on personal and professional development; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 k) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b10, the other items in group k) and the level 6 descriptor qaa/fheq-2024/4.15.b5 (spine:6)."
  author-agent-dialogue: "Raise it when a student plans their learning, reflection or continuing development. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What is the next thing you want to develop, and how will you know you have? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.k.iv
  forPractitioner: { text: "Graduates will record reflective activity on clinical practice in a portfolio that evidences CPD for the statutory regulator.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to record your reflections on clinical practice in a portfolio that shows your professional development to the regulator.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on personal and professional development; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 k) iv. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b10, the other items in group k) and the level 6 descriptor qaa/fheq-2024/4.15.b5 (spine:6)."
  author-agent-dialogue: "Raise it when a student plans their learning, reflection or continuing development. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What entry from your portfolio best shows your development this year? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.k.ix
  forPractitioner: { text: "Graduates will contribute to, or understand, research and scholarly activity that supports their personal and professional development.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to take part in, or make sense of, research and other scholarly work to help you grow personally and professionally.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on personal and professional development; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 k) ix. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b10, the other items in group k) and the level 6 descriptor qaa/fheq-2024/4.15.b5 (spine:6)."
  author-agent-dialogue: "Raise it when a student plans their learning, reflection or continuing development. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How has a piece of research you took part in or read shaped your practice? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.k.v
  forPractitioner: { text: "Graduates will evidence critical problem-solving that informs interpretation of clinical and other data and supports clinical reasoning and decisions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to solve problems critically, so that you read clinical information well and reason soundly about what to do.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on personal and professional development; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 k) v. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b10, the other items in group k) and the level 6 descriptor qaa/fheq-2024/4.15.b5 (spine:6)."
  author-agent-dialogue: "Raise it when a student plans their learning, reflection or continuing development. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Walk me through how you solved a puzzling case: where did your reasoning change direction? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.k.vi
  forPractitioner: { text: "Graduates will evidence peer review and respectful feedback that supports collaborative group work for individual and professional development.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will take part in peer review, giving and receiving feedback respectfully so that you and your colleagues improve together.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on personal and professional development; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 k) vi. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b10, the other items in group k) and the level 6 descriptor qaa/fheq-2024/4.15.b5 (spine:6)."
  author-agent-dialogue: "Raise it when a student plans their learning, reflection or continuing development. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What feedback from a peer changed how you practise? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.k.vii
  forPractitioner: { text: "Graduates will show self-care and self-awareness enough to sustain an acceptable standard of patient care.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will look after yourself and know yourself well enough to keep your care of patients at a good standard.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on personal and professional development; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 k) vii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b10, the other items in group k) and the level 6 descriptor qaa/fheq-2024/4.15.b5 (spine:6)."
  author-agent-dialogue: "Raise it when a student plans their learning, reflection or continuing development. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How do you notice when tiredness or stress might affect your care? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.k.viii
  forPractitioner: { text: "Graduates will have the attitudes and skills to comply fully with continuing fitness to practise requirements and stay registered.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will have the attitudes and skills to keep meeting fitness to practise requirements, so you can stay on the register.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on personal and professional development; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 k) viii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b10, the other items in group k) and the level 6 descriptor qaa/fheq-2024/4.15.b5 (spine:6)."
  author-agent-dialogue: "Raise it when a student plans their learning, reflection or continuing development. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What would put your fitness to practise at risk, and how would you guard against it? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.l.i
  forPractitioner: { text: "Graduates will understand the concept and importance of statutory regulation of the profession.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand what it means for your profession to be regulated by law, and why that matters.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professional identity, accountability and ethics; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 l) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group l) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when professional conduct, regulation or patient safety comes up. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Why do you think osteopathy is regulated by law, and what does that mean for you? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.l.ii
  forPractitioner: { text: "Graduates will abide by the OPS and other guidance from the GOsC and other appropriate bodies.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will follow the regulator's professional standards and other guidance for osteopaths.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professional identity, accountability and ethics; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 l) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group l) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when professional conduct, regulation or patient safety comes up. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Which part of the professional standards do you find hardest to apply in practice? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.l.iii
  forPractitioner: { text: "Graduates will practise safely, competently and effectively within the law, including consent, safeguarding, equality, data protection and health and safety legislation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will practise safely, competently and effectively within the law, including the rules on consent, safeguarding, equality, data protection and health and safety.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professional identity, accountability and ethics; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 l) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group l) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when professional conduct, regulation or patient safety comes up. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Which legal duty do you feel least sure about, and how could you check it? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.l.iv
  forPractitioner: { text: "Graduates will act quickly to prevent harm, alone, with a colleague or by reporting, covering candour, safeguarding, reports to the regulator and concerns about colleagues or their own health.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will act quickly to prevent harm: dealing with it yourself, talking to a colleague or reporting it, including being open with patients, safeguarding, raising concerns about colleagues or your own health and reporting to the regulator.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professional identity, accountability and ethics; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 l) iv. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group l) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when professional conduct, regulation or patient safety comes up. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: If you saw a colleague putting a patient at risk, what would you do first? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.l.v
  forPractitioner: { text: "Graduates will respect and uphold patient dignity, autonomy and confidentiality.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will respect and protect each patient's dignity, independence and privacy.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professional identity, accountability and ethics; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 l) v. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group l) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when professional conduct, regulation or patient safety comes up. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How do you protect a patient's dignity during examination? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.l.vi
  forPractitioner: { text: "Graduates will disclose and justify their actions to others when appropriate.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be open about what you have done and be able to explain why, when that is called for.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professional identity, accountability and ethics; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 l) vi. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group l) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when professional conduct, regulation or patient safety comes up. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: When have you had to explain a clinical decision to someone else? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.l.vii
  forPractitioner: { text: "Graduates will take responsibility for professional boundaries and uphold high standards of conduct and the profession's integrity.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will take responsibility for keeping professional boundaries and for behaving well, personally and professionally, so the profession can be trusted.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on professional identity, accountability and ethics; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 l) vii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b12, the other items in group l) and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when professional conduct, regulation or patient safety comes up. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What does professional conduct outside clinic mean for you? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.m.i
  forPractitioner: { text: "Graduates will critically understand UK and overseas healthcare delivery and osteopathy's contribution, as an Allied Health Profession in NHS England and as primary care.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand critically how healthcare is organised in the UK and elsewhere, and where osteopathy fits, including as an allied health profession and in primary care.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on collaboration across professions; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 m) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b8, the other items in group m) and the level 6 descriptor qaa/fheq-2024/4.15.b3.2 (spine:6)."
  author-agent-dialogue: "Raise it when osteopathy's place in wider healthcare or its claims are discussed. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Where does osteopathy fit in the care pathway for back pain in your area? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.m.ii
  forPractitioner: { text: "Graduates will critically understand the claims of conventional and non-conventional health professions and their relation to osteopathy.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand critically what other health professions, mainstream and not, claim to do and how that relates to osteopathy.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on collaboration across professions; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 m) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b8, the other items in group m) and the level 6 descriptor qaa/fheq-2024/4.15.b3.2 (spine:6)."
  author-agent-dialogue: "Raise it when osteopathy's place in wider healthcare or its claims are discussed. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How do the claims of a neighbouring profession compare with what osteopathy can show? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.m.iii
  forPractitioner: { text: "Graduates will demonstrate critical evaluation of current claims made for osteopathic practice at home and abroad.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to judge critically what osteopathy currently claims to achieve, in the UK and elsewhere.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on collaboration across professions; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 m) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b8, the other items in group m) and the level 6 descriptor qaa/fheq-2024/4.15.b3.2 (spine:6)."
  author-agent-dialogue: "Raise it when osteopathy's place in wider healthcare or its claims are discussed. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: Which claim made for osteopathy would you want stronger evidence for? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.n.i
  forPractitioner: { text: "Graduates will understand financial and operational practice management within legal and ethical requirements, including health and safety and employment law.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand the money and day-to-day running of a practice within the law and ethics, including health and safety and employment rules.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on running a practice; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 n) i. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b13, the other items in group n) and the level 6 descriptor qaa/fheq-2024/4.15.b9.2 (spine:6)."
  author-agent-dialogue: "Raise it when a student thinks about running or working in a practice. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What would you need to have in place, legally and financially, before opening your own clinic? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.n.ii
  forPractitioner: { text: "Graduates will understand audit's role in monitoring practice quality and contribute to operational and strategic planning.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how audit checks the quality of a practice and be able to help plan how a practice runs and develops.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on running a practice; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 n) ii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b13, the other items in group n) and the level 6 descriptor qaa/fheq-2024/4.15.b9.2 (spine:6)."
  author-agent-dialogue: "Raise it when a student thinks about running or working in a practice. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: What would you audit first in a clinic you worked in, and why? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.n.iii
  forPractitioner: { text: "Graduates will maintain records and information that meet the legal and ethical duties of confidentiality and of peer support.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will keep patient records and information in a way that meets legal and ethical rules on confidentiality.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on running a practice; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 n) iii. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b13, the other items in group n) and the level 6 descriptor qaa/fheq-2024/4.15.b9.2 (spine:6)."
  author-agent-dialogue: "Raise it when a student thinks about running or working in a practice. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How do you store and share patient records safely? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.n.iv
  forPractitioner: { text: "Graduates will generate effective, high-standard contact with external agencies, including referrals within and outside the NHS, insurers and public services.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will deal effectively and professionally with outside organisations, such as the NHS, other health professionals, insurers and public services.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on running a practice; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 n) iv. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b13, the other items in group n) and the level 6 descriptor qaa/fheq-2024/4.15.b9.2 (spine:6)."
  author-agent-dialogue: "Raise it when a student thinks about running or working in a practice. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How would you write to a GP about a patient you were concerned about? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/3.6.n.v
  forPractitioner: { text: "Graduates will demonstrate the business knowledge needed to establish a viable practice that puts patients ahead of profit.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know the business skills needed to set up a practice that works financially while putting patients before profit.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on running a practice; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 3.6 n) v. Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b13, the other items in group n) and the level 6 descriptor qaa/fheq-2024/4.15.b9.2 (spine:6)."
  author-agent-dialogue: "Raise it when a student thinks about running or working in a practice. With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. Ask: How would you keep a new practice viable without letting income drive clinical decisions? Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."
- statement: qaa/osteopathy-2024/4.2
  forPractitioner: { text: "Teaching and learning will be critical and reflective about osteopathic concepts, principles and personalised care; students will gain reflective, leadership, peer-review and lifelong learning skills, and methods suit diverse learners and are delivered sustainably and inclusively.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will learn in a critical, reflective way and gain skills in reflection, leadership, peer review and lifelong learning that prepare you to practise on your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation (will) about the teaching and learning experience and the skills students gain from it (reflection, leadership, peer review, lifelong learning), at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 4.2. Set it beside qaa/osteopathy-2024/3.6.k.i, 3.6.k.vi, the threshold standard 6.10.b13 on leadership and the level descriptor qaa/fheq-2024/4.15.b9.3; its mention of sustainable and inclusive delivery links it to the cross-cutting themes without making it a theme statement."
  author-agent-dialogue: "Raise it when a student asks what kind of learning to expect or how leadership and peer review fit an osteopathy course. Tell a student plainly that you will be asked to reflect, give and take peer feedback and lead, because you will practise on your own; for staff, frame it as what teaching should build. Ask where the person has practised leadership or peer review so far. Avoid presenting it as a list of assessed units."
- statement: qaa/osteopathy-2024/5.1
  forPractitioner: { text: "Design assessment that supports development and finally enables students to demonstrate they meet the OPS; only those who meet them graduate.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your assessments should help you develop as a practitioner and let you show that you meet the professional standards; you will only graduate once you have met them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) on assessment strategy, with a plain condition attached: only students who meet the OPS are permitted to graduate. It holds for the pre-registration award at FHEQ level 6 or 7, not for a single module. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 5.1, and the regulator's OPS for the standards themselves. Set it beside qaa/osteopathy-2024/5.2 to 5.4 and 6.8, and do not claim the statement defines the OPS."
  author-agent-dialogue: "Raise it when a student asks what they must show to graduate or a team designs final assessments. Tell a student plainly that assessment is there to help you develop and that you graduate only when you have shown you meet the professional standards; for staff, frame it as a design expectation with a firm condition at the end. Ask how the person's assessments so far map to the professional standards. Avoid reading out the standards or implying a grade alone decides it."
- statement: qaa/osteopathy-2024/5.2
  forPractitioner: { text: "Make assessment reflect the range and depth of OPS competence and real practice where possible; involve experienced educators and practitioners centrally, supported by the patient voice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in designing assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) on how assessment strategies are designed: authentic, matched to OPS competence and shaped by practitioners and the patient voice; it is a provider duty with no level of its own. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 5.2. Set it beside qaa/osteopathy-2024/5.1, 5.3 and 5.4, and do not claim it requires patients to mark students."
  author-agent-dialogue: "Raise it when a team reviews assessment design, patient involvement or authenticity. Frame it for staff as an expectation that assessment mirrors real practice and draws on practitioners and patients. Ask where patients now shape assessment and how close the tasks are to real clinic. Avoid giving it to students as their responsibility."
- statement: qaa/osteopathy-2024/5.3
  forPractitioner: { text: "Use varied, valid and reliable assessment tools that support different learners and give a transparent path to progression, centred on formative and summative assessment and involving peers, patients, educators and external expertise where suitable.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in choosing assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) on the assessment toolset: varied, valid, reliable and centred on formative and summative assessment with peer, patient and external involvement; a provider duty with no level of its own. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 5.3. Set it beside qaa/osteopathy-2024/5.2 and 5.4 and the inclusive design paragraphs 1.17 and 1.22, and do not claim it names particular tools."
  author-agent-dialogue: "Raise it when a team reviews the assessment mix or a concern arises about fairness for different learners. Frame it for staff as an expectation of variety, validity and transparency. Ask whether students can see how each assessment leads to the next stage, and where formative feedback sits. Avoid presenting it to a student as their duty."
- statement: qaa/osteopathy-2024/5.4
  forPractitioner: { text: "Assessment should track rising complexity and responsibility and the OPS requirements, supporting the move from novice to competent practitioner able to handle clinical uncertainty and act autonomously across settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your assessments should grow more demanding as you progress, helping you move from beginner to competent practitioner who can handle clinical uncertainty and work independently in different settings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) on assessment progression, with the outcome it serves stated in will: by the end students need to manage clinical uncertainty and show the competence of an autonomous practitioner, at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 5.4. Set it beside qaa/osteopathy-2024/5.1, the threshold standard 6.10.b13 and the level 6 descriptor qaa/fheq-2024/4.15.b9.2, and do not claim it sets level 7 outcomes for integrated master's courses."
  author-agent-dialogue: "Raise it when a student asks why assessment gets harder or a team designs progression across years. Tell a student plainly that assessment grows with you, towards handling uncertainty on your own; for staff, frame it as the progression assessment should follow. Ask what clinical uncertainty the person has handled recently and how. Avoid presenting the end point as something expected in the first year."
- statement: qaa/osteopathy-2024/6.2
  forPractitioner: { text: "Expect most students to exceed the threshold; set your own method for judging evidence of higher achievement and refer to Annex D of the Frameworks for Higher Education Qualifications.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in judging achievement above the threshold; the student-facing point is the threshold list at 6.10", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) on providers: judge achievement above the threshold by their own method, with reference to Annex D, the degree classification descriptions. It holds for the honours award at FHEQ level 6. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.2, and Annex D as std:doc:qaa-fheq-2024-framework (for example qaa/fheq-2024/annex-d/summary/r1/3rd for the threshold class). Set it beside qaa/osteopathy-2024/6.1 and the 6.10 list, and do not claim the statement itself defines typical or excellent rungs."
  author-agent-dialogue: "Raise it when a team sets classification criteria or a student asks how a first differs from a pass. With staff, frame it as the provider's own judgement, anchored in Annex D; with a student, explain only that the 6.10 list is the floor and that classes above it are described elsewhere. Ask how the course's marking criteria line up with Annex D's descriptions. Avoid treating the classification descriptions as part of this statement."
- statement: qaa/osteopathy-2024/6.6
  forPractitioner: { text: "Students develop critical engagement with research, clinical experience and patient expectations; they are expected to judge the clinical relevance of published research and to conduct audit, service evaluation and research that improve practice and care.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will build the skills to weigh research, clinical experience and what patients expect, and you are expected to judge how relevant published research is and to take part in audit and research that improves care.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as an expectation the issuer words as 'are expected to', outside the five force words and recorded as describes (Part E): students judge the relevance of research and conduct audit, service evaluation and research, at FHEQ level 6 for the honours award. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.6. Set it beside the threshold standard qaa/osteopathy-2024/6.10.b11, the outcomes 3.6.a.viii and 3.6.k.ix and the level 6 descriptor qaa/fheq-2024/4.15.b3.2, and do not write it up as a must."
  author-agent-dialogue: "Raise it when a student plans an audit or research project or asks how research fits clinical work. Tell a student plainly that you are expected to weigh research, experience and what patients want, and to help improve care through audit and research; for staff, frame it as the expectation behind research teaching. Ask which recent study has changed, or should change, how the person treats patients. Avoid presenting it as a requirement to publish."
- statement: qaa/osteopathy-2024/6.8
  forPractitioner: { text: "Courses gain and keep Recognised Qualification status from the GOsC through regular review, which requires following its graduate outcomes and education standards (September 2022) and delivering the OPS effectively; graduates and registrants must meet the OPS throughout their careers.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Throughout your career, from graduation onwards, you must meet the regulator's professional practice standards; your course is approved and regularly reviewed to make sure it prepares you for this.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a requirement (required, recorded as must) reported from the regulator's system: courses hold Recognised Qualification status under regular review, and graduates and registrants must meet the OPS throughout their careers. It is not a level outcome. Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.8, and the regulator's documents for the standards. Set it beside qaa/osteopathy-2024/1.5, 5.1 and 6.9, and do not claim that the statement's own standards are the regulator's approval criteria."
  author-agent-dialogue: "Raise it when a student asks what happens after graduation or a team prepares for regulatory review. Tell a student plainly that you must keep meeting the professional standards for as long as you practise; for staff, frame it as the condition of the course's recognition. Ask whether the person knows how the standards will apply to them in their first year of practice. Avoid reading the standards aloud or confusing course approval with the student's own registration."
- statement: qaa/osteopathy-2024/6.10.b1
  forPractitioner: { text: "At threshold, graduates will have developed highly effective interpersonal and communication skills for professional, ethical dealings with diverse patients, peers and other health professionals.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for the award, you will have developed strong people and communication skills, so that you deal professionally, ethically and effectively with a wide range of patients, fellow students and other health professionals.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (interpersonal and communication skills). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.10, bullet 1. Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). Set it beside the outcomes qaa/osteopathy-2024/3.6.d.i and 3.6.d.ii and the level 6 descriptor qaa/fheq-2024/4.15.b8 (spine:6)."
  author-agent-dialogue: "Raise it when a student asks how well they need to communicate to pass, or a team sets communication assessment. With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. Ask: Where have you had to communicate with a patient or professional whose needs were unlike your own? Do not quote the bullet at length or present the higher classification descriptions as the minimum."
- statement: qaa/osteopathy-2024/6.10.b2
  forPractitioner: { text: "At threshold, graduates will have shown critical understanding of osteopathy's philosophy and principles and how these can guide rational clinical decisions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will understand the philosophy and principles of osteopathy critically and how they can guide sound clinical decisions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (osteopathic philosophy and principles in decisions). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.10, bullet 2. Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). Set it beside the outcomes qaa/osteopathy-2024/3.6.b.i and 3.6.b.iv and the level 6 descriptor qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when osteopathic principles are being tied to clinical decisions. With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. Ask: Can you show how an osteopathic principle led you to a clinical decision you could defend? Do not quote the bullet at length or present the higher classification descriptions as the minimum."
- statement: qaa/osteopathy-2024/6.10.b3
  forPractitioner: { text: "At threshold, graduates will have coherent, detailed knowledge of the interplay of biological, physical and behavioural sciences that underpin practice, and of their clinical use across the lifespan.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will have a clear, detailed understanding of how the biological, physical and behavioural sciences behind osteopathy link together and apply to patients at every stage of life.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (the sciences underpinning practice across the lifespan). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.10, bullet 3. Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). Set it beside the outcomes qaa/osteopathy-2024/3.6.a.i to 3.6.a.iv and the level 6 descriptor qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a team checks the science base of the course or a student asks how much science is enough. With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. Ask: How would you explain a patient's problem using more than one of the biological, physical and behavioural sciences? Do not quote the bullet at length or present the higher classification descriptions as the minimum."
- statement: qaa/osteopathy-2024/6.10.b4
  forPractitioner: { text: "At threshold, graduates will be able to assess a patient safely and effectively, reach a working diagnosis and agree a treatment plan through shared decision-making that respects the person's physical, psychosocial, cultural and diversity needs and their values and preferences.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to assess a patient safely and effectively, reach a working diagnosis and agree a treatment plan with them that takes account of their whole situation, values and wishes.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (safe assessment, working diagnosis and shared planning). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.10, bullet 4. Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). Set it beside the outcomes qaa/osteopathy-2024/3.6.e.i to 3.6.e.v and 3.6.g.iv and the level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when a student prepares for a clinical assessment or a team designs one. With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. Ask: Talk me through how you reached a working diagnosis and agreed a plan with your last new patient. Do not quote the bullet at length or present the higher classification descriptions as the minimum."
- statement: qaa/osteopathy-2024/6.10.b5
  forPractitioner: { text: "At threshold, graduates will assess critically, using problem-solving and clinical reasoning drawn from their knowledge, including incomplete, complex or unpredictable areas, to plan treatment and management.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will approach assessment critically, using problem-solving and clinical reasoning, even where what you know is incomplete or the picture is complex, to plan treatment.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (critical clinical reasoning with incomplete knowledge). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.10, bullet 5. Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). Set it beside the outcomes qaa/osteopathy-2024/3.6.g.i, 3.6.g.ii and 3.6.k.v and the level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when a student meets a case that does not fit what they were taught. With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. Ask: What did you do when your knowledge ran out in a recent case? Do not quote the bullet at length or present the higher classification descriptions as the minimum."
- statement: qaa/osteopathy-2024/6.10.b6
  forPractitioner: { text: "At threshold, graduates will critically select, apply and justify treatment for the individual, monitor and evaluate its effect across the plan and guide and educate the patient to support progress.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to choose, carry out and justify treatment that suits each patient, check and judge how well it is working and guide and teach the patient to help them progress.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (selecting, applying and evaluating treatment). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.10, bullet 6. Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). Set it beside the outcomes qaa/osteopathy-2024/3.6.h.i to 3.6.h.iv and 3.6.i.i to 3.6.i.iv and the level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when treatment choice and monitoring are assessed or discussed. With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. Ask: How do you know whether the treatment you chose for a patient is working? Do not quote the bullet at length or present the higher classification descriptions as the minimum."
- statement: qaa/osteopathy-2024/6.10.b7
  forPractitioner: { text: "At threshold, graduates will appreciate osteopathy's value for well-being over the lifespan and in changing public health contexts, including palliative and supportive care for lifelong illness or disability.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will appreciate how osteopathy can support people's well-being throughout life and as public health needs change, including helping people who live with long-term illness or disability.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (supporting well-being across the lifespan, including long-term illness). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.10, bullet 7. Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). Set it beside the outcomes qaa/osteopathy-2024/3.6.j.i to 3.6.j.iv and the level 6 descriptor qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student wonders what osteopathy offers someone who will not get better. With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. Ask: What could you offer a patient whose condition is lifelong? Do not quote the bullet at length or present the higher classification descriptions as the minimum."
- statement: qaa/osteopathy-2024/6.10.b8
  forPractitioner: { text: "At threshold, graduates will understand osteopathy's distinctive approach well enough to collaborate effectively with other professions for the best patient and population outcomes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will understand what makes osteopathy distinctive, so you can work well with other health professions for the best results for patients and communities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (osteopathy's distinctiveness for collaboration). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.10, bullet 8. Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). Set it beside the outcomes qaa/osteopathy-2024/3.6.m.i, 3.6.m.ii and 3.6.b.iii and the level 6 descriptor qaa/fheq-2024/4.15.b8 (spine:6)."
  author-agent-dialogue: "Raise it when working with other professions or referral pathways comes up. With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. Ask: How would you explain what osteopathy adds to a GP or physiotherapist you were working with? Do not quote the bullet at length or present the higher classification descriptions as the minimum."
- statement: qaa/osteopathy-2024/6.10.b9
  forPractitioner: { text: "At threshold, graduates will know the limits of their competence across practice, education and research and respond by seeking CPD, mentoring or shadowing, or by referring on.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will know the limits of your own skills, knowledge and experience, and respond by seeking more training, mentoring or shadowing, or by referring the patient to someone better placed.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (knowing the limits of one's own competence). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.10, bullet 9. Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). Set it beside the outcomes qaa/osteopathy-2024/3.6.k.ii, 3.6.j.vi and 3.4.b6 and the level 6 descriptor qaa/fheq-2024/4.15.b4 (spine:6)."
  author-agent-dialogue: "Raise it when a student is unsure whether to treat or refer, or plans their next learning. With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. Ask: Where are the edges of your competence right now, and what do you do when a patient takes you there? Do not quote the bullet at length or present the higher classification descriptions as the minimum."
- statement: qaa/osteopathy-2024/6.10.b10
  forPractitioner: { text: "At threshold, graduates will show commitment to ongoing self-directed professional learning that informs practice, monitors and improves care quality and draws on current advice and research.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be committed to directing your own learning throughout your career, using current advice and research to keep improving the care you give.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (self-directed professional learning). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.10, bullet 10. Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). Set it beside the outcomes qaa/osteopathy-2024/3.6.k.i, 3.6.k.iii and 3.6.k.iv and the level 6 descriptor qaa/fheq-2024/4.15.b9.3 (spine:6)."
  author-agent-dialogue: "Raise it when a student plans continuing development or a team designs reflective assessment. With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. Ask: What have you changed in your practice because of something you chose to learn? Do not quote the bullet at length or present the higher classification descriptions as the minimum."
- statement: qaa/osteopathy-2024/6.10.b11
  forPractitioner: { text: "At threshold, graduates will apply relevant research, clinical experience and patient expectations to support and critically evaluate evidence-informed practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will combine research, clinical experience and what patients expect to judge and improve the care you give, critically and on good evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (evidence-informed practice). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.10, bullet 11. Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). Set it beside the outcomes qaa/osteopathy-2024/3.6.a.viii, 3.6.k.ix and 6.6 and the level 6 descriptor qaa/fheq-2024/4.15.b3.2 (spine:6)."
  author-agent-dialogue: "Raise it when research use or evidence-informed practice is assessed or discussed. With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. Ask: How did research, your experience and the patient's wishes each shape a recent decision? Do not quote the bullet at length or present the higher classification descriptions as the minimum."
- statement: qaa/osteopathy-2024/6.10.b12
  forPractitioner: { text: "At threshold, graduates will critically evaluate their own professional integrity, attending to probity, respect, self-care and the duty of candour.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to judge your own professional integrity critically, paying attention to honesty, respect, looking after yourself and being open when things go wrong.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (professional integrity, probity and candour). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.10, bullet 12. Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). Set it beside the outcomes qaa/osteopathy-2024/3.6.l.vii, 3.6.c.iv and 3.6.c.vii and the level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when professional integrity, honesty or a mistake is discussed. With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. Ask: When did you last have to be open with a patient or tutor about something that went wrong? Do not quote the bullet at length or present the higher classification descriptions as the minimum."
- statement: qaa/osteopathy-2024/6.10.b13
  forPractitioner: { text: "At threshold, graduates will make decisions in unfamiliar, complex and unpredictable professional settings, showing leadership, resilience, commitment and accountability.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to make decisions in situations that are new, complex or unpredictable, showing leadership, resilience, commitment and accountability.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (decisions in complex, unpredictable situations). Cite it as QAA, 2024, Osteopathy Subject Benchmark Statement, para 6.10, bullet 13. Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). Set it beside the outcomes qaa/osteopathy-2024/3.6.c.iv and 3.6.n.iv and the level 6 descriptor qaa/fheq-2024/4.15.b9.2 (and, for integrated master's, qaa/fheq-2024/4.17.b5) (spine:6)."
  author-agent-dialogue: "Raise it when a student faces an unfamiliar or uncertain clinical situation. With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. Ask: Describe a decision you made without all the information: what did you weigh, and who did you tell? Do not quote the bullet at length or present the higher classification descriptions as the minimum."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.7; 2.8; 6.9", note: "bachelor's (Level 6); the descriptors are cited as the FHEQ's degree-level qualification descriptors" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.8; 6.9", note: "integrated master's and pre-registration master's (Level 7)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 6.9", note: "\"Level 11 of the Scottish Credit and Qualifications Framework\" on the FQHEIS" }
  - { id: "fqheis:10", role: "inferred", locator: "not named; the FQHEIS honours level beside fheq:6 (std:doc:qaa-fheq-2024-framework, Table 1)", note: "Part E" }
crosswalks:
  - { from: "fheq:7", to: "fqheis:11", relation: "shared-descriptor", basis: "inferred: the statement names both at 6.9 but states no equivalence; the FHEQ document gives one descriptor for both (std:doc:qaa-fheq-2024-framework, 4.8, 4.17)" }
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "inferred from std:doc:qaa-fheq-2024-framework, Table 1 (honours); the statement names no SCQF level 10 (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["front matter", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "1.19", "3.6", "4.2", "4.4", "6.10"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["front matter", "1.20", "1.21", "1.22", "1.33"] }
- { id: "theme:esd", role: "carries", carriedIn: ["front matter", "1.23", "1.24", "1.25", "4.2"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["front matter", "1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "3.6"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-osteopathy-<previous year>-benchmarks (not yet ingested)", note: "the text calls this the fifth edition and dates the third 2019, the second 2014 and the original 2007; the fourth is not dated: Part E" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "degree classification descriptions for achievement above the threshold (6.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "degree-level qualification descriptors (2.7); Levels 6 and 7 (2.8, 6.9)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "named at 2.7 and 6.9; SCQF Level 11 (6.9)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "\"the QAA and Advance HE guidance\" on education for sustainable development (1.25)" }
- { rel: "refersTo", target: "GOsC Osteopathic Practice Standards (not yet ingested: Part E)", note: "1.5, 3.2, 3.5, 3.6 l) ii, 4.1, 5.1 to 5.4, 6.4, 6.8" }
- { rel: "refersTo", target: "GOsC Graduate Outcomes and Standards for Education and Training, September 2022 (not yet ingested: Part E)", note: "1.5, 2.1, 3.5, 4.1, 4.4, 6.8" }
- { rel: "refersTo", target: "QAA Quality Code for Higher Education and its Advice and Guidance (not yet ingested)", note: "front matter; 2.3" }
- { rel: "refersTo", target: "CEN European Standard on Osteopathic Healthcare Provision (not ingested)", note: "1.10" }
- { rel: "refersTo", target: "Office for Students sector-recognised standards (not ingested)", note: "front matter; 6.9" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2024-04"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "an Advisory Group chaired from NCOR, with GOsC, QAA, the Osteopathic Alliance, the Institute of Osteopathy, the Council for Osteopathic Education Institutions and providers (D1, section 8)"
replacedBy: "none"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- A primary healthcare profession that diagnoses, manages, treats and prevents a range of disorders, and an Allied Health Profession in England (D1, 1.1, 1.3).
- Care centres on the person, not the condition, and supports the body's own capacity to keep and restore health, with biopsychosocial factors always in view (D1, 1.12, 6.3).
- Its methods combine person-centred tools, hands-on technique, palpation, rehabilitation exercise and self-help advice, with diagnosis built from case history and examination and guided by clinical reasoning (D1, 1.2, 1.12, 6.5).
- It is a regulated profession: only those registered with the General Osteopathic Council may practise or use the title, and graduates may practise autonomously from registration (D1, 1.5, 1.6).
- Training joins academic study with extensive supervised clinical work in teaching clinics, at least 1,000 hours (D1, 1.4, 2.4, 6.4).
- It is evidence-informed and self-critical, weighing research, clinical experience and patient expectations and appraising its own claims (D1, 1.9, 6.6, 3.6 d) iv, 3.6 m) iii).
- Most osteopaths are self-employed, so business, enterprise and practice management sit inside the curriculum (D1, 1.7, 1.26 to 1.39, 3.6 n)).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "framed as a collective responsibility of an inclusive learning community that reaches past legal minimums: critical theory and decolonial perspectives across the curriculum, anticipatory design for each learning site (technique class, clinic, online), care for self and others and questions for reviewing a course; in practice, attention to protected characteristics, socioeconomic status and diverse patient groups (D1, 1.13 to 1.19, 3.6 e) vi, 4.4, 6.10)"
  statements: ["qaa/osteopathy-2024/1.13", "qaa/osteopathy-2024/1.14", "qaa/osteopathy-2024/1.15", "qaa/osteopathy-2024/1.16", "qaa/osteopathy-2024/1.17", "qaa/osteopathy-2024/1.18", "qaa/osteopathy-2024/3.6.e.vi", "qaa/osteopathy-2024/3.6.l.iii", "qaa/osteopathy-2024/6.10.b4"]
- theme: theme:accessibility
  inThisSubject: "part-time and full-time modes, blended and recorded delivery and reasonable adjustments, always bounded by the regulation that protects patient safety in clinic (D1, 1.20 to 1.22); accessible communication with digital tools (D1, 1.33)"
  statements: ["qaa/osteopathy-2024/1.22", "qaa/osteopathy-2024/1.33"]
- theme: theme:esd
  inThisSubject: "whole-person training, critical study of the profession's structures and discourses, the eight UNESCO competencies modelled in facilities and curricula and personal and social responsibility for well-being (D1, 1.23 to 1.25); sustainable delivery of teaching (D1, 4.2)"
  statements: ["qaa/osteopathy-2024/1.24", "qaa/osteopathy-2024/1.25", "qaa/osteopathy-2024/4.2"]
- theme: theme:enterprise
  inThisSubject: "named employability, enterprise and entrepreneurship education (EEE): most osteopaths are self-employed, so the entrepreneurial mindset, career planning, marketing, legal and financial skills, external speakers and clinic placements prepare graduates for private practice (D1, 1.26 to 1.39); a viable business that puts patients before profit (D1, 3.6 n) v)"
  statements: ["qaa/osteopathy-2024/1.27", "qaa/osteopathy-2024/1.33", "qaa/osteopathy-2024/1.34", "qaa/osteopathy-2024/1.35", "qaa/osteopathy-2024/3.6.n.v"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.1", gloss: "the broad curriculum: cognitive and perceptual learning, manual and palpatory skills, generic skills, problem-solving, reflective practice, ICT, practice management and leadership, research and critical reasoning" }
  - { component: "3.6", gloss: "fourteen outcome groups from the knowledge base (a) to running a practice (n); also the stem of 83 statements" }
  - { component: "6.5", gloss: "anatomy, biomechanics, physiology, pathology and behavioural sciences as the foundation for assessment and management" }
practices:
  - { component: "2.2", kind: "teaching", gloss: "evidence-based pedagogy; feed-forward feedback and self-assessment" }
  - { component: "2.4", kind: "learning", gloss: "technical skill integrated with closely supervised outpatient clinical work" }
  - { component: "4.3", kind: "teaching", gloss: "innovative, research-informed methods chosen by each institution" }
  - { component: "4.4", kind: "learning", gloss: "supervised clinical learning in institutional and satellite clinics across diverse patient groups" }
  - { component: "1.36", kind: "assessment", gloss: "assignments on contemporary practice, marketing and the law of private practice" }
  - { component: "1.38", kind: "learning", gloss: "supervised clinic placements as a bridge to an entrepreneurial mindset" }
  - { component: "5.3", kind: "assessment", gloss: "varied, valid and reliable tools; formative and summative assessment with peers, patients and external expertise" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "6.10", award: "bachelor's with honours", items: 13 }
rungBases: "6.1 defines the 6.10 list as the minimum threshold standards for an honours degree; 6.2 says most students perform significantly better and leaves the evidence of this to each provider with reference to Annex D. No typical or excellent lists."
outcomeLists:
  - { leadIn: "3.4", gloss: "six key characteristics a graduate can demonstrate", items: 6, award: ["bachelor's with honours", "integrated master's"] }
  - { leadIn: "3.6", gloss: "83 outcomes in fourteen lettered groups, developed on successful completion", items: 83, award: ["bachelor's with honours", "integrated master's"] }
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
- { body: "General Osteopathic Council (GOsC)", says: "the statutory regulator: only its registrants may practise or use the title; it recognises qualifications (Recognised Qualification status, reviewed regularly), which must deliver its Osteopathic Practice Standards and align with its Graduate Outcomes and Standards for Education and Training; graduates and registrants must meet the OPS throughout their careers (D1, 1.5, 1.6, 2.1, 3.5, 3.6 l) ii, 4.1, 6.8, 6.9)", requirements: "not yet ingested: the OPS and GO-SET (Part E; D3)" }
- { body: "Professional Standards Authority", says: "oversees the GOsC and nine other health regulators (D1, 1.5)", requirements: "not-applicable-by-design: named only as the regulator's overseer" }
- { body: "Privy Council", says: "approves the qualifications the GOsC recognises (D1, 1.5)", requirements: "not-applicable-by-design: approval role only" }
- { body: "National Council for Osteopathic Research (NCOR)", says: "works to strengthen the evidence base and research capacity of the profession (D1, 1.9); chairs the advisory group (D1, section 8)", requirements: "not-applicable-by-design: sets no requirements on courses" }
- { body: "National Institute for Health and Care Excellence (NICE)", says: "its low back pain guideline (NG59) is among the independent assessments that include osteopathy (D1, 1.8; the text gives its older name)", requirements: "not-applicable-by-design: clinical guidance, not a course requirement" }
- { body: "European Committee for Standardisation (CEN)", says: "publishes a European Standard on Osteopathic Healthcare Provision for countries without regulation (D1, 1.10)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion (front matter: equality, diversity, and inclusion)", carriedIn: ["front matter", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "1.19", "3.6", "4.2", "4.4", "6.10"], statements: ["qaa/osteopathy-2024/1.13", "qaa/osteopathy-2024/1.14", "qaa/osteopathy-2024/1.15", "qaa/osteopathy-2024/1.16", "qaa/osteopathy-2024/1.17", "qaa/osteopathy-2024/1.18", "qaa/osteopathy-2024/3.6.e.vi", "qaa/osteopathy-2024/3.6.l.iii", "qaa/osteopathy-2024/6.10.b4"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["front matter", "1.20", "1.21", "1.22", "1.33"], statements: ["qaa/osteopathy-2024/1.22", "qaa/osteopathy-2024/1.33"] }
  - { id: "theme:esd", named: "Education for Sustainable Development (ESD)", carriedIn: ["front matter", "1.23", "1.24", "1.25", "4.2"], statements: ["qaa/osteopathy-2024/1.24", "qaa/osteopathy-2024/1.25", "qaa/osteopathy-2024/4.2"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (front matter: employability, entrepreneurship, and enterprise education; EEE at 1.29)", carriedIn: ["front matter", "1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "3.6"], statements: ["qaa/osteopathy-2024/1.27", "qaa/osteopathy-2024/1.33", "qaa/osteopathy-2024/1.34", "qaa/osteopathy-2024/1.35", "qaa/osteopathy-2024/3.6.n.v"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.7", "2.8", "6.9"] }
  - { framework: "scqf", levels: ["fqheis:11"], citedIn: ["2.7", "6.9"] }
  - { framework: "other: Office for Students sector-recognised standards", levels: [], citedIn: ["front matter", "6.9"] }
bodies:
  - { body: "General Osteopathic Council", citedIn: ["1.5", "1.6", "2.1", "3.5", "3.6", "4.1", "6.8", "6.9"] }
  - { body: "Professional Standards Authority", citedIn: ["1.5"] }
  - { body: "Privy Council", citedIn: ["1.5"] }
  - { body: "National Council for Osteopathic Research", citedIn: ["1.9"] }
  - { body: "National Institute for Health and Clinical Excellence (NICE)", citedIn: ["1.8"] }
  - { body: "European Committee for Standardisation (CEN)", citedIn: ["1.10"] }
  - { body: "PSRBs (generic)", citedIn: ["front matter"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["6.2"], role: "how each provider evidences achievement above the threshold" }
  - { document: "std:doc:qaa-fheq-2024-framework", named: "the degree-level qualification descriptors in the FHEQ; Qualifications Frameworks", citedIn: ["2.7", "6.9"], role: "the levels training reflects and the capabilities map to" }
  - { document: "std:doc:qaa-fqheis-2024-framework", named: "the Framework for Qualifications of Higher Education Institutions in Scotland", citedIn: ["2.7", "6.9"], role: "the Scottish framework, Level 11 named" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "the QAA and Advance HE guidance", citedIn: ["1.25"], role: "more information on education for sustainable development" }
  - { document: "QAA Quality Code for Higher Education and Advice and Guidance (not yet ingested: Part E)", named: "Quality Code; Advice and Guidance", citedIn: ["front matter", "2.3"], role: "course design and progressive levels" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "recognised-qualification", definition: "a qualification the regulator recognises, with Privy Council approval, as leading to registration; it must deliver the OPS and is reviewed regularly (D1, 1.5, 6.8)", beneficiaryDefinition: "a course the regulator has approved, which you need to complete before you can register", scopeNote: "the regulator's term; abbreviated RQ", category: "unknown", practices: ["healthcare education"] }
- { slug: "osteopathic-practice-standards", definition: "the regulator's professional standards, in four themes, that registrants must meet and courses must deliver (D1, 1.5, 6.4, 6.8)", beneficiaryDefinition: "the standards you will have to meet as a registered osteopath", scopeNote: "abbreviated OPS; a separate document, not ingested", category: "unknown", practices: ["healthcare education"] }
- { slug: "evidence-informed-practice", definition: "practice drawing on three parts: clinical experience, research and patient expectations (D1, 6.6)", beneficiaryDefinition: "practice that weighs research, your experience and what the patient wants", scopeNote: "", category: "unknown", practices: ["healthcare"] }
- { slug: "employability-enterprise-entrepreneurship-education", definition: "education for the behaviours, attributes and competencies of employed or self-employed practice (D1, 1.29 to 1.32)", beneficiaryDefinition: "learning that prepares you for work, including running your own practice", scopeNote: "abbreviated EEE", category: "unknown", practices: ["education"] }
- { slug: "anticipatory-design", definition: "design of teaching and practice that plans ahead for the needs of each learning site and those it has served badly (D1, 1.17, 1.18)", beneficiaryDefinition: "courses planned in advance so that everyone can take part", scopeNote: "", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "recognised-qualification", form: "Recognised Qualification (RQ)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "osteopathic-practice-standards", form: "Osteopathic Practice Standards (OPS)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "evidence-informed-practice", form: "evidence-informed practice", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "employability-enterprise-entrepreneurship-education", form: "employability, enterprise, and entrepreneurship education (EEE)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "anticipatory-design", form: "anticipatory design", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Osteopathy"
  edition: "April 2024 (fifth edition)"
  year: 2024
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/osteopathy-2024/osteopathy-2024.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: dc11b8bca50a250cf49ea4d936ebb9b0ad011096993b0f82a0f107ee823dd3fb
  heldFiles: ["wkspc2601-library/txt/qaa-2024-osteopathy-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2024-osteopathy-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2024-osteopathy-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2024-osteopathy-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0088", source: "General Osteopathic Council, Osteopathic Practice Standards (current edition)", why: "the standards every Recognised Qualification must deliver; cited throughout (1.5, 5.1, 6.8)" }
- { w: "W-std-0089", source: "General Osteopathic Council, Graduate Outcomes and Standards for Education and Training (September 2022)", why: "the regulator's graduate outcomes the 3.6 outcomes are designed to show (3.5, 6.8)" }
- { w: "W-std-0090", source: "QAA, Subject Benchmark Statement: Osteopathy, previous edition", why: "the edition this one supersedes; the text does not name or date it" }
```

## Part E Gaps and questions
- Rungs: one rung only. 6.10 lists 13 threshold standards for the honours degree; 6.1 calls them the minimum threshold; 6.2 leaves higher achievement to each provider and Annex D (std:doc:qaa-fheq-2024-framework). No typical or excellent lists, so no gradeOf links (as Archaeology).
- Pattern: the threshold lead-in (6.10) is "To be awarded an honours degree in Osteopathy, a student will have demonstrated:"; force recorded as threshold, with forceFrom 6.1, which defines the list as the minimum.
- Pattern: two outcome lists outside the rungs: 3.4 (six key characteristics, lead-in "can demonstrate", recorded as will; for P3) and 3.6 (83 outcomes in fourteen lettered groups a) to n), lead-in "will have developed").
- Skeleton correction: 3.6 is flattened in the held text (lettered groups with roman-numbered items run into one paragraph). The skeleton cut it into 12 wrong items (3.6.b1 to 3.6.b12); this run cuts 83 items by find, with ids 3.6.<letter>.<roman> in the issuer's numbering. Placements are by the markers a) to n) and i to ix; all 83 texts are unique in the held text. For P3: the builder reads only numeric ids, so these 83 records sort after section 6 and show stem none and a blank sub-heading; their stem is 3.6 and their group heading is the letter's (a) to n)).
- Skeleton correction: 6.10.b7 crosses a page break; its span is extended by find to the end of the bullet, page number 22 included in source. 3.6 d) v and l) iv each hold an unnumbered dash list, kept inside the one record; l) iv crosses page break 17.
- Skeleton correction: paragraph spans trimmed by find to drop trailing page numbers and the flattened sub-headings that follow 1.22 ("Education for Sustainable Development (ESD)") and 1.25 ("Enterprise and entrepreneurship education"). Other sub-headings sit at the end of 1.4, 1.10, 1.12, 2.6, 3.3 and 6.9 (not statements).
- Awards: the statement covers pre-registration courses at bachelor's (Level 6) and integrated master's (Level 7), and names pre-registration master's (Level 7) at 2.8; the outcome lists are not split by award. Outcome records carry both awards at level fheq:6; the threshold list is for the honours degree (fheq:6). Whether integrated master's needs fheq:7 records is for P3. No master's column, so no .masters ids.
- Levels: 6.9 names SCQF "Level 11" on the FQHEIS but not SCQF 10, the honours level beside FHEQ 6. fqheis:10 and both crosswalks in S5 are inferred from std:doc:qaa-fheq-2024-framework (Table 1; 4.8 and 4.17). The CQFW is not named, though the statement applies in Wales.
- Force, outside the five: 1.6 ("it is critical that"; "requires") recorded as must; 1.18 and 1.24 ("requires") recorded as must; 6.8 ("required") recorded as must; 1.35 ("is recommended") recorded as describes; 6.6 ("are expected to") recorded as describes; 1.13 ("will need to"; "responsibility and duty") recorded as will. For Abbott.
- Force, mixed in one paragraph: 1.14 has should (foster) and must (acknowledge and counter), recorded as must; 1.5 has must and should, recorded as must; 2.3 has should with "essential" and "required", recorded as should; 2.5 has "it is important that" and should, recorded as should; 5.1 and 5.4 have should with a will or a plain condition, recorded as should.
- Plain-present provider norms, not statements (template open point 5): 1.4, 2.2, 2.4, 3.1 (the curriculum "include"s eight areas), 4.1, 4.3, 4.4 and 6.4 (courses integrate "at least 1,000 hours of supervised clinical practice"), 6.5, 6.7. 6.4 also says graduates "understand and can demonstrate" the OPS themes in plain present. For P3: 6.4's 1,000 hours is the one quantified course requirement in the text.
- Not statements: 1.12 bullets 2 to 7 (features of practice, descriptive; bullet 1 has should and is a statement); 1.19 (review questions); 1.28 (the entrepreneurial mindset defined); 1.30 to 1.32 ("can include"); 1.23, 1.29, 1.36, 1.39 (will in a descriptive or predictive sense); 6.1 (the rung definition, in SB4 rungBases); 6.9 (level mapping).
- Codes: HECoS 100243 osteopathy is stated by subject name. CAH02-06-06 (complementary and alternative medicine), CAH02-06 and CAH02 are inferred from HECoS's own mapping; the text calls osteopathy an Allied Health Profession (1.1) and never complementary or alternative. For P3.
- Themes: ESD skeleton hits at 1.22 (the flattened heading) and 6.4 ("sustainability and development of practice life", a business sense) are not ESD and are not cited. 4.2 ("sustainable and inclusive way") is cited for ESD and EDI. Accessibility at 1.33 ("accessibly") and EDI at 3.6, 4.4 and 6.10 are cited by what the paragraph says.
- Bodies: the GOsC's OPS and GO-SET (September 2022) are not ingested (D3). CEN's European Standard is not ingested. 1.8 names NICE by an older name ("National Institute for Health and Clinical Excellence").
- Shared documents: the Quality Code and its Advice and Guidance (front matter, 2.3) are not ingested. Legislation named (Osteopaths Act 1993 at 1.5; Equality Act 2010 at 1.13) is recorded only in the statements that carry it.
- Supersedes: the back matter calls this the fifth edition and dates the third (2019), the second (2014, by membership) and the original (2007); the fourth edition is not dated. The edition superseded is not named.
- Typos in the held text, left as held: "Versus Arthtritis" (1.16), "make decision" (6.10 b13), "ones' own" (6.10 b12), "A bout" and "O steopathy" from extraction.
- Generic-skill records carry fheq:6, the level they refine (S5); their aaw points to the matching FHEQ 4.15 item and spine:6. For integrated master's, the 4.17 items are the counterpart (named at 6.10.b13 only).
- S9 commentary not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:11: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0123 (P1); built by tools/bm_build.py.
