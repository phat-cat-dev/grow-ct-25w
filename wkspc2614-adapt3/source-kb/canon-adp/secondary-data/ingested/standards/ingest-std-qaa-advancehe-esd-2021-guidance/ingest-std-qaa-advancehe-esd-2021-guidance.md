---
id: std:doc:qaa-advancehe-esd-2021-guidance
title: "Education for Sustainable Development Guidance"
profile: standards/guidance   # proposed variant (D-std-0011, P5b); not yet in the profile
profileVersion: 0.1.6-draft
issuer: The Quality Assurance Agency for Higher Education (QAA) and Advance HE
kind: guidance
theme: theme:esd
jurisdiction: [England, Wales, Scotland, Northern Ireland]
subjectScope: universal
subjects: []
edition: March 2021 (second edition)
published: 2021-03
status: current   # as at the held text; not checked against either issuer's site (Part E)
supersedes: "QAA and HEA, Education for Sustainable Development: Guidance for UK Higher Education Providers (2014)"
heldText: { method: sha256-bytes, raw: 4193716f88575729a92da292eac62d282789f4a9fd5741db2335f75f84140c41, normalised: 354c816b51112367b96be4b0b260362332b7b7db71cc932ecc865bfae734963e }
original: { method: sha256-bytes, pdf: 9463b40b98309b37fca334cda8ad2c755f857bdafe8e6c8c17e9d2aa0fcff3d2, held: no }
licence: none read yet
parts:
  S: "full: 207 statements in thirteen families, 128 of them Table 2's learning outcomes"
  GU: "guidance analysis: families, progression and a verb-level profile of the outcomes, employability, framework and criteria links, pathways, the benchmark web, the crosswalk to the enterprise guidance, pedagogy handed on"
  B: "the guidance's defined terms"
  C: "none"
pins: { structure: 0.13.0-draft, template: "guidance 0.1.0-draft (proposed)", runFrame: 0.1.1-draft, runLayer: 0.5.0-draft }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0063
passes:
  P1: "2026-10-03, std (claude.ai, META Project): read direct from Abbott's PDF of the full guidance (06:46); built 06:57"
  P2: "skipped: read direct from the issuers' PDF"
  P3: open
version: 0.2.1
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.6.1-draft under the proposed standards/guidance variant (template wpk-0016-ingest-pd-template-standards-guidance.md 0.1.0-draft), with the guidance analysis Part GU -->
# Education for Sustainable Development Guidance (QAA and Advance HE, 2021)

> Run 0063, P1 by std. **The full guidance** (Abbott, 06:46), read for its standards statements: what a student with each sustainability competency can do, know and value, and what the guidance asks of educators and providers so that students can. Its executive summary is a separate document, std:doc:qaa-advancehe-esd-2021-execsummary (variant `execsummary`). Teaching practices and the assessment model go to theory ingest (GU7). Every link to a framework statement, criterion, benchmark or pathway is our reading and marked `inferred`.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA and Advance HE's 2021 guidance on education for sustainable development, second edition: a cross-cutting theme for every subject. Reach for it to say what a student with each of the eight sustainability competencies can do (Table 1's short statements and Table 2's 128 learning outcomes, sorted into knowledge, skills and attributes and values), how learning outcomes for ESD should be written, what an institution, its academics and its services do to embed ESD, and how sustainability reaches the subject benchmarks (GU6). It sets no levels: it tells course designers to adapt its outcomes to the level and credit of each module.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Sustainable development is defined as a continuing process, aspirational in aim, that tackles social, environmental and economic concerns together; ESD as creating curriculum structures and subject content that support and enact it. The guidance takes the SDGs as the policy frame and UNESCO's eight key competencies as the core of learning, grouped as ways of thinking (systems, anticipatory, critical), ways of practising (strategic, collaborative, integrated problem-solving) and ways of being (self-awareness, normative). Table 2 gives indicative outcomes for each competency in three columns. Section 2 sets out who to involve (students, employers, academics, professional services, communities) with guidance for each; Section 3 adds learning environments, teaching practices and an assessment model (for, as and of learning).

## Part S Standard

### S1 Identity
```yaml
issuer: [The Quality Assurance Agency for Higher Education, Advance HE]
title: "Education for Sustainable Development Guidance"
edition: March 2021, second edition
dates: { published: 2021-03, other: ["first edition 2014 (QAA and HEA)", "executive summary: std:doc:qaa-advancehe-esd-2021-execsummary"] }
kind: guidance
chairs: "the ESD Advisory Group's co-chairs (named in the foreword)"
heldText: wkspc2601-library/txt/qaa-and-advance-he-2021-education-sustainable-development-guidance-standard.norm.txt
```

### S2 Purpose and scope
<!-- label: both; status: drafted; basis: primary -->
Mainly for staff who design, manage and teach courses; also for senior managers, quality staff, those directing teaching and staff running extracurricular activity. A reference point for designing, delivering and reviewing curricula, to be read beside the subject benchmark statements and QAA's Quality Code advice and guidance themes; also an advocacy aid. It has no regulatory function: following it does not by itself show compliance with any UK code or framework. It is deliberately not prescriptive about delivery.

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
Chairs' foreword; QAA and Advance HE preface; definitions of terms; introduction (context, audience, purpose, support). Section 1 (what ESD is; the role of higher education; the SDGs). Section 2 (getting started: institutional commitment and the five conditions; curriculum framing and Figure 2's strategic intersections; consulting key players: students, employers and enterprise, academics, professional services and governance, communities; each with guidance points and examples from practice). Section 3 (key competencies: Table 1; the competencies described by ways of thinking, practising and being; course and module learning outcomes; Table 2; learning environments; teaching and assessment guidance; Figure 3, assessment for, as and of learning; Table 3, teaching practices). Section 4 (annotated references and resources). Annex (the advisory group). Statements are cut from the aims, the five conditions, Tables 1 and 2, the competency descriptions, the outcome-design paragraphs, the guidance points and the learning-environment list. Tables are held linearised (D1).

### S4 Statements
<!-- label: both; status: drafted; basis: primary. One record per statement, cut at the issuer's own list items and sentences. Extra fields (guidance variant, proposed): `family` (GU1), `employability` (direct: names work, careers or ventures; bridge: a transferable capability employers value; academic: within study), `category` (behaviour, attribute, competency, literacy, awareness, mindset, capability, effectiveness, opportunity, assessment, educator, institution, aim, principle), `maps` (our reading: related framework statements, assessment criteria and academic practice pathways; all `inferred`). -->
```yaml
- id: qaa-advancehe/esd-2021/aim.1
  family: aim
  locator: { heading: "Aims: what ESD is about" }
  span: { start: 20313, end: 20438 }
  source: "Supporting students and staff to develop the knowledge, competencies and ability to pursue sustainable visions of the future."
  statementType: aim
  force: describes
  addressee: student
  employability: bridge
  verbs: [develop, pursue]
  maps: { pathways: [creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/aim.2
  family: aim
  locator: { heading: "Aims: what ESD is about" }
  span: { start: 20443, end: 20641 }
  source: "Supporting students and staff to appreciate the complexity of our world, the ‘wicked problems’ that continuously emerge, and how they can personally and professionally contribute to positive change."
  statementType: aim
  force: describes
  addressee: student
  employability: bridge
  verbs: [appreciate, contribute]
  maps: { framework: [qaa/fheq-2024/4.15.b4], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/aim.3
  family: aim
  locator: { heading: "Aims: what ESD is about" }
  span: { start: 20646, end: 20761 }
  source: "Challenging, supporting and enabling students and staff to co-design solutions and drive change for sustainability."
  statementType: aim
  force: describes
  addressee: student
  employability: bridge
  verbs: [co-design, drive]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [creativity, work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/aim.foreword
  family: aim
  locator: { heading: "Chairs' foreword" }
  span: { start: 1194, end: 1435 }
  source: "ensure that every graduate has not only the knowledge and skills but the attributes that will enable them at least to cope and ideally thrive in the face of the multiple challenges they will face across their life course in the 21st century."
  statementType: aim
  force: must
  addressee: provider
  employability: bridge
  verbs: [ensure, cope, thrive]
  maps: { framework: [qaa/fheq-2024/4.15.b9.2], pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/principle.b1
  family: principle
  locator: { heading: "Guidance: ESD is best achieved when" }
  span: { start: 26199, end: 26322 }
  source: "ESD objectives, targets and KPIs are part of the institution’s strategic priorities and subsequent strategies and policies."
  statementType: institution
  force: describes
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/principle.b2
  family: principle
  locator: { heading: "Guidance: ESD is best achieved when" }
  span: { start: 26326, end: 26451 }
  source: "The framing of ESD within the curriculum is included in the validation of new courses and ongoing review of existing courses."
  statementType: institution
  force: describes
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/principle.b3
  family: principle
  locator: { heading: "Guidance: ESD is best achieved when" }
  span: { start: 26455, end: 26567 }
  source: "ESD is central to the staff and student induction process, as well as staff appraisal and/or promotion criteria."
  statementType: institution
  force: describes
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/principle.b4
  family: principle
  locator: { heading: "Guidance: ESD is best achieved when" }
  span: { start: 26571, end: 26641 }
  source: "ESD is articulated within quality assurance and enhancement processes."
  statementType: institution
  force: describes
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/principle.b5
  family: principle
  locator: { heading: "Guidance: ESD is best achieved when" }
  span: { start: 26645, end: 26722 }
  source: "Staff development to enable ESD is fully supported at an institutional level."
  statementType: institution
  force: describes
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/competency.systems.b1
  family: competency
  locator: { heading: "Table 1: systems thinking competency (ways of thinking)" }
  span: { start: 48357, end: 48395 }
  source: "recognise and understand relationships"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [recognise, understand]
  maps: { criteria: [bristol/generic-2024: critical-approach, cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.systems.b2
  family: competency
  locator: { heading: "Table 1: systems thinking competency (ways of thinking)" }
  span: { start: 48398, end: 48421 }
  source: "analyse complex systems"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [analyse]
  maps: { criteria: [bristol/generic-2024: critical-approach, cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.systems.b3
  family: competency
  locator: { heading: "Table 1: systems thinking competency (ways of thinking)" }
  span: { start: 48424, end: 48493 }
  source: "consider how systems are embedded within different domains and scales"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [consider]
  maps: { criteria: [bristol/generic-2024: critical-approach, cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.systems.b4
  family: competency
  locator: { heading: "Table 1: systems thinking competency (ways of thinking)" }
  span: { start: 48496, end: 48517 }
  source: "deal with uncertainty"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [deal]
  maps: { criteria: [bristol/generic-2024: critical-approach, cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.anticipatory.b1
  family: competency
  locator: { heading: "Table 1: anticipatory thinking competency (ways of thinking)" }
  span: { start: 48582, end: 48623 }
  source: "understand and evaluate multiple outcomes"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [understand, evaluate]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [creativity, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.anticipatory.b2
  family: competency
  locator: { heading: "Table 1: anticipatory thinking competency (ways of thinking)" }
  span: { start: 48626, end: 48665 }
  source: "create their own visions for the future"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [create]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [creativity, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.anticipatory.b3
  family: competency
  locator: { heading: "Table 1: anticipatory thinking competency (ways of thinking)" }
  span: { start: 48668, end: 48701 }
  source: "apply the precautionary principle"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [apply]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [creativity, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.anticipatory.b4
  family: competency
  locator: { heading: "Table 1: anticipatory thinking competency (ways of thinking)" }
  span: { start: 48704, end: 48738 }
  source: "assess the consequences of actions"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [assess]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [creativity, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.anticipatory.b5
  family: competency
  locator: { heading: "Table 1: anticipatory thinking competency (ways of thinking)" }
  span: { start: 48741, end: 48768 }
  source: "deal with risks and changes"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [deal]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [creativity, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.critical.b1
  family: competency
  locator: { heading: "Table 1: critical thinking competency (ways of thinking)" }
  span: { start: 48802, end: 48840 }
  source: "question norms, practices and opinions"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [question]
  maps: { criteria: [bristol/generic-2024: critical-approach, cardiffmet/generic-2020: argument], pathways: [criticality, reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.critical.b2
  family: competency
  locator: { heading: "Table 1: critical thinking competency (ways of thinking)" }
  span: { start: 48843, end: 48895 }
  source: "reflect on one’s own values, perceptions and actions"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [reflect]
  maps: { criteria: [bristol/generic-2024: critical-approach, cardiffmet/generic-2020: argument], pathways: [criticality, reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.critical.b3
  family: competency
  locator: { heading: "Table 1: critical thinking competency (ways of thinking)" }
  span: { start: 48898, end: 48954 }
  source: "take a position in the sustainable development discourse"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [take]
  maps: { criteria: [bristol/generic-2024: critical-approach, cardiffmet/generic-2020: argument], pathways: [criticality, reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.strategic.b1
  family: competency
  locator: { heading: "Table 1: strategic thinking competency (ways of practising)" }
  span: { start: 48980, end: 49097 }
  source: "develop and implement innovative actions that further sustainable\n• development at the local level and further afield"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [develop, implement]
  maps: { criteria: [bristol/generic-2024: decision-making, bristol/generic-2024: problem-solving], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.collaborative.b1
  family: competency
  locator: { heading: "Table 1: collaborative competency (ways of practising)" }
  span: { start: 49147, end: 49234 }
  source: "learn from others (including peers, and others inside and outside of their institution)"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [learn]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.collaborative.b2
  family: competency
  locator: { heading: "Table 1: collaborative competency (ways of practising)" }
  span: { start: 49237, end: 49305 }
  source: "understand and respect the needs, perspectives and actions of others"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [understand, respect]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.collaborative.b3
  family: competency
  locator: { heading: "Table 1: collaborative competency (ways of practising)" }
  span: { start: 49308, end: 49338 }
  source: "deal with conflicts in a group"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [deal]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.collaborative.b4
  family: competency
  locator: { heading: "Table 1: collaborative competency (ways of practising)" }
  span: { start: 49341, end: 49399 }
  source: "facilitate collaborative and participatory problem solving"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [facilitate]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.problem.b1
  family: competency
  locator: { heading: "Table 1: integrated problem-solving competency (ways of practising)" }
  span: { start: 49442, end: 49528 }
  source: "apply different problem-solving frameworks to complex sustainable development problems"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [apply]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [criticality, creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.problem.b2
  family: competency
  locator: { heading: "Table 1: integrated problem-solving competency (ways of practising)" }
  span: { start: 49531, end: 49580 }
  source: "develop viable, inclusive and equitable solutions"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [develop]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [criticality, creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.problem.b3
  family: competency
  locator: { heading: "Table 1: integrated problem-solving competency (ways of practising)" }
  span: { start: 49583, end: 49633 }
  source: "utilise appropriate competencies to solve problems"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [utilise, solve]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [criticality, creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.selfaware.b1
  family: competency
  locator: { heading: "Table 1: self-awareness competency (ways of being)" }
  span: { start: 52926, end: 52978 }
  source: "reflect on their own values, perceptions and actions"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [reflect]
  maps: { criteria: [bristol/generic-2024: insight, bristol/generic-2024: self-management], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.selfaware.b2
  family: competency
  locator: { heading: "Table 1: self-awareness competency (ways of being)" }
  span: { start: 52981, end: 53048 }
  source: "reflect on their own role in the local community and global society"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [reflect]
  maps: { criteria: [bristol/generic-2024: insight, bristol/generic-2024: self-management], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.selfaware.b3
  family: competency
  locator: { heading: "Table 1: self-awareness competency (ways of being)" }
  span: { start: 53051, end: 53106 }
  source: "continually evaluate and further motivate their actions"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [evaluate, motivate]
  maps: { criteria: [bristol/generic-2024: insight, bristol/generic-2024: self-management], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.selfaware.b4
  family: competency
  locator: { heading: "Table 1: self-awareness competency (ways of being)" }
  span: { start: 53109, end: 53145 }
  source: "deal with their feelings and desires"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [deal]
  maps: { criteria: [bristol/generic-2024: insight, bristol/generic-2024: self-management], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.normative.b1
  family: competency
  locator: { heading: "Table 1: normative competency (ways of being)" }
  span: { start: 53186, end: 53260 }
  source: "understand and reflect on the norms and values that underlie one’s actions"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [understand, reflect]
  maps: { criteria: [bristol/generic-2024: logical-argument-and-evaluation-of-perspectives], pathways: [criticality, reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/competency.normative.b2
  family: competency
  locator: { heading: "Table 1: normative competency (ways of being)" }
  span: { start: 53263, end: 53431 }
  source: "negotiate sustainable development values, principles,\n• goals and targets, in a context of conflicts of interests and trade-offs, uncertain knowledge and contradictions"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [negotiate]
  maps: { criteria: [bristol/generic-2024: logical-argument-and-evaluation-of-perspectives], pathways: [criticality, reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/narrative.strategic.1
  family: narrative
  locator: { heading: "Ways of practising: strategic competency" }
  span: { start: 53814, end: 53973 }
  source: "Strategic competency includes core employability skills such as goal setting, time and resource management, and implementing and evaluating a course of action."
  statementType: competency
  force: describes
  addressee: student
  employability: direct
  verbs: [includes]
  maps: { framework: [qaa/fheq-2024/4.15.b9.1], criteria: [bristol/generic-2024: self-management, bristol/generic-2024: decision-making], pathways: [work-based-and-experiential-learning, starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/narrative.strategic.2
  family: narrative
  locator: { heading: "Ways of practising: strategic competency" }
  span: { start: 54117, end: 54254 }
  source: "They engage with stakeholders to develop and deliver change projects through consultation, co-production, co-creation and/or co-delivery."
  statementType: competency
  force: describes
  addressee: graduate
  employability: direct
  verbs: [engage, develop, deliver]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/narrative.collaborative.1
  family: narrative
  locator: { heading: "Ways of practising: collaborative competency" }
  span: { start: 54280, end: 54497 }
  source: "Graduates will be expected to communicate effectively with colleagues, clients and stakeholders, ethically and professionally across platforms, disciplines, cultures, national boundaries and cyber-physical interfaces."
  statementType: competency
  force: will
  addressee: graduate
  employability: direct
  verbs: [communicate]
  maps: { framework: [qaa/fheq-2024/4.15.b8], criteria: [bristol/generic-2024: communication, cardiffmet/generic-2020: presentation], pathways: [presenting, work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/narrative.collaborative.2
  family: narrative
  locator: { heading: "Ways of practising: collaborative competency" }
  span: { start: 54621, end: 54822 }
  source: "Learners should be enabled to create visions, analyse problem solutions, conduct sustainability assessments, and develop strategies with stakeholders who may have different perspectives and priorities."
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: [create, analyse, conduct, develop]
  maps: { criteria: [bristol/generic-2024: teamwork, bristol/generic-2024: problem-solving], pathways: [work-based-and-experiential-learning, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/narrative.problem.1
  family: narrative
  locator: { heading: "Ways of practising: integrated problem-solving competency" }
  span: { start: 55270, end: 55508 }
  source: "Building on their problem-solving skills, students will broaden their focus by integrating knowledge and research methods from other disciplines and subject areas to develop and evaluate viable solutions to authentic, real-world problems."
  statementType: competency
  force: will
  addressee: student
  employability: bridge
  verbs: [broaden, integrating, develop, evaluate]
  maps: { framework: [qaa/fheq-2024/4.17.b5], criteria: [bristol/generic-2024: problem-solving, bristol/generic-2024: research], pathways: [researching-and-research-methods, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/narrative.selfaware.1
  family: narrative
  locator: { heading: "Ways of being: self-awareness competency" }
  span: { start: 55710, end: 55924 }
  source: "Through recognition of their individual context, students can develop a sense of agency and responsibility to drive sustainable action within their own environment, be it their local community or the wider society."
  statementType: mindset
  force: describes
  addressee: student
  employability: bridge
  verbs: [develop, drive]
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice, starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/narrative.normative.1
  family: narrative
  locator: { heading: "Ways of being: normative competency" }
  span: { start: 56279, end: 56426 }
  source: "Informed by concepts of justice, equity, inclusion and responsibility, students are equipped to identify biases and barriers to sustainable action."
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [identify]
  maps: { framework: [qaa/fheq-2024/4.15.b7], criteria: [bristol/generic-2024: critical-approach], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.k1
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Knowledge" }
  span: { start: 60063, end: 60178 }
  source: "Describe the relationships between environmental, social and economic systems, at scales from local to global level"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [describe]
  maps: { framework: [qaa/fheq-2024/4.10.b1], criteria: [cardiffmet/generic-2020: knowledge], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.k2
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Knowledge" }
  span: { start: 60181, end: 60259 }
  source: "Identify the tensions between the 17 SDGs and recognise their interconnections"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [identify, recognise]
  maps: { criteria: [cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.k3
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Knowledge" }
  span: { start: 60262, end: 60465 }
  source: "Recognise that a collective effort is not necessarily just a simple sum of each individual’s effort, but is likely to be more complex and have multiple drivers that may be personal, political or communal"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [recognise]
  maps: { pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.k4
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Knowledge" }
  span: { start: 60468, end: 60554 }
  source: "Identify that positive or negative environmental change may arise from economic growth"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [identify]
  maps: { pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.k5
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Knowledge" }
  span: { start: 60557, end: 60621 }
  source: "Describe how power structures and political systems influence SD"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [describe]
  maps: { criteria: [cardiffmet/generic-2020: knowledge], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.s1
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Skills" }
  span: { start: 60632, end: 60670 }
  source: "Recognise and understand relationships"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [recognise, understand]
  maps: { criteria: [bristol/generic-2024: critical-approach], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.s2
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Skills" }
  span: { start: 60673, end: 60696 }
  source: "Analyse complex systems"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [analyse]
  maps: { framework: [qaa/fheq-2024/4.12.b5], criteria: [cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.s3
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Skills" }
  span: { start: 60699, end: 60797 }
  source: "Consider how a system’s constituent parts interact and operate at different scales and across time"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [consider]
  maps: { criteria: [cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.s4
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Skills" }
  span: { start: 60800, end: 60948 }
  source: "Work with interconnectedness and complexity in a systemic context, synthesising diverse information and data to offer a range of potential solutions"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [work, synthesising, offer]
  maps: { framework: [qaa/fheq-2024/4.17.b5], criteria: [bristol/generic-2024: problem-solving], pathways: [criticality, creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.s5
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Skills" }
  span: { start: 60951, end: 61027 }
  source: "Identify the interactions between social, economic and environmental systems"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [identify]
  maps: { criteria: [cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.s6
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Skills" }
  span: { start: 61030, end: 61085 }
  source: "Assess a problem from different scales and perspectives"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [assess]
  maps: { framework: [qaa/fheq-2024/4.15.b7], criteria: [bristol/generic-2024: logical-argument-and-evaluation-of-perspectives], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.a1
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Attributes and values" }
  span: { start: 61111, end: 61261 }
  source: "Think systemically, in terms of recognising connections and interactions between factors, and understand that actions often have multiple consequences"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [think, recognising, understand]
  maps: { criteria: [bristol/generic-2024: critical-approach], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.a2
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Attributes and values" }
  span: { start: 61264, end: 61296 }
  source: "Deal with and manage uncertainty"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [deal, manage]
  maps: { framework: [qaa/fheq-2024/4.15.b9.2], criteria: [bristol/generic-2024: decision-making], pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.a3
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Attributes and values" }
  span: { start: 61299, end: 61451 }
  source: "Appreciate the root causes of unsustainable development including environmental, social and economic actions, and their links to cultural considerations"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: academic
  verbs: [appreciate]
  maps: { criteria: [cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.systems.a4
  family: outcome
  locator: { heading: "Table 2: systems thinking competency: Attributes and values" }
  span: { start: 61454, end: 61538 }
  source: "Identify the factors that have the biggest potential for driving constructive change"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [identify]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.k1
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Knowledge" }
  span: { start: 61673, end: 61795 }
  source: "Identify the risks associated with complex systems that can lead to unintended consequences or negative cumulative effects"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [identify]
  maps: { criteria: [cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.k2
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Knowledge" }
  span: { start: 61798, end: 61995 }
  source: "Evaluate the impacts and interconnections between the activities of different generations, demographic groups and cultures, recognising that there may be tensions and competing factors between them"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [evaluate, recognising]
  maps: { framework: [qaa/fheq-2024/4.15.b7], criteria: [cardiffmet/generic-2020: argument], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.k3
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Knowledge" }
  span: { start: 61998, end: 62109 }
  source: "Identify the causes and possible solutions to inequity at intragenerational and intergenerational global levels"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [identify]
  maps: { pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.k4
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Knowledge" }
  span: { start: 62112, end: 62251 }
  source: "Identify that natural systems have non-negotiable limits and may become unstable or collapse if subjected to excessive pressures or changes"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [identify]
  maps: { criteria: [cardiffmet/generic-2020: knowledge], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.k5
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Knowledge" }
  span: { start: 62254, end: 62348 }
  source: "Identify risks and uncertainties associated with the transformation of the natural environment"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [identify]
  maps: { pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.k6
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Knowledge" }
  span: { start: 62351, end: 62530 }
  source: "Identify the need for decisions about natural resources to involve judgements, not just about economic viability but about risks to future ecological, social or cultural wellbeing"
  statementType: knowledge
  force: describes
  addressee: student
  employability: bridge
  verbs: [identify]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.s1
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Skills" }
  span: { start: 62541, end: 62672 }
  source: "Generate and evaluate different approaches to SD and assess their likely impact, within the context of their own discipline/subject"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [generate, evaluate, assess]
  maps: { framework: [qaa/fheq-2024/4.15.b6], criteria: [bristol/generic-2024: problem-solving], pathways: [creativity, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.s2
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Skills" }
  span: { start: 62675, end: 62794 }
  source: "Use historical knowledge and an understanding of the consequences of past actions to envision how futures may be shaped"
  statementType: skill
  force: describes
  addressee: student
  employability: academic
  verbs: [use, envision]
  maps: { criteria: [cardiffmet/generic-2020: analysis], pathways: [criticality, creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.s3
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Skills" }
  span: { start: 62797, end: 62847 }
  source: "Develop, understand and evaluate multiple outcomes"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [develop, understand, evaluate]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.s4
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Skills" }
  span: { start: 62850, end: 62889 }
  source: "Create their own visions for the future"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [create]
  maps: { pathways: [creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.s5
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Skills" }
  span: { start: 62892, end: 62925 }
  source: "Apply the precautionary principle"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [apply]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.s6
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Skills" }
  span: { start: 62928, end: 62962 }
  source: "Assess the consequences of actions"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [assess]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.s7
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Skills" }
  span: { start: 62965, end: 63007 }
  source: "Evaluate risks and their potential impacts"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [evaluate]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.s8
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Skills" }
  span: { start: 63010, end: 63074 }
  source: "Identify future scenarios and use them to inform decision making"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [identify, use, inform]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [criticality, creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.s9
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Skills" }
  span: { start: 63077, end: 63239 }
  source: "Use backcasting skills - starting with defining a desirable future and working backwards to identify policies and programmes that will connect that to the present"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [use]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [creativity, work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.s10
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Skills" }
  span: { start: 63242, end: 63355 }
  source: "Use forecasting skills - looking at past trends and present conditions to extrapolate anticipated future outcomes"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [use]
  maps: { criteria: [bristol/generic-2024: research], pathways: [researching-and-research-methods], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.a1
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Attributes and values" }
  span: { start: 63381, end: 63517 }
  source: "Be flexible, resourceful and adaptable to fit changing and/or unforeseen circumstances if it is likely to have a positive outcome for SD"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { framework: [qaa/fheq-2024/4.15.b9.2], criteria: [bristol/generic-2024: self-management], pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.a2
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Attributes and values" }
  span: { start: 63520, end: 63560 }
  source: "Imagine and envision sustainable futures"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [imagine, envision]
  maps: { pathways: [creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.a3
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Attributes and values" }
  span: { start: 63563, end: 63666 }
  source: "Consider the impacts, both positive and negative, of heritage and cultures when planning for the future"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: academic
  verbs: [consider]
  maps: { pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.a4
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Attributes and values" }
  span: { start: 63669, end: 63743 }
  source: "Apply an awareness of intergenerational fairness to decisions and planning"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [apply]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.a5
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Attributes and values" }
  span: { start: 63746, end: 63810 }
  source: "Be prepared to learn from others and consider their perspectives"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [learn, consider]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.a6
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Attributes and values" }
  span: { start: 63813, end: 63887 }
  source: "Learn to unlearn when situations and contexts demand alternative solutions"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [learn, unlearn]
  maps: { framework: [qaa/fheq-2024/4.15.b4], criteria: [bristol/generic-2024: insight], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.anticipatory.a7
  family: outcome
  locator: { heading: "Table 2: anticipatory thinking competency: Attributes and values" }
  span: { start: 63890, end: 63954 }
  source: "Demonstrate an open mindset to new approaches to problem solving"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [demonstrate]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.k1
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Knowledge" }
  span: { start: 64085, end: 64209 }
  source: "Draw upon scientific evidence and scholarly research to develop understanding of SD and the impact of human activity upon it"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [draw, develop]
  maps: { framework: [qaa/fheq-2024/4.15.b5], criteria: [bristol/generic-2024: use-of-evidence-and-sources, cardiffmet/generic-2020: research], pathways: [finding-and-using-sources, researching-and-research-methods], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.k2
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Knowledge" }
  span: { start: 64212, end: 64368 }
  source: "Identify the rationale for encouraging behavioural change, where existing practices are shown to have a negative impact on the human and natural environment"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [identify]
  maps: { criteria: [cardiffmet/generic-2020: argument], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.k3
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Knowledge" }
  span: { start: 64371, end: 64485 }
  source: "Identify change makers who have made positive contributions and draw upon their practices to enhance understanding"
  statementType: knowledge
  force: describes
  addressee: student
  employability: bridge
  verbs: [identify, draw]
  maps: { pathways: [finding-and-using-sources], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.s1
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Skills" }
  span: { start: 64496, end: 64534 }
  source: "Present a simplified view of a concept"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [present]
  maps: { framework: [qaa/fheq-2024/4.10.b4], criteria: [bristol/generic-2024: communication, cardiffmet/generic-2020: presentation], pathways: [presenting, academic-writing], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.s2
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Skills" }
  span: { start: 64537, end: 64591 }
  source: "Identify and formulate critical questions and problems"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [identify, formulate]
  maps: { framework: [qaa/fheq-2024/4.15.b3.1], criteria: [bristol/generic-2024: critical-approach], pathways: [criticality, researching-and-research-methods], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.s3
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Skills" }
  span: { start: 64594, end: 64685 }
  source: "Assess new information and continuously incorporate it into existing models as they develop"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [assess, incorporate]
  maps: { criteria: [bristol/generic-2024: use-of-evidence-and-sources], pathways: [finding-and-using-sources, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.s4
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Skills" }
  span: { start: 64688, end: 64823 }
  source: "Critically assess and analyse SD issues within the context of their own discipline/ subject area or future profession/career intentions"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [assess, analyse]
  maps: { framework: [qaa/fheq-2024/4.15.b7], criteria: [bristol/generic-2024: critical-approach, cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.s5
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Skills" }
  span: { start: 64826, end: 64983 }
  source: "Analyse, synthesise and evaluate data and information and reach well-reasoned conclusions and solutions, testing them against relevant criteria and standards"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [analyse, synthesise, evaluate, reach, testing]
  maps: { framework: [qaa/fheq-2024/4.15.b7], criteria: [bristol/generic-2024: logical-argument-and-evaluation-of-perspectives, cardiffmet/generic-2020: argument], pathways: [criticality, researching-and-research-methods], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.s6
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Skills" }
  span: { start: 64986, end: 65054 }
  source: "Differentiate evidence based conclusions from opinion and conjecture"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [differentiate]
  maps: { criteria: [bristol/generic-2024: use-of-evidence-and-sources], pathways: [criticality, finding-and-using-sources], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.a1
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Attributes and values" }
  span: { start: 65080, end: 65217 }
  source: "Demonstrate the capacity for independent, evidence-based integrated thinking as the foundation for developing their personal ethical code"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [demonstrate, developing]
  maps: { criteria: [bristol/generic-2024: critical-approach], pathways: [criticality, reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.a2
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Attributes and values" }
  span: { start: 65220, end: 65292 }
  source: "Evaluate the consequences of their own actions and of collective actions"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [evaluate]
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.a3
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Attributes and values" }
  span: { start: 65295, end: 65412 }
  source: "Reflect on their own values, perceptions and actions, comparing and contrasting them to others who may have influence"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [reflect, comparing, contrasting]
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.a4
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Attributes and values" }
  span: { start: 65415, end: 65466 }
  source: "Take an evidence-based position in the SD discourse"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [take]
  maps: { framework: [qaa/fheq-2024/4.15.b3.1], criteria: [cardiffmet/generic-2020: argument], pathways: [criticality, academic-writing], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.critical.a5
  family: outcome
  locator: { heading: "Table 2: critical thinking competency: Attributes and values" }
  span: { start: 65469, end: 65561 }
  source: "Recognise their assumptions and evaluate the potential implications and consequences of them"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [recognise, evaluate]
  maps: { framework: [qaa/fheq-2024/4.15.b7], criteria: [bristol/generic-2024: critical-approach], pathways: [criticality, reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.k1
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Knowledge" }
  span: { start: 65693, end: 65800 }
  source: "Identify the root causes of unsustainable development, including environmental, social and economic actions"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [identify]
  maps: { criteria: [cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.k2
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Knowledge" }
  span: { start: 65803, end: 65881 }
  source: "Understand how emotional and cognitive awareness can influence decision making"
  statementType: knowledge
  force: describes
  addressee: student
  employability: bridge
  verbs: [understand]
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.k3
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Knowledge" }
  span: { start: 65884, end: 65984 }
  source: "Identify then enact changes to actions or behaviours where existing practices have a negative impact"
  statementType: knowledge
  force: describes
  addressee: student
  employability: bridge
  verbs: [identify, enact]
  maps: { criteria: [bristol/generic-2024: self-management], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.k4
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Knowledge" }
  span: { start: 65987, end: 66075 }
  source: "Appreciate how aspects of their own discipline contribute positively or negatively to SD"
  statementType: knowledge
  force: describes
  addressee: student
  employability: direct
  verbs: [appreciate]
  maps: { criteria: [cardiffmet/generic-2020: knowledge], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.k5
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Knowledge" }
  span: { start: 66078, end: 66178 }
  source: "Understand the risks and uncertainties associated with the transformation of the natural environment"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [understand]
  maps: { pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.s1
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Skills" }
  span: { start: 66189, end: 66267 }
  source: "Link the environmental, social and economic actions to cultural considerations"
  statementType: skill
  force: describes
  addressee: student
  employability: academic
  verbs: [link]
  maps: { criteria: [cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.s2
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Skills" }
  span: { start: 66270, end: 66451 }
  source: "Evaluate the impact of and connections between the activities of different generations, demographic groups and cultures, recognising that there may be competing factors between them"
  statementType: skill
  force: describes
  addressee: student
  employability: academic
  verbs: [evaluate, recognising]
  maps: { framework: [qaa/fheq-2024/4.15.b7], criteria: [cardiffmet/generic-2020: argument], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.s3
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Skills" }
  span: { start: 66454, end: 66605 }
  source: "Identify SD strategies to facilitate and mediate progressive discussions among interested parties (stakeholders) to help resolve dilemmas and conflicts"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [identify, facilitate, mediate]
  maps: { criteria: [bristol/generic-2024: teamwork, bristol/generic-2024: decision-making], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.s4
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Skills" }
  span: { start: 66608, end: 66694 }
  source: "Develop and implement innovative actions that further SD at the local level and beyond"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [develop, implement]
  maps: { framework: [qaa/fheq-2024/4.17.b6], criteria: [bristol/generic-2024: problem-solving], pathways: [work-based-and-experiential-learning, creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.s5
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Skills" }
  span: { start: 66697, end: 66786 }
  source: "Use planning and assessment tools to identify and address SD challenges and opportunities"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [use, identify, address]
  maps: { criteria: [bristol/generic-2024: decision-making, bristol/generic-2024: specialist-skills-and-techniques], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.a1
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Attributes and values" }
  span: { start: 66812, end: 66879 }
  source: "Practise decision-making and analyse consequences of decisions made"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [practise, analyse]
  maps: { framework: [qaa/fheq-2024/4.15.b9.2], criteria: [bristol/generic-2024: decision-making], pathways: [work-based-and-experiential-learning, reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.a2
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Attributes and values" }
  span: { start: 66882, end: 66928 }
  source: "Undertake reflection on actions and behaviours"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [undertake]
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.a3
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Attributes and values" }
  span: { start: 66931, end: 67008 }
  source: "Integrate thinking as a foundation for developing their personal ethical code"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [integrate, developing]
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.a4
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Attributes and values" }
  span: { start: 67011, end: 67134 }
  source: "Demonstrate flexibility and resourcefulness and adapt a problem-solving mindset to fit changing or unforeseen circumstances"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [demonstrate, adapt]
  maps: { framework: [qaa/fheq-2024/4.15.b9.2], criteria: [bristol/generic-2024: self-management], pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.strategic.a5
  family: outcome
  locator: { heading: "Table 2: strategic thinking competency: Attributes and values" }
  span: { start: 67137, end: 67182 }
  source: "Demonstrate a commitment to lifelong learning"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: direct
  verbs: [demonstrate]
  maps: { framework: [qaa/fheq-2024/4.15.b9.3], criteria: [bristol/generic-2024: self-management], pathways: [starting-progressing-and-succeeding, reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.k1
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Knowledge" }
  span: { start: 67309, end: 67410 }
  source: "Understand the value of collaborating with others offering different knowledge, views and experiences"
  statementType: knowledge
  force: describes
  addressee: student
  employability: bridge
  verbs: [understand]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.k2
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Knowledge" }
  span: { start: 67413, end: 67472 }
  source: "Identify and critique differing approaches to collaboration"
  statementType: knowledge
  force: describes
  addressee: student
  employability: bridge
  verbs: [identify, critique]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.k3
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Knowledge" }
  span: { start: 67475, end: 67512 }
  source: "Recognise group management strategies"
  statementType: knowledge
  force: describes
  addressee: student
  employability: direct
  verbs: [recognise]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.k4
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Knowledge" }
  span: { start: 67515, end: 67600 }
  source: "Recognise verbal and non-verbal communication skills and their role in group cohesion"
  statementType: knowledge
  force: describes
  addressee: student
  employability: bridge
  verbs: [recognise]
  maps: { criteria: [bristol/generic-2024: communication], pathways: [presenting], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.k5
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Knowledge" }
  span: { start: 67603, end: 67686 }
  source: "Recognise the goals, skills and needs of others as part of successful collaboration"
  statementType: knowledge
  force: describes
  addressee: student
  employability: bridge
  verbs: [recognise]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.s1
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Skills" }
  span: { start: 67697, end: 67786 }
  source: "Communicate effectively through listening, clarity of expression and constructive inquiry"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [communicate]
  maps: { framework: [qaa/fheq-2024/4.15.b8], criteria: [bristol/generic-2024: communication, cardiffmet/generic-2020: presentation], pathways: [presenting], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.s2
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Skills" }
  span: { start: 67789, end: 67928 }
  source: "Engage in interdisciplinary discussion to inform their thinking about sustainable futures and seek holistic, creative solutions to problems"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [engage, inform, seek]
  maps: { criteria: [bristol/generic-2024: logical-argument-and-evaluation-of-perspectives], pathways: [criticality, creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.s3
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Skills" }
  span: { start: 67931, end: 68053 }
  source: "Identify the importance of encouraging and enabling individuals and organisations to work together to create new knowledge"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [identify]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.s4
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Skills" }
  span: { start: 68056, end: 68103 }
  source: "Clearly communicate complex SD issues to others"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [communicate]
  maps: { framework: [qaa/fheq-2024/4.15.b8], criteria: [bristol/generic-2024: communication, cardiffmet/generic-2020: presentation], pathways: [presenting, academic-writing], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.s5
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Skills" }
  span: { start: 68106, end: 68231 }
  source: "Facilitate and mediate progressive discussions among interested parties (stakeholders) to help resolve dilemmas and conflicts"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [facilitate, mediate]
  maps: { criteria: [bristol/generic-2024: teamwork, bristol/generic-2024: communication], pathways: [work-based-and-experiential-learning, presenting], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.s6
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Skills" }
  span: { start: 68234, end: 68264 }
  source: "Listen actively and critically"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [listen]
  maps: { criteria: [bristol/generic-2024: communication], pathways: [presenting, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.s7
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Skills" }
  span: { start: 68267, end: 68312 }
  source: "Connect, adapt and synthesise what they learn"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [connect, adapt, synthesise]
  maps: { criteria: [cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.s8
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Skills" }
  span: { start: 68315, end: 68360 }
  source: "Address conflict and develop mediation skills"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [address, develop]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.s9
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Skills" }
  span: { start: 68363, end: 68400 }
  source: "Utilise appropriate leadership styles"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [utilise]
  maps: { framework: [qaa/fheq-2024/4.17.b8.1], criteria: [bristol/generic-2024: teamwork, bristol/generic-2024: self-management], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.a1
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Attributes and values" }
  span: { start: 68426, end: 68505 }
  source: "Learn from others including peers, professionals, expert groups and communities"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [learn]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning, reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.a2
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Attributes and values" }
  span: { start: 68508, end: 68538 }
  source: "Deal with conflicts in a group"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [deal]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.a3
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Attributes and values" }
  span: { start: 68541, end: 68599 }
  source: "Facilitate collaborative and participatory problem solving"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [facilitate]
  maps: { criteria: [bristol/generic-2024: teamwork, bristol/generic-2024: problem-solving], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.a4
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Attributes and values" }
  span: { start: 68602, end: 68637 }
  source: "Assist others through peer learning"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [assist]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [understanding-learning-assessment-and-feedback], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.a5
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Attributes and values" }
  span: { start: 68640, end: 68678 }
  source: "Question norms, practices and opinions"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [question]
  maps: { criteria: [bristol/generic-2024: critical-approach], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.a6
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Attributes and values" }
  span: { start: 68681, end: 68749 }
  source: "Understand and respect the needs, perspectives and actions of others"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [understand, respect]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.a7
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Attributes and values" }
  span: { start: 68752, end: 68802 }
  source: "Empathise with the views and experiences of others"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [empathise]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.collaborative.a8
  family: outcome
  locator: { heading: "Table 2: collaborative competency: Attributes and values" }
  span: { start: 68805, end: 68868 }
  source: "Collaborate equitably across gender, ethnicity and other groups"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: direct
  verbs: [collaborate]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.k1
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Knowledge" }
  span: { start: 69008, end: 69144 }
  source: "Describe the potential for their discipline to interconnect with other disciplines or areas of expertise and make creative leaps forward"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [describe]
  maps: { criteria: [cardiffmet/generic-2020: knowledge], pathways: [creativity, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.k2
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Knowledge" }
  span: { start: 69147, end: 69239 }
  source: "Describe how aspects of their own area of study contribute to SD and connects to the UN SDGs"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [describe]
  maps: { criteria: [cardiffmet/generic-2020: knowledge], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.k3
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Knowledge" }
  span: { start: 69242, end: 69296 }
  source: "Appreciate research methods from different disciplines"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [appreciate]
  maps: { framework: [qaa/fheq-2024/4.12.b3], criteria: [bristol/generic-2024: research, cardiffmet/generic-2020: research], pathways: [researching-and-research-methods], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.k4
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Knowledge" }
  span: { start: 69299, end: 69380 }
  source: "Understands the academic norms of a discipline and explore disciplinary integrity"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [understands, explore]
  maps: { criteria: [cardiffmet/generic-2020: knowledge], pathways: [researching-and-research-methods, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.s1
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Skills" }
  span: { start: 69391, end: 69580 }
  source: "Use and apply established frameworks and methodologies for analysing the impact(s) of a behaviour or process, utilising the skills and expertise developed through their own area(s) of study"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [use, apply, analysing, utilising]
  maps: { framework: [qaa/fheq-2024/4.15.b2], criteria: [bristol/generic-2024: specialist-skills-and-techniques, bristol/generic-2024: research], pathways: [researching-and-research-methods], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.s2
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Skills" }
  span: { start: 69583, end: 69648 }
  source: "Apply different problem-solving frameworks to complex SD problems"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [apply]
  maps: { framework: [qaa/fheq-2024/4.17.b5], criteria: [bristol/generic-2024: problem-solving], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.s3
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Skills" }
  span: { start: 69651, end: 69700 }
  source: "Develop viable, inclusive and equitable solutions"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [develop]
  maps: { framework: [qaa/fheq-2024/4.17.b6], criteria: [bristol/generic-2024: problem-solving], pathways: [creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.s4
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Skills" }
  span: { start: 69703, end: 69760 }
  source: "Effectively engage with real-life problems relevant to SD"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [engage]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.s5
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Skills" }
  span: { start: 69763, end: 69877 }
  source: "Combine different sources and types of evidence, drawing from different disciplines, to view and address a problem"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [combine, drawing, view, address]
  maps: { framework: [qaa/fheq-2024/4.15.b5], criteria: [bristol/generic-2024: use-of-evidence-and-sources, cardiffmet/generic-2020: research], pathways: [finding-and-using-sources, researching-and-research-methods], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.a1
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Attributes and values" }
  span: { start: 69903, end: 69966 }
  source: "Utilise appropriate competencies to identify and solve problems"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [utilise, identify, solve]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.a2
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Attributes and values" }
  span: { start: 69969, end: 70046 }
  source: "Communicate effectively with others to identify solutions to complex problems"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [communicate, identify]
  maps: { criteria: [bristol/generic-2024: communication, bristol/generic-2024: teamwork], pathways: [presenting], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.a3
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Attributes and values" }
  span: { start: 70049, end: 70137 }
  source: "Listen critically when presented with alternative ideas or frameworks, systems and ideas"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [listen]
  maps: { criteria: [bristol/generic-2024: logical-argument-and-evaluation-of-perspectives], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.a4
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Attributes and values" }
  span: { start: 70140, end: 70206 }
  source: "Work effectively in multidisciplinary and interdisciplinary groups"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: direct
  verbs: [work]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.problem.a5
  family: outcome
  locator: { heading: "Table 2: integrated problem-solving competency: Attributes and values" }
  span: { start: 70209, end: 70340 }
  source: "Consider academic norms and ways of thinking across different disciplines and subject areas, bringing them into play as appropriate"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: academic
  verbs: [consider, bringing]
  maps: { criteria: [cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.selfaware.k1
  family: outcome
  locator: { heading: "Table 2: self-awareness competency: Knowledge" }
  span: { start: 70468, end: 70530 }
  source: "Identify and evaluate their own competences and learning needs"
  statementType: knowledge
  force: describes
  addressee: student
  employability: bridge
  verbs: [identify, evaluate]
  maps: { framework: [qaa/fheq-2024/4.15.b5], criteria: [bristol/generic-2024: insight, bristol/generic-2024: self-management], pathways: [reflective-practice, starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.selfaware.k2
  family: outcome
  locator: { heading: "Table 2: self-awareness competency: Knowledge" }
  span: { start: 70533, end: 70576 }
  source: "Understand their own heritages and cultures"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [understand]
  maps: { pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.selfaware.k3
  family: outcome
  locator: { heading: "Table 2: self-awareness competency: Knowledge" }
  span: { start: 70579, end: 70670 }
  source: "Identify the importance of empowering individuals and organisations to work collaboratively"
  statementType: knowledge
  force: describes
  addressee: student
  employability: bridge
  verbs: [identify]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.selfaware.k4
  family: outcome
  locator: { heading: "Table 2: self-awareness competency: Knowledge" }
  span: { start: 70673, end: 70739 }
  source: "Understand how power structures and political systems influence SD"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [understand]
  maps: { criteria: [cardiffmet/generic-2020: knowledge], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.selfaware.k5
  family: outcome
  locator: { heading: "Table 2: self-awareness competency: Knowledge" }
  span: { start: 70742, end: 70883 }
  source: "Identify the wide range of human cultures in existence and understand both the benefits and the challenges that these cultures present for SD"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [identify, understand]
  maps: { pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.selfaware.s1
  family: outcome
  locator: { heading: "Table 2: self-awareness competency: Skills" }
  span: { start: 70894, end: 71065 }
  source: "Employ leadership for SD by challenging assumptions and negotiating alternatives to unsustainable current practices, especially within their own discipline or subject area"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [employ, challenging, negotiating]
  maps: { framework: [qaa/fheq-2024/4.17.b8.1], criteria: [bristol/generic-2024: critical-approach, bristol/generic-2024: teamwork], pathways: [criticality, work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.selfaware.s2
  family: outcome
  locator: { heading: "Table 2: self-awareness competency: Skills" }
  span: { start: 71068, end: 71199 }
  source: "Actively implement or contribute to changes that promote SD within the scope of their own learning experience and study environment"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [implement, contribute]
  maps: { criteria: [bristol/generic-2024: self-management], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.selfaware.s3
  family: outcome
  locator: { heading: "Table 2: self-awareness competency: Skills" }
  span: { start: 71202, end: 71267 }
  source: "Take responsibility for their own learning and skills development"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [take]
  maps: { framework: [qaa/fheq-2024/4.15.b5], criteria: [bristol/generic-2024: self-management], pathways: [starting-progressing-and-succeeding, reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.selfaware.s4
  family: outcome
  locator: { heading: "Table 2: self-awareness competency: Skills" }
  span: { start: 71270, end: 71369 }
  source: "Facilitate and mediate progressive discussions among stakeholders to resolve dilemmas and conflicts"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [facilitate, mediate]
  maps: { criteria: [bristol/generic-2024: teamwork, bristol/generic-2024: communication], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.selfaware.a1
  family: outcome
  locator: { heading: "Table 2: self-awareness competency: Attributes and values" }
  span: { start: 71395, end: 71510 }
  source: "Clarify their own views on ways that SD can be achieved in different local and global communities and circumstances"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: academic
  verbs: [clarify]
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice, criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.selfaware.a2
  family: outcome
  locator: { heading: "Table 2: self-awareness competency: Attributes and values" }
  span: { start: 71513, end: 71578 }
  source: "Access and engage with their own and other cultures and heritages"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: academic
  verbs: [access, engage]
  maps: { pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.selfaware.a3
  family: outcome
  locator: { heading: "Table 2: self-awareness competency: Attributes and values" }
  span: { start: 71581, end: 71960 }
  source: "Maintain healthy mental and emotional state and be aware of their mental and emotional health, in particular to: ` reflect on their own values, perceptions and actions ` reflect on their own role in the local community and global society ` continually evaluate and further motivate their actions ` be aware of and engage with their own emotions ` make meaning in the work they do"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [maintain]
  maps: { criteria: [bristol/generic-2024: self-management], pathways: [reflective-practice, starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.normative.k1
  family: outcome
  locator: { heading: "Table 2: normative competency: Knowledge" }
  span: { start: 72083, end: 72233 }
  source: "Identify the wide range of human cultures in existence, and understand both the benefits and the challenges that these cultures present in terms of SD"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [identify, understand]
  maps: { pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.normative.k2
  family: outcome
  locator: { heading: "Table 2: normative competency: Knowledge" }
  span: { start: 72236, end: 72392 }
  source: "Demonstrate that both unsustainable and sustainable practices take place in an evolving context, necessitating adaptability in policy and planning responses"
  statementType: knowledge
  force: describes
  addressee: student
  employability: bridge
  verbs: [demonstrate]
  maps: { criteria: [cardiffmet/generic-2020: argument], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.normative.k3
  family: outcome
  locator: { heading: "Table 2: normative competency: Knowledge" }
  span: { start: 72395, end: 72530 }
  source: "Identify the interactions between human communities and ecological systems, and be able to assess the potential impacts upon each other"
  statementType: knowledge
  force: describes
  addressee: student
  employability: academic
  verbs: [identify, assess]
  maps: { criteria: [cardiffmet/generic-2020: analysis], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.normative.k4
  family: outcome
  locator: { heading: "Table 2: normative competency: Knowledge" }
  span: { start: 72533, end: 72586 }
  source: "Identify ethical questions and use ethical frameworks"
  statementType: knowledge
  force: describes
  addressee: student
  employability: direct
  verbs: [identify, use]
  maps: { criteria: [bristol/generic-2024: critical-approach], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.normative.k5
  family: outcome
  locator: { heading: "Table 2: normative competency: Knowledge" }
  span: { start: 72589, end: 72651 }
  source: "Identify practical interventions for sustainability challenges"
  statementType: knowledge
  force: describes
  addressee: student
  employability: direct
  verbs: [identify]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.normative.s1
  family: outcome
  locator: { heading: "Table 2: normative competency: Skills" }
  span: { start: 72662, end: 72755 }
  source: "Tackle and negotiate SD conflicts with an awareness of different perspectives and motivations"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [tackle, negotiate]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.normative.s2
  family: outcome
  locator: { heading: "Table 2: normative competency: Skills" }
  span: { start: 72758, end: 72928 }
  source: "Identify the opportunities to support and develop a progressive and resilient culture that encourages citizens, professions and institutions to put learning into practice"
  statementType: skill
  force: describes
  addressee: student
  employability: direct
  verbs: [identify, support, develop]
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.normative.s3
  family: outcome
  locator: { heading: "Table 2: normative competency: Skills" }
  span: { start: 72931, end: 72996 }
  source: "Debate and explore fairness and justice, including social justice"
  statementType: skill
  force: describes
  addressee: student
  employability: academic
  verbs: [debate, explore]
  maps: { criteria: [cardiffmet/generic-2020: argument], pathways: [criticality, presenting], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.normative.s4
  family: outcome
  locator: { heading: "Table 2: normative competency: Skills" }
  span: { start: 72999, end: 73082 }
  source: "Develop alternative solutions that provide new opportunities for engagement with SD"
  statementType: skill
  force: describes
  addressee: student
  employability: bridge
  verbs: [develop, provide]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.normative.a1
  family: outcome
  locator: { heading: "Table 2: normative competency: Attributes and values" }
  span: { start: 73108, end: 73253 }
  source: "Negotiate SD values, principles, goals and targets, in a context of conflicts of interests and trade-offs, uncertain knowledge and contradictions"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [negotiate]
  maps: { framework: [qaa/fheq-2024/4.17.b5], criteria: [bristol/generic-2024: logical-argument-and-evaluation-of-perspectives], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.normative.a2
  family: outcome
  locator: { heading: "Table 2: normative competency: Attributes and values" }
  span: { start: 73256, end: 73330 }
  source: "Understand and reflect on the norms and values that underlie one’s actions"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [understand, reflect]
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.normative.a3
  family: outcome
  locator: { heading: "Table 2: normative competency: Attributes and values" }
  span: { start: 73333, end: 73381 }
  source: "Engage with and understand different world views"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [engage, understand]
  maps: { criteria: [bristol/generic-2024: logical-argument-and-evaluation-of-perspectives], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/outcome.normative.a4
  family: outcome
  locator: { heading: "Table 2: normative competency: Attributes and values" }
  span: { start: 73384, end: 73442 }
  source: "Appreciate, critique and value different cultural contexts"
  statementType: attribute-value
  force: describes
  addressee: student
  employability: bridge
  verbs: [appreciate, critique, value]
  maps: { criteria: [bristol/generic-2024: logical-argument-and-evaluation-of-perspectives], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/design.1
  family: design
  locator: { heading: "Course and module learning outcomes for ESD" }
  span: { start: 57384, end: 57539 }
  source: "Course and module-level learning outcomes for ESD should interconnect subject-specific knowledge and skills, sustainability competencies and the 17 UN SDGs"
  statementType: outcome-design
  force: should
  addressee: educator
  employability: academic
  verbs: [interconnect]
  maps: { pathways: [understanding-learning-assessment-and-feedback], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/design.2
  family: design
  locator: { heading: "Course and module learning outcomes for ESD" }
  span: { start: 59285, end: 59448 }
  source: "Educators are therefore invited to select, interpret, and modify these outcomes as required to meet the discipline, context, level and credit-rating of the module."
  statementType: outcome-design
  force: may
  addressee: educator
  employability: academic
  verbs: [select, interpret, modify]
  maps: { pathways: [understanding-learning-assessment-and-feedback], basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/students.b1
  family: students
  locator: { heading: "Consulting key players: students (guidance)" }
  span: { start: 34045, end: 34200 }
  source: "Consider the understanding and experience of ESD that you want every student to have, and how this can be incorporated into course-level learning outcomes."
  statementType: opportunity
  force: should
  addressee: educator
  employability: academic
  verbs: []
  maps: { pathways: [understanding-learning-assessment-and-feedback], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/students.b2
  family: students
  locator: { heading: "Consulting key players: students (guidance)" }
  span: { start: 34201, end: 34358 }
  source: "Think about the understanding and experiences you wish to offer them, and how this choice can be provided, and sequentially build, across the years of study."
  statementType: opportunity
  force: should
  addressee: educator
  employability: academic
  verbs: []
  maps: { pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/students.b3
  family: students
  locator: { heading: "Consulting key players: students (guidance)" }
  span: { start: 34359, end: 34578 }
  source: "Provide students with, and support them to develop, opportunities to put ESD learning into practice and to ‘live what they are learning’, with, for example, opportunities for volunteering and extracurricular activities."
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/students.b4
  family: students
  locator: { heading: "Consulting key players: students (guidance)" }
  span: { start: 34579, end: 34709 }
  source: "Include ESD during student induction, covering an understanding of what your institution is doing and how students can contribute."
  statementType: opportunity
  force: should
  addressee: educator
  employability: academic
  verbs: []
  maps: { pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/students.b5
  family: students
  locator: { heading: "Consulting key players: students (guidance)" }
  span: { start: 34892, end: 35000 }
  source: "Students who wish to take SD considerations into account in their career plans should be supported to do so."
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/students.b6
  family: students
  locator: { heading: "Consulting key players: students (guidance)" }
  span: { start: 35001, end: 35170 }
  source: "Encourage your careers service (where applicable) to provide students with information on the social and environmental performance of potential employers and enterprise."
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/students.b7
  family: students
  locator: { heading: "Consulting key players: students (guidance)" }
  span: { start: 35171, end: 35314 }
  source: "Students should be supported to develop their enterprise and entrepreneurial skills that can lead to ventures that positively contribute to SD."
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [creativity, work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/students.b8
  family: students
  locator: { heading: "Consulting key players: students (guidance)" }
  span: { start: 35402, end: 35486 }
  source: "ESD should be part of module, end-of-course, placement and work experience feedback."
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [understanding-learning-assessment-and-feedback], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/employers.b1
  family: employers
  locator: { heading: "Consulting key players: employers and enterprise (guidance)" }
  span: { start: 37397, end: 37524 }
  source: "Ensure every graduate has an opportunity to engage with and shape solutions to SD challenges within and beyond the institution."
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/employers.b2
  family: employers
  locator: { heading: "Consulting key players: employers and enterprise (guidance)" }
  span: { start: 37525, end: 37751 }
  source: "Create partnerships with enterprising individuals and companies who can contribute to educational experiences such as, for example, living labs, case studies, experiential learning, simulation activities and research projects."
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/employers.b3
  family: employers
  locator: { heading: "Consulting key players: employers and enterprise (guidance)" }
  span: { start: 37955, end: 38140 }
  source: "Ensure graduates are ready to help their future workplace(s) meet SD challenges and that they recognise the importance of creativity and a willingness to try new approaches in doing so."
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning, creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/academics.b1
  family: academics
  locator: { heading: "Consulting key players: academics (guidance)" }
  span: { start: 40521, end: 40764 }
  source: "Understand ESD and the UN SDGs in the context of their own discipline/subject area and associated professional contexts (including how their discipline/subject area may entrench and reproduce unjust and unsustainable thinking and/or practice)."
  statementType: educator
  force: should
  addressee: educator
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/academics.b2
  family: academics
  locator: { heading: "Consulting key players: academics (guidance)" }
  span: { start: 40768, end: 40898 }
  source: "Understand the UNESCO sustainability competencies (see Table 1, page 20) and integrate them as part of course and module outcomes."
  statementType: educator
  force: should
  addressee: educator
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/academics.b3
  family: academics
  locator: { heading: "Consulting key players: academics (guidance)" }
  span: { start: 40902, end: 41023 }
  source: "Facilitate teaching and assessment approaches that support the development and assessment of sustainability competencies."
  statementType: educator
  force: should
  addressee: educator
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/academics.b4
  family: academics
  locator: { heading: "Consulting key players: academics (guidance)" }
  span: { start: 41027, end: 41112 }
  source: "Facilitate interdisciplinary and transdisciplinary teaching practices and assessment."
  statementType: educator
  force: should
  addressee: educator
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/academics.b5
  family: academics
  locator: { heading: "Consulting key players: academics (guidance)" }
  span: { start: 41116, end: 41225 }
  source: "Create opportunities for the sharing of ESD ideas, knowledge exchange and experiences across the institution."
  statementType: educator
  force: should
  addressee: educator
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/academics.b6
  family: academics
  locator: { heading: "Consulting key players: academics (guidance)" }
  span: { start: 41229, end: 41327 }
  source: "Have conversations with key players to enable ESD learning and contribution beyond the curriculum."
  statementType: educator
  force: should
  addressee: educator
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/services.b1
  family: services
  locator: { heading: "Consulting key players: professional services and governance (guidance)" }
  span: { start: 43870, end: 44027 }
  source: "Ensure that staff driving quality assurance and enhancement have knowledge and understanding of ESD and how they can enable its positioning across curricula."
  statementType: institution
  force: should
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/services.b2
  family: services
  locator: { heading: "Consulting key players: professional services and governance (guidance)" }
  span: { start: 44028, end: 44223 }
  source: "Ensure that curriculum validation and review templates, and other appropriate teaching and learning templates, drive a focus on authentically evidencing ESD engagement at course and module level."
  statementType: institution
  force: should
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/services.b3
  family: services
  locator: { heading: "Consulting key players: professional services and governance (guidance)" }
  span: { start: 44368, end: 44490 }
  source: "Develop mechanisms for evaluating the impact and efficacy of ESD to demonstrate outcomes and drive continuous enhancement."
  statementType: institution
  force: should
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/communities.b1
  family: communities
  locator: { heading: "Consulting key players: communities (guidance)" }
  span: { start: 46342, end: 46472 }
  source: "Enable students to work with communities of practice, as well as place-based physical communities, to contribute positively to SD."
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: [enable]
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/environment.b1
  family: environment
  locator: { heading: "ESD requires a learning environment in which:" }
  span: { start: 75028, end: 75102 }
  source: "interdisciplinary or transdisciplinary learning approaches are facilitated"
  statementType: institution
  force: describes
  addressee: provider
  employability: academic
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/environment.b2
  family: environment
  locator: { heading: "ESD requires a learning environment in which:" }
  span: { start: 75106, end: 75150 }
  source: "learning is inclusive and accessible for all"
  statementType: institution
  force: describes
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/environment.b3
  family: environment
  locator: { heading: "ESD requires a learning environment in which:" }
  span: { start: 75154, end: 75190 }
  source: "policies support synoptic assessment"
  statementType: institution
  force: describes
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021/environment.b4
  family: environment
  locator: { heading: "ESD requires a learning environment in which:" }
  span: { start: 75194, end: 75259 }
  source: "extra and co-curricular opportunities are provided and recognised"
  statementType: institution
  force: describes
  addressee: provider
  employability: academic
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/environment.b5
  family: environment
  locator: { heading: "ESD requires a learning environment in which:" }
  span: { start: 75263, end: 75424 }
  source: "learning spaces including the campus and outdoor environments are fully utilised to provide alternative locations to develop and express the competencies of ESD."
  statementType: institution
  force: describes
  addressee: provider
  employability: academic
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/environment.b6
  family: environment
  locator: { heading: "Developing learning environments to support ESD" }
  span: { start: 75435, end: 75600 }
  source: "Teaching, learning and assessment should take advantage of the learning opportunities afforded by the campus and the local community, as well as online environments."
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: [take]
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/environment.b7
  family: environment
  locator: { heading: "Developing learning environments to support ESD" }
  span: { start: 76058, end: 76207 }
  source: "Consider how the course can broaden its literature and resources to include diverse voices in ESD and perspectives from underrepresented communities."
  statementType: opportunity
  force: should
  addressee: educator
  employability: academic
  verbs: [consider, broaden]
  maps: { pathways: [finding-and-using-sources], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/assessment.b1
  family: assessment
  locator: { heading: "Teaching and assessment practice (guidance)" }
  span: { start: 79906, end: 80092 }
  source: "Use group-based work within and beyond the course, subject, university or community to develop collaborative competencies though meaningful discussions with peers and other stakeholders."
  statementType: assessment
  force: should
  addressee: educator
  employability: bridge
  verbs: [use, develop]
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/assessment.b2
  family: assessment
  locator: { heading: "Teaching and assessment practice (guidance)" }
  span: { start: 80093, end: 80383 }
  source: "Use play-based approaches, including game-based learning and simulation, to provide an environment for students to explore alternative scenarios and practice and develop alternative ways of thinking, allowing students to take risks, experiment with new approaches and learn through failure."
  statementType: assessment
  force: should
  addressee: educator
  employability: bridge
  verbs: [use, provide, explore, take, experiment, learn]
  maps: { pathways: [creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/assessment.b3
  family: assessment
  locator: { heading: "Teaching and assessment practice (guidance)" }
  span: { start: 80384, end: 80548 }
  source: "Provide opportunities for critical reflection on personal perspectives and that of others, to consider what has influenced their thinking and practice in this area."
  statementType: assessment
  force: should
  addressee: educator
  employability: bridge
  verbs: [provide, consider]
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/assessment.b4
  family: assessment
  locator: { heading: "Teaching and assessment practice (guidance)" }
  span: { start: 82533, end: 82680 }
  source: "The developmental nature of competencies benefits from formative assessment and placing a focus on the process rather than the product of learning."
  statementType: assessment
  force: describes
  addressee: educator
  employability: bridge
  verbs: [benefits]
  maps: { pathways: [understanding-learning-assessment-and-feedback], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/assessment.b5
  family: assessment
  locator: { heading: "Teaching and assessment practice (guidance)" }
  span: { start: 82681, end: 82824 }
  source: "Assessment criteria should be designed to prioritise how students reached a viable solution to a problem in preference to the problem solution."
  statementType: assessment
  force: should
  addressee: educator
  employability: academic
  verbs: [designed, prioritise, reached]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [understanding-learning-assessment-and-feedback], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/assessment.b6
  family: assessment
  locator: { heading: "Teaching and assessment practice (guidance)" }
  span: { start: 82825, end: 83015 }
  source: "Authentic assessment instruments such as blogs, vlogs, websites and wikis engage students and provide a way for students to showcase their learning and share it with interested stakeholders."
  statementType: assessment
  force: should
  addressee: educator
  employability: direct
  verbs: [engage, provide, showcase, share]
  maps: { criteria: [bristol/generic-2024: communication, cardiffmet/generic-2020: presentation], pathways: [presenting, ai-and-technology], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021/assessment.b7
  family: assessment
  locator: { heading: "Teaching and assessment practice (guidance)" }
  span: { start: 84609, end: 84884 }
  source: "Sustainability competencies can also be developed through extracurricular and co-curricular activities and evidenced via a range of non-formal routes including micro-credentialling, digital badges, CVs, LinkedIn profiles, professional development planning or the HEAR report."
  statementType: assessment
  force: describes
  addressee: educator
  employability: direct
  verbs: [developed, evidenced]
  maps: { pathways: [starting-progressing-and-succeeding, work-based-and-experiential-learning], basis: inferred }
  audience: both
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. Student versions in the second person, naming no issuer; force kept. -->
```yaml
- statement: qaa-advancehe/esd-2021/aim.1
  forPractitioner: { text: "ESD helps students and staff build the knowledge, competence and capacity to work towards sustainable futures.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You build the knowledge and abilities to work towards a sustainable future.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/aim.2
  forPractitioner: { text: "ESD helps students and staff grasp the world's complexity and its recurring wicked problems, and see how they can help change things in their personal and working lives.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn how complex the world's problems are and how you can help change things, at work and in your own life.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/aim.3
  forPractitioner: { text: "ESD challenges and equips students and staff to design solutions together and lead change for sustainability.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are challenged and supported to design solutions with others and lead change for sustainability.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/aim.foreword
  forPractitioner: { text: "The chairs ask every provider to make sure graduates leave with the knowledge, skills and attributes to cope with, and ideally thrive among, the challenges of this century.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course should leave you with the knowledge, skills and qualities to cope with, and do well in, the challenges ahead.", rewrite: full, force: must, status: drafted }
- statement: qaa-advancehe/esd-2021/principle.b1
  forPractitioner: { text: "ESD objectives, targets and KPIs sit in the institution's strategic priorities and the strategies and policies that follow.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa-advancehe/esd-2021/principle.b2
  forPractitioner: { text: "Course validation and periodic review look at how the curriculum frames ESD.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect sustainability to be part of how your course is approved, reviewed and introduced to you.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/principle.b3
  forPractitioner: { text: "ESD is central to induction for staff and students and to staff appraisal or promotion criteria.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect sustainability to be part of how your course is approved, reviewed and introduced to you.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/principle.b4
  forPractitioner: { text: "Quality assurance and enhancement processes state ESD.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa-advancehe/esd-2021/principle.b5
  forPractitioner: { text: "The institution fully supports staff development for ESD.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa-advancehe/esd-2021/competency.systems.b1
  forPractitioner: { text: "Recognises and understands relationships.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You see how things are related.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.systems.b2
  forPractitioner: { text: "Analyses complex systems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You analyse complex systems.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.systems.b3
  forPractitioner: { text: "Considers how systems sit inside different domains and scales.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You think about how systems sit inside other domains and at other scales.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.systems.b4
  forPractitioner: { text: "Deals with uncertainty.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You cope with uncertainty.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.anticipatory.b1
  forPractitioner: { text: "Understands and evaluates several possible outcomes.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You weigh up several possible outcomes.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.anticipatory.b2
  forPractitioner: { text: "Creates own visions of the future.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You form your own vision of the future.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.anticipatory.b3
  forPractitioner: { text: "Applies the precautionary principle.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You take care before acting where the risks are not yet known.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.anticipatory.b4
  forPractitioner: { text: "Assesses the consequences of actions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You judge what actions will lead to.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.anticipatory.b5
  forPractitioner: { text: "Deals with risk and change.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You cope with risk and change.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.critical.b1
  forPractitioner: { text: "Questions norms, practices and opinions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You question accepted ways, practices and views.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.critical.b2
  forPractitioner: { text: "Reflects on own values, perceptions and actions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own values, views and actions.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.critical.b3
  forPractitioner: { text: "Takes a position in debates on sustainable development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You take a position in debates about sustainability.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.strategic.b1
  forPractitioner: { text: "Develops and carries out new actions that advance sustainable development locally and beyond.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You plan and carry out new actions for sustainability, locally and further away.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.collaborative.b1
  forPractitioner: { text: "Learns from others, peers and people inside and outside the institution.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn from others, inside and outside your university.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.collaborative.b2
  forPractitioner: { text: "Understands and respects others' needs, views and actions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand and respect other people's needs, views and actions.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.collaborative.b3
  forPractitioner: { text: "Handles conflict in a group.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You handle disagreement in a group.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.collaborative.b4
  forPractitioner: { text: "Facilitates problem-solving that involves everyone.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You help a group solve problems together.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.problem.b1
  forPractitioner: { text: "Applies a range of problem-solving frameworks to complex sustainability problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use different problem-solving methods on complex sustainability problems.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.problem.b2
  forPractitioner: { text: "Develops workable, inclusive and fair solutions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You develop solutions that work and are fair to everyone.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.problem.b3
  forPractitioner: { text: "Uses the right competencies to solve problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You bring the right abilities to bear on a problem.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.selfaware.b1
  forPractitioner: { text: "Reflects on own values, perceptions and actions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your values, views and actions.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.selfaware.b2
  forPractitioner: { text: "Reflects on own role in the local community and in global society.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your part in your community and in the wider world.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.selfaware.b3
  forPractitioner: { text: "Keeps evaluating own actions and the motivation behind them.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You keep reviewing what you do and what drives you.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.selfaware.b4
  forPractitioner: { text: "Deals with own feelings and desires.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You manage your feelings and wishes.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.normative.b1
  forPractitioner: { text: "Understands and reflects on the norms and values behind own actions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand and reflect on the values behind what you do.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/competency.normative.b2
  forPractitioner: { text: "Negotiates sustainability values, principles, goals and targets amid conflicting interests, trade-offs, uncertainty and contradiction.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You negotiate sustainability values and goals where interests clash and knowledge is uncertain.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/narrative.strategic.1
  forPractitioner: { text: "Strategic competency takes in core employability skills: setting goals, managing time and resources, and carrying out and evaluating a plan of action.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Planning for sustainability builds skills employers look for in you: setting goals, managing time and resources, and carrying out and reviewing a plan.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/narrative.strategic.2
  forPractitioner: { text: "Effective strategists work with stakeholders to plan and run change projects by consultation and by producing, creating or delivering them jointly.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You work with the people affected to plan and run change projects together.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/narrative.collaborative.1
  forPractitioner: { text: "Graduates are expected to communicate well, ethically and professionally, with colleagues, clients and stakeholders across media, disciplines, cultures, borders and digital interfaces.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be expected to communicate well and ethically with colleagues, clients and others, across subjects, cultures, countries and digital tools.", rewrite: full, force: will, status: drafted }
- statement: qaa-advancehe/esd-2021/narrative.collaborative.2
  forPractitioner: { text: "Learners should get the chance to form visions, analyse possible solutions, carry out sustainability assessments and build strategies with stakeholders whose views and priorities differ.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should get the chance to form visions, test solutions, assess sustainability and plan with people who see things differently.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/narrative.problem.1
  forPractitioner: { text: "Students widen their problem-solving by drawing knowledge and research methods from other subjects to develop and judge workable solutions to authentic problems.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You widen your problem-solving by borrowing knowledge and research methods from other subjects to tackle real problems.", rewrite: full, force: will, status: drafted }
- statement: qaa-advancehe/esd-2021/narrative.selfaware.1
  forPractitioner: { text: "By recognising their own situation, students can gain agency and responsibility for sustainable action in their community or society.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By understanding your own situation, you gain the sense that you can and should act for sustainability where you live.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/narrative.normative.1
  forPractitioner: { text: "Drawing on justice, equity, inclusion and responsibility, students can spot biases and barriers that hold back sustainable action.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Using ideas of justice and fairness, you learn to spot the biases and barriers that block sustainable action.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.k1
  forPractitioner: { text: "Describes how environmental, social and economic systems relate, from local to global scale.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You describe how the environment, society and the economy connect, locally and globally.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.k2
  forPractitioner: { text: "Identifies where the 17 SDGs pull against each other and how they connect.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You spot where the 17 global goals conflict and how they link up.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.k3
  forPractitioner: { text: "Recognises that collective effort is more than the sum of individual efforts, with personal, political or communal drivers.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You see that people acting together is more complex than adding up what each does, with personal and political causes.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.k4
  forPractitioner: { text: "Identifies that economic growth can bring environmental change for better or worse.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You recognise that economic growth can help or harm the environment.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.k5
  forPractitioner: { text: "Describes how power and political systems shape sustainable development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You explain how power and politics shape sustainability.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.s1
  forPractitioner: { text: "Recognises and understands relationships.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You see and understand how things relate.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.s2
  forPractitioner: { text: "Analyses complex systems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You analyse complex systems.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.s3
  forPractitioner: { text: "Considers how a system's parts interact and work at different scales and over time.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You think about how the parts of a system work together, at different scales and over time.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.s4
  forPractitioner: { text: "Works with interconnection and complexity, combining varied information and data into a range of possible solutions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You handle connected, complex situations, pulling together varied data to suggest several solutions.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.s5
  forPractitioner: { text: "Identifies interactions between social, economic and environmental systems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You identify how social, economic and environmental systems affect one another.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.s6
  forPractitioner: { text: "Assesses a problem at different scales and from different viewpoints.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You look at a problem at different scales and from different points of view.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.a1
  forPractitioner: { text: "Thinks in systems: sees connections between factors and knows that actions have many consequences.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You think in systems, seeing links between factors and the knock-on effects of actions.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.a2
  forPractitioner: { text: "Deals with and manages uncertainty.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You cope with and manage uncertainty.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.a3
  forPractitioner: { text: "Appreciates the root causes of unsustainable development across environment, society and economy, and their cultural links.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand what really drives unsustainable development and how culture is involved.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.systems.a4
  forPractitioner: { text: "Identifies the factors most likely to drive constructive change.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You pick out what could do most to bring about positive change.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.k1
  forPractitioner: { text: "Identifies risks in complex systems that can bring unintended consequences or harmful cumulative effects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You identify risks in complex systems that could cause unexpected or growing harm.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.k2
  forPractitioner: { text: "Evaluates the effects and links between what different generations, groups and cultures do, recognising tensions between them.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You weigh up how different generations, groups and cultures affect each other, and where they clash.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.k3
  forPractitioner: { text: "Identifies causes of, and possible remedies for, inequity within and across generations worldwide.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You identify why inequality exists within and across generations and what could reduce it.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.k4
  forPractitioner: { text: "Identifies that natural systems have fixed limits and may destabilise or collapse under too much pressure or change.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know that nature has fixed limits and can break down under too much pressure.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.k5
  forPractitioner: { text: "Identifies risks and uncertainties in transforming the natural environment.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You identify the risks and unknowns of changing the natural environment.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.k6
  forPractitioner: { text: "Identifies that decisions on natural resources must weigh ecological, social and cultural risk to the future, not only economic return.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You see that decisions about natural resources must weigh future harm to nature and people, not just profit.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.s1
  forPractitioner: { text: "Generates and evaluates approaches to sustainable development and judges their likely effect in own subject.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You come up with and judge different ways to tackle sustainability in your subject.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.s2
  forPractitioner: { text: "Uses history and the results of past actions to picture how futures may be shaped.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use history and what past actions led to, to imagine how the future could turn out.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.s3
  forPractitioner: { text: "Develops, understands and evaluates several possible outcomes.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You work out and weigh up several possible outcomes.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.s4
  forPractitioner: { text: "Creates own visions of the future.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You form your own vision of the future.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.s5
  forPractitioner: { text: "Applies the precautionary principle.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You act with caution where harm is possible but not yet understood.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.s6
  forPractitioner: { text: "Assesses the consequences of actions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You judge what actions will lead to.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.s7
  forPractitioner: { text: "Evaluates risks and their possible impact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You weigh up risks and what they could do.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.s8
  forPractitioner: { text: "Identifies future scenarios and uses them in decisions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You sketch possible futures and use them to make decisions.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.s9
  forPractitioner: { text: "Uses backcasting: defines a desirable future, then works back to the policies and programmes that lead there from now.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You start from the future you want and work back to the steps that get there.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.s10
  forPractitioner: { text: "Uses forecasting: projects likely outcomes from past trends and present conditions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You project likely futures from past trends and present conditions.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.a1
  forPractitioner: { text: "Is flexible, resourceful and adaptable to changing or unexpected circumstances where that serves sustainability.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You stay flexible and resourceful when things change unexpectedly, if that helps sustainability.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.a2
  forPractitioner: { text: "Imagines sustainable futures.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You imagine what a sustainable future could look like.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.a3
  forPractitioner: { text: "Considers the good and bad effects of heritage and culture when planning ahead.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You think about how heritage and culture help or hinder when planning for the future.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.a4
  forPractitioner: { text: "Applies fairness between generations to decisions and plans.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You keep fairness to future generations in mind when deciding and planning.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.a5
  forPractitioner: { text: "Is ready to learn from others and take their views into account.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are ready to learn from other people and consider their views.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.a6
  forPractitioner: { text: "Learns to set aside what it knows when a situation calls for other solutions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to let go of what you know when a situation needs a new answer.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.anticipatory.a7
  forPractitioner: { text: "Shows openness to new ways of solving problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You stay open to new ways of solving problems.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.k1
  forPractitioner: { text: "Uses scientific evidence and scholarship to understand sustainable development and human effects on it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use scientific evidence and research to understand sustainability and how people affect it.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.k2
  forPractitioner: { text: "Identifies the case for changing behaviour where current practice is shown to harm people or nature.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can explain why behaviour should change where it is shown to harm people or nature.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.k3
  forPractitioner: { text: "Identifies people who have driven positive change and learns from their practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You find people who have made a positive difference and learn from how they did it.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.s1
  forPractitioner: { text: "Presents a concept in simplified form.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You explain an idea simply.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.s2
  forPractitioner: { text: "Identifies and frames critical questions and problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You find and frame the questions and problems that matter.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.s3
  forPractitioner: { text: "Assesses new information and keeps folding it into developing models.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You judge new information and keep building it into your thinking.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.s4
  forPractitioner: { text: "Critically assesses and analyses sustainability issues in own subject or intended profession.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You critically analyse sustainability issues in your subject or the career you plan.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.s5
  forPractitioner: { text: "Analyses, synthesises and evaluates data to reach reasoned conclusions and solutions, tested against criteria and standards.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You analyse and combine data to reach sound conclusions, and test them against agreed standards.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.s6
  forPractitioner: { text: "Tells evidence-based conclusions apart from opinion and guesswork.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You tell conclusions based on evidence apart from opinion and guesswork.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.a1
  forPractitioner: { text: "Shows independent, evidence-based, joined-up thinking as the base for a personal ethical code.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You think independently from evidence, as the base for your own ethics.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.a2
  forPractitioner: { text: "Evaluates the consequences of own and collective actions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You judge the effects of what you and others do together.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.a3
  forPractitioner: { text: "Reflects on own values, views and actions against those of influential others.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your values and actions and compare them with those of people with influence.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.a4
  forPractitioner: { text: "Takes a position in sustainability debates grounded in evidence.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You take a stand in sustainability debates and back it with evidence.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.critical.a5
  forPractitioner: { text: "Recognises own assumptions and evaluates what follows from them.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You notice your own assumptions and think through where they lead.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.k1
  forPractitioner: { text: "Identifies the root causes of unsustainable development in environment, society and economy.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You identify what really drives unsustainable development.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.k2
  forPractitioner: { text: "Understands how awareness of emotion and thought affects decisions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand how your feelings and thinking affect your decisions.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.k3
  forPractitioner: { text: "Identifies, then makes, changes to actions or behaviour where current practice does harm.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You spot harmful habits and change them.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.k4
  forPractitioner: { text: "Appreciates how own discipline helps or hinders sustainable development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand how your subject helps or harms sustainability.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.k5
  forPractitioner: { text: "Understands the risks and uncertainties of transforming the natural environment.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the risks and unknowns of changing the natural environment.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.s1
  forPractitioner: { text: "Links environmental, social and economic action to cultural factors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You connect environmental, social and economic action with culture.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.s2
  forPractitioner: { text: "Evaluates the effects and links between what different generations, groups and cultures do, recognising competing factors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You judge how different generations, groups and cultures affect each other, and what competes between them.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.s3
  forPractitioner: { text: "Identifies strategies that help stakeholders discuss and resolve dilemmas and conflicts.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You find ways to help the people involved talk through and settle disagreements.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.s4
  forPractitioner: { text: "Develops and carries out new actions that advance sustainable development locally and beyond.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You plan and carry out new actions for sustainability, locally and further away.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.s5
  forPractitioner: { text: "Uses planning and assessment tools to find and tackle sustainability challenges and opportunities.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use planning and assessment tools to find and tackle sustainability problems and chances.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.a1
  forPractitioner: { text: "Practises making decisions and analyses what follows from them.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You practise making decisions and look at what they lead to.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.a2
  forPractitioner: { text: "Reflects on actions and behaviour.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on what you do and how you behave.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.a3
  forPractitioner: { text: "Brings thinking together as the base for a personal ethical code.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You bring your thinking together to form your own ethics.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.a4
  forPractitioner: { text: "Shows flexibility and resourcefulness, adapting a problem-solving approach to changing or unexpected circumstances.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You stay flexible and resourceful, adapting how you solve problems when things change.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.strategic.a5
  forPractitioner: { text: "Shows commitment to learning throughout life.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show you will keep learning throughout your life.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.k1
  forPractitioner: { text: "Understands the value of working with people who bring different knowledge, views and experience.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand why it helps to work with people who know and see things differently.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.k2
  forPractitioner: { text: "Identifies and critiques different ways of collaborating.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You compare and critique different ways of working together.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.k3
  forPractitioner: { text: "Recognises strategies for managing groups.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know ways of managing a group.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.k4
  forPractitioner: { text: "Recognises verbal and non-verbal communication and its part in group cohesion.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You notice how spoken and unspoken communication holds a group together.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.k5
  forPractitioner: { text: "Recognises others' goals, skills and needs as part of collaborating well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You recognise what others aim for, can do and need when you work together.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.s1
  forPractitioner: { text: "Communicates well by listening, expressing ideas clearly and asking constructive questions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate well: you listen, speak clearly and ask useful questions.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.s2
  forPractitioner: { text: "Joins discussion across disciplines to inform thinking on sustainable futures and find whole, creative solutions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You discuss problems with people from other subjects to find fuller, creative answers.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.s3
  forPractitioner: { text: "Identifies why people and organisations should be helped to work together to create new knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You see why helping people and organisations work together creates new knowledge.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.s4
  forPractitioner: { text: "Communicates complex sustainability issues clearly.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You explain complex sustainability issues clearly.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.s5
  forPractitioner: { text: "Facilitates and mediates stakeholder discussion to help resolve dilemmas and conflicts.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You lead and mediate discussions between the people involved to help settle disagreements.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.s6
  forPractitioner: { text: "Listens actively and critically.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You listen actively and critically.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.s7
  forPractitioner: { text: "Connects, adapts and synthesises learning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You connect, adapt and combine what you learn.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.s8
  forPractitioner: { text: "Addresses conflict and builds mediation skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You tackle conflict and build skills in mediating.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.s9
  forPractitioner: { text: "Uses fitting styles of leadership.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You lead in the way the situation needs.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.a1
  forPractitioner: { text: "Learns from others: peers, professionals, expert groups and communities.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn from others: classmates, professionals, experts and communities.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.a2
  forPractitioner: { text: "Handles conflict in a group.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You handle disagreement in a group.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.a3
  forPractitioner: { text: "Facilitates problem-solving that involves everyone.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You help a group solve problems together.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.a4
  forPractitioner: { text: "Helps others through peer learning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You help others learn alongside you.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.a5
  forPractitioner: { text: "Questions norms, practices and opinions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You question accepted ways, practices and views.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.a6
  forPractitioner: { text: "Understands and respects others' needs, views and actions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand and respect other people's needs, views and actions.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.a7
  forPractitioner: { text: "Empathises with others' views and experience.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You put yourself in other people's shoes.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.collaborative.a8
  forPractitioner: { text: "Collaborates fairly across gender, ethnicity and other groups.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You work fairly with people whatever their gender, ethnicity or background.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.k1
  forPractitioner: { text: "Describes how own discipline could link with others to make creative leaps.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You describe how your subject could join with others to make creative leaps.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.k2
  forPractitioner: { text: "Describes how own field contributes to sustainable development and links to the SDGs.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You describe how your subject contributes to sustainability and the global goals.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.k3
  forPractitioner: { text: "Appreciates other disciplines' research methods.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You value the research methods of other subjects.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.k4
  forPractitioner: { text: "Understands a discipline's academic norms and explores its integrity.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand how your subject works as a discipline and what keeps it sound.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.s1
  forPractitioner: { text: "Applies established frameworks and methods, from own field, to analyse the effects of a behaviour or process.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use established methods from your subject to analyse what a behaviour or process does.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.s2
  forPractitioner: { text: "Applies a range of problem-solving frameworks to complex sustainability problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use different problem-solving methods on complex sustainability problems.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.s3
  forPractitioner: { text: "Develops workable, inclusive and fair solutions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You develop solutions that work and are fair to everyone.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.s4
  forPractitioner: { text: "Engages well with real sustainability problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You work on real sustainability problems.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.s5
  forPractitioner: { text: "Combines evidence of different kinds and from different disciplines to see and tackle a problem.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You combine different kinds of evidence, from different subjects, to tackle a problem.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.a1
  forPractitioner: { text: "Uses the right competencies to identify and solve problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You bring the right abilities to finding and solving problems.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.a2
  forPractitioner: { text: "Communicates well with others to find solutions to complex problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate well with others to find solutions to complex problems.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.a3
  forPractitioner: { text: "Listens critically to other ideas, frameworks and systems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You listen critically to other ideas and ways of thinking.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.a4
  forPractitioner: { text: "Works well in teams drawn from several disciplines.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You work well in teams that mix subjects.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.problem.a5
  forPractitioner: { text: "Considers other disciplines' norms and ways of thinking and uses them where they fit.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You consider how other subjects think and use their approaches where they fit.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.selfaware.k1
  forPractitioner: { text: "Identifies and evaluates own competences and learning needs.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You work out what you can do and what you still need to learn.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.selfaware.k2
  forPractitioner: { text: "Understands own heritage and culture.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand your own heritage and culture.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.selfaware.k3
  forPractitioner: { text: "Identifies why empowering people and organisations to collaborate matters.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You see why it matters to help people and organisations work together.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.selfaware.k4
  forPractitioner: { text: "Understands how power and political systems shape sustainable development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand how power and politics shape sustainability.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.selfaware.k5
  forPractitioner: { text: "Identifies the range of human cultures and the opportunities and difficulties each brings for sustainable development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know how varied human cultures are and how each can help or hinder sustainability.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.selfaware.s1
  forPractitioner: { text: "Leads for sustainability by challenging assumptions and negotiating alternatives to unsustainable practice, especially in own field.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You lead for sustainability by challenging assumptions and agreeing better ways of doing things, especially in your subject.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.selfaware.s2
  forPractitioner: { text: "Makes or helps make changes for sustainability within own learning and study setting.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make or support changes for sustainability where you study.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.selfaware.s3
  forPractitioner: { text: "Takes responsibility for own learning and skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You take charge of your own learning and skills.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.selfaware.s4
  forPractitioner: { text: "Facilitates and mediates stakeholder discussion to resolve dilemmas and conflicts.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You lead and mediate discussions to help settle disagreements.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.selfaware.a1
  forPractitioner: { text: "Clarifies own views on how sustainable development can be reached in different communities and settings.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You get clear about your own views on how sustainability can be reached in different places.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.selfaware.a2
  forPractitioner: { text: "Engages with own and other cultures and heritages.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You explore your own and other cultures and heritages.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.selfaware.a3
  forPractitioner: { text: "Looks after own mental and emotional health and stays aware of it, so as to reflect on values and role, review and motivate actions, engage with emotions and find meaning in work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You look after your mental and emotional health so you can reflect, stay motivated, notice your feelings and find meaning in your work.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.normative.k1
  forPractitioner: { text: "Identifies the range of human cultures and the opportunities and difficulties each brings for sustainable development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know how varied human cultures are and how each can help or hinder sustainability.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.normative.k2
  forPractitioner: { text: "Shows that practices, sustainable or not, sit in a changing context that calls for adaptable policy and planning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show that practices change over time, so policy and planning must adapt.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.normative.k3
  forPractitioner: { text: "Identifies how human communities and ecosystems interact and assesses their effects on each other.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You identify how people and ecosystems interact and judge their effects on each other.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.normative.k4
  forPractitioner: { text: "Identifies ethical questions and uses ethical frameworks.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You spot ethical questions and use ethical frameworks to think them through.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.normative.k5
  forPractitioner: { text: "Identifies practical interventions for sustainability challenges.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You identify practical actions for sustainability problems.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.normative.s1
  forPractitioner: { text: "Tackles and negotiates sustainability conflicts aware of differing views and motives.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You work through sustainability conflicts, aware of what each side wants and why.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.normative.s2
  forPractitioner: { text: "Identifies chances to build a forward-looking, resilient culture in which citizens, professions and institutions act on what they learn.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You find chances to build a culture where people and organisations act on what they learn.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.normative.s3
  forPractitioner: { text: "Debates and explores fairness and justice, social justice included.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You debate fairness and justice, including social justice.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.normative.s4
  forPractitioner: { text: "Develops alternative solutions that open new ways to engage with sustainable development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You develop other solutions that open new ways into sustainability.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.normative.a1
  forPractitioner: { text: "Negotiates sustainability values, principles, goals and targets amid conflicting interests, trade-offs, uncertainty and contradiction.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You negotiate sustainability values and goals where interests clash and knowledge is uncertain.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.normative.a2
  forPractitioner: { text: "Understands and reflects on the norms and values behind own actions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand and reflect on the values behind what you do.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.normative.a3
  forPractitioner: { text: "Engages with and understands different world views.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You engage with and understand world views unlike your own.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/outcome.normative.a4
  forPractitioner: { text: "Appreciates, critiques and values different cultural contexts.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You appreciate, question and value different cultural settings.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/design.1
  forPractitioner: { text: "Course and module outcomes for ESD should join subject knowledge and skills with the sustainability competencies and the SDGs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course and module outcomes should link your subject with sustainability skills and the global goals.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/design.2
  forPractitioner: { text: "Table 2's outcomes are indicative: educators choose and adapt them to the discipline, context, level and credit of a module.", rewrite: light, force: may, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa-advancehe/esd-2021/students.b1
  forPractitioner: { text: "Decide what ESD understanding and experience every student should gain and write it into course outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should set out what every student learns about sustainability.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/students.b2
  forPractitioner: { text: "Plan the ESD offered so it builds year on year.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "What you learn about sustainability should build from one year to the next.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/students.b3
  forPractitioner: { text: "Give students chances, such as volunteering and extracurricular activity, to put ESD into practice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should get chances, such as volunteering, to put what you learn about sustainability into practice.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/students.b4
  forPractitioner: { text: "Cover ESD at induction: what the institution does and how students can join in.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At induction you should hear what your university does on sustainability and how you can take part.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/students.b5
  forPractitioner: { text: "Support students who want sustainability to shape their career plans.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you want sustainability to shape your career, you should get support to do that.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/students.b6
  forPractitioner: { text: "Have careers services tell students how potential employers perform socially and environmentally.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Careers advice should tell you how employers perform on social and environmental issues.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/students.b7
  forPractitioner: { text: "Support students to build enterprise skills that could lead to ventures serving sustainable development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should get support to build enterprise skills that could lead to a venture that helps sustainability.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/students.b8
  forPractitioner: { text: "Include ESD in module, course, placement and work-experience feedback.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be asked about sustainability in feedback on modules, courses and placements.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/employers.b1
  forPractitioner: { text: "Give every graduate a chance to help shape solutions to sustainability challenges, inside and outside the institution.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should get the chance to help solve sustainability problems, on and off campus.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/employers.b2
  forPractitioner: { text: "Partner with enterprising people and firms to provide living labs, cases, experiential learning, simulations and research projects.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You may learn through projects, simulations and live cases run with businesses and entrepreneurs.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/employers.b3
  forPractitioner: { text: "Prepare graduates to help future employers meet sustainability challenges, valuing creativity and readiness to try new approaches.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should leave ready to help your future workplace meet sustainability challenges, with creativity and a willingness to try new things.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/academics.b1
  forPractitioner: { text: "Understand ESD and the SDGs in their own subject and its professions, including how the subject may perpetuate unjust or unsustainable thinking.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa-advancehe/esd-2021/academics.b2
  forPractitioner: { text: "Understand the eight competencies and build them into course and module outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa-advancehe/esd-2021/academics.b3
  forPractitioner: { text: "Use teaching and assessment that develop and assess the competencies.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa-advancehe/esd-2021/academics.b4
  forPractitioner: { text: "Teach and assess across disciplines.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa-advancehe/esd-2021/academics.b5
  forPractitioner: { text: "Share ESD ideas and experience across the institution.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa-advancehe/esd-2021/academics.b6
  forPractitioner: { text: "Talk with key players to extend ESD beyond the curriculum.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa-advancehe/esd-2021/services.b1
  forPractitioner: { text: "Quality staff know ESD and how to help place it in curricula.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa-advancehe/esd-2021/services.b2
  forPractitioner: { text: "Validation and review templates ask for real evidence of ESD in courses and modules.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa-advancehe/esd-2021/services.b3
  forPractitioner: { text: "Evaluate ESD's impact to show outcomes and drive enhancement.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa-advancehe/esd-2021/communities.b1
  forPractitioner: { text: "Let students work with communities of practice and local communities to contribute to sustainable development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should get to work with communities, local or professional, to help sustainability.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/environment.b1
  forPractitioner: { text: "Learning across disciplines is made possible.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can learn alongside other subjects.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/environment.b2
  forPractitioner: { text: "Learning is inclusive and accessible to everyone.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your learning is open and accessible to you, whoever you are.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/environment.b3
  forPractitioner: { text: "Policies allow synoptic assessment.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa-advancehe/esd-2021/environment.b4
  forPractitioner: { text: "Extracurricular and co-curricular activity is offered and recognised.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Activities outside your course are offered and count.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/environment.b5
  forPractitioner: { text: "The campus, outdoors and other spaces are used to develop and show the competencies.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your campus and outdoor spaces are used as places to learn.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/environment.b6
  forPractitioner: { text: "Use the campus, local community and online spaces as learning opportunities, such as a living laboratory.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your campus, local community and online spaces can all be places where you learn.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/environment.b7
  forPractitioner: { text: "Widen reading lists and resources to include diverse voices and underrepresented communities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your reading should include diverse voices, including those often left out.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/assessment.b1
  forPractitioner: { text: "Use group work, in and beyond the course, to build collaborative competency through discussion with peers and stakeholders.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You will work in groups, on and beyond your course, discussing problems with others.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/assessment.b2
  forPractitioner: { text: "Use games and simulation so students can explore scenarios, take risks, try new approaches and learn from failure.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You may use games and simulations to try ideas, take risks and learn from failure.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/assessment.b3
  forPractitioner: { text: "Give students chances to reflect critically on their own views and others', and what shaped them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You get chances to reflect on your own views and others', and on what shaped them.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/assessment.b4
  forPractitioner: { text: "Competencies develop over time, so assess formatively and focus on process more than product.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Because these abilities grow over time, feedback along the way and attention to how you work matter more than the end product.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021/assessment.b5
  forPractitioner: { text: "Write criteria that value how students reached a workable solution above the solution itself.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your marks should reward how you reached a workable answer, more than the answer itself.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/assessment.b6
  forPractitioner: { text: "Use authentic formats (blogs, vlogs, websites, wikis) that let students show and share their learning with stakeholders.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You may be assessed through blogs, videos, websites or wikis that show your learning to real audiences.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021/assessment.b7
  forPractitioner: { text: "Competencies can also be built outside the curriculum and evidenced through micro-credentials, badges, CVs, online profiles, development planning or the HEAR.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can build these abilities outside your course too, and show them on your CV, online profile, digital badges or HEAR.", rewrite: full, force: describes, status: drafted }
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary for the absence of levels; inferred for the alignment -->
No levels. The guidance says its Table 2 outcomes are indicative, not a checklist, and that educators should select and adapt them to the discipline, context, level and credit of each module (`design.2`). So the guidance hands levelling to the course designer. GU2 gives a verb-level profile of the outcomes and a suggested ladder; GU4 lists the framework statements records most resemble.

### S6 Themes
`theme:esd` (this document is the theme's reference text); `theme:enterprise` (the employers section names enterprise competencies as a catalyst for sustainable change and cites the enterprise guidance, std:doc:qaa-enterprise-2018-guidance); `theme:edi` (Figure 2 places equality, diversity and inclusion, with decolonisation, among the priorities ESD intersects; collaborative outcomes ask for equitable collaboration); employability (strategic competency is said to include core employability skills; GU3).

### S7 Relations
```yaml
- { type: themeReference, target: theme:esd }
- { type: supersedes, target: "QAA and HEA ESD guidance 2014 (not held)" }
- { type: summarisedBy, target: std:doc:qaa-advancehe-esd-2021-execsummary, basis: primary }
- { type: cites, target: std:doc:qaa-enterprise-2018-guidance, note: "employers and enterprise section; Section 4 resources", basis: primary }
- { type: readWith, target: "the QAA subject benchmark statements (S2)", basis: primary }
- { type: citedBy, target: "49 of the 54 subject benchmark statements held cite ESD guidance by title (GU6)", basis: primary }
- { type: mapsTo, target: std:doc:qaa-fheq-2024-framework, basis: inferred, note: "39 records linked (GU4)" }
- { type: mapsTo, target: std:doc:bristol-generic-2024-assesscriteria, basis: inferred }
- { type: mapsTo, target: std:doc:cardiffmet-generic-2020-assesscriteria, basis: inferred }
- { type: overlaps, target: std:doc:qaa-enterprise-2018-guidance, basis: inferred, note: "GU2 crosswalk" }
- { type: handsTo, target: "theory ingest (ing): the pedagogy in GU7" }
```

### S8 Currency and review
<!-- label: both; status: drafted; basis: primary -->
Second edition, March 2021, after sector consultation from November 2020 to January 2021; replaces the 2014 guidance. Any later revision is unchecked (E1).

### S9 Commentary (optional)
<!-- label: practitioner; status: drafted; basis: inferred -->
This is the richest student-facing standards source we hold outside the frameworks: 128 outcomes, each a plain "a student can" statement, already sorted into knowledge, skills and attributes and values. That three-way split is one the frameworks only half have (knowledge and skills; no values). Its weakness as a standard is that it is level-free and, by its own words, indicative. Its strength is that it is ready to use as learning-outcome text, and that it says how: adapt to level and credit, assess process over product.

## Part GU Guidance analysis

### GU1 Statement families
<!-- The kinds of standards assertion the guidance makes, by family: who it addresses, its usual force, and how many records. -->

| Family | Heading | Records | Addressee | Force | Student versions |
|---|---|---|---|---|---|
| aim | Aims: what ESD is about | 4 | provider, student | describes, must | 4 |
| principle | Guidance: ESD is best achieved when | 5 | provider | describes | 2 |
| competency | Table 1: UNESCO key competencies for sustainability (a student who displays this competency can) | 26 | student | describes | 26 |
| narrative | Section 3: the competencies described | 7 | educator, graduate, student | describes, should, will | 7 |
| outcome | Table 2: learning outcomes aligned with key competencies (a student with this competency can) | 128 | student | describes | 128 |
| design | Course and module learning outcomes for ESD | 2 | educator | may, should | 1 |
| students | Consulting key players: students (guidance) | 8 | educator | should | 8 |
| employers | Consulting key players: employers and enterprise (guidance) | 3 | educator | should | 3 |
| academics | Consulting key players: academics (guidance) | 6 | educator | should | 0 |
| services | Consulting key players: professional services and governance (guidance) | 3 | provider | should | 0 |
| communities | Consulting key players: communities (guidance) | 1 | educator | should | 1 |
| environment | Developing learning environments to support ESD | 7 | educator, provider | describes, should | 6 |
| assessment | Teaching and assessment practice (guidance) | 7 | educator | describes, should | 7 |

### GU2 Progression
<!-- label: both; status: drafted; basis: primary for the three ways; inferred for the verb profile and levels -->
The guidance's model of growth is a transformative journey through three ways: thinking (systems, anticipatory, critical), practising (strategic, collaborative, integrated problem-solving) and being (self-awareness, normative), all resting on subject knowledge and knowledge of the SDGs (Table 1's frame). It names no stages and no levels.

**Verb-level profile of Table 2** (ours). Each outcome's first verb placed on the FHEQ document's verb ladder (std:doc:qaa-fheq-2024-framework, SL3): L4 know and describe (identify, recognise, understand, describe, appreciate); L5 apply and analyse (use, apply, analyse, consider, communicate, engage); L6 evaluate and judge (evaluate, assess, develop, demonstrate, reflect, take a position); L7 lead and negotiate under uncertainty (negotiate, facilitate, mediate, implement, lead); disposition (be, deal with, imagine, empathise, maintain).

| Competency | Column | Outcomes | L4 | L5 | L6 | L7 | Disposition |
|---|---|---|---|---|---|---|---|
| systems thinking | Knowledge | 5 | 5 | 0 | 0 | 0 | 0 |
| systems thinking | Skills | 6 | 2 | 3 | 1 | 0 | 0 |
| systems thinking | Attributes and values | 4 | 2 | 0 | 1 | 0 | 1 |
| anticipatory thinking | Knowledge | 6 | 5 | 0 | 1 | 0 | 0 |
| anticipatory thinking | Skills | 10 | 1 | 4 | 5 | 0 | 0 |
| anticipatory thinking | Attributes and values | 7 | 0 | 4 | 1 | 0 | 2 |
| critical thinking | Knowledge | 3 | 2 | 1 | 0 | 0 | 0 |
| critical thinking | Skills | 6 | 1 | 2 | 3 | 0 | 0 |
| critical thinking | Attributes and values | 5 | 1 | 0 | 4 | 0 | 0 |
| strategic thinking | Knowledge | 5 | 5 | 0 | 0 | 0 | 0 |
| strategic thinking | Skills | 5 | 1 | 2 | 2 | 0 | 0 |
| strategic thinking | Attributes and values | 5 | 0 | 2 | 3 | 0 | 0 |
| collaborative | Knowledge | 5 | 5 | 0 | 0 | 0 | 0 |
| collaborative | Skills | 9 | 1 | 5 | 2 | 1 | 0 |
| collaborative | Attributes and values | 8 | 1 | 3 | 1 | 1 | 2 |
| integrated problem-solving | Knowledge | 4 | 4 | 0 | 0 | 0 | 0 |
| integrated problem-solving | Skills | 5 | 0 | 4 | 1 | 0 | 0 |
| integrated problem-solving | Attributes and values | 5 | 0 | 4 | 1 | 0 | 0 |
| self-awareness | Knowledge | 5 | 5 | 0 | 0 | 0 | 0 |
| self-awareness | Skills | 4 | 0 | 0 | 1 | 3 | 0 |
| self-awareness | Attributes and values | 3 | 1 | 0 | 1 | 0 | 1 |
| normative | Knowledge | 5 | 4 | 0 | 1 | 0 | 0 |
| normative | Skills | 4 | 1 | 1 | 1 | 1 | 0 |
| normative | Attributes and values | 4 | 2 | 1 | 0 | 1 | 0 |
| **all** | **Knowledge** | **38** | **35** | **1** | **2** | **0** | **0** |
| **all** | **Skills** | **49** | **7** | **21** | **16** | **5** | **0** |
| **all** | **Attributes and values** | **41** | **7** | **14** | **12** | **2** | **6** |

**Reading.** The knowledge column sits mostly at L4 ("identify" alone opens 26 outcomes across the table); the skills column runs mostly at L5 and L6, with five at L7; the attributes and values column mixes judgement with dispositions. So each competency's three columns already form a rough ladder, knowledge first, then skills, then values. But within a column the levels are mixed, and nothing tells a designer which outcome suits which year. The frameworks' level language (independence, complexity, uncertainty) is what is missing.

**Suggestion: a levelled ladder for three competencies** (ours, `suggested`), built from Table 2's own outcomes:

| Competency | L4 | L5 | L6 | L7 |
|---|---|---|---|---|
| systems thinking | describe how environmental, social and economic systems relate (`outcome.systems.k1`) | analyse a complex system in your subject (`s2`, `s3`) | combine varied data into a range of solutions and judge them (`s4`) | identify the levers with most potential for change and act on them under uncertainty (`a4`, `a2`) |
| critical thinking | identify the case for behaviour change (`k2`) | critically analyse a sustainability issue in your subject (`s4`) | reach and test reasoned conclusions; take an evidenced position (`s5`, `a4`) | build a personal ethical code on independent, evidence-based thinking (`a1`) |
| collaborative | recognise group strategies and communication (`k3`, `k4`) | communicate clearly and listen critically (`s1`, `s6`) | work across disciplines towards creative solutions (`s2`) | facilitate and mediate stakeholder conflict; lead (`s5`, `s9`) |

**Crosswalk to the enterprise guidance** (std:doc:qaa-enterprise-2018-guidance; ours). With the full text the overlap is clearer than the summary showed:

| ESD competency | Enterprise outcome theme | Shared ground (record ids) |
|---|---|---|
| systems thinking | decision | analysing and synthesising complex information (`outcome.systems.s4`; enterprise `outcome.decision.b3`) |
| anticipatory thinking | communication; opportunity | visualising futures; reviewing solutions under uncertainty and risk (`outcome.anticipatory.s1`, `s8`, `s9`) |
| critical thinking | decision | evaluating information and building arguments (`outcome.critical.s5`) |
| strategic thinking | implementation; decision | planning and resource management; "core employability skills" (`narrative.strategic.1`) |
| collaborative | communication; implementation | stakeholders, trust, negotiation, leadership (`outcome.collaborative.s5`, `s9`) |
| integrated problem-solving | creativity; opportunity | several solutions for real problems (`outcome.problem.s2` to `s4`) |
| self-awareness | reflection; the mindset family | own competences and learning needs; motivation (`outcome.selfaware.k1`, `s3`) |
| normative | (none) | the enterprise guidance names ethics but has no values competency |

Seven of the eight have an enterprise counterpart; only normative competency is ESD's own (the summary's reading had two). The ESD guidance makes the link itself: enterprise education, it says, can build qualities such as creativity, spotting opportunities, self-determination and adaptability that speed sustainable change.


### GU3 Employability
<!-- Each record tagged: `direct` names work, careers, employers or ventures; `bridge` is a capability that study and work share; `academic` stays within study. Our reading. -->

| Tag | Records | Categories |
|---|---|---|
| direct | 39 | skill 20, opportunity 7, knowledge 4, competency 3, attribute-value 3, assessment 2 |
| bridge | 110 | attribute-value 33, competency 28, skill 25, knowledge 11, aim 4, opportunity 4, assessment 4, mindset 1 |
| academic | 58 | knowledge 23, institution 13, educator 6, attribute-value 5, skill 4, opportunity 4, outcome-design 2, assessment 1 |

**Direct statements:** `narrative.strategic.1`; `narrative.strategic.2`; `narrative.collaborative.1`; `outcome.anticipatory.s5`; `outcome.anticipatory.s7`; `outcome.anticipatory.s8`; `outcome.anticipatory.s9`; `outcome.anticipatory.s10`; `outcome.critical.s4`; `outcome.strategic.k4`; `outcome.strategic.s3`; `outcome.strategic.s4`; `outcome.strategic.s5`; `outcome.strategic.a5`; `outcome.collaborative.k3`; `outcome.collaborative.s3`; `outcome.collaborative.s4`; `outcome.collaborative.s5`; `outcome.collaborative.s8`; `outcome.collaborative.s9`; `outcome.collaborative.a8`; `outcome.problem.s1`; `outcome.problem.s4`; `outcome.problem.a4`; `outcome.selfaware.s1`; `outcome.selfaware.s4`; `outcome.normative.k4`; `outcome.normative.k5`; `outcome.normative.s1`; `outcome.normative.s2`; `students.b5`; `students.b6`; `students.b7`; `employers.b1`; `employers.b2`; `employers.b3`; `communities.b1`; `assessment.b6`; `assessment.b7`.

**Reading.** Of 207 records, 39 are direct and 110 bridges. The guidance is more explicit about work than its summary suggested: strategic competency "includes core employability skills" (goal setting, time and resource management, planning and evaluating action); graduates are expected to communicate professionally across disciplines, cultures and borders; careers services should report employers' social and environmental performance; students should be supported to build enterprise skills towards ventures; and competencies can be evidenced on CVs, online profiles, digital badges and the HEAR. In Table 2, the direct outcomes cluster in the skills columns of anticipatory (precaution, risk, scenarios, backcasting, forecasting), strategic (planning tools, stakeholder strategy) and collaborative competency (group management, mediation, leadership, equitable collaboration).

**Suggestions.**
1. Read the anticipatory and strategic skills outcomes as professional competencies: risk evaluation, scenario planning, backcasting and forecasting are workplace methods and can be assessed as such (live briefs, consultancy projects).
2. Use the guidance's evidencing routes (badges, HEAR, CV, PDP) as the bridge to employability records: a competency met in an extracurricular activity is still a standard met.
3. Pair ESD's strategic and collaborative outcomes with the enterprise guidance's implementation and communication outcomes in one employability strand.


### GU4 Links to framework levels and assessment criteria
<!-- Counts of records linked, our reading (`inferred`). Framework statements are std:doc:qaa-fheq-2024-framework's; criteria are Bristol's (b:) and Cardiff Met's (c:) generic marking criteria. -->

| Framework statement | Records |
|---|---|
| qaa/fheq-2024/4.15.b7 | 7 |
| qaa/fheq-2024/4.15.b9.2 | 5 |
| qaa/fheq-2024/4.17.b5 | 4 |
| qaa/fheq-2024/4.15.b5 | 4 |
| qaa/fheq-2024/4.15.b8 | 3 |
| qaa/fheq-2024/4.15.b4 | 2 |
| qaa/fheq-2024/4.15.b3.1 | 2 |
| qaa/fheq-2024/4.17.b6 | 2 |
| qaa/fheq-2024/4.17.b8.1 | 2 |
| qaa/fheq-2024/4.15.b9.1 | 1 |
| qaa/fheq-2024/4.10.b1 | 1 |
| qaa/fheq-2024/4.12.b5 | 1 |
| qaa/fheq-2024/4.15.b6 | 1 |
| qaa/fheq-2024/4.10.b4 | 1 |
| qaa/fheq-2024/4.15.b9.3 | 1 |
| qaa/fheq-2024/4.12.b3 | 1 |
| qaa/fheq-2024/4.15.b2 | 1 |

| Assessment criterion | Records |
|---|---|
| Bristol: teamwork | 30 |
| Bristol: problem-solving | 20 |
| Bristol: decision-making | 19 |
| Bristol: critical-approach | 17 |
| Cardiff Met: analysis | 17 |
| Bristol: insight | 15 |
| Bristol: self-management | 14 |
| Cardiff Met: argument | 10 |
| Bristol: communication | 10 |
| Bristol: logical-argument-and-evaluation-of-perspectives | 9 |
| Cardiff Met: knowledge | 8 |
| Cardiff Met: presentation | 5 |
| Bristol: research | 4 |
| Bristol: use-of-evidence-and-sources | 4 |
| Cardiff Met: research | 3 |
| Bristol: specialist-skills-and-techniques | 2 |

**Reading.** Thirty-nine records sit close to an FHEQ statement, spread across Levels 4 to 7 because Table 2 spans them: knowledge outcomes near the CertHE's knowledge of concepts (4.10), analysis near the foundation degree's critical analysis (4.12), evaluation and evidence near the honours descriptor (4.15: evaluating arguments, managing own learning, the uncertainty of knowledge, decisions in complex contexts), and negotiation and leadership near the master's (4.17). Bristol's skills criteria take most criterion links (teamwork, problem-solving, decision-making, critical approach, insight, self-management), Cardiff Met's analysis and argument rows the knowledge and critical outcomes. Values and dispositions (empathy, wellbeing, intergenerational fairness) have no criterion in either grid.

**Suggestions for learning outcomes and assessment.**
1. **Writing outcomes.** The guidance's own rule (`design.1`): join subject knowledge and skills, a sustainability competency and the SDGs in each course or module outcome. Pattern: verb at the module's level + subject object + competency context + SDG. Example (ours): "Evaluate the trade-offs between two flood-defence options for a coastal town, weighing social, economic and environmental effects (systems thinking; SDGs 11 and 13)."
2. **Process over product.** The guidance asks for criteria that reward how a student reached a viable solution above the solution (`assessment.b5`). The enterprise guidance asks the same for process-driven assessment. A shared criterion row, "approach to the problem", banded from a described approach at the pass band to an evaluated, adapted approach at 70 and above, would serve both.
3. **For, as and of learning** (Figure 3, adapted from the National Forum): assessment *of* learning shows achievement (self-assessment against holistic criteria, synoptic tasks linking subject to the SDGs); assessment *as* learning builds self-regulation (self-review, peer review, portfolios recording competencies, co-created criteria); assessment *for* learning gives feedback on teaching (scaffolded tasks, real-life scenarios, dialogue). Map each module's assessment to one of the three and to the competency it develops.
4. **Values.** Assess attributes and values through reflection and position-taking, judged on how explicit and well reasoned the values are, never on which values are held.
5. **Synoptic assessment.** The guidance asks for policies that allow it; it is the natural home for systems and integrated problem-solving outcomes at L6 and L7.


### GU5 Academic practice pathways
<!-- Records per pathway (ACPRAC-DAT's thirteen, used loosely as categories), our reading. -->

| Pathway | Records | Families |
|---|---|---|
| reflective-practice | 32 | outcome 21, competency 9, narrative 1, assessment 1 |
| researching-and-research-methods | 9 | outcome 8, narrative 1 |
| work-based-and-experiential-learning | 49 | outcome 27, competency 5, narrative 4, environment 4, employers 3, students 2, assessment 2, aim 1, communities 1 |
| finding-and-using-sources | 6 | outcome 5, environment 1 |
| criticality | 89 | outcome 68, competency 17, narrative 3, aim 1 |
| academic-writing | 3 | outcome 3 |
| referencing | 0 | (none) |
| understanding-learning-assessment-and-feedback | 7 | design 2, students 2, assessment 2, outcome 1 |
| starting-progressing-and-succeeding | 15 | outcome 7, students 4, narrative 2, aim 1, assessment 1 |
| presenting | 10 | outcome 8, narrative 1, assessment 1 |
| revising-and-exams | 0 | (none) |
| ai-and-technology | 1 | assessment 1 |
| creativity | 26 | outcome 13, competency 8, aim 2, students 1, employers 1, assessment 1 |

**Reading.** Criticality dominates (89 records: systems, anticipatory, critical and normative thinking), then work-based and experiential learning (49: strategic and collaborative practice, live problems, communities), reflective practice (32: self-awareness, values, reflection on action), creativity (26: futures, visions, solutions) and starting, progressing and succeeding (15: adaptability, lifelong learning, careers). Finding and using sources, research methods and presenting appear through the critical and problem-solving outcomes (evidence, research methods from other disciplines, communicating complex issues). Referencing, revision and exams are absent; AI and technology appears once (authentic digital assessment), though the guidance's definition of 4IR technologies and its resources on new technologies would support it.

**Suggestions for pathways.**
1. **Criticality:** Table 2's critical thinking skills (`outcome.critical.s1` to `s6`) are a ready outcome set for the pathway's evidence and argument strand; systems and normative thinking add a strand the frameworks lack.
2. **Reflective practice:** self-awareness and normative outcomes give the pathway its "being" strand: values, emotions, wellbeing, own role (`outcome.selfaware.a1` to `a3`, `outcome.normative.a2`).
3. **Work-based and experiential learning:** collaborative and strategic skills (mediation, stakeholder strategy, planning tools, leadership) are the pathway's practice outcomes; the employers guidance (`employers.b1` to `b3`) says what students should be offered.
4. **Creativity:** anticipatory thinking (visions, backcasting, scenarios) pairs with the enterprise guidance's creativity theme.
5. **Finding and using sources:** `outcome.critical.k1`, `s3`, `s6` and `outcome.problem.s5` (evidence across disciplines; telling evidence from opinion) and `environment.b7` (diverse voices in reading lists).


### GU6 The benchmark web
<!-- label: practitioner; status: drafted; basis: primary for the paragraph and citation counts (a scan of the 54 benchmark texts held in stan); inferred for the reading -->
The scan shared with std:doc:qaa-enterprise-2018-guidance GU6, read for sustainability. Columns as there.

| Benchmark (held text) | Enterprise ¶ | ESD ¶ | Employability ¶ | Cites EEE 2018 | Cites ESD | Enterprise in standards | ESD in standards | Employability in standards |
|---|---|---|---|---|---|---|---|---|
| accounting-2025 | 11 | 26 | 5 | yes | yes | - | 4.5, 4.8 | 3.9 |
| agriculture-rural-environmental-sciences-animal-studies-consumer-science-forestry-food-horticulture-and-human-nutrition-2024 | 5 | 13 | 4 | yes | yes | 4.2 | 4.2 | 4.3 |
| anthropology-2024 | 3 | 4 | 1 | yes | no | - | - | - |
| archaeology-2022 | 2 | 6 | 0 | no | yes | - | 4.3, 4.4 | 4.4 |
| architectural-technology-2022 | 3 | 19 | 5 | yes | yes | - | 4.6, 4.8 | 4.5, 4.8 |
| architecture-2026 | 6 | 5 | 5 | no | yes | - | 4.7 | - |
| art-and-design-2026 | 6 | 11 | 5 | no | yes | 4.4 | 4.4 | 4.4 |
| biomedical-science-and-biomedical-sciences-2023 | 6 | 6 | 4 | yes | yes | - | 4.5 | - |
| biosciences-2023 | 5 | 11 | 5 | yes | yes | - | 4.5 | - |
| business-and-management-2023 | 9 | 11 | 4 | yes | yes | - | - | - |
| chemistry-2022 | 4 | 4 | 3 | yes | yes | - | - | - |
| classics-and-ancient-history-including-byzantine-studies-and-modern-greek-2022 | 2 | 5 | 1 | no | yes | - | - | - |
| communication-media-film-and-cultural-studies-2024 | 10 | 9 | 3 | yes | yes | 4.5, 4.8, 4.10 | 4.4, 4.7, 4.9 | - |
| computing-2022 | 3 | 6 | 3 | yes | yes | 4.6 | 4.6, 4.14 | 4.10 |
| counselling-and-psychotherapy-2022 | 8 | 5 | 4 | no | yes | 4.3, 4.7 | 4.3, 4.13 | 4.3, 4.10, 4.13 |
| creative-writing-2024 | 7 | 4 | 1 | yes | yes | 4.3, 4.4, 4.5 | 4.3, 4.4, 4.5, 4.7 | 4.3, 4.4 |
| criminology-2022 | 2 | 10 | 3 | no | yes | - | - | - |
| dance-drama-and-performance-2024 | 8 | 7 | 4 | yes | yes | 4.7 | 4.7, 4.8, 4.11, 4.14 | - |
| early-childhood-studies-2022 | 0 | 11 | 4 | no | yes | - | 4.4 | - |
| earth-sciences-environmental-sciences-and-environmental-studies-2022 | 4 | 10 | 6 | yes | yes | - | 4.6 | 4.6, 4.8 |
| economics-2023 | 3 | 7 | 2 | no | yes | - | - | - |
| education-studies-2025 | 5 | 9 | 3 | no | yes | - | - | - |
| engineering-2023 | 2 | 6 | 1 | yes | yes | - | 4.8, 4.11, 4.15 | - |
| english-2023 | 6 | 4 | 0 | yes | yes | 4.2 | 4.2 | 4.2 |
| finance-2025 | 5 | 13 | 4 | yes | yes | - | 4.4 | - |
| forensic-science-2022 | 4 | 2 | 1 | no | yes | - | - | - |
| geography-2022 | 1 | 7 | 1 | yes | yes | - | 4.5, 4.8 | - |
| health-studies-2024 | 7 | 12 | 8 | yes | yes | - | 4.1, 4.5 | 4.4, 4.5 |
| history-2022 | 2 | 6 | 2 | no | yes | - | 4.6 | - |
| history-of-art-architecture-and-design-2026 | 3 | 7 | 5 | no | no | - | 4.5 | - |
| housing-studies-2022 | 8 | 18 | 8 | yes | yes | 4.8 | 4.3, 4.8 | 4.8 |
| land-construction-real-estate-and-surveying-2024 | 4 | 11 | 6 | yes | yes | - | 4.3 | 4.3 |
| landscape-architecture-2024 | 1 | 3 | 3 | yes | yes | - | 4.4 | 4.4 |
| languages-cultures-and-societies-2023 | 5 | 3 | 1 | yes | yes | - | - | 4.11 |
| law-2023 | 4 | 5 | 3 | no | yes | - | 4.4 | 4.3 |
| librarianship-information-knowledge-records-and-archives-management-2025 | 6 | 6 | 4 | yes | no | 4.11 | 4.8 | 4.12 |
| linguistics-2023 | 4 | 6 | 1 | yes | yes | - | 4.5, 4.6 | 4.6 |
| masters-degrees-in-business-and-management-2023 | 9 | 12 | 5 | yes | yes | - | - | - |
| mathematics-statistics-and-operational-research-2023 | 10 | 6 | 5 | yes | yes | - | 4.9 | - |
| music-2025 | 4 | 5 | 3 | no | yes | - | - | - |
| optometry-2024 | 4 | 4 | 2 | yes | yes | - | 4.5 | - |
| osteopathy-2024 | 5 | 6 | 4 | no | yes | - | 6.4 | 6.8 |
| philosophy-2025 | 3 | 4 | 4 | no | no | - | - | 4.11 |
| physics-astronomy-and-astrophysics-2025 | 8 | 4 | 5 | yes | yes | 4.6 | - | - |
| policing-in-partnership-with-2022 | 0 | 3 | 2 | no | no | - | 4.4 | 4.4 |
| politics-and-international-relations-2023 | 3 | 4 | 1 | yes | yes | - | - | - |
| psychology-2023 | 6 | 5 | 3 | yes | yes | - | - | 4.10 |
| public-policy-and-public-administration-2025 | 6 | 6 | 3 | yes | yes | 4.7 | - | - |
| social-policy-2026 | 3 | 10 | 4 | yes | yes | - | 4.5, 4.7, 4.13 | 4.5, 4.7, 4.12 |
| social-work-2026 | 6 | 5 | 3 | no | yes | - | 4.11 | - |
| sociology-2026 | 3 | 3 | 3 | yes | yes | - | - | - |
| theology-and-religious-studies-2022 | 3 | 7 | 3 | yes | yes | - | 4.6 | - |
| town-and-country-planning-2024 | 6 | 14 | 4 | yes | yes | - | 4.7 | - |
| veterinary-nursing-2024 | 3 | 5 | 2 | yes | yes | - | 4.2 | - |


**Reading.** The link runs both ways. The guidance tells readers to use it beside the subject benchmark statements (S2); the benchmarks cite it back (49 of 54 by title, either edition), all 54 have sustainability paragraphs, and 37 carry sustainability words into their benchmark standards, against 12 for enterprise. In the standards we sampled, the theme mostly appears as one clause in a list of contexts a graduate weighs (social, economic, environmental, ethical); some subjects give it more than one standard (accounting, agriculture and related sciences, architectural technology, for example). With the full guidance held, each such benchmark standard can now be mapped to a Table 2 outcome, not just a competency name.

**Suggestion.** When a benchmark is ingested (S-02), tag its sustainability statements `theme:esd` and give each a `mapsTo` to the Table 2 outcome it most resembles (most often systems `k1`, `s5`, critical `s4` or normative `k3`). Then "what does sustainability mean at the threshold in my subject" is a query, not a reading exercise.

### GU7 Pedagogy handed to theory ingest
<!-- label: practitioner; status: drafted; basis: primary -->
Named here, not ingested:
- UNESCO's key competencies for sustainability and its learning objectives for the SDGs (UNESCO, 2017); ESD for 2030 (UNESCO, 2019);
- ways of thinking, practising and being; transformative learning; critical pedagogy;
- the whole-institution approach; ESD as curriculum framing (Figure 2's intersections with employability, enterprise, internationalisation, EDI and decolonisation, health and wellbeing, civic engagement, students as partners, research and knowledge exchange);
- assessment for, as and of learning for SD (Figure 3, after Ireland's National Forum for teaching and learning enhancement); synoptic assessment;
- Table 3's teaching practices: collaborative learning, enquiry-based learning, play-based learning (game-based learning, gamification, simulation), learning through storytelling, problem-based learning;
- triggers and authentic artefacts; the Iceberg Model for systems thinking; the campus as a living laboratory;
- Advance HE's Future Fit Framework (2012); Giangrande and others (2019) on ESD competencies in higher education; the ESDG guidelines (2014);
- UNECE's competences in ESD for educators (2012): a staff competence framework, a standards candidate for this profile (D3).

## Part B Terminology
<!-- label: both; status: drafted; basis: primary; paraphrased -->
```yaml
- { term: sustainable development, gloss: "An ongoing process, aspirational in aim, of tackling social, environmental and economic concerns together for a better world." }
- { term: education for sustainable development, gloss: "Creating curriculum structures, subject content and pedagogy that support and put into practice sustainable development." }
- { term: key competencies for sustainability, gloss: "UNESCO's eight competencies (S4 competency.*), grouped as ways of thinking, practising and being; the base of Table 2's outcomes." }
- { term: learning outcomes, gloss: "What a learner is expected to know, understand or be able to show after a period of learning." }
- { term: synoptic assessment, gloss: "Assessment of a learner's ability to connect different parts of a programme; suited to ESD." }
- { term: wicked problem, gloss: "A problem with no single definition or solution, whose parts are interdependent and keep changing." }
- { term: complex system, gloss: "A system of many interacting parts, such as the climate, an organism or a city." }
- { term: transformative learning, gloss: "Learning that changes how learners see themselves and the world, beyond gaining knowledge and skills." }
- { term: critical pedagogy, gloss: "Teaching that questions inequality and dominant power structures and assumptions." }
- { term: precautionary principle, gloss: "Caution, pause and review before innovations that may cause harm where scientific knowledge is lacking." }
- { term: 4IR technology, gloss: "Technologies linking the physical and digital, such as AI, robotics, 3D printing, VR and AR, cloud computing, big data and the Internet of Things." }
- { term: HEAR, gloss: "The Higher Education Achievement Report: an electronic record of a student's achievement during study." }
- { term: PSRBs, gloss: "Professional, statutory and regulatory bodies." }
- { term: SDGs, gloss: "The UN's 17 Sustainable Development Goals (2015), with 169 targets, for 2030." }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->
None: the guidance sets no process that providers must follow.

## Part D Sources

### D1 Held text
The PDF Abbott supplied (51 pages, sha256-bytes 9463b40b…), not held in UNI. Text by pdftotext page by page, except the pages holding ruled tables (Tables 1, 2 and 3), where each table is linearised row by row and cell by cell with pdfplumber so that each column's items stay together; the vertical labels set in mirror image ("Ways of thinking" and the like) are restored; bullet glyphs are written as bullets. Normalised with stan's normalise.js 1.0 (words equal). Figures 1 to 3 are not cut into statements; Figure 3 is described in our words (GU4) from the page.

### D2 Research log
- 2026-10-03 06:46 to 06:57, std: held and normalised; 207 statements in thirteen families; verb profile; crosswalk; benchmark scan shared with run 0056.

### D3 Wanted sources
- W-std-0009: UNESCO (2017), Education for Sustainable Development Goals: Learning Objectives: the competencies' source, with outcomes for each SDG.
- W-std-0011: UNECE (2012), Learning for the future: competences in ESD: staff competences, a standards document.
- W-std-0012: Advance HE (2019), Framework for Enterprise and Entrepreneurship Education, cited here beside QAA's enterprise guidance.
- W-std-0010: The 2014 QAA and HEA guidance, for the change record.

## Part E Gaps and questions
- E1 Currency unchecked.
- E2 Table 2 is indicative by the guidance's own words; its outcomes are standards statements of what a student can do, not thresholds.
- E3 Some outcomes repeat across competencies (conflict mediation in collaborative and self-awareness; power structures in systems and self-awareness; the range of cultures in self-awareness and normative): kept as separate records, as the guidance places them; a `sameAs` link is a P3 job.
- E4 The verb profile (GU2) and every map are ours.

---

## Change notes
- 0.2.1, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`; texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.2.0, 3 October 2026, 11:00: every statement record now carries the issuer's statement in full (`source`, taken from its span in the held text) beside our paraphrase and versions, for language analysis; private, never published (Abbott, 10:56 and 10:59; D-std-0014). No paraphrase changed.
- 0.1.1, 3 October 2026, 07:34: provenance lines added to Parts B and C; wanted sources in D3 given their W-std ids from the wanted-sources list (the ingest tool's G3 and G7 warnings; std N-0100). No statement changed.
- 0.1.0, 3 October 2026, 06:57: first build, run 0063 (std; Abbott, 06:46: "I do have the full esd. can you redo using this").

